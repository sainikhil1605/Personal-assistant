import pyttsx3 
import speech_recognition as sr 
#datatime is used to get the time of the system to greet hime
import datetime
import wikipedia 
#webbrowser is imported to open websites in your default browser
import webbrowser
#getpass is used for geeting the username of the system it is not mandatory
import getpass
import os
import smtplib
#random is used to get a random joke in the joke database in line 37
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#change value of the 0 to 1 to get different voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    #Reads the time of the system and greets him accordingly
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    #This reads the use name of the system and greets him
    s=(getpass.getuser())
    s=s.lower()
    speak("Hi"+s+"I am your personal assistant, How may I help you!!")       

def takeCommand():
    #Function for taking the command
    r = sr.Recognizer()
    #If you get an error in the below linw please install PyAudio and try again
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        #change the language to the langauge of your choice  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    #if the system is not able to recognise then an exception will be raised and the except block is executed
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
    #The below is the list where the jokes are stored
    a=[{"joke":"Did you hear about the guy whose whole left side was cut off? He's all right now."},{"joke":"I'm reading a book about anti-gravity. It's impossible to put down."},{"joke":"I wondered why the baseball was getting bigger. Then it hit me."},{"joke":"It's not that the man did not know how to juggle, he just didn't have the balls to do it."},{"joke":"I'm glad I know sign language, it's pretty handy."},{"joke":"My friend's bakery burned down last night. Now his business is toast."},{"joke":"Why did the cookie cry? It was feeling crumby."},{"joke":"I used to be a banker, but I lost interest."},{"joke":"A drum and a symbol fall off a cliff"},{"joke":"Why do seagulls fly over the sea? Because they aren't bay-gulls!"},{"joke":"Why did the fireman wear red, white, and blue suspenders? To hold his pants up."},{"joke":"Why didn't the crab share his food? Because crabs are territorial animals, that don't share anything."},{"joke":"Why was the javascript developer sad? Because he didn't Node how to Express himself."},{"joke":"What do I look like? A JOKE MACHINE!?"},{"joke":"How did the hipster burn the roof of his mouth? He ate the pizza before it was cool."},{"joke":"Why is it hard to make puns for kleptomaniacs? They are always taking things literally."},{"joke":"Why do mermaid wear sea-shells? Because b-shells are too small."},{"joke":"I'm a humorless, cold hearted, machine."},{"joke":"Two fish in a tank. One looks to the other and says 'Can you even drive this thing???'"},{"joke":"Two fish swim down a river, and hit a wall. One says: 'Dam!'"},{"joke":"What's funnier than a monkey dancing with an elephant? Two monkeys dancing with an elephant."},{"joke":"How did Darth Vader know what Luke was getting for Christmas? He felt his presents."},{"joke":"What's red and bad for your teeth? A Brick."},{"joke":"What's orange and sounds like a parrot? A Carrot."},{"joke":"What do you call a cow with no legs? Ground beef"},{"joke":"Two guys walk into a bar. You'd think the second one would have noticed."},{"joke":"What is a centipedes's favorite Beatle song?  I want to hold your hand, hand, hand, hand..."},{"joke":"What do you call a chicken crossing the road? Poultry in moton. "},{"joke":"Did you hear about the Mexican train killer?  He had locomotives"},{"joke":"What do you call a fake noodle?  An impasta"},{"joke":"How many tickles does it take to tickle an octupus? Ten-tickles!"},{"joke":"At the rate law schools are turning them out, by 2050 there will be more lawyers than humans."},{"joke":"I've decided to sell my Hoover... well it was just collecting dust."},{"joke":"I've written a joke about a fat badger but I couldn't fit it into my set."},{"joke":"Always leave them wanting more my uncle used to say to me. Which is why he lost his job in disaster relief."},{"joke":"I was given some Sudoku toilet paper. It didn't work. You could only fill it in with number ones and number twos."},{"joke":"I wanted to do a show about feminism. But my husband wouldn't let me."},{"joke":"Money can't buy you happiness? Well check this out I bought myself a Happy Meal."},{"joke":"Scotland had oil but it's running out thanks to all that deep frying."},{"joke":"I've been married for 10 years I haven't made a decision for seven."},{"joke":"This show is about perception and perspective. But it depends how you look at it."},{"joke":"I've written a joke about a fat badger but I couldn't fit it into my set."},{"joke":"I heard a rumour that Cadbury is bringing out an oriental chocolate bar. Could be a Chinese Wispa."},{"joke":"I used to work in a shoe-recycling shop. It was sole-destroying."},{"joke":"I'm in a same-sex marriage... the sex is always the same."},{"joke":"My friend told me he was going to a fancy dress party as an Italian island. I said to him 'Don't be Sicily'."},{"joke":"I can give you the cause of anaphylactic shock in a nutshell."},{"joke":"The Pope is a lot like Doctor Who. He never dies just keeps being replaced by white men."},{"joke":"You know you are fat when you hug a child and it gets lost."},{"joke":"The universe implodes. No matter."},{"joke":"I was adopted at birth and have never met my mum. That makes it very difficult to enjoy any lapdance."},{"joke":"The good thing about lending someone your time machine is that you basically get it back immediately."},{"joke":"You know who really gives kids a bad name? Posh and Becks."},{"joke":"Last night me and my girlfriend watched three DVDs back to back. Luckily I was the one facing the telly."},{"joke":"I was raised as an only child which really annoyed my sister."},{"joke":"You know you're working class when your TV is bigger than your book case."},{"joke":"I'm good friends with 25 letters of the alphabet... I don't know Y."},{"joke":"I took part in the sun tanning Olympics - I just got Bronze."},{"joke":"Pornography is often frowned upon but that's only because I'm concentrating."},{"joke":"I saw a documentary on how ships are kept together. Riveting!"},{"joke":"I waited an hour for my starter so I complained: 'It's not rocket salad."},{"joke":"My mum's so pessimistic that if there was an Olympics for pessimism... she wouldn't fancy her chances."},{"joke":"I needed a password eight characters long so I picked Snow White and the Seven Dwarves."},{"joke":"Crime in multi-storey car parks. That is wrong on so many different levels."},{"joke":"People say 'I'm taking it one day at a time'. You know what? So is everybody. That's how time works."},{"joke":"Drive-Thru McDonalds was more expensive than I thought... once you've hired the car..."},{"joke":"I was playing chess with my friend and he said 'Let's make this interesting'. So we stopped playing chess."},{"joke":"My mother told me you don't have to put anything in your mouth you don't want to. Then she made me eat broccoli which felt like double standards."},{"joke":"I was in a band which we called The Prevention because we hoped people would say we were better than The Cure."},{"joke":"Someone asked me recently - what would I rather give up food or sex. Neither! I'm not falling for that one again wife."},{"joke":"I admire these phone hackers. I think they have a lot of patience. I can't even be bothered to check my OWN voicemails."},{"joke":"My friend died doing what he loved ... Heroin."},{"joke":"I've just been on a once-in-a-lifetime holiday. I'll tell you what never again."},{"joke":"I'm currently dating a couple of anorexics. Two birds one stone."},{"joke":"I picked up a hitch hiker. You've got to when you hit them."},{"joke":"I bought one of those anti-bullying wristbands when they first came out. I say 'bought' I actually stole it off a short fat ginger kid."},{"joke":"As a kid I was made to walk the plank. We couldn't afford a dog."},{"joke":"Being an England supporter is like being the over-optimistic parents of the fat kid on sports day."},{"joke":"What do you call a kid with no arms and an eyepatch? Names."},{"joke":"Dave drowned. So at the funeral we got him a wreath in the shape of a lifebelt. Well it's what he would have wanted."},{"joke":"For Vanessa Feltz life is like a box of chocolates: Empty."},{"joke":"Wooden spoons are great. You can either use them to prepare food. Or if you can't be bothered with that just write a number on one and walk into a pub..."},{"joke":"Hedgehogs - why can't they just share the hedge?"},{"joke":"I was watching the London Marathon and saw one runner dressed as a chicken and another runner dressed as an egg. I thought: 'This could be interesting'."},{"joke":"I had my boobs measured and bought a new bra. Now I call them Joe Cocker and Jennifer Warnes because they're up where they belong."},{"joke":"I went on a girls' night out recently. The invitation said 'dress to kill'. I went as Rose West."},{"joke":"I'm sure wherever my dad is; he's looking down on us. He's not dead just very condescending."},{"joke":"Going to Starbucks for coffee is like going to prison for sex. You know you're going to get it but it's going to be rough."},{"joke":"To the people who've got iPhones: you just bought one you didn't invent it!"},{"joke":"A spa hotel? It's like a normal hotel only in reception there's a picture of a pebble."},{"joke":"I've been reading the news about there being a civil war in Madagascar. Well I've seen it six times and there isn't."},{"joke":"I started so many fights at my school - I had that attention-deficit disorder. So I didn't finish a lot of them"}]
    s=[]
    for i in a:
        s.append(i["joke"]) 
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
        elif 'set timer for' in query:
            import time
            query=(query.replace("set timer for ",""))
            query=int(query.replace("mins",""))
            mins = 1
            # Loop until we reach query minutes running
            print("Running Time for {}".format(query))
            while mins != query+1:
                print("{}".format(mins))
                # Sleep for a minute
                time.sleep(60)
                # Increment the minute total
                mins += 1
        elif 'search google' in query:
            speak('Searching Google...')
            query = query.replace("google", "")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                print(j) 
        elif "joke" in query:
            e=s[random.randint(0,94)]
            print(e)
            speak(e)
            
        elif 'open youtube' in query:
            #the website will open in your default webbrowser
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            #the website will open in your default webbrowser
            webbrowser.open("google.com")

        elif 'open github' in query:
            #the website will open in your default webbrowser
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
        print("Done with the query waiting for further instructions")
        speak("Done with the query waiting for further instructions")


