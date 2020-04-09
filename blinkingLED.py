import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)  # set GPIO physical pin no 7

for i in range(10):
    GPIO.output(7, True)  # switch on pin 7
    print("LED on")

    time.sleep(1)

    GPIO.output(7, False)  # switch off pin 7
    print("LED off")

    time.sleep(1)

print("Done")
GPIO.cleanup()  # resets GPIO port