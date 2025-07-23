from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import os
import difflib

app = Flask(__name__, template_folder="../client/templates", static_folder="../client/static")
CORS(app)

# Load TrOCR model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Word list for correction (you can add more words as needed)
CORRECT_WORDS = ["JavaScript", "Python", "Handwriting", "Recognition", "AI", "Deep Learning", "Machine Learning"]

def correct_word(word):
    """Returns the closest matching word from the predefined list."""
    matches = difflib.get_close_matches(word, CORRECT_WORDS, n=1, cutoff=0.7)
    return matches[0] if matches else word  # Return the corrected word if found

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        image = Image.open(image_file).convert("RGB")

        # Perform OCR
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        extracted_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # Autocorrect words
        corrected_text = " ".join(correct_word(word) for word in extracted_text.split())

        return jsonify({"extracted_text": corrected_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

