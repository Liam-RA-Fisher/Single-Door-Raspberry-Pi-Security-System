# Homemade Door Security System

This project is a Raspberry Pi 3B+ enabled single door security system. The purpose of the project is to have
a homemade single door security system that can monitor and provide security for a single door.

The usage of the system is as follows:

1. System is booted up by running security_system_controller.py
2. Sign in and authentification to Google Drive is prompted
3. System is then on but not armed
4. Upon button press, password to arm is requested
    1. If password was wrong, three tries are allowed until alarm sounds and text alert is sent
5. If password is correct system is active
6. If door sensor is triggered
    1. Audio alarm sounds
    2. Security cam activated
    3. Text alert sent via sms
    4. Security footage uploaded to Google Drive
7. System disarming happens the same way as arming

## Required Components

- Raspberry Pi 3B+
- KY-021 Mini Reed Switch

<img src="https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System/blob/master/reed.jpg" width=30% height=30%>

- Push Button
- Red LED
- MakerFocus Raspberry Pi 4 Camera Night Vision Camera Adjustable-Focus Module 5MP OV5647

<img src="https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System/blob/master/camera.jpg" width=30% height=30%>

- 10 k Ohm Resistor

<img src="https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System/blob/master/10.jpg" width=30% height=30%>

- 220 Ohm Resistor

<img src="https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System/blob/master/220.jpg" width=30% height=30%>

- USB Keyboard
- USB Mouse
- Speakers that connect to Pi via aux cord

## Wiring

### Connections

#### Reed Switch

- S - GPIO 21
- Positive - 3.3V
- Negative - Gnd

#### Button

- Terminal - 10 k Ohm resistor to Gnd
- Same terminal - GPIO 19 inbetween terminal and resistor
- Opposite terminal - 3.3V

#### LED

- LED - GPIO 18
- LED - 220 Ohm resistor to Gnd

#### Camera

- Connected via usual connector on Pi

#### **Important Note**

The image below outlines the wiring of the security system. In an actual usefull implementation,
the components would not be hooked up to a singular breadboard. The engineering challenge of
physically implementing the security system is left out of this documentation. Broadly speaking, the
physical implementation could involve hooking the reed switch next to the door, atttaching a magnet 
to the door itself so that it will triger reed switch when the door is opened, 
and setting up the keypad / led / arm-disarm button outside the protected door.

![Wiring](https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System/blob/master/Security_System_Wiring.jpg)

## Technologies

### Twilio

Twilio is used for sending SMS alerts when security system is triggered.

[Link to Twilio Docs](https://www.twilio.com/docs/sms/quickstart/python)

### Google Drive

Google Drive is used for storing security footage. A tutorial for setting up a Google Drive to interact with python can be found below.

[Link to Tutorial](https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python)

## Directory

### security_system_controller.py

This is the program that gets executed to start up the system.
It imports the other files and takes care of the threading of the components of the security system.

### security_cam.py

This file takes care of the seciruty camera.
It connects to Google Drive on start up and performs authorization.
It also creates a function to record footage when prompted and upload the footage to Google Drive.

### send_sms.py

This file is the API to interact with the Twilio SMS service.

### door_monitor.py

This program creates three functions. One function monitors and responds to the arm and disarm button.
When the system is armed or dissarmed, a password is requested as well. There is also an LED
to indicate if the system is active or not.
The other function monotors the mini reed door sensor. If the sensor is activated the audio alarm is triggered,
the security cam is triggered, and an SMS alert is sent.

## Set Up

**Step 1.** Collect all of the required components.

**Step 2.** Attach the camera to the Pi.

**Step 3.** Wire up the rest of the components with the PI shutdown on a breadboard for testing. Use the wiring diagram 
above for reference.

**Step 4.** Clone the github repo into whatever directory you want the security system on your Pi:

    git clone https://github.com/Liam-RA-Fisher/Single-Door-Raspberry-Pi-Security-System
    
**Step 5.** Install the following Python3 dependencies:

    pip3 install pydrive
    pip3 install twilio
    pip3 install pygame

**Step 6.** Register for a free tier trial Twilio account: [Twilio](https://www.twilio.com/docs/sms/quickstart/python).
Once you have registered, you can navigate to your account and locate your Account SID, Auth Token, and Phone Number.
Then copy this information into the send_sms.py file Like so:

    client = Client("Account SID", "Auth Token")
    client.messages.create(to="Some Number",
                           from_="Twilio Acct Number",
                           body="SECURITY ALERT! Door was opened when system was active.")
                           
**Step 7.** Create a new google account. **Do not use your personal google account for security reasons!!!**

**Step 8.** Use this tutorial: [Link to Google Auth Tutorial](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf),
to set up the google drive with the account you just created to be allowed to interact with the security system program.
Make sure you download the client_secrets.json file into your project directory for the program to be able to connect
with Google Drive.

**Step 9.** Create a folder on your Google Drive called security_videos_pi and copy the ID of that folder. To do this,
you can locate the folder ID once you have clicked on it in the browser search bar at the top. Then copy the ID 
into the security_cam.py file:

    gfile = drive.CreateFile({'parents': [{'id': 'Folder ID'}]})
    
**Step 10.** Open a terminal in your security system directory and test out your new security system!

    python3 security_system_controller.py


## Project Demonstration



## Future Ideas

Overall this project is a sucessful template for a homemade single door security system. The next thing that I would like 
to implement is a UI for easy booting and shutting down of the system. Currently to boot the program you 
have to run a Python program in the terminal. It would be nice to have a web interface to boot and shutdown the system.

## Referances

1. https://github.com/fritzing/fritzing-parts/tree/master/svg/core/breadboard
2. https://www.makersupplies.sg/products/ky-021-reed-switch-module-magnetic-switch
3. https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python
4. https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf
5. https://www.twilio.com/docs/sms/quickstart/python

