import cv2 

img = cv2.imread('도도.jpeg', cv2.IMREAD_COLOR)
img2 = cv2.imread('도도.jpeg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('도도.jpeg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.IMREAD_COLOR: 컬리이미지, 투명 영역은 무시(기본값)
# cv2.IMREAD_GRAYSCALE: 흑백이미지
# cv2.IMREAD_UNCHANGED: 투명 영역까지 포함

