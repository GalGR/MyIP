#!/usr/bin/python3

import socketserver

HOST = "" # Bind to all interfaces
PORT = 1995

class MyIP_RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("{}".format(self.client_address[0]))
        self.wfile.write(bytes("{}".format(self.client_address[0]), "utf-8"))

def main():
    print("Running server at port: %s" % PORT)
    try:
        server = socketserver.TCPServer((HOST, PORT), MyIP_RequestHandler)
        server.serve_forever()
    except:
        pass

if __name__ == "__main__":
    main()