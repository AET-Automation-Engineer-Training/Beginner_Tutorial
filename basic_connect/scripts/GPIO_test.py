#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

if __name__ == '__main__':
    try:
        while (True):
            x = GPIO.input(7)
            y = GPIO.input(13)
            z = GPIO.input(15)
            
            print(x)
            print(y)
            print(z)
        
    except rospy.ROSInterruptException:
        pass

