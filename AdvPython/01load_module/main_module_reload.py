#coding=utf-8
import imp
import sub_module_1
print('this is a main module!')
re=imp.reload(sub_module_1)
print(re)