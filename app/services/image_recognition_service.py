from typing import List

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO





class ImageRecognitionService:
    def __init__(self):
        self._model = ResNet50(weights="imagenet")
        self._graph = tf.get_default_graph()

    def predict(self, image_url: str, top: int) -> List[str]:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content)).resize((224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        with self._graph.as_default():
            preds = self._model.predict(x)
        return [prediction[1] for prediction in decode_predictions(preds, top=top)[0]]
