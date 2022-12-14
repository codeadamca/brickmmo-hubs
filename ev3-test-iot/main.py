#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import DCMotor


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Initialize EV3 touch sensor and motors
motorA = Motor(Port.A)
motorB = Motor(Port.B)
lights = DCMotor(Port.C)
# touch = TouchSensor(Port.S1)
color = ColorSensor(Port.S1)

# Initialize lights
ev3.light.on(Color.RED)

# Set button vairble
touchButton = "Off"

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():

        motorA.stop()
        motorB.stop()
        lights.dc(0)
        ev3.light.off()
        touchButton = "Off"
        break

    print(color.color())
    print(color.ambient())
    print(color.reflection())


    '''
    # If the touch sensor is pressed
    if touch.pressed() is True and touchButton == "Off":

        motorA.dc(100)
        motorB.dc(100)
        lights.dc(100)
        ev3.light.on(Color.GREEN)
        touchButton = "On"

    # If the touch sensor is released
    elif touch.pressed() is False and touchButton == "On":

        motorA.stop()
        motorB.stop()
        lights.dc(0)
        ev3.light.on(Color.RED)
        touchButton = "Off"
    '''



    wait(500)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
