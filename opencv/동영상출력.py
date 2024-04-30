import cv2

cap = cv2.VideoCapture('aa.mp4')
while cap.isOpened():
    ret, frame = cap.read() # ret: 성공여부, frame: 받아온 이미지
    if not ret:
        print('프레임없음')
        break
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release() # 자원 해체
cv2.destroyAllWindows()
