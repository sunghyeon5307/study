# 입력 이미지 or 영상에서 edge & contour를 이용해 차량 외곽 검출
# → 사각형으로 표시하고, “Car” 텍스트 추가하기

import cv2
import numpy as np
 
img1 = "img/car1.jpeg"
img2 = "img/car2.jpeg"
img3 = "img/car3.jpeg"

def detect_car(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    edges = cv2.Canny(gray, 100, 200)
    _, thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_contour = img.copy()
    cv2.drawContours(img_contour, contours, -1, (0, 255, 0), 1) 
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h > 5000: 
            cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img_contour, 'car', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 1, cv2.LINE_AA)
    return img_contour

for idx, img_path in enumerate([img1, img2, img3]):
    cv2.imwrite(f'cannyEdge{idx}.jpeg', detect_car(img_path))
    cv2.imshow(f'canny Edges{idx}', detect_car(img_path))

cv2.waitKey(0)
cv2.destroyAllWindows()
