import speech_recognition as sr
from gtts import gTTS
import os
import platform
import pygame

def voice_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-IN")  # Use "hi-IN" for Hindi text.
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def text_to_voice(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")

def play_audio(file_path):
    if platform.system() == "Darwin":  # MacOS
        os.system("open " + file_path)
    elif platform.system() == "Linux":
        os.system("xdg-open " + file_path)
    elif platform.system() == "Windows":
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # Voice to Text
    user_input = voice_to_text()

    # Text to Voice
    if user_input:
        print("Converting the text to speech...")
        text_to_voice(user_input, language='en')
        play_audio("output.mp3")
