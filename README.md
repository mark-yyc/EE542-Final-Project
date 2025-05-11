# EE542-Final-Project: Calorie Track
Member: 

- Yicheng Yang: [Github](https://github.com/mark-yyc)
- Tianyu Peng: [Github](https://github.com/tianyu0923)
- Yang Jiao: [Github](https://github.com/Young884)

### File Structure
/Flask: Backend server developed using flask, including services like calorie intake and comsumption calculator.
/Android: Frontend developed using android studio, with funtions like calorie dashboard, commuting map and calorie calculate by food images.

### Setup
##### Dependency
```
pip install -r requirements.txt
```
##### Training Food Recgnition Model:
Before starting backend and frontend, train the model using dataset [Food-101](https://www.kaggle.com/datasets/dansbecker/food-101) to train Food Recgnition Model.
1. Go to directory /Flask/model, copy dataset into this directory.
2. Use command to start trainning model
```
    python ./FoodRecognitionModel.py
```
Then the model will be stored in food_recognition_model.h5(about 130 MB) and label encoder will be stored in label_encoder.pkl (1KB)
##### Backend:
Go to directory /Flask, and use command:
```
python App.py
```
Then the backend server will be started, it will load the Food Recgnition Model before listening request.

##### Frontend:
Go to directory /Android, open it in android studio or just gradle build to get the packet and install it on an android phone.

