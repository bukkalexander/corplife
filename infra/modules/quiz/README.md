<!-- BEGIN_TF_DOCS -->
## Quiz Module

Terraform module to deploy infra for the corplife quiz app. Deploys a lambda, dynamodb table, api-gateway that are integrated together.

TODO: Add S3 bucket

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | 3.2.3 |
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.72.1 |
| <a name="provider_null"></a> [null](#provider\_null) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_apigatewayv2_api.api-gateway](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/apigatewayv2_api) | resource |
| [aws_apigatewayv2_integration.lambda-integration](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/apigatewayv2_integration) | resource |
| [aws_apigatewayv2_route.lambda-route](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/apigatewayv2_route) | resource |
| [aws_apigatewayv2_stage.api-stage](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/apigatewayv2_stage) | resource |
| [aws_dynamodb_table.corplife-quiz-questions](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |
| [aws_iam_role.lambda-exec-role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy.lambda_dynamodb_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy) | resource |
| [aws_iam_role_policy_attachment.basic-execution-attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_lambda_function.corplife-quiz-backend](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_lambda_permission.api-gateway-lambda-permission](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [archive_file.lambda-zip](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_function_memory_size"></a> [function\_memory\_size](#input\_function\_memory\_size) | The size in MB of memory allowed for the function | `number` | `128` | no |
| <a name="input_function_runtime"></a> [function\_runtime](#input\_function\_runtime) | The runtime to use for lambda function | `string` | `"python3.12"` | no |
| <a name="input_function_timeout"></a> [function\_timeout](#input\_function\_timeout) | The function exectuion time limit in seconds | `number` | `10` | no |
| <a name="input_region"></a> [region](#input\_region) | Default region to use for the resources. | `string` | `"eu-north-1"` | no |
| <a name="input_resource_prefix"></a> [resource\_prefix](#input\_resource\_prefix) | Optional prefix, that can be appended to all resource names for easy identification. | `string` | `"corplife-quiz-"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_api_gateway_invoke_url"></a> [api\_gateway\_invoke\_url](#output\_api\_gateway\_invoke\_url) | API Gateway invoke URL |
| <a name="output_lambda_function_name"></a> [lambda\_function\_name](#output\_lambda\_function\_name) | Lambda function name |
<!-- END_TF_DOCS -->