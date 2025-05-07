import sys
import random
import string
import pyperclip
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QGridLayout, QMessageBox, QListWidget,
                             QAbstractItemView, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def generate_strong_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generates a strong password based on the specified criteria."""
    if length < 4:
        return "Password length must be at least 4."
    if length > 18:
        return "Password length cannot exceed 18."

    available_characters = ""
    guaranteed_characters = ""
    if use_lowercase:
        available_characters += string.ascii_lowercase
        guaranteed_characters += random.choice(string.ascii_lowercase)
    if use_uppercase:
        available_characters += string.ascii_uppercase
        guaranteed_characters += random.choice(string.ascii_uppercase)
    if use_digits:
        available_characters += string.digits
        guaranteed_characters += random.choice(string.digits)
    if use_symbols:
        available_characters += string.punctuation
        guaranteed_characters += random.choice(string.punctuation)

    if not available_characters:
        return "Please select at least one parameter."

    # Ensure at least as many guaranteed characters as selected parameters (up to length)
    guaranteed_length = len(guaranteed_characters)
    if guaranteed_length > length:
        guaranteed_characters = guaranteed_characters[:length]
        guaranteed_length = length

    password = guaranteed_characters
    remaining_length = length - guaranteed_length
    if remaining_length > 0:
        password += ''.join(random.choice(available_characters) for _ in range(remaining_length))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

class PasswordGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 600, 400)
        self.copy_button_original_text = "Copy"
        self.grid_layout = QGridLayout()
        self.initUI()
        self.setLayout(self.grid_layout)

    def initUI(self):
        self.grid_layout.setHorizontalSpacing(15)
        self.grid_layout.setVerticalSpacing(8)

        # Title Label with Light Blue Background
        title_label = QLabel("Password Generator")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("background-color: lightblue; border-radius: 5px; padding: 5px;")
        self.grid_layout.addWidget(title_label, 0, 0, 1, 2)

        # Subtitle Label with Light Blue Background
        subtitle_label = QLabel("Create Bulletproof Passwords in Seconds!")
        subtitle_label.setFont(QFont("Arial", 10, QFont.Bold))
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("background-color: lightblue; border-radius: 5px; padding: 5px;")
        self.grid_layout.addWidget(subtitle_label, 1, 0, 1, 2)

        # Vertical Spacer after Subtitle
        subtitle_spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.grid_layout.addItem(subtitle_spacer, 2, 0, 1, 2)

        # Password Length Label with Rounded Background
        length_label = QLabel("Select Length")
        length_label.setFont(QFont("Arial", 12))
        length_label.setStyleSheet("background-color: lightgrey; border-radius: 5px; padding: 2px;")
        self.grid_layout.addWidget(length_label, 3, 0)

        # Password Length Input (Smaller Width)
        self.length_entry = QLineEdit("8")
        self.length_entry.setFont(QFont("Arial", 12))
        self.length_entry.setMaximumWidth(80)
        self.grid_layout.addWidget(self.length_entry, 4, 0, Qt.AlignLeft)

        # Choose Parameters Label with Rounded Background
        params_label = QLabel("Select Parameters")
        params_label.setFont(QFont("Arial", 12))
        params_label.setStyleSheet("background-color: lightgrey; border-radius: 5px; padding: 2px;")
        self.grid_layout.addWidget(params_label, 3, 1)

        # "Select" Button (Dropdown Trigger - Wider)
        self.select_button = QPushButton("Select ▼")
        self.select_button.setFont(QFont("Arial", 12))
        self.select_button.clicked.connect(self.toggle_params_dropdown)
        self.select_button.setMinimumWidth(150)
        self.grid_layout.addWidget(self.select_button, 4, 1, Qt.AlignLeft)

        # Parameters List Widget (Initially Hidden - Wider)
        self.params_list = QListWidget()
        self.params_list.addItems(["Lowercase Letters", "Uppercase Letters", "Digits", "Symbols"])
        self.params_list.setFont(QFont("Arial", 12))
        self.params_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.params_list.setVisible(False)
        self.params_list.setMinimumWidth(150)
        self.grid_layout.addWidget(self.params_list, 5, 1, 2, 1, Qt.AlignLeft)

        self.dropdown_visible = False

        # Generated Password Label with Rounded Background and Centered Text
        password_label = QLabel("GENERATED PASSWORD")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("background-color: lightgrey; border-radius: 5px; padding: 2px;")
        password_label.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(password_label, 7, 0, 1, 2)

        # Generated Password Input (Centered Text)
        self.password_entry = QLineEdit()
        self.password_entry.setReadOnly(True)
        self.password_entry.setFont(QFont("Arial", 12))
        self.password_entry.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.password_entry, 8, 0, 1, 2)

        # Vertical Spacer
        vertical_spacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.grid_layout.addItem(vertical_spacer, 9, 0, 1, 2)

        # Copy Button (Initially Hidden, Placed Above Generate, Light Grey BG)
        self.copy_button = QPushButton(self.copy_button_original_text)
        self.copy_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setVisible(False)
        self.copy_button.setStyleSheet("background-color: lightgrey; border-radius: 8px; padding: 8px;")
        self.grid_layout.addWidget(self.copy_button, 10, 0, 1, 2)

        # Generate Button
        self.generate_button = QPushButton("Generate")
        self.generate_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.generate_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 8px; padding: 8px;")
        self.generate_button.clicked.connect(self.generate_password)
        self.grid_layout.addWidget(self.generate_button, 11, 0, 1, 2)

    def toggle_params_dropdown(self):
        """Toggles the visibility of the parameters dropdown list."""
        self.dropdown_visible = not self.dropdown_visible
        self.params_list.setVisible(self.dropdown_visible)
        if self.dropdown_visible:
            self.select_button.setText("Select ▲")
        else:
            self.select_button.setText("Select ▼")

    def generate_password(self):
        """Generates a password based on the selected criteria."""
        try:
            length = int(self.length_entry.text())
            if length < 4 or length > 18:
                QMessageBox.warning(self, "Invalid Input", "Password length must be between 4 and 18.")
                return

            selected_params = [item.text() for item in self.params_list.selectedItems()]
            use_lowercase = "Lowercase Letters" in selected_params
            use_uppercase = "Uppercase Letters" in selected_params
            use_digits = "Digits" in selected_params
            use_symbols = "Symbols" in selected_params

            if not any([use_lowercase, use_uppercase, use_digits, use_symbols]):
                QMessageBox.warning(self, "No Parameters", "Please select at least one parameter.")
                return

            password = generate_strong_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
            if "Password length must be at least 4." in password or "Password length cannot exceed 18." in password or "Please select at least one parameter." in password:
                QMessageBox.warning(self, "Input Error", password)
                return
            self.password_entry.setText(password)
            self.copy_button.setVisible(True)
            self.copy_button.setText(self.copy_button_original_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for password length.")

    def copy_password(self):
        """Copies the generated password to the clipboard."""
        password = self.password_entry.text()
        if password:
            try:
                pyperclip.copy(password)
                self.copy_button.setText("Copied to Clipboard!")
            except pyperclip.PyperclipException:
                QMessageBox.warning(self, "Clipboard Error", "Could not copy to clipboard. Is pyperclip installed?")
        else:
            QMessageBox.warning(self, "No Password", "No password to copy!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PasswordGeneratorGUI()
    gui.show()
    sys.exit(app.exec_())