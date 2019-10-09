import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	print("hello say any anthing")
	audio=r.listen(source)
	try:
		text=r.recognize_google(audio)
		print("you sai:{}".format(text))
	except:
		print("sorry")