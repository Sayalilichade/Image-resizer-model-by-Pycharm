import cv2

#configurable parameters
source= "money.jpg"
destination = "newImage.jpg"
scale_percent = 50

src = cv2.imread("money.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)

#percent by which image is resized
scale_percent = 50

#calculate the 50 percent of origional dinensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

#resize image
output = cv2.resize(src, (width, height))

cv2.imwrite(destination, output)
cv2.waitKey(0)