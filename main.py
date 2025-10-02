#!/usr/bin/env python3
"""
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
"""

import argparse
import sys
import cv2
from person_detection import PersonDetector, CameraManager
import config

def run_gui():
    """Run the GUI version of the application"""
    try:
        from gui_app import main as gui_main
        print("🚀 Starting GUI application...")
        gui_main()
    except ImportError as e:
        print(f"❌ Error importing GUI components: {e}")
        print("💡 Try installing missing packages: pip install pillow tkinter")
        sys.exit(1)

def run_terminal():
    """Run the terminal/command-line version"""
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
    print("\n🎯 Detection started! Press 'q' to quit, 's' to save screenshot")
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
        print("\n⏹️ Detection stopped by user")

    finally:
        # Cleanup
        camera.stop_camera()
        cv2.destroyAllWindows()
        print("✅ Cleanup completed")

def main():
    """Main entry point"""
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