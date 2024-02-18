import os
from PIL import Image

def resize_images_in_directory(root_dir, target_size):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        img_resized = img.resize(target_size, resample=Image.NEAREST)
                        img_resized.save(file_path)
                        print(f"Resized {file} to {target_size} pixels.")
                except Exception as e:
                    print(f"Error resizing {file}: {e}")

# Ask for the root directory containing the subfolders
root_directory = input("Enter the root directory containing the subfolders: ")

# Ask for the target size
target_width = int(input("Enter the target width (in pixels): "))
target_height = int(input("Enter the target height (in pixels): "))
target_size = (target_width, target_height)

# Call the function to resize images in all subfolders
resize_images_in_directory(root_directory, target_size)
