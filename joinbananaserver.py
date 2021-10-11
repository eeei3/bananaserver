import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10001)

print("Connectiong to '%s' Port '%s'" % server_address)
sock.connect(server_address)

try:

    message = "Client to Banana Server, we have touchdown!"

    print("Sending '%s'" % message)

    sock.sendall(str.encode(message))

    amount_received = 0
    amount_expected=len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("Received '%s'" % data)

finally:
    print("Closing socket")
    sock.close()
