# YOLO-Object-Detection
YOLO is a state-of-the-art, real-time object detection algorithm. In this notebook, we will apply the YOLO algorithm to detect objects in images.
darknet prints out the objects it detected, its confidence, and how long it took to find them. We didn't compile Darknet with OpenCV so it can't display the detections directly. Instead, it saves them in predictions.png. You can open it to see the detected objects. Since we are using Darknet on the CPU it takes around 6-12 seconds per image. If we use the GPU version it would be much faster.


How to run:

1. Open Jupter Notebook in your browser
2. Open the folder containing this folder
3. Run YOLO.ipynb

# Send video screen capture from Unity to the YOLO code

1. In Unity, create a project
2. In Unity, attach `unity_scripts/ScreenRecorder.cs` to the "Main Camera" GameObject (for details, see https://docs.unity3d.com/Manual/CreatingAndUsingScripts.html)
3. Open a terminal window and run `python detection_server.py`
4. In Unity, click on the "Play" button
5. You should see a window open with the video screen capture with some bounding boxes and labels identifying objects in the Unity scene