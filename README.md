# -project
  ### Project Title: CS50 Shirtificate Generator
    #### Video Demo:  <URL HERE>
    #### Description:
The CS50 Shirtificate Generator is a Python program that generates a personalized "shirtificate" PDF for users. The shirtificate features the user's name and the number of minutes they have been alive, presented in a stylized format. This project utilizes the `fpdf2` library for PDF creation and the `datetime` module to calculate the user's age in minutes.

#### Features:
- **User Input**: Prompts the user to enter their name and date of birth.
- **Age Calculation**: Calculates the user's age in minutes, considering leap years and the exact date.
- **Number to Words Conversion**: Converts the calculated age in minutes to its English word representation.
- **PDF Generation**: Creates a PDF with a customized shirt image and the user's name and age in words, centered and styled appropriately.

#### Project Structure:
- **project.py**: Contains the main function and other core functions for age calculation, number to words conversion, and PDF generation.
- **test_project.py**: Includes test functions to ensure the correctness of the core functions using pytest.
- **requirements.txt**: Lists the required Python libraries for the project.


#### Usage:
1. **Run the Program**: Execute `project.py` to generate a personalized shirtificate.
   ```
   python project.py
   ```
2. **Tests**: Run the test suite to ensure the core functions are working correctly.
   ```
   pytest test_project.py
   ```

#### Requirements:
- Python 3.x
- fpdf2 library


