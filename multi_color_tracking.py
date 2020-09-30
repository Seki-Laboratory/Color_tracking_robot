# -*- coding: utf-8 -*-
import cv2
import numpy as np

def red_detect(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色のHSVの値域1

    hsv_min = np.array([0,230,80])
    hsv_max = np.array([30,255,255])

    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色のHSVの値域2
    hsv_min = np.array([150,230,80])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    return mask1 + mask2

# ブロブ解析
def analysis_blob(binary_img):
    # 2値画像のラベリング処理
    label = cv2.connectedComponentsWithStats(binary_img)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1
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

def blue_detect(img):
        # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色のHSVの値域1

    hsv_min = np.array([90,127,80])
    hsv_max = np.array([150,255,255])

    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    return mask1 

def analysis_blob_blue(binary_img):
    # 2値画像のラベリング処理
    label = cv2.connectedComponentsWithStats(binary_img)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1
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
    #videofile_path = "C:/github/sample/python/opencv/video/color_tracking/red_pendulum.mp4"

    # カメラのキャプチャ
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        # フレームを取得
        ret, frame = cap.read()

        # 赤色検出
        mask = red_detect(frame)
        maskb = blue_detect(frame)
        # マスク画像をブロブ解析（面積最大のブロブ情報を取得）
        target = analysis_blob(mask)
        targetb = analysis_blob_blue(maskb)        
        # 面積最大ブロブの中心座標を取得
        center_x = int(target["center"][0])
        center_y = int(target["center"][1])
        centerb_x = int(targetb["center"][0])
        centerb_y = int(targetb["center"][1])       
        area_red = int(target["area"])
        area_blue = int(targetb["area"])

        # フレームに面積最大ブロブの中心周囲を円で描く
        if area_red > 1000 :
                
            cv2.circle(frame, (center_x, center_y), 30, (0, 0, 255),
                    thickness=3, lineType=cv2.LINE_AA)
        if area_blue > 1000 :
            cv2.circle(frame, (centerb_x, centerb_y), 30, (255, 0, 0),
                    thickness=3, lineType=cv2.LINE_AA)

        print(area_red) 


        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        x = center_x - w/2

       

        # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask_red", mask)
        cv2.imshow("Mask_blue", maskb)

        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):

            break
        

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main() 
