
# Lambda Layer resource using the generated zip file
resource "aws_lambda_layer_version" "python-deps-layer" {
  filename            = "${path.module}/${var.lambda_layer_archive_path}"
  compatible_runtimes = ["python3.12"]
  layer_name          = "python_dependencies_layer"
  description         = "Lambda layer for Python 3.12 with dependencies from requirements.txt to run quiz app"

  # Set a unique version ID to trigger updates when requirements change
  source_code_hash = filebase64sha256("${path.module}/${var.lambda_layer_archive_path}")

}
