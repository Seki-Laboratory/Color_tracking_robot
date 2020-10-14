import cv2
import numpy as np


class color:
    i = 0
    def __init__(self,hm1,hm2,hm3,hM1,hM2,hM3):
        color.i = color.i +1
        print("コンストラクト",color.i)
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
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    blue = color(90,127,80,150,255,255)
    

    while(cap.isOpened()):
        ret,frame = cap.read()
        result = blue.color_detect(frame)
        cv2.imshow('hsv_mask_blue',result)



        # キー入力を1ms待って、keyが「q」だったらbreak
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            print("exit")
            break
        
    cap.release()
    cv2.destroyAllWindows()  

if __name__ == '__main__':
    main() 
