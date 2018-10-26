from contextlib import contextmanager
'''
@contextmanager
def TheWith():
    try:
        print('enter')
        yield '返回的as后面的值'
        print("exit")
    except Exception as e:
        print(e)
        print("这里做关闭工作")

with TheWith() as w:
    print("With过程：",w)
    print(1/0)
'''
@contextmanager
def TheWith():
    print('enter')
    yield '返回的as后面的值'
    print("exit")

with TheWith() as w:
    print("With过程：",w)

