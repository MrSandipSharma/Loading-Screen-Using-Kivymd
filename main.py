from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.lang import Builder
import threading
from kivy.properties import StringProperty

KV = """

<Item>
    orientation: "vertical"
    md_bg_color: "lightblue"

    Image:
        size_hint: None, None
        size: dp(800), dp(45)
        source: "one.png"
        pos_hint: {'center_x': .5, 'center_y': .5}

MDScreenManager:
    MDScreen:
        name: "one"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                anchor_title: "center"
                title: "Loading Page"

            MDProgressBar:
                id: progress
                color: 1,0,0,1
                size_hint_y:.01
                type: "indeterminate"

            MDBoxLayout:
                orientation: "vertical"
                size_hint_y:.2

                MDLabel:
                    text: "Screen One"
                    parent_background: 1,0,0,1
				    color: 219/255,230/255,193/255,1
				    halign: "center"
                    font_size: 35

            MDSpinner:
                id: spinner
                size_hint: None, None
                size: dp(46), dp(46)
                color: 1,0,0,1
                pos_hint: {'center_x': .5, 'center_y': .5}
                active: False

            MDGridLayout:
                cols: 1
                padding: [dp(15), dp(15), dp(15),dp(15)]
                spacing: dp(15)
                size_hint_y:.6
                MDRaisedButton:
                    text: "MDSpinner"
                    size_hint: .7, .3
                    on_press: 
                        app.load()

                MDRaisedButton:
                    text: "MDProgressBar"
                    size_hint: .7, .3
                    on_press: app.loadProgressBar()

                MDRaisedButton:
                    text: "MDDailog"
                    size_hint: .7, .3
                    on_press: app.loadattractive()

                MDRaisedButton:
                    text: "Loading Page"
                    size_hint: .7, .3
                    on_press: app.loadpage()


    MDScreen:
        name: "two"
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                text: "Screen Two"
                pos_hint: {'center_x': .5, 'center_y': .4}

            MDRaisedButton:
                text: "Back"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_press: root.current = "one"

    MDScreen:
        name: "load"
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                text: "Screen loading"
                parent_background: 1,0,0,1
				color: 219/255,230/255,193/255,1
				halign: "center"
                font_size: 35


"""
class Item(BoxLayout):
    divider = None

class LoadApp(MDApp):
    state = StringProperty("stop")
    dialog = None
    def build(self):
        self.title = "Loading Screen"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_state(self, instance, value):
        {
            "start": self.root.ids.progress.start,
            "stop": self.root.ids.progress.stop,
        }.get(value)()

    def load(self):
        self.root.ids.spinner.active = True
        threading.Thread(target=self.openpage3).start()

    def loadProgressBar(self):
        threading.Thread(target=self.openpage2).start()
        self.state = "start"

    def loadattractive(self):
        if not self.dialog:
            self.dialog = MDDialog(
                md_bg_color = (1,0,0,1),
                size_hint= (None, None),
                size= (dp(100), dp(40)),
                type="custom",
                content_cls=Item(),
            )
        self.dialog.open()
        threading.Thread(target=self.openpage).start()

    def loadpage(self):
        self.root.current = "load"
        threading.Thread(target=self.openpage4).start()

    def openpage(self):
        for i in range(10000):
            print(i)
        self.dialog.dismiss()
        self.root.current = "two"

    def openpage2(self):
        for i in range(10000):
            print(i)
        self.state = "stop"
        self.root.current = "two"

    def openpage3(self):
        for i in range(10000):
            print(i)
        self.root.ids.spinner.active = False
        self.root.current = "two"

    def openpage4(self):
        for i in range(10000):
            print(i)
        self.root.current = "two"

LoadApp().run()