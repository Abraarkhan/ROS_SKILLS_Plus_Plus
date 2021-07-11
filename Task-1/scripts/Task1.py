#!/usr/bin/env python
"""This  script makes the turtle revolve in a circle by adding linear and angular velocity.
It also makes it stop when it has completed one turn"""

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
k = 10  # to store theta value

def pose_callback(msg):
    """This function returns the theta value of turtle at any instant"""
    global k
    k = msg.theta

def main():
    """This is the main function"""
    global k
    rospy.init_node('node_turtle_revolve', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    var_loop_rate = rospy.Rate(4)

    vel_msg.linear.x = 0.6
    vel_msg.angular.z = 0.4
    while not rospy.is_shutdown():
        rospy.loginfo("Moving in a circle")
        rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        if k == 10:  # it will print 'move' at the start
            print "MOVE"
        elif k < 0 and (k+6.3) > 6:  # will make the turtle stop after one cycle
            print k+6.3
            print "goal completed"
            break
        else:  # prints distance covered from start in each iteration
            if k > 0:
                print k
            else:
                print 6.285714286+k
        velocity_publisher.publish(vel_msg)
        var_loop_rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
