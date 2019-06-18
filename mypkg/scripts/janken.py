#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import random
import time
from std_msgs.msg import Int32
rospy.init_node('janken')
pub = rospy.Publisher('janken_up', Int32, queue_size= 1)
rate = rospy.Rate(10)



while not rospy.is_shutdown():
    user_choice = input('三つから選んでください　グー(0) チョキ(1) パー(2) :')
    pub.publish(user_choice)
    rate.sleep()
