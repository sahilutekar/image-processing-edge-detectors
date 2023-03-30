import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/sahil/Desktop/Image_matching/doraemon.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the Canny algorithm to detect edges
canny_edges = cv2.Canny(blur, 50, 150)
cv2.imshow("canny_edges", canny_edges)

# Apply the Sobel operator to detect edges
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=0)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=0)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)
cv2.imshow("sobel_edges", sobel_edges)



# Apply the Laplacian operator to detect edges
laplacian_edges = cv2.Laplacian(blur, cv2.CV_64F)
cv2.imshow("laplacian_edges", laplacian_edges)



# Display the original image 
cv2.imshow("Original Image", img)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
