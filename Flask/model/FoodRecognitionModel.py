import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
import joblib

# Step 1: Load the data
# Define the paths to the dataset
data_dir = 'food-101/images'

# Function to load and preprocess images
def load_images_from_folder(folder):
    images = []
    labels = []
    for label in os.listdir(folder):
        label_folder = os.path.join(folder, label)
        if os.path.isdir(label_folder):
            for filename in os.listdir(label_folder):
                if filename.endswith('.jpg'):
                    img_path = os.path.join(label_folder, filename)
                    img = load_img(img_path, target_size=(224, 224))  # Load and resize image
                    img = img_to_array(img)  # Convert image to array
                    img = img / 255.0  # Normalize pixel values
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

# Load images and labels
print("image loading...")
X, y = load_images_from_folder(data_dir)
print("image loaded")

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_categorical = to_categorical(y_encoded)

joblib.dump(label_encoder, 'label_encoder.pkl')  # Save as a .pkl file
print("LabelEncoder saved successfully!")

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# Step 3: Build the CNN model using VGG16
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(6, activation='softmax')  # Assuming 101 classes
])

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 4: Train the model
history = model.fit(X_train, y_train, epochs=2, batch_size=32, validation_split=0.2)

# Step 5: Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc}')

model.save('food_recognition_model.h5')

# Plot training history
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.show()

# Step 6: Calorie Estimation
# Create a mapping of food items to their calorie content
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

# Example usage
predicted_labels = label_encoder.inverse_transform(np.argmax(model.predict(X_test), axis=1))
for i in range(5):
    print(f'Predicted Food Item: {predicted_labels[i]}, Estimated Calories: {estimate_calories(predicted_labels[i])}')