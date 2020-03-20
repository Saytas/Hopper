#! /usr/bin/env python

import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = pitch = yaw = 0.0

def get_rotation(msg):
  global roll, pitch, yaw
  orientation_quaternion = msg.pose.pose.orientation
  orientation_list = [orientation_quaternion.x,
                      orientation_quaternion.y,
                      orientation_quaternion.z,
                      orientation_quaternion.w]
  (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
  # In radians
  print yaw

rospy.init_node('rotate_from_quaternions_to_euler_angles_node')
sub = rospy.Subscriber('/odom', Odometry, get_rotation)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
  quat = quaternion_from_euler(roll, pitch, yaw)
  print quat
  rate.sleep()
