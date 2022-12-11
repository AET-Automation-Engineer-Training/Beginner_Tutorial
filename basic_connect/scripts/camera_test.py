#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from std_msgs.msg import String

GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=30/1 ! nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'

def cameraOpenTest():

    # Video Capturing class from OpenCV		
    video_capture = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
    if video_capture.isOpened():
        cv2.namedWindow("Camera demo Window", cv2.WINDOW_AUTOSIZE)

        while True:
            return_key, imageFrame = video_capture.read()
           # imageFrame = imageFrame[50:430, 100:540]
            if not return_key:
                break

            cv2.imshow("Camera demo Window", imageFrame)

            key = cv2.waitKey(30) & 0xff
            # Stop the program on the ESC key
            if key == 27:
                break

        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Cannot open Camera")

if __name__ == "__main__":
    cameraOpenTest()
    
