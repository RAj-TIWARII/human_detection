#!/usr/bin/env python3
"""
Setup script for Person Detection System
Automates the installation of required packages
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a command and handle errors"""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print("✅ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} is not compatible. Need Python 3.7+")
        return False

def install_requirements():
    """Install required packages"""
    packages = [
        "opencv-python==4.8.1.78",
        "numpy==1.24.3", 
        "imutils==0.5.4",
        "Pillow==10.0.1",
        "python-dateutil==2.8.2"
    ]

    print("📦 Installing core packages...")
    for package in packages:
        if not run_command(f"pip install {package}"):
            print(f"⚠️ Failed to install {package}")
            return False

    # Optional YOLO installation
    print("\n🤖 Installing YOLO (optional but recommended)...")
    yolo_packages = ["ultralytics", "torch", "torchvision"]
    for package in yolo_packages:
        run_command(f"pip install {package}")

    return True

def test_installation():
    """Test if all packages are working"""
    print("🧪 Testing installation...")

    try:
        import cv2
        print("✅ OpenCV imported successfully")
    except ImportError:
        print("❌ OpenCV import failed")
        return False

    try:
        import numpy
        print("✅ NumPy imported successfully")
    except ImportError:
        print("❌ NumPy import failed")
        return False

    try:
        import PIL
        print("✅ Pillow imported successfully")
    except ImportError:
        print("❌ Pillow import failed")
        return False

    try:
        import tkinter
        print("✅ Tkinter imported successfully")
    except ImportError:
        print("⚠️ Tkinter not available - GUI mode won't work")

    try:
        from ultralytics import YOLO
        print("✅ YOLO imported successfully")
    except ImportError:
        print("⚠️ YOLO not available - only HOG detection will work")

    return True

def main():
    """Main setup function"""
    print("🎥 Person Detection System Setup")
    print("=" * 40)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Upgrade pip
    print("\n🔧 Upgrading pip...")
    run_command("python -m pip install --upgrade pip")

    # Install requirements
    print("\n📦 Installing requirements...")
    if not install_requirements():
        print("❌ Installation failed!")
        sys.exit(1)

    # Test installation
    print("\n🧪 Testing installation...")
    if test_installation():
        print("\n✅ Setup completed successfully!")
        print("\n🚀 You can now run the application:")
        print("   python main.py                    # GUI mode")
        print("   python main.py --mode terminal    # Terminal mode")
    else:
        print("\n⚠️ Setup completed with some issues.")
        print("Try installing missing packages manually.")

if __name__ == "__main__":
    main()