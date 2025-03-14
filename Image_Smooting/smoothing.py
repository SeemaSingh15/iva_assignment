import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('../images/smoothing_sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply different smoothing techniques
blur = cv2.GaussianBlur(img, (15, 15), 0)  # Gaussian Blur
median = cv2.medianBlur(img, 15)  # Median Blur
bilateral = cv2.bilateralFilter(img, 15, 75, 75)  # Bilateral Filter

# Display the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(blur)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Median Blur')
plt.imshow(median)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Bilateral Filter')
plt.imshow(bilateral)
plt.axis('off')

plt.show()
