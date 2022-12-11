#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def data(msg):
    data = msg.data
    X = data.split()
    tam_y = X[1]
    tam_x = X[0]
    rospy.loginfo(rospy.get_caller_id() + ' data color=%s', data)
    if (int(tam_x) > 350):
       cmd("right")
    elif (int(tam_x) < 290):
       cmd("left")
    else :
       cmd("stop")

def cmd(msg):
    pub = rospy.Publisher('/jetbot_motors/cmd_str', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    pub.publish(msg)

if __name__ == '__main__' :
    try:
      rospy.init_node('control_motor_color')
      rospy.Subscriber('~data', String, data)
      rospy.spin()
    except rospy.ROSInterruptException:
        pass
