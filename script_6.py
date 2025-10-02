# Create a comprehensive installation and usage guide
installation_guide = """
# 🎥 PERSON DETECTION SYSTEM - COMPLETE INSTALLATION GUIDE

## 📋 WHAT YOU NEED TO DOWNLOAD FROM TERMINAL

### Method 1: Automatic Setup (Recommended)

**For Windows:**
```cmd
cd person_detector
setup_windows.bat
```

**For Linux/Mac:**
```bash
cd person_detector
chmod +x setup_unix.sh
./setup_unix.sh
```

**Or using Python (All platforms):**
```bash
cd person_detector
python setup.py
```

### Method 2: Manual Installation

**Step 1: Install Core Packages**
```bash
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install imutils==0.5.4
pip install Pillow==10.0.1
pip install python-dateutil==2.8.2
```

**Step 2: Install YOLO (Optional but Recommended)**
```bash
pip install ultralytics
pip install torch torchvision
```

## 🚀 HOW TO RUN THE PROJECT

### GUI Mode (Recommended)
```bash
cd person_detector
python main.py
```

### Terminal Mode
```bash
cd person_detector
python main.py --mode terminal
```

### With Options
```bash
# Use YOLO detection method
python main.py --method YOLO

# Use specific camera (if you have multiple)
python main.py --camera 1

# Terminal mode with YOLO
python main.py --mode terminal --method YOLO
```

## 🎯 WHAT THE PROJECT DOES

✅ **Real-time person detection** - Detects people in camera feed
✅ **Bounding boxes** - Green squares around detected persons  
✅ **Person counting** - Shows current, average, and maximum counts
✅ **Accurate clock** - Current time displayed in top-left corner
✅ **Professional GUI** - Easy-to-use interface
✅ **Detection history** - Recent detections with timestamps
✅ **Multiple methods** - HOG (fast) or YOLO (accurate)
✅ **Statistics panel** - Comprehensive detection analytics

## 🖥️ SYSTEM REQUIREMENTS

- **Python**: 3.7 or higher
- **Operating System**: Windows 10/11, macOS, or Linux
- **Camera**: Built-in webcam or USB camera
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB free space

## 🔧 TROUBLESHOOTING

### "Cannot access camera"
```bash
# Try different camera indices
python main.py --camera 0  # Default camera
python main.py --camera 1  # Second camera
python main.py --camera 2  # Third camera
```

### "Module not found" errors
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Reinstall packages
pip install --force-reinstall opencv-python numpy pillow
```

### YOLO not working
```bash
# Install YOLO separately
pip install ultralytics

# Or use HOG method only
python main.py --method HOG
```

### GUI not opening
```bash
# Try terminal mode instead
python main.py --mode terminal

# On Linux, install tkinter
sudo apt-get install python3-tk
```

## 📱 FEATURES OVERVIEW

### Detection Features:
- 👥 **Person Detection**: Automatically detects people in camera feed
- 🎯 **Bounding Boxes**: Green rectangles around each detected person
- 🔢 **Person Labels**: "Person 1", "Person 2", etc.
- ⏰ **Real-time Clock**: Accurate timestamp in top-left corner
- 📊 **Live Statistics**: Current count, average, and maximum

### GUI Features:
- 🖼️ **Live Camera Feed**: Real-time video display
- 📈 **Statistics Panel**: Detection analytics and history
- 🎛️ **Control Buttons**: Start, stop, and method switching
- 📋 **Detection History**: Timestamped log of recent detections
- 🔄 **Method Toggle**: Switch between HOG and YOLO

### Terminal Features:
- 🖥️ **Command Line Interface**: Run without GUI
- 📸 **Screenshot Saving**: Press 's' to save current frame
- ⌨️ **Keyboard Controls**: 'q' to quit, 's' to save
- 📊 **Console Statistics**: Printed detection stats

## 🎮 HOW TO USE

### GUI Mode:
1. Run: `python main.py`
2. Click "▶️ Start Detection"
3. See people detected with green boxes
4. View statistics on the right panel
5. Use "🔄 Switch Method" to change detection type
6. Click "⏹️ Stop Detection" when done

### Terminal Mode:
1. Run: `python main.py --mode terminal`
2. Camera window opens automatically
3. Press 'q' to quit
4. Press 's' to save screenshot

## 📊 UNDERSTANDING THE DISPLAY

**On Video:**
- ⏰ Top-left: Current date and time
- 🎯 Green boxes: Detected persons
- 🏷️ Labels: "Person 1", "Person 2", etc.
- 📊 Status: Detection method and person count

**In GUI Panel:**
- 👥 Large number: Current person count
- 📈 Average: Moving average of detections
- 📈 Maximum: Highest count in session
- 📋 History: Recent detections with timestamps

## ⚙️ CUSTOMIZATION

Edit `config.py` to change:
- Detection method (HOG/YOLO)
- Camera index
- Colors and display settings
- Camera resolution
- Detection parameters

## 🛠️ PROJECT STRUCTURE

```
person_detector/
├── main.py                 # ← RUN THIS FILE
├── person_detection.py     # Detection algorithms
├── gui_app.py             # GUI interface  
├── config.py              # Settings
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── setup.py               # Auto installer
├── setup_windows.bat      # Windows installer
└── setup_unix.sh          # Linux/Mac installer
```

## 🏆 DETECTION METHODS

### HOG (Histogram of Oriented Gradients)
- ⚡ **Speed**: Very fast
- 🎯 **Accuracy**: Good
- 💻 **Resources**: Low CPU usage
- ✅ **Best for**: Real-time applications, older computers

### YOLO (You Only Look Once)
- ⚡ **Speed**: Moderate
- 🎯 **Accuracy**: Excellent
- 💻 **Resources**: Higher CPU/GPU usage  
- ✅ **Best for**: High accuracy requirements, modern computers

## 🆘 COMMON ISSUES & SOLUTIONS

| Issue | Solution |
|-------|----------|
| Camera not working | Try `--camera 1` or `--camera 2` |
| GUI freezing | Use terminal mode instead |
| Low accuracy | Switch to YOLO method |
| High CPU usage | Switch to HOG method |
| Import errors | Run setup script again |
| No tkinter | `sudo apt-get install python3-tk` (Linux) |

## ✅ FINAL CHECKLIST

Before running, make sure you have:
- [ ] Python 3.7+ installed
- [ ] All packages installed (run setup script)
- [ ] Camera connected and working
- [ ] Proper camera permissions
- [ ] All project files in same directory

## 🎉 YOU'RE READY TO GO!

Run this command to start:
```bash
python main.py
```

Enjoy your person detection system! 🚀
"""

# Write the comprehensive guide
with open('person_detector/INSTALLATION_GUIDE.md', 'w') as f:
    f.write(installation_guide.strip())

print("✅ INSTALLATION_GUIDE.md created")

# Create a quick start file
quick_start = """
🎥 QUICK START GUIDE
==================

1. INSTALL:
   Windows: Double-click setup_windows.bat
   Linux/Mac: ./setup_unix.sh
   Or: python setup.py

2. RUN:
   python main.py

3. ENJOY:
   - Green boxes around people
   - Time in top-left corner
   - Statistics on right panel
   - Press Start Detection to begin!

TROUBLESHOOTING:
- Camera not found? Try: python main.py --camera 1
- GUI issues? Try: python main.py --mode terminal
- Poor accuracy? Try: python main.py --method YOLO

That's it! 🚀
"""

with open('person_detector/QUICK_START.txt', 'w') as f:
    f.write(quick_start.strip())

print("✅ QUICK_START.txt created")

print("\\n" + "🎉"*20)
print("PROJECT COMPLETE! ALL FILES READY!")
print("🎉"*20)