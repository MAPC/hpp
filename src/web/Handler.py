"""
HPP Web - Handler

Processes requests for the web server.
"""

from pprint import pprint
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):


    def do_POST(self):
        body = self.parse_body()
        pprint(body)


    def parse_body(self):
        content_len = int(self.headers.getheader('content-length'))
        body_data = self.rfile.read(content_len)
        pprint(body_data)
        return parse_qs(body_data)

