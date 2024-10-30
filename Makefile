# ---------------------------------------------------------------------------
# PATHS AND VARIABLES
# ---------------------------------------------------------------------------

# Define BASE_DIR as the directory where this Makefile is located
BASE_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

# Python dependency paths for Lambda layer
PIP_TARGET := $(BASE_DIR)/infra/modules/quiz/python-libs/
REQUIREMENTS_FILE := $(BASE_DIR)/api/requirements.txt

# Lambda function archive paths
LAMBDA_FUNC_SOURCE := $(BASE_DIR)/api/
LAMBDA_FUNC_DEST := $(BASE_DIR)/infra/modules/quiz/lambda/corplife_quiz.zip

# Lambda layer archive paths
LAMBDA_LAYER_SOURCE := $(BASE_DIR)/infra/modules/quiz/python-libs/
LAMBDA_LAYER_DEST := $(BASE_DIR)/infra/modules/quiz/lambda/python_deps.zip

# Base directory for archive outputs
ARCHIVES_DIR := $(BASE_DIR)/infra/modules/quiz/lambda/

# Tofu (Terraform equivalent) paths
TOFU_DIR := $(BASE_DIR)/infra/main
PLAN_FILE := $(TOFU_DIR)/tfplan


# ---------------------------------------------------------------------------
# CHECK REQUIRED TOOLS
# ---------------------------------------------------------------------------

.PHONY: check-tools
check-tools:
	@command -v zip >/dev/null 2>&1 || { \
	    echo >&2 "Error: zip is not installed. Running script to install zip"; \
	    bash $(BASE_DIR)/scripts/install_zip.sh || exit 1; \
	}
	@command -v tofu >/dev/null 2>&1 || { \
	    echo >&2 "Error: tofu is not installed. Running script to install tofu"; \
	    bash $(BASE_DIR)/scripts/install_opentofu.sh || exit 1; \
	}

# ---------------------------------------------------------------------------
# HELPER TARGETS
# ---------------------------------------------------------------------------

# Default target to list all available targets
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  prepare       - Full preparation of archives"
	@echo "  tofu-all      - Full Terraform workflow (init, plan, apply)"
	@echo "  install       - Install Python packages in target directory"
	@echo "  lambda        - Create an archive from source code to upload to lambda"
	@echo "  lambda-layer  - Create a lambda layer archive from python dependencies"
	@echo "  archive       - Create both lambda and lambda-layer archives"
	@echo "  tofu          - Run tofu apply command"
	@echo "  tofu-init     - Run tofu init command"
	@echo "  tofu-plan     - Run tofu plan command"
	@echo "  tofu-destroy  - Run tofu destroy command"
	@echo "  clean         - Clean up build and output directories"

# ---------------------------------------------------------------------------
# DIRECTORY CREATION
# ---------------------------------------------------------------------------

# Ensure directories are created if they don't exist
$(ARCHIVES_DIR) $(PIP_TARGET):
	mkdir -p $@

# ---------------------------------------------------------------------------
# PREPARATION AND ARCHIVE TARGETS
# ---------------------------------------------------------------------------

# Install Python packages to target directory
.PHONY: install
install: $(PIP_TARGET)
	pip install -r $(REQUIREMENTS_FILE) -t $(PIP_TARGET) --upgrade

# Create archive for lambda function code
.PHONY: lambda
lambda: check-tools $(ARCHIVES_DIR)
	zip -r $(LAMBDA_FUNC_DEST) $(LAMBDA_FUNC_SOURCE)

# Create archive for lambda layer dependencies
.PHONY: lambda-layer
lambda-layer: check-tools $(ARCHIVES_DIR)
	zip -r $(LAMBDA_LAYER_DEST) $(LAMBDA_LAYER_SOURCE)

# Re-archive both lambda and lambda-layer targets
.PHONY: archive
archive: lambda lambda-layer

# ---------------------------------------------------------------------------
# HIGH-LEVEL TARGETS FOR ARCHIVES
# ---------------------------------------------------------------------------

# Prepare everything needed for deployment (install dependencies and create archives)
.PHONY: prepare
prepare: install lambda lambda-layer
	@echo "Preparation complete: dependencies installed, archives created."

# ---------------------------------------------------------------------------
# TERRAFORM TARGETS WITH PLAN OUTPUT
# ---------------------------------------------------------------------------

.PHONY: tofu-init tofu-plan tofu-apply tofu-destroy tofu

# Initialize Terraform (OpenTofu) environment
tofu-init: check-tools
	cd $(TOFU_DIR) && tofu init

# Generate and save a plan file
tofu-plan: check-tools
	cd $(TOFU_DIR) && tofu plan -out=$(PLAN_FILE)

# Apply the saved plan file, if it exists
tofu-apply: check-tools
	@if [ -f $(PLAN_FILE) ]; then \
	    echo "Applying saved plan from $(PLAN_FILE)"; \
	    cd $(TOFU_DIR) && tofu apply $(PLAN_FILE); \
	else \
	    echo "Error: No plan file found. Run 'make tofu-plan' to create one."; \
	    exit 1; \
	fi

# Standard apply without a saved plan, as a fallback or for quick applies
tofu: check-tools
	cd $(TOFU_DIR) && tofu apply -auto-approve

# Destroy the infrastructure
tofu-destroy: check-tools
	cd $(TOFU_DIR) && tofu destroy -auto-approve

# ---------------------------------------------------------------------------
# HIGH-LEVEL TARGET FOR TERRAFORM
# ---------------------------------------------------------------------------

# Full Terraform workflow: init, plan, and apply
.PHONY: tofu-all
tofu-all: tofu-init tofu-plan tofu-apply
	@echo "Terraform workflow complete: init, plan, and apply done."

# ---------------------------------------------------------------------------
# CLEANUP
# ---------------------------------------------------------------------------

# Clean up all build and output directories
.PHONY: clean
clean:
	rm -rf $(PIP_TARGET) $(LAMBDA_FUNC_DEST) $(LAMBDA_LAYER_DEST) $(PLAN_FILE)
	@echo "Clean up complete."
