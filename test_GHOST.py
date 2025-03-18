
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
import webbrowser
import os

# Download necessary NLTK data files
nltk.download(['punkt'])

# Global variables
Password = "Gyro221"
welcome_Message = "Welcome back sir, Ghost protocol activated. How can I assist you today?"

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert speech to text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

def respond_to_command(command):
    with sr.Microphone() as source: 
        if "open website" in command.lower():
            browse_web(command)
    
# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
#Function to  recognize the time and greet the user

    
             
            

    # Main loop
def main():
    speak("Hello sir, WELCOME BACK! I'm GHOST AI, your latest developing AI assistant. How can I help you Sir?")
    while True:
        if command := recognize_speech():
            if respond_to_command(command) == False:
                break
    engine.stop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to activate the Ghost protocol
def Ghost_protocol(command):
    with sr.Microphone() as source:
        token = word_tokenize(command.lower())
        speak(welcome_Message)
        if "exit" in command.lower():
            speak("Returning to the user interface")
            return welcome_Message
        # Add more natural language processing capabilities
        elif any(word in token for word in ["hello", "hi", "hey"]):
            speak("Hello! How can I assist you today?")
        elif "how are you" in command.lower():
            speak("I'm functioning well, thank you for asking.")
        elif "what can you do" in command.lower():
            speak("I can help you browse websites, answer questions, and assist with various tasks.")
        else:
            speak("I didn't understand that command. Could you please rephrase it?")