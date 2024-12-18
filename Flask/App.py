from flask import Flask, request, send_file, jsonify
from service.RouteMapService import route_on_map
from service.CalorieGraph import calorie_graph
from service.CalorieCalculatorPulse import calculate_from_pulse_rate
from service.CalorieCalculatorGPS import calculate_from_GPS
from model.loadModel import get_intake
from util.Constant import map_file, calorie_graph_image
from tensorflow.keras.models import load_model
import joblib
import os

app = Flask(__name__)

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "model", "food_recognition_model.h5")
model = load_model(file_path)

file_path = os.path.join(current_dir, "model", "label_encoder.pkl")
loaded_encoder = joblib.load(file_path)
intake = 0

@app.route('/map', methods=['GET'])
def get_map():
    route_on_map()
    return send_file(map_file, mimetype='text/html')

@app.route('/calorie_graph', methods=['GET'])
def get_calorie_graph():
    calorie_graph()
    return send_file(calorie_graph_image, mimetype='image/png')

@app.route('/calorie_today', methods=['GET'])
def get_calorie_today():
    global intake
    consumption = calculate_from_pulse_rate()
    data = {"intake": intake, "consumption": consumption}
    return jsonify(data)

@app.route('/calorie_commute', methods=['GET'])
def get_calorie_commute():
    data = calculate_from_GPS()
    return jsonify(data)

@app.route('/upload_image', methods=['GET'])
def upload_image():
    global intake
    intake += get_intake(model,loaded_encoder)
    data = {"intake": intake, "consumption": 0}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
