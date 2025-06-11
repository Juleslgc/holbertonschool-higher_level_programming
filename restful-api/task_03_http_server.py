#!/usr/bin/python3
"""
It contains the class:
MyHandler
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
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
            status = {"status": "OK"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(status).encode('utf-8'))
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
            message = {"error": "404 Not Found",
                       "message": "Endpoint not found"}
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(message).encode('utf-8'))


if __name__ == "__main__":
    server = HTTPServer(("", 8000), MyHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
