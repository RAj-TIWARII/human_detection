# Create a setup script for easy installation
setup_script = """#!/usr/bin/env python3
\"\"\"
Setup script for Person Detection System
Automates the installation of required packages
\"\"\"

import subprocess
import sys
import os

def run_command(command):
    \"\"\"Run a command and handle errors\"\"\"
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
    \"\"\"Check if Python version is compatible\"\"\"
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} is not compatible. Need Python 3.7+")
        return False

def install_requirements():
    \"\"\"Install required packages\"\"\"
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
    print("\\n🤖 Installing YOLO (optional but recommended)...")
    yolo_packages = ["ultralytics", "torch", "torchvision"]
    for package in yolo_packages:
        run_command(f"pip install {package}")
    
    return True

def test_installation():
    \"\"\"Test if all packages are working\"\"\"
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
    \"\"\"Main setup function\"\"\"
    print("🎥 Person Detection System Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Upgrade pip
    print("\\n🔧 Upgrading pip...")
    run_command("python -m pip install --upgrade pip")
    
    # Install requirements
    print("\\n📦 Installing requirements...")
    if not install_requirements():
        print("❌ Installation failed!")
        sys.exit(1)
    
    # Test installation
    print("\\n🧪 Testing installation...")
    if test_installation():
        print("\\n✅ Setup completed successfully!")
        print("\\n🚀 You can now run the application:")
        print("   python main.py                    # GUI mode")
        print("   python main.py --mode terminal    # Terminal mode")
    else:
        print("\\n⚠️ Setup completed with some issues.")
        print("Try installing missing packages manually.")

if __name__ == "__main__":
    main()
"""

# Write setup script
with open('person_detector/setup.py', 'w') as f:
    f.write(setup_script.strip())

print("✅ setup.py created")

# Create a batch file for Windows users
windows_setup = """@echo off
echo 🎥 Person Detection System - Windows Setup
echo ==========================================

echo 📍 Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo 📍 Upgrading pip...
python -m pip install --upgrade pip

echo 📍 Installing required packages...
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install imutils==0.5.4
pip install Pillow==10.0.1
pip install python-dateutil==2.8.2

echo 📍 Installing YOLO (optional)...
pip install ultralytics
pip install torch torchvision

echo ✅ Setup completed!
echo.
echo 🚀 You can now run:
echo    python main.py
echo.
pause
"""

# Write Windows setup script
with open('person_detector/setup_windows.bat', 'w') as f:
    f.write(windows_setup)

print("✅ setup_windows.bat created")

# Create a shell script for Linux/Mac users
unix_setup = """#!/bin/bash
echo "🎥 Person Detection System - Unix Setup"
echo "========================================"

echo "📍 Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python3 is not installed"
    echo "Please install Python 3.7+ using your package manager"
    exit 1
fi

echo "📍 Upgrading pip..."
python3 -m pip install --upgrade pip

echo "📍 Installing required packages..."
python3 -m pip install opencv-python==4.8.1.78
python3 -m pip install numpy==1.24.3
python3 -m pip install imutils==0.5.4
python3 -m pip install Pillow==10.0.1
python3 -m pip install python-dateutil==2.8.2

echo "📍 Installing YOLO (optional)..."
python3 -m pip install ultralytics
python3 -m pip install torch torchvision

echo "✅ Setup completed!"
echo ""
echo "🚀 You can now run:"
echo "   python3 main.py"
echo ""
"""

# Write Unix setup script
with open('person_detector/setup_unix.sh', 'w') as f:
    f.write(unix_setup)

print("✅ setup_unix.sh created")

# Make Unix script executable (if on Unix system)
try:
    os.chmod('person_detector/setup_unix.sh', 0o755)
    print("✅ Made setup_unix.sh executable")
except:
    print("⚠️ Could not set executable permissions (probably on Windows)")

print("\\n" + "="*60)
print("🎉 COMPLETE PERSON DETECTION PROJECT CREATED!")
print("="*60)

# List all created files
print("\\n📁 Project Structure:")
for root, dirs, files in os.walk('person_detector'):
    level = root.replace('person_detector', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

print("\\n📋 Files Created:")
files_description = {
    'main.py': 'Main entry point - run this file',
    'person_detection.py': 'Core detection algorithms (HOG & YOLO)',
    'gui_app.py': 'Professional GUI interface',
    'config.py': 'Configuration settings',
    'requirements.txt': 'Python package dependencies',
    'README.md': 'Complete documentation',
    'setup.py': 'Automated setup script',
    'setup_windows.bat': 'Windows installation script',
    'setup_unix.sh': 'Linux/Mac installation script'
}

for filename, description in files_description.items():
    print(f"  ✓ {filename:<20} - {description}")

print("\\n" + "="*60)