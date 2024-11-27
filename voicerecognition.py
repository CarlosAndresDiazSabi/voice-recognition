# -*- coding: utf-8 -*-
"""voicerecognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EFDS1AW27YcT0mxeJn8cx9u59wXzZO8c
"""

#Install SpeechRecognition with pip install SpeechRecognition
# Install pyttsx3 with pip install pyttsx3

# https://www.temu.com/

!pip install SpeechRecognition
!pip install pyttsx3
!pip install eSpeak

import webbrowser
import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
  microphone = sr.microphone()
  with mic as source:
    audio = recognizer.listen(source)
  text = recognizer.recognize_google(audio, lenguage = "ES")

  print(f"Has dicho {text}")
  return text.lower()

if "temu" in talk():
  ingine.say(f"Que quieres comprar en temu ")
  ingine.runAndWait()
  text = talk()
  webbrowser.open(f"https://www.temu.com/{text}")