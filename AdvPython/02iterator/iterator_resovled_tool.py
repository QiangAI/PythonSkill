#coding=utf-8

#range列表解析函数
'''
range(stop)
range(start, stop[, step])
'''
rng=range(10)
print(rng)
for i in rng:
    print(i)


'''
tuple([iterable])
'''
tup=tuple(range(5)) #把range可迭代对象转换为元组
print(tup)
for i in tup:
    print(i)

'''
class list([iterable])
'''
lst=list(range(5))
print(lst)

'''
map(function, iterable, ...)#function的参数个数对应后面的迭代器对象个数
'''
mp=map(lambda x,y:x+y,range(4),range(6,11))
print(tuple(mp))

'''
class set([iterable]) 返回内置的set类型对象
'''
s={3,1,4,2}
t=set(range(5))
v={i for i in [3,2,5,1]}
print(s)        #{1, 2, 3, 4}
print(t)        #{0, 1, 2, 3, 4}
print(v)       #{1, 2, 3, 5}

'''
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
'''
dt1=dict(name="louis",age=20)           #**kwarg
dt2=dict({"name":"louis","age":20},price=24.88)    #mapping, **kwarg
dt3=dict([("name","louis"),("age",20)],price=24.88) #iterable, **kwarg
print(dt1)
print(dt2)
print(dt3)

'''
filter(function, iterable)
使用function过滤迭代器
'''

flt=filter(lambda x:True if x>0 else False,(1,-2,5,-7,-3,9))
print(list(flt))    #[1, 5, 9]

'''
zip(*iterables)
'''
zp=zip(("name","age","price",4),("louis",20,27.88))
#print(list(zp)) #[('name', 'louis'), ('age', 20), ('price', 27.88)]
print(dict(zp)) #{'name': 'louis', 'age': 20, 'price': 27.88}   #如果上面运行后，该语句返回{}


