# =================================================================
# =          Authors: Brad Heffernan & Erik Dubois
#
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
        "<big>Welcome to <b>FreedomOS</b></big>")
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/FreedomOS-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    label_warning = Gtk.Label(xalign=0)
    label_warning.set_justify(Gtk.Justification.CENTER)
    label_warning.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "Thank you for choosing to use <b>FreedomOS</b>.\n" +
            "Come and join our fourms and be the first to find out about\n" +  # noqa
            "updates and new features. pop over to our support page if you\n" +  # noqa
            "require any help.\n" +  # noqa
            "We are currently using a basic Calamares installer but this will\n" +  # noqa
            "have more features as we continue to grow.\n")
        label_warning.set_markup(
            "\n<span size='x-large'><b>Live Session, Nothing will be saved.")
    else:
        label2.set_markup(
            "The links below will get you started on <b>FreedomOS</b>.\n"
            "Come and join out fourms and be the first to find out about\n" +  # noqa
            "updates and new features. pop over to our support page if you\n" +  # noqa
            "require any help.\n")

    hbox4.set_center_widget(label2)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    #hbox4.pack_start(label2, False, False, 0)
    hbox8.pack_start(label_warning, True, False, 0)

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 80)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Install FreedomOS</b></span>")
    button2.connect("clicked", self.on_ai_clicked)
    button2.set_size_request(0, 80)



    self.button8 = Gtk.Button(label="")
    button8_label = self.button8.get_child()
    button8_label.set_markup("<span size='large'><b>Update Repo</b></span>")
    self.button8.connect("clicked", self.on_mirror_clicked)
    self.button8.set_size_request(420, 70)



    self.buttonpamac = Gtk.Button(label="")
    buttonpamac_label = self.buttonpamac.get_child()
    buttonpamac_label.set_markup("<span size='large'><b>Install software</b></span>")
    self.buttonpamac.connect("clicked", self.on_buttonpamac_clicked)
    self.buttonpamac.set_size_request(420, 70)

    # grid.add(button1)
    if username == user:
        grid = Gtk.Grid()
        #grid.attach(self.button8, 2, 0, 2, 2)
        #grid.attach(button13, 2, 0, 2, 2)
        grid.attach(button1, 2, 2, 2, 2)
        grid.attach(button2, 2, 4, 2, 2)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
    else:
        grid = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        #self.button8.set_size_request(300, 70)
        #self.buttonatt.set_size_request(300, 70)
        self.buttonpamac.set_size_request(300, 70)
        grid.pack_start(self.buttonpamac, True, False, 0)
        #grid.pack_start(self.buttonatt, True, False, 0)
        #grid.pack_start(self.button8, True, False, 0)
    # grid.set_row_homogeneous(True)

    # ======================================================================
    #                   NOTICE
    # ======================================================================

    # label3 = Gtk.Label(xalign=0)
    # label3.set_line_wrap(True)

    # label4 = Gtk.Label(xalign=0)
    # label4.set_line_wrap(True)

    # self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # self.vbox2.pack_start(label3, False,False,0)
    # self.vbox2.pack_start(label4, False,False,0)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("live")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("live")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================

    # change this one every year
    button3 = Gtk.Button(label="Website")
    button3.connect("clicked", self.on_link_clicked,
                    "https://freedomos.co.uk/")
    button3.set_size_request(180, 50)

    button4 = Gtk.Button(label="Github")
    button4.connect("clicked", self.on_link_clicked,
                    "https://github.com/freedomos")
    button4.set_size_request(180, 50)

    #button5 = Gtk.Button(label="Core info")
    #button5.connect("clicked", self.on_link_clicked,
    #                "https://FreedomOS.info/FreedomOS-editions/")
    #button5.set_size_request(180, 50)

    button6 = Gtk.Button(label="Wiki")
    button6.connect("clicked", self.on_link_clicked,
                    "https://freedomos-docs.readthedocs.io/en/latest/")
    button6.set_size_request(180, 50)

    button7 = Gtk.Button(label="Forum")
    button7.connect("clicked", self.on_link_clicked,
                    "https://sourceforge.net/p/freedomoslinux/discussion/")
    button7.set_size_request(180, 50)

    button70 = Gtk.Button(label="Screen resolution")
    button70.set_size_request(180, 50)
    button70.set_property("has-tooltip", True)
    button70.connect("query-tooltip",
                      self.tooltip_callback,
                      "Launch Arandr")
    button70.connect("clicked", self.on_buttonarandr_clicked)

    hbox2.pack_start(button3, True, True, 0)
    hbox2.pack_start(button4, True, True, 0)
    #hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)
    hbox2.pack_start(button70, True, True, 0)

    #button8 = Gtk.Button(label="")
    #button8_label = button8.get_child()
    #button8_label.set_markup("<b>P-holder</b>")
    #button8.connect("clicked", self.on_link_clicked,
    #                "")

    button9 = Gtk.Button(label="Become a Beta Tester")
    button9.connect("clicked", self.on_link_clicked,
                    "https://sourceforge.net/p/freedomoslinux/discussion/beta/")

    button10 = Gtk.Button(label="Get Involved - Github")
    button10.connect("clicked", self.on_link_clicked,
                     "https://github.com/freedomos")

    button11 = Gtk.Button(label="Donate")
    button11.connect("clicked", self.on_link_clicked,
                 "https://freedomos.co.uk/donate")

    button12 = Gtk.Button(label="Quit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)
    #button12.set_tooltip_markup("Quit the FreedomOS Welcome App")

    #hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)
    hbox5.pack_start(button12, True, True, 0)


    # hbox8.pack_start(self.button8, True, False, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================

    check = Gtk.CheckButton(label="Autostart")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)



    # ======================================================================
    #                   Start FreedomOS Tweak Tool
    # ======================================================================
    launchBox = Gtk.EventBox()
    pblaunch = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/archlinux-tweak-tool.svg'), 40, 40)
    launchimage = Gtk.Image().new_from_pixbuf(pblaunch)

    launchBox.add(launchimage)
    launchBox.connect("button_press_event", self.on_launch_clicked, "")

    launchBox.set_property("has-tooltip", True)
    launchBox.connect("query-tooltip",
                      self.tooltip_callback,
                      "Launch FreedomOS Tweak Tool")

    hbox6.pack_start(launchBox, False, False, 0)
    #hbox6.pack_start(infoE, False, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    label3 = Gtk.Label("v20.6-4")
    hbox7.pack_end(label3, False, False, 0)
    # if self.is_connected():
    #     self.get_message(label3, label4)

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label
    self.vbox.pack_start(hbox8, False, False, 7)  # warning Label

    self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares

    # if self.results and self.is_connected():
    #     self.vbox.pack_start(self.vbox2, False, False, 0)  # Notice

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    #self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
