from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):
    def change_to_templates(self):
        if not self.manager.has_screen("templates"):
            Builder.load_file("libs/uix/kv/templates_screen.kv")
            from libs.uix.baseclass.templates_screen import TemplatesScreen

            screen_object = TemplatesScreen(name="templates")
            self.manager.add_widget(screen_object)
        self.manager.current = "templates"