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

    def analysis_blob(self,b):
        # 2値画像のラベリング処理
        label = cv2.connectedComponentsWithStats(b)

        # ブロブ情報を項目別に抽出
        #n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)

        # ブロブ面積最大のインデックス
        max_index = np.argmax(data[:, 4])

        # 面積最大ブロブの情報格納用
        maxblob = {}

        # 面積最大ブロブの各種情報を取得
        maxblob["upper_left"] = (data[:, 0][max_index], data[:, 1][max_index]) # 左上座標
        maxblob["width"] = data[:, 2][max_index]  # 幅
        maxblob["height"] = data[:, 3][max_index]  # 高さ
        maxblob["area"] = data[:, 4][max_index]   # 面積
        maxblob["center"] = center[max_index]  # 中心座標
        
        return maxblob    

    
    
def main():
    print("main")
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #インスタンス生成
    blue = color(90,127,80,150,255,255)
    
    while(cap.isOpened()):
        ret,frame = cap.read()
        mask = blue.color_detect(frame)
        target_blue = blue.analysis_blob(mask)

        center_blue_y = int(target_blue["center"][1])  
        center_blue_x = int(target_blue["center"][0])

        cv2.circle(frame, (center_blue_x, center_blue_y), 30, (255, 0, 0),
        thickness=3, lineType=cv2.LINE_AA)
        cv2.imshow('hsv_mask_blue',frame)



        # キー入力を1ms待って、keyが「q」だったらbreak
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            print("exit")
            break
        
    cap.release()
    cv2.destroyAllWindows()  

if __name__ == '__main__':
    main() 
