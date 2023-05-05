#!/usr/bin/python

import gi
gi.require_version('Gtk', '4.0')
import math
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Drawing')

        area = Gtk.DrawingArea.new()
        area.set_draw_func(self.on_draw)

        self.set_default_size(450, 300)
        self.set_child(area)


    def on_draw(self, da, ctx, w, h):

        ctx.set_source_rgb(0.6, 0.6, 0.6)

        ctx.rectangle(20, 20, 120, 80)
        ctx.rectangle(180, 20, 80, 80)
        ctx.fill()

        ctx.arc(330, 60, 40, 0, 2*math.pi)
        ctx.fill()

        ctx.arc(90, 160, 40, math.pi/4, math.pi)
        ctx.fill()

        ctx.translate(220, 180)

        ctx.scale(1, 0.7)
        ctx.arc(0, 0, 50, 0, 2*math.pi)
        ctx.fill()


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='com.zetcode.Drawing')
app.connect('activate', on_activate)
app.run(None)