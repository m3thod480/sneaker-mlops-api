import json
from pathlib import Path

import tensorflow as tf

from app.config import MODEL_PATH, CLASS_INDICES_PATH, MODEL_INFO_PATH
from app.model_downloader import download_model_if_needed

_model = None
_class_indices = None
_model_info = None

def get_model():
    global _model

    if _model is None:
        download_model_if_needed()
        _model = tf.keras.models.load_model(MODEL_PATH)

    return _model


def get_class_indices():
    global _class_indices

    if _class_indices is None:
        with open(CLASS_INDICES_PATH, "r", encoding="utf-8") as file:
            _class_indices = json.load(file)

    return _class_indices


def get_model_info():
    global _model_info

    if _model_info is None:
        with open(MODEL_INFO_PATH, "r", encoding="utf-8") as file:
            _model_info = json.load(file)

    return _model_info