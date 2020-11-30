#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 30, 2020 08:29:29 AM +07  platform: Windows NT

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

import Student - My Assignments_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Student - My Assignments_support.set_Tk_var()
    top = student_myassignments (root)
    Student - My Assignments_support.init(root, top)
    root.mainloop()

w = None
def create_student_myassignments(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_student_myassignments(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Student - My Assignments_support.set_Tk_var()
    top = student_myassignments (w)
    Student - My Assignments_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_student_myassignments():
    global w
    w.destroy()
    w = None

class student_myassignments:
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

        top.geometry("600x380+604+121")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1,  1)
        top.title("Student - My Assignments")
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
                label="Classes")
        self.sub_menu1.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="Add Class")
        self.sub_menu1.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="My Classes")
        self.menubar.add_separator(
)
        self.menubar.add_separator(
)
        self.sub_menu12 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#ffffff",
                borderwidth=1,
                disabledforeground="#bfbfbf",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                label="Assignment")
        self.sub_menu12.add_command(
                activebackground="white",
                activeforeground="#05bff5",
                background="white",
                foreground="black",
                label="My Assignment")

        self.navbar = tk.Frame(top)
        self.navbar.place(relx=0.0, rely=0.0, relheight=0.071, relwidth=1.0)
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
        self.app_name.place(relx=0.0, rely=0.0, height=27, width=120)
        self.app_name.configure(activebackground="#05bff5")
        self.app_name.configure(activeforeground="white")
        self.app_name.configure(background="#05bff5")
        self.app_name.configure(disabledforeground="black")
        self.app_name.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.app_name.configure(foreground="white")
        self.app_name.configure(highlightbackground="#ffffff")
        self.app_name.configure(highlightcolor="black")
        self.app_name.configure(text='''Buku Penghubung''')

        self.main_assignments = tk.LabelFrame(top)
        self.main_assignments.place(relx=0.017, rely=0.095, relheight=0.882
                , relwidth=0.967)
        self.main_assignments.configure(relief='flat')
        self.main_assignments.configure(borderwidth="4")
        self.main_assignments.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.main_assignments.configure(foreground="black")
        self.main_assignments.configure(relief="flat")
        self.main_assignments.configure(text='''My Assignments''')
        self.main_assignments.configure(background="white")
        self.main_assignments.configure(highlightbackground="#ffffff")
        self.main_assignments.configure(highlightcolor="black")

        self.back_butt = tk.Button(self.main_assignments)
        self.back_butt.place(relx=0.388, rely=0.881, height=30, width=60
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

        self.box_class = ScrolledListBox(self.main_assignments)
        self.box_class.place(relx=0.033, rely=0.078, relheight=0.737
                , relwidth=0.333, bordermode='ignore')
        self.box_class.configure(background="white")
        self.box_class.configure(cursor="xterm")
        self.box_class.configure(disabledforeground="#bfbfbf")
        self.box_class.configure(font="TkFixedFont")
        self.box_class.configure(foreground="black")
        self.box_class.configure(highlightbackground="#ffffff")
        self.box_class.configure(highlightcolor="#ffffff")
        self.box_class.configure(selectbackground="white")
        self.box_class.configure(selectforeground="#05bff5")
        self.box_class.configure(listvariable=Student - My Assignments_support.class_n)

        self.class_detail = tk.Frame(self.main_assignments)
        self.class_detail.place(relx=0.383, rely=0.078, relheight=0.737
                , relwidth=0.583, bordermode='ignore')
        self.class_detail.configure(relief='groove')
        self.class_detail.configure(borderwidth="2")
        self.class_detail.configure(relief="groove")
        self.class_detail.configure(background="#ffffff")
        self.class_detail.configure(highlightbackground="#ffffff")
        self.class_detail.configure(highlightcolor="black")

        self.class_name = tk.LabelFrame(self.class_detail)
        self.class_name.place(relx=0.03, rely=0.04, relheight=0.243
                , relwidth=0.947)
        self.class_name.configure(relief='groove')
        self.class_name.configure(foreground="black")
        self.class_name.configure(text='''Name''')
        self.class_name.configure(background="#ffffff")
        self.class_name.configure(highlightbackground="#ffffff")
        self.class_name.configure(highlightcolor="black")

        self.get_assignment_name = tk.Text(self.class_name)
        self.get_assignment_name.place(relx=0.031, rely=0.333, relheight=0.5
                , relwidth=0.938, bordermode='ignore')
        self.get_assignment_name.configure(background="white")
        self.get_assignment_name.configure(font="TkTextFont")
        self.get_assignment_name.configure(foreground="black")
        self.get_assignment_name.configure(highlightbackground="#ffffff")
        self.get_assignment_name.configure(highlightcolor="black")
        self.get_assignment_name.configure(insertbackground="black")
        self.get_assignment_name.configure(selectbackground="blue")
        self.get_assignment_name.configure(selectforeground="white")
        self.get_assignment_name.configure(wrap="word")

        self.teacher = tk.LabelFrame(self.class_detail)
        self.teacher.place(relx=0.03, rely=0.283, relheight=0.425
                , relwidth=0.947)
        self.teacher.configure(relief='groove')
        self.teacher.configure(foreground="black")
        self.teacher.configure(text='''Description''')
        self.teacher.configure(background="#ffffff")
        self.teacher.configure(highlightbackground="#ffffff")
        self.teacher.configure(highlightcolor="black")

        self.get_description = tk.Text(self.teacher)
        self.get_description.place(relx=0.031, rely=0.19, relheight=0.714
                , relwidth=0.938, bordermode='ignore')
        self.get_description.configure(background="white")
        self.get_description.configure(font="TkTextFont")
        self.get_description.configure(foreground="black")
        self.get_description.configure(highlightbackground="#ffffff")
        self.get_description.configure(highlightcolor="black")
        self.get_description.configure(insertbackground="black")
        self.get_description.configure(selectbackground="blue")
        self.get_description.configure(selectforeground="white")
        self.get_description.configure(wrap="word")

        self.deadline = tk.LabelFrame(self.class_detail)
        self.deadline.place(relx=0.03, rely=0.709, relheight=0.243
                , relwidth=0.296)
        self.deadline.configure(relief='groove')
        self.deadline.configure(foreground="black")
        self.deadline.configure(text='''Deadline''')
        self.deadline.configure(background="#ffffff")
        self.deadline.configure(highlightbackground="#ffffff")
        self.deadline.configure(highlightcolor="black")

        self.get_deadline = tk.Text(self.deadline)
        self.get_deadline.place(relx=0.1, rely=0.333, relheight=0.5, relwidth=0.8
                , bordermode='ignore')
        self.get_deadline.configure(background="white")
        self.get_deadline.configure(font="TkTextFont")
        self.get_deadline.configure(foreground="black")
        self.get_deadline.configure(highlightbackground="#ffffff")
        self.get_deadline.configure(highlightcolor="black")
        self.get_deadline.configure(insertbackground="black")
        self.get_deadline.configure(selectbackground="blue")
        self.get_deadline.configure(selectforeground="white")
        self.get_deadline.configure(wrap="word")

        self.status = tk.LabelFrame(self.class_detail)
        self.status.place(relx=0.355, rely=0.709, relheight=0.243
                , relwidth=0.296)
        self.status.configure(relief='groove')
        self.status.configure(foreground="black")
        self.status.configure(text='''Status''')
        self.status.configure(background="#ffffff")
        self.status.configure(highlightbackground="#ffffff")
        self.status.configure(highlightcolor="black")

        self.get_status = tk.Text(self.status)
        self.get_status.place(relx=0.1, rely=0.333, relheight=0.5, relwidth=0.8
                , bordermode='ignore')
        self.get_status.configure(background="white")
        self.get_status.configure(font="TkTextFont")
        self.get_status.configure(foreground="black")
        self.get_status.configure(highlightbackground="#ffffff")
        self.get_status.configure(highlightcolor="black")
        self.get_status.configure(insertbackground="black")
        self.get_status.configure(selectbackground="blue")
        self.get_status.configure(selectforeground="white")
        self.get_status.configure(wrap="word")

        self.score = tk.LabelFrame(self.class_detail)
        self.score.place(relx=0.68, rely=0.709, relheight=0.243, relwidth=0.296)
        self.score.configure(relief='groove')
        self.score.configure(foreground="black")
        self.score.configure(text='''Score''')
        self.score.configure(background="#ffffff")

        self.Text2 = tk.Text(self.score)
        self.Text2.place(relx=0.1, rely=0.333, relheight=0.5, relwidth=0.8
                , bordermode='ignore')
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#ffffff")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        self.Text2.configure(wrap="word")

        self.submission_butt = tk.Button(self.main_assignments)
        self.submission_butt.place(relx=0.5, rely=0.881, height=30, width=80
                , bordermode='ignore')
        self.submission_butt.configure(activebackground="#05bff5")
        self.submission_butt.configure(activeforeground="white")
        self.submission_butt.configure(background="#ffffff")
        self.submission_butt.configure(disabledforeground="#bfbfbf")
        self.submission_butt.configure(font="-family {Arcon Rounded-} -size 9 -weight bold")
        self.submission_butt.configure(foreground="#05bff5")
        self.submission_butt.configure(highlightbackground="#ffffff")
        self.submission_butt.configure(highlightcolor="black")
        self.submission_butt.configure(pady="0")
        self.submission_butt.configure(text='''submission''')

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





