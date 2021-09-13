#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def spiral():
    rospy.init_node("circle1",anonymous=True)
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    
    rate=rospy.Rate(1)
    velocity=Twist()
    r = float(input("Enter Radius: "))
    v = float(input("Enter Linear Velocity: "))
    while not rospy.is_shutdown():
        r=r+0.2
        velocity.linear.x=v
        velocity.angular.z=v/r
        pub.publish(velocity)
        rate.sleep()
        
if __name__ == '__main__':
    try: spiral()
    except rospy.ROSInterruptException:
        pass