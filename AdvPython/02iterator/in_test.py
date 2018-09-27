#coding=utf-8
#in的使用语法
str="This is Louis Young"

print("Young" in str)
print("You" in str)


#非迭代对象使用in
class Data:
    pass

data=Data()
#print("Y" in data)  #错误：TypeError: argument of type 'Data' is not iterable

#定制迭代对象使用in
class Tata:
    def __init__(self):
        self.counter=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter>5:
            raise StopIteration
        else:
            self.counter+=1
            return "Y"

tata=Tata()
print("Y" in tata)