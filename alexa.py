import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import jokes

import datetime
import sys
import time

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Optional: choose a voice (0 = male, 1 = female on many systems)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

def talk(text: str) -> None:
    """Speak the given text out loud."""
    engine.say(text)
    engine.runAndWait()

def take_command(timeout: int = 7, phrase_time_limit: int = 10) -> str:
    """Listen from microphone and return a lowercased command string.
    Returns an empty string if nothing recognized or on error."""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1.5)
            print("Listening...")
            audio = listener.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            command = listener.recognize_google(audio)
            command = command.lower()
            return command
    except sr.WaitTimeoutError:
        # no speech detected within timeout
        return ""
    except sr.UnknownValueError:
        # speech unintelligible
        return ""
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        print(f"Speech recognition error: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error while listening: {e}")
        return ""

def run_alexa():
    command = take_command()
    print(f"[DEBUG] Raw command: '{command}'")
    if not command:
        print("[DEBUG] No command recognized, waiting...")
        time.sleep(0)
        return  # nothing to do

    print("Command:", command)

    # Wake word handling (optional). Remove if you don't want a wake word.
    if 'alexa' in command:
        # remove the wake word
        command = command.replace('alexa', '').strip()

    # Play music on YouTube
    if command.startswith('play '):
        song = command.replace('play ', '').strip()
        if song:
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        else:
            talk('Please say the song name.')
        return

    # Tell the current time
    if 'time' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is', now)
        talk('Current time is ' + now)
        return
    
    # Who is ... (Wikipedia)
    if command.startswith('who is') or command.startswith('who the heck is') or command.startswith('who\'s'):
        # remove the question part
        person = command.replace('who is', '').replace('who the heck is', '').replace("who's", '').strip()
        if person:
            try:
                info = wikipedia.summary(person, sentences=1)
                print(info)
                talk(info)
            except Exception as e:
                print(f"Wikipedia error: {e}")
                talk("Sorry, I couldn't find information on that.")
        else:
            talk("Who would you like to know about?")
        return

    # Jokes
    if 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return

    # Date (funny reply)
    if 'date' in command:
        print("Sorry, I have a headache.")
        talk('Sorry, I have a headache.')
        return

    # Relationship question
    if 'are you single' in command or 'are you in a relationship' in command:
        print("I am in a relationship with Wi-Fi.")
        talk('I am in a relationship with Wi-Fi.')
        return

    # Fallback
    talk('Please say the command again.')
    # Test manually
#command = input("Type command to test: ").lower()
# Then pass it to your command handling logic


if __name__ == "__main__":
    print("Voice assistant started. Press Ctrl+C to stop.")
    try:
        while True:
            run_alexa()
            # short pause to avoid tight loop if mic returns empty quickly
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
