from multiprocessing import Process
import random
from createbananaserver import ScrollBar
from tkinter import *
from joinbananaservertest import *
from PIL import ImageTk, Image


def error(message):
    err = Toplevel()

    errorlabel = Label(err, text=message, font=("MS Comic Sans", "17"))
    errorlabel.pack()

    err.title("A error has occured")
    err.mainloop()


def titlepicker():

    randomNumber = random.randint(0,9)
    nameList = ["Banana Server", "Server for Banana's!", "Bnana Server", "lol", "Not a Anomaly!",
                "We (I mean you) are not affiliated with Banana Server", "2chtubo", "Banana Serer", "Linux Rocks!",
                "Be sure to like and subscribe!"]
    return nameList[randomNumber]


def createBananaServer():

    def bananapeel():
        bananaport = port.get()

        bananamessage = bmessage.get()

        ipaddr = internetprotocoladdress.get()

        try:
            ScrollBar.runGUI(bananaport, bananamessage, ipaddr)
        except Exception as e:
            error(e)

        return 0

    sub = Toplevel()

    port = IntVar(sub)

    internetprotocoladdress = StringVar(sub)

    port.set(10001)

    internetprotocoladdress.set("localhost")

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

    addressLabel = Label(sub, text="IP address?", font=("MS Comic Sans", "17"))
    addressLabel.pack()

    addressEntry = Entry(sub, textvariable=internetprotocoladdress)
    addressEntry.pack()

    startButton = Button(sub, text="Start my Banana Server!", command=bananapeel)
    startButton.pack()

    sub.title("Creating Banana Server")
    sub.maxsize(400, 400)
    sub.minsize(400, 400)
    sub.mainloop()

def main(title):

    def joincommand():
        username = uname.get()
        IPaddress = ipaddr.get()
        port = port2join.get()
        if IPaddress == "":
            IPaddress = "localhost"
        print(username, port, IPaddress)
        a = Process(target=server_comms.connection, args=(username, port, IPaddress))
        a.run()

    root = Tk()

    joinframe = Frame(root)
    joinframe.pack(side=BOTTOM)

    uname = StringVar(root)
    ipaddr = StringVar(root)
    port2join = IntVar(root)
    defaultmsg = StringVar(root)

    defaultmsg.set("Client to Banana Server, we have touchdown!")

    guestnumber = random.randint(0, 999)

    guestname = "Guest %s" % guestnumber

    uname.set(guestname)

    maintitleimg = ImageTk.PhotoImage(Image.open("bananaserverpic.png"))

    titleLabel = Label(root, text="Welcome to Fabulous Banana Server!", font=("MS Comic Sans", "17"))
    titleLabel.pack()

    panel= Label(root,image=maintitleimg)
    panel.pack()

    createbutton = Button(root, text="Create a Banana Server", command=createBananaServer)
    createbutton.place(relx=0.35, rely=0.3, anchor='sw')

    usernamefield = Entry(root, textvariable=uname)
    usernamefield.place(relx=0.35, rely=0.5, anchor='sw')

    usernamelabel = Label(root, text="Enter your username", font=("MS Comic Sans", "12"))
    usernamelabel.place(relx=0.33, rely=0.48, anchor='sw')

    ipfield = Entry(root, textvariable=ipaddr)
    ipfield.place(relx=0.35, rely=0.66, anchor='sw')

    iplabel = Label(root, text="IP of Banana Server", font=("MS Comic Sans", "12"))
    iplabel.place(relx=0.33, rely=0.6, anchor='sw')

    portlabel = Label(root, text="Banana Server port", font=("MS Comic Sans", "12"))
    portlabel.place(relx=0.33, rely=0.76, anchor='sw')

    portentry = Entry(root, textvariable=port2join)
    portentry.place(relx=0.33, rely=0.80, anchor='sw')

    message = Entry(root, textvariable=defaultmsg)
    message.place(relx=0.33, rely=0.92, anchor='sw')

    messagelabel = Label(root, text="Message to send after successful connection", font=("MS Comic Sans", "12"))
    messagelabel.place(relx=0.10, rely=0.85)

    joinbutton = Button(joinframe, command = joincommand, text="Join Banana Server!")
    joinbutton.pack()

    root.title(title)
    root.maxsize(400, 700)
    root.minsize(400, 700)
    root.mainloop()


title = titlepicker()
main(title)
