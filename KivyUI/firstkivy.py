#coding=utf-8

#kivy入门：kivy程序结构
from kivy.app import App
from kivy.uix.screenmanager import Screen

#继承实现一个App类
class KivyFirstApp(App):
    #覆盖build函数，返回一个Widget组件
    def build(self):
        return Screen()

#构造一个App对象
app=KivyFirstApp()
#调用run启动App应用的UI消息循环
app.run()