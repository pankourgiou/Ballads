from gtts import gTTS
import os
text = "Try listenning Dream Theater band ballads"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
