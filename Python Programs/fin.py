import RPI.GPIO as GPIO
import time
GPIO.setmode(GPIO,BOARD)
GPIO.setwarnings(False)
led1=16
but1=18
led2=12
but2=22
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(but1,GPIO.IN,pull_up_down=GPIO.PUD_up)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(but2,GPIO.IN,pull_up_down=GPIO.PUD_up)
bs1=False
bs2=False
while True:
    if(GPIO.input(but1)==0):
        print("button 1 pressed")
        if(bs1==False):
            GPIO.output(led1,True)
            bs1=True
            time.sleep(0.4)
        else:
            GPIO.output(led1,False)
            bs1=False
            time.sleep(0.4)
    if(GPIO.input(but2)==0):
        print("button 1 pressed")
        if(bs2==False):
            GPIO.output(led1,True)
            bs2=True
            time.sleep(0.4)
        else:
            GPIO.output(led1,False)
            bs2=False
            time.sleep(0.4)


