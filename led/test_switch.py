import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def on_change(channel):
  print GPIO.input(channel)

try:
  GPIO.add_event_detect(25, GPIO.RISING, callback=on_change, bouncetime=200)
  sleep(5)
except KeyboardInterrupt:
  GPIO.cleanup()
finally:
  GPIO.cleanup()
