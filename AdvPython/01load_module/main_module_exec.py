#coding=utf-8
print('this is a main module!')
re=exec("a=20;print(a);")

print(a)

print(re)

#exec("class A:pass",globals=globals(),locals=locals())  #不能带参数名，这个语句错误
exec("class A:pass",globals(),locals())
o=A()
print(o)
print(globals())


#代码修改
