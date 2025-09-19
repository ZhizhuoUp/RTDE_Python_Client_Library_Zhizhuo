import socket

HOST = '192.168.1.2'
PORT = 30001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(((HOST, PORT)))

cmd = "movej([0, 0.4, 0, 0.4, 0, 0], a=1.0, v=0.2)\n"
print('send command!')
s.sendall(cmd.encode("utf-8"))
s.close()