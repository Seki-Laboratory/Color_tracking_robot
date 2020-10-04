# Color_tracking_robot
ラズパイ上で動作する

# raspi_i2c
## Raspberry PiのI2Cを有効にする
Raspberry PiのI2C接続をraspi-configを使って有効にします。
$sudo raspi-config
『5 Interfacing Options 』⇒『P5 I2C』⇒『はい』
## Raspberry Piでの通信の準備と通信確認
$sudo apt-get update
$sudo apt-get upgrade
$ sudo apt-get dist-upgrade
$sudo apt-get install python-dev and python3-dev
$sudo apt-get -y install python-smbus i2c-tools
$sudo i2cdetect -y 1

以下のようにArduinoのI2Cチャンネル0x04が表示されれば通信はうまくいっています。

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- 04 -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
