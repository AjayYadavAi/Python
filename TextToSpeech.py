from gtts import gTTS
import os

string="Hello How are you ?"
def say(s):
	tts = gTTS(text=s, lang='en')
	tts.save("good.mp3")
	os.system("mpg123 good.mp3")


say("enter your name :")
name=raw_input("Enter your name :")
say('Hello' + name + '   Nice to meet you')


 