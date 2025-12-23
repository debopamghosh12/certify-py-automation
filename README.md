# 🎓 Bulk Certificate Generator

A robust Python automation tool designed to generate hundreds of certificates instantly by placing names from a CSV file onto a certificate template. It handles text alignment, custom fonts, and organizes outputs into batches to prevent clutter.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas)
![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-green?style=for-the-badge)

## 🚀 Features

- **Automated Text Placement:** Reads names directly from a CSV file.
- **Batch Processing:** Automatically creates folders (e.g., `Batch_1`, `Batch_2`) containing 25 certificates each.
- **Smart Formatting:** Auto-converts images to RGB to prevent JPEG saving errors.
- **Customizable:** Easily adjust font style, size, color, and (X, Y) coordinates.
- **High-Res Support:** Works perfectly with high-quality print-ready templates.

## 📂 Project Structure

```text
├── main.py                 # The main script logic
├── requirements.txt        # List of dependencies
├── participants.csv        # Input file with names
├── template.jpg            # Certificate design template
└── arial.ttf               # Font file (Place your .ttf file here)
🛠️ Installation & Setup
Clone the Repository

Bash

git clone [https://github.com/debopamghosh12/bulk-certificate-generator.git](https://github.com/debopamghosh12/bulk-certificate-generator.git)
cd bulk-certificate-generator
Install Dependencies

Bash

pip install -r requirements.txt
Prepare Your Files

Template: Place your certificate image in the folder and rename it to template.jpg.

Font: Add your desired font (e.g., SquadaOne.ttf) to the folder.

Data: Create a participants.csv file with a single column header named "Name".

⚙️ Configuration
Open main.py in any code editor (VS Code, Notepad) and update the User Configuration section at the top:

Python

# 1. File Paths
TEMPLATE_PATH = "template.jpg"
CSV_PATH = "participants.csv"
FONT_PATH = "arial.ttf"  # Change to your font filename

# 2. Coordinates (Use MS Paint to find exact X, Y)
TEXT_X = 500   # Horizontal position
TEXT_Y = 400   # Vertical position
🏃‍♂️ Usage
Run the script using Python:

Bash

python main.py
Check the Generated_Certificates folder for your output! 🎉

🤝 Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or create a pull request.

📝 License
This project is open-source and available for personal and educational use.


---

### Ki korbi ekhon:
1.  GitHub e `README.md` file ta edit mode e open kor.
2.  Oporer box theke copy kore paste kore de.
3.  **Commit Changes** click kor.

Dekhbi ekdom professional lagche! Kono line break ba font issue hobe na. All set? 🚀