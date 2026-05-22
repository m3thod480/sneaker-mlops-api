from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

MODEL_PATH = MODEL_DIR / "sneaker_classifier.keras"
CLASS_INDICES_PATH = MODEL_DIR / "class_indices.json"
MODEL_INFO_PATH = MODEL_DIR / "model_info.json"

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_MODEL_KEY = os.getenv("S3_MODEL_KEY", "models/sneaker_classifier.keras")