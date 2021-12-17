import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

listener =sr.Recognizer()
engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('leena', '')
                print(command)
    except:
        pass
    return command

def run_leena():
    command =take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.time.now().strftime('%I:%M:%p')
        talk('current time is'+time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

class widget:
    def __init__(self):
        root =tk.Tk()

        root.title('leena')
        root.geometry('520x320')

        img = ImageTk.PhotoImage (Image.open('h12.png')) 

        panel = Label(root,image=img)
        panel.pack(side='right', fill='both',expand='no')

        compText = StringVar()
        userText = StringVar()

        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Leena', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')


        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', ).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')

        root.mainloop()

while True:
    run_leena()