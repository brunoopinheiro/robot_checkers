import cv2
import numpy as np
import time

class Capture:
    def __init__(self) -> None:
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        self.nframes = 2
        self.interval = 5

    def capture_image(self):
        for i in range(self.nframes):
            ret, img = self.cam.read()
            cv2.imwrite('./img_'+str(i).zfill(4)+'.png', img)
            time.sleep(self.interval)