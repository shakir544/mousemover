#! /usr/bin/python

# A python program to move the mouse from one location to another 
import pyautogui
import time



for i in range(100):
    if i %2 ==0 :
        pyautogui.moveTo(100,400)
        time.sleep(5)
    else :
        pyautogui.moveTo(400,100)
        time.sleep(5)