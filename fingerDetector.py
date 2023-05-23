
import numpy as np

class FingerDetector:
    tipIds = [4,8,12,16,20]
    def __init__(self,hand1=[],hand2=[],handCount = 0):
        self.hand1 = hand1
        self.hand2 = hand2
        self.handCount = handCount
        self.fingersL = np.zeros((5),np.int8)
        self.fingersR =  np.zeros((5),np.int8)
    def detectLeftOrRight(self,hand=[]):
        if not hand: None
        elif hand[4][1] > hand[18][1]:
            return "left"
        elif hand[4][1] < hand[18][1]:
            return "right"
        
    def one_hand_detector(self,hand):
        fingers = self.fingersR
        if(self.detectLeftOrRight(hand)=="right"):
            if hand[4][1] < hand[5][1]:
                fingers[0] = 1
            elif hand[4][1] > hand[5][1]:
                fingers[0] = 0
            for id in range(1,len(self.tipIds)):
                if hand[self.tipIds[id]][2] < hand[self.tipIds[id]-2][2]:
                    fingers[id] = 1
                else:
                    fingers[id] = 0
            return "left",fingers
        elif(self.detectLeftOrRight(hand)=="left"):
            fingers = self.fingersL
            if hand[4][1] > hand[5][1]: 
                fingers[0] = 1
            elif hand[4][1] < hand[5][1]:
                fingers[0] = 0
            for id in range(1,len(self.tipIds)):
                if hand[self.tipIds[id]][2] < hand[self.tipIds[id]-2][2]:
                    fingers[id] = 1
                else:
                    fingers[id] = 0
            return "right",fingers
    
    def two_hand_detector(self,hand1,hand2):
        fingers = self.fingersR
        fingers2 = self.fingersL
        if(self.detectLeftOrRight(hand1)=="right"):
            if hand1[4][1] < hand1[5][1]:
                fingers[0] = 1
            elif hand1[4][1] > hand1[5][1]:
                fingers[0] = 0
            if hand2[4][1] > hand2[5][1]:
                fingers2[0] = 1
            elif hand2[4][1] < hand2[5][1]:
                fingers2[0] = 0
            for id in range(1,len(self.tipIds)):
                if hand1[self.tipIds[id]][2] < hand1[self.tipIds[id]-2][2]:
                    fingers[id] = 1
                else:
                    fingers[id] = 0

            for id in range(1,len(self.tipIds)):
                if hand2[self.tipIds[id]][2] < hand2[self.tipIds[id]-2][2]:
                    fingers2[id] = 1
                else:
                    fingers2[id] = 0
            return {"left":fingers,"right":fingers2}
        else:
            if hand1[4][1] > hand1[5][1]:
                fingers[0] = 1
            elif hand1[4][1] < hand1[5][1]:
                fingers[0] = 0
            if hand2[4][1] < hand2[5][1]:
                fingers2[0] = 1
            elif hand2[4][1] > hand2[5][1]:
                fingers2[0] = 0
            for id in range(1,len(self.tipIds)):
                if hand1[self.tipIds[id]][2] < hand1[self.tipIds[id]-2][2]:
                    fingers[id] = 1
                else:
                    fingers[id] = 0

            for id in range(1,len(self.tipIds)):
                if hand2[self.tipIds[id]][2] < hand2[self.tipIds[id]-2][2]:
                    fingers2[id] = 1
                else:
                    fingers2[id] = 0
            return {"right":fingers,"left":fingers2}