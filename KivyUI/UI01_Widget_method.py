#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class MyWidget(Widget):
    def on_touch_down(self, touch):
        print("点击位置：",touch.pos)
        print("local:",self.to_local(*touch.pos,relative=True))
        print("parent:", self.to_parent(*touch.pos,relative=True))
        print("widget:", self.to_widget(*touch.pos,relative=True))
        print("window:", self.to_window(*touch.pos,relative=True))

class WidgetApp(App):
    def build(self):
        widget=Widget(size=Window.size)
        with widget.canvas:
            #设置颜色
            Color(255,0,255)
            #绘制一个与Widget一样大小的矩形
            Rectangle(pos=widget.pos, size=widget.size)

        mywidget=MyWidget(size=(400,400),pos=(200,200))
        with mywidget.canvas:
            #设置颜色
            Color(0,0,255)
            #绘制一个与Widget一样大小的矩形
            Rectangle(pos=mywidget.pos, size=mywidget.size)

        widget.add_widget(mywidget)

        widget.export_to_png("img.png")

        return widget

app=WidgetApp()
app.run()
