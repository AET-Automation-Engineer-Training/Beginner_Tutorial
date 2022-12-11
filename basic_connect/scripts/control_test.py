#!/usr/bin/env python

# Simple demo that published std_msgs/Strings messages
# to the '/jetbot_motors/cmd_str' topic

import rospy
from time import sleep
from std_msgs.msg import String

def cmd(msg):
    pub = rospy.Publisher('/jetbot_motors/cmd_str', String, queue_size=10)

    rospy.init_node('sender')
    rate = rospy.Rate(10)  # 10hz
    pub.publish(String(msg))


if __name__ == '__main__':
    try:
        cmd("forward")
        sleep(5)
        cmd("stop")
        sleep(2)

        cmd("right")
        sleep(1)
        cmd("stop")
        sleep(2)

        cmd("forward")
        sleep(5)
        cmd("stop")
        sleep(2)
    except rospy.ROSInterruptException:
        pass

