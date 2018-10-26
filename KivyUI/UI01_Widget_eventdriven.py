#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core.window import Window

class WidgetApp(App):
    def build(self):
        widget=Widget()
        #2. 使用on_<属性名>绑定一个事件方法。
        widget.on_size=self.changeSize()
        #3.改变size会触发change方法的调用。
        widget.size=(Window.size[0]/2,Window.size[1]/2,)
        with widget.canvas:
            Color(0,255,255)
            Rectangle(pos=widget.pos, size=widget.size)
        return widget

    #1.实现一个事件方法
    def changeSize(self):
        print("Size Change")

app=WidgetApp()
app.run()

