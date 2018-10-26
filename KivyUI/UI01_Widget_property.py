#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class WidgetApp(App):
    def build(self):
        widget=Widget(opacity=0.5,size=Window.size)
        with widget.canvas:
            #设置颜色
            Color(255,255,255)
            #绘制一个与Widget一样大小的矩形
            Rectangle(pos=widget.pos, size=widget.size)
        return widget

app=WidgetApp()
app.run()
