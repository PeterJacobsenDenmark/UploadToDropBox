#! /usr/bin/python
import threading
import time
from datetime import datetime
import sys
import os
import dropbox

from test import upload



def startUploadThread( ):
   

   
    while True:




        now = datetime.now() # current date and time


       
        fb = open('/home/pi/WeatherLog/log.txt','a+')
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        fb.write(date_time)	

        fb.write(": test") 
        fb.write('\n')
        fb.close()

        upload()


        time.sleep(10)

