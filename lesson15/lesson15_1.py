import socket
import logging

logging.basicConfig(filename='server_15.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55001))
sock.listen(10)
logging.info('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
logging.debug('connected:' + str(addr))
while True:
    try:
        data = conn.recv(1024).decode("utf-8")
        logging.info("User message:" + str(data))
        if data == "Hello":
            answer = "Hi!"
            logging.info("Sending answer message to the user")
        elif data == "How are you?":
            answer = "Good, are you?"
            logging.info("Sending answer message to the user")
        else:
            answer = "I don`t understand you"
            logging.warning("Sending error message to the user")
        conn.send(bytes(answer, encoding='UTF-8'))
    except Exception as ex:
        logging.error(ex)
        conn.close()
conn.close()
