"""
HPP Web - Handler

Processes requests for the web server.
"""

import collections
from os import path
from pprint import pprint
from jinja2 import Template
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler

from ..services import prql
from ..data import DataComposer
from ..writers import ExcelWriter, CSVWriter


class Handler(SimpleHTTPRequestHandler):

    formatWriters = {
        'xlsx': ExcelWriter,
        'csv': CSVWriter,
    }

    def __init__(self, *args, **kwargs):
        self.composer = DataComposer()
        self.tables = [dataset.title for dataset in self.composer.datasets]

        muni_response = prql.request('SELECT DISTINCT municipal FROM tabular.b25010_avg_hhsize_by_tenure_acs_m')
        munis = [row['municipal'] for row in muni_response['rows']]
        munis.sort()
        self.munis = munis

        super(Handler, self).__init__(*args, **kwargs)


    def do_GET(self):
        template = Template(load_file('templates', 'index.tmpl'))

        page = template.render(
            munis = self.munis, 
            tables = self.tables, 
            formats = list(self.formatWriters.keys())
        )

        self.send('text/html', page)


    def do_POST(self):
        body = self.parse_body()
        pprint(body)
        self.composer.compose(body['munis'], body['tables'])

        writer = self.formatWriters[body['format']]
        writer.write()

        file_data = load_file('compositions', writer.file_name)
        self.send('application/octet-stream', file_data)


    def parse_body(self):
        content_len = int(self.headers.get(name="content-length"))
        body_data = self.rfile.read(content_len)
        parsed_body = parse_qs(body_data)

        return convert_binary(parsed_body)


    def send(self, content_type, data):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()

        encoded_data = str.encode(data)
        self.wfile.write(encoded_data)



def convert_binary(data):
    if isinstance(data, dict):
        items = list(data.items())
        pprint(items)

        for key, value in items:
            data[key.decode()] = convert_binary(value)
            del data[key]

        return data
    elif isinstance(data, list):
        print(data)
        return list(map(convert_binary, data))
    else:
        return data.decode()


def load_file(self, directory, file_name):
    cwd = path.dirname(path.realpath(__file__))
    file_path = path.join(cwd, directory, file_name)

    with open(file_path, 'r') as fp:
        file_contents = fp.read()

    return file_contents
