# class C:
#     def f1(self):
#         print('C')
# class A(C):
#     def f1(self):
#         print('A')
#         B.f1(self)
# class B:
#     def f1(self):
#         print('B')
# class Foo(A, B):
#     pass
#
# obj = Foo()
# obj.f1()

class Foo:
    def __contains__(self, item):
        print(item)
        return True

obj = Foo()

v = "x" in obj  # 直接调用Foo类的__contains__方法
print(v)        # True

##########################################################################
class Bar(object):
    def __init__(self):
        pass
    def __setitem__(self, key, value):
        print(key,value)        # key就是name，value就是ray
    def __getitem__(self, item):
        print(item)             # item就是name
    def __delitem__(self, key):
        print(key)              # key就是name

obj = Bar()
obj['name'] = 'ray'             # 调用setitem
obj['name']                     # 调用getitem
del obj['name']                 # 调用delitem

