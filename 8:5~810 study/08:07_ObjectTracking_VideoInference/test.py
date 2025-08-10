from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

video=cv2.VideoCapture('videos/drive.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break

    results = model.predict(source=frame, save=False, verbose=False)

    # 결과 시각화
    annotated_frame = results[0].plot()

    # 화면에 출력
    cv2.imshow('YOLOv8 Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()