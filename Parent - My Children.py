#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Dec 03, 2020 10:30:33 PM +07  platform: Windows NT

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

import Parent - My Children_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Parent - My Children_support.set_Tk_var()
    top = parent_mychildren (root)
    Parent - My Children_support.init(root, top)
    root.mainloop()

w = None
def create_parent_mychildren(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_parent_mychildren(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Parent - My Children_support.set_Tk_var()
    top = parent_mychildren (w)
    Parent - My Children_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_parent_mychildren():
    global w
    w.destroy()
    w = None

class parent_mychildren:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x358+654+111")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1,  1)
        top.title("Parent - My Children")
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
        self.navbar.place(relx=0.0, rely=0.0, relheight=0.084, relwidth=1.0)
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

        self.main_children = tk.LabelFrame(top)
        self.main_children.place(relx=0.017, rely=0.098, relheight=0.885
                , relwidth=0.967)
        self.main_children.configure(relief='flat')
        self.main_children.configure(borderwidth="4")
        self.main_children.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.main_children.configure(foreground="black")
        self.main_children.configure(relief="flat")
        self.main_children.configure(text='''My Children List''')
        self.main_children.configure(background="white")
        self.main_children.configure(highlightbackground="#ffffff")
        self.main_children.configure(highlightcolor="black")

        self.back_butt = tk.Button(self.main_children)
        self.back_butt.place(relx=0.448, rely=0.852, height=30, width=60
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

        self.children_box = ScrolledListBox(self.main_children)
        self.children_box.place(relx=0.207, rely=0.095, relheight=0.379
                , relwidth=0.621, bordermode='ignore')
        self.children_box.configure(background="white")
        self.children_box.configure(cursor="xterm")
        self.children_box.configure(disabledforeground="#bfbfbf")
        self.children_box.configure(font="TkFixedFont")
        self.children_box.configure(foreground="black")
        self.children_box.configure(highlightbackground="#ffffff")
        self.children_box.configure(highlightcolor="#ffffff")
        self.children_box.configure(selectbackground="blue")
        self.children_box.configure(selectforeground="white")
        self.children_box.configure(listvariable=Parent - My Children_support.my_child)

        self.add_child = tk.LabelFrame(self.main_children)
        self.add_child.place(relx=0.207, rely=0.473, relheight=0.315
                , relwidth=0.621, bordermode='ignore')
        self.add_child.configure(relief='groove')
        self.add_child.configure(foreground="black")
        self.add_child.configure(text='''Add Child''')
        self.add_child.configure(background="#ffffff")

        self.entry_name = tk.Entry(self.add_child)
        self.entry_name.place(relx=0.306, rely=0.2, height=30, relwidth=0.667
                , bordermode='ignore')
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#bfbfbf")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(insertbackground="black")

        self.Label1 = tk.Label(self.add_child)
        self.Label1.place(relx=0.014, rely=0.25, height=21, width=98
                , bordermode='ignore')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''New child name :''')

        self.add_butt = tk.Button(self.add_child)
        self.add_butt.place(relx=0.833, rely=0.6, height=25, width=50
                , bordermode='ignore')
        self.add_butt.configure(activebackground="#ececec")
        self.add_butt.configure(activeforeground="#000000")
        self.add_butt.configure(background="#ffffff")
        self.add_butt.configure(disabledforeground="#bfbfbf")
        self.add_butt.configure(foreground="#000000")
        self.add_butt.configure(highlightbackground="#ffffff")
        self.add_butt.configure(highlightcolor="black")
        self.add_butt.configure(pady="0")
        self.add_butt.configure(text='''add''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





