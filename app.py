import json
import os
import random

def load_data(file_path):
    """Load data from a JSON file or create a new one if it doesn't exist."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({}, file)  # Create an empty JSON file
    else:
        with open(file_path, 'r') as file:
            return json.load(file)

def multi_line_input(prompt):
    """Collect multiple lines of input until 'END' is entered."""
    lines = []
    print(prompt)
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def save_data(file_path, data):
    """Save the data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file)

def create_entry(result_dict):
    """Create a new entry in the result dictionary."""
    key = multi_line_input("Enter Prompt (type 'END' when done):")
    value = multi_line_input("Enter Answer (type 'END' when done):")
    result_dict[key] = value

def edit_entry(result_dict):
    """Edit an existing entry in the result dictionary."""
    print("Type 'edit' if needed")
    for key, value in result_dict.items():
        print("----------------------------------- \n")
        print(key)
        input("")
        print(value)
        if input("") == "edit":
            new_key = multi_line_input(f"Current Prompt: {key}\n")
            new_val = multi_line_input(f"Current Value: {value}\n")
            del result_dict[key]
            result_dict[new_key] = new_val

def main():
    file_path = "index_card.json"
    result_dict = load_data(file_path)

    command_type = input("What would you like to do (create or study): ").strip().lower()

    if command_type == 'create':
        create_entry(result_dict)
        save_data(file_path, result_dict)
    elif command_type == "study":
        edit_entry(result_dict)
        save_data(file_path, result_dict)

    print("-----------------------------------")

if __name__ == "__main__":
    main()
