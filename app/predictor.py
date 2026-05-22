import numpy as np
from PIL import Image

from app.model_loader import get_model, get_class_indices, get_model_info


def preprocess_image(image: Image.Image):
    model_info = get_model_info()
    input_size = model_info["input_size"]

    image = image.convert("RGB")
    image = image.resize((input_size[0], input_size[1]))

    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


def predict(image: Image.Image):
    model = get_model()
    class_indices = get_class_indices()

    processed_image = preprocess_image(image)

    predictions = model.predict(processed_image)[0]

    top_indices = predictions.argsort()[-3:][::-1]

    top_predictions = []

    for index in top_indices:
        top_predictions.append(
            {
                "class": class_indices[str(index)],
                "confidence": float(predictions[index])
            }
        )

    return {
        "predicted_class": top_predictions[0]["class"],
        "confidence": top_predictions[0]["confidence"],
        "top_predictions": top_predictions
    }