# API Gateway invoke URL
output "api_gateway_invoke_url" {
  value = aws_apigatewayv2_api.api-gateway.api_endpoint
}

# Lambda function name
output "lambda_function_name" {
  value = aws_lambda_function.corplife-quiz-backend.function_name
}
