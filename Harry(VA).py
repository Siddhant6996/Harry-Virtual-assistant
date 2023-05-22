import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the speech synthesis engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # Use Google Speech Recognition to convert audio to text
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""

# Function to handle user commands and provide appropriate responses
def process_command(command):
    command = command.lower()

    if "hello" in command:
        speak("Hello! How can I assist you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "wikipedia" in command:
        search_query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(search_query, sentences=2)
            speak("According to Wikipedia:")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please provide more specific search terms.")
        except wikipedia.exceptions.PageError as e:
            speak("No results found. Please check your search terms.")

    elif "open AI" in command:
        website = command.replace("https://chat.openai.com/", "").strip()
        speak(f"Opening {website}")
        webbrowser.open(website)

    elif "open folder" in command:
        folder_path = command.replace("open folder", "").strip()
        try:
            os.startfile(folder_path)
            speak("Folder opened.")
        except FileNotFoundError:
            speak("Folder not found.")

    elif "play music" in command:
        music_folder = "path/to/music/folder"  # Replace with your music folder path
        music_files = os.listdir(music_folder)
        if music_files:
            random.shuffle(music_files)
            random_music = os.path.join(music_folder, music_files[0])
            os.startfile(random_music)
            speak("Playing music.")
        else:
            speak("No music files found in the specified folder.")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I can't help with that.")

# Main loop of the virtual assistant
while True:
    user_input = listen()
    process_command(user_input)
