"""
HPP Web - Server

The class that manages the server lifecycle.
"""

import config
from socketserver import TCPServer

from .Handler import Handler


class Server(object):

    def __init__(self):
        self.handler = Handler

    def serve(self):
        with TCPServer(("", config.web.PORT), self.handler) as httpd:
            return httpd.serve_forever()
