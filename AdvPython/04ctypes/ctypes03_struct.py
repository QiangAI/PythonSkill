import ctypes
#结构体
class Point(ctypes.Structure):
    _fields_=[("x",ctypes.c_byte,4),("y",ctypes.c_byte,4)]

a=ctypes.c_byte(20)
p2=Point.from_buffer(a,0)
print(p2)
print(p2.x,p2.y)
