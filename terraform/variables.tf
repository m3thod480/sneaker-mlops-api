variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "eu-west-1"
}

variable "bucket_name" {
  description = "S3 bucket name for ML model artifacts"
  type        = string
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "sneaker-mlops-api"
}

variable "ecr_image_url" {
  description = "ECR image URL"
  type        = string
  default     = "810498828675.dkr.ecr.eu-west-1.amazonaws.com/sneaker-mlops-api:latest"
}

variable "s3_model_key" {
  description = "S3 key where the model artifact is stored"
  type        = string
  default     = "models/sneaker_classifier.keras"
}