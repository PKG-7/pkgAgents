import http.server
import socketserver
import webbrowser
import os

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Веб-интерфейс доступен по адресу: http://localhost:{PORT}")
        webbrowser.open(f'http://localhost:{PORT}')
        httpd.serve_forever()

if __name__ == "__main__":
    run_server() 