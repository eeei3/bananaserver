from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import random
from createbananaserver import creatingbananaserver


def titlepicker():
    randomNumber = random.randint(0,9)
    nameList = ["Banana Server", "Server for Banana's!", "Bnana Server", "lol", "Not a Anomaly!",
                "We (I mean you) are not affiliated with Banana Server", "Unlucky...", "Banana Serer", "Linux Rocks!",
                "Be sure to like and subscribe!"]
    return nameList[randomNumber]

def createBananaServer():


    def bananapeel():
        bananaport = port.get()

        bananamessage = bmessage.get()

        creatingbananaserver(bananaport, bananamessage)

        return 0


    sub = Toplevel()

    port = IntVar(sub)

    port.set(10001)

    bmessage = StringVar(sub)
    bmessage.set("Welcome to my Banana Server!")

    portLabel = Label(sub, text="Please enter your desired port", font=("MS Comic Sans", "17"))
    portLabel.pack()

    portEntry = Entry(sub, textvariable=port)
    portEntry.pack()

    message = Label(sub, text="Please enter default message", font=("MS Comic Sans", "17"))
    message.pack()

    messageEntry = Entry(sub, textvariable=bmessage)
    messageEntry.pack()

    startButton = Button(sub, text="Start my Banana Server!", command=bananapeel)
    startButton.pack()



    sub.title("Creating Banana Server")
    sub.maxsize(400, 400)
    sub.minsize(400, 400)
    sub.mainloop()

def main(title):

    root = Tk()

    maintitleimg = ImageTk.PhotoImage(Image.open("bananaserverpic.png"))

    titleLabel = Label(root, text="Welcome to Fabulous Banana Server!", font=("MS Comic Sans", "17"))
    titleLabel.pack()

    panel= Label(root,image=maintitleimg)
    panel.pack()

    createbutton = Button(root, text="Create a Banana Server", command=createBananaServer)
    createbutton.place(relx=0.35, rely=0.3, anchor='sw')

    usernamefield = Entry(root)
    usernamefield.place(relx=0.35, rely=0.6, anchor='sw')

    usernamelabel = Label(root, text="Enter your username", font=("MS Comic Sans", "12"))
    usernamelabel.place(relx=0.33, rely=0.58, anchor='sw')

    ipfield = Entry(root)
    ipfield.place(relx=0.35, rely=0.8, anchor='sw')

    iplabel = Label(root, text="IP of Banana Server", font=("MS Comic Sans", "12"))
    iplabel.place(relx=0.33, rely=0.7)


    root.title(title)
    root.maxsize(400, 700)
    root.minsize(400, 700)
    root.mainloop()

title = titlepicker()
main(title)