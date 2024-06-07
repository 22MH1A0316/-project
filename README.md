# -project
### **NAME** : **ZULU CHARLTON SHALLOCK**
### **GITHUB USERNAME** : **22MH1A0316**
### **EdX USERNAME**: **22MH1A0316**
### **CITY** : **KAKINADA**
### **COUNTRY** : **INDIA**
### **DATE** : **07-JUNE-2024**
### Project Title: CUSTOMIZED SHIRTIFICATE GENERATOR
### Video Demo:  <URL HERE>
### Description:
_____
The " Customized Shirtificate Generator" is a Python project designed to generate a customizable "shirtificate" PDF. This PDF includes an image of a t-shirt with the  customized user's name and a custom message. The project leverages the `fpdf2` library to create the PDF and allows users to specify their name and message, which will be embedded into the PDF at designated locations.

### Features:
- **Customizable Name and Message:** Users can input their name and a custom message, both of which will be displayed on the PDF.
- **PDF Generation:** The project creates a high-quality PDF with the specified details.
- **Configuration:** Easy configuration of font and title through a JSON configuration file.
- **Testing:** Comprehensive testing of core functions using `pytest`.

### Project Structure:

```
Shirtificate-Generator/
│
├── project.py
├── test_project.py
├── requirements.txt
├── config.json
├── shirtificate.png
└── README.md
```

### Files and Their Purpose:

- **project.py:** Contains the main function and the core functionalities for loading configurations, validating input, and creating the PDF.
- **test_project.py:** Contains the test functions to validate the correctness of the core functionalities using `pytest`.
- **requirements.txt:** Lists all the dependencies required for the project.
- **config.json:** Configuration file to specify settings like font and title for the PDF.
- **shirtificate.png:** Image of the t-shirt used in the PDF.
- **README.md:** Provides an overview of the project, setup instructions, and usage guidelines.

### Usage:

1. **Setup:**
   - Install the required dependencies:
     ```sh
     pip install -r requirements.txt
     ```

2. **Run the Main Program:**
   - Execute the following command to run the program:
     ```sh
     python project.py
     ```

3. **Testing:**
   - Run the tests to ensure everything is working correctly:
     ```sh
     pytest test_project.py
     ```

4. **Configuration:**
   - Modify the `config.json` file to change the font and title settings for the PDF.

### Example Workflow:

1. The user runs the `project.py` script.
2. The script prompts the user to enter their name and a custom message.
3. The script validates the inputs and creates a PDF with the user's name and message displayed on a t-shirt image.
4. The generated PDF is saved with the filename format `shirtificate_<name>.pdf`.
5. The user can then open and view their personalized "shirtificate".

This project ensures that the process of creating a customized certificate is simple, efficient, and thoroughly tested for reliability.
_______



