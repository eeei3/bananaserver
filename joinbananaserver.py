import socket


def joinBananaServer(username, defaultmessage, port, ipaddress):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (ipaddress, port)

    print("Connectiong to %s Port %s" % server_address)
    sock.connect(server_address)

    try:

        message = defaultmessage, " User %s connected!" % username

        print("Sending %s" % message)

        sock.sendall(str.encode(message))

        amount_received = 0
        amount_expected=len(message)

        sock.sendall(str.encode(defaultmessage))

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("Received %s" % data)

    finally:
        print("Closing socket")
        sock.close()
