#!/usr/bin/env python3
# =================================================================
# =          Authors: Brad Heffernan & Erik Dubois                =
# =================================================================
import gi
import os
import GUI
import conflicts
#import wnck
import subprocess
import threading
import webbrowser
import shutil
import socket
from time import sleep
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib, Wnck  # noqa

REMOTE_SERVER = "www.google.com"


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="FreedomOS Welcome")
        self.set_border_width(10)
        self.set_default_size(860, 250)
        self.set_icon_from_file(os.path.join(
            GUI.base_dir, 'images/freedomos-welcome.png'))
        self.set_position(Gtk.WindowPosition.CENTER)
        self.results = ""
        if not os.path.exists(GUI.home + "/.config/freedomos-welcome/"):
            os.mkdir(GUI.home + "/.config/freedomos-welcome/")
            with open(GUI.Settings, "w") as f:
                f.write("autostart=True")
                f.close()

        GUI.GUI(self, Gtk, GdkPixbuf)

        if GUI.username == GUI.user:
            t = threading.Thread(target=self.internet_notifier, args=())
            t.daemon = True
            t.start()

    def on_mirror_clicked(self, widget):
        t = threading.Thread(target=self.mirror_update)
        t.daemon = True
        t.start()

    def on_update_clicked(self, widget):
        print("Clicked")

    def on_ai_clicked(self, widget):
        t.start()
        subprocess.Popen(["/usr/bin/calamares_polkit", "-d"], shell=False)

    def on_aica_clicked(self, widget):
        t.start()
        subprocess.Popen(["/usr/bin/calamares_polkit", "-d"], shell=False)

    def on_gp_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["/usr/bin/gparted"],))
        t.daemon = True
        t.start()

    def on_buttonatt_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["/usr/bin/archlinux-tweak-tool"],))
        t.daemon = True
        t.start()

    def check_package_installed(self,package):
        try:
            subprocess.check_output("pacman -Qi " + package,shell=True,stderr=subprocess.STDOUT)
            #package is installed
            return True
        except subprocess.CalledProcessError as e:
            #package is not installed
            return False

    def on_buttonarandr_clicked(self,widget):
        if not self.check_package_installed("arandr"):
            install = 'pacman -S arandr --noconfirm'
            subprocess.call(install.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
            t = threading.Thread(target=self.run_app, args=(["/usr/bin/arandr"],))
            t.daemon = True
            t.start()
        else:
            t = threading.Thread(target=self.run_app, args=(["/usr/bin/arandr"],))
            t.daemon = True
            t.start()

    def on_buttonpamac_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["/usr/bin/pamac-manager"],))
        t.daemon = True
        t.start()

    def run_app(self, command):
        subprocess.call(command,
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    def statup_toggle(self, widget):
        if widget.get_active() is True:
            if os.path.isfile(GUI.dot_desktop):
                shutil.copy(GUI.dot_desktop, GUI.autostart)
        else:
            if os.path.isfile(GUI.autostart):
                os.unlink(GUI.autostart)
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(GUI.Settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if os.path.isfile(GUI.Settings):
            with open(GUI.Settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def on_link_clicked(self, widget, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_social_clicked(self, widget, event, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_info_clicked(self, widget, event):
        window_list = Wnck.Screen.get_default().get_windows()
        state = False
        for win in window_list:
            if "Information" in win.get_name():
                state = True
        if not state:
            w = conflicts.Conflicts()
            w.show_all()

    def weblink(self, link):
        webbrowser.open_new_tab(link)

    def is_connected(self):
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:  # noqa
            pass
        return False

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True

    def on_launch_clicked(self, widget, event, link):
        if os.path.isfile("/usr/bin/archlinux-tweak-tool"):
            t = threading.Thread(target=self.run_app,
                                 args=("/usr/bin/archlinux-tweak-tool",))
            t.daemon = True
            t.start()
        else:
            md = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.YES_NO,
                                   text="Not Found!")
            md.format_secondary_markup(
                "<b>ArcoLinux Tweak Tool</b> was not found on your system\n\
Do you want to install it?")

            result = md.run()

            md.destroy()

            if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
                t1 = threading.Thread(target=self.installATT, args=())
                t1.daemon = True
                t1.start()

    def internet_notifier(self):
        bb = 0
        dis = 0
        while(True):
            if not self.is_connected():
                dis = 1
                GLib.idle_add(self.button8.set_sensitive, False)
                GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Not connected to internet</i></b> \nCalamares will <b>not</b> install additional software</span>")  # noqa
            else:
                if bb == 0 and dis == 1:
                    GLib.idle_add(self.button8.set_sensitive, True)
                    GLib.idle_add(self.cc.set_text, "")
                    bb = 1
            sleep(3)

    # def mirror_reload(self):
    #     md = Gtk.MessageDialog(parent=self,
    #                            flags=0,
    #                            message_type=Gtk.MessageType.INFO,
    #                            buttons=Gtk.ButtonsType.YES_NO,
    #                            text="You are now connected")
    #     md.format_secondary_markup("Would you like to update the <b>Arch Linux</b> mirrorlist?")
    #     response = md.run()

    #     if response == Gtk.ResponseType.YES:
    #         GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Updating your mirrorlist</i></b> \nThis may take some time, please wait...</span>")  # noqa
    #         t = threading.Thread(target=self.mirror_update)
    #         t.daemon = True
    #         t.start()
    #     md.destroy()

    def mirror_update(self):
        GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Updating your mirrorlist</i></b> \nThis may take some time, please wait...</span>")  # noqa
        GLib.idle_add(self.button8.set_sensitive, False)
        subprocess.run(["pkexec", "/usr/bin/reflector", "--age", "6", "--latest", "21", "--fastest", "21", "--threads", "21", "--sort", "rate", "--protocol", "https", "--save", "/etc/pacman.d/mirrorlist"], shell=False)
        print("FINISHED!!!")
        GLib.idle_add(self.cc.set_markup, "<b>DONE</b>")
        GLib.idle_add(self.button8.set_sensitive, True)

    #def btrfs_update(self):
    #    if GUI.DEBUG:
    #        path = "/home/bheffernan/Repos/GITS/XFCE/hefftor-calamares-oem-config/calamares/modules/partition.conf"
    #    else:
    #        path = "/etc/calamares/modules/partition.conf"

    #    with open(path, "r") as f:
    #        lines = f.readlines()
    #        f.close()
    #    data = [x for x in lines if "defaultFileSystemType" in x]
    #    pos = lines.index(data[0])

    #    lines[pos] = "defaultFileSystemType:  \"ext4\"\n"

    #    with open(path, "w") as f:
    #        f.writelines(lines)
    #        f.close()

    #    GLib.idle_add(self.MessageBox,"Success", "Your filesystem has been changed.")

    # def finished_mirrors(self):
    #     md = Gtk.MessageDialog(parent=self,
    #                            flags=0,
    #                            message_type=Gtk.MessageType.INFO,
    #                            buttons=Gtk.ButtonsType.OK,
    #                            text="Finished")
    #     md.format_secondary_markup("Mirrorlist has been updated!")
    #     md.run()
    #     md.destroy()
    #     GLib.idle_add(self.cc.set_markup, "")
    #     GLib.idle_add(self.button8.set_sensitive, True)

    def MessageBox(self, title, message):
        md = Gtk.MessageDialog(parent=self,
                               flags=0,
                               message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK,
                               text=title)
        md.format_secondary_markup(message)
        md.run()
        md.destroy()


    def installATT(self):
        subprocess.call(["pkexec",
                         "/usr/bin/pacman",
                         "-S",
                         "archlinux-tweak-tool-git",
                         "--noconfirm"], shell=False)
        GLib.idle_add(self.MessageBox,
                      "Success!",
                      "<b>ArcoLinux Tweak Tool</b> has been installed successfully")  # noqa
    # def get_message(self, title, message):
    #     t = threading.Thread(target=self.fetch_notice,
#                              args=(title, message,))
    #     t.daemon = True
    #     t.start()
    #     t.join()

    # def fetch_notice(self, title, message):
    #     try:
    #         url = 'https://bradheff.github.io/notice/notice'
    #         req = requests.get(url, verify=True, timeout=1)

    #         if req.status_code == requests.codes.ok:
    #             if not len(req.text) <= 1:
    #                 title.set_markup(
    #                 "<big><b><u>Notice</u></b></big>")
    #                 message.set_markup(req.text)
    #                 self.results = True
    #             else:
    #                 self.results = False
    #         else:
    #             self.results = False
    #     except:
    #         self.results = False


if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
