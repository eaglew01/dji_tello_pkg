#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from djitellopy import Tello

# Create a Tello object
tello = Tello()

def callback(data):
    # Check if the message received is to make the drone go forward

    if data.data == "start":
        # Connect to the drone
        tello.connect()
        tello.takeoff()



    elif data.data == "forward":


        # Send the command to make the drone go forward
        tello.move_forward(20)

        
    elif data.data == "back":
        # Send the command to make the drone go back
        tello.move_back(20)

    elif data.data == "left":
        # Send the command to make the drone go left
        tello.move_left(20)

    elif data.data == "right":
        # Send the command to make the drone go right
        tello.move_right(20)

    elif data.data == "up":
        # Send the command to make the drone go up
        tello.move_up(20)

    elif data.data == "down":
        # Send the command to make the drone go down
        tello.move_down(20)

    elif data.data == "rotateleft":
        # Send the command to make the drone rotate left
        tello.rotate_counter_clockwise(20)

    elif data.data == "rotateright":
        # Send the command to make the drone rotate right
        tello.rotate_clockwise(20)


    elif data.data == "end":
        #send the command to make the drobe land
        tello.land()

        # Send the command to make the drone land and disconnect
        tello.end()


def listener():
    # Initialize ROS node
    rospy.init_node('tello_listener_tello_cmd', anonymous=True)

    # Subscribe to the Tello command topic
    rospy.Subscriber('tello/cmd', String, callback)

    # Spin the node
    rospy.spin()

if __name__ == '__main__':
    listener()

