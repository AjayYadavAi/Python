from gtts import gTTS
import webbrowser as wb
import time
import os

string="Hello How are you ?"
def say(s):
	tts = gTTS(text=s, lang='en')
	tts.save("good.mp3")
	os.system("mpg123 good.mp3")

say("enter your name :")
name=raw_input("Enter your name :")
say('Hello' + name + '   Nice to meet you')
say("Enter your     age    ")
age=raw_input("Age :")
say("you are  "+age)
say("Enter you question  :")
qtime=['what is time','time','time please ','current time','what\'s time']
website=['youtube','google','facebook','quora','w3schools','github','linkedin']
q=raw_input("Q :")
if q in qtime:
	ans=time.strftime("%H : %M ")
	say('time   isss  ' + ans)

elif q in website:
	say("Wait i am looking on the webbrowser  :")
	url='http://'+website[q]+'.com'
	wb.open_new_tab(url)
else:
	say("Wait i looking on the web .....:")
	url="https://www.google.co.in/search?dcr=0&ei=nCTQWsJMgYu9BKyamVg&q="+q+"&oq="+q+"&gs_l=psy-ab.3..33i22i29i30k1.874443.884343.0.884585.41.32.0.0.0.0.476.5061.0j2j8j5j2.17.0....0...1.1.64.psy-ab..24.16.4876...0j35i39k1j0i67k1j0i131i67k1j0i131k1j0i20i263k1j0i131i20i263k1.0.tUQBgicFMzo"
	wb.open_new_tab(url)



 