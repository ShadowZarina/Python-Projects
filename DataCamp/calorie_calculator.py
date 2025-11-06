import json  # Import the json module to work with JSON files

# Open the nutrition.json file in read mode and load its content into a dictionary
with open('nutrition.json', 'r') as json_file:
    nutrition_dict = json.load(json_file)  # Load the JSON content into a dictionary
    
# Display the first 3 items of the nutrition dictionary
list(nutrition_dict.items())[:3]
