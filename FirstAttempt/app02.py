import tornado.ioloop
import tornado.web
from controllers.account import LoginHandler
from controllers.home import HomeHandler

container = {}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")



application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/home", HomeHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()