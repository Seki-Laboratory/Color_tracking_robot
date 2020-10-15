import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)

    #----------------moter_assign---------------#
    #
    #    FL_moter  / / ｜-----｜ / /  FR_moter
    #                  ｜     ｜
    #                    robot
    #                  ｜     ｜
    #    BL_moter  / / ｜-----｜ / /  BR_moter
    #
    #-------------------------------------------#

#  FL_moter
FL_pin = 26
FL_dir1 = 19
GPIO.setup(FL_pin,GPIO.OUT)
GPIO.setup(FL_dir1,GPIO.OUT)
#  FR_moter
FR_pin = 13
FR_dir1 = 6
GPIO.setup(FR_pin,GPIO.OUT)
GPIO.setup(FR_dir1,GPIO.OUT)
#  BL_moter
BL_pin = 21
BL_dir1 = 20
GPIO.setup(BL_pin,GPIO.OUT)
GPIO.setup(BL_dir1,GPIO.OUT)
#  BR_moter 
BR_pin = 16
BR_dir1 = 12
GPIO.setup(BR_pin,GPIO.OUT)
GPIO.setup(BR_dir1,GPIO.OUT)

pwmFL = GPIO.PWM(FL_pin,200)
pwmFR = GPIO.PWM(FR_pin,200)
pwmBL = GPIO.PWM(BL_pin,200)
pwmBR = GPIO.PWM(BR_pin,200)

def moter(FLspeed,FRspeed,BLspeed,BRspeed):
    if FLspeed > 0:
        GPIO.output(FL_dir1,True)
    else:
        GPIO.output(FL_dir1,False)
    
    if FRspeed > 0:
        GPIO.output(FR_dir1,True)
    else:
        GPIO.output(FR_dir1,False)

    if BLspeed > 0:
        GPIO.output(BL_dir1,True)
    else:
        GPIO.output(BL_dir1,False)
    
    if BRspeed > 0:
        GPIO.output(BR_dir1,True)
    else:
        GPIO.output(BR_dir1,False)
    
    pwmFL.start(abs(FLspeed))  
    pwmBL.start(abs(FLspeed))
    pwmFR.start(abs(FLspeed))  
    pwmBR.start(abs(FLspeed))

def cleanup():
    GPIO.cleanup()
    pwmFL.start(0)  
    pwmBL.start(0)
    pwmFR.start(0)  
    pwmBR.start(0)
