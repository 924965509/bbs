import socket
import threading
import time
def talk():
    sk = socket.socket()

    sk.connect(("127.0.0.1",8081))

    # time.sleep(5)
    print(sk.recv(1024))

    sk.send(b'im18cm')
    print(sk.recv(1024))

    sk.close()

for i in range(5000):
    threading.Thread(target=talk).start()
