import cv2
from PIL import Image
import numpy as np
import os
import time
from utils.ascii_utils import resize_image, grayify, pixels_to_ascii, render_ascii_to_image

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def process_video(path, new_width=100):
    cap = cv2.VideoCapture(path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0: fps = 30
    frame_delay = 1.0 / fps

    save_path = "ascii-video.mp4"
    video_writer = None
    
    frame_count = 0
    try:
        while True:
            start_time = time.time()
            
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert BGR (OpenCV) to RGB (PIL)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            
            resized = resize_image(pil_image, new_width)
            grayscale = grayify(resized)
            ascii_str = pixels_to_ascii(grayscale)
            
            img_width = resized.width
            img_height = resized.height
            ascii_str_len = len(ascii_str)
            ascii_img_str = ""
            
            # Construct ASCII lines
            for i in range(0, ascii_str_len, img_width):
                ascii_img_str += ascii_str[i:i+img_width] + "\n"
            
            # Render ASCII to Image
            ascii_frame_img = render_ascii_to_image(ascii_img_str, img_width, img_height)
            
            # Initialize Video Writer if not already done
            if video_writer is None:
                height, width = ascii_frame_img.size[1], ascii_frame_img.size[0]
                # 'mp4v' is a safe bet for .mp4 containers
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                video_writer = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
            
            # Convert PIL image back to OpenCV BGR format
            opencv_frame = cv2.cvtColor(np.array(ascii_frame_img), cv2.COLOR_RGB2BGR)
            video_writer.write(opencv_frame)
            
            clear_screen()
            print(ascii_img_str)
            
            frame_count += 1

            # Maintain simpler frame rate control
            elapsed = time.time() - start_time
            sleep_time = max(0, frame_delay - elapsed)
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        cap.release()
        if video_writer:
            video_writer.release()
        print(f"Video saved to {save_path}")
