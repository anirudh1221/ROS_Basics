#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
global j
j=True
def callback(data):
    if data.data=="hello world_10":
        global j
        j=False

    rospy.loginfo("I heard %s",data.data)
    
def listener():
    rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber("chatter1", String, callback)
    rate=rospy.Rate(1)
   
    while not rospy.is_shutdown() and j:
        rate.sleep()
    
if __name__ == '__main__':
    listener()