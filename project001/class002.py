import json

# Open the JSON file and load its content
with open('file/employees.json') as f:
    data = json.load(f)

    # Iterate through each item in the JSON data and print it
    for item in data:
        print(item)

