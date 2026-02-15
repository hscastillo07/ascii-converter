import PIL.Image
import os
import time
from utils.ascii_utils import resize_image, grayify, pixels_to_ascii

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def process_gif(path, new_width=100):
   try:
       image = PIL.Image.open(path)
   except Exception as e:
       print(f"Invalid GIF path: {e}")
       return
   
   try:
       save_path = "ascii-gif.txt"
       with open(save_path, "w") as f:
           f.write("")
           
       frame_count = 0
       total_frames = getattr(image, 'n_frames', float('inf')) 
       
       while True:
            # Resize and convert current frame

            if image.mode != 'RGB':
                frame = image.convert('RGB')
            else:
                frame = image.copy()
                
            resized = resize_image(frame, new_width)
            grayscale = grayify(resized)
            ascii_str = pixels_to_ascii(grayscale)
            
            img_width = resized.width
            ascii_str_len = len(ascii_str)
            ascii_img = ""
            
            for i in range(0, ascii_str_len, img_width):
                ascii_img += ascii_str[i:i+img_width] + "\n"
            
            clear_screen()
            print(ascii_img)
            

            if frame_count < total_frames:
               with open(save_path, "a") as f:
                   f.write(f"--- FRAME {frame_count} ---\n")
                   f.write(ascii_img)
                   f.write("\n")
            
            time.sleep(0.1)
            frame_count += 1
            
            try:
                image.seek(image.tell() + 1)
            except EOFError:
                image.seek(0)

                if frame_count >= total_frames:
                     pass 
                
   except KeyboardInterrupt:
       print("\nStopped.")
