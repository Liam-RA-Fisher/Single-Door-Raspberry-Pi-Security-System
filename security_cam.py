from picamera import PiCamera
from time import sleep
from datetime import datetime
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import send_sms
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
camera = PiCamera()
camera.rotation = 180

def security_record(time):
    dt = datetime.now().strftime("%d-%m-%y_%H:%M:%S")
    filename = dt + ".h264"
    camera.start_recording(filename)
    sleep(time)
    camera.stop_recording()
    gfile = drive.CreateFile({'parents': [{'id': 'Folder ID'}]})
    gfile.SetContentFile(filename)
    gfile.Upload() # Upload the file.
    os.remove(filename)
    send_sms.send_alert()
