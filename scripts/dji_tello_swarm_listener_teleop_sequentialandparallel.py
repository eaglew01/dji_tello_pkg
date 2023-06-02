#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from djitellopy import Tello
from djitellopy import TelloSwarm
import time

# Create a Tello swarm and IP
# Add the IP adresses from the different IP adresses of the DJI Tello

swarm = TelloSwarm.fromIps([
    #"192.168.137.222"
    "192.168.137.164"
    #,"192.168.137.65"
])
tello = swarm

def callback(data):
    # Check if the message received is to make the drone go forward

    if data.data == "start":
        # Connect to the drone
        tello.connect()
        print("Tellos connected")
        #time.sleep(3)
        tello.takeoff()



    elif data.data == "forward":


        # Send the command to make the drone go forward
        tello.move_forward(20)

    elif data.data == "forwardseq":
        # Send the command to make the drone go forward
        swarm.sequential(lambda i, tello: tello.move_forward(20))

        
    elif data.data == "back":
        # Send the command to make the drone go back
        tello.move_back(20)
    
    elif data.data == "backseq":
        # Send the command to make the drone go back
        swarm.sequential(lambda i, tello: tello.move_back(20))

    elif data.data == "left":
        # Send the command to make the drone go left
        tello.move_left(20)

    elif data.data == "lefthigh":
        # Send the command to make the drone go left
        tello.move_left(200)

    elif data.data == "leftseq":
        # Send the command to make the drone go left
        swarm.sequential(lambda i, tello: tello.move_left(20))

    elif data.data == "right":
        # Send the command to make the drone go right
        tello.move_right(20)

    elif data.data == "righthigh":
        # Send the command to make the drone go left
        tello.move_right(150)

    elif data.data == "rightseq":
        # Send the command to make the drone go right
        swarm.sequential(lambda i, tello: tello.move_right(20))

    elif data.data == "up":
        # Send the command to make the drone go up
        tello.move_up(20)

    elif data.data == "upseq":
        # Send the command to make the drone go up
        swarm.sequential(lambda i, tello: tello.move_up(20))

 
    elif data.data == "upseqhigh":
        # Send the command to make the drone go up
        swarm.sequential(lambda i, tello: tello.move_up(100))   

    elif data.data == "down":
        # Send the command to make the drone go down
        tello.move_down(20)

    elif data.data == "downseq":
        # Send the command to make the drone go down
        swarm.sequential(lambda i, tello: tello.move_down(20))

    elif data.data == "downseqhigh":
        # Send the command to make the drone go down
        swarm.sequential(lambda i, tello: tello.move_down(100))

    elif data.data == "rotateleft":
        # Send the command to make the drone rotate left
        tello.rotate_counter_clockwise(20)

    elif data.data == "rotateleftseq":
        # Send the command to make the drone rotate left
        swarm.sequential(lambda i, tello: tello.rotate_counter_clockwise(20))

    elif data.data == "rotateright":
        # Send the command to make the drone rotate right
        tello.rotate_clockwise(20)


    elif data.data == "rotaterightseq":
        # Send the command to make the drone rotate right
        swarm.sequential(lambda i, tello: tello.rotate_clockwise(20))

    elif data.data == "end":
        tello.land()
        # Send the command to make the drone land and disconnect
        tello.end()

    elif data.data == "flipleft":
        tello.flip_left()

    elif data.data == "flipright":
        tello.flip_right()
    
    elif data.data == "flipleftseq":
        swarm.sequential(lambda i, tello: tello.flip_left())


def listener():
    # Initialize ROS node
    rospy.init_node('tello_listener_tello_cmd', anonymous=True)

    # Subscribe to the Tello command topic
    rospy.Subscriber('tello/cmd', String, callback)

    # Spin the node
    rospy.spin()

if __name__ == '__main__':
    listener()

