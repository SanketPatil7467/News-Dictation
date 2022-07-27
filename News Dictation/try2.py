from tkinter import *

index = 0
index1 = 0


def function():

    import requests
    import json

    # l = ['Sanket', 'Patil', 'Shubham', 'Ravi', 'Rohan']
    root = Tk()
    root.geometry("734x456")
    root.minsize(734, 456)

    l = []
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]

    for article in arts:
        l.append(article["title"])

    def speak3(str):
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(str)

    def speak():
        global index1
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(l[index1])
        index1 += 1

    def func():
        global index
        lab.configure(text=l[index], fg="grey38", font=(
            "COPPERPLATE GOTHIC BOLD", 16, "bold"))
        # speak(l[index])
        index += 1

    def func2():
        global index
        index -= 1
        lab.configure(text=l[index], fg="grey38", font=(
            "COPPERPLATE GOTHIC BOLD", 16, "bold"))
        # speak(l[index])

    def all_news():
        for article in arts:
            speak3(article["title"])
            # print(article["title"])
            speak3("Moving to next news: ")

    f1 = Frame(root, bg="burlywood1", height=1000, width=1500)
    f1.pack(side=LEFT, fill=BOTH)
    lab = Label(f1, text="Welcome HERE!\n News telling software", bg="burlywood1",
                fg="midnight blue", font=("COPPERPLATE GOTHIC BOLD", 55, "bold"), padx=1000, pady=100)
    lab.pack(anchor="center")

    bt = Button(f1, text="Previous News", command=func2, padx=15, pady=8,
                font=("COPPERPLATE GOTHIC BOLD", 15, "bold"), bg="orange2", fg="grey19", relief=SUNKEN)
    bt.pack(pady=5)

    b = Button(f1, text="Next News", command=func, padx=15, pady=8,
               font=("COPPERPLATE GOTHIC BOLD", 15, "bold"), bg="orange2", fg="grey19", relief=SUNKEN)
    b.pack(pady=5)

    b2 = Button(f1, text="Listen News", command=speak, padx=7, pady=8,
                font=("COPPERPLATE GOTHIC BOLD", 15, "bold"), bg="orange2", fg="grey19", relief=SUNKEN)
    b2.pack(pady=10)

    b3 = Button(f1, text="Listen Today's Top News", command=all_news, padx=7, pady=8,
                font=("COPPERPLATE GOTHIC BOLD", 15, "bold"), bg="orange2", fg="grey19", relief=SUNKEN)
    b3.pack(pady=10)

    root.mainloop()
