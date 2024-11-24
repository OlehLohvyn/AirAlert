from gtts import gTTS
import os

# Set the text to be converted to speech
text = "Привіт! Це тест озвучування тексту українською мовою."

def say(text):
    # Create a gTTS object for Ukrainian text-to-speech
    tts = gTTS(text=text, lang='uk')

    # Save the audio output to a file
    tts.save("voice_ua.mp3")

    # Play the audio file (platform-dependent command)
    os.system("start voice_ua.mp3")  # For Windows
    # os.system("afplay voice_ua.mp3")  # For macOS
    # os.system("xdg-open voice_ua.mp3")  # For Linux
