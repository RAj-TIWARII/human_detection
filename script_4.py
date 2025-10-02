# Create the main.py file - the main entry point
main_content = """#!/usr/bin/env python3
\"\"\"
Real-Time Person Detection System
================================

A comprehensive person detection system using computer vision.
Supports both GUI and command-line interfaces.

Features:
- Real-time person detection using HOG or YOLO
- Live camera feed with bounding boxes
- Person counting and statistics
- Detection history tracking
- Professional GUI interface

Author: Generated for B.Tech Student
Date: October 2025
\"\"\"

import argparse
import sys
import cv2
from person_detection import PersonDetector, CameraManager
import config

def run_gui():
    \"\"\"Run the GUI version of the application\"\"\"
    try:
        from gui_app import main as gui_main
        print("🚀 Starting GUI application...")
        gui_main()
    except ImportError as e:
        print(f"❌ Error importing GUI components: {e}")
        print("💡 Try installing missing packages: pip install pillow tkinter")
        sys.exit(1)

def run_terminal():
    \"\"\"Run the terminal/command-line version\"\"\"
    print("🚀 Starting Terminal Person Detection...")
    print("📹 Initializing camera and detector...")
    
    # Initialize components
    detector = PersonDetector(method=config.DETECTION_METHOD)
    camera = CameraManager(config.CAMERA_INDEX)
    
    if not camera.start_camera():
        print("❌ Error: Cannot access camera!")
        return
    
    print("✅ Camera initialized successfully")
    print("🔍 Detection method:", config.DETECTION_METHOD)
    print("\\n🎯 Detection started! Press 'q' to quit, 's' to save screenshot")
    print("=" * 60)
    
    frame_count = 0
    
    try:
        while True:
            ret, frame = camera.read_frame()
            if not ret:
                print("❌ Error reading frame from camera")
                break
            
            # Perform detection
            annotated_frame, person_count = detector.detect_persons(frame)
            
            # Display frame
            cv2.imshow('Person Detection - Press q to quit, s to save', annotated_frame)
            
            # Print detection info every 30 frames (~1 second)
            frame_count += 1
            if frame_count % 30 == 0:
                stats = detector.get_current_stats()
                print(f"👥 Current: {stats['current_count']} | Avg: {stats['avg_count']} | Max: {stats['max_count']}")
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                # Save screenshot
                filename = f"detection_screenshot_{frame_count}.jpg"
                cv2.imwrite(filename, annotated_frame)
                print(f"💾 Screenshot saved: {filename}")
                
    except KeyboardInterrupt:
        print("\\n⏹️ Detection stopped by user")
    
    finally:
        # Cleanup
        camera.stop_camera()
        cv2.destroyAllWindows()
        print("✅ Cleanup completed")

def main():
    \"\"\"Main entry point\"\"\"
    parser = argparse.ArgumentParser(description='Real-Time Person Detection System')
    parser.add_argument('--mode', '-m', choices=['gui', 'terminal'], default='gui',
                       help='Run mode: gui (default) or terminal')
    parser.add_argument('--method', choices=['HOG', 'YOLO'], default=config.DETECTION_METHOD,
                       help='Detection method: HOG (default) or YOLO')
    parser.add_argument('--camera', '-c', type=int, default=config.CAMERA_INDEX,
                       help='Camera index (default: 0)')
    
    args = parser.parse_args()
    
    # Update config with command line arguments
    config.DETECTION_METHOD = args.method
    config.CAMERA_INDEX = args.camera
    
    print("🎥 Real-Time Person Detection System")
    print("=" * 40)
    print(f"🔍 Detection Method: {config.DETECTION_METHOD}")
    print(f"📹 Camera Index: {config.CAMERA_INDEX}")
    print(f"🖥️  Run Mode: {args.mode.upper()}")
    print("=" * 40)
    
    if args.mode == 'gui':
        run_gui()
    else:
        run_terminal()

if __name__ == "__main__":
    main()
"""

