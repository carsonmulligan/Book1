from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - - [{self.log_date_time_string()}] {format%args}")

TCPServer(('', 8000), CORSRequestHandler).serve_forever() 