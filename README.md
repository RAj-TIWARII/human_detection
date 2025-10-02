# 🎥 Real-Time Person Detection System

A professional computer vision application for detecting and counting persons in real-time using webcam feed.

![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![OpenCV](https://img.shields.io/badge/opencv-4.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 📋 Table of Contents
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Project Structure](#-project-structure)

## ✨ Features

### Core Functionality
- ✅ **Real-time Detection:** Detect persons instantly from webcam feed
- ✅ **Multiple Methods:** Support for HOG and YOLO detection algorithms
- ✅ **Person Counting:** Accurate counting of detected persons
- ✅ **Statistics Dashboard:** Real-time analytics and metrics
- ✅ **Screenshot Capture:** Save detection results as images
- ✅ **History Tracking:** Monitor detection trends over time

### User Interface
- 🖥️ **Professional GUI:** Beautiful Tkinter-based interface
- 💻 **Terminal Mode:** Lightweight command-line option
- 📊 **Live Statistics:** Current, average, and maximum counts
- 🎨 **Visual Feedback:** Bounding boxes and labels
- ⚙️ **Easy Configuration:** Simple settings interface

## 🎯 Screenshots

### GUI Mode
```
┌─────────────────────────────────────────────────┐
│  🎥 Real-Time Person Detection System          │
├─────────────────────┬──────────────────────────┤
│                     │  Controls                 │
│   Camera Feed       │  ┌────────────────────┐  │
│   [Video Display]   │  │ Detection: HOG     │  │
│                     │  │ Camera: 0          │  │
│                     │  └────────────────────┘  │
│                     │  [▶ Start Detection]     │
│                     │  [📸 Screenshot]          │
│                     │                          │
│                     │  Statistics              │
│                     │  Current: 2 persons      │
│                     │  Average: 1.5            │
│                     │  Max: 3                  │
└─────────────────────┴──────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- **Python 3.11 or 3.12** (NOT 3.13!)
- Webcam/Camera
- Windows/Mac/Linux OS

### Quick Install (Windows)

1. **Download Python 3.11 or 3.12**
   - Go to https://python.org/downloads
   - ⚠️ DO NOT use Python 3.13!

2. **Download Project Files**
   - Save all files in a folder (e.g., `Room_security`)

3. **Run Installation Script**
   ```bash
   # Double-click or run:
   install.bat
   ```

4. **Launch Application**
   ```bash
   # Double-click or run:
   run.bat
   ```

### Manual Install

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install opencv-python numpy pillow

# 4. Run application
python main.py
```

## 📖 Usage

### GUI Mode (Recommended)
```bash
# Default - Opens GUI window
python main.py

# Or double-click
run.bat
```

**GUI Controls:**
- Select detection method (HOG/YOLO)
- Choose camera index
- Click "Start Detection"
- View live statistics
- Save screenshots

### Terminal Mode
```bash
# Run in terminal
python main.py --mode terminal

# Controls:
# 'q' - Quit
# 's' - Save screenshot
```

### Command Line Options
```bash
# Show help
python main.py --help

# Specific camera
python main.py --camera 1

# YOLO detection
python main.py --method YOLO

# Terminal mode with YOLO
python main.py --mode terminal --method YOLO
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Detection Method
DETECTION_METHOD = 'HOG'  # or 'YOLO'

# Camera Settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30

# Detection Thresholds
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4

# Display Settings
BOUNDING_BOX_COLOR = (0, 255, 0)
BOUNDING_BOX_THICKNESS = 2
```

## 🔧 Troubleshooting

### Problem: NumPy Installation Fails

**Error Message:**
```
ERROR: Unknown compiler(s): [['cl'], ['gcc'], ['clang']]
```

**Solution:**
```bash
# You're using Python 3.13!
# Uninstall Python 3.13
# Install Python 3.11 or 3.12
# Try again
```

### Problem: Camera Not Accessible

**Solutions:**
1. Close other apps using camera (Zoom, Skype, etc.)
2. Try different camera index:
   ```bash
   python main.py --camera 1
   ```
3. Check camera permissions in system settings

### Problem: Module Not Found

**Solution:**
```bash
# Activate virtual environment first
venv\Scripts\activate

# Then install
pip install opencv-python numpy pillow
```

### Problem: YOLO Not Working

**Solution:**
- YOLO requires additional model files (~200MB)
- Download from: https://pjreddie.com/darknet/yolo/
- For beginners, use HOG method (default)

## 📁 Project Structure

```
Room_security/
│
├── main.py                 # Main entry point
├── person_detection.py     # Detection logic
├── gui_app.py             # GUI interface
├── config.py              # Configuration
├── requirements.txt       # Dependencies
│
├── install.bat            # Installation script (Windows)
├── run.bat               # Launch script (Windows)
├── README.md             # This file
└── SETUP_GUIDE.md        # Detailed setup guide
```

## 🔍 Detection Methods

### HOG (Histogram of Oriented Gradients)
- ✅ Fast and efficient
- ✅ No extra files required
- ✅ Good for real-time
- ❌ Less accurate than YOLO
- **Best for:** Learning, real-time applications

### YOLO (You Only Look Once)
- ✅ Very accurate
- ✅ Detects multiple objects
- ❌ Requires model files
- ❌ Higher resource usage
- **Best for:** Accuracy-critical applications

## 📊 Performance Tips

### For Better Speed:
- Use HOG method
- Lower camera resolution
- Close other applications
- Reduce history size in config

### For Better Accuracy:
- Use YOLO method
- Improve lighting
- Use higher resolution
- Adjust confidence threshold

## 🎓 Technical Details

### Technologies Used:
- **OpenCV:** Computer vision and image processing
- **NumPy:** Numerical computations
- **Pillow:** Image handling for GUI
- **Tkinter:** GUI framework
- **Python Threading:** Real-time processing

### Detection Pipeline:
1. Capture frame from camera
2. Preprocess image
3. Run detection algorithm (HOG/YOLO)
4. Draw bounding boxes
5. Calculate statistics
6. Display results
7. Update history

## 🌟 Future Enhancements

- [ ] Face recognition for person identification
- [ ] Motion detection to reduce false positives
- [ ] Email/SMS alerts on detection
- [ ] Video recording of detections
- [ ] Web-based interface
- [ ] Multi-camera support
- [ ] Database integration for history
- [ ] Mobile app for remote monitoring

## 📝 License

This project is created for educational purposes.

## 🤝 Contributing

Suggestions and improvements are welcome!

## 📞 Support

### Common Issues:
1. **Python Version:** Must be 3.11 or 3.12
2. **Camera Access:** Close other camera apps
3. **Package Installation:** Use virtual environment
4. **Performance:** Try HOG method first

### Resources:
- OpenCV Docs: https://docs.opencv.org/
- Python Docs: https://docs.python.org/
- Computer Vision: https://pyimagesearch.com/

## 🎉 Success Checklist

- [x] Python 3.11/3.12 installed
- [x] Virtual environment created
- [x] Dependencies installed
- [x] Camera working
- [x] Application runs successfully

**Congratulations! Your person detection system is ready!** 🎊

---

**Created for B.Tech Project | October 2025**