"""
HPP Web - Handler

Processes requests for the web server.
"""

from jinja2 import Template
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler

from ..services import prql
from ..data import DataComposer
from ..util import convert_binary, load_file
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
        template_contents = convert_binary(load_file('templates', 'index.tmpl'))
        template = Template(template_contents)

        page = template.render(
            munis = self.munis, 
            tables = self.tables, 
            formats = list(self.formatWriters.keys())
        )

        self.send('text/html', page)


    def do_POST(self):
        body = self.parse_body()

        if not 'munis' in body or not 'tables' in body:
            self.reload()
            return

        self.composer.compose(body['munis'], body['tables'])

        writer = self.formatWriters[body['format']](self.composer, body['include_metadata'])
        writer.write()

        file_data = load_file('compositions', writer.get_file())
        self.send('application/octet-stream', file_data, writer.get_file())


    def parse_body(self):
        content_len = int(self.headers.get(name="content-length"))
        body_data = self.rfile.read(content_len)
        parsed_body = parse_qs(body_data)

        body = convert_binary(parsed_body)

        if 'format' in body and isinstance(body['format'], list):
            body['format'] = body['format'][0]

        body['include_metadata'] = bool('include_metadata' in body)

        return body


    def send(self, content_type, data, attachment = None):
        if isinstance(data, str):
            data = str.encode(data)

        self.send_response(200)
        self.send_header('Content-Type', content_type)
        if attachment != None:
            self.send_header('Content-Disposition', 'attachment; filename="%s"' % attachment)
        self.send_header('Content-Length', len(data))
        self.end_headers()

        self.wfile.write(data)


    def reload(self):
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()
