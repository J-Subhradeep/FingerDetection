import cv2
import time
import os
import numpy as np
import handTrackingModule as htm
from firebase import firebase
import fingerDetector as fd
firebase  = firebase.FirebaseApplication("https://finger-number-detection-default-rtdb.asia-southeast1.firebasedatabase.app/",None)


cap = cv2.VideoCapture(0)
# cap.set(3,900)
# cap.set(4,720)


detector = htm.handDetector(detectionCon=0.70)

tipIds = [4,8,12,16,20]
whichHand = "left"
count = 0
lmList2 = []
lmList = []
while True:
    success, img = cap.read()
    img = cv2.resize(img,(700,550))
    img = detector.findHands(img) 
    # print(img.shape) 
    lmList = detector.findPosition(img,draw = False)
    fingerDetector = fd.FingerDetector(lmList,handCount=detector.handCount)
    # print(detector.handCount)
    if detector.handCount ==2:
        lmList2 = detector.findPosition(img,1,False)
        fingerDetector = fd.FingerDetector(lmList,lmList2,handCount=detector.handCount)
        
    if lmList:
        fingers = np.array([0,0,0,0,0],np.int8)
        fingers2 = np.array([0,0,0,0,0],np.int8)
        if detector.handCount == 1:
            # print(fingerDetector.detectLeftOrRight(lmList),fingerDetector.detectLeftOrRight(lmList2))
            d = fingerDetector.one_hand_detector(lmList)
            # print(d)
            
            # assigning left fingers in fingers array / right fingers in fingers2 array
            if d and d[0] == "left":
                fingers = d[1]
            elif d and d[0] == "right":
                fingers2 = d[1]
           

        elif detector.handCount == 2:
            data = fingerDetector.two_hand_detector(lmList,lmList2)
            fingers = data.get("left")
            fingers2 = data.get("right")
            # print(data)
        # print(fingers,fingers2)
        cv2.putText(img,f"Count : {fingers.sum()+fingers2.sum()}",(30,60),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),4)
        try:
            if count>=35:
                firebase.put("/","data",{
                    "finger0":str(fingers[0]),
                    "finger1":str(fingers[1]),
                    "finger2":str(fingers[2]),
                    "finger3":str(fingers[3]),
                    "finger4":str(fingers[4]),
                    "finger5":str(fingers2[0]),
                    "finger6":str(fingers2[1]),
                    "finger7":str(fingers2[2]),
                    "finger8":str(fingers2[3]),
                    "finger9":str(fingers2[4]),})
                count = 0

        except Exception as e:
            print(e)
            pass
        count+=1
            
        # print(fingers.sum()+fingers2.sum())
        
            
    cv2.imshow("Image",img)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()