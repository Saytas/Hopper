#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

class RobotControl():
  def __init__(self):
    rospy.init_node('rotate_robot_node', anonymous=True)
    self.vel_publisher = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
    self.cmd = Twist()
    self.ctrl_c = False
    self.rate = rospy.Rate(10)
    rospy.on_shutdown(self.shutdownhook)

  def publish_once_in_cmd_vel(self):
    """
    This is because publishing in topics sometimes fails the first time you publish.
    In continuous publishing systems, this is no big deal, but in systems that publish only once, it is very important.
    """
    while not self.ctrl_c:
      connections = self.vel_publisher.get_num_connections()
      if connection > 0:
        self.vel_publisher.publish(self.cmd)
        break
      else:
        self.rate.sleep()

  def shutdownhook(self):
    self.stop_robot()
    self.ctrl_c = True

  def stop_robot(self):
    rospy.loginfo("Shutdown time! Stop the robot")
    self.cmd.linear.x = 0.0
    self.cmd.angular.z = 0.0
    self.publish_once_in_cmd_vel()

  def get_inputs_rotate(self):
    self.angular_speed_d = int(raw_input('Enter desired angular speed (in degrees): '))
    self.angle_d = int(raw_input('Enter desired angle (in degrees): '))
    clockwise_yn = raw_input('Do you want to rotate clockwise: (y/n): ')
    if clockwise_yn == 'y':
      self.clockwise = True
    if clockwise_yn == 'n':
      self.clockwise = False

    return [self.angular_speed_d, self.angle_d]

  def convert_degree_to_rad(self, speed_deg, angle_deg):
    self.angular_speed_r = speed_deg * 3.14 / 180
    self.angle_r = angle_deg * 3.14 / 180
    return [self.angular_speed_r, self.angle_r]

  def rotate(self):
    # Initialize velocities
    self.cmd.linear.x = 0.0
    self.cmd.linear.y = 0.0
    self.cmd.linear.z = 0.0
    self.cmd.angular.x = 0.0
    self.cmd.angular.y = 0.0

    # Convert speed and angle to radians
    speed_d, angle_d = self.get_inputs_rotate()
    self.convert_degree_to_rad(speed_d, angle_d)

    # Check the direction of the rotation
    if self.clockwise:
      self.cmd.angular.z = -abs(self.angular_speed_r)
    else:
      self.cmd.angular.z = abs(self.angular_speed_r)

    # t0 is the current time
    t0 = rospy.Time.now().secs

    current_angle = 0

    # Loop to publish the velocity estimate, current_distance = velocity * (t1 - t0)
    while (current_angle < self.angle_r):
      # Publish the velocity
      self.vel_publisher.publish(self.cmd)
      # t1 is the current time
      t1 = rospy.Time.now().secs
      # Calculate the current angle
      current_angle = self.angular_speed_r * (t1 - t0)
      self.rate.sleep()

    # Set velocity to zero to stop the robot
    # self.stop_robot()

if __name__ == '__main__':
  robot_control_object = RobotControl()
  try:
    res = robot_control_object.rotate()
  except rospy.ROSInterruptException:
    pass
