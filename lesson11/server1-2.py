import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55001))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)
while True:
    data = conn.recv(1024).decode("utf-8")
    print(data)
    if data == "Hello":
        answer = "Hi!"
    elif data == "How are you?":
        answer = "Good, are you?"
    else:
        answer = "I don`t understand you"
    conn.send(bytes(answer, encoding='UTF-8'))
conn.close()
