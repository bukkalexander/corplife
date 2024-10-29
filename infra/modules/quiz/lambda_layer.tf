# Resources for Lambda Layer
# Processes dependencies

locals {
    python-libs = "${path.module}/python-libs"
}

# Null resource to run a local command to install dependencies
resource "null_resource" "install-dependencies" {
  # Ensure dependencies are installed in the right directory
  provisioner "local-exec" {
    command = <<EOT
      rm -rf ${local.python-libs} && mkdir -p ${local.python-libs} &&
      pip install -r ${path.module}/../../../api/requirements.txt -t ${local.python-libs}
    EOT
  }

  # Only run if requirements.txt changes
  triggers = {
    requirements_sha = filesha256("${path.module}/../../../api/requirements.txt")
  }
}

# Data source to zip the contents of the layer_path directory
data "archive_file" "lambda-layer-zip" {
  type        = "zip"
  source_dir  = local.python-libs
  output_path = "${path.module}/lambda/lambda_layer.zip"
  
  # Ensure zip is only created after dependencies are installed
  depends_on = [null_resource.install-dependencies]
}

# Lambda Layer resource using the generated zip file
resource "aws_lambda_layer_version" "python-deps-layer" {
  filename            = data.archive_file.lambda-layer-zip.output_path
  compatible_runtimes = ["python3.12"]
  layer_name          = "python_dependencies_layer"
  description         = "Lambda layer for Python 3.12 with dependencies from requirements.txt to run quiz app"

  # Set a unique version ID to trigger updates when requirements change
  source_code_hash = data.archive_file.lambda-layer-zip.output_base64sha256

  depends_on = [ null_resource.install-dependencies, data.archive_file.lambda-layer-zip ]
}
