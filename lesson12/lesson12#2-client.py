import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55001))
print("При использования сервера с заданием с урока отправь ему уравнение.")
print("При использования сервера с заданием от учителя отправь ему текст.")
print("Для выхода отправь quit.")
promt = None
while True and promt != "quit":
    promt = input("Ваш текст:")
    sock.send(bytes(promt, encoding='UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    print("Сообщение от сервера: " + data)
sock.close()