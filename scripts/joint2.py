#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def joint2():
    pub = rospy.Publisher('/robot/right_joint_position_controller/joints/right_j2_controller/command', Float64, queue_size=20)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 20hz
    for i in range(10):
    	hello_str = 0.0
    	rospy.loginfo(hello_str)
    	pub.publish(hello_str)
    	rate.sleep()

if __name__ == '__main__':
    try:
        joint2()
    except rospy.ROSInterruptException:
        pass
