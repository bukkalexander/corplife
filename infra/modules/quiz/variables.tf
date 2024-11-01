variable "resource_prefix" {
  type        = string
  description = "Optional prefix, that can be appended to all resource names for easy identification."
  default     = "corplife-quiz-"
}

variable "region" {
  type        = string
  description = "Default region to use for the resources."
  default     = "eu-north-1"
}

variable "function_timeout" {
  type = number
  description = "The function exectuion time limit in seconds"
  default = 10
}

variable "function_memory_size" {
  type = number
  description = "The size in MB of memory allowed for the function"
  default = 128
  
}

variable "function_runtime" {
  type = string
  description = "The runtime to use for lambda function"
  default = "python3.12"
}

variable "lambda_layer_archive_path" {
  type = string
  description = "The path to the lambda layer archive relative to module"
  default = "lambda/python_deps.zip"
}

variable "lambda_function_archive_path" {
  type = string
  description = "The path to the lambda function archive relative to module"
  default = "lambda/corplife_quiz.zip"
}

variable "npm_output_dir" {
  type = string
  description = "The path to the lambda function archive relative to module"
  default = "../../../web/dist"
}