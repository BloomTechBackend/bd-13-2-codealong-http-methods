#!/usr/bin/env python3

import argparse
import http.server
import os
import json
from urllib import parse
import getpass

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    endpoint_message = ""
    answers = []

    def do_GET(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows POST requests")

    def do_POST(self):
        if (self.headers['Content-Length']): # Check if request body was provided
            content_length = int(self.headers['Content-Length']) # Gets the size of data so we know how much to read
            if content_length > 0:
                post_data = self.rfile.read(content_length).decode('utf-8') # Gets the data itself
                try:
                    body = json.loads(post_data)
                except ValueError:
                    error_message = "Unable to deserialize body, is it JSON? Got: {}".format(post_data)
                    self.send_error(400, "Bad Request", error_message)
                    return
                if {'username', 'answer'} != set(body):
                    error_message = "Expected a username and answer in the request body"
                    self.send_error(400, "Bad Request", error_message)
                    return

                self.answers.append(body) # add the json object to the list of stored answers

                print("\033[2J") # Clear screen
                print(endpoint_message)
                for pair in self.answers:
                    print(pair)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(("Successful POST: " + str(body) + "\n").encode())
            else:
                self.send_error(400, "Bad Request", "Expected a non-empty request body")
                return
        else:
            self.send_error(400, "Bad Request", "Expected a username and answer in the request body")

        return

    def do_PUT(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows POST requests")

    def log_request(self, code='-', size='-'):
        # don't log requests
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8001, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8001]')
    parser.add_argument('--hostname', default=getpass.getuser() + '.aka.corp.amazon.com',
                        help='Specify host name for participants to curl against (e.g. <alias>.aka.corp.amazon.com')
    args = parser.parse_args()

    endpoint_message = "Serving POST endpoint at http://" + args.hostname + ":8001"
    print(endpoint_message)
    http.server.test(HandlerClass=HTTPRequestHandler, port=args.port, bind=args.bind)
