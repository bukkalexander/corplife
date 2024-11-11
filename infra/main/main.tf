
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

# Url to access the frontend via s3
output "fronted_url" {
  value = module.quiz.fronted_url
}

# Lambda function name
output "lambda_function_name" {
  value = module.quiz.lambda_function_name
}
