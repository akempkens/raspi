# raspi
Within this repository I store code for my work with the Raspberry 3 and especially the GPIO stuff

The idea of the various projects follows a simple startup routine based on the https://www.modmypi.com/raspberry-pi/sensors-1061/kits-and-interface-boards-1062/raspberry-pi-youtube-workshop-kit

The kit is pretty simple, however you should clearly follow the videos on that site as some other videos within the wild use different resistors or circuits that makes following the tutorials pretty complex.

# Overview of code / tutorial steps
1. 1_ledoff.py - based on the circuit of the standard LEDs to switch them off
2. 2_blink.py let the LEDs flash
3. 3_pressbutton.py - just reacts on a button press
4. 4_input.py - a simple script to react on user input
5. 5_button_LDE.py - this is the combination of 2,3 & 4 to let the LED light up only if you press the button

