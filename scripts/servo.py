#!/usr/bin/python

import rospy
import time
import maestro
servo = maestro.Controller()

from FactoryOS.msg import servo


def servo_callback(msg):

	servo.setAccel(0,msg.accel)
	servo.setSpeed(0,msg.speed)
	servo.setTarget(0,msg.target)

	curr_servo = servo_msg()
	curr_servo.pos = servo.getPosition(0)
	servo_pub.publish(curr_servo)


rospy.init_node('servo_node')
servo_pub = rospy.Publisher('/MC1/servo1/CurrPos', servo_msg, queue_size=1)
rospy.Subscriber('/MC1/servo1/ToMove', servo_msg, servo_callback)
rospy.spin()
	