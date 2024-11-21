# Create the API Gateway
resource "aws_apigatewayv2_api" "api-gateway" {
  name          = "${var.resource_prefix}api"
  protocol_type = "HTTP"
  description = <<EOF
  ${var.resource_prefix}api uses a lambda function as backend.
  The lambda function is responsible for properly handling the request,
  based on HTTP methods and routes.
  EOF

  cors_configuration {
    allow_origins     = ["http://${aws_s3_bucket_website_configuration.web_config.website_endpoint}"]
    allow_methods     = ["GET", "POST", "OPTIONS", "*"]
    allow_headers     = ["Authorization", "Content-Type"]
    allow_credentials = true
    max_age           = 0
  }
}

# Integration with Lambda
resource "aws_apigatewayv2_integration" "lambda-integration" {
  api_id           = aws_apigatewayv2_api.api-gateway.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.corplife-quiz-backend.invoke_arn
  integration_method = "POST"
}

# Authorizer with congnito
resource "aws_apigatewayv2_authorizer" "cognito-authorizer" {
  name           = "${var.resource_prefix}cognito-authorizer"
  api_id         = aws_apigatewayv2_api.api-gateway.id
  authorizer_type = "JWT"
  identity_sources = ["$request.header.Authorization"]

  jwt_configuration {
    audience = [aws_cognito_user_pool_client.user_pool_client.id]
    issuer   = "https://${aws_cognito_user_pool.user_pool.endpoint}"
  }
}

# Secured route for users
resource "aws_apigatewayv2_route" "user-secured-route" {
  api_id    = aws_apigatewayv2_api.api-gateway.id
  route_key = "ANY /user/{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.lambda-integration.id}"
  authorization_type = "JWT"
  authorizer_id = aws_apigatewayv2_authorizer.cognito-authorizer.id
}

# Allow OPTION type requests through without auth (Required for proper cors handling)
resource "aws_apigatewayv2_route" "user-options-route" {
  api_id    = aws_apigatewayv2_api.api-gateway.id
  route_key = "OPTIONS /user/{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.lambda-integration.id}"
}

# Route for all HTTP methods
resource "aws_apigatewayv2_route" "lambda-route" {
  api_id    = aws_apigatewayv2_api.api-gateway.id
  route_key = "ANY /{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.lambda-integration.id}"
}

# Deploy the API
resource "aws_apigatewayv2_stage" "api-stage" {
  api_id      = aws_apigatewayv2_api.api-gateway.id
  name        = "$default"
  auto_deploy = true
}
