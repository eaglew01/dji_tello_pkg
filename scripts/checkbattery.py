#!/usr/bin/env python

from djitellopy import Tello

# Instantiate the Tello object
tello = Tello()

tello.connect()

print(tello.get_battery())

tello.end