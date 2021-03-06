#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Dec 03, 2020 10:45:35 PM +07  platform: Windows NT

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

import Parent - Give Alert_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = parent_givealert (root)
    Parent - Give Alert_support.init(root, top)
    root.mainloop()

w = None
def create_parent_givealert(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_parent_givealert(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = parent_givealert (w)
    Parent - Give Alert_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_parent_givealert():
    global w
    w.destroy()
    w = None

class parent_givealert:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x315+654+111")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1,  1)
        top.title("Parent - Give Alert")
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
        self.navbar.place(relx=0.0, rely=0.0, relheight=0.095, relwidth=1.0)
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

        self.main_alert = tk.LabelFrame(top)
        self.main_alert.place(relx=0.017, rely=0.111, relheight=0.873
                , relwidth=0.967)
        self.main_alert.configure(relief='flat')
        self.main_alert.configure(borderwidth="4")
        self.main_alert.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.main_alert.configure(foreground="black")
        self.main_alert.configure(relief="flat")
        self.main_alert.configure(text='''Alert''')
        self.main_alert.configure(background="white")
        self.main_alert.configure(highlightbackground="#ffffff")
        self.main_alert.configure(highlightcolor="black")

        self.set_name = tk.LabelFrame(self.main_alert)
        self.set_name.place(relx=0.198, rely=0.091, relheight=0.218
                , relwidth=0.603, bordermode='ignore')
        self.set_name.configure(relief='groove')
        self.set_name.configure(foreground="black")
        self.set_name.configure(text='''Name''')
        self.set_name.configure(background="#ffffff")
        self.set_name.configure(highlightbackground="#ffffff")
        self.set_name.configure(highlightcolor="black")

        self.entry_name = tk.Entry(self.set_name)
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

        self.back_butt = tk.Button(self.main_alert)
        self.back_butt.place(relx=0.362, rely=0.836, height=30, width=60
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

        self.message = tk.LabelFrame(self.main_alert)
        self.message.place(relx=0.198, rely=0.327, relheight=0.436
                , relwidth=0.603, bordermode='ignore')
        self.message.configure(relief='groove')
        self.message.configure(foreground="black")
        self.message.configure(text='''Message''')
        self.message.configure(background="#ffffff")
        self.message.configure(highlightbackground="#ffffff")
        self.message.configure(highlightcolor="black")

        self.entry_message = tk.Entry(self.message)
        self.entry_message.place(relx=0.029, rely=0.167, height=90
                , relwidth=0.943, bordermode='ignore')
        self.entry_message.configure(background="white")
        self.entry_message.configure(disabledforeground="#bfbfbf")
        self.entry_message.configure(font="TkFixedFont")
        self.entry_message.configure(foreground="#000000")
        self.entry_message.configure(highlightbackground="#ffffff")
        self.entry_message.configure(highlightcolor="black")
        self.entry_message.configure(insertbackground="black")
        self.entry_message.configure(selectbackground="blue")
        self.entry_message.configure(selectforeground="white")

        self.send_butt = tk.Button(self.main_alert)
        self.send_butt.place(relx=0.474, rely=0.836, height=30, width=80
                , bordermode='ignore')
        self.send_butt.configure(activebackground="#05bff5")
        self.send_butt.configure(activeforeground="white")
        self.send_butt.configure(background="white")
        self.send_butt.configure(cursor="fleur")
        self.send_butt.configure(disabledforeground="#bfbfbf")
        self.send_butt.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.send_butt.configure(foreground="#05bff5")
        self.send_butt.configure(highlightbackground="#ffffff")
        self.send_butt.configure(highlightcolor="black")
        self.send_butt.configure(pady="0")
        self.send_butt.configure(text='''send alert''')

if __name__ == '__main__':
    vp_start_gui()





