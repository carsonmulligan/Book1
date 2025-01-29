from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

TCPServer(('', 8000), CORSRequestHandler).serve_forever() 