import socket
from tkinter import *
from concurrent import futures

log = []

newMessage = False


class ScrollBar:


    @staticmethod
    def runGUI(port, message, **ipaddr):
        thread_pool_executor = futures.ThreadPoolExecutor(max_workers=5)
        root = Tk()

        def add_text(message):
            t.insert(END, message)

        def creatingbananaserver():
            s = ScrollBar()

            def gui():
                s.runGUI()

            global log
            try:
                thread_pool_executor.submit(gui)
            except Exception as e:
                print(e)

            if ipaddr["ip"] == {}:
                raise "IPAddressNotHandled"
            elif ipaddr["ip"] == "localhost":
                pass
            else:
                if len(ipaddr["ip"].split(".")) > 4 or len(ipaddr["ip"].split(".")):
                    raise "InvalidIPAddress!"
                else:
                    pass

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            banana_address = ('localhost', int(port))

            print("Server IP {} | Port {}".format(banana_address[0], banana_address[1]))

            add_text("Server IP {} | Port {}".format(banana_address[0], banana_address[1]) + "\n")

            sock.bind(banana_address)

            sock.listen(1)

            while True:
                print("Waiting for any Connection")
                add_text("Waiting for any Connection")

                try:
                    connection, client_address = sock.accept()
                    print("Connection from", client_address)
                    print("Appending")
                    add_text("Connection from" + str(client_address) + "\n")
                    print(len(log))
                    while True:
                        data = connection.recv(16)
                        print("Received '%s'" % data)
                        add_text("Received '%s'" % data + "\n")
                        print(len(log))
                        if data:
                            print("Sending data back to the client")
                            add_text("Sending data back to the client")
                            connection.sendall(str.encode(message))
                            print("Message Sent: '%s" % message)
                            add_text("Message Sent: '%s" % message + "\n")
                            print(len(log))
                        else:
                            print("No more data from", client_address)
                            add_text("No more data from " + client_address + "\n")
                            print(len(log))
                            print("Conversation has ceased")
                            break
                finally:
                    connection.close()

        v = Scrollbar(root, orient='vertical')
        v.pack(side=RIGHT, fill=Y)

        t = Text(root, width=15, height=100, wrap=NONE,
                 yscrollcommand=v.set)

        t.pack(side=TOP, fill=X)

        v.config(command=t.yview)

        root.after(5)

        thread_pool_executor.submit(creatingbananaserver)

        root.title("Banana Server server sided-client")
        root.minsize(400, 700)
        root.mainloop()
