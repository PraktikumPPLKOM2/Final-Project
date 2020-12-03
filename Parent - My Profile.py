#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Dec 01, 2020 10:48:43 AM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Parent - My Profile_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = parent_myprofile (root)
    Parent - My Profile_support.init(root, top)
    root.mainloop()

w = None
def create_parent_myprofile(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_parent_myprofile(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = parent_myprofile (w)
    Parent - My Profile_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_parent_myprofile():
    global w
    w.destroy()
    w = None

class parent_myprofile:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x480+654+111")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1,  1)
        top.title("Parent - My Profile")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#ffffff")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg='#05bff5')
        top.configure(menu = self.menubar)

        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.sub_menu = tk.Menu(top,
                activebackground="white",
                activeborderwidth=1,
                activeforeground="#05bff5",
                background="#ffffff",
                borderwidth=1,
                disabledforeground="#bfbfbf",
                foreground="#05bff5",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                label="Profile")
        self.sub_menu.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="My Profile")
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#ffffff",
                borderwidth=1,
                disabledforeground="#bfbfbf",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Children")
        self.sub_menu1.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="My Children")
        self.sub_menu1.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="My Child's Assignment")
        self.sub_menu1.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="Give Alert")

        self.navbar = tk.Frame(top)
        self.navbar.place(relx=0.0, rely=0.0, relheight=0.063, relwidth=1.0)
        self.navbar.configure(relief='flat')
        self.navbar.configure(borderwidth="2")
        self.navbar.configure(background="#05bff5")
        self.navbar.configure(highlightbackground="#ffffff")
        self.navbar.configure(highlightcolor="black")

        self.logout_butt = tk.Button(self.navbar)
        self.logout_butt.place(relx=0.9, rely=0.0, height=30, width=60)
        self.logout_butt.configure(activebackground="white")
        self.logout_butt.configure(activeforeground="#000000")
        self.logout_butt.configure(background="white")
        self.logout_butt.configure(disabledforeground="black")
        self.logout_butt.configure(font="-family {Arcon Rounded-} -size 9")
        self.logout_butt.configure(foreground="#05bff5")
        self.logout_butt.configure(highlightbackground="#ffffff")
        self.logout_butt.configure(highlightcolor="black")
        self.logout_butt.configure(pady="0")
        self.logout_butt.configure(relief="flat")
        self.logout_butt.configure(text='''Logout''')

        self.app_name = tk.Label(self.navbar)
        self.app_name.place(relx=0.0, rely=0.0, height=30, width=120)
        self.app_name.configure(activebackground="#05bff5")
        self.app_name.configure(activeforeground="white")
        self.app_name.configure(background="#05bff5")
        self.app_name.configure(disabledforeground="black")
        self.app_name.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.app_name.configure(foreground="white")
        self.app_name.configure(highlightbackground="#ffffff")
        self.app_name.configure(highlightcolor="black")
        self.app_name.configure(text='''Buku Penghubung''')

        self.main_profile = tk.LabelFrame(top)
        self.main_profile.place(relx=0.017, rely=0.075, relheight=0.904
                , relwidth=0.967)
        self.main_profile.configure(relief='flat')
        self.main_profile.configure(borderwidth="4")
        self.main_profile.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.main_profile.configure(foreground="black")
        self.main_profile.configure(relief="flat")
        self.main_profile.configure(text='''My Profile''')
        self.main_profile.configure(background="white")
        self.main_profile.configure(highlightbackground="#ffffff")
        self.main_profile.configure(highlightcolor="black")

        self.get_name = tk.LabelFrame(self.main_profile)
        self.get_name.place(relx=0.198, rely=0.069, relheight=0.138
                , relwidth=0.603, bordermode='ignore')
        self.get_name.configure(relief='groove')
        self.get_name.configure(foreground="black")
        self.get_name.configure(text='''Name''')
        self.get_name.configure(background="#ffffff")
        self.get_name.configure(highlightbackground="#ffffff")
        self.get_name.configure(highlightcolor="black")

        self.entry_name = tk.Entry(self.get_name)
        self.entry_name.place(relx=0.029, rely=0.367, height=30, relwidth=0.943
                , bordermode='ignore')
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#bfbfbf")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(highlightbackground="#ffffff")
        self.entry_name.configure(highlightcolor="black")
        self.entry_name.configure(insertbackground="black")
        self.entry_name.configure(selectbackground="blue")
        self.entry_name.configure(selectforeground="white")

        self.get_username = tk.LabelFrame(self.main_profile)
        self.get_username.place(relx=0.198, rely=0.207, relheight=0.138
                , relwidth=0.603, bordermode='ignore')
        self.get_username.configure(relief='groove')
        self.get_username.configure(foreground="black")
        self.get_username.configure(text='''Username''')
        self.get_username.configure(background="#ffffff")
        self.get_username.configure(highlightbackground="#ffffff")
        self.get_username.configure(highlightcolor="black")

        self.entry_username = tk.Entry(self.get_username)
        self.entry_username.place(relx=0.029, rely=0.35, height=30
                , relwidth=0.943, bordermode='ignore')
        self.entry_username.configure(background="white")
        self.entry_username.configure(disabledforeground="#bfbfbf")
        self.entry_username.configure(font="TkFixedFont")
        self.entry_username.configure(foreground="#000000")
        self.entry_username.configure(highlightbackground="#ffffff")
        self.entry_username.configure(highlightcolor="black")
        self.entry_username.configure(insertbackground="black")
        self.entry_username.configure(selectbackground="blue")
        self.entry_username.configure(selectforeground="white")

        self.get_email = tk.LabelFrame(self.main_profile)
        self.get_email.place(relx=0.198, rely=0.346, relheight=0.138
                , relwidth=0.603, bordermode='ignore')
        self.get_email.configure(relief='groove')
        self.get_email.configure(foreground="black")
        self.get_email.configure(text='''Email''')
        self.get_email.configure(background="#ffffff")
        self.get_email.configure(highlightbackground="#ffffff")
        self.get_email.configure(highlightcolor="black")

        self.entry_email = tk.Entry(self.get_email)
        self.entry_email.place(relx=0.029, rely=0.333, height=30, relwidth=0.943
                , bordermode='ignore')
        self.entry_email.configure(background="white")
        self.entry_email.configure(disabledforeground="#bfbfbf")
        self.entry_email.configure(font="TkFixedFont")
        self.entry_email.configure(foreground="#000000")
        self.entry_email.configure(highlightbackground="#ffffff")
        self.entry_email.configure(highlightcolor="black")
        self.entry_email.configure(insertbackground="black")
        self.entry_email.configure(selectbackground="blue")
        self.entry_email.configure(selectforeground="white")

        self.get_phone_number = tk.LabelFrame(self.main_profile)
        self.get_phone_number.place(relx=0.198, rely=0.484, relheight=0.138
                , relwidth=0.603, bordermode='ignore')
        self.get_phone_number.configure(relief='groove')
        self.get_phone_number.configure(foreground="black")
        self.get_phone_number.configure(text='''Phone Number''')
        self.get_phone_number.configure(background="#ffffff")
        self.get_phone_number.configure(highlightbackground="#ffffff")
        self.get_phone_number.configure(highlightcolor="black")

        self.entry_phone_number = tk.Entry(self.get_phone_number)
        self.entry_phone_number.place(relx=0.029, rely=0.333, height=30
                , relwidth=0.943, bordermode='ignore')
        self.entry_phone_number.configure(background="white")
        self.entry_phone_number.configure(disabledforeground="#bfbfbf")
        self.entry_phone_number.configure(font="TkFixedFont")
        self.entry_phone_number.configure(foreground="#000000")
        self.entry_phone_number.configure(highlightbackground="#ffffff")
        self.entry_phone_number.configure(highlightcolor="black")
        self.entry_phone_number.configure(insertbackground="black")
        self.entry_phone_number.configure(selectbackground="blue")
        self.entry_phone_number.configure(selectforeground="white")

        self.get_address = tk.LabelFrame(self.main_profile)
        self.get_address.place(relx=0.198, rely=0.622, relheight=0.233
                , relwidth=0.603, bordermode='ignore')
        self.get_address.configure(relief='groove')
        self.get_address.configure(foreground="black")
        self.get_address.configure(text='''Address''')
        self.get_address.configure(background="#ffffff")
        self.get_address.configure(highlightbackground="#ffffff")
        self.get_address.configure(highlightcolor="black")

        self.entry_address = tk.Entry(self.get_address)
        self.entry_address.place(relx=0.029, rely=0.168, height=75
                , relwidth=0.943, bordermode='ignore')
        self.entry_address.configure(background="white")
        self.entry_address.configure(disabledforeground="#bfbfbf")
        self.entry_address.configure(font="TkFixedFont")
        self.entry_address.configure(foreground="#000000")
        self.entry_address.configure(highlightbackground="#ffffff")
        self.entry_address.configure(highlightcolor="black")
        self.entry_address.configure(insertbackground="black")
        self.entry_address.configure(selectbackground="blue")
        self.entry_address.configure(selectforeground="white")

        self.back_butt = tk.Button(self.main_profile)
        self.back_butt.place(relx=0.448, rely=0.894, height=30, width=60
                , bordermode='ignore')
        self.back_butt.configure(activebackground="#05bff5")
        self.back_butt.configure(activeforeground="white")
        self.back_butt.configure(background="white")
        self.back_butt.configure(disabledforeground="#bfbfbf")
        self.back_butt.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.back_butt.configure(foreground="#05bff5")
        self.back_butt.configure(highlightbackground="#ffffff")
        self.back_butt.configure(highlightcolor="black")
        self.back_butt.configure(pady="0")
        self.back_butt.configure(text='''back''')

if __name__ == '__main__':
    vp_start_gui()





