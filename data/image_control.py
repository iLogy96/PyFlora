import os
from PIL import Image
from pathlib import Path
import shutil

def copy_image(image_path):
    """
    Function used for making a copy of the selected image for the plant.
    If there is no image inside the 'images' folder with the same name as the selected image,
    it will make a copy of the image inside the 'images' folder.
    If the image is already in the 'images' folder or an identical image exists in the 'images' folder, return "OK".

    Parameters:
    image_path (str): The path to the selected image.

    Returns:
    str: "OK" if the image is already in the 'images' folder or copied successfully, otherwise the path of the new copied image.
    """
    image_path = Path(image_path)
    filename = image_path.name
    images_folder = Path("./images")

    if image_path.parent == images_folder:
        return "OK"

    if filename not in os.listdir(images_folder):
        destination_path = images_folder / filename
        try:
            shutil.copy(image_path, destination_path)
            print("Image copied")
            return "OK"
        except Exception as e:
            print(e)
            return "Error copying image"
    
    else:
        with open(image_path, "rb") as file:
            new_image = file.read()

        for file_name in images_folder.glob("*"):
            if file_name.is_file() and file_name.name == filename:
                with file_name.open("rb") as file:
                    existing_image = file.read()

                if new_image == existing_image:
                    print("Images are the same.")
                    return "OK"

        # If images are not the same, add prefix "new" to the filename
        prefix = "new"
        new_filename = filename
        while (images_folder / new_filename).is_file():
            new_filename = prefix + new_filename

        destination_path = images_folder / new_filename
        try:
            shutil.copy(image_path, destination_path)
            print("Image copied")
            return str(destination_path)
        except Exception as e:
            print(e)
            return "Error copying image"

def open_image(image_path):
    """
    Function used to return an Image object to a button for displaying the image on the button.

    Parameters:
    image_path (str): The path to the image.

    Returns:
    PIL.Image: The Image object.
    """
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(e)
        image = Image.open("./images/default.jpg")
        return image
