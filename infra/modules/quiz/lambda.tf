## BACKEND ##
resource "aws_lambda_function" "corplife-quiz-backend" {
  function_name = "${var.resource_prefix}function"
  handler       = "lambda.handler"   # file_name.function_name
  runtime       = var.function_runtime

  role          = aws_iam_role.lambda-exec-role.arn

  filename      = "${path.module}/${var.lambda_function_archive_path}"
  source_code_hash = filesha256("${path.module}/${var.lambda_function_archive_path}")
  package_type = "Zip"

  # Attach the Lambda Layer containig all deps
  layers = [
    aws_lambda_layer_version.python-deps-layer.arn
  ]

  # Environment variables (if needed, add them here)
  environment {
    variables = {
      LOG_LEVEL = "DEBUG"
      DYNAMODB_TABLE_NAME_QUESTIONS = aws_dynamodb_table.corplife-quiz-questions.id
      DYNAMODB_TABLE_NAME_USERS = aws_dynamodb_table.corplife-quiz-users.id
    }
  }

  # Lambda basic settings
  memory_size      = var.function_memory_size
  timeout          = var.function_timeout

  depends_on = [ aws_lambda_layer_version.python-deps-layer, aws_iam_role.lambda-exec-role ]
}

## RECONCILIATION FUNCTION ##

resource "aws_lambda_function" "reconciliation_lambda" {
  function_name    = "${var.resource_prefix}ReconciliationFunction"
  role             = aws_iam_role.lambda-exec-role.arn
  handler          = "lambda.handler"
  runtime          = "python3.12"
  filename      = "${path.module}/${var.lambda_function_reconciler_archive_path}"
  source_code_hash = filesha256("${path.module}/${var.lambda_function_reconciler_archive_path}")
  package_type = "Zip"

  environment {
    variables = {
      LOG_LEVEL            = "DEBUG"
      USER_POOL_ID         = "${aws_cognito_user_pool.user_pool.id}"
      DYNAMODB_TABLE_NAME  = "${aws_dynamodb_table.corplife-quiz-users.id}"
    }
  }

  depends_on = [ aws_iam_role.lambda-exec-role, aws_cognito_user_pool.user_pool, aws_dynamodb_table.corplife-quiz-users ]

}


## Post Sign Up HOOK (Adding user to dynamodb) ##

# Lambda Function
resource "aws_lambda_function" "post_confirmation_trigger" {
  function_name = "${var.resource_prefix}PostConfirmationTrigger"
  role          = aws_iam_role.lambda-exec-role.arn
  handler       = "lambda.handler"
  runtime       = "python3.12"

  environment {
    variables = {
      DYNAMODB_TABLE_NAME = aws_dynamodb_table.corplife-quiz-users.id
    }
  }

  filename         =  "${path.module}/${var.lambda_function_signup_hook_archive_path}"
  source_code_hash = filesha256("${path.module}/${var.lambda_function_signup_hook_archive_path}")

  depends_on = [ aws_iam_role.lambda-exec-role, aws_dynamodb_table.corplife-quiz-users ]
}
