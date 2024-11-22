import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import joblib

model = load_model('food_recognition_model.h5')
loaded_encoder = joblib.load('label_encoder.pkl')

def preprocess_image(image_path, target_size=(224, 224)):
    # Load the image with the target size
    image = load_img(image_path, target_size=target_size)
    # Convert the image to a numpy array
    image_array = img_to_array(image)
    # Normalize the image to [0, 1]
    image_array = image_array / 255.0
    # Add a batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


image_path = '2432.jpg'  # Replace with the path to your image
input_image = preprocess_image(image_path)
predictions = model.predict(input_image)

# Get the predicted class index
predicted_class = np.argmax(predictions, axis=-1)
decoded_labels = loaded_encoder.inverse_transform(predicted_class)

calorie_mapping = {
    'apple_pie': 230,
    'baby_back_ribs': 300,
    'baklava': 180,
    'beef_carpaccio': 250,
    'beef_tartare': 200,
    'beet_salad': 100,
    'beignets': 220,
    'bibimbap': 400,
    'bread_pudding': 250,
    'breakfast_burrito': 350,
    # Add more food items and their calorie content
}

# Function to estimate calorie content based on the recognized food item
def estimate_calories(food_item):
    return calorie_mapping.get(food_item, 'Unknown food item')

print(f'Predicted Food Item: {decoded_labels[0]}, Estimated Calories: {estimate_calories(decoded_labels[0])}')