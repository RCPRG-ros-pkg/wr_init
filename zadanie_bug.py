#!/usr/bin/env python
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from turtlesim.msg  import Pose
from sensor_msgs.msg import LaserScan
# funkcja wywolywana przy przyjsciu danych ze skanera laserowego
def scan_callback(scan):
	print scan


# funkcja wywolywana przy przyjsciu danych o lokalizacji robota
def odom_callback(odom):
	global new_vel
	pose = Pose()
	pose.x = odom.pose.pose.position.x
	pose.y = odom.pose.pose.position.y
	pose.theta = tf.transformations.euler_from_quaternion([odom.pose.pose.orientation.x,odom.pose.pose.orientation.y,odom.pose.pose.orientation.z,odom.pose.pose.orientation.w])[2]
	print "Pozycja x: ",odom.pose.pose.position.x
	print "Pozycja y: ",odom.pose.pose.position.y
	print "Pozycja theta: ",pose.theta
	new_vel.linear.x = 0.15
	new_vel.angular.z = 0.3

if __name__== "__main__":
	global new_vel
	new_vel = Twist()
	rospy.init_node('wr_zad', anonymous=True)
	print("ready")
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
	rospy.Subscriber( '/odom' , Odometry, odom_callback)
	rospy.Subscriber( '/scan' , LaserScan, scan_callback)
	
	rate=rospy.Rate(10) # 10Hz
	while not rospy.is_shutdown():
		pub.publish(new_vel)#wyslanie predkosci zadanej
		rate.sleep()

	print("END")
