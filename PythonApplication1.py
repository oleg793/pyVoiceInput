import keyboard
import speech_recognition as sr
import config
import os

r = sr.Recognizer()
print("To stop dicting say exit")
while(True):
	with sr.Microphone(device_index=1) as source:
		print("Say!")
		audio=r.listen(source)
	try:
		query = r.recognize_google(audio, language=config.lang)
	except:
		print("error")

	if(query.lower() == config.exit):
		print("exiting")
		break
	elif(query.lower() == config.backspace):
		keyboard.write("\b");
	elif(query.lower() == config.select_all):
		keyboard.press_and_release("ctrl+a")
	elif(query.lower() == config.dot):
		keyboard.write("\b");
		keyboard.write(". ")
	elif(query.lower() == config.open_editor):
		file_path = config.editor;
		os.system("start "+file_path)
	elif(query.lower() == config.save):
		keyboard.press_and_release("ctrl+s")
	elif(query.lower() == config.close):
		keyboard.press_and_release("alt+f4")
	else:
		keyboard.write(query.lower() + ' ')