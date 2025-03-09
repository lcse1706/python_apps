import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Reshape, BatchNormalization, Dropout, LSTM

# Data Paths
train_csv = 'dataset/written_name_train_v2.csv'
val_csv = 'dataset/written_name_validation_v2.csv'
test_csv = 'dataset/written_name_test_v2.csv'
image_train = 'dataset/train_v2/train'
image_val = 'dataset/validation_v2/validation'
image_test = 'dataset/test_v2/test'

#  Reading the CSV files
train_df = pd.read_csv(train_csv)
val_df = pd.read_csv(val_csv)
test_df = pd.read_csv(test_csv)

# Deleting rows with missing values
train_df.dropna(subset=['IDENTITY'], inplace=True)
val_df.dropna(subset=['IDENTITY'], inplace=True)
test_df.dropna(subset=['IDENTITY'], inplace=True)

# Converting the 'IDENTITY' column to string
train_df['IDENTITY'] = train_df['IDENTITY'].astype(str)
val_df['IDENTITY'] = val_df['IDENTITY'].astype(str)
test_df['IDENTITY'] = test_df['IDENTITY'].astype(str)

# Function to preprocess the image
def preprocess_image(image_path, target_size=(128, 32)):
    try:
        img = Image.open(image_path).convert("L")  # scale to grayscale
        img = img.resize(target_size)  # Change the image size
        img_array = np.array(img) / 255.0 # Normalize the image
        return img_array
    except Exception as e:
        print(f"Nie można otworzyć {image_path}: {e}")
        return None  # Return None if error occurs

# Function to load and process the data
def load_and_process_data(df, image_folder):
    images = []
    labels = []
    
    for _, row in tqdm(df.iterrows(), total=len(df)):
        image_path = os.path.join(image_folder, row['FILENAME'])
        img_array = preprocess_image(image_path)
        
        if img_array is not None:
            images.append(img_array)
            labels.append(row['IDENTITY'])
    
    return np.array(images), labels

# Load and process the data
X_train, y_train = load_and_process_data(train_df, image_train)
X_val, y_val = load_and_process_data(val_df, image_val)
X_test, y_test = load_and_process_data(test_df, image_test)

# Check the shape of the data
print("Train:", X_train.shape, len(y_train))
print("Validation:", X_val.shape, len(y_val))
print("Test:", X_test.shape, len(y_test))

# Tokenization
tokenizer = Tokenizer(char_level=True)  # Character level tokenization
tokenizer.fit_on_texts(y_train)

# Convert text to sequences
y_train_seq = tokenizer.texts_to_sequences(y_train)
y_val_seq = tokenizer.texts_to_sequences(y_val)
y_test_seq = tokenizer.texts_to_sequences(y_test)

# Padding sequences
max_length = max(max(len(seq) for seq in y_train_seq), 
                 max(len(seq) for seq in y_val_seq),
                 max(len(seq) for seq in y_test_seq))

# Zero-padding a sequence to the same length
y_train_padded = pad_sequences(y_train_seq, maxlen=max_length, padding='post')
y_val_padded = pad_sequences(y_val_seq, maxlen=max_length, padding='post')
y_test_padded = pad_sequences(y_test_seq, maxlen=max_length, padding='post')

# Check the shape of the data
print("Shape X_train:", X_train.shape)
print("Shape y_train_padded:", y_train_padded.shape)

# Neural network model
model = Sequential([
    Reshape((32, 128, 1), input_shape=(32, 128)),  # Size of the image
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(max_length, activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_padded, validation_data=(X_val, y_val_padded), epochs=10, batch_size=64)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test_padded)
print(f"Test Accuracy: {test_acc:.4f}")
