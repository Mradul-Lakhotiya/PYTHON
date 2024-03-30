# Import necessary libraries
import pyttsx3  # Text to speech library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # Open websites
import datetime  # Get current time
import pyjokes  # Retrieve jokes
import time  # Provide delay

# Function to convert speech to text
def speechToText():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening......")
            audio = recognizer.listen(source)

            try:
                print("Recognizing.....")
                
                # Convert speech to text using Google Speech Recognition API
                data = recognizer.recognize_google(audio)
                print(data)
                return data.lower()

            except sr.UnknownValueError:
                print("Did not Understand")
        
        time.sleep(3)

# Function to convert text to speech
def textToSpeech(data):
    text_to_speech_engine = pyttsx3.init()

    voices = text_to_speech_engine.getProperty('voices')
    text_to_speech_engine.setProperty('voice', voices[0].id)

    text_to_speech_engine.setProperty('rate', 150)

    text_to_speech_engine.setProperty('volume', 1.0)

    text_to_speech_engine.say(data)  # Convert text to speech
    text_to_speech_engine.runAndWait()

# Main block
if __name__ == '__main__':
    ans = None

    while True:
        data = speechToText()

        # Check if the wake word is detected
        if "vortex" in data or "vort" in data:

            # Handle different commands based on user input
            if "your name" in data:
                ans = "Hi There I am Vortex You can call me Vort"

            elif "yourself" in data:
                ans = """I am a Voice Assistant created by Mradul Lakhotiya.
                I can provide information, tell jokes, and open websites for you.
                Feel free to ask me anything!"""

            elif "how are you" in data or "your mood" in data:
                ans = "I'm just a computer program, but I'm always here to assist you!"

            # Get current time
            elif "time" in data:
                ans = datetime.datetime.now().strftime("%I:%M %p")  # Get current time in HH:MM AM/PM format
                
            # Get a random joke
            elif "jokes" in data or "joke" in data:
                ans = pyjokes.get_joke(language='en', category='neutral')  # Get a random joke

            # Open Spotify
            elif "spotify" in data or "music" in data or "song" in data:
                webbrowser.open('https://open.spotify.com/search')  # Open Spotify

            # Open YouTube
            elif "youtube" in data:
                webbrowser.open('https://www.youtube.com/')  # Open YouTube

            # Open Anime website
            elif "anime" in data:
                webbrowser.open('https://aniwatch.to/home')  # Open Anime website

            # Exit the loop
            elif "exit" in data or "stop" in data or "end" in data:
                break

            else:
                ans = "I don't have that feature yet"

            print(ans)
            textToSpeech(ans)

        # Exit the loop if the user says the exit command
        elif "exit" in data or "stop" in data or "end" in data:
            break

        else:
            print("Say \"Hey Vortex\" To activate the voice assistance")
            print("Say \"Exit\" To exit the loop")

