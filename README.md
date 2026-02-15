# ASCII Media Converter

A Python-based tool that converts various media formats (Images, GIFs, and Videos) into ASCII art.

## Features

- **Images**: Converts static images (`.jpg`, `.png`, etc.) to ASCII text and saves to `ascii-image.txt`.
- **GIFs**: Plays animated GIFs (`.gif`) in the terminal as ASCII and saves frames to `ascii-gif.txt`.
- **Videos**: Converts video files (`.mp4`, `.avi`, etc.) into an ASCII-styled video file (`ascii-video.mp4`) and plays it in the terminal.

## Requirements

This project relies on the following Python packages:
- **Pillow (PIL)**: For image manipulation and processing.
- **OpenCV (cv2)**: For video capture and writing.
- **NumPy**: For efficient array operations during video processing.

## Installation

1. Clone the repository / Download the files.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the `main.py` script with the path to your media file. You can optionally specify the width of the ASCII output (default is 100 characters).

### Basic Usage
```bash
python main.py "path/to/your/file.jpg"
```

### Specifying Width
```bash
python main.py "path/to/your/video.mp4" 150
```

### Supported Formats
- **Images**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp`, `.tiff`
- **GIFs**: `.gif`
- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`

## Output

- **Images**: Saved to `ascii-image.txt`
- **GIFs**: Saved to `ascii-gif.txt` (frames separated by markers)
- **Videos**: Saved to `ascii-video.mp4`

## Project Structure

- `main.py`: Entry point for the application.
- `utils/`: Contains shared logic for ASCII conversion.
- `processors/`: Modules for handling specific media types.
