#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys, select, termios, tty
from pynput import keyboard
import time

# Define arrow key codes
FORWARD = 'z'
BACK = 's'
LEFT = 'q'
RIGHT = 'd'

UP= 'i'
DOWN= 'k'
ROTATE_LEFT= 'j'
ROTATE_RIGHT= 'l'
ESCAPE= 'p'

def teleop():
    # Initialize ROS node
    rospy.init_node('tello_teleop')

    # Create a publisher for the Tello command topic
    pub = rospy.Publisher('tello/cmd', String, queue_size=10)

    # Set terminal settings for reading arrow key input
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

    print("Welcome to keyboard TELEOP for the DJI TELLO ")
    print("To launch the drone press SPACEBAR")
    def on_press(key):
        if key == keyboard.Key.space:
            print('Spacebar is pressed')
            pub.publish("start")
            listener.stop()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


    print("SPACEBAR+takeoff")
    time.sleep(8)
    print("TELEOP STARTED")
    print("zqsd for forward, left, back and right")
    print("i,k,j and l keys for up down, rotate left and rotate right")
    print("press p to land")
    


    # Loop to listen for keyboard input
    while not rospy.is_shutdown():
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            # Read a single character of input from the arrow keys
            key = sys.stdin.read(1)

            # Check which arrow key was pressed and publish the corresponding command
            if key == FORWARD:
                pub.publish("forward")
            elif key == BACK:
                pub.publish("back")
            elif key == LEFT:
                pub.publish("left")
            elif key == RIGHT:
                pub.publish("right")
            elif key == UP:
                pub.publish("up")
            elif key == DOWN:
                pub.publish("down")
            elif key == ROTATE_LEFT:
                pub.publish("rotateleft")
            elif key == ROTATE_RIGHT:
                pub.publish("rotateright")
            elif key == ESCAPE:
                pub.publish("end")

    # Restore original terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass

