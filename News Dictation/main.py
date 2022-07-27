import multiprocessing as mp
import time
from try2 import function
import datetime


def welcome_speak():
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")

    num_hour = datetime.datetime.now().hour
    if num_hour in range(5, 12):
        speak.Speak("Good Morning Sir!")
    elif num_hour in range(12, 18):
        speak.Speak("Good Afternoon Sir!")
    elif num_hour in range(18, 23):
        speak.Speak("Good Evening Sir!")

    speak.Speak("Welcome to our live news software")


if __name__ == '__main__':
    p1 = mp.Process(target=welcome_speak)
    p2 = mp.Process(target=function)
    p2.start()
    time.sleep(0.8)
    p1.start()
