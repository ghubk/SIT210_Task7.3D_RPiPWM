
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO_TRIG = 16
GPIO_ECHO = 18
BUZZER = 33

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.output(BUZZER, True)

buz = GPIO.PWM(BUZZER, 0.1)
buz.start(1)

def setfrequency(meseaured_dis):
    if meseaured_dis < 50 and meseaured_dis > 40:
        return 2
    if meseaured_dis < 40 and meseaured_dis > 30:
        return 4
    if meseaured_dis < 30 and meseaured_dis > 20:
        return 6
    if meseaured_dis < 20 and meseaured_dis > 10:
        return 8
    if meseaured_dis < 10:
        return 10
    if meseaured_dis < 5:
        return 12
    if meseaured_dis > 50:
        return 0.25
    else:
        return 0.25


def distance():
    GPIO.output(GPIO_TRIG, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    timeElapsed = StopTime - StartTime
    
    distance = (timeElapsed * 34300)/2
    return distance



if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            freq = setfrequency(dist)
            buz.ChangeFrequency(freq)
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        buz.stop()



