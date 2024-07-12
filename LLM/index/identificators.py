
import uuid
# JSON data
# Save the JSON data to a local file
import json

# Replace 'path_to_file.json' with the path to your JSON file

def adduuid(file_path):
    # Read the JSON file and store its content in the 'data' variable
    with open(file_path, 'r') as file:
        data = json.load(file)



    # Add UUID to each entry
    for entry in data:
        entry["id"] = str(uuid.uuid4())

    # Save the JSON data with UUID to a local file
    file_path = 'data_with_uuid.json'
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    file_path
