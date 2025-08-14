<b>Image Batch Resizer</b></br>

This script resizes all images in a specified folder to a fixed size and saves the resized images to a new folder.</br>

<b>How it works:</b></br>

1. **Folder Paths Setup:**
   - `input_folder`: Path to the folder containing the original images.
   - `output_folder`: Path where resized images will be saved.

2. **Target Size:**
   - The desired dimensions for all images are set to 800 pixels wide and 600 pixels tall (`target_size = (800, 600)`).

3. **Create Output Folder:**
   - If the output folder does not exist, it is created automatically.

4. **Supported Image Formats:**
   - The script processes images with extensions: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`.

5. **Processing Loop:**
   - The script iterates through each file in the input folder.
   - Checks if the file is an image based on its extension.
   - Opens the image, resizes it using high-quality resampling (`LANCZOS`), and saves the resized image to the output folder.
   - Prints a message for each successful resize or any errors encountered.

<b>Usage:</b>

- Update the `input_folder` and `output_folder` variables with your desired paths.
- Run the script to resize all images in the input folder to 800x600 pixels. This value can be modified as per requirement.

- ### Note:
Ensure you have the `Pillow` library installed:
pip install pillow

Tools used: Python, Pillow

