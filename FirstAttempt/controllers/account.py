import tornado.ioloop
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    """
    账户相关信息
    """
    def get(self, *args, **kwargs):
        self.render('login.html',msg="")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == "root" and password == '123':
            self.set_secure_cookie('xxxxxx','oooooo')
            # self.set_secure_cookie('xxxxxx','oooooo')
            self.redirect('/home')
        else:
            self.render('login.html',msg="用户名或密码错误")