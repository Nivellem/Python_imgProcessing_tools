import os
from tkinter import filedialog, Tk
from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_image_path, output_image_path):
    # Load the image
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    # Create a drawing object
    draw = ImageDraw.Draw(original_image)

    # Load the Tahoma font
    try:
        font = ImageFont.truetype("tahoma.ttf", 30)
    except IOError:
        print("Tahoma font not found, using default font.")
        font = ImageFont.load_default()

    # Text to be drawn
    text = "@NivellemStudio"

    # Calculate width and height of the text to be drawn
    textwidth, textheight = draw.textsize(text, font=font)

    # Calculate X, Y position of the watermark
    x = width - textwidth - 10  # 10 pixels from the right edge
    y = height - textheight - 10  # 10 pixels from the bottom edge

    # Draw the shadow first
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(50, 50, 50, 128))

    # Draw text
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    # Save watermarked image
    original_image.save(output_image_path)


def main():
    # Initialize Tkinter
    root = Tk()
    root.withdraw()

    # Open folder dialog
    folder_path = filedialog.askdirectory(title="Select Folder")

    # Check if the user canceled the folder selection
    if not folder_path:
        print("No folder selected, exiting.")
        return

    # Create 'watermarked_output' subfolder if it doesn't exist
    output_folder = os.path.join(folder_path, 'watermarked_output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the selected folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(folder_path, filename)
            output_image_path = os.path.join(output_folder, filename)
            add_watermark(input_image_path, output_image_path)


if __name__ == "__main__":
    main()
