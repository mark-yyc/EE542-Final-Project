## Calorie Consumption
1. Daliy commuting
   Use GPS to track daily commuting route

2. Exercise in the gym
   Use Heart rate sensor to track heart rate. (heart rate, exercise intensity, Oxygen level)

## Calorie Calculation Equations

### 1. Calories per Minute for Men
\[
\text{Calories/min} = \frac{-55.0969 + (0.6309 \times \text{HR}) + (0.1988 \times \text{Weight (kg)}) + (0.2017 \times \text{Age})}{4.184}
\]

### 2. Calories per Minute for Women
\[
\text{Calories/min} = \frac{-20.4022 + (0.4472 \times \text{HR}) - (0.1263 \times \text{Weight (kg)}) + (0.074 \times \text{Age})}{4.184}
\]

### 3. Heart Rate Reserve (HRR)
\[
HRR = HR_{\text{max}} - HR_{\text{rest}}
\]

### 4. Heart Rate Intensity
\[
\text{Intensity} = \frac{HR - HR_{\text{rest}}}{HRR}
\]

### 5. Calories Burned Using HRR Method
\[
\text{Calories/min} = \text{Intensity} \times \text{VO₂ Max} \times 0.00193 \times \text{Weight (kg)}
\]

### 6. Total Calories Burned
\[
\text{Total Calories} = \text{Calories/min} \times \text{Duration (minutes)}
\]

### 7. MET-Based Total Calories Burned
\[
\text{Total Calories} = \text{MET} \times \text{Weight (kg)} \times \frac{\text{Duration (minutes)}}{60}
\]

### 8. Adjusted Calories with Heart Rate
\[
\text{Adjusted Calories} = \text{Total Calories} \times \frac{\text{Average HR during run}}{\text{Estimated Max HR (220 - Age)}}
\]

## Calorie Intake - Food
1. Food Recognition
   - Using RNN to identify the type of food.
   - Choose a pre-trained model: Many models like ResNet, Inception, and EfficientNet have been pre-trained on large datasets (e.g., ImageNet) and can be fine-tuned for food recognition.
   - Fine-tuning for food datasets: Models fine-tuned on food-specific datasets like Food-101 (101 categories of food) or UECFOOD-256 (256 Japanese food categories) can be very effective.
2. Food size calculation
   - Identify the Plate and Food Regions:
      - Object Detection Models: Use an object detection model like YOLO, Faster R-CNN, or Detectron2 to identify and segment the plate and the food within the image.
      - Instance Segmentation: use instance segmentation models (like Mask R-CNN) to segment both the plate and the food.
   - Estimate the Plate's Diameter:
     Utiling pixels in the photo
   - Calculate the Size of the Food
