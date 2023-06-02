#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys, select, termios, tty
from pynput import keyboard
import time
import cv2


def showDrone():
    # Initialize ROS node
    rospy.init_node('tello_show')

    # Create a publisher for the Tello command topic
    pub = rospy.Publisher('tello/cmd', String, queue_size=10)

    # Set terminal settings for reading arrow key input
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

    print("Welcome to the DJI TELLO SHOW!!! ")
    print("To launch the show press SPACEBAR")
    def on_press(key):
        if key == keyboard.Key.space:
            print('Spacebar is pressed')
            pub.publish("start")
            listener.stop()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


    print("SPACEBAR+takeoff")
    time.sleep(6)
    print("SHOW STARTING")
    time.sleep(2)
    print("3")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("1")

    pub.publish("upseqhigh")
    #time.sleep(1)
    pub.publish("downseqhigh")
    #time.sleep(1)
    pub.publish("lefthigh")
    #time.sleep(1)
    pub.publish("rotateleftseq")
    time.sleep(1)
    #pub.publish("rotateright")
    pub.publish("righthigh")
    #time.sleep(1)
    pub.publish("flipleft")
    #time.sleep(1)
    pub.publish("flipright")
    pub.publish("end")


    # while True:
    #     pub.publish("up")
    #     pub.publish("up")

    #     pub.publish("left")
    #     pub.publish("left")

    #     pub.publish("flipleftseq")
    #     pub.publish("end")
        
    #     #     # Wait for a key press, and exit if the user pressed "q"
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         pub.publish("end")
    #         break


    # Restore original terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    try:
        showDrone()
    except rospy.ROSInterruptException:
        pass

