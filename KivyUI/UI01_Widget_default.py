#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core.window import Window

class MyWidget(Widget):
    # 3. on_touch_down(), on_touch_move(), on_touch_up() 不检测Widget的触发边界
    # 点击Widget区域之外，事件照样触发。
    def on_touch_up(self, touch):
        print(touch)

class WidgetApp(App):
    def build(self):
        widget=MyWidget()

        #1. size与size_hint的默认值。
        print("大小:(%d,%d)"%(widget.width,widget.height))         #(100，100)
        print("大小提示(%d,%d)"%(widget.size_hint[0],widget.size_hint[1]))                #(1,1)

        widget.size = (Window.size[0] / 2, Window.size[1] / 2,)     #是窗体一般大小。

        with widget.canvas:
            Color(0,255,255)
            Rectangle(pos=widget.pos, size=widget.size)

        #2. 不改变子组件的位置与大小
        widget2=Widget()
        widget.add_widget(widget2)

        with widget2.canvas:
            Color(255,0,255)
            Rectangle(pos=widget2.pos, size=widget2.size)

        return widget

app=WidgetApp()
app.run()

