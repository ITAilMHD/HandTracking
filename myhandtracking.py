# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 02:05:15 2021

@author: hp
"""

import cv2
import numpy as np
import time
import HandTrackingModule as htm


######################################################
wCam=640
hCam=480

detector=htm.handDetector()
######################################################


cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    sucess,img=cap.read()
    img=detector.findHands(img)
    
    
    cv2.imshow("img",img)
    cv2.waitKey(0)