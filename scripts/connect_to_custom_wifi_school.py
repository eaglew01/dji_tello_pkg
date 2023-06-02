#!/usr/bin/env python3

from djitellopy import Tello

# Instantiate the Tello object
tello = Tello()

# Set the SSID and password of your custom WIFI network
ssid = "wifi_wouter"
password = "wouter123456"
tello.connect()

# Connect to your custom WIFI network
tello.connect_to_wifi(ssid, password)

# Print the current WIFI network status of Tello
print("Tello's WIFI network status: " + tello.get_wifi_status())

# Disconnect from Tello's default WIFI network
tello.disconnect()

