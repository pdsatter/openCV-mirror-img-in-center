import cv2
from numpy import half

img = cv2.imread('assets/github.png', 1) # load img
img = cv2.resize(img, (0,0), fx=4, fy=4) # makes img 4 times bigger

# get top half of image
[height, width, depth] = img.shape

if (height == 0 or width == 0):
    raise ValueError('Img has a dimension of 0, input actual img')

print("height:", height)
print("width:", width)
print("depth:", depth) # rgb, so will always be 3 (in openCV it's actually bgr)

halfheight = 0

# Calculate half img height
# This could be done skipped and just calculated when needed
# But for readability I will calculate here
if (height%2 == 0):
    halfheight = height/2
else: halfheight = int(height/2)  # 5/2 = 2.5 -> 2

if (height%2 == 0):
    halfheight = int(height/2)
else: halfheight = int(height/2)


# Set top half and mirror "tophalf"
tophalf = img[0:halfheight, 0:width]  # copies tophalf of "img" into "tophalf"
tophalf = cv2.flip(tophalf, 0) # mirror on y axis

# Add "tophalf" back onto "img"
img[height-halfheight:height, 0:width] = tophalf   # adds "tophalf" onto bottom half of "img"

cv2.imwrite('assets/mirrored-github.png', img)
cv2.imshow('Mirrored github', img)
cv2.waitKey(0)
cv2.destroyAllWindows() # close windows


# Made my pdsatter
# 5/22/2022