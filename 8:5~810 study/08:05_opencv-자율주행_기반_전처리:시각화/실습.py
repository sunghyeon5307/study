import cv2
import numpy as np

img = 'img/기운도라에몽.jpg'
img = cv2.imread(img)

# 1. 이미지 읽고 출력
cv2.imshow('도라에몽', img)
cv2.imwrite('도라에몽복제하기.jpg', img)


# 2. 색공간 변환
rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('RGB.jpg', rgb)
cv2.imwrite('HSV.jpg', hsv)
cv2.imwrite('GRAY.jpg', gray)

cv2.imshow('RGB', rgb)
cv2.imshow('HSV', hsv)
cv2.imshow('GRAY', gray)


# 3. 블러 처리
blur=cv2.GaussianBlur(img, (35, 35), 0)
median=cv2.medianBlur(img, 15)

cv2.imwrite('GaussianBlur.jpg', blur)
cv2.imwrite('MedianBlur.jpg', median)    

cv2.imshow('GaussianBlur', blur)
cv2.imshow('MedianBlur', median)


# 4. 이진화(threshold): 흑/백 (0, 255)로 변환
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('Threshold.jpg', thresh)
cv2.imwrite('AdaptiveThreshold.jpg', adaptive)
cv2.imshow('Threshold', thresh)
cv2.imshow('Adaptive Threshold', adaptive)


# 5. Canny 엣지: 윤곽선 추출
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imwrite('CannyEdges.jpg', edges)
cv2.imshow('Canny Edges', edges)


# 6. Contour 추출/그리기: 외곽선을 좌표로 추출
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_contour = img.copy()
cv2.drawContours(img_contour, contours, -1, (0, 255, 0), 2)

cv2. imwrite('Contours.jpg', img_contour)
cv2.imshow('Contours', img_contour)


# 7. 도형 및 텍스트 그리기
draw = img.copy()
cv2.rectangle(draw, (50, 50), (200, 200), (255, 0, 0), -1)
cv2.circle(draw, (400, 300), 100, (0, 255, 0), -1)
cv2.putText(draw, 'hello', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)

cv2.imshow('draw', draw)


# 8. 동영상 프레임 처리
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()