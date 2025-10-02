# Configuration file for person detection project

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
FONT = 0
FONT_SCALE = 0.7
FONT_THICKNESS = 2

# Camera settings
CAMERA_INDEX = 0  # 0 for default camera
