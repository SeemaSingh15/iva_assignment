import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../images/t_pyramid_sample.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 


layer1 = cv2.pyrDown(img)  
layer2 = cv2.pyrDown(layer1) 
layer3 = cv2.pyrDown(layer2)  


plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Level 1 (Half Size)')
plt.imshow(layer1)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Level 2 (Quarter Size)')
plt.imshow(layer2)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Level 3 (Eighth Size)')
plt.imshow(layer3)
plt.axis('off')

plt.show()
