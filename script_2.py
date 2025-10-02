# Create the main person detection module
person_detection_content = """
import cv2
import numpy as np
import datetime
from typing import Tuple, List, Optional
import config

class PersonDetector:
    def __init__(self, method="HOG"):
        self.method = method
        self.person_count = 0
        self.detection_history = []
        
        if method == "HOG":
            self.setup_hog()
        elif method == "YOLO":
            self.setup_yolo()
    
    def setup_hog(self):
        \"\"\"Setup HOG descriptor for person detection\"\"\"
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        print("✓ HOG Person Detector initialized")
    
    def setup_yolo(self):
        \"\"\"Setup YOLO model for person detection (requires ultralytics)\"\"\"
        try:
            from ultralytics import YOLO
            self.yolo_model = YOLO('yolov8n.pt')  # Download model automatically
            print("✓ YOLO Person Detector initialized")
        except ImportError:
            print("⚠ YOLO not available. Install: pip install ultralytics")
            print("Falling back to HOG detector...")
            self.method = "HOG"
            self.setup_hog()
    
    def detect_persons_hog(self, frame: np.ndarray) -> Tuple[List, int]:
        \"\"\"Detect persons using HOG descriptor\"\"\"
        # Detect people in the frame
        boxes, weights = self.hog.detectMultiScale(
            frame, 
            winStride=config.HOG_WIN_STRIDE,
            padding=config.HOG_PADDING,
            scale=config.HOG_SCALE
        )
        
        # Convert to list of bounding boxes
        person_boxes = []
        for (x, y, w, h) in boxes:
            person_boxes.append((x, y, x + w, y + h))
        
        return person_boxes, len(person_boxes)
    
    def detect_persons_yolo(self, frame: np.ndarray) -> Tuple[List, int]:
        \"\"\"Detect persons using YOLO model\"\"\"
        try:
            results = self.yolo_model(frame, verbose=False)
            person_boxes = []
            
            for r in results:
                boxes = r.boxes
                if boxes is not None:
                    for box in boxes:
                        # Check if detected class is 'person' (class 0 in COCO)
                        if int(box.cls[0]) == 0:  # Person class
                            coords = box.xyxy[0].tolist()
                            person_boxes.append(coords)
            
            return person_boxes, len(person_boxes)
        except Exception as e:
            print(f"YOLO detection error: {e}")
            return [], 0
    
    def detect_persons(self, frame: np.ndarray) -> Tuple[np.ndarray, int]:
        \"\"\"Main detection method that returns annotated frame and person count\"\"\"
        if self.method == "HOG":
            boxes, count = self.detect_persons_hog(frame)
        else:
            boxes, count = self.detect_persons_yolo(frame)
        
        # Update person count and history
        self.person_count = count
        current_time = datetime.datetime.now()
        self.detection_history.append({
            'time': current_time,
            'count': count,
            'boxes': boxes
        })
        
        # Keep only last 10 entries
        if len(self.detection_history) > 10:
            self.detection_history.pop(0)
        
        # Draw bounding boxes and annotations
        annotated_frame = self.draw_detections(frame, boxes, count)
        
        return annotated_frame, count
    
    def draw_detections(self, frame: np.ndarray, boxes: List, count: int) -> np.ndarray:
        \"\"\"Draw bounding boxes and information on frame\"\"\"
        annotated_frame = frame.copy()
        
        # Draw bounding boxes around detected persons
        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box)
            
            # Draw rectangle
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), config.BBOX_COLOR, 2)
            
            # Add person label
            label = f'Person {i+1}'
            label_size, _ = cv2.getTextSize(label, config.FONT, 0.5, 1)
            cv2.rectangle(annotated_frame, (x1, y1-label_size[1]-10), 
                         (x1+label_size[0], y1), config.BBOX_COLOR, -1)
            cv2.putText(annotated_frame, label, (x1, y1-5), 
                       config.FONT, 0.5, (0, 0, 0), 1)
        
        # Add current date and time (top left)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(annotated_frame, current_time, (10, 30), 
                   config.FONT, 0.6, config.TIME_COLOR, config.FONT_THICKNESS)
        
        # Add detection status (below time)
        status_text = f'Status: Detecting ({self.method})'
        cv2.putText(annotated_frame, status_text, (10, 60), 
                   config.FONT, 0.6, config.TEXT_COLOR, config.FONT_THICKNESS)
        
        # Add person count (below status)
        count_text = f'Total Persons: {count}'
        cv2.putText(annotated_frame, count_text, (10, 90), 
                   config.FONT, 0.6, config.TEXT_COLOR, config.FONT_THICKNESS)
        
        return annotated_frame
    
    def get_detection_history(self) -> List[dict]:
        \"\"\"Get recent detection history\"\"\"
        return self.detection_history[-5:]  # Last 5 entries
    
    def get_current_stats(self) -> dict:
        \"\"\"Get current detection statistics\"\"\"
        if not self.detection_history:
            return {'current_count': 0, 'avg_count': 0, 'max_count': 0}
        
        recent_counts = [entry['count'] for entry in self.detection_history[-10:]]
        
        return {
            'current_count': self.person_count,
            'avg_count': round(np.mean(recent_counts), 1),
            'max_count': max(recent_counts)
        }


class CameraManager:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None
        self.is_active = False
    
    def start_camera(self) -> bool:
        \"\"\"Start the camera capture\"\"\"
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print(f"Error: Cannot open camera {self.camera_index}")
            return False
        
        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        
        self.is_active = True
        print(f"✓ Camera {self.camera_index} started")
        return True
    
    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        \"\"\"Read a frame from camera\"\"\"
        if not self.is_active or self.cap is None:
            return False, None
        
        ret, frame = self.cap.read()
        return ret, frame
    
    def stop_camera(self):
        \"\"\"Stop camera capture and release resources\"\"\"
        if self.cap:
            self.cap.release()
        self.is_active = False
        print("✓ Camera stopped")
    
    def __del__(self):
        self.stop_camera()
"""

# Write the person detection module
with open('person_detector/person_detection.py', 'w') as f:
    f.write(person_detection_content.strip())

print("✓ person_detection.py created")