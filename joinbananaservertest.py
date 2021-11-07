import socket
from tkinter import *
from concurrent import futures
from multiprocessing import Process
import time

class server_comms:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, sock):
        server_comms.sock = sock

    @staticmethod
    def connection(username, port, ipaddress):
        thread_pool_executor = futures.ThreadPoolExecutor(max_workers=5)
        try:
            thread_pool_executor.submit(gui.maingui)
            server_address = (ipaddress, port)
            print("Connecting to %s Port %s" % server_address)
            server_comms.sock.connect(server_address)

            message = " User %s connected!" % username

            print("Sending %s" % message)

            server_comms.sock.sendall(str.encode(message))

            gui.log.append(message)

            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = server_comms.sock.recv(80)
                print(data)
                print(len(data))
                amount_received += len(data)
                print("Received %s" % data)
                gui.log.append("Received %s" % data)
        finally:
            # thread_pool_executor.submit(gui)
            while 1:
                time.sleep(0.5)
                data = server_comms.sock.recv(1024)
                if not data:
                    break
                data = data.strip()
                print("Received %s from host" % data)
                gui.log.append("Received %s" % data)
                server_comms.sock.sendall(data.upper())

    @staticmethod
    def quitting():
        server_comms.sock.close()
        quit()

    @staticmethod
    def sendmessage(msg):
        server_comms.sock.sendall(str.encode(msg))
        gui.log.append(msg)

    def __call__(self, username, port, ipaddress):
        self.connection(username, port, ipaddress)


class gui:
    log = []
    def __init__(self, log):
        gui.log = log

    @staticmethod
    def maingui():

        def msgwrapper():
            msg2send = msg.get()
            server_comms.sendmessage(msg2send)

        print("This MOFO has started")

        thread_pool_executor = futures.ThreadPoolExecutor(max_workers=5)

        sroot = Tk()
        msg = StringVar(sroot)

        v = Scrollbar(sroot, orient='vertical')
        v.pack(side=RIGHT, fill=Y)

        t = Text(sroot, width=75, height=35, wrap=NONE,
                 yscrollcommand=v.set)

        t.place(relx=0.01, rely=0.81, anchor='sw')

        def addtext():
            prevlen = len(gui.log)
            for x in gui.log:
                t.insert(END, x)
            while True:
                messagelist = len(gui.log)
                if messagelist > prevlen:
                    print(messagelist)
                    print(prevlen)
                    print(gui.log)
                    t.insert(END, gui.log[-1])
                    t.insert(END, "\n")
                    prevlen = messagelist
                    time.sleep(0.1)
                else:
                    time.sleep(0.1)
                    pass

        thread_pool_executor.submit(addtext)
        print("Threads executed")
        v.config(command=t.yview)

        sendmessageentry = Entry(sroot, width=100, textvariable=msg)
        sendmessageentry.place(relx=0.01, rely=0.87, anchor='sw')

        sendmessagebutton = Button(sroot, text="Send", command=msgwrapper)
        sendmessagebutton.place(relx=0.8, rely=0.90, anchor='sw')

        closeconnection = Button(sroot, text="Quit", command=server_comms.quitting)
        closeconnection.place(relx=0.8, rely=1, anchor='sw')

        sroot.title("Banana Server server sided-client")
        sroot.minsize(800, 700)
        print("Done!")
        sroot.mainloop()
