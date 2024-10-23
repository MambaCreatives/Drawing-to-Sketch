import cv2


img = cv2.imread('mamba.jpg')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


inverted_image = 255 - gray_image


blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)


inverted_blurred_image = 255 - blurred_image


sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)


cv2.imwrite('sketch_image.jpg', sketch_image)
cv2.imshow('Pencil Sketch', sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
