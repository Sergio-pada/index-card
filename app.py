import json
import os
from PyQt5 import QtWidgets, QtCore
import random  

def load_data(file_path):
    """Load data from a JSON file or create a new one if it doesn't exist."""
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump({}, file) 
            return {}  # Return an empty dictionary if the file is created
        else:
            with open(file_path, 'r') as file:
                return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return {}  # Return an empty dictionary on error

def multi_line_input(prompt):
    """Collect multiple lines of input until 'END' is entered."""
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)# Return all lines as a single string

def save_data(file_path, data):
    """Save the data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        print(f"Error saving data: {e}")

def create_entry(result_dict):
    """Create a new entry in the result dictionary."""
    entry_dialog = QtWidgets.QDialog()  
    entry_dialog.setWindowTitle("Create Entry")
    entry_layout = QtWidgets.QVBoxLayout()

    prompt_text_edit = QtWidgets.QTextEdit()  
    prompt_text_edit.setPlaceholderText("Enter Prompt...")  
    entry_layout.addWidget(prompt_text_edit)  

    answer_text_edit = QtWidgets.QTextEdit()  
    answer_text_edit.setPlaceholderText("Enter Answer...")  
    entry_layout.addWidget(answer_text_edit)  

    submit_button = QtWidgets.QPushButton("Submit")  
    entry_layout.addWidget(submit_button)  

    entry_dialog.setLayout(entry_layout)  

    submit_button.clicked.connect(lambda: (
        result_dict.update({prompt_text_edit.toPlainText(): answer_text_edit.toPlainText()}),
        entry_dialog.accept()
    ))

    entry_dialog.exec_()  

def edit_entry(result_dict, key, value):
    """Edit an existing entry in the result dictionary."""
    edit_dialog = QtWidgets.QDialog()  
    edit_dialog.setWindowTitle("Edit Entry")
    edit_layout = QtWidgets.QVBoxLayout()

    prompt_text_edit = QtWidgets.QTextEdit()  
    prompt_text_edit.setPlainText(key)  
    edit_layout.addWidget(prompt_text_edit)  

    answer_text_edit = QtWidgets.QTextEdit()  
    answer_text_edit.setPlainText(value)  
    edit_layout.addWidget(answer_text_edit)  

    submit_button = QtWidgets.QPushButton("Submit")  
    edit_layout.addWidget(submit_button)  

    edit_dialog.setLayout(edit_layout)  

    def handle_submit():
        del result_dict[key]  
        result_dict[prompt_text_edit.toPlainText()] = answer_text_edit.toPlainText()  
        save_data("index_card.json", result_dict)
        edit_dialog.accept()  

    submit_button.clicked.connect(handle_submit)

    edit_dialog.exec_()  

def study_entries(result_dict):
    """Display entries as flashcards in random order."""
    items = list(result_dict.items())
    random.shuffle(items)  

    for key, value in items:
        flashcard_dialog = QtWidgets.QDialog()  
        flashcard_dialog.setWindowTitle("Flashcard")
        flashcard_layout = QtWidgets.QVBoxLayout()

        prompt_label = QtWidgets.QLabel(f"Prompt: {key}")  
        flashcard_layout.addWidget(prompt_label)

        show_answer_button = QtWidgets.QPushButton("Show Answer")
        flashcard_layout.addWidget(show_answer_button)

        answer_label = QtWidgets.QLabel(f"Answer: {value}")  
        answer_label.setVisible(False)  
        flashcard_layout.addWidget(answer_label)

        show_answer_button.clicked.connect(lambda: answer_label.setVisible(True))

        edit_button = QtWidgets.QPushButton("Edit")  
        flashcard_layout.addWidget(edit_button)

        close_button = QtWidgets.QPushButton("Close")  
        flashcard_layout.addWidget(close_button)

        edit_button.clicked.connect(lambda: (
            edit_entry(result_dict, key, value),  
            flashcard_dialog.accept()  
        ))

        close_button.clicked.connect(flashcard_dialog.accept)  

        flashcard_dialog.setLayout(flashcard_layout)  
        flashcard_dialog.exec_()  

def main():
    file_path = "index_card.json"
    result_dict = load_data(file_path)

    app = QtWidgets.QApplication([]) 
   

    app.setStyleSheet("""
        QWidget {
            background-color: #F4F1ED;  
            color: #5A5A5A;
        }
        QPushButton {
            background-color: #8C6A5D;  
            color: #FFFFFF;              
            border: none;                
            padding: 10px;               
            border-radius: 5px; 
        }
        QPushButton:hover {
            background-color: #7A5A4D;   /* Darker version of the button color */
        }
        QTextEdit {
            background-color: #D6C6B5;   
            color: #5A5A5A;               
            border: 1px solid #555;       
            border-radius: 5px;           
        }
        QLabel {
            color: #5A5A5A;               
        }
        QLabel.secondary {
            color: #AFAFAF;               
        }
    """)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Flashly")
    window.resize(400, 100)

    layout = QtWidgets.QVBoxLayout()

    title_label = QtWidgets.QLabel("Welcome to Flashly")
    title_label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(title_label)

    create_button = QtWidgets.QPushButton("Create Entry")
    create_button.clicked.connect(lambda: (create_entry(result_dict), save_data(file_path, result_dict)))
    layout.addWidget(create_button)

    study_button = QtWidgets.QPushButton("Study Entries")
    study_button.clicked.connect(lambda: (study_entries(result_dict), save_data(file_path, result_dict)))
    layout.addWidget(study_button)

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
