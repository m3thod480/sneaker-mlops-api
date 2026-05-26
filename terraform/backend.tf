terraform {
  backend "s3" {
    bucket = "sneaker-mlops-tfstate-810498828675"
    key    = "sneaker-mlops-api/terraform.tfstate"
    region = "eu-west-1"
  }
}