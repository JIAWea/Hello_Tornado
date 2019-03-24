import tornado.ioloop
import tornado.web
from controllers.account import LoginHandler
from controllers.home import HomeHandler

class Foo(tornado.web.RequestHandler):
    def initialize(self):               # RequestHandler中init的示例，
        self.A = 123
        self.set_cookie('xxxx','oooo')
        super(Foo, self).initialize()   # 执行父类的initialize方法


class MainHandler(Foo):
    def get(self):
        print(self.A)                   #　没有A则往上找
        self.write("Hello, world")
        # self.render("main.html")
        # self.redirect('http://www.baidu.com')

settings = {
    "template_path": 'views',           # 模板
    "cookie_secret":'abcdefgijk',       # cookie加密

}

application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()