#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter1', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    i=1
    while not rospy.is_shutdown() and i<=10:
        hello_str = "hello world_"+str(i)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        i=i+1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass