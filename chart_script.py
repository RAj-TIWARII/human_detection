# Create mermaid flowchart for person detection system
diagram_code = """
flowchart TD
    start([Start Application])
    init[Initialize Camera<br/>& Detector]
    capture[Capture Frame<br/>from Camera]
    detect[Detect Persons<br/>HOG/YOLO]
    draw[Draw Bounding Boxes<br/>& Labels]
    display[Show Annotated<br/>Frame]
    stats[Update Person Count<br/>& Statistics]
    time[Add Current Time<br/>Overlay]
    continue{Continue?}
    stop([Stop Application<br/>& Release Camera])
    
    start --> init
    init --> capture
    capture --> detect
    detect --> draw
    draw --> time
    time --> display
    display --> stats
    stats --> continue
    continue -->|Yes| capture
    continue -->|No| stop
    
    classDef setup fill:#4A90E2,stroke:#333,stroke-width:2px,color:#fff
    classDef processing fill:#7ED321,stroke:#333,stroke-width:2px,color:#fff
    classDef display fill:#F5A623,stroke:#333,stroke-width:2px,color:#fff
    classDef stop fill:#D0021B,stroke:#333,stroke-width:2px,color:#fff
    classDef decision fill:#BD10E0,stroke:#333,stroke-width:2px,color:#fff
    
    class init setup
    class capture,detect,draw,stats processing
    class display,time display
    class stop stop
    class continue decision
"""

# Create the mermaid diagram
png_path, svg_path = create_mermaid_diagram(diagram_code, 'person_detection_flowchart.png', 'person_detection_flowchart.svg')
print(f"Flowchart saved as PNG: {png_path}")
print(f"Flowchart saved as SVG: {svg_path}")