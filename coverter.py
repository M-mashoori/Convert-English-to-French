import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the recognizer and translator
r = sr.Recognizer()
translator = Translator()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Speak Now")
    audio = r.listen(source)
    
    try:
        # Recognize speech using Google Web Speech API
        speech_text = r.recognize_google(audio)
        print("You said:", speech_text)

        # Translate the recognized speech to French
        translated_text = translator.translate(speech_text, dest='Urdu').text
        print("Translated to French:", translated_text)

        # Convert the translated text to speech
        tts = gTTS(translated_text, lang='Urdu')
        tts.save("translated_speech.mp3")
        
        # Play the translated speech using the default media player
        os.system("start translated_speech.mp3")

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
