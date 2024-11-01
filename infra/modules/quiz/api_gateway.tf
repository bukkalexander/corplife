# Create the API Gateway
resource "aws_apigatewayv2_api" "api-gateway" {
  name          = "${var.resource_prefix}api"
  protocol_type = "HTTP"
  description = <<EOF
  ${var.resource_prefix}api uses a lambda function as backend.
  The lambda function is responsible for properly handling the request,
  based on HTTP methods and routes.
  EOF
}

# Integration with Lambda
resource "aws_apigatewayv2_integration" "lambda-integration" {
  api_id           = aws_apigatewayv2_api.api-gateway.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.corplife-quiz-backend.invoke_arn
  integration_method = "POST"
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
