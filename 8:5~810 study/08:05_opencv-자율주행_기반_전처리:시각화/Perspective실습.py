import cv2
import numpy as np

img_path = 'img/기운도라에몽.jpg'
img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {img_path}")

points = []

def select_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point {len(points)}: ({x}, {y})")
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select 4 Points", img)

cv2.imshow("Select 4 Points", img)
cv2.setMouseCallback("Select 4 Points", select_point)
cv2.waitKey(0)
cv2.destroyAllWindows()

src_points = np.float32(points)
dst_points = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])

M = cv2.getPerspectiveTransform(src_points, dst_points)
warped = cv2.warpPerspective(cv2.imread(img_path), M, (400, 400))

cv2.imshow("Warped Image", warped)
cv2.imwrite("Warped_Image.jpg", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
