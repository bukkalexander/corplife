# IAM Role for Lambda with assume role policy
resource "aws_iam_role" "lambda-exec-role" {
  name = "${var.resource_prefix}lambda-exec-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

## Attach more policies to the iam role

# Attaching the basic execution policy for now
resource "aws_iam_role_policy_attachment" "basic-execution-attachment" {
  role       = aws_iam_role.lambda-exec-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Allow DynamoDB

resource "aws_iam_role_policy" "lambda_dynamodb_policy" {
  name   = "AllowCRUDDynamoDB"
  role   = aws_iam_role.lambda-exec-role.name

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "dynamodb:PutItem",
          "dynamodb:GetItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem" 
        ],
        "Resource": "${aws_dynamodb_table.corplife-quiz-questions.arn}"
      }
    ]
  })
}


# Allow API

# Permission for API Gateway to invoke the Lambda function
resource "aws_lambda_permission" "api-gateway-lambda-permission" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.corplife-quiz-backend.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.api-gateway.execution_arn}/*"
}



