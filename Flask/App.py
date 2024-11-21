from flask import Flask, request, send_file, jsonify
from service.RouteMapService import route_on_map
from service.CalorieGraph import calorie_graph
from util.Constant import map_file, calorie_graph_image

app = Flask(__name__)

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
    data = {"intake": 2000, "consumption": 2300}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
