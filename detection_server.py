#!/usr/bin/env python

# WS server example

import cv2
import asyncio
import websockets
import numpy as np

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


async def detect_objects_server(websocket, path):
    frame = await websocket.recv()
    print(len(frame))
    frame = np.frombuffer(frame, dtype=np.uint8)
    original_image = np.reshape(frame, (240, 424, 3))
    # resized_image = cv2.resize(frame, (416, 416))

    # We resize the image to the input width and height of the first layer of the network.
    resized_image = cv2.resize(original_image, (m.width, m.height))

    # Detect objects in the image
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)

    # Plot the image with bounding boxes and corresponding object class labels
    frame = plot_boxes(original_image, boxes, class_names, plot_labels=True)

    cv2.imshow('Video window', frame)

    # press 'q' on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pass
    message = "next, please"
    await websocket.send(message)


start_server = websockets.serve(detect_objects_server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

