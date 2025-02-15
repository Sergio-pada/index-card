import json
import os
import random
import tkinter as tk  
from tkinter import simpledialog, messagebox

def load_data(file_path):
    """Load data from a JSON file or create a new one if it doesn't exist."""
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
    key = simpledialog.askstring("Input", "Enter Prompt:")
    if key is None: return
    value = simpledialog.askstring("Input", "Enter Answer:")
    if value is None: return
    result_dict[key] = value

def edit_entry(result_dict):
    """Edit an existing entry in the result dictionary."""
    for key, value in result_dict.items():
        if messagebox.askyesno("Edit Entry", f"Edit this entry?\n\nPrompt: {key}\nAnswer: {value}"):
            new_key = simpledialog.askstring("Input", f"Current Prompt: {key}")
            if new_key is None: return
            new_val = simpledialog.askstring("Input", f"Current Value: {value}")
            if new_val is None: return
            del result_dict[key]
            result_dict[new_key] = new_val

def main():
    file_path = "index_card.json"
    result_dict = load_data(file_path)

    root = tk.Tk()
    root.title("Entry Manager")

    def on_create():
        create_entry(result_dict)
        save_data(file_path, result_dict)

    def on_study():
        edit_entry(result_dict)
        save_data(file_path, result_dict)

    create_button = tk.Button(root, text="Create Entry", command=on_create)
    create_button.pack(pady=10)

    study_button = tk.Button(root, text="Study Entries", command=on_study)
    study_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
