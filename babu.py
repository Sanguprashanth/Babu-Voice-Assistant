# Project Name: Babu ( Voice Assistant )
# Libraries
import speech_recognition as sr   # for converting speech to text
import pyttsx3                    # for text to speech conversion
import datetime         # to access system time
import webbrowser       # used to access websites
# intitalize text to speech engine
engine = pyttsx3.init()
# This function will speak the text passed to it
def speak(text):
    voices = engine.getProperty('voices')  # bring list of voices
    engine.setProperty('voice', voices[1].id) # choose the voice
    engine.say(text)
    engine.runAndWait()
# This function will listen your voice command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language = 'en-in' )  #'hi-in', 'te-in'
            print("Your Command:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I am not able to understand")
            speak("Sorry, I am not able to understand")
            return ""
        except sr.RequestError:  
            print("Speech service not available")
            speak("Speech service not available")
            return ""
def run_assistant():
    speak("Hello, I am your Baby Siri. How I can help you")
    while True:
        command = listen()
        if 'time' in command:
            now = datetime.datetime.now()
            speak(f"Right now time is {now}")
        elif 'today date' in command:
            today = datetime.date.today().strftime("%B %d, %y")
            speak(f"Todays date is {today}")
        elif 'open google' in command:
            speak("Ok Sir, let me open google for you")
            webbrowser.open("https://www.google.com/")
        elif 'exit' in command or 'stop' in command or 'go to hell' in command:
            speak("Okey bye bye, you also go to hell")
            break
        else:
            speak("What the hell you are speaking")
run_assistant()