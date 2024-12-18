import math
import pandas as pd
import os

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the distance in meters between two lat/lon points using Haversine formula."""
    R = 6371000  
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calculate_calories(gps_data):
    """Estimate calories burned based on GPS data."""
    total_distance = 0
    
    for i in range(1, len(gps_data)):
        total_distance += haversine(
            gps_data[i-1]['latitude'], gps_data[i-1]['longitude'],
            gps_data[i]['latitude'], gps_data[i]['longitude']
        )
    
    
    kcal_per_meter = 0.04
    total_calories = total_distance * kcal_per_meter
    return total_distance, total_calories

def calculate_from_GPS():
    current_dir = os.path.dirname(__file__)

    parent_dir = os.path.dirname(current_dir)

    file_path = os.path.join(parent_dir, "data", "gps.txt")
    with open(file_path, 'r') as file:
        gps_data = [eval(line.strip()) for line in file]


    total_distance, total_calories = calculate_calories(gps_data)
    return {"distance":int(total_distance),"calorie":int(total_calories)}

print(calculate_from_GPS())