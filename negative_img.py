import cv2
import numpy as np
import matplotlib.pyplot as plt

def negative_image(image_name):
    # Read image
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    
    # Create negative image
    negative_img = 255 - img
    
    # Plot original image
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Grayscale Image')
    
    # Plot negative image
    plt.subplot(1, 2, 2)
    plt.imshow(negative_img, cmap='gray')
    plt.title('Negative Grayscale Image')

    plt.show()

# Provide just the image name
image_name = 'abc.jpg'
# Call the function
negative_image(image_name)
