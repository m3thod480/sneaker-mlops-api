import json
from pathlib import Path

import tensorflow as tf


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

MODEL_PATH = MODEL_DIR / "sneaker_classifier.keras"
CLASS_INDICES_PATH = MODEL_DIR / "class_indices.json"
MODEL_INFO_PATH = MODEL_DIR / "model_info.json"


def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


def load_class_indices():
    with open(CLASS_INDICES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def load_model_info():
    with open(MODEL_INFO_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


model = load_model()
class_indices = load_class_indices()
model_info = load_model_info()