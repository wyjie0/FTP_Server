import os
import sys
import socketserver
from core.server import MyFTPServer
from conf import settings
sys.path.append(os.path.dirname(os.getcwd()))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(settings.addr, MyFTPServer)
    server.serve_forever()