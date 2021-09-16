#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist
global pi 
pi=3.14
def circle():
    rospy.init_node("circle1",anonymous=True)
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate=rospy.Rate(10)
    velocity=Twist()
    r = float(input("Enter Radius: "))
    v = float(input("Enter Linear Velocity: "))
    d=2*pi*r
    dist=0
    t0 = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and dist<d:
        t = rospy.Time.now().to_sec()
        dist= v*(t-t0)
        velocity.linear.x=v
        velocity.angular.z=v/r
        pub.publish(velocity)
        rate.sleep()
if __name__ == '__main__':
    try: circle()
    except rospy.ROSInterruptException:
        pass