#coding=utf-8

#传统写法
file = open("with_try.py")
try:
    data = file.read()
    print(data)
finally:
    file.close()

#简洁写法
with open("with_try.py") as file:
    data = file.read()
    print(data)