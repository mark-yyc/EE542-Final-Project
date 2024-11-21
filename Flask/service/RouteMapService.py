import folium
from datetime import datetime,timedelta
from util.Constant import location_data, map_file

def route_on_map():
    now = datetime.now()
    start_time = datetime(now.year, now.month, now.day)
    end_time = datetime(now.year, now.month, now.day) + timedelta(days=1)

    # Filter location data by timestamp
    route_points = [
        (data['latitude'], data['longitude'])
        for data in location_data
        if start_time <= datetime.fromisoformat(data['timestamp']) <= end_time
    ]

    # Create a map centered at the starting point
    map_route = folium.Map(location=route_points[0], zoom_start=14)

    # Draw the route
    folium.PolyLine(route_points, color="blue", weight=5, opacity=0.5).add_to(map_route)

    map_route.save(map_file)
    return map_file