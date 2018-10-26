#coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core.window import Window

class TheWidget(Widget):
    def on_touch_down(self, touch):
        print("self.size=",self.size,"self.pos=",self.pos,"touch.pos=",touch.pos)
        print(self.collide_point(*touch.pos))

class TheApp(App):
    def build(self):
        parent_widget=Widget()
        with parent_widget.canvas:
            Color(255,0,0)
            Rectangle(pos=parent_widget.pos,size=Window.size)

        child_widget = TheWidget(size=(400,400))
        with child_widget.canvas:
            Color(0,255,0)
            Rectangle(pos=child_widget.pos,size=child_widget.size)
        parent_widget.add_widget(child_widget)
        return parent_widget

TheApp().run()
