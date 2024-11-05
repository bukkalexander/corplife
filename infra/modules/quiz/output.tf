# API Gateway invoke URL
output "api_gateway_invoke_url" {
  value = aws_apigatewayv2_api.api-gateway.api_endpoint

}

# Url to access the frontend via s3
output "fronted_url" {
  value = aws_s3_bucket_website_configuration.web_config.website_endpoint
}

# Lambda function name
output "lambda_function_name" {
  value = aws_lambda_function.corplife-quiz-backend.function_name
}

# Outputs for important information
output "user_pool_id" {
  value = aws_cognito_user_pool.user_pool.id
}

output "user_pool_client_id" {
  value = aws_cognito_user_pool_client.user_pool_client.id
}