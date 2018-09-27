#coding=utf-8

#列表解析
data=(1,2,3,4,5)
x=[r+1 for r in data]
print(x)

#列表解析扩展
y=[r+1 for r in data if r%2==0] #过滤偶数
print(y)

#双解析
tata=(0.1,0.2,0.3)
z=[r+s for r in data for s in tata]
print(z)