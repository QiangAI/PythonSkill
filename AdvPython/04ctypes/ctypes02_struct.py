import ctypes
#结构体
class Point(ctypes.Structure):
    _fields_=[("x",ctypes.c_int),("y",ctypes.c_byte,4)]

p=Point(200,5)
print(p)
print(p.x,p.y)


