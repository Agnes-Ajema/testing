import cv2
import numpy as np

# Create a blank image (black image)
image = np.zeros((300, 300, 3), dtype=np.uint8)

# Add some text to the image (optional)
cv2.putText(image, 'Hello OpenCV!', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image in a window
cv2.imshow('Test Window', image)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
