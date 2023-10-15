import os
from tkinter import filedialog, Tk  # Import filedialog
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFilter
from PIL import ImageChops
# To change transparency check line 37 and 52


def add_watermark(input_image_path, output_image_path):
    # Load the image
    # original_image = Image.open(input_image_path)
    
    if (Image.open(input_image_path)).mode != 'RGBA':
        original_image = (Image.open(input_image_path)).convert('RGBA')
    
    width, height = original_image.size

    # Create a drawing object
    # draw = ImageDraw.Draw(original_image)

    # Load the Tahoma font
    try:
        fnt = ImageFont.truetype("Pillow/Tests/fonts/tahoma.ttf", 72)
    except IOError:
        print("Tahoma font not found, using default font.")
        fnt = ImageFont.load_default()
        
    # Text to be drawn
    txt = "@NivellemStudio"
    
    x_offset = int(width * 0.72)
    y_offset = int(height * 0.92)
    watermark = Image.new('RGBA', original_image.size, (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    
    # Draw the white text with 50% opacity
    watermark_draw.text((x_offset, y_offset), txt, font=fnt, fill=(255, 255, 255, 32))  # <--- 128 for 50% opacity 
    
    # Create a separate image to draw the shadow
    shadow_layer = Image.new('RGBA', original_image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    
    # Shadow offsets
    shadow_offset_x = 2  # Horizontal offset for shadow
    shadow_offset_y = 2  # Vertical offset for shadow

    # Draw shadow
    shadow_draw.text(
        (x_offset + shadow_offset_x, y_offset + shadow_offset_y),
        text=txt,
        font=fnt,
        fill=(0, 0, 0, 64)  # <--- 128 for 50% opacity 
    )
    
    # Crop the area around the shadow text
    shadow_area = original_image.crop((x_offset, y_offset, x_offset + 600, y_offset + 100))  # Adjust these values as needed

    # Convert the cropped area to RGBA if it's not
    if shadow_area.mode != 'RGBA':
        shadow_area = shadow_area.convert('RGBA')

    # Apply Gaussian blur to the shadow
    blurred_shadow = shadow_layer.filter(ImageFilter.GaussianBlur(10))  # The parameter controls the blur radius

    # Create a blank image for text masking
    text_mask = Image.new('RGBA', original_image.size, (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_mask)

    # Draw text on the blank image
    text_draw.text((x_offset, y_offset), text=txt, font=fnt, fill=(255, 255, 255, 255))

    # Subtract the text from the blurred shadow layer
    subtracted_shadow = ImageChops.subtract(blurred_shadow, text_mask)

    # Composite the subtracted and blurred shadow onto the original image
    final_image = Image.alpha_composite(original_image, subtracted_shadow)
    final_image_with_white = Image.alpha_composite(final_image, watermark)
    # Save the final image
    final_image_with_white.save(output_image_path)


def main():
    # Initialize Tkinter
    root = Tk()
    root.withdraw()

    # Open folder dialog
    root = Tk()
    root.withdraw()  # Hide the Tk window
    folder_path = None
    while not folder_path:  # Loop until a folder is selected
        folder_path = filedialog.askdirectory(title="Select Folder")
        if not folder_path:
            print("No folder selected. Please choose a folder to proceed.")
    root.destroy()  # Destroy the Tk root window

    # Check if the user canceled the folder selection
    if not folder_path:
        print("No folder selected, exiting.")
        return

    # Create 'watermarked_output' subfolder if it doesn't exist
 
    output_folder = os.path.join(folder_path, 'Upscale_watermarked_output')
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
