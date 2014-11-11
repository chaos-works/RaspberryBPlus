# -*- coding: utf-8 -*-

# http://kampis-elektroecke.de/?page_id=3740
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and
# https://pypi.python.org/pypi/RPi.GPIO
# Original : http://spaceblogs.org/2013/06/03/shut-down-your-raspberry-pi-on-but
# Modified by 김영규 2014년 10월 28일
# http://cafe.naver.com/audiostudy
# Naver Cafe : 좌충우돌 PC-FI오디오

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

print ("Press Button to shutdown")
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

def Int_shutdown(channel):
        # 볼루미오를 종료함.
        GPIO.output(24, True) #종료처리중임을 알리는 LED를 On
        print "button Pressed >> shutdown rpi..."
        time.sleep(3)

        os.system("sudo shutdown -h now")

GPIO.add_event_detect(23, GPIO.FALLING, callback = Int_shutdown, bouncetime = 20

#종료버튼이 눌려질때 까지 대기함.
while 1:
        time.sleep(1)
