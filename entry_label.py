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

        vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, 8)
        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 8)

        vbox.set_margin_start(5)
        vbox.set_margin_top(5)

        self.entry = Gtk.Entry()
        hbox.append(self.entry)

        keycont = Gtk.EventControllerKey()
        keycont.connect('key-released', self.on_key_released)
        self.add_controller(keycont)

        self.label = Gtk.Label.new('...')
        hbox.append(self.label)

        self.set_title('Entry')
        self.set_default_size(450, 350)

        vbox.append(hbox)
        self.set_child(vbox)


    def on_key_released(self, *_):
        self.label.set_text(self.entry.get_text())


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='com.zetcode.QuitButton')
app.connect('activate', on_activate)
app.run(None)