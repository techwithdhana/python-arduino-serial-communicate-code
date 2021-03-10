# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:00:05 2021

@author: Dhanasekar
"""

import serial

port = serial.Serial('COM10', 9600)

while (port.isOpen()):
    data = input("Enter the option: ")
    
    if (data == 'on'):
        port.write(str.encode('1'))
    elif(data == 'off'):
        port.write(str.encode('0'))
    else:
        print("Invalid Number!!")
        