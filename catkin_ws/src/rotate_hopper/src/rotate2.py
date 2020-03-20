#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def rotate():
    # Starts a new node
    rospy.init_node('rotate2_hopper_node')
    
    # pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    # Use '/cmd_vel_mux/input/navi' for TurtleBot2
    #pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size = 1)

    # Use '/mobile_base/commands/velocity' topic for Kobuki base
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)
    rate = rospy.Rate(2)
    rotate = Twist()

    rotate.angular.z = 0.5

    while not rospy.is_shutdown():
        pub.publish(rotate)
        rate.sleep()


if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptExcepiton:
        pass
