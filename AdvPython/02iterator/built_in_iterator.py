#coding=utf-8
'''
内置可迭代对象
'''

#字符串迭代
str="Louis Young"
for c in str:
    print(c)

#列表迭代
lst=[1,2,3,4]
for l in lst:
    print(l)
#元组迭代
tpl=(1,2,3,4)
for t in tpl:
    print(t)

#文件迭代
fil=open("data.txt")
for r in fil:
    print(r)

#字典迭代
dit={"name":"Louis","age":20}
for key in dit.keys():
    print(key,":",dit[key])

for key in dit:     #直接迭代key键值
    print(key, ":", dit[key])