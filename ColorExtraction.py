import numpy as np
import cv2
# ________色抽出__________#
image = cv2.imread('./driver.jpg') # ファイル読み込み
hsvLower = np.array([150, 0, 0])    # 抽出する色の下限
hsvUpper = np.array([179, 255, 255])    # 抽出する色の上限
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 画像をHSVに変換
hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
# result = cv2.bitwise_and(image, image, mask=hsv_mask) # 元画像とマスクを合成

# ________ノイズ処理__________#
blur = cv2.medianBlur(hsv_mask,9)
kernel = np.ones((15,15),np.uint8)# カーネルサイズ
opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)# オープニング処理
mask_opening = cv2.bitwise_and(image, image, mask=opening) # マスク処理
closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)# クロージング処理
mask_closing = cv2.bitwise_and(image, image, mask=closing) # マスク処理

# ________輪郭検出__________#
img,contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = []
for cnt in contours:
    area.append(cv2.contourArea(cnt))
area_max = area.index(max(area))
image_copy = image.copy()
image_outline = cv2.drawContours(image_copy, contours,area_max, (0,255,0), 3)

# ________重心位置と描画__________#
M = cv2.moments(contours[area_max])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv2.circle(image_outline, (cx,cy), 5, (0, 255, 255), -1)

#_________上下左右の端点位置と描画＿＿＿＿#
leftmost = tuple(contours[area_max][contours[area_max][:,:,0].argmin()][0])
rightmost = tuple(contours[area_max][contours[area_max][:,:,0].argmax()][0])
topmost = tuple(contours[area_max][contours[area_max][:,:,1].argmin()][0])
bottommost = tuple(contours[area_max][contours[area_max][:,:,1].argmax()][0])
cv2.circle(image_outline,(leftmost), 5, (255, 0, 0), -1)
cv2.circle(image_outline,(rightmost), 5, (255, 0, 0), -1)
cv2.circle(image_outline,(topmost), 5, (255, 0, 0), -1)
cv2.circle(image_outline,(bottommost), 5, (255, 0, 0), -1)

while True:
    # キー入力を1ms待って、keyが「q」だったらbreak
    cv2.imshow('blur',blur)
    cv2.imshow('openig_mask', opening)
    cv2.imshow('opening_result',mask_opening)
    cv2.imshow('closing_mask', closing)
    cv2.imshow('closing_result',mask_closing)
    cv2.imshow('image_outline',image_outline)
  

    key = cv2.waitKey(1)&0xff
    if key == ord('q'):
        break
cv2.destroyAllWindows()



