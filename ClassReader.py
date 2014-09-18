#! /usr/bin/python
# -*- coding: utf-8-*-

from tts import *
from datetime import date
import RPi.GPIO as GPIO
from time import sleep, time
import random

classes = [u"明天是周一，课程有：班队会，语文，语文，品德与生活，校本习惯，语文，体育活动", 
           u"明天是周二，课程有：数学，外语，体育，语文，校本或语文，校本或语文",
           u"明天是周三，课程有：数学，语文，音乐，美术，外语，体育",
           u"明天是周四，课程有：数学，语文，美术，品德与生活，体育，专题教育",
           u"明天是周五，课程有：数学，语文，书法，外语，音乐，体育",
           u"明天是休息日, 祝你周末愉快!",
           u"明天是休息日, 祝你周末愉快!" ]

wishes = [u"祝你有一个好心情!", u"祝你过得开心!", u"祝你好运!", 
          u"加油吧,未来的科学家!", u"祝你学到更多的知识!",
          u"我等着你来不断改进我的功能哦!", u"祝你度过丰富多彩的一天",
          u"报告完毕，长官!"]

last_report_time = 0

def on_change(channel):
  global last_report_time
  if (time() - last_report_time) < 1:
    return

  print "start to report class"
  todayIndex = (date.today().weekday()+1)%7
  speaker.speakText(classes[todayIndex])
  speaker.speakText(random.choice(wishes))
  last_report_time = time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
  GPIO.add_event_detect(25, GPIO.RISING, callback=on_change, bouncetime=1000)
  while(True):
    sleep(10)
except KeyboardInterrupt:
  GPIO.cleanup()
finally:
  GPIO.cleanup()
