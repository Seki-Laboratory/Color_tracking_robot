import cv2
import numpy as np


class color:
    def __init__(self,hm1,hm2,hm3,hM1,hM2,hM3):
        print("コンストラクト")
        self.hsv_min = np.array([hm1,hm2,hm3])
        self.hsv_max = np.array([hM1,hM2,hM3])
        

    def color_detect(self,img):
        # HSV色空間に変換
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # 赤色のHSVの値域1
        mask = cv2.inRange(hsv, self.hsv_min, self.hsv_max)

        return mask


def main():
    print("main")

if __name__ == '__main__':
    main() 
