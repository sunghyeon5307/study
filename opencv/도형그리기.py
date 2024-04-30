import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
# img[:]=(255,255,255) # 전체 공간을 흰 색으로 채우기
img[100:200, 200:300] = (255,255,255) # [세로영역, 가로영역]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()