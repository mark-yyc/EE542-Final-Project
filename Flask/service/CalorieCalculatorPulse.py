import json
import os

def calculate_cal(pulse_rate, duration_seconds, weight, height):
 
    met = 0.6309 * pulse_rate - 55.0969
    
    return (met * (weight / 2.2) * (duration_seconds / 3600))  

def calculate_from_pulse_rate():
    current_dir = os.path.dirname(__file__)

    parent_dir = os.path.dirname(current_dir)

    file_path = os.path.join(parent_dir, "data", "pulse_rate.txt")
    with open(file_path, 'r') as file:
        data = json.load(file)

    try:
        # weight = float(input("Enter your weight  kg: "))
        weight=50
        # height = float(input("Enter your height  cm: "))
        height=170
    except ValueError:
        print("Invalid input. ")
        exit()


    total_calories = 0
    before_date = None


    for entry in data:
        if entry["Pulse Rate"] != "--" and entry["Oxygen Level"] != "--":  
            pulse_rate = int(entry["Pulse Rate"])
            oxygen_level = int(entry["Oxygen Level"])
            time = entry["Time"]
        
       
        if before_date is not None:
            duration_seconds = time - before_date
            calories = calculate_cal(pulse_rate, duration_seconds, weight, height)
            total_calories += calories
            
            
            # print(f"Time: {time}, Pulse Rate: {pulse_rate}, Oxygen Level: {oxygen_level}, Calories Burned: {calories:.2f} kcal")
        
        before_date = time
    return int(-total_calories*1000)

print("Total Calorie burned: ", calculate_from_pulse_rate())