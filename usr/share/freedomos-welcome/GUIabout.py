# =================================================================
#
#
# =     Authors: Brad Heffernan & Erik Dubois & Frazer Grant      =
# =================================================================
import os
import getpass
from os.path import expanduser
DEBUG = False
#DEBUG = True

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()
if DEBUG:
    user = username
else:
    user = "live"

Settings = home + "/.config/freedomos-welcome/settings.conf"
Skel_Settings = "/etc/skel/.config/freedomos-welcome/settings.conf"
dot_desktop = "/usr/share/applications/freedomos-welcome.desktop"
autostart = home + "/.config/autostart/freedomos-welcome.desktop"


def GUI(self, Gtk, GdkPixbuf):

    autostart = eval(self.load_settings())

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    infoE = Gtk.EventBox()
    pbinfo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/question.png'), 38, 38)
    infoimage = Gtk.Image().new_from_pixbuf(pbinfo)
    infoE.add(infoimage)
    infoE.connect("button_press_event", self.on_info_clicked)
    infoE.set_property("has-tooltip", True)
    infoE.connect("query-tooltip", self.tooltip_callback, "Conflicts Info")



    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>About <b>FreedomOS Welcome</b></big>")
    label.set_line_wrap(True)

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/FreedomOS-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    label_warning = Gtk.Label(xalign=0)
    label_warning.set_justify(Gtk.Justification.CENTER)
    label_warning.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "FreedomOS Welcome is built from <b>ArcoLinux Welcome App Version 22-05-12</b>.\n" +
            "Authors (ArcoLinux Welcome): Brad Heffernan and Erik Dubois\n"  # noqa
            "FreedomOS Welcome has been changed/ modified to suit the requirements of FreedomOS\n")
    else:
        label2.set_markup (
            "FreedomOS Welcome is built from <b>ArcoLinux Welcome App Version 22-05-12</b>.\n" +
            "Authors (ArcoLinux Welcome): Brad Heffernan and Erik Dubois\n"  # noqa
            "FreedomOS Welcome has been changed/ modified to suit the requirements of FreedomOS\n")

    hbox4.set_center_widget(label2)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    #hbox4.pack_start(label2, False, False, 0)
    hbox8.pack_start(label_warning, True, False, 0)



    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label
    self.vbox.pack_start(hbox8, False, False, 7)  # warning Label

    button12 = Gtk.Button(label="Quit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)
    #button12.set_tooltip_markup("Quit the FreedomOS Welcome App")



    hbox5.pack_start(button12, True, True, 0)

    # if self.results and self.is_connected():
    #     self.vbox.pack_start(self.vbox2, False, False, 0)  # Notice

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    #self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
