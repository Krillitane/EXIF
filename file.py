import folium
import piexif

def display_location_on_map(latitude, longitude):
    # Create a folium map centered at the specified location
    map_center = [latitude, longitude]
    my_map = folium.Map(location=map_center, zoom_start=12)

    # Add a marker at the specified location
    folium.Marker(location=map_center, popup="Image Location").add_to(my_map)

    # Display the map
    my_map.save("image_location.html")
    print("Map saved as 'image_location.html'. Open this file in a web browser to view the location.")

def extract_gps_info_from_image(image_path):
    # Load the EXIF data
    exif_data = piexif.load(image_path)

    # Check if GPS info is available
    if 'GPS' in exif_data:
        gps_info = exif_data['GPS']
        latitude = gps_info.get(piexif.GPSIFD.GPSLatitude)
        longitude = gps_info.get(piexif.GPSIFD.GPSLongitude)
        
        if latitude and longitude:
            # Convert GPS coordinates to degrees
            lat_degrees = latitude[0][0] / latitude[0][1]
            lat_minutes = latitude[1][0] / latitude[1][1]
            lat_seconds = latitude[2][0] / latitude[2][1]
            lat_direction = gps_info.get(piexif.GPSIFD.GPSLatitudeRef)

            lon_degrees = longitude[0][0] / longitude[0][1]
            lon_minutes = longitude[1][0] / longitude[1][1]
            lon_seconds = longitude[2][0] / longitude[2][1]
            lon_direction = gps_info.get(piexif.GPSIFD.GPSLongitudeRef)

            print(f"Latitude: {lat_degrees}° {lat_minutes}' {lat_seconds}\" {lat_direction}")
            print(f"Longitude: {lon_degrees}° {lon_minutes}' {lon_seconds}\" {lon_direction}")

            # Display the location on a map
            display_location_on_map(lat_degrees, lon_degrees)
        else:
            print("GPS coordinates not available in the image.")
    else:
        print("No GPS information found in the image.")

#let's see
image_path = "images/five.jpg"
extract_gps_info_from_image(image_path)
