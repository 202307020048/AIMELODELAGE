import pyttsx3 as pyt
x = pyt.init()
voices = x.getProperty('voices')
x.setProperty('voice', voices[1].id)
x.say(input())
x.runAndWait()
