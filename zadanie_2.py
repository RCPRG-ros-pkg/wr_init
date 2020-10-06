#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from turtlesim.msg  import Pose
from sensor_msgs.msg import LaserScan
import turtlesim

def turtlesim_pose_callback(data):
        global new_vel
        pose = turtlesim.msg.Pose()
        pose.x = data.x
        pose.y = data.y
        pose.theta = data.theta
        print "Pozycja x: ",pose.x
        print "Pozycja y: ",pose.y
        print "Pozycja theta: ",pose.theta
        new_vel.linear.x = 0.15
        new_vel.angular.z = 0.3

if __name__== "__main__":
	global new_vel
	new_vel = Twist()
	rospy.init_node('wr_zad', anonymous=True)
	print("ready")
        rospy.Subscriber( '/turtle1/pose' , turtlesim.msg.Pose, turtlesim_pose_callback)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

	rate=rospy.Rate(10) # 10Hz
	while not rospy.is_shutdown():
		pub.publish(new_vel)#wyslanie predkosci zadanej
		rate.sleep()

	print("END")
