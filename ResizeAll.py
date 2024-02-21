import os
from PIL import Image

def resize_images_in_directory(root_dir, target_size=(5500, 5500)):
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

# Specify the root directory containing your subfolders
root_directory = "/Users/ianherdegen/Desktop/Designs"

# Call the function to resize images in all subfolders
resize_images_in_directory(root_directory)
