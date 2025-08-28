import requests
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    api_key = "2c1d2cbf97a7f8d316e8f913e8e819ed"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None

    temp = round(data["main"]["temp"]) 
    description = data["weather"][0]["main"]  
    detail = data["weather"][0]["description"]  

    return f"Today in {city}, it's {temp}°C with {description} ({detail})."

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return None

if __name__ == "__main__":
    speak("Welcome, Which city's weather would you like me to report?")
    while True:
        city = listen()
        if city:
            print("You said:", city)
            weather_report = get_weather(city)
            if weather_report:
                print(weather_report)
                speak(weather_report)
                break
            else:
                speak(f"Sorry, I couldn't find weather for {city}. Please say again.")
        else:
            speak("I didn't catch that. Please say the city name again.")
