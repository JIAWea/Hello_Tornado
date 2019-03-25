import tornado.ioloop
import tornado.web
import time,hashlib
from controllers.account import LoginHandler
from controllers.home import HomeHandler

container = {}
# container = { '随机字符串或者cookie':{'uuuu':'root','k1':'v1'}, }

class Cache(object):
    """将session保存在内存"""
    def __init__(self):
        # self.container = {}
        pass
    def __contains__(self, item):
        print('__contains__:',item)
        return True
    def initial(self,random_str):
        container[random_str] = {}
    def get(self,random_str,key):
        return container[random_str].get(key)

    def set(self,random_str,key,value):
        container[random_str]={}
        container[random_str][key] = value
    def delete(self,random_str,key):
        del container[random_str][key]
    def open(self):
        pass
    def close(self):
        pass
    def clear(self,random_str):
        del container[random_str]

class Memcache(object):
    def __init__(self):
        pass
    def get(self,key):
        pass
    def set(self,key,value):
        pass
    def delete(self,key):
        pass
    def open(self):
        pass
    def close(self):
        pass

P = Cache           # 3. 可以是Memcache，根据用户自己选择要写入缓存还是数据库...

class Session(object):
    def __init__(self,handler):
        self.handler = handler
        self.random_str = None              # 随机字符串，也有可能是cookie
        self.ppp = P()
        # 去用户请求信息中获取session_id，如果没有，新用户
        self.client_random_str = self.handler.get_cookie('session_id')
        if not self.client_random_str:
            "新用户"
            self.random_str = self.create_random_str()
            container[self.random_str] = {}
        else:
            if self.client_random_str in self.ppp:
                "老用户"
                self.random_str = self.client_random_str
            else:
                "非法用户"
                self.random_str = self.create_random_str()
                self.ppp.initial(self.random_str)

        # 2. 生成cookie，必须调用LoginHandler才能使用set_cookie()
        timeOut = time.time()
        self.handler.set_cookie('session_id',self.random_str,expires=timeOut+1800)

        # 3. 写入缓存或数据库 Cahce、Memcache    ==> 后面用户自己调用session['uuuu'] = 'root'

    def create_random_str(self):
        now = str(time.time())
        m = hashlib.md5()
        m.update(bytes(now,encoding='utf-8'))
        return m.hexdigest()

    def __setitem__(self, key, value):
        # print(key,value)                 # key 就是用户自己设置session['uuuu']='root'中的uuuu，value就是root
        self.ppp.set(self.random_str, key, value)
        print('1',container)

    def __getitem__(self, item):
        # print(item)                       # uuuu
        # print('getitem',container)
        print('2',container)
        return self.ppp.get(self.random_str,item)

    def __delitem__(self, key):
        self.ppp.delete(self.random_str,key)
    def open(self):
        pass
    def cloes(self):
        pass

class Foo(object):
    def initialize(self):
        # print(self)         # <__main__.LoginHandler object at 0x00000000038702E8>
        self.session = Session(self)        # 传入Session的self就是调用者，谁调用Session谁就是self
        super(Foo, self).initialize()       # 执行RequestHandler中的initialize

class HomeHandler(Foo,tornado.web.RequestHandler):
    def get(self):
        user = self.session['uuuu']         # 调用Session类中的__getitem__方法, 获取value
        print('user',user)
        if not user:
            self.write('不是合法登录')
        else:
            self.write(user)
        print('哈哈哈测试成功，删除啦')
        del self.session['uuuu']
        print(container)

class LoginHandler(Foo,tornado.web.RequestHandler):
    def get(self):
        # self.session['uuuu']                  # 调用Session类中的__getitem__方法, 获取value
        # del self.session['uuuu']              # 调用Session类中的__delitem__方法, 删除
        self.session['uuuu'] = "root"           # 调用Session类中的__setitem__方法，在session里面设置了uuuu
        self.write("Hello, world")
        # print(container)
        self.redirect('/home')



application = tornado.web.Application([
    # (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/home", HomeHandler),
])

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()


