terraform {
  backend "s3" {
    bucket         = "${var.resource_prefix}tf-state"
    key            = substr(var.resource_prefix, 0, length(var.resource_prefix) - 1)
    region         = var.region
    dynamodb_table = "${var.resource_prefix}state-lock"
  }
}
