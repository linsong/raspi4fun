#! /usr/bin/python
# -*- coding: utf-8-*-

import os
import urllib
import md5
import subprocess

def cachedFilePath(url):
  m = md5.new()
  m.update(url)
  soundFilePath = os.path.join(os.path.dirname(__file__), "cache", m.hexdigest())
  return soundFilePath

def speakText(phrase, tl="zh-CN"):
  user_agent = "'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0)'"
  encoded_params = urllib.urlencode({"q": phrase.encode('utf-8'), "tl": tl})
  googleSpeechURL = "http://translate.google.com/translate_tts?" + encoded_params
  filePath = cachedFilePath(googleSpeechURL)
  if not os.path.exists(filePath):
    subprocess.check_call(["wget", "-O", filePath, "--user-agent", user_agent, googleSpeechURL], shell=False)
  subprocess.call(["mpg123", filePath], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
