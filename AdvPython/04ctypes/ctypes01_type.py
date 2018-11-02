import ctypes
v = ctypes.c_int ( 2 )
print ( v )
print ( v.value )
s = ctypes.c_wchar_p  ("这是一个字符串" )
print ( s )
print ( s.value )

#从其他字节序列中拷贝
v2=ctypes.c_int.from_buffer(v,0)
print(v2,v2.value)
a=20
v3=ctypes.c_int.from_param(a)
print(v3)

