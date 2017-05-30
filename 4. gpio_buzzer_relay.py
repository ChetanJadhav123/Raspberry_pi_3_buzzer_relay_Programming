import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)

while 1:
    GPIO.output(18, False)
    sleep(1)
    GPIO.output(18, True)
    sleep(1)
