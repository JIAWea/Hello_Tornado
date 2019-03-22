"""
模板标签不自动渲染
"""
from tornado import escape

def tab(request,val):


    # print(request)      # LoginHandler
    # print(val)          # 前端传过来的值
    return "<h1>这是模板</h1>"