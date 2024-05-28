import json
import pandas as pd

# Load the GeoJSON file
with open('../geodata/tz-wards.json') as f:
    tanzania_wards_geojson = json.load(f)

# Load the CSV file
ward_data = pd.read_csv('../geodata/wardData.csv')

# Extract the list of ward names
ward_names = ward_data['Ward_Name'].tolist()

# Filter GeoJSON features
filtered_features = [feature for feature in tanzania_wards_geojson['features']
                     if feature['properties']['Ward_Name'] in ward_names]

# Create a new GeoJSON object with the filtered features
filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

# Save the filtered GeoJSON to a new file
with open('../geodata/tz-wards-useful.json', 'w') as f:
    json.dump(filtered_geojson, f)

print("Filtered GeoJSON has been saved to filtered_geojson_file.json")