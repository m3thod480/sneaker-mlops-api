import boto3

from app.config import MODEL_PATH, S3_BUCKET_NAME, S3_MODEL_KEY


def download_model_if_needed():
    if MODEL_PATH.exists():
        return

    if not S3_BUCKET_NAME:
        raise RuntimeError("S3_BUCKET_NAME environment variable is not set")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    s3 = boto3.client("s3")
    s3.download_file(
        S3_BUCKET_NAME,
        S3_MODEL_KEY,
        str(MODEL_PATH)
    )