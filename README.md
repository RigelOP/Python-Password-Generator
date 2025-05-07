
# Password Generator Application

This is a simple and user-friendly Password Generator application built using Python and the PyQt5 library for the graphical user interface. It allows users to generate strong and secure passwords based on their specified criteria.

## Features

* **Password Length Selection:** Users can specify the desired length of the password (between 4 and 18 characters).
* **Parameter Selection:** Users can choose which character types to include in the generated password:
    * Lowercase Letters
    * Uppercase Letters
    * Digits
    * Symbols
* **Strong Password Generation:** The application uses the `random` and `string` modules in Python to generate unpredictable passwords based on the selected parameters. It ensures that if a character type is selected, at least one character of that type is included.
* **Copy to Clipboard:** A "Copy" button allows users to easily copy the generated password to their system clipboard for convenient use.
* **User-Friendly Interface:** The application provides a clean and intuitive graphical interface built with PyQt5.

## How to Run (If Running from Source)

1.  **Install Python:** Make sure you have Python 3 installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Install PyQt5:** Open your command prompt or terminal and run the following command to install the PyQt5 library:
    ```bash
    pip install PyQt5
    ```
3.  **Install pyperclip (for clipboard functionality):**
    ```bash
    pip install pyperclip
    ```
    On some Linux systems, you might need to install additional clipboard tools like `xclip` or `xsel`.
4.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `password_generator.py`).
5.  **Run the Application:** Navigate to the directory where you saved the file in your command prompt or terminal and run:
    ```bash
    python password_generator.py
    ```

## How to Use the Executable (If Running the `.exe` File)

1.  **Download the Executable:** If you have received or downloaded the standalone executable file (e.g., `password_generator.exe`), simply double-click the file to run the application.
2.  **Specify Password Length:** Enter the desired length of the password in the "Select Length" field. The length must be between 4 and 18.
3.  **Select Parameters:** Click the "Select ▼" button to open a dropdown list of character types. Select the checkboxes next to the character types you want to include in your password (Lowercase Letters, Uppercase Letters, Digits, Symbols). Click "Select ▲" to close the dropdown.
4.  **Generate Password:** Click the "Generate" button. A strong password based on your selections will be displayed in the "GENERATED PASSWORD" field.
5.  **Copy to Clipboard:** Click the "Copy" button to copy the generated password to your clipboard. The button text will briefly change to "Copied to Clipboard!".

## Dependencies

If running from source, you need to have the following Python libraries installed:

* **PyQt5:** For the graphical user interface.
* **pyperclip:** For clipboard functionality.
* **random:** For generating random characters.
* **string:** For accessing string constants (lowercase, uppercase, digits, punctuation).
* **sys:** For system-specific parameters and functions.

If running the standalone executable, these dependencies are bundled within the `.exe` file, and you do not need to install them separately.

## How to Convert to Executable (for Developers)

This application was likely converted to an executable using **PyInstaller**. To create your own executable from the `password_generator.py` script, you can follow these steps:

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Navigate to Script Directory:** Open your command prompt or terminal and go to the directory where `password_generator.py` is located.
3.  **Run PyInstaller:**
    ```bash
    pyinstaller --onefile password_generator.py
    ```
    The executable file will be created in the `dist` folder. You might need to experiment with additional PyInstaller options (like `--windowed` for GUI applications and `--hidden-import` for PyQt modules if they are not detected automatically).

## Author

This Password Generator application was created using Python and PyQt5.

## License

This project is open-source and available under a permissive license (e.g., MIT License). See the `LICENSE` file for more details (if a license file is included).
