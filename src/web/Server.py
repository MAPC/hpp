"""
HPP Web - Server

The class that manages the server lifecycle.
"""

import config
from http.server import HTTPServer

from .Handler import Handler


class Server(object):

    def __init__(self, handler = Handler):
        self.handler = handler

    def serve(self):
        with HTTPServer(("", config.web.PORT), self.handler) as httpd:
            return httpd.serve_forever()
