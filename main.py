import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Convert DEZ")


        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.box.pack_start(self.entry, True, True, 0)

        button = Gtk.Button.new_with_label("Convert")
        button.connect("clicked", self.on_button_convert)
        self.box.pack_start(button, True, True, 0)

        self.table = Gtk.ListStore(str, str)
        self.show_all()

    def on_button_convert(self, button):
        treeiter = self.table.append(["Binary Code", "010001101"])
        self.show_all()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()