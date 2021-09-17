#!/usr/bin/env python3

import rospy
import random
from chatterbot.msg import temphum
from std_msgs.msg import String

def Temphum_talker():
    pub=rospy.Publisher("sensor",temphum,queue_size=10)
    rospy.init_node("Temp_talker",anonymous=True)
    rate=rospy.Rate(1)
    i=1

    while not rospy.is_shutdown():
        temp_hum=temphum()
        temp_hum.id=i
        temp_hum.patient="covid patient 00"+str(i)
        temp_hum.temperature=20+(random.random()*2)
        temp_hum.humidity=32.5+(random.random()*2)
        rospy.loginfo("I publish: ")
        rospy.loginfo(temp_hum)
        pub.publish(temp_hum)
        rate.sleep()
        i=i+1
    
if __name__ == '__main__':
    try:
        Temphum_talker()
    except rospy.ROSInterruptException:
        pass