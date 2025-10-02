# Create a well-spaced horizontal system architecture diagram
diagram_code = '''
flowchart LR
    subgraph UI["👥 USER INTERFACE LAYER"]
        direction TB
        GUI["<b>GUI Interface</b><br/>tkinter Framework"]
        Terminal["<b>Terminal Interface</b><br/>Command Line"]
    end
    
    subgraph Detection["🔍 DETECTION ENGINE LAYER"]
        direction TB
        PersonDetector["<b>PersonDetector</b><br/>Main Engine"]
        HOG["<b>HOG Method</b><br/>Traditional CV"]
        YOLO["<b>YOLO Method</b><br/>Deep Learning"]
        PersonDetector --- HOG
        PersonDetector --- YOLO
    end
    
    subgraph Camera["📹 CAMERA MANAGEMENT LAYER"]
        direction TB
        CameraManager["<b>CameraManager</b><br/>Control Hub"]
        OpenCV["<b>OpenCV</b><br/>VideoCapture API"]
        FrameProc["<b>Frame Processing</b><br/>Image Pipeline"]
        CameraManager --- OpenCV
        OpenCV --- FrameProc
    end
    
    subgraph Display["📊 DISPLAY & STATISTICS LAYER"]
        direction TB
        VideoDisplay["<b>Video Display</b><br/>Real-time View"]
        StatsPanel["<b>Statistics Panel</b><br/>Detection Metrics"]
        TimeOverlay["<b>Time Overlay</b><br/>Timestamp Info"]
        DetectionHist["<b>Detection History</b><br/>Event Logging"]
    end
    
    subgraph Config["⚙️ CONFIGURATION LAYER"]
        direction TB
        ConfigPy["<b>config.py</b><br/>Main Settings"]
        Settings["<b>Runtime Settings</b><br/>Dynamic Config"]
        Parameters["<b>Model Parameters</b><br/>Tuning Values"]
        ConfigPy --- Settings
        ConfigPy --- Parameters
    end
    
    %% Main data flow with clear spacing
    UI ==> Detection
    Detection ==> Camera
    Camera ==> Display
    
    %% Configuration connections
    Config ==> Detection
    Config ==> Camera
    
    %% Specific data connections
    FrameProc -.-> PersonDetector
    PersonDetector -.-> VideoDisplay
    PersonDetector -.-> StatsPanel
    PersonDetector -.-> DetectionHist
    VideoDisplay --> TimeOverlay
    
    %% Enhanced styling with better contrast and borders
    classDef uiStyle fill:#E8F4FD,stroke:#1565C0,stroke-width:4px,color:#000000
    classDef detectionStyle fill:#E8F8E8,stroke:#2E7D32,stroke-width:4px,color:#000000
    classDef cameraStyle fill:#FFF8E1,stroke:#F57C00,stroke-width:4px,color:#000000
    classDef displayStyle fill:#F1E8F8,stroke:#6A1B9A,stroke-width:4px,color:#000000
    classDef configStyle fill:#F8F8E8,stroke:#558B2F,stroke-width:4px,color:#000000
    
    %% Apply styles to components
    class GUI,Terminal uiStyle
    class PersonDetector,HOG,YOLO detectionStyle
    class CameraManager,OpenCV,FrameProc cameraStyle
    class VideoDisplay,StatsPanel,TimeOverlay,DetectionHist displayStyle
    class ConfigPy,Settings,Parameters configStyle
    
    %% Style subgraphs for better layer definition
    style UI fill:#E8F4FD,stroke:#1565C0,stroke-width:3px
    style Detection fill:#E8F8E8,stroke:#2E7D32,stroke-width:3px
    style Camera fill:#FFF8E1,stroke:#F57C00,stroke-width:3px
    style Display fill:#F1E8F8,stroke:#6A1B9A,stroke-width:3px
    style Config fill:#F8F8E8,stroke:#558B2F,stroke-width:3px
'''

# Create the well-spaced horizontal diagram with optimal dimensions
png_path, svg_path = create_mermaid_diagram(diagram_code, 'system_architecture.png', 'system_architecture.svg', width=1800, height=1000)

print(f"Optimized system architecture diagram saved as: {png_path} and {svg_path}")