#color_tracking test source for windows & raspberrypi 2020/10/10 

# -*- coding: utf-8 -*-
#from functools import update_wrapper
import cv2
import numpy as np

def red_detect(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色のHSVの値域1

    hsv_min = np.array([0,180,30])
    hsv_max = np.array([30,255,255])

    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色のHSVの値域2
    hsv_min = np.array([150,180,30])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    maska = mask1 + mask2

    return maska

# ブロブ解析
def analysis_blob(binary_img):
    # 2値画像のラベリング処理
    label = cv2.connectedComponentsWithStats(binary_img)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1
    if n != 0:
        #print(n)
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
    else:    
        return 0


def main():
    # カメラのキャプチャ
    #windowsの場合はcv2．CAP_DSHOWを第2引数にいれる  
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    #cap = cv2.VideoCapture(0) 

    while(cap.isOpened()):
        # フレームを取得
        ret, frame = cap.read()

        # 赤色検出
        mask = red_detect(frame)
        target = analysis_blob(mask)

 
        if target != 0 :
            # # # 面積最大ブロブの中心座標を取得
            center_x = int(target["center"][0])
            center_y = int(target["center"][1])       
            area = int(target["area"])

            # # # フレームに面積最大ブロブの中心周囲を円で描く
            cv2.circle(frame, (center_x, center_y), 30, (0, 200, 0),
                    thickness=3, lineType=cv2.LINE_AA)
           # w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            #x = center_x - w/2
            
            # # # 四角で囲む
            upx = int(target["upper_left"][0])
            upy = int(target["upper_left"][1])
            w = int(target["width"])
            h = int(target["height"])
            cv2.rectangle(frame, (upx, upy), (upx+w, upy+h), (0, 0, 255))

       

        # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        
        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):

            break
        
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main() 
