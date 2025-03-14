import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('../images/edge_sample.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale (edge detection works better in grayscale)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply Sobel Edge Detection (X and Y directions)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Apply Canny Edge Detection
canny = cv2.Canny(gray, 100, 200)

# Display the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Sobel X')
plt.imshow(sobel_x, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Sobel Y')
plt.imshow(sobel_y, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Canny Edges')
plt.imshow(canny, cmap='gray')
plt.axis('off')

plt.show()
