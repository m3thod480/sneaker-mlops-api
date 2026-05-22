variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "eu-west-1"
}

variable "bucket_name" {
  description = "S3 bucket name for ML model artifacts"
  type        = string
}