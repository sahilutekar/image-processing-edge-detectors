# image-processing-edge-detectors

This code demonstrates how to detect edges using various edge detection algorithms in OpenCV library. The following algorithms are used in this code:

    Canny Edge Detection Algorithm: This algorithm is used to detect a wide range of edges in an image. The Canny algorithm uses a multi-stage process to detect edges that include noise reduction, finding the intensity gradient of the image, applying non-maximum suppression to get thin edges, and finally, applying hysteresis to eliminate false edges.

    Sobel Operator: This operator is used to detect edges by calculating the gradient of the image intensity function. It performs a 2D spatial gradient measurement on an image and emphasizes regions with high spatial frequency. The Sobel operator can detect edges in both horizontal and vertical directions.

    Laplacian Operator: This operator is used to detect edges by measuring the second derivative of an image intensity function. It detects edges by looking for zero crossings in the second derivative of the image. The Laplacian operator is a simple and effective way to detect edges in an image.

The code loads an image and converts it to grayscale. Gaussian blur is applied to the image to reduce noise. The Canny, Sobel, and Laplacian edge detection algorithms are applied to the blurred image, and the resulting edges are displayed in separate windows. Finally, the original image is displayed.

To run this code, you will need to have OpenCV installed on your machine. You can install OpenCV using pip or conda. You will also need an image file that you want to use for edge detection. Make sure to update the image file path in the code to the correct path on your machine.
