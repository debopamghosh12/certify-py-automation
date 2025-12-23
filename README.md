# 🎓 Bulk Certificate Generator

A Python automation script to generate hundreds of certificates instantly by placing names from a CSV file onto a certificate template. Perfect for events, hackathons, and workshops.

## 🚀 Features
- **Automated Text Placement:** Reads names from a CSV file.
- **Batch Processing:** Automatically organizes outputs into folders (25 per batch).
- **Format Handling:** Auto-converts images to RGB to prevent JPEG errors.
- **Customizable:** Easy to change font, size, color, and position.

## 🛠️ Setup

1. **Install Requirements**
   ```bash
   pip install -r requirements.txt
Prepare Files

Place your template image as template.jpg.

Create a participants.csv with a header named Name.

Add your .ttf font file to the folder.

Configure Open main.py and edit the configuration section:

Python

TEMPLATE_PATH = "template.jpg"
TEXT_X = 500  # Adjust based on your design
TEXT_Y = 400
Run

Bash

python main.py
📝 License
Open Source - Feel free to use and modify!