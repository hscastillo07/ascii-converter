import sys
import os
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path> [width]")
        print("Supported formats: Images (.jpg, .png, etc.), GIFs (.gif), Videos (.mp4, .avi, etc.)")
        return

    path = sys.argv[1].strip('"')
    
    # Check if file exists
    if not os.path.exists(path):
        print(f"Error: File not found: {path}")
        return

    width = 100
    if len(sys.argv) > 2:
        try:
            width = int(sys.argv[2])
        except ValueError:
            print("Warning: Invalid width provided. Using default width (100).")

    ext = os.path.splitext(path)[1].lower()
    
    # Image Formats
    if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff']:
        try:
            from processors.image_processor import process_image
            process_image(path, width)
        except ImportError as e:
            print(f"Error importing image processor: {e}")

    # GIF Format
    elif ext == '.gif':
        try:
            from processors.gif_processor import process_gif
            print("Playing GIF... Press Ctrl+C to stop.")
            time.sleep(1)
            process_gif(path, width)
        except ImportError as e:
             print(f"Error importing GIF processor: {e}")

    # Video Formats
    elif ext in ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv']:
        try:
            # Check for opencv
            import cv2
            from processors.video_processor import process_video
            print("Playing Video... Press Ctrl+C to stop.")
            time.sleep(1)
            process_video(path, width)
        except ImportError:
            print("Error: Video processing requires 'opencv-python'.")
            print("Please run: pip install opencv-python")

    else:
        print(f"Unsupported file format: {ext}")

if __name__ == "__main__":
    main()
