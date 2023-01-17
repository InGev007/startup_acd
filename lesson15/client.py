import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55001))
while True:
    sock.send(bytes(input("Ваш текст:"), encoding='UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    print("Сообщение от сервера: " + data)
sock.close()
