# Weather Voice Assistant 🌤️🎙️

A Python-based voice-controlled weather application that provides real-time weather updates through speech recognition and text-to-speech capabilities. This project demonstrates API integration, voice processing, and real-time data retrieval.

## Features
- 🎤 **Voice Recognition** - Speech-to-text conversion for city input
- 🔊 **Voice Feedback** - Text-to-speech weather reports
- 🌡️ **Real-time Weather Data** - Live weather information from OpenWeatherMap API
- 🌍 **Global City Support** - Weather data for cities worldwide
- ⚡ **Instant Responses** - Quick weather updates with temperature and conditions
- 🔄 **Error Handling** - Robust handling of invalid inputs and API errors

## Installation & Setup

### Prerequisites
- Python 3.6+
- Microphone hardware
- Internet connection
- OpenWeatherMap API key

### Required Libraries
pip install requests speechrecognition pyttsx3 pywin32

## API Setup
1. Get free API key from OpenWeatherMap
2. Replace api_key in code with your actual key.

## Usage Examples
### Typical Interaction
- Assistant: "Welcome, Which city's weather would you like me to report?"
- User: "London" (spoken)
- Assistant: "Today in London, it's 15°C with Clouds (overcast clouds)."

## Supported Input Formats
- Single city names: "London"
- City with country: "New York"
- Any city worldwide with available weather data

## Project Structure
### Core Components
- OpenWeatherMap API - Real-time weather data retrieval
- SpeechRecognition - Audio input processing
- pyttsx3 - Text-to-speech conversion
- Requests - HTTP API communication

### Key Functions
- get_weather(city) - Fetches weather data from API
- speak(text) - Converts text to audio output
- listen() - Captures and processes voice input

## API Response Handling
The application processes:

- Temperature in Celsius (rounded)
- Weather condition (main description)
- Detailed weather description
- Error codes and invalid city handling

## Technologies Used
- Python 3.x - Core programming language
- OpenWeatherMap API - Weather data provider
- SpeechRecognition - Google Speech API integration
- pyttsx3 - Offline text-to-speech engine
- Requests - HTTP library for API calls

## Learning Outcomes
- REST API integration and JSON parsing
- Speech recognition implementation
- Text-to-speech conversion
- Error handling and user feedback
- Real-time data processing
- Voice-based user interfaces

## Future Enhancements
- Multi-day weather forecasts
- Weather alerts and notifications
- Multiple temperature units (Celsius/Fahrenheit)
- Location detection via IP address
- Graphical weather display
- Multilingual support
- Weather history and trends

## Important Notes
- Requires valid OpenWeatherMap API key
- Internet connection mandatory for API calls and speech recognition
- Microphone needed for voice input
- API has rate limits (60 calls/minute for free tier)

