import speech_recognition as sr
from speech import speak, listen_for_command
from commands import process_command

recognizer = sr.Recognizer()

if __name__ == "__main__":
    speak("Jarvis here....")

    while True:
        print("Jarvis listening, sir!")
        command = listen_for_command(recognizer)
        
        if command:
            if "jarvis" in command.lower():
                speak("Yes, sir?")
                process_command(command)
            else:
                print("Wake word not detected")
        else:
            print("Command not recognized")
