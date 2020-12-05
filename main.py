#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  

import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

def upload():
    access_token = 'c4g63lFy7KoAAAAAAAAAAUeWmLmnXGMtk5N4nskzPXdNVRZCdsnKIcjh3vNFh4L3'
    transferData = TransferData(access_token)

    file_from = '/home/pi/WeatherPi/log.txt' # This is name of the file to be uploaded
    file_to = '/log.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)


def main():
   
  while True:
      upload()




if __name__ == '__main__':
    main()

