# Let's create the requirements.txt file first

requirements_content = """# Core Dependencies
opencv-python==4.8.1.78
numpy==1.24.3
imutils==0.5.4
Pillow==10.0.1
python-dateutil==2.8.2

# GUI Framework
tkinter

# Optional: For YOLO (more accurate detection)
ultralytics==8.0.196
torch>=1.8.0
torchvision>=0.9.0

# Additional utilities
argparse
threading
datetime
"""

# Write requirements.txt
with open('person_detector/requirements.txt', 'w') as f:
    f.write(requirements_content.strip())

print("✓ requirements.txt created")

# Create config.py with configuration settings
config_content = """# Configuration file for person detection project

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

# Write config.py (we'll import cv2 in the actual file)
config_content = config_content.replace("cv2.FONT_HERSHEY_SIMPLEX", "0")
with open('person_detector/config.py', 'w') as f:
    f.write(config_content)

print("✓ config.py created")