import json
import os
import random


file_path = "index_card.json";

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")
    result_dict = {}
else:

    with open('index_card.json', 'r') as fh:
        result_dict = json.load(fh)

items = list(result_dict.items())
random.shuffle(items)
result_dict = dict(items)

command_type = input("What would you like to do(create or study): ")

if command_type == 'create': 
    
    lines = []
    print("Enter Prompt(type 'END' when done):")
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    key = "\n".join(lines)


    # value = input("Enter answer: ")
    lines = []
    print("Enter Prompt(type 'END' when done):")
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    value = "\n".join(lines)

    result_dict[key] = value
    with open(file_path, 'w') as file:
        json.dump(result_dict, file)




elif command_type == "study":
    
    for key, value in result_dict.items():
        print("----------------------------------- \n")
        print(key)
        input("")
        print(value)
        input("")
