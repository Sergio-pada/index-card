import json
import os
import random

def load_data(file_path):
    """Load data from a JSON file or create a new one if it doesn't exist."""
    # Check if the file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({}, file)  # Create an empty JSON file
    else:
        with open(file_path, 'r') as file:
            return json.load(file)  # Load existing data

def multi_line_input(prompt):
    """Collect multiple lines of input until 'END' is entered."""
    lines = []
    print(prompt)  # Display the prompt
    while True:
        line = input()  # Get user input
        if line == "END":
            break  # Exit on 'END'
        lines.append(line)  # Store the input lines
    return "\n".join(lines)  # Return all lines as a single string

def save_data(file_path, data):
    """Save the data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file)  # Write data to file

def create_entry(result_dict):
    """Create a new entry in the result dictionary."""
    key = multi_line_input("Enter Prompt (type 'END' when done):")  # Get prompt
    value = multi_line_input("Enter Answer (type 'END' when done):")  # Get answer
    result_dict[key] = value  # Add entry to dictionary

def edit_entry(result_dict):
    """Edit an existing entry in the result dictionary."""
    print("Type 'edit' if needed")
    for key, value in result_dict.items():
        print("----------------------------------- \n")
        print(key)  # Display the key
        input("")  # Wait for user input
        print(value)  # Display the value
        if input("") == "edit":  # Check if user wants to edit
            new_key = multi_line_input(f"Current Prompt: {key}\n")  # Get new prompt
            new_val = multi_line_input(f"Current Value: {value}\n")  # Get new answer
            del result_dict[key]  # Remove old entry
            result_dict[new_key] = new_val  # Add updated entry

def main():
    file_path = "index_card.json"
    result_dict = load_data(file_path)  # Load existing data

    command_type = input("What would you like to do (create or study): ").strip().lower()

    if command_type == 'create':
        create_entry(result_dict)  # Create a new entry
        save_data(file_path, result_dict)  # Save updated data
    elif command_type == "study":
        edit_entry(result_dict)  # Edit an existing entry
        save_data(file_path, result_dict)  # Save updated data

    print("-----------------------------------")

if __name__ == "__main__":
    main()  # Run the main function
