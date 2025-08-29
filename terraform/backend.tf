terraform {

  # Comment this out when initialising resources.
  backend "s3" {
    region         = "us-east-2"
    bucket         = "aws-glue-terraform-state-kspr"
    key            = "lambda-terraform-ci-cd/tf-workspace/default.tfstate"
    dynamodb_table = "eks-terraform"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.11.0"
    }
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = {
      Environment = "${terraform.workspace}"
      Project     = "LAMBDA-TERRAFORM-CI-CD"
    }
  }
}

variable "region" {
  description = "AWS Region"
  default     = "us-east-2"
  type        = string
}