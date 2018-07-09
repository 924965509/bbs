import socket
import time

sk = socket.socket()
sk.bind(("127.0.0.1", 8081))
sk.setblocking(False)
sk.listen()
conn_l = []
del_conn=[]
while True:
    try:
        conn, addr = sk.accept()
        conn.send(b"hello")
        conn_l.append(conn)
    except BlockingIOError:
        for con in conn_l:
            try:
                msg = con.recv(1024)
                if msg == b"":
                    del_conn.append(con)
                    continue
                print(msg)
                con.send(b'180bey')

            except BlockingIOError:pass
        for con in del_conn:
            con.close()
            conn_l.remove(con)
            del_conn.clear()

sk.close()
