import speech_recognition as sr
import pyttsx3
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hemo():
	engine=pyttsx3.init()
	engine.say("hello dude developer")
	engine.runAndWait()
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("hello say any anthing")
		audio=r.listen(source)
		try:
			text=r.recognize_google(audio)
			print("you sai:{}".format(text))
			engine=pyttsx3.init()
			engine.say(text)
			engine.runAndWait()
		except:
			engine=pyttsx3.init()
			engine.say("oooluugaaa peesu")
			engine.runAndWait()
	return "say anything"
if __name__ == '__main__':
	app.run(debug=True)