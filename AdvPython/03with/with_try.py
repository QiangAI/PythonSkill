#coding=utf-8
import traceback
class MyWith:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        print("异常类型",exc_type)
        print("异常值", exc_val)
        print("异常跟踪",exc_tb)
        traceback.print_tb(exc_tb)
        print(":",traceback.format_tb(exc_tb))
        #return False    #需要调用者处理异常
        return True #调用者不处理异常

    def biz(self):
        print(1 / 0)  # 人为制造一个异常

o=MyWith()

with o as b:
    #b.biz()
    print(1 / 0)  # 人为制造一个异常
