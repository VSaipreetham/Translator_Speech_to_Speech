import speech_recognition as sr
import playsound
import googletrans
import pyttsx3
import gtts

engine = pyttsx3.init()


rate = engine.getProperty('rate')
engine.setProperty('rate',150)
volume=engine.getProperty('volume')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Please say to preetham translator we will translate it....")
engine.runAndWait()

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'te'
output_lang = 'es'
try:
    with sr.Microphone() as source:
        print('Please speak now')
        voice = recognizer.listen(source)
        voice = recognizer.recognize_google(voice, language=input_lang)
        print(voice)
except:
    print("Mic not working")
    pass

translated = translator.translate(voice, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text,lang=output_lang)
converted_audio.save('voice.mp3')
playsound.playsound('voice.mp3')