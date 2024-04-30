# cv2.LINE_4: 상하좌우 4방향으로 연결된 선
# cv2.LINE_8: 대각선을 포함한 8방향으로 연결된 선 (기본값)
# cv2.LINE_AA: 부드러운 선

import cv2
import numpy as np

img=np.zeros((480, 640, 3), dtype=np.uint8)

color = (0, 255, 255) 
thickness = 3 # 두께

cv2.line(img, (50, 100), (400, 50), color, thickness, cv2.LINE_8)
cv2.line(img, (50, 200), (400, 150), color, thickness, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 250), color, thickness, cv2.LINE_AA)
# 그릴위치, 시작 점, 끝 점, 색깔, 두께, 선 종류

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()