# Write main.py
with open('person_detector/main.py', 'w') as f:
    f.write(main_content.strip())

print("✓ main.py created")

# Create README.md with comprehensive documentation
readme_content = """# 🎥 Real-Time Person Detection System

A comprehensive Python application for real-time person detection using computer vision. This project uses your webcam to detect people in the camera feed, display bounding boxes around detected persons, show accurate timestamps, and provide detailed statistics.

## ✨ Features

- **Real-time person detection** using HOG (Histogram of Oriented Gradients) or YOLO
- **Live camera feed** with bounding boxes around detected persons
- **Accurate timestamp display** in the top-left corner
- **Person counting** with current, average, and maximum statistics
- **Detection history** tracking recent detections
- **Professional GUI interface** built with Tkinter
- **Terminal mode** for command-line usage
- **Multiple detection methods** (HOG and YOLO) with easy switching
- **Configurable settings** for different cameras and parameters

## 🚀 Quick Start

### 1. Install Requirements

```bash
# Navigate to the project directory
cd person_detector

# Install required packages
pip install -r requirements.txt
```

### 2. Run the Application

**GUI Mode (Recommended):**
```bash
python main.py
```

**Terminal Mode:**
```bash
python main.py --mode terminal
```

**With specific options:**
```bash
# Use YOLO detection method with camera 0
python main.py --method YOLO --camera 0

# Run in terminal mode with HOG detection
python main.py --mode terminal --method HOG
```

## 📦 Installation Guide

### Prerequisites
- Python 3.7 or higher
- Webcam or USB camera
- Windows, macOS, or Linux

### Step-by-Step Installation

1. **Clone or download this project:**
   ```bash
   # If you have git
   git clone <repository-url>
   cd person_detector
   
   # Or download and extract the ZIP file
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv person_detection_env
   
   # Activate virtual environment
   # Windows:
   person_detection_env\\Scripts\\activate
   
   # macOS/Linux:
   source person_detection_env/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **For YOLO support (optional but recommended for better accuracy):**
   ```bash
   pip install ultralytics
   ```

### Terminal Commands to Download Everything:

```bash
# Install OpenCV
pip install opencv-python==4.8.1.78

# Install image processing libraries
pip install numpy==1.24.3
pip install imutils==0.5.4
pip install Pillow==10.0.1

# Install YOLO (optional - for better detection)
pip install ultralytics

# Install other utilities
pip install python-dateutil
```

## 🎮 How to Use

### GUI Mode
1. Run `python main.py`
2. Click "▶️ Start Detection" to begin
3. The camera feed will appear with:
   - **Timestamp** in the top-left corner
   - **Green bounding boxes** around detected persons
   - **Person labels** (Person 1, Person 2, etc.)
   - **Detection statistics** on the right side
4. Use "⏹️ Stop Detection" to pause
5. Use "🔄 Switch Method" to toggle between HOG and YOLO

### Terminal Mode
1. Run `python main.py --mode terminal`
2. A window will open showing the camera feed
3. Press 'q' to quit
4. Press 's' to save a screenshot

### Detection Information Display

The system shows:
- **Current time** (top-left): Accurate system time
- **Detection status**: Current detection method
- **Person count**: Number of people detected
- **Bounding boxes**: Green rectangles around each person
- **Statistics**: Average and maximum person counts
- **Recent history**: Timeline of recent detections

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Detection method
DETECTION_METHOD = "HOG"  # or "YOLO"

# Camera settings
CAMERA_INDEX = 0  # Change if you have multiple cameras

# Display settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# Colors (BGR format)
BBOX_COLOR = (0, 255, 0)  # Green bounding boxes
TEXT_COLOR = (0, 0, 255)  # Red text
```

## 🔧 Troubleshooting

### Camera Issues
- **"Cannot access camera"**: Try different camera indices (0, 1, 2...)
- **Poor video quality**: Adjust `CAMERA_WIDTH` and `CAMERA_HEIGHT` in config.py
- **Camera permission denied**: Check system camera permissions

### Installation Issues
- **OpenCV import error**: `pip install opencv-python --upgrade`
- **Tkinter missing**: `sudo apt-get install python3-tk` (Linux)
- **YOLO not working**: `pip install ultralytics torch torchvision`

### Performance Issues
- **Slow detection**: Use HOG method instead of YOLO
- **High CPU usage**: Reduce camera resolution in config.py
- **GUI freezing**: Close other applications using the camera

## 📁 Project Structure

```
person_detector/
├── main.py                 # Main entry point
├── person_detection.py     # Core detection algorithms
├── gui_app.py             # GUI interface
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── README.md             # This documentation
```

## 🧠 How It Works

### Detection Methods

1. **HOG (Histogram of Oriented Gradients):**
   - Fast and lightweight
   - Good for real-time applications
   - Uses pre-trained SVM classifier
   - Lower accuracy but better performance

2. **YOLO (You Only Look Once):**
   - State-of-the-art accuracy
   - Neural network-based
   - Better at detecting partially occluded persons
   - Requires more computational resources

### Technical Details

- **Camera Management**: Uses OpenCV VideoCapture for camera access
- **Threading**: Separate threads for GUI updates and detection processing
- **Image Processing**: Real-time frame analysis with bounding box overlay
- **Statistics**: Moving average calculations for detection trends

## 🎯 Use Cases

- **Security Systems**: Monitor entrances and exits
- **Retail Analytics**: Count customers in stores  
- **Smart Home**: Occupancy detection
- **Learning Projects**: Computer vision education
- **Research**: Crowd analysis and social distancing

## 🔄 Detection Methods Comparison

| Feature | HOG | YOLO |
|---------|-----|------|
| Speed | Very Fast ⚡ | Moderate 🔄 |
| Accuracy | Good ✅ | Excellent 🎯 |
| Resource Usage | Low 💚 | Higher 🔶 |
| Setup Complexity | Simple | Moderate |

## 📊 Statistics Explained

- **Current Count**: People detected in the current frame
- **Average**: Moving average of recent detections
- **Maximum**: Highest count detected in the session
- **Recent History**: Timestamped log of recent detections

## 🛠️ Advanced Usage

### Custom Camera Settings
```python
# In config.py
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
```

### Multiple Camera Support
```bash
python main.py --camera 1  # Use second camera
```

### Save Detection Videos
The terminal mode automatically saves screenshots when you press 's'.

## 🤝 Contributing

This project was created as a learning exercise. Feel free to:
- Add new detection methods
- Improve the GUI design
- Add video recording features
- Optimize performance
- Add more statistics

## 📝 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Test with a simple camera application first
4. Try different camera indices
5. Check system camera permissions

---

**Enjoy your person detection system! 🎉**
"""

# Write README.md
with open('person_detector/README.md', 'w') as f:
    f.write(readme_content.strip())

print("✓ README.md created")

# Update config.py with proper cv2 import
config_updated = """# Configuration file for person detection project
import cv2

# Detection methods
DETECTION_METHOD = "HOG"  # Options: "HOG", "YOLO"

# Display settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Colors (BGR format)
BBOX_COLOR = (0, 255, 0)  # Green
TEXT_COLOR = (0, 0, 255)  # Red
TIME_COLOR = (255, 255, 255)  # White

# Detection parameters
HOG_WIN_STRIDE = (8, 8)
HOG_PADDING = (16, 16)
HOG_SCALE = 1.05

# Text settings
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
FONT_THICKNESS = 2

# Camera settings
CAMERA_INDEX = 0  # 0 for default camera
"""

# Update config.py with proper cv2 import
with open('person_detector/config.py', 'w') as f:
    f.write(config_updated.strip())

print("✓ Updated config.py with cv2 import")
print("\\n✅ Complete project created successfully!")