from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.track(
    source="videos/drive.mp4",  
    tracker="bytetrack.yaml",   
    show=True,              
    persist=True                
)