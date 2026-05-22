output "bucket_name" {
  description = "Name of the S3 bucket for model artifacts"
  value       = aws_s3_bucket.model_artifacts.bucket
}