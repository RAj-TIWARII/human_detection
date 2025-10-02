# 🎥 Person Detection System - Complete Setup Guide

## ⚠️ IMPORTANT: Python Version

**DO NOT use Python 3.13!** It's too new and many packages aren't compatible yet.

### ✅ Recommended: Python 3.11 or 3.12

Download from: https://www.python.org/downloads/

---

## 📁 Project Structure

Create this folder structure:

```
Room_security/
│
├── main.py                  # Main entry point
├── person_detection.py      # Detection logic
├── gui_app.py              # GUI interface
├── config.py               # Configuration
├── requirements.txt        # Dependencies
└── README.md              # This file
```

---

## 🚀 Quick Setup (Step by Step)

### Step 1: Install Python 3.11 or 3.12

1. Go to https://www.python.org/downloads/
2. Download Python 3.11.x or 3.12.x (NOT 3.13)
3. During installation, **check "Add Python to PATH"**
4. Verify installation:
   ```bash
   python --version
   ```
   Should show: `Python 3.11.x` or `Python 3.12.x`

### Step 2: Create Project Folder

```bash
cd Desktop
mkdir Room_security
cd Room_security
```

### Step 3: Save All Project Files

Save these files in your `Room_security` folder:
- `main.py`
- `person_detection.py`
- `gui_app.py`
- `config.py`
- `requirements.txt`

### Step 4: Install Dependencies

Open PowerShell/Command Prompt in the project folder and run:

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
# GUI Mode (Default - Recommended)
python main.py

# Terminal Mode
python main.py --mode terminal

# With specific camera
python main.py --camera 1

# With YOLO (requires YOLO files)
python main.py --method YOLO
```

---

## 🎮 Usage Guide

### GUI Mode Features:
- ✅ User-friendly interface
- ✅ Real-time video feed
- ✅ Person counting
- ✅ Statistics display
- ✅ Screenshot capture
- ✅ Easy start/stop controls

### Terminal Mode Features:
- ✅ Lightweight
- ✅ Real-time detection
- ✅ Statistics in console
- ✅ Press 'q' to quit
- ✅ Press 's' to save screenshot

---

## 🔧 Troubleshooting

### Issue: "Cannot access camera"
**Solution:**
- Make sure no other application is using the camera
- Try different camera index: `python main.py --camera 1`
- Check camera permissions in Windows Settings

### Issue: "Module not found"
**Solution:**
```bash
pip install opencv-python numpy pillow
```

### Issue: "numpy installation fails"
**Solution:**
- Uninstall Python 3.13
- Install Python 3.11 or 3.12
- Try again

### Issue: YOLO not working
**Solution:**
- YOLO requires additional model files
- Download from: https://pjreddie.com/darknet/yolo/
- For beginners, use HOG method (default)

---

## 📊 Detection Methods

### HOG (Default) ✅ Recommended for Beginners
- **Pros:** Fast, reliable, no extra files needed
- **Cons:** Less accurate than YOLO
- **Best for:** Real-time applications, learning

### YOLO (Advanced)
- **Pros:** Very accurate, detects multiple objects
- **Cons:** Requires model files (~200MB), slower
- **Best for:** High accuracy requirements

---

## 🎯 Command Line Options

```bash
# Show help
python main.py --help

# GUI mode (default)
python main.py --mode gui

# Terminal mode
python main.py --mode terminal

# Change detection method
python main.py --method YOLO
python main.py --method HOG

# Change camera
python main.py --camera 0  # Default webcam
python main.py --camera 1  # External camera
```

---

## 💡 Tips for Best Results

1. **Good Lighting:** Ensure room is well-lit
2. **Camera Angle:** Position camera at eye level
3. **Distance:** Stand 2-6 feet from camera
4. **Background:** Clear background works better
5. **Performance:** Close other heavy applications

---

## 🎓 Project Features

### Core Functionality:
- ✅ Real-time person detection
- ✅ Multiple detection methods (HOG/YOLO)
- ✅ Live person counting
- ✅ Detection statistics
- ✅ Screenshot capture
- ✅ History tracking
- ✅ Professional GUI interface

### Technical Highlights:
- **Computer Vision:** OpenCV for image processing
- **Machine Learning:** Pre-trained HOG/YOLO models
- **GUI Development:** Tkinter for interface
- **Threading:** Smooth real-time processing
- **Statistics:** Real-time analytics

---

## 📝 Configuration Options

Edit `config.py` to customize:

```python
# Detection settings
DETECTION_METHOD = 'HOG'  # or 'YOLO'
CONFIDENCE_THRESHOLD = 0.5

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30

