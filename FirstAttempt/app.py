import tornado.ioloop
import tornado.web
from controllers.account import LoginHandler
from controllers.home import HomeHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("main.html")
        # self.redirect('http://www.baidu.com')

import uimethods as ut
import uimodules as mm

settings = {
    "template_path": 'views',           # 模板
    "cookie_secret":'abcdefgijk',       # cookie加密
    "ui_methods":ut,                    # 模板标签不渲染
    "ui_modules":mm,                    # 模板标签自动渲染
    "static_path":'static',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/home", HomeHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()