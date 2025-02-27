# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 03:18:02 2021

@author: hp
"""

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False,maxHands=2,detCon=1,trackCon=1):
        
        self.mode=mode
        self.maxHands=maxHands
        self.detCon=detCon
        self.trackCon=trackCon
        self.mpHand=mp.solutions.hands
        self.hand=self.mpHand.Hands(self.mode,self.maxHands,self.detCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
        


#cap=cv2.VideoCapture(0)
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hand.process(imgRGB)
   # print(results.multi_hand_landmarks) #to know if there is a hand or not
        if self.results.multi_hand_landmarks:
            for mHand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,mHand,self.mpHand.HAND_CONNECTIONS)
        return img
    
    
    def getPositions(self,img,handNo=0,draw=True):
        lmlist=[]
        
        if self.results.multi_hand_landmarks:
            myhand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                h, w, c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
            
        return lmlist
    
    


def main():
    cap=cv2.VideoCapture(0)
    
    detector=handDetector()
    
    while True:
        sucess,img=cap.read()
        
        img=detector.findHands(img)
        lmlist=detector.getPositions(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        cv2.imshow("image",img)
        cv2.waitKey(1)
        
        
        
        
        



if __name__=="__main__":
    main()

