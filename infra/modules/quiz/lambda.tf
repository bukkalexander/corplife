# Lambda archive (ZIP file) creation from the source directory
data "archive_file" "lambda-zip" {
  type        = "zip"
  source_dir  = "${path.module}/../../../api"
  output_path = "${path.module}/lambda/${var.resource_prefix}src.zip"
}

# Upload the ZIP file to AWS Lambda
resource "aws_lambda_function" "corplife-quiz-backend" {
  function_name = "${var.resource_prefix}function"
  handler       = "main.lambda_handler"   # file_name.function_name
  runtime       = var.function_runtime

  role          = aws_iam_role.lambda-exec-role.arn

  filename      = data.archive_file.lambda-zip.output_path
  source_code_hash = data.archive_file.lambda-zip.output_base64sha256
  package_type = "Zip"

  # Attach the Lambda Layer containig all deps
  layers = [
    aws_lambda_layer_version.python-deps-layer.arn
  ]

  # Environment variables (if needed, add them here)
  environment {
    variables = {
      LOG_LEVEL = "INFO"
      DYNAMODB_TABLE_NAME = aws_dynamodb_table.corplife-quiz-questions.id
    }
  }

  # Lambda basic settings
  memory_size      = var.function_memory_size
  timeout          = var.function_timeout

  depends_on = [ aws_lambda_layer_version.python-deps-layer, data.archive_file.lambda-zip, aws_iam_role.lambda-exec-role ]
}
