import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import time
import datetime
from person_detection import PersonDetector, CameraManager
import config

class PersonDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Person Detection System")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg='#2c3e50')

        # Initialize components
        self.detector = PersonDetector(method=config.DETECTION_METHOD)
        self.camera = CameraManager(config.CAMERA_INDEX)

        # GUI variables
        self.is_running = False
        self.current_frame = None
        self.photo_image = None

        # Threading
        self.detection_thread = None
        self.stop_thread = False

        self.setup_gui()

    def setup_gui(self):
        """Setup the main GUI layout"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        title_label = tk.Label(main_frame, text="🎥 Real-Time Person Detection System", 
                              font=('Arial', 20, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(pady=(0, 10))

        # Create two main sections: video and stats
        content_frame = tk.Frame(main_frame, bg='#2c3e50')
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Left side - Video feed
        self.setup_video_section(content_frame)

        # Right side - Statistics and controls
        self.setup_stats_section(content_frame)

        # Bottom - Controls
        self.setup_controls_section(main_frame)

    def setup_video_section(self, parent):
        """Setup video display section"""
        video_frame = tk.LabelFrame(parent, text="📹 Live Camera Feed", 
                                   font=('Arial', 12, 'bold'),
                                   fg='white', bg='#34495e', 
                                   relief=tk.RAISED, bd=2)
        video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Video display label
        self.video_label = tk.Label(video_frame, bg='black', 
                                   text="Camera Feed will appear here\nClick 'Start Detection' to begin",
                                   font=('Arial', 14), fg='white')
        self.video_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def setup_stats_section(self, parent):
        """Setup statistics display section"""
        stats_frame = tk.LabelFrame(parent, text="📊 Detection Statistics", 
                                   font=('Arial', 12, 'bold'),
                                   fg='white', bg='#34495e',
                                   relief=tk.RAISED, bd=2)
        stats_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 0))
        stats_frame.configure(width=300)

        # Current time display
        time_frame = tk.Frame(stats_frame, bg='#34495e')
        time_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(time_frame, text="🕐 Current Time:", 
                font=('Arial', 10, 'bold'), fg='white', bg='#34495e').pack(anchor='w')
        self.time_label = tk.Label(time_frame, text="--:--:--", 
                                  font=('Arial', 14, 'bold'), fg='#3498db', bg='#34495e')
        self.time_label.pack(anchor='w')

        # Separator
        separator1 = ttk.Separator(stats_frame, orient='horizontal')
        separator1.pack(fill=tk.X, padx=10, pady=5)

        # Current detection stats
        current_frame = tk.Frame(stats_frame, bg='#34495e')
        current_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(current_frame, text="👥 Current Detection:", 
                font=('Arial', 10, 'bold'), fg='white', bg='#34495e').pack(anchor='w')

        # Person count display
        count_frame = tk.Frame(current_frame, bg='#2c3e50', relief=tk.RAISED, bd=2)
        count_frame.pack(fill=tk.X, pady=5)

        self.count_label = tk.Label(count_frame, text="0", 
                                   font=('Arial', 36, 'bold'), 
                                   fg='#e74c3c', bg='#2c3e50')
        self.count_label.pack()

        tk.Label(count_frame, text="Persons Detected", 
                font=('Arial', 10), fg='white', bg='#2c3e50').pack()

        # Separator
        separator2 = ttk.Separator(stats_frame, orient='horizontal')
        separator2.pack(fill=tk.X, padx=10, pady=5)

        # Detection method
        method_frame = tk.Frame(stats_frame, bg='#34495e')
        method_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(method_frame, text="🔍 Detection Method:", 
                font=('Arial', 10, 'bold'), fg='white', bg='#34495e').pack(anchor='w')
        self.method_label = tk.Label(method_frame, text=config.DETECTION_METHOD, 
                                    font=('Arial', 12, 'bold'), fg='#2ecc71', bg='#34495e')
        self.method_label.pack(anchor='w')

        # Statistics
        stats_info_frame = tk.Frame(stats_frame, bg='#34495e')
        stats_info_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(stats_info_frame, text="📈 Session Statistics:", 
                font=('Arial', 10, 'bold'), fg='white', bg='#34495e').pack(anchor='w')

        self.avg_label = tk.Label(stats_info_frame, text="Average: --", 
                                 font=('Arial', 10), fg='white', bg='#34495e')
        self.avg_label.pack(anchor='w', pady=2)

        self.max_label = tk.Label(stats_info_frame, text="Maximum: --", 
                                 font=('Arial', 10), fg='white', bg='#34495e')
        self.max_label.pack(anchor='w', pady=2)

        # Recent detections history
        history_frame = tk.LabelFrame(stats_frame, text="📋 Recent History", 
                                     font=('Arial', 10, 'bold'),
                                     fg='white', bg='#34495e')
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollable text widget for history
        self.history_text = tk.Text(history_frame, height=8, width=30,
                                   bg='#2c3e50', fg='white', font=('Consolas', 9))
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_text.yview)
        self.history_text.configure(yscrollcommand=scrollbar.set)

        self.history_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def setup_controls_section(self, parent):
        """Setup control buttons section"""
        controls_frame = tk.Frame(parent, bg='#2c3e50')
        controls_frame.pack(fill=tk.X, pady=10)

        # Control buttons
        button_frame = tk.Frame(controls_frame, bg='#2c3e50')
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="▶️ Start Detection", 
                                     command=self.start_detection,
                                     font=('Arial', 12, 'bold'),
                                     bg='#27ae60', fg='white',
                                     relief=tk.RAISED, bd=3,
                                     padx=20, pady=10)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(button_frame, text="⏹️ Stop Detection", 
                                    command=self.stop_detection,
                                    font=('Arial', 12, 'bold'),
                                    bg='#e74c3c', fg='white',
                                    relief=tk.RAISED, bd=3,
                                    padx=20, pady=10,
                                    state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Method toggle button
        self.toggle_button = tk.Button(button_frame, text="🔄 Switch to YOLO", 
                                      command=self.toggle_method,
                                      font=('Arial', 12, 'bold'),
                                      bg='#3498db', fg='white',
                                      relief=tk.RAISED, bd=3,
                                      padx=20, pady=10)
        self.toggle_button.pack(side=tk.LEFT, padx=10)

    def start_detection(self):
        """Start the detection process"""
        if not self.camera.start_camera():
            messagebox.showerror("Error", "Cannot access camera!")
            return

        self.is_running = True
        self.stop_thread = False

        # Update button states
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.toggle_button.config(state=tk.DISABLED)

        # Start detection thread
        self.detection_thread = threading.Thread(target=self.detection_loop, daemon=True)
        self.detection_thread.start()

        # Start GUI update loop
        self.update_gui()

    def stop_detection(self):
        """Stop the detection process"""
        self.is_running = False
        self.stop_thread = True

        # Stop camera
        self.camera.stop_camera()

        # Update button states
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.toggle_button.config(state=tk.NORMAL)

        # Clear video display
        self.video_label.config(image='', text="Detection Stopped\nClick 'Start Detection' to begin again")

    def toggle_method(self):
        """Toggle between HOG and YOLO detection methods"""
        current_method = self.detector.method
        new_method = "YOLO" if current_method == "HOG" else "HOG"

        try:
            self.detector = PersonDetector(method=new_method)
            self.method_label.config(text=new_method)
            self.toggle_button.config(text=f"🔄 Switch to {'HOG' if new_method == 'YOLO' else 'YOLO'}")
            messagebox.showinfo("Success", f"Switched to {new_method} detection method")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to switch method: {str(e)}")

    def detection_loop(self):
        """Main detection loop running in separate thread"""
        while not self.stop_thread and self.is_running:
            ret, frame = self.camera.read_frame()
            if ret:
                # Perform detection
                annotated_frame, count = self.detector.detect_persons(frame)
                self.current_frame = annotated_frame

            time.sleep(0.03)  # ~30 FPS

    def update_gui(self):
        """Update GUI elements (runs on main thread)"""
        if not self.is_running:
            return

        # Update time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)

        # Update video display
        if self.current_frame is not None:
            self.update_video_display(self.current_frame)

        # Update statistics
        self.update_statistics()

        # Update detection history
        self.update_history()

        # Schedule next update
        self.root.after(100, self.update_gui)  # Update every 100ms

    def update_video_display(self, frame):
        """Update the video display with current frame"""
        # Resize frame to fit display
        display_width = 640
        display_height = 480
        frame_resized = cv2.resize(frame, (display_width, display_height))

        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

        # Convert to PIL Image
        pil_image = Image.fromarray(frame_rgb)

        # Convert to Tkinter PhotoImage
        self.photo_image = ImageTk.PhotoImage(pil_image)

        # Update label
        self.video_label.config(image=self.photo_image, text="")

    def update_statistics(self):
        """Update detection statistics display"""
        stats = self.detector.get_current_stats()

        # Update person count
        self.count_label.config(text=str(stats['current_count']))

        # Update session statistics
        self.avg_label.config(text=f"Average: {stats['avg_count']}")
        self.max_label.config(text=f"Maximum: {stats['max_count']}")

    def update_history(self):
        """Update detection history display"""
        history = self.detector.get_detection_history()

        # Clear current text
        self.history_text.delete(1.0, tk.END)

        # Add recent detections
        for entry in reversed(history):  # Show most recent first
            time_str = entry['time'].strftime("%H:%M:%S")
            count = entry['count']
            self.history_text.insert(tk.END, f"{time_str} - {count} person(s)\n")

        # Auto-scroll to bottom
        self.history_text.see(tk.END)

    def on_closing(self):
        """Handle window closing"""
        if self.is_running:
            self.stop_detection()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = PersonDetectionGUI(root)

    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()