#coding=utf-8
'''
class Data:
    pass

data=Data()
print(dir(data))    #打印属性，确认与迭代有关的属性
print(dir(Data))    #使用类打印属性。

for d in data:
    print(d)

'''
class Data:
    def __init__(self):
        self.counter=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter>=5: #控制迭代结束
            raise StopIteration
        else:
            self.counter+=1
            return "x"

data=Data()
for d in data:
    print(d)