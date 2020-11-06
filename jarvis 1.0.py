import pyttsx3
import datetime
import speech_recognition as sr # pip install speech recognition

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M") #for 24 hour clock
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back ERIZTA!")
    time_()
    date_()

    #Greetings
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Madam!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Madam!")
    else:
        speak("Good Night Madam!")
    
    speak("Alain at your service. Please tell me how can I help you?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.adjust_for_ambient_noise(source)
        print("Say something ...")
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()

    while True:
        query = TakeCommand().lower()

        #All commands will be stored in lower case in query

        if 'time' in query: 
            time_()

        if 'date' in query:
            date_()