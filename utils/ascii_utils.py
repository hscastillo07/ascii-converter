import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

ASCII_CHARS = "Ñ@#W$?!;:+=-,._  "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    try: 
        pixels = image.getdata()
    except:
        # Fallback for older Pillow versions or different image types
        w, h = image.size
        pixels = list(image.getdata())
        
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def image_to_ascii_string(image, new_width=100):
    """Orchestrates the conversion pipeline: Resize -> Grayscale -> ASCII"""
    return pixels_to_ascii(grayify(resize_image(image, new_width)))

def render_ascii_to_image(ascii_str, width_chars, height_chars, font_path="consola.ttf", font_size=10):
    """Render ASCII string to an image used for video frames."""
    try:
        font = PIL.ImageFont.truetype(font_path, font_size)
    except IOError:
        font = PIL.ImageFont.load_default()
    
    # Calculate character size
    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    
    # Add some padding or use literal metrics if getbbox is tight
    # Usually for monospace, we might want a bit of vertical spacing
    line_spacing = int(char_height * 0.2)
    full_line_height = char_height + line_spacing
    
    img_width = char_width * width_chars
    img_height = full_line_height * height_chars
    
    image = PIL.Image.new("RGB", (img_width, img_height), "black")
    draw = PIL.ImageDraw.Draw(image)
    
    lines = ascii_str.split('\n')
    for i, line in enumerate(lines):
        draw.text((0, i * full_line_height), line, fill="white", font=font)
        
    return image
