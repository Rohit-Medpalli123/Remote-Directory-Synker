import http.server
import socketserver

class HostServer:

    def __init__(self,port):
        self.PORT = port
        self.Handler = http.server.SimpleHTTPRequestHandler

    def turn_on_server(self):
        """This function  hosts the generated text file using httpserver"""

        with socketserver.TCPServer(("",self.PORT), self.Handler) as httpd:
            print("serving at port", self.PORT)
            httpd.serve_forever()
