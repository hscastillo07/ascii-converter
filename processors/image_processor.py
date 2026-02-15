import PIL.Image
from utils.ascii_utils import resize_image, grayify, pixels_to_ascii
import os

def process_image(path, new_width=100):
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"Unable to open image file {path}. {e}")
        return

    resized_image = resize_image(image, new_width)
    greyscale_image = grayify(resized_image)
    ascii_str = pixels_to_ascii(greyscale_image)
    
    img_width = resized_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    print(ascii_img)
    
    try:
        output_path = "ascii-image.txt"
        with open(output_path, "w") as f:
            f.write(ascii_img)
        print(f"ASCII art saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
