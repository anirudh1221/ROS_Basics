#!/usr/bin/env python3

import rospy
from chatterbot.msg import temphum
from std_msgs.msg import String

def Temp_hum_callback(temp_hum_message):
    rospy.loginfo("The data recieved : (%d, %s, %.2f ,%.2f)", 
        temp_hum_message.id,temp_hum_message.patient,
        temp_hum_message.temperature,temp_hum_message.humidity)

def temp_hum_listener():
    rospy.init_node('Temp_receiver', anonymous=True)
    rospy.Subscriber("sensor", temphum,Temp_hum_callback)
    rospy.spin()

if __name__ == '__main__':
    temp_hum_listener()