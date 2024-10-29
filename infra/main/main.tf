
module "providers" {
    source = "../modules/providers"
}
module "quiz" {
  source = "../modules/quiz"
  region = var.region
  depends_on = [module.providers]
}

# API Gateway invoke URL
output "api_gateway_invoke_url" {
  value = module.quiz.api_gateway_invoke_url
}

# Lambda function name
output "lambda_function_name" {
  value = module.quiz.lambda_function_name
}
