import os
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def analyze_and_move_png_files(folder_path):
    # Create squareArch folder if it doesn't exist
    square_arch_folder = os.path.join(folder_path, 'squareArch')
    if not os.path.exists(square_arch_folder):
        os.mkdir(square_arch_folder)

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a PNG image
        if filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)

            # Open the image and get its dimensions
            with Image.open(file_path) as img:
                width, height = img.size

            # Check if the image dimensions are within 10% tolerance
            larger_dimension = max(width, height)
            tolerance = 0.15 * larger_dimension
            if abs(width - height) <= tolerance:
                # Move the image to the squareArch folder
                new_path = os.path.join(square_arch_folder, filename)
                shutil.move(file_path, new_path)
                print(f"Moved {filename} to {square_arch_folder}")


if __name__ == "__main__":
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()

    # Open the folder dialog
    folder_path = filedialog.askdirectory(title="Select Folder")

    if folder_path:
        analyze_and_move_png_files(folder_path)
    else:
        print("No folder selected. Exiting.")
