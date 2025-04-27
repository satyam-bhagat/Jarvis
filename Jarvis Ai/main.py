import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
import together



recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api="84cd197fac12481597d1770f01656a05"

def speak(text):
    engine.say(text)
    engine.runAndWait()



def Ai_integration(command):
    client = together.Together(
        api_key="f1b7d081abfcb857cad05a63ab3950ec005ca3d8bc9e355e077233b1eee4f6cb"
    )

    stream = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[
            {
                "role": "user",
                "content": command,
            }
        ],
        stream=True,
    )

    full_response = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            full_response += content

    return full_response


def processcommand(c):
    print(f"Processing command: {c}")
    command_lower = c.lower()
    
    if "open google" in command_lower:
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in command_lower:
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in command_lower:
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in command_lower:
        webbrowser.open("https://www.linkedin.com/")
    elif command_lower.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song_requested = parts[1].strip().lower()
            found = False
            for song_name, link in musiclib.music.items():
                if song_requested in song_name.lower():
                    webbrowser.open(link)
                    speak(f"Playing {song_name}")
                    found = True
                    break
            if not found:
                speak("Sorry, song not found.")
        else:
            speak("Please say the song name after 'play'.")
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=84cd197fac12481597d1770f01656a05")

        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=84cd197fac12481597d1770f01656a05"

# Fetch data
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Check if response is successful
        if data["status"] == "ok":
            articles = data["articles"]
            
            print("\nTop News Headlines:\n")
            for i, article in enumerate(articles, 1):
                print(f"{i}. {article['title']}")
                speak(article['title'])

        else:
            print("Failed to fetch news. Please check your API key or request.")
        


    else:
        output=Ai_integration(c)
        speak(output)


if __name__ == "__main__":
    speak("Starting Jarvis")
    while True:
        print("Waiting for activation word...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for activation...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            if command.lower() == "jarvis":
                speak("Hello, I am listening now.")
                print("Jarvis Activated...")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")

                processcommand(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected. Waiting again...")
        except sr.UnknownValueError:
            print("Could not understand audio. Please speak clearly.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")





