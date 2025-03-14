import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('../images/color_sample.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to HSV (better for color range detection)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Define color ranges (example: red color)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create a mask for red color
mask = cv2.inRange(hsv, lower_red, upper_red)

# Apply the mask to the image
result = cv2.bitwise_and(img, img, mask=mask)

# Display the results
plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Red Color Mask')
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Detected Red Areas')
plt.imshow(result)
plt.axis('off')

plt.show()
