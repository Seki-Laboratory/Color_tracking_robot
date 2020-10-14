import cv2
import datetime
import time


def check_camera_connection():
    """
    Check the connection between any camera and the PC.

    """


    print('[', datetime.datetime.now(), ']', 'searching any camera...')
    true_camera_is = []  # 空の配列を用意

    # カメラ番号を0～9まで変えて、COM_PORTに認識されているカメラを探す
    for camera_number in range(0, 4):
        cap = cv2.VideoCapture(camera_number,cv2.CAP_DSHOW)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(camera_number)
            print("camera_number", camera_number, "Find!")

        else:
            print("camera_number", camera_number, "None")
    print("接続されているカメラは", len(true_camera_is), "台です。")

     # カメラのキャプチャ
    #windowsの場合はcv2．CAP_DSHOWを第2引数にいれる  

    #カメラのIDを取得
    cams = []

    for i in true_camera_is:
        cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        cams.append(cam) 
        print("CAM_DeviceID===>"+str(cam))

    while True:
        frames = []

        for cam in cams:
            ret,i = cam.read()
            frames.append(i)
        
        img = cv2.hconcat(frames)


        #img = cv2.hconcat(frames)
        # 結果表示
        cv2.imshow("Frame",img)
 

        
        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):

            break

    for cam in cams:       
      cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    check_camera_connection()

