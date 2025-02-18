import json
import os
from PyQt5 import QtWidgets, QtGui

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
    key, ok1 = QtWidgets.QInputDialog.getText(None, "Input", "Enter Prompt:")
    if not ok1: return
    value, ok2 = QtWidgets.QInputDialog.getText(None, "Input", "Enter Answer:")
    if not ok2: return
    result_dict[key] = value

def edit_entry(result_dict):
    """Edit an existing entry in the result dictionary."""
    for key, value in result_dict.items():
        reply = QtWidgets.QMessageBox.question(None, "Edit Entry", f"Edit this entry?\n\nPrompt: {key}\nAnswer: {value}",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            new_key, ok1 = QtWidgets.QInputDialog.getText(None, "Input", f"Current Prompt: {key}")
            if not ok1: return
            new_val, ok2 = QtWidgets.QInputDialog.getText(None, "Input", f"Current Value: {value}")
            if not ok2: return
            del result_dict[key]
            result_dict[new_key] = new_val

def main():
    file_path = "index_card.json"
    result_dict = load_data(file_path)

    app = QtWidgets.QApplication([])  # Create the application
    window = QtWidgets.QWidget()  # Create the main window
    window.setWindowTitle("Entry Manager")

    layout = QtWidgets.QVBoxLayout()  # Set layout for the window

    create_button = QtWidgets.QPushButton("Create Entry")
    create_button.clicked.connect(lambda: (create_entry(result_dict), save_data(file_path, result_dict)))
    layout.addWidget(create_button)

    study_button = QtWidgets.QPushButton("Study Entries")
    study_button.clicked.connect(lambda: (edit_entry(result_dict), save_data(file_path, result_dict)))
    layout.addWidget(study_button)

    window.setLayout(layout)  # Set the layout to the window
    window.show()  # Show the window
    app.exec_()  # Start the application event loop

if __name__ == "__main__":
    main()
