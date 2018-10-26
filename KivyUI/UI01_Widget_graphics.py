#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import *
from kivy.core.window import Window

class WidgetApp(App):
    def build(self):
        widget=Widget()
        widget.size=Window.size
        #Kivy不提供专门的图形绘制函数，而是采用组件与绘制分离模式，这样，可以在任何地方实现图形绘制。
        with widget.canvas:
            #设置颜色
            Color(255,255,255)
            #绘制一个与Widget一样大小的矩形
            Rectangle(pos=widget.pos, size=widget.size)
            Color(255, 255, 0)
            Line(points=[0,0,widget.size[0],widget.size[1]],width=5)
            print(widget.size)
        return widget

app=WidgetApp()
app.run()
