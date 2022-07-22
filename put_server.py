#!/usr/bin/env python3

import argparse
import http.server
import os
import json
import getpass

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    endpoint_message = ""
    answers = {}

    def do_GET(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows PUT requests")

    def do_POST(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows PUT requests")
        self.wfile.write("The server listening on this port only allows PUT requests\n".encode())

    def do_PUT(self):
        path = self.translate_path(self.path)
        if path.endswith('/'):
            self.send_error(404, "Not Found", "Please include the full path in the URL, without a trailing /")
            return

        if not self.headers['Content-Length']:
            self.send_error(400, "Bad Request", "Please specify a request body")
            return

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data

        if content_length > 0:
            post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
            resource = path.rpartition('/')[-1]
            try:
                body = json.loads(post_data)
            except ValueError:
                error_message = "Unable to deserialize body, is it JSON? Got: {}\n".format(post_data)
                self.send_error(400, "Bad Request", error_message)
                return
            if "answer" not in body:
                self.send_error(400, "Bad Request", "Expected a string [answer] in the request body")
                return

            self.answers[resource] = body["answer"]
            print("\033[2J") # Clear screen
            print(endpoint_message)
            for pair in self.answers.items():
                print(pair)
            self.send_response(201, "Created")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(("Successful PUT: username=" + resource + ",answer=" + body["answer"] + "\n").encode())
        else:
            self.send_error(400, "Bad Request", "Received request with empty body")
        return

    def log_request(self, code='-', size='-'):
        # don't log requests
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8002, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8002]')
    parser.add_argument('--hostname', default=getpass.getuser() + '.aka.corp.amazon.com',
                        help='Specify host name for participants to curl against (e.g. <alias>.aka.corp.amazon.com')
    args = parser.parse_args()

    endpoint_message = "Serving PUT endpoint at http://" + args.hostname + ":8002"
    print(endpoint_message)
    http.server.test(HandlerClass=HTTPRequestHandler, port=args.port, bind=args.bind)
