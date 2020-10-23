import cv2

img = cv2.imread("./docs/swagger.png")

cv2.imwrite('./docs/swagger.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])