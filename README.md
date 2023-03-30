# image-processing-edge-detectors

This code demonstrates how to detect edges using various edge detection algorithms in OpenCV library. The following algorithms are used in this code:

    Canny Edge Detection Algorithm: This algorithm is used to detect a wide range of edges in an image. The Canny algorithm uses a multi-stage process to detect edges that include noise reduction, finding the intensity gradient of the image, applying non-maximum suppression to get thin edges, and finally, applying hysteresis to eliminate false edges.

    Sobel Operator: This operator is used to detect edges by calculating the gradient of the image intensity function. It performs a 2D spatial gradient measurement on an image and emphasizes regions with high spatial frequency. The Sobel operator can detect edges in both horizontal and vertical directions.

    Laplacian Operator: This operator is used to detect edges by measuring the second derivative of an image intensity function. It detects edges by looking for zero crossings in the second derivative of the image. The Laplacian operator is a simple and effective way to detect edges in an image.

The code loads an image and converts it to grayscale. Gaussian blur is applied to the image to reduce noise. The Canny, Sobel, and Laplacian edge detection algorithms are applied to the blurred image, and the resulting edges are displayed in separate windows. Finally, the original image is displayed.

To run this code, you will need to have OpenCV installed on your machine. You can install OpenCV using pip or conda. You will also need an image file that you want to use for edge detection. Make sure to update the image file path in the code to the correct path on your machine.





Code Exlpain 
Sure, here's an explanation of the code:
1.	Import the necessary libraries:
import cv2
import numpy as np
The OpenCV (cv2) library is used for image processing operations, while the NumPy (np) library is used for numerical operations on arrays.
2.	Load the image:
img = cv2.imread("C:/Users/sahil/Desktop/Image_matching/doraemon.png")
The imread() function reads the image from the specified file path and stores it in the img variable.
3.	Convert the image to grayscale:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
The cvtColor() function is used to convert the image from one color space to another. Here, we convert the image from the default BGR color space to grayscale.
4.	Apply Gaussian blur to the image to reduce noise:
blur = cv2.GaussianBlur(gray, (5, 5), 0)
The GaussianBlur() function applies a Gaussian blur filter to the image, which helps to reduce noise and smooth out the edges.
5.	Apply the Canny algorithm to detect edges:
canny_edges = cv2.Canny(blur, 50, 150)
cv2.imshow("canny_edges", canny_edges)
The Canny() function is used to detect edges in the image using the Canny algorithm. The function takes two threshold values as inputs, which are used to determine which edges to keep and which to discard.
6.	Apply the Sobel operator to detect edges:
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=0)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=0)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)
cv2.imshow("sobel_edges", sobel_edges)
The Sobel() function is used to detect edges in the image using the Sobel operator. The function calculates the gradient of the image in the x and y directions, which are then combined using the magnitude() function to produce the final edge map.
7.	Apply the Laplacian operator to detect edges:
laplacian_edges = cv2.Laplacian(blur, cv2.CV_64F)
cv2.imshow("laplacian_edges", laplacian_edges)
The Laplacian() function is used to detect edges in the image using the Laplacian operator. The function calculates the second derivative of the image, which highlights the areas of high intensity variation.
8.	Display the original image:
cv2.imshow("Original Image", img)
The imshow() function is used to display the original image in a window with the specified title.
9.	Wait for a key press and then close the windows:
cv2.waitKey(0)
cv2.destroyAllWindows()
The waitKey() function waits for a key press before closing the windows, while the destroyAllWindows() function closes all open windows.

