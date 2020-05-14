import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import getpass
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#change value of the 0 to 1 to get different voice
engine.setProperty('voice', voices[0].id)


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
    s=(getpass.getuser())
    s=s.lower()
    speak("Hi"+s+"I am your personal assistant, How may I help you!!")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        #change the language to the langauge of your choice  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Repeat please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found") 
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'search google' in query:
            speak('Searching Google...')
            query = query.replace("google", "")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                print(j) 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")   
        elif 'open' in query:
            query=query.replace("open","")
            query=query+".com"
            webbrowser.open(query)
        elif 'play music' in query:
            music_dir = 'Enter your music directory'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to Mike' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mikeEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry...Try again") 
        elif(query!="none"):
            print("Here are the google results for your search")
            speak("Here are the google results for your search")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                print(j)
        else:
            speak("Sorry Didn't get you speak again")


