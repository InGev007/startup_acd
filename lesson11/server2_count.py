import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode("utf-8")
    print(data)
    len_data = len(data.split())
    conn.send(bytes(f"Ты прислал {len_data} слова", encoding='UTF-8'))
conn.close()
