import io

from fastapi import FastAPI, UploadFile, File
from PIL import Image

from app.predictor import predict


app = FastAPI(
    title="Sneaker Classifier API",
    description="API for classifying sneaker images using a TensorFlow/Keras model.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Sneaker Classifier API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/predict")
async def predict_sneaker(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    result = predict(image)

    return result