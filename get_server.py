#!/usr/bin/env python3

import argparse
import http.server
import os
import json
import random
import getpass

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    questions = [
    	"What's the strangest word you've ever read/heard?",
    	"What's your favorite color?",
    	"Who's your favorite actor?",
    	"What's a recent book you've read?",
    	"What's a recent movie you've watched?",
    	"What's your favorite city you've been to?",
    	"What's your manager's alias?",
    	"What's your favorite programming language?",
    	"How many years have you worked at Amazon?",
    	"What's a hobby of yours?"
    ]

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        question = random.choice(self.questions)
        self.wfile.write((json.dumps({'question': question}) + "\n").encode())

    def do_POST(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows GET requests")

    def do_PUT(self):
        self.send_error(405, "Method Not Allowed", "The server listening on this port only allows GET requests")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    parser.add_argument('--hostname', default=getpass.getuser() + '.aka.corp.amazon.com',
                        help='Specify host name for participants to curl against (e.g. <alias>.aka.corp.amazon.com')
    args = parser.parse_args()

    print("Serving GET endpoint at http://" + args.hostname + ":8000")
    http.server.test(HandlerClass=HTTPRequestHandler, port=args.port, bind=args.bind)
