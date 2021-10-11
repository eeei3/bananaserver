import socket


def creatingbananaserver(port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    banana_address = ('localhost', int(port))

    print("Server IP {} | Port {}".format(banana_address[0], banana_address[1]))

    sock.bind(banana_address)

    sock.listen(1)

    while True:
        print("Waiting for Connection")

        try:
            connection, client_address = sock.accept()
            print("Connection from", client_address)
            while True:
                data = connection.recv(16)
                print("Received '%s'" % data)
                if data:
                    print("Sending data back to the client")
                    connection.sendall(str.encode(message))
                    print("Message Sent: '%s" % message)
                else:
                    print("No more data from", client_address)
                    break
        finally:
            connection.close()
