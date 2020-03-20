#! /usr/bin/env python

import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = pitch = yaw = 0.0

target = 90
kP = 0.5

def get_rotation(msg):
  global roll, pitch, yaw
  orientation_quaternion = msg.pose.pose.orientation
  orientation_list = [orientation_quaternion.x,
                      orientation_quaternion.y,
                      orientation_quaternion.z,
                      orientation_quaternion.w]
  (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
  # In radians
  #print yaw

rospy.init_node('rotate_from_quaternions_to_euler_angles_node')
sub = rospy.Subscriber('/odom', Odometry, get_rotation)

pub = rospy.Publisher('/mobile_base/commands/velocity',Twist, queue_size = 2)
rate = rospy.Rate(10)

command = Twist()

while not rospy.is_shutdown():
  # quat = quaternion_from_euler(roll, pitch, yaw)
  # print quat
  target_rad = target * (math.pi/180)
  command.angular.z = kP * (target_rad - yaw)
  pub.publish(command)
  print("Target = {}	Current Yaw = {}".format(target_rad,yaw))
  rate.sleep()


# Control the robot using yaw value instead of using teleop

