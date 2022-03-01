import subprocess   
import progress
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    name1 = "Jarvis"
    speak("I am your Assistant")
    speak(name1)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():
    rr = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query1 = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query1}\n")

    except Exception as e1:
        print(e1)
        print("Unable to Recognize your voice.")
        return "None"

    return query1


def sendEmail(to1, content1):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to1, content1)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "F:\\mob backup\\Audio\\audios"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            name1 = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            name1 = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(name1)
            print("My friends call me", name1)

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Gaurav.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "EWGWUT-6L7YG93QHK"
            client = wolframalpha.Client(app_id)
            ind = query.lower().split().index('calculate')
            query = query.split()[ind + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'ppt' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\niroo\Downloads\\VoiceAssistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Neeroop")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Neeroop ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org/v2/top-headlines?country=in&apiKey=ceb58e1bdd5843d1a31407c0bc787303''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news of india')
                print('''=============== Top News OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm1 = takeCommand()
            if 'yes' in snfm1 or 'sure' in snfm1:
                strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%I%p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)
        elif "jarvis" in query:

            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            speak(name1)

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "c32a08e413a226cc307e5195418cf171"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric";
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(base_url.format(city_name, api_key))
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

                speak(" Temperature (in kelvin unit) is " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) is" + str(
                    current_pressure) + "\n humidity (in percentage) is " + str(
                    current_humidiy) + "\n description is " + str(weather_description))
            else:
                speak(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(name1)

        # most asked question from google Assistant

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("EWGWUT-6L7YG93QHK")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "bye" in query:
            speak("Thank you for giving me your time!!")
            exit(0)



