import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

calorie_mapping = {
        'apple_pie': 230,
        'baby_back_ribs': 560,
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

def estimate_calories(food_item):
    return calorie_mapping.get(food_item, 'Unknown food item')

def get_intake(model,loaded_encoder):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "2432.jpg") 
    input_image = preprocess_image(image_path)
    predictions = model.predict(input_image)

    # Get the predicted class index
    predicted_class = np.argmax(predictions, axis=-1)
    decoded_labels = loaded_encoder.inverse_transform(predicted_class)
    print(decoded_labels[0])
    return estimate_calories(decoded_labels[0])
