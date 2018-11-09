#coding=utf-8
import js2py
script=r'''
    a=20;
    f=function(param1,param2){
        return param1+param2
    }
'''
#构造JS执行上下文环境
ctx = js2py.EvalJs()
#加载脚本
ctx.execute(script)
#访问变量
print(ctx.a)    #20
#调用函数
print(ctx.f(45,55)) #100
