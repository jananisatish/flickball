#!/usr/bin/env python3

# Python libraries
import time
import os
import sys
from smbus import SMBus

# Ev3dev2 libraries
from ev3dev2.sensor import INPUT_1
from ev3dev2.port import LegoPort
from ev3dev2.motor import LargeMotor, OUTPUT_C
from ev3dev2.sound import Sound

sound = Sound()
# CONSTANTS

# Make sure the same address is set in Pixy2
PIXY2_I2C_ADDRESS = 0x54

# Signature of the ball configured in PixyMon
BALL_SIGNATURE = 1

# Data for requesting block
GET_OBJECTS_COMMAND = [174, 193, 32, 2, BALL_SIGNATURE, 1]

# The y position of the ball when it reaches the goal - I found this value by opening PixyMon and hovering 
# my mouse over the goalie line on the board. PixyMon shows the coordinates of the mouse, so I used 
# the y-position of the mouse as Ye.
Ye = 190 

# Sets the lego port of the large motor to port C
lm = LargeMotor(OUTPUT_C)  

#Where the robot starts
BALL_START = 170

# Set LEGO port for Pixy2 on input port 1
in1 = LegoPort(INPUT_1)
in1.mode = 'other-i2c'

# Short wait for the port to get ready
time.sleep(0.5)

# Settings for I2C (SMBus(3) for INPUT_1)
bus = SMBus(3)

# Function that reads the signature, x-position and y-position of the ball and checks that they are
# valid values. It checks this by making sure that the signature read is 1, the signature we asked for
def readValues():
    sig = 0
    while sig != BALL_SIGNATURE:
        # Request block
        bus.write_i2c_block_data(PIXY2_I2C_ADDRESS, 0, GET_OBJECTS_COMMAND)
        # Read block
        block = bus.read_i2c_block_data(PIXY2_I2C_ADDRESS, 0, 20)
        # Extract data
        sig = block[7]*256 + block[6]
        x = block[9]*256 + block[8]
        y = block[11]*256 + block[10]
        time.sleep(0.01)
    return [sig, x, y]

#Lets player know that it is looking for the ball
string = "Looking for the ball"
print(string)
sound.speak(string)


# The current signature, x, and y values of the ball
[Sig1, X1, Y1] = readValues() 

# A duplicate of the variables above, but will later be changed
[Sig2, X2, Y2] = [Sig1, X1, Y1] 

#Let player know they can flick
string2 = "Start"
print(string2)
sound.speak(string2)

# This loop repeatedly checks whether the ball has been flicked and waits until it has
while abs(X1 - X2) <= 8 and abs(Y1 - Y2) <= 8:
    #Current signature, x, and y values of the ball
    [Sig2, X2, Y2] = readValues()
    time.sleep(0.1)

# Calculates the x-position of the ball when it reaches the goalie line
Xe = -(((X1 - X2) * (Y1 - Ye))/(Y1 - Y2)) + X1 

# Limits the goalie to move within the resolution of the PixyMon (0-316 on the x-axis)
if Xe > 316:
    Xe = 316
elif Xe < 0:
    Xe = 0

# Moves the goalie the distance it needs to move in pixels divided by 130, because the goalie moves 
# 130 pixels in one rotation.
lm.on_for_rotations(speed=80, rotations=(Xe - BALL_START)/130)
