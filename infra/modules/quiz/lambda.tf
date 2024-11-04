# Upload the ZIP file to AWS Lambda
resource "aws_lambda_function" "corplife-quiz-backend" {
  function_name = "${var.resource_prefix}function"
  handler       = "lambda.handler"   # file_name.function_name
  runtime       = var.function_runtime

  role          = aws_iam_role.lambda-exec-role.arn

  filename      = "${path.module}/${var.lambda_function_archive_path}"
  source_code_hash = filebase64sha256("${path.module}/${var.lambda_function_archive_path}")
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

  depends_on = [ aws_lambda_layer_version.python-deps-layer, aws_iam_role.lambda-exec-role ]
}
