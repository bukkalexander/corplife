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
