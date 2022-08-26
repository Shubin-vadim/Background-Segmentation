import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cvzone
import numpy as np
import time


class BackgroundModule:
    def __init__(self, wCap=640, hCap=480, imgs=None, color=(None, None, None)):
        self.wCap = wCap
        self.hCap = hCap
        self.imgs = imgs
        self.color = color

    def empty(self, arg):
        pass

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, self.wCap)
        cap.set(4, self.hCap)
        if self.imgs!=None:
            maxiIndImg = len(self.imgs) - 1
            indImg = 0
        segmentor = SelfiSegmentation()
        process = True
        pTime = 0
        cv2.namedWindow("Background")
        cv2.resizeWindow("Background",self.hCap, self.wCap)
        cv2.createTrackbar("Threashold", "Background", 50, 100, self.empty)
        while process:
            success, frame = cap.read()
            threashold = int(cv2.getTrackbarPos("Threashold", "Background")) / 100
            if threashold == 0.0: threashold = -1
            if self.imgs!=None:
                removeBackground = segmentor.removeBG(frame, cv2.resize(self.imgs[indImg], (self.wCap, self.hCap)), threashold)
            else:removeBackground = segmentor.removeBG(frame, self.color, threashold)
            cTime = time.time()
            fps = int(1 / (cTime - pTime))
            pTime = cTime
            text = f'FPS:{fps}'
            cv2.putText(removeBackground, text, (20, 50), cv2.FONT_ITALIC, 2, (255,0,0),2)
            cv2.imshow('Background', removeBackground)
            key = cv2.waitKey(1)
            if key == 226 or key == 100:
                if indImg > 0:
                    indImg -= 1
                else:
                    indImg = maxiIndImg
            elif key == 244 or key == 97:
                if indImg >= maxiIndImg:
                    indImg = 0
                else:
                    indImg += 1
            elif key == 233 or key == 113:
                process = False
                cv2.destroyWindow('Background')

        if process == False:
            end_img = np.zeros([512, 512])
            x, y = end_img.shape[0] // 2, end_img.shape[1] // 2
            text = 'Seans is complete'
            cv2.putText(end_img, text, (x - 200, y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 255), 3)
            cv2.imshow('End_img', end_img)