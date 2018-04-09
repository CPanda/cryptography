"""
This is the main python file that will use functions from playfair, vigenere, etc.

Simple GTK Glade GUI.

"""

import playfair as pf #this one is not complete yet.
import vigenere as vc
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def decrypt_clicked(self, button):
        text = builder.get_object("maintext")
        print(vc.decrypt(text.get_text(), 'kool'))
    def encrypt_clicked_cb(self, button):
        text = builder.get_object("maintext")
        print(vc.encrypt(text.get_text(), 'kool'))

builder = Gtk.Builder()
builder.add_from_file("gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainwin")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()




