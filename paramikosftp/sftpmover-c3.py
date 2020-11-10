#!/usr/bin/env python3
## Moving files with SFTP

def movethemfiles():
## iterate across the files within directory
    # iterate on directory contents
    for x in os.listdir("/home/student/filestocopy/"):
        # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x):
            # iterate on directory contents
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

## import paramiko so we can talk SSH
import paramiko
import os
import sys

## where to connect to
target = input('What is the IP of the target machine? ')
t = paramiko.Transport(target , 22) ## IP and port
username = input('What is the user name on the target machine? ')
password = input('What is the user\' password? ')

try:
## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=username, password=password)
except:
    print("There was an error trying to SFTP to",target, "as", username, "!" )
    sys.exit()

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

movethemfiles()

## close the connection
sftp.close() # close the connection
