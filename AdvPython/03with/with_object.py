#coding=utf-8
class MyWith:
    def __enter__(self):
        print("enter")
        print(1/0)      #人为制造一个异常
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        print(exc_type,exc_val,exc_tb)

o=MyWith()
with o as b:
    print("执行with过程！",b)        #b就是__enter__返回的值