# Display settings
BOUNDING_BOX_COLOR = (0, 255, 0)  # Green
BOUNDING_BOX_THICKNESS = 2
```

---

## 🐛 Common Errors & Solutions

### Error: "Python was not found"
```bash
# Solution: Add Python to PATH or use full path
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe main.py
```

### Error: "No module named 'cv2'"
```bash
# Solution: Install OpenCV
pip install opencv-python
```

### Error: "No module named 'PIL'"
```bash
# Solution: Install Pillow
pip install pillow
```

### Error: "DLL load failed"
```bash
# Solution: Install Visual C++ Redistributable
# Download from Microsoft website
```

---

## 📚 Learning Resources

### OpenCV:
- Official Docs: https://docs.opencv.org/
- Tutorials: https://opencv-python-tutroals.readthedocs.io/

### Python GUI:
- Tkinter Docs: https://docs.python.org/3/library/tkinter.html
- Real Python: https://realpython.com/python-gui-tkinter/

### Computer Vision:
- PyImageSearch: https://pyimagesearch.com/
- Towards Data Science: https://towardsdatascience.com/

---

## 🚀 Advanced Usage

### Running as Background Service:
```bash
# Run in background (Windows)
start /B python main.py --mode terminal

# Run in background (Linux/Mac)
nohup python main.py --mode terminal &
```

### Logging Output:
```bash
# Save console output to file
python main.py --mode terminal > detection_log.txt 2>&1
```

### Multiple Cameras:
```bash
# Camera 0
python main.py --camera 0

# Camera 1
python main.py --camera 1
```

---

## 📈 Performance Tips

### For Better FPS:
1. Lower resolution in `config.py`
2. Use HOG instead of YOLO
3. Reduce `MAX_HISTORY_SIZE`
4. Close unnecessary applications

### For Better Accuracy:
1. Use YOLO method
2. Improve lighting conditions
3. Use higher resolution
4. Adjust confidence threshold

---

## 🎯 Project Ideas for Enhancement

1. **Alert System:** Send email/SMS when person detected
2. **Face Recognition:** Identify specific persons
3. **Motion Detection:** Only detect when movement occurs
4. **Recording:** Save video clips of detections
5. **Web Interface:** Access via browser
6. **Multi-Camera:** Support multiple camera feeds
7. **Database:** Store detection history in database
8. **Mobile App:** Control via smartphone

---

## 📄 License & Credits

This project uses:
- **OpenCV** - Computer vision library
- **NumPy** - Numerical computing
- **Pillow** - Image processing
- **Tkinter** - GUI framework

Created for educational purposes.

---

## 🆘 Getting Help

If you encounter issues:

1. **Check Error Messages:** Read the full error carefully
2. **Google the Error:** Most errors have solutions online
3. **Check Python Version:** Must be 3.11 or 3.12
4. **Update Packages:** `pip install --upgrade opencv-python numpy pillow`
5. **Reinstall:** Delete `venv` folder and start fresh

---

## ✅ Quick Start Checklist

- [ ] Python 3.11 or 3.12 installed
- [ ] All files saved in project folder
- [ ] Virtual environment created
- [ ] Dependencies installed (`requirements.txt`)
- [ ] Camera connected and working
- [ ] Ran `python main.py` successfully

---

## 🎉 Success!

If everything works, you should see:
- GUI window opens
- Camera feed displays
- Detection boxes appear around persons
- Statistics update in real-time

**Congratulations!** Your person detection system is running! 🎊

---

## 📞 Support

For questions or issues:
- Check the troubleshooting section
- Review Python/OpenCV documentation
- Search for specific error messages online

**Good luck with your B.Tech project!** 🎓