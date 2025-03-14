import cv2

# Load Haar Cascade classifiers from OpenCV's pre-installed directory
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# ✅ Debugging: Check if cascades are loading properly
if face_cascade.empty():
    print("⚠️ Failed to load face cascade!")
if eye_cascade.empty():
    print("⚠️ Failed to load eye cascade!")
if smile_cascade.empty():
    print("⚠️ Failed to load smile cascade!")

# Read the image
img = cv2.imread('../images/object_sample.jpeg')

# ✅ Debugging: Check if the image is loading correctly
if img is None:
    print("⚠️ Failed to load image!")
else:
    print(f"✅ Image loaded successfully. Shape: {img.shape}")

# ✅ Resize the image for better detection
img = cv2.resize(img, (600, 800))  # Increased size for better detail

# ✅ Reduce blur strength for fine details
img = cv2.GaussianBlur(img, (3, 3), 0)

# Convert to grayscale for better accuracy
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ✅ Face Detection (Final Parameters)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=2)
print(f"✅ Faces detected: {len(faces)}")

# ✅ Draw a rectangle around the detected face(s)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Blue for face

    # ✅ Resize the ROI for better eye/smile detection
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # ✅ Eye Detection (Even More Flexible Parameters)
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.02, minNeighbors=1)  
    print(f"✅ Eyes detected: {len(eyes)}")
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)  # Green for eyes
    
    # ✅ Smile Detection (Final Parameters)
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=10)
    print(f"✅ Smiles detected: {len(smiles)}")
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 255, 0), 2)  # Yellow for smile

# ✅ Show the result directly using OpenCV
cv2.imshow("Face, Eye, and Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
