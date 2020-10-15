import numpy as np
import cv2

def hsvExtraction(image, hsvLower, hsvUpper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 画像をHSVに変換
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
    result = cv2.bitwise_and(image, image, mask=hsv_mask) # 元画像とマスクを合成
    return result

def main():
    image = cv2.imread('./test.jpg') # ファイル読み込み
    hsvLower = np.array([150, 64, 0])    # 抽出する色の下限
    hsvUpper = np.array([179, 255, 255])    # 抽出する色の上限
    hsvResult = hsvExtraction(image, hsvLower, hsvUpper)
    cv2.imshow('HSV_test1', hsvResult)
    cv2.imwrite('red.jpg',hsvResult)

    while True:
        # キー入力を1ms待って、keyが「q」だったらbreak
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

