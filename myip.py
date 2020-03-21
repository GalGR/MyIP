#!/usr/bin/python3

import socket
import sys
import os

# Default host to connect to
HOST = "localhost"

# Port used on both sides DON'T CHANGE
PORT = 1995

FILENAME = "ip.cfg"

def main():
    global HOST

    # Configure to which host to connect to (the default is localhost)
    if len(sys.argv) > 1:
        HOST = sys.argv[1]
    else:
        # Try to read the ip from ip.cfg if it exists
        path = os.path.dirname(os.path.abspath(__file__))
        cfg_path = os.path.join(path, FILENAME)
        if os.path.isfile(cfg_path):
            cfg_file = None
            try:
                cfg_file = open(cfg_path, mode="r", encoding="utf-8")
                HOST = cfg_file.read().strip(" \t\r\n")
            except:
                if cfg_file != None:
                    cfg_file.close()
                print("Couldn't read file")
                print(sys.exc_info())
                return

    # Connect to the host and get the external IP
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(bytes("", "utf-8"))
        received = str(sock.recv(1024), "utf-8")

        print(str(received))
    except:
        if sock != None:
            sock.close()
        print("Couldn't connect to %s" % HOST)
        print(sys.exc_info())
        return

if __name__ == "__main__":
    main()