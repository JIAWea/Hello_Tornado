"""
模板自动帮我们渲染
"""

from tornado.web import UIModule
from tornado import escape

class Foo(UIModule):
    def css_files(self):
        """添加static下面的common.css样式到login.html"""
        return "common.css"
    def embedded_css(self):
        """添加下面的样式到login.html"""
        return ".c1{display:none}"
    def javascript_files(self):
        """添加static下面的common.js样式到login.html"""
        return "common.js"
    def embedded_javascript(self):
        """添加下面的JS样式到login.html"""
        return "function fun(){alert(1)}"

    def render(self):

        return "<h1>这是modules模板</h1>"
        # return escape.xhtml_escape("<h1>这是modules模板</h1>")