# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)
    #cam3 = cv2.VideoCapture(2)
    #cam4 = cv2.VideoCapture(3)
    
    while True:
        # フレームを取得
        ret, frame = cam1.read()
        ret, frame1 = cam2.read()
        # ret, frame2 = cam3.read()
        # ret, frame3 = cam4.read()

            # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Frame1", frame1)
        # cv2.imshow("Frame2", frame2)
        # cv2.imshow("Frame3", frame3)


        
        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):

            break
        

    cam1.release()
    cam2.release()
    # cam3.release()
    # cam4.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()