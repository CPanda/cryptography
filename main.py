"""
This is the main python file that will use functions from playfair, vigenere, etc.

Simple GTK Glade GUI.

"""

import playfair
import vigenere
#import gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("gui.glade")

window = builder.get_object("mainwin")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()