import cv2

# Step 1: Read the image
img = cv2.imread("input.jpg")   # make sure input.jpg is in same folder

# Step 2: Rotate the image (90 degrees clockwise)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Step 3: Adjust brightness (increase by 50)
# cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)  

# Step 4: Save results
cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("bright.jpg", bright)

# Step 5: Show results (optional)
cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.imshow("Brightened", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()
