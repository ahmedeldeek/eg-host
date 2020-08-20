import socket
import os
import time
################
time.sleep (0.500)
os.system ("clear")
print (" \033[0;32m ___  __ _          | |__   ___  ___| |_")
print ("\033[0;32m/  _ \/ _` |  _____  | '_ \ / _ \/ __| __|")
print ("\033[0;32m|  __/ (_| | |_____| | | | | (_) \__ \ |_")
print (" \033[0;32m\___|\__, |         |_| |_|\___/|___/\__|")
print ("      \033[0;32m|___/")
print ("")
###############
def h () :
    time.sleep (1)
    hostname=input ("\033[0;33mtarget is : ")
    ip=socket.gethostbyname(hostname)
    print ("\033[0;32mip is :" ,ip ,"\033[0;37m")
h ()
