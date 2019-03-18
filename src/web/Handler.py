"""
HPP Web - Handler

Processes requests for the web server.
"""

from os import path
from pprint import pprint
from jinja2 import Template
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler

from ..services import prql
from ..data import DataComposer


class Handler(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        composer = DataComposer()
        self.tables = [dataset.title for dataset in composer.datasets]
        self.munis = prql.request('SELECT DISTINCT municipal FROM tabular.b25010_avg_hhsize_by_tenure_acs_m')['rows']

        super(Handler, self).__init__(*args, **kwargs)


    def do_GET(self):
        cwd = path.dirname(path.realpath(__file__))
        file_path = path.join(cwd, 'templates', 'index.tmpl')

        with open(file_path, 'r') as fp:
            template = Template(fp.read())

        page = template.render(munis=self.munis, tables=self.tables)
        self.send_page(page)


    def do_POST(self):
        body = self.parse_body()
        pprint(body)


    def parse_body(self):
        content_len = int(self.headers.get(name="content-length"))
        body_data = self.rfile.read(content_len)
        return parse_qs(body_data)


    def send_page(self, page):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        page_data = str.encode(page)
        self.wfile.write(page_data)
