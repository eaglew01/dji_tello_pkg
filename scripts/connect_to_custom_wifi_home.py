#!/usr/bin/env python3

from djitellopy import Tello

# Instantiate the Tello object
tello = Tello()

# Set the SSID and password of your custom WIFI network
ssid = ""
password = ""
tello.connect()

# Connect to your custom WIFI network
tello.connect_to_wifi(ssid, password)

# Disconnect from Tello's default WIFI network
tello.end()


