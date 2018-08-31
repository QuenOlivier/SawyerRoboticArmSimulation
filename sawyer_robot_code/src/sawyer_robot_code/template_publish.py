#!/usr/bin/env python

import rospy
from biotac_sensors.msg import BioTacHand
from sawyer_robot_code import python_class
#from <library> import <package>
#import <library>
#from <package>.msg import <message>

## \file template.py
# \brief A template script to help you get started
# \details It is prepared to use code from the sawyer_robot_code package. The comments are made in accordance to the Doxygen rules so that you simply have to replace this description by the one of your one making. Let this file in this folder to allow him to be imported like any Python library.

## \brief This is your main function
# \details This is where you will put your argument parseer lines and main code
def main():
	"""<Your file name>

	Short description of what this script does once launched in a terminal.

	To use this script, type in a terminal :
		rosrun sawyer_robot_code <your_script_name>
	"""

	##########################################
	# ARGUMENT PARSEER
	# Translate the arguments in the command line into arguments ready to be used in the code
	# Here, args.position after that bloc would be an int
	##########################################
	arg_fmt = argparse.RawDescriptionHelpFormatter
	parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
	parser.add_argument('-s', '--string', type=str, default="test",
        choices=['test','this_is_a_test'], help='This will be the explanation of the use for this option')
	parser.add_argument('-r', '--raw', action='store_true',
        help="This doesn't take argument")
	parser.add_argument('-p', '--position', type=int,
        help='Another example')
	parser.add_argument('-t', '--tab', type=int,
        nargs=2,help='A tab of 2 int')
	args = parser.parse_args(rospy.myargv()[1:])

	print "Initializing ROS node...\n\n"
	rospy.init_node("Main",anonymous=True)
	print "Doing stuff...\n"
	pub = rospy.Publisher('topic_name', message, queue_size=10)

	###########################################
	# Write your own code here
	###########################################

	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
	   pub.publish(your_data)
	   r.sleep()


## \brief these lines are simply made to check if this script was called in a terminal or imported 
if __name__ == '__main__':
	main()
