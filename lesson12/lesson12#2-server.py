import socket
import asyncio
import time


async def client_handle(client):
    loop = asyncio.get_event_loop()
    s_time = time.time()
    request = None
    while (request != 'quit') and ((time.time()-s_time) < 180): # Разрыв соединения через 3минуты без сообщений или по команде quit
        request = (await loop.sock_recv(client, 1024)).decode('utf8')
        if request.count("+") == 1:
            temp = request.split("+")
            answer = str(float(temp[0]) + float(temp[1]))
        elif request.count("-") == 1:
            temp = request.split("-")
            answer = str(float(temp[0]) - float(temp[1]))
        elif request.count("*") == 1:
            temp = request.split("*")
            answer = str(float(temp[0]) * float(temp[1]))
        elif request.count("/") == 1:
            temp = request.split("/")
            answer = str(float(temp[0]) / float(temp[1]))
        elif request == "quit":
            answer = "Goodbay!"
        else:
            answer = "I don`t understand you"
        await loop.sock_sendall(client, answer.encode('utf8'))
        s_time = time.time()
    client.close()


async def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 55001))
    sock.listen(10)
    sock.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(sock)
        loop.create_task(client_handle(client))

if __name__ == '__main__':
    asyncio.run(server())