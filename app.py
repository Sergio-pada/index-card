import json
import os


file_path = "index_card.json";

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")
    result_dict = {}
else:
    print("The file '{file_path}' already exists")

    with open('index_card.json', 'r') as fh:
        result_dict = json.load(fh)

command_type = input("What would you like to do(create or study): ")

if command_type == 'create': 
    key = input("Enter prompt: ")
    value = input("Enter answer: ")
    result_dict[key] = value
    with open(file_path, 'w') as file:
        json.dump(result_dict, file)
elif command_type == "study":
    for key, value in result_dict.items():
        print(key)
        input("")
        print(value)
        input("")
print("test")