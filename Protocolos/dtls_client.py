import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = sock.sendto(b"hello from Client", ("localhost", 9998))
print(f"Client got: {data}")
sock.close()









