
import os
from PIL import Image

input_folder = "C:\\Users\\Administrator\\Desktop\\original_images"
output_folder = "C:\\Users\\Administrator\\Desktop\\resized_images"

#(width, height)
target_size = (800, 600)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

# Loop through files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:

                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

                resized_img.save(output_path)

                print(f"Resized and saved: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Batch resizing complete.")