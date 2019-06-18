#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import random
from std_msgs.msg import Int32

def main(message):
    ms = message.data
    sys = random.randrange(3)
    if ms == 0:
        if sys == 1:
            print('you:グ-  pc:チョキ')
            print('you win')
        elif sys ==2:
            print('you:グ-  pc:パー')
            print('you lose')
        else:
            print('you:グ-  pc:グー')
            print('drow')
    elif ms == 1:
        if sys == 2:
            print('you:チョキ  pc:パー')
            print('you win')
        elif sys ==0:
            print('you:チョキ  pc:グー')
            print('you lose')
        else:
            print('you:チョキ  pc:チョキ')
            print('drow')
    elif ms == 2:
        if sys == 0:
            print('you:パー  pc:グー')
            print('you win')
        elif sys ==1:
            print('you:パー  pc:チョキ')
            print('you lose')
        else:
            print('you:パー  pc:パー')
            print('drow')

    else:
        print('retry')


if __name__ == '__main__':
    rospy.init_node('judg')
    sub = rospy.Subscriber('janken_up', Int32, main)
    rospy.spin()

