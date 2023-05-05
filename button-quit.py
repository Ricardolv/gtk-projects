#!/usr/bin/python

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Quit button')

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.set_margin_start(5)
        box.set_margin_top(5)

        btn = Gtk.Button(label="Quit")
        btn.connect('clicked', lambda _: self.close())

        btn.set_halign(Gtk.Align.START)
        box.append(btn)

        self.set_default_size(350, 250)
        self.set_child(box)


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='com.zetcode.QuitButton')
app.connect('activate', on_activate)
app.run(None)