import os
from flask import Flask, render_template, request, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
try:
    model = load_model('model/handwriting_recognition.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Load the tokenizer (Ensure this is the same tokenizer used during training)
tokenizer = Tokenizer(char_level=True)
print("Tokenizer index_word:", tokenizer.index_word)

# Function to preprocess image
def preprocess_image(image_path, target_size=(128, 32)):
    img = Image.open(image_path).convert("L")  # Przekształcenie na odcienie szarości
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0  # Normalizacja
    return img_array

# Function to predict the handwritten text
def predict_text(image_path):
    img_array = preprocess_image(image_path)
    img_array = np.expand_dims(img_array, axis=0)  # Dodanie wymiaru partii
    img_array = np.expand_dims(img_array, axis=-1)  # Dodanie wymiaru kanału

    # Predykcja za pomocą modelu
    prediction = model.predict(img_array)
    predicted_sequence = np.argmax(prediction, axis=-1)

    # Debug: Sprawdzenie predykcji
    print("Predicted sequence:", predicted_sequence)

    # Przekształcanie przewidywanej sekwencji z powrotem na tekst
    decoded_text = ''.join([tokenizer.index_word.get(int(i), '') for i in np.atleast_1d(predicted_sequence[0])])

    # Debug: Sprawdzenie zdekodowanego tekstu
    print("Decoded text:", decoded_text)

    return decoded_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded."
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected."
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    predicted_text = predict_text(file_path)
    
    return render_template('result.html', text=predicted_text)

if __name__ == '__main__':
    app.run(debug=True)
