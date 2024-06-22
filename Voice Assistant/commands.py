import webbrowser
from speech import speak
from youtube import get_first_youtube_result
from weather import get_weather
from jokes import get_joke
from news import get_news
from tasks import added_to_schedule, your_schedule
from email import send_email
import speech_recognition as sr

recognizer = sr.Recognizer()

def process_command(command):
    print(f"Processing command: {command}")
    command = command.lower()

    if "open" in command:
        site = command.split("open ")[-1].strip()
        common_sites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "facebook": "https://www.facebook.com",
            "twitter": "https://www.twitter.com",
        }   

        if site in common_sites:
            url = common_sites[site]
        else:
            if not site.startswith("http"):
                if "." not in site:
                    site += ".com"
                url = "https://" + site
            else:
                url = site

        speak(f"Opening {site}")
        webbrowser.open(url)

    elif "play" in command:
        song = command.split("play ")[-1].strip()
        video_url = get_first_youtube_result(song)
        if video_url:
            speak(f"Playing {song} on YouTube")
            webbrowser.open(video_url)
        else:
            speak("Sorry, I couldn't find the song on YouTube.")
                
    elif "search" in command:
        query = command.split("search ")[-1].strip()
        speak(f"Searching for {query} on Google")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)

    elif "weather" in command:
        location = command.split("weather in ")[-1].strip()
        weather_report = get_weather(location)
        speak(weather_report)

    elif "add to my schedule" in command:
        task = command.split("add to my schedule ")[-1].strip()
        result = added_to_schedule(task)
        speak(result)

    elif "what's my schedule" in command:
        result = your_schedule()
        speak(result)
        
    elif "tell me a joke" in command:
        joke = get_joke()
        speak(joke)

    elif "news" in command:
        news_report = get_news()
        speak(news_report)
        
    elif "send email" in command:
        from_ = "ajeet1973.at@gmail.com"
        speak("To whom should I send the email?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            to_mail = input(speak(": Enter the recievers email :"))
            
        speak("What is the subject?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            subject = recognizer.recognize_google(audio)
        speak("What should I say?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            message = recognizer.recognize_google(audio)
        email_status = send_email(subject, message, to_mail, from_)
        speak(email_status)

    elif command:
        search_for = command.split("jarvis")[-1].strip()
        speak(f"Searching for {search_for} on Google")
        search_url = f"https://www.google.com/search?q={search_for}"
        webbrowser.open(search_url)

    else:
        speak("Sorry, I don't know how to do that.")
