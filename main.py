import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 👇 USER CONFIGURATION (EDIT THIS SECTION)
# ==========================================

# 1. File Paths
TEMPLATE_PATH = "template.jpg"      # Put your dummy template image name here
CSV_PATH = "participants.csv"       # Put your dummy CSV file name here
FONT_PATH = "arial.ttf"             # Font file name (e.g., SquadaOne-Regular.ttf)

# 2. Output Settings
OUTPUT_FOLDER = "Generated_Certificates"

# 3. Text Settings
FONT_SIZE = 60
TEXT_COLOR = (0, 0, 0) # RGB Color (0,0,0 is Black, 255,255,255 is White)

# 4. Coordinates (Use MS Paint to find X, Y)
TEXT_X = 500   # Horizontal Position
TEXT_Y = 400   # Vertical Position

# ==========================================
# 🚀 MAIN SCRIPT STARTS HERE
# ==========================================

def generate_certificates():
    # Create Output Directory
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"📁 Created output folder: {OUTPUT_FOLDER}")

    # Load Data
    print("Reading CSV file...")
    try:
        df = pd.read_csv(CSV_PATH)
        # Clean header to remove accidental spaces
        df.columns = df.columns.str.strip()
        
        # Check for 'Name' column
        if 'Name' not in df.columns:
            print(f"❌ Error: Could not find 'Name' column in {CSV_PATH}")
            print(f"   Found columns: {df.columns}")
            return
            
        names = df['Name'].tolist()
        print(f"✅ Found {len(names)} names to process.")

    except FileNotFoundError:
        print(f"❌ Error: CSV file '{CSV_PATH}' not found!")
        return

    # Process Each Name
    print("Starting generation...")
    for index, name in enumerate(names):
        # Batch Logic (Optional: Organize 25 files per folder)
        batch_num = (index // 25) + 1
        batch_folder = os.path.join(OUTPUT_FOLDER, f"Batch_{batch_num}")
        if not os.path.exists(batch_folder):
            os.makedirs(batch_folder)

        try:
            # Open Image
            img = Image.open(TEMPLATE_PATH)
            # Convert to RGB to fix JPEG issues
            if img.mode == 'RGBA':
                img = img.convert('RGB')
                
            draw = ImageDraw.Draw(img)

            # Load Font
            try:
                font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
            except IOError:
                print(f"⚠ Warning: Font '{FONT_PATH}' not found. Using default.")
                font = ImageFont.load_default()

            # Prepare Name
            safe_name = str(name).strip()
            if not safe_name or safe_name == "nan":
                continue

            # Draw Text
            draw.text((TEXT_X, TEXT_Y), safe_name, fill=TEXT_COLOR, font=font)

            # Save File
            clean_filename = "".join([c if c.isalnum() else "_" for c in safe_name]) + ".jpg"
            save_path = os.path.join(batch_folder, clean_filename)
            
            img.save(save_path, "JPEG", quality=95)
            print(f"[{index+1}/{len(names)}] Saved: {clean_filename}")

        except FileNotFoundError:
            print(f"❌ Error: Template image '{TEMPLATE_PATH}' not found!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            break

    print("\n🎉 Process Completed!")
    print(f"📂 Check the '{OUTPUT_FOLDER}' directory.")

if __name__ == "__main__":
    generate_certificates()