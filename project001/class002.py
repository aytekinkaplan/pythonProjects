import json

# Open the JSON file and load its content
with open('file/employees.json') as f:
    data = json.load(f)

    # Iterate through each item in the JSON data and print it
    for item in data:
        print(item)

    # Print the number of items in the JSON data
    print(len(data))

    # Print the first item in the JSON data
    print(data[0])

    # Print the last item in the JSON data
    print(data[-1])

    # Print the third item in the JSON data
    print(data[2])

    # Print the last three items in the JSON data
    print(data[-3:])

    # Print the first three items in the JSON data
    print(data[:3])
    # Close the file
    f.close()

