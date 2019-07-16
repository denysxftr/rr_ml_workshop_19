from flask import Flask, jsonify, request

from app.services.image_recognition_service import ImageRecognitionService

image_recognition_service = ImageRecognitionService()

app = Flask(__name__)


@app.route("/api/v1/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/v1/predict")
def predict():
    image_url = request.args.get("url")
    top_predictions = int(request.args.get("top"))
    result = image_recognition_service.predict(image_url, top_predictions)
    return jsonify({"predictions": result})


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
