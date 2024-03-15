# Day 6(10-03-2024)
# Image Resizer using python

import cv2

image = cv2.imread("ex.jpg") # reading the normal image
scale_percent = 50 # scale percentage

# If we want to make it grayscale image
# image = cv2.imread("ex.jpg",cv2.IMREAD_GRAYSCALE)

# display the image
# cv2.imshow("A girl reading the book", image)

# new width and the new height
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# resizeing the image
output = cv2.resize(image, (new_width, new_height))

# save the new image with the given name
cv2.imwrite("newImage.png", output)

# wait for the user to press key
cv2.waitKey(0)