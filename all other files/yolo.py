from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image

# Load YOLOv8 model
model = YOLO('yolov8s.pt')  # You can use 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'

# Load an image
img = Image.open('cars.jpg')

# Perform inference
results = model(img)

# Print results
print(results)  # Print results to the console

# Display the image with bounding boxes
plt.imshow(results[0].plot())
plt.show()

# Save the image with bounding boxes
results[0].save('path/to/save')
