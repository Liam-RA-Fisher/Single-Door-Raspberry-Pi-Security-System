import security_cam
from time import sleep
import pygame
import send_sms

On = -1

n_attempts = 0

def power():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    
    global On
    
    while True:
        if GPIO.input(19):
            pw = input("Enter Password: ")
            if pw == "pw":
                On *= -1
                n_attempts = 0
                if On == 1:
                    GPIO.output(18, True)
                else:
                    GPIO.output(18, False)
            else:
                n_attempts += 1
                if n_attempts >= 3:
                    pygame.mixer.init()
                    pygame.mixer.music.load("Alarm.mp3")
                    pygame.mixer.music.play()
                    send_sms.password_alert()
                    n_attempts = 0
                else:
                    pygame.mixer.init()
                    pygame.mixer.music.load("Wrong-answer-sound-effect.mp3")
                    pygame.mixer.music.play()
        sleep(0.005)

def door_sense():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    global On
    
    while True:
        if GPIO.input(21) == 0 and On == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("Alarm.mp3")
            pygame.mixer.music.play()
            security_cam.security_record(10)
            print("Gotcha")
        sleep(0.02)