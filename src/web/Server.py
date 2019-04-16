"""
HPP Web - Server

The class that manages the server lifecycle.
"""

import config
from http.server import HTTPServer

from .Handler import Handler


class LongHTTPServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        self.timeout = 60
        super(LongHTTPServer, self).__init__(*args, **kwargs)
         

class Server(object):

    def __init__(self):
        self.handler = Handler

    def serve(self):
        with LongHTTPServer(("", config.web.PORT), self.handler) as httpd:
            return httpd.serve_forever()
