from fpdf import FPDF
import json
import sys
from datetime import datetime

def load_config():
    """
    Load configuration from config.json file.
    """
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        return config
    except Exception as e:
        print(f"file does not exist {e}")
        sys.exit(1)

def validate_input(name, message):
    """
    Validate user input for name and message.
    """
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if not message.strip():
        raise ValueError("Message cannot be empty")
    return True

def create_pdf(name, message, config):
    """
    Create a PDF with the given name and message using the configuration settings.
    """
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Add the title
    pdf.set_font(config["font"], "B", 24)
    pdf.cell(0, 10, config["title"], 0, 1, "C")
    pdf.ln(20)

    # Add the shirt image
    pdf.image("shirtificate.png", x=(210-165)/2, y=60, w=165)

    # Add the user's name
    pdf.set_font(config["font"], "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=105, y=140, txt=name)

    # Add the user's custom message
    pdf.set_font(config["font"], "", 16)
    pdf.text(x=105, y=160, txt=message)

    # Save the PDF
    pdf.output(f"shirtificate_{name}.pdf")

def main():
    """
    Main function to execute the program.
    """
    config = load_config()

    name = input("Name: ")
    message = input("Enter your custom message: ")

    try:
        validate_input(name, message)
        create_pdf(name, message, config)
        print("Shirtificate created successfully!")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
