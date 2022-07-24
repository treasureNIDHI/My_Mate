import speech_recognition as suno
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = suno.Recognizer()
engine=pyttsx3.init()
engine.say("hey my nidhee")
engine.say("O my treasure")
engine.say("I am your assis")
engine.say("how can i help you")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with suno.Microphone()as bolo:
            print("listening...........")
            voice = listener.listen(bolo)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assis' in command:
                command = command.replace('assis','')
                print(command)
           
    except:
        pass
    return (command)

def run_assis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is'+time)
    elif 'tell me about' in command:
        topic = command.replace('tell me about','')
        info = wikipedia.summary(topic, 3)
        print(info)
        talk('here is some related results')
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thanks' in command:
        talk('you are welcome')
    elif 'thank you' in command:
        talk('no prob')
    elif 'thank you so much' in command:
        talk('my pleasure')
    elif 'dance' in command:
        talk("my bad , i can't dance")
    elif 'please' in command:
        talk('oh i am so sorry')
    elif 'bye' in command:
        talk('bye dear , take care')
    elif 'good night' in command:
        talk('good night , sweet dreams')
    elif 'good morning' in command:
        talk('very good morning')
    elif ' hello my rog' in command:
        talk('hii dear')
    elif 'how are you' in command:
        talk('i am good , how are you')
    else:
        topic = command
        info = wikipedia.summary(topic, 2)
        print(info)
        talk (info)
        talk('sorry..........please tell me again')
while True:
    run_assis()
        
    