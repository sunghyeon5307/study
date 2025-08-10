from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 또는 best.pt
model.track(
    source="videos/drive.mp4",  # 영상 경로
    tracker="bytetrack.yaml",   # 기본값이라 생략 가능
    show=True,                  # 영상 창 표시
    persist=True                # 같은 영상 내 ID 유지
)
