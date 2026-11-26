import cv2
image = cv2.imread("image.jpg")
if image is not None:
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours = cv2.Canny(gris, 100, 200)
cv2.imshow("Contours", contours)
cv2.waitKey(0)
