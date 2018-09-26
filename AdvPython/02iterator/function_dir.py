#coding=utf-8
#可循环对象
str="Louis Young"   #字符串
lst=[1,2,3,4]       #列表
tpl=(1,2,3,4)       #元组
fle=open("data.txt")    #文件

print(dir(str))
print(dir(lst))
print(dir(tpl))
print(dir(fle))


#可循环对象，都有一个—__iter__方法
