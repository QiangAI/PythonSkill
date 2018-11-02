import ctypes
#结构体
class Point(ctypes.Structure):
    _fields_=[("x",ctypes.c_byte,4),("y",ctypes.c_byte,4)]
    def __new__(self, buf):
        return self.from_buffer(buf,0)
    #参数与__new__保持一致
    def __init__(self,buf):
        self.x=6

a=ctypes.c_byte(20)
p2=Point(a)
print(p2.x,p2.y)


