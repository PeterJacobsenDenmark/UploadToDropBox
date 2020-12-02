#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  


import threading
import time
import sys

import RPi.GPIO as GPIO

from multiprocessing import Queue, Value #Needed for cross thread value communnication

from UploadThread import startUploadThread





def main():
    try:       
        print( "READ OUT")

        uploadThread = threading.Thread( target=startUploadThread, args=( ))
        uploadThread.start()


    except (KeyboardInterrupt, SystemExit):
        print( "MAIN - Keyboard interrup " )
    except Exception as e:
        error_log(e, "Unhandled Exception in Main")
        if not debug:
            time.sleep(60)
            reboot()




if __name__ == '__main__':
    main()

