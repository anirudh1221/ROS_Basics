#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def line():
    rospy.init_node("line_node", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    vel = Twist()
    d = float(input("Enter Distance to be travelled: "))
    move = 0
    v = float(input("Enter Linear Velocity: "))
    vel.linear.x = v
    t0 = rospy.Time.now().to_sec()
    rate = rospy.Rate(10)

    while (move <= d):
        t = rospy.Time.now().to_sec()
        move = v*(t-t0)
        pub.publish(vel)
        rate.sleep()

    vel.linear.x = 0
    pub.publish(vel)

if __name__ == '__main__':
    try: line()
    except rospy.ROSInterruptException:
        pass