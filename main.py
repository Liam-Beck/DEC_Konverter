import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Convert DEZ")

        #self.set_default_size(280, 180)
        self.width = 2
        grid = Gtk.Grid()
        self.add(grid)

        self.entry = Gtk.Entry()
        grid.attach(self.entry, 0, 0, self.width, 1)

        button = Gtk.Button.new_with_label("Convert")
        button.connect("clicked", self.on_button_convert)
        grid.attach(button, 0, 1, self.width, 1)

        self.table = Gtk.ListStore(str, str)
        self.table.append(["Binary Code", ""])
        self.table.append(["Octal Code", ""])
        self.table.append(["Hexidecimal", ""])

        self.tree = Gtk.TreeView(self.table)
        renderer = Gtk.CellRendererText()

        column1 = Gtk.TreeViewColumn("First", renderer, text=0)
        self.tree.append_column(column1)

        column2 = Gtk.TreeViewColumn("Second", renderer, text=1)
        self.tree.append_column(column2)

        grid.attach(self.tree, 0, 2, self.width, 1)

    def on_button_convert(self, button):
        self.decimal = self.entry.get_text()
        self.table.clear()
        self.table.append(["Binary Code", bin(int(self.decimal))])
        self.table.append(["Octal Code", oct(int(self.decimal))])
        self.table.append(["Hexidecimal", hex(int(self.decimal))])



win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()