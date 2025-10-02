#!/bin/bash
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
