import tornado.ioloop
import tornado.web
import tornado.httpserver
from urls import urls
from utils.db import ConnectDB

import os
import sys
import uuid
import base64
import logging

class Application(tornado.web.Application):
    def __init__(self):
        
        settings = {
            "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
            "static_path" : os.path.join(os.path.dirname(__file__), "static"),
            "cookie_secret" : base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            "debug" : True,
        }
        
        tornado.web.Application.__init__(self, handlers=urls, **settings)
        self.session = ConnectDB()

def main():
    PORT = '8888'
    if len(sys.argv) > 1:
        #PORT = sys.argv[1]
        PORT = sys.argv[1].split('=')[1]
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(PORT)
    logging.debug('server starts on port ', PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
