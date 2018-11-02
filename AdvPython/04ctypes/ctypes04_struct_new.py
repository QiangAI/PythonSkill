import ctypes
#结构体
class Point(ctypes.Structure):
    _fields_=[("x",ctypes.c_byte,4),("y",ctypes.c_byte,4)]
    def __new__(self, buf):
        return self.from_buffer(buf,0)

a=ctypes.c_byte(20)
p2=Point(a)
print(p2.x,p2.y)

#p3=Point(2,2)  #这种方式就不能再使用，参数个数无法匹配

