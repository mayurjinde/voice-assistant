import datetime
import os
import webbrowser
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Anya Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...") 
        speak("Say that again please") 
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        query = query.lower()

        if 'how are you' in query:
            speak("i am doing good sir")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print({strTime})
            speak(f"Sir, the time is {strTime}")

        elif 'youtube' in query:
            print("Opening youtube...")
            speak("opening youtube")
            webbrowser.open("youtube.com")

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("in", "")
            results = wikipedia.summary(query, 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google","")
            query = query.replace("google","")

            try:
                result = googleScrap.summary(query,1)
                query = query.replace(" ","+")
                url = 'https://www.google.co.in/search?q='
                search = url+query
                webbrowser.open(search)
                speak(result)

            except:
                speak("say that again please")

        elif 'stack overflow' in query:
            print("Opening stack overflow...")
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")

        elif 'screenshot' in query: 
            im = pyautogui.screenshot()
            im.save("ss.jpeg")
            codePath = "C:\\Users\\Mayur Jinde\\Downloads\\IT351\\Project\\IT351 Project\\ss.jpeg"
            os.startfile(codePath)
   

        elif 'course plan' in query:
            print("Opening the course plan...")
            speak("opening the course plan")
            codePath = "C:\\Users\\Mayur Jinde\\Downloads\\IT351\\Project\\IT351 Project\\HCI_IT351 Course Plan 2023.docx"
            os.startfile(codePath)

        elif 'music' in query:
            music_dir = 'C:\\Users\\Mayur Jinde\\Downloads\\IT351\\Project\\IT351 Project\\faded.mpeg'
            os.startfile(music_dir)

        elif 'tell me a tongue twister' in query:
            print("Betty bought a bit of butter but the butter was bitter, so betty bought a bit of better butter to make the bitter butter better")
            speak("Betty bought a bit of butter but the butter was bitter, so betty bought a bit of better butter to make the bitter butter better")


        elif 'exit' in query:
            print("Have a good day sir")
            speak("Have a good day sir")
            exit()