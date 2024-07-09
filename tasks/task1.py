import numpy as np

def main():
    # Constants
    earth_radius_km = 6371.0
    earth_circumference_km = 40000.0
    distance_traveled_km = 1000.0

    # Convert km traveled to degrees
    degrees_traveled = (distance_traveled_km / earth_circumference_km) * 360

    # Initial position
    initial_lat = 0.0
    initial_lon = 0.0

    # Move 1000 km East
    lon_after_east = initial_lon + degrees_traveled

    # Move 1000 km North (9 degrees)
    lat_after_north = degrees_traveled

    # Move 1000 km West at 9 degrees North
    lat_radians = np.radians(lat_after_north)
    local_circumference_km = earth_circumference_km * np.cos(lat_radians)
    degrees_west = (distance_traveled_km / local_circumference_km) * 360
    lon_after_west = lon_after_east - degrees_west

    # Move 1000 km South back to the equator
    lat_after_south = initial_lat

    # Calculate final longitude
    final_lon = lon_after_west

    # Calculate shortest surface distance on sphere using Haversine formula
    delta_lat = np.radians(lat_after_south - initial_lat)
    delta_lon = np.radians(final_lon - initial_lon)
    a = np.sin(delta_lat / 2)**2 + np.cos(np.radians(initial_lat)) * np.cos(np.radians(lat_after_south)) * np.sin(delta_lon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    surface_distance_km = earth_radius_km * c

    # Calculate straight line distance in 3D space (Euclidean distance)
    x1 = earth_radius_km * np.cos(np.radians(initial_lat)) * np.cos(np.radians(initial_lon))
    y1 = earth_radius_km * np.cos(np.radians(initial_lat)) * np.sin(np.radians(initial_lon))
    z1 = earth_radius_km * np.sin(np.radians(initial_lat))

    x2 = earth_radius_km * np.cos(np.radians(lat_after_south)) * np.cos(np.radians(final_lon))
    y2 = earth_radius_km * np.cos(np.radians(lat_after_south)) * np.sin(np.radians(final_lon))
    z2 = earth_radius_km * np.sin(np.radians(lat_after_south))

    straight_line_distance_km = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    print('=== Task 1 ===')
    print(f'surface distance (Haversine formula): {surface_distance_km} km, straight line distance (Euclidian): {straight_line_distance_km} km')
    print(" ")

if __name__ == "__main__":
    main()
