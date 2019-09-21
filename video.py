# import cv2
# import time

from utils import *
from darknet import Darknet

# Load the network architecture
m = Darknet('./cfg/yolov3.cfg')

# Load the pre-trained weights
m.load_weights('./weights/yolov3.weights')

# Load the COCO object classes
class_names = load_class_names('data/coco.names')

# Set the NMS threshold
nms_thresh = 0.6

# Set the IOU threshold
iou_thresh = 0.4

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, m.width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, m.height)
while True:
    ret, frame = cap.read()

    original_image = frame

    # We resize the image to the input width and height of the first layer of the network.
    resized_image = cv2.resize(original_image, (m.width, m.height))

    # Detect objects in the image
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)

    # Plot the image with bounding boxes and corresponding object class labels
    frame = plot_boxes(original_image, boxes, class_names, plot_labels=True)

    cv2.imshow('Video window', frame)

    # press 'q' on keyboard to exit
    # this call is necessary in order rendering to work.
    # Returns control to event loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
