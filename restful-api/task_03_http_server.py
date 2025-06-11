#!/usr/bin/python3
"""
It contains the class:
MyHandler
"""
import http.server
import json
import socketserver


class MyHandler(http.server.BaseHTTPRequestHandler):
    """
    Create Handler class for http.server
    """
    def do_GET(self):
        """
        Create the do_GET method to handle GET requests.
        """
        if self.path == "/data":
            dataset = {"name": "John", "age": 30,
                       "city": "New York"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
