# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:50:39 2022

@author: Electroinc.cyou

This script is used as a tutorial along with the e3631a.py module
from electroinc.cyou.

It will sweep the +25V output of a Keysight/Agilent/HP E3631A power
supply between 0 - 5 Volts inclusive, measure current at each step, 
and print the measurements.

Please use this script at your own risk and check your instrument 
before use. Thank you.

v1.0
"""

import serial
import time
import e3631a
import numpy as np
import csv
from datetime import datetime

#Create an Serial instance, called ps1 (powersupply1)
ps1 = serial.Serial('COM3',
                baudrate = 9600,
                bytesize=8,
                timeout=1,
                stopbits = serial.STOPBITS_TWO,
                parity = serial.PARITY_NONE,
                dsrdtr = 1)

#Request IDN from ps1
e3631a.sendscpi(ps1,'*IDN?')
idn = e3631a.readscpi(ps1)
print('IDN of ps1: ' + idn)

#Put ps1 into remote operation mode
e3631a.sendscpi(ps1,'SYST:REM')

#######################################
#Test begin
#######################################

#Declare variables for our voltage sweep
start_voltage = 0
end_voltage   = 5
step_voltage  = 1

#Create empty array to store instrument IDN, step, voltage, and current
num_rows = int(((end_voltage - start_voltage)/step_voltage) + 4)
data = [['' for x in range(3)] for y in range(num_rows)]
data[0][0] = [idn]
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
data[1][0] = date_time
data[2] = ['STEP', 'VOLTAGE', 'CURRENT']
row = 3

#Control the +25V output - ready the start voltage - turn output on
e3631a.sendscpi(ps1,'INST P25V')
e3631a.sendscpi(ps1,'VOLT ' + str(start_voltage))
e3631a.sendscpi(ps1,'OUTP ON')

#Loop through each voltage as defined by lines 32-34.
for current_voltage in range(start_voltage, end_voltage+step_voltage, step_voltage):
    #Set voltage and wait 1 second to allow measurement to settle
    e3631a.sendscpi(ps1,'VOLT ' + str(current_voltage))
    time.sleep(1)
    #Request current and voltage
    e3631a.sendscpi(ps1,'MEAS:CURR?')
    current = e3631a.readscpi(ps1)
    e3631a.sendscpi(ps1,'MEAS:VOLT?')
    voltage = e3631a.readscpi(ps1)
    #Put data into array
    data[row] = [row-2, voltage, current]
    row += 1

#Close the serial port when finished.    
ps1.close()

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
data[1][1] = date_time

#Save the data array to a .txt file
with open("e3631a_test_file.csv","w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)