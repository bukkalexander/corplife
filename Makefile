# Define BASE_DIR as the directory where this Makefile is located
BASE_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

# Define paths using BASE_DIR
# Path to python libraries for lambda layer
PIP_TARGET := $(BASE_DIR)/infra/modules/quiz/python-libs/
# Source directory for archiving lambda function
LAMBDA_FUNC_SOURCE := $(BASE_DIR)/api/
# Source directory for archiving the lambda layer
LAMBDA_LAYER_SOURCE := $(BASE_DIR)/infra/modules/quiz/python-libs/
# Base directory for where to drop the archives
ARCHIVES_DIR := $(BASE_DIR)/infra/modules/quiz/lambda/
# Path to requirements.txt
REQUIREMENTS_FILE := $(BASE_DIR)/api/requirements.txt

# Archive paths aliases
LAMBDA_FUNC_DEST := $(ARCHIVES_DIR)corplife_quiz.zip
LAMBDA_LAYER_DEST := $(ARCHIVES_DIR)python_deps.zip

# Default target to list all available targets
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install     - Install Python packages in target directory"
	@echo "  lambda    - Creates an archive from source code to upload to lambda"
	@echo "  lambda-layer    - Creates a lambda layer archive from python dependencies to upload to lambda layer"
	@echo "  rearchive   - Recreate both archives"
	@echo "  tofu - Run tofu apply command"
	@echo "  tofu-init - Run tofu init command"
	@echo "  tofu-plan - Run tofu plan command"
	@echo "  tofu-destroy - Run tofu destroy command"
	@echo "  clean       - Clean up build and output directories"

# Ensure directories are created if they don't exist
$(ARCHIVES_DIR) $(PIP_TARGET):
	mkdir -p $@

# Install Python packages to target directory
.PHONY: install
install: $(PIP_TARGET)
	pip install -r $(REQUIREMENTS_FILE) -t $(PIP_TARGET)

# Create first archive
.PHONY: lambda
lambda: $(ARCHIVES_DIR)
	zip -r $(LAMBDA_FUNC_DEST) $(LAMBDA_FUNC_SOURCE)

# Create second archive
.PHONY: lambda-layer
lambda-layer: $(ARCHIVES_DIR)
	zip -r $(LAMBDA_LAYER_DEST) $(LAMBDA_LAYER_SOURCE)

# Re-archive both targets after modifying source code or dependencies
.PHONY: rearchive
rearchive: lambda lambda-layer

# Terraform commands
.PHONY: tofu tofu-plan tofu-init tofu-destroy
tofu:
	cd $(BASE_DIR)/infra/main && tofu apply -auto-approve

tofu-destroy:
	cd $(BASE_DIR)/infra/main && tofu destroy -auto-approve

tofu-init:
	cd $(BASE_DIR)/infra/main && tofu init

tofu-plan:
	cd $(BASE_DIR)/infra/main && tofu plan

# Clean up all build and output directories
.PHONY: clean
clean:
	rm -rf $(PIP_TARGET) $(LAMBDA_FUNC_DEST) $(LAMBDA_LAYER_DEST)
