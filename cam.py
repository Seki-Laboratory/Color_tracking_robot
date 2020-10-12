# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        # フレームを取得
        ret, frame = cap.read()

        # グレースケール変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2値化
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # ラベリング処理
        label = cv2.connectedComponentsWithStats(gray)

        # ブロブ情報を項目別に抽出
        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)

        # ラベルの個数nだけ色を用意
        print("ブロブの個数:", n)
        print("各ブロブの外接矩形の左上x座標", data[:,0])
        print("各ブロブの外接矩形の左上y座標", data[:,1])
        print("各ブロブの外接矩形の幅", data[:,2])
        print("各ブロブの外接矩形の高さ", data[:,3])
        print("各ブロブの面積", data[:,4])
        print("各ブロブの中心座標:\n",center)
            # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", gray)

        
        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):

            break
        

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()