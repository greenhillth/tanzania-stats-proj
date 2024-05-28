import pandas as pd
import csv
import json

with open('geodata/tz-wards-useful.json') as f:
    tanzania_wards_geojson = json.load(f)
    
data = pd.read_csv('geodata/wardData.csv')
ward_names = [feature['properties']['Ward_Name']
              for feature in tanzania_wards_geojson['features']]

# # Print the list of ward names
ward_names.sort()

# Write to a CSV file
with open('sorted_ward_names.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Ward_Name'])
    # Write each ward name in a new row
    for name in ward_names:
        writer.writerow([name])
