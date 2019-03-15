"""
HPP Web - Handler

Processes requests for the web server.
"""

from pprint import pprint
from jinja2 import Template
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        with open('src/web/static/index.tmpl', 'r') as fp:
            template = fp.read()

        self.send_response(200, page)


    def do_POST(self):
        body = self.parse_body()
        pprint(body)


    def parse_body(self):
        content_len = int(self.headers.get(name="content-length"))
        body_data = self.rfile.read(content_len)
        return parse_qs(body_data)

