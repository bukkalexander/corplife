terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.72.1"
    }

    null = {
      source = "hashicorp/null"
      version = "3.2.3"
    }
  }
}

provider "aws" {
  # Configuration options
  region = var.region
}
