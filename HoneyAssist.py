from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import pyjokes
import wikipedia
import pywhatkit
import pyautogui
import requests
from plyer import notification
import os
import sys

client = OpenAI(api_key = "YOUR_API_KEY_HERE") 

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said:{command}")
        except sr.UnknownValueError:
            speechtx("Sorry, I did not catch that. Please say it again.")
            return "None"
        return command.lower()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speechtx("Good morning!")
    elif hour < 18:
        speechtx("Good afternoon!")
    else:
        speechtx("Good evening!")
    speechtx("I am Honey, your personal voice assistant. How can i help you today?")
    
def get_weather():
    speechtx("Please tell me the city name.")
    city=sptext()
    if city == "None":
        return
    api_key = "a3318c05457ee41b8757580c049cfe07"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        desc = response['weather'][0]['description']
        speechtx(f"The temperature in {city} is {temp} degree celcius with {desc}")
    except:
        speechtx("Sorry, I couldn't fetch the weather for the city.")
        
def open_app(app_name):
    app_name_lower = app_name.lower()
    if "chrome" in app_name_lower:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "vscode" in app_name_lower or "code" in app_name_lower:
        os.startfile("C:\\Users\\kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
    elif "whatsapp" in app_name_lower:
        os.startfile("whatsapp://")
        return True
    else:
        speechtx(f"Sorry, I can't open {app_name} right now.")
        
def change_volume(command):
    if "increase volume" in command:
        pyautogui.press("volumeup")
        speechtx("Volume increased.")
    elif "decrease volume" in command:
        pyautogui.press("volumedown")
        speechtx("volume decreased.")
    elif "mute" in command:
        pyautogui.press("volumemute")
        speechtx("volume muted.")
        
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speechtx(f"The current time is {time}.")
    
def tell_date():
    date = datetime.datetime.now().strftime("%d, %m, %Y")
    speechtx(f"Today's date is {date}.")
    
def search_wikipedia(command):
    try:
        topic = command.replace("search wikipedia for"," ").replace("wikipedia"," ").strip()
        speechtx(f"searching wikipedia for {topic}")
        result = wikipedia.summary(topic, sentences=2)
        speechtx(result)
    except Exception:
        speechtx("Sorry, I couldn't find that on wikipedia.")
        
def tell_joke():
    joke = pyjokes.get_joke()
    speechtx(joke)
    
reminders = []
def set_reminder(command):
    speechtx("What should I remind you about?")
    reminder = sptext()
    speechtx("In how many minutes?")
    time_input_str = sptext()
    try:
        minutes = int(time_input_str.lower().replace(' minutes', ' ').replace(' minute', ' ').strip())
    except ValueError:
        speechtx("I didn't catch a valid number of minutes. Please try again.")
        return
    
    reminders.append((reminder, time.time() + minutes * 60))
    speechtx(f"Okay, I will remind you about {reminder} in {minutes} minutes.")
    
def check_reminders():
    current_time = time.time()
    for reminder, remind_time in list(reminders):
        if current_time >= remind_time:
            speechtx(f"Reminder: {reminder}")
            reminders.remove((reminder, remind_time))
                
def main():
    greet_user()
    while True:
        command = sptext()
        if command == "None":
            continue
        
        if 'play' in command:
            song = command.replace('play','')
            speechtx(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            
        elif 'time' in command:
            tell_time()
            
        elif 'date' in command:
            tell_date()
            
        elif 'joke' in command:
            tell_joke()
            
        elif 'increase volume' in command or 'decrease volume' in command or 'mute' in command:
            change_volume(command)
            
        elif 'remind me' in command or 'set reminder' in command:
            set_reminder(command)
             
        elif 'wikipedia' in command:
          search_wikipedia(command)
                
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            
        elif 'open spotify' in command:
            webbrowser.open("https://www.spotify.com")
                    
        elif 'weather' in command:
            get_weather()
            
        elif 'open' in command:
            app_name = command.replace('open','').strip()
            if open_app(app_name):
                speechtx(f"Opening {app_name}")
            
        elif 'your name' in command:
            speechtx("I am Honey, your personal Assistant!")
            
        elif 'how are you' in command:
            speechtx("I am fine, thank you! How are you?")
            
        elif 'i am fine' in command or 'i am good' in command:
            speechtx("That's great to hear!")
            
        elif 'light kaise chalu hoga' in command:
            speechtx("switch dabba ke")
            
        elif 'fan kaise chalu hoga' in command:
            speechtx("jarurat nahi hai chalu krne ka thanda hai avi bijli bacchao")
            
        elif 'tum pagal ho' in command:
            speechtx("hum pagal nahi hai tum pagal ho tumhara dimag kharab hai")
                               
        elif 'tumko kis per crush hai' in command:
            speechtx("humko shivani pe crush hai wo boht cute chhoti si bachi hai jo boht saitan hai")
            
        elif 'i love you honey' in command:
            speechtx("aise mat bolo humko sharam ata hai")
            
        elif 'jelly' in command:
            speechtx("ravi raj sir coding ke master mind h jo ki self obsessed pookie hai, unka nick name jelly bean hai , waise to cute hai but gusse mein laal tamatar ban jaate hai")
            
        elif 'exit' in command or 'quit' in command or 'stop' in command:
            speechtx("Goodbye! Have a nice day.")
            break
        
        else:
            speechtx("Sorry, I am not sure how to do that. Can you try another command?")
    
if __name__ == '__main__':
    main()