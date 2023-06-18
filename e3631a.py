# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:23:45 2022

@author: Electroinc

This module is designed to allow for easy RS232 communication with Keysight/
Agilent/HP E3631A power supply. A sleep-time of 0.1 seconds is included to 
facilitate reliable communication without flow control.

Please use this script at your own risk and check your instrument 
before use. Thank you.

v1.0
"""

import time

def sendscpi(port, command):
    time.sleep(0.1)
    eol_char = '\r\n'
    port.write((command+eol_char).encode('utf-8'))
      
def readscpi(port):
    time.sleep(0.1)
    reply = port.readline()
    decoded = reply.decode("utf-8")
    return decoded.strip()
    