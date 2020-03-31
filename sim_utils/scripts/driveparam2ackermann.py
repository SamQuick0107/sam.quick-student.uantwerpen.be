#!/usr/bin/env python

import rospy
from sim_utils.msg import drive_param 
from std_msgs.msg import Header
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped 

publisher = None

# Properties of the Ackermann implementation
steering_angle_velocity = 5.0
acceleration = 1.0
jerk = 0.0


def callback(data):
    rospy.loginfo(str(data.steer) + " - " + str(data.throttle))
    
    ackermsg = AckermannDriveStamped()
    ackermsg.header = Header()
    ackermsg.header.stamp = rospy.Time.now()

    ackermsg.drive = AckermannDrive()
    ackermsg.drive.steering_angle = data.steer
    ackermsg.drive.steering_angle_velocity = steering_angle_velocity

    ackermsg.drive.speed = data.throttle
    ackermsg.drive.acceleration = acceleration
    ackermsg.drive.jerk = jerk

    publisher.publish(ackermsg)


def node():
    global publisher

    rospy.init_node('driveparam2ackermann', anonymous=False)
    rospy.Subscriber("drive_parameters", drive_param, callback)
    publisher = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    node()
