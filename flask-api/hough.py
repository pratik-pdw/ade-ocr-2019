import numpy as np
import cv2

img = cv2.imread('./uploads/Form.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Show gray image
# show_wait_destroy("gray", gray)
    # [gray]
    # [bin]
    
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
gray = cv2.bitwise_not(img)
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 15, -2)
    # Show binary image
# show_wait_destroy("binary", bw)
    # [bin]
    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
horizontal = np.copy(bw)
vertical = np.copy(bw)
    # [init]
    # [horiz]
    # Specify size on horizontal axis
cols = horizontal.shape[1]
horizontal_size = cols // 30
    # Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    # Apply morphology operations
horizontal = cv2.erode(horizontal, horizontalStructure)
horizontal = cv2.dilate(horizontal, horizontalStructure)
    # Show extracted horizontal lines
# show_wait_destroy("horizontal", horizontal)
    # [horiz]
    # [vert]
    # Specify size on vertical axis
rows = vertical.shape[0]
verticalsize = rows // 30
    # Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
vertical = cv2.erode(vertical, verticalStructure)
vertical = cv2.dilate(vertical, verticalStructure)
    # Show extracted vertical lines
    # show_wait_destroy("vertical", vertical)
    # [vert]
    # [smooth]
    # Inverse vertical image
vertical = cv2.bitwise_not(vertical)
    # show_wait_destroy("vertical_bit", vertical)
"""
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
"""
    # Step 1
edges = cv2.adaptiveThreshold(vertical, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 3, -2)
    # show_wait_destroy("edges", edges)
    # Step 2
kernel = np.ones((2, 2), np.uint8)
edges = cv2.dilate(edges, kernel)
    # show_wait_destroy("dilate", edges)
    # Step 3
smooth = np.copy(vertical)
    # Step 4
smooth = cv2.blur(smooth, (2, 2))
    # Step 5
(rows, cols) = np.where(edges != 0)
vertical[rows, cols] = smooth[rows, cols]
cv2.imshow('res', vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()