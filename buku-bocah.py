"""
WORKS IN PYTHON 3.x ONLY,
AND PROBABLY UNIX (WSL2-UBUNTU).
"""
#"""MODULES"""
import tkinter as tk
from tkinter import ttk

from os import name as os_name
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

import tkinter.font as tkFont
from ttkthemes import ThemedStyle

#"""PROGRAM"""
from src import main

#"""GLOBAL VARIABLES"""
title   = 'eZTugas'
user    = None
user_role = 0
link_file = ''
list_assess = []
stud_list_class = []
tchr_list_class = []
tchr_list_assess = []
tchr_list_stud = []
tchr_list_full = []
tchr_class_name = ''
tchr_assess_name = ''
tchr_name_class = ''
var_name = None
var_asg = None
#"""GLOBAL WIDGETS"""
home_first = None
home_second = None
home_third = None
home_fourth = None
profile_first = None
profile_second = None
profile_third = None
profile_fourth = None
profile_fifth = None
profile_sixth = None
profile_seventh = None
addcls_first = None
addcls_second = None
studclass_first = None
studassign_first = None
submitassess_first = None
submitassess_second = None
tchrclass_first = None
tchrassign_first = None
tchrassign_second = None
prntasg_first = None
prntasg_second = None
prntasg_third = None
prntasg_fourth = None
prntasg_fifth = None
seeassess_first = None
seeassess_second = None
givealert_first = None


#"""USER LOGIN'S FUNCTION"""
def change_widgets(controller, user, role):
    global user_role
    user_role = role.get()

    global home_first, home_second, home_third, home_fourth
    home_fourth.configure(text='Hello, '+user.USER.getName()+'!')
    if user_role == 1:
        user_role = 'Student'
        # Get Alert
        list_alert = user.getAlert()
        for i in range(len(list_alert)):
            messagebox.showinfo(
                    'Alert from your lovely Parent!',
                    list_alert[i]['pesan']
                )
        # HomePage
        home_first.configure(
                text='My Classes',
                command=lambda: controller.show_frame('StudentClassPage')
            )
        home_second.configure(
                text='My Assignments',
                command=lambda: controller.show_frame('StudentAssignPage')
            )
        home_third.configure(
                text='Add Class',
                command=lambda: controller.show_frame('AddClassPage')
            )
        # ProfilePage
        profile_sixth.configure(command=lambda: controller.show_frame('StudentClassPage'))
        profile_seventh.configure(command=lambda: controller.show_frame('StudentAssignPage'))
        # StudentClassPage
        for i in studclass_first.get_children():
            studclass_first.delete(i)
        global stud_list_class
        stud_list_class = user.getKELAS()
        for i in range(len(stud_list_class)):
            studclass_first.insert('', tk.END, iid=i, text=stud_list_class[i]['name'])
        # AddClassPage
        addcls_first.configure(command=lambda: controller.show_frame('StudentClassPage'))
        addcls_second.configure(command=lambda: controller.show_frame('StudentAssignPage'))
        # StudentAssignPage
        for i in studassign_first.get_children():
            studassign_first.delete(i)
        global list_assess
        list_assess = user.getTUGAS()
        for i in range(len(list_assess)):
            studassign_first.insert('', tk.END, iid=i, text=list_assess[i]['nama'])

    elif user_role == 2:
        user_role = 'Teacher'
        # HomePage
        home_first.configure(
                text='My Classes',
                command=lambda: controller.show_frame('TeacherClassPage')
            )
        home_second.configure(
                text='Assignments List',
                command=lambda: controller.show_frame('TeacherAssignPage')
            )
        home_third.configure(
                text='Create Class',
                command=lambda: controller.show_frame('AddClassPage')
            )
        # ProfilePage
        profile_sixth.configure(command=lambda: controller.show_frame('TeacherClassPage'))
        profile_seventh.configure(command=lambda: controller.show_frame('TeacherAssignPage'))
        # TeacherClassPage
        for i in tchrclass_first.get_children():
            tchrclass_first.delete(i)
        global tchr_list_class
        tchr_list_class = user.getKelas()
        for i in range(len(tchr_list_class)):
            tchrclass_first.insert('', tk.END, iid=i, text=tchr_list_class[i]['namakelas'])
        # AddClassPage
        addcls_first.configure(command=lambda: controller.show_frame('TeacherClassPage'))
        addcls_second.configure(command=lambda: controller.show_frame('TeacherAssignPage'))
        # TeacherAssignPage
        # SeeAssessPage
        for i in tchrassign_first.get_children():
            tchrassign_first.delete(i)
        for i in seeassess_second.get_children():
            seeassess_second.delete(i)
        global tchr_list_assess
        for i in range(len(tchr_list_class)):
            tchr_list_assess.append(tchr_list_class[i]['listtugas'])
            for j in range(len(tchr_list_assess[i])):
                tchrassign_first.insert('', tk.END, iid=(i,j), text=tchr_list_assess[i][j][0]['nama'])

    elif user_role == 3:
        user_role = 'Parent'
        # Get Alert
        list_alert = user.getDeadlineAlert()
        for i in range(len(list_alert)):
            messagebox.showinfo(
                    'Your child has assignment due!',
                    'Your child ' + list_alert[i] + ' has assignment due!\nAlert him.'
                )
        # HomePage
        home_first.configure(
                text='My Children',
                command=lambda: controller.show_frame('MyChildrenPage')
            )
        home_second.configure(
                text='My Children\'s Assignments',
                command=lambda: controller.show_frame('MyChildAssignmentPage')
            )
        home_third.configure(
                text='Give Alert',
                command=lambda: controller.show_frame('GiveAlertPage')
            )
        # MyChildrenPage
        prntchild_first.configure(text=user.getAnak())
        # MyChildAssignmentPage
        prntasg_first['values'] = user.getAnak().split('\n')

    # ProfilePage
    global profile_first, profile_second, profile_third, profile_fourth, profile_fifth
    profile_first.configure(text=user.USER.getName())
    profile_second.configure(text=user.USER.getUname())
    profile_third.configure(text=user.USER.getEmail())
    profile_fourth.configure(text=user.USER.getNoTelp())
    profile_fifth.configure(text=user.USER.getAddress())


#"""FUNCTIONS"""
def select_file():
    """Open a file for editing."""
    filepath = askopenfilename(
            filetypes=[
                ('PDF Files', '*.pdf'),
                ('TXT Files', '*.txt'),
                ('All Files', '*.*')
            ]
    )
    if not filepath:
        return
    submitassess_second.configure(text=filepath)
    global link_file
    link_file = filepath

def open_file():
    pass

def add_score(name_class, name_score):
    global tchr_name_class
    done = user.nilaiTugas(tchr_name_class, name_score, name_class)

    if type(done) is str:
        if done == 'kelas':
            messagebox.showerror(
                    'Name Class Not Found.',
                    'The class you have entered not found.\nPlease try again.'
                )

def submit_assess(name, link):
    done = user.kumpulTugas(name, link)

    if not done:
        messagebox.showerror(
                'Assessment Has Been Closed',
                'You have submitted the assignments passed the deadline.'
            )
    else:
        messagebox.showinfo(
                'Assessment Has Been Submitted',
                '.'
            )

def add_assign(name_class, name_assess, desc_assess, dl):
    done = user.giveTugas(name_class, name_assess, desc_assess, dl)

def add_class(name_class, have_enroll, enroll):
    if have_enroll.get() == 0:
        enroll.delete(0, tk.END)

    if user_role == 'Student':
        done = user.sign_class(name_class.get(), enroll.get())
        if not done:
            messagebox.showerror(
                    'Class Not Found',
                    'The class you have entered not found.\nPlease try again.'
                )
    elif user_role == 'Teacher':
        user.makeKelas(name_class.get(), have_enroll.get(), enroll.get())

    name_class.delete(0, tk.END)
    have_enroll.set(0)
    enroll.delete(0, tk.END)

def see_assess(name_class, name_assess, controller):
    global tchr_list_full, tchr_name_class
    tchr_name_class = name_class
    tchr_list_full = user.cekhasilpekerjaan(name_assess, name_class)

    for i in seeassess_second.get_children():
        seeassess_second.delete(i)
    for i in range(len(tchr_list_full)):
        seeassess_second.insert('', tk.END, iid=i, text=tchr_list_full[i]['namamurid'])

    controller.show_frame('SeeAssessPage')

def send_alert(name, msg):
    user.giveAlert(name, msg)

def add_child(name):
    user.setAnak(name)

def select_child(event):
    global list_assess, prntasg_first
    list_assess = user.getTugasAnak(prntasg_first.get())
    list_name = []
    for i in range(len(list_assess)):
        list_name.append(list_assess[i]['nama'])
    prntasg_second['values'] = list_name
    prntasg_third.configure(text='')
    prntasg_fourth.configure(text='')
    prntasg_fifth.configure(text='')

def select_assess(event):
    global list_assess, prntasg_second, givealert_first
    for i in range(len(list_assess)):
        if list_assess[i]['nama'] == prntasg_second.get():
            prntasg_third.configure(text=list_assess[i]['deskripsi'])
            prntasg_fourth.configure(text=list_assess[i]['deadline'])
            prntasg_fifth.configure(text=list_assess[i]['submission'])
            givealert_first.insert(tk.END, list_assess[i]['nama'])
            break

def user_login(controller, role, name, pw):
    """USER LOGIN"""
    if role.get() == 0:
        return
    result = main.login(role.get(), name.get(), pw.get())

    if type(result) == str:
        if result == 'pw':
            messagebox.showerror(
                    'Incorrect Password',
                    'The password you entered is incorrect.\nPlease try again.'
                )
            pw.delete(0, tk.END)
        else:
            messagebox.showerror(
                    'Log In Error',
                    'Couldn\'t find your Account.\nPlease try again'
                )
        return

    global user
    user = result
    change_widgets(controller, user, role)

    role.set(0)
    name.delete(0, tk.END)
    pw.delete(0, tk.END)

    controller.show_frame('HomePage')

def user_regist(controller, role, name, uname, pw, phone, addr, mail):
    """USER REGIST"""
    if role.get() == 0:
        return
    result = main.regist(
            role.get(),
            name.get(),
            uname.get(),
            pw.get(),
            phone.get(),
            addr.get(),
            mail.get(),
        )

    if result:
        if result == 'email':
            messagebox.showerror(
                    'Invalid Email',
                    'An email address must contain a single @.'
                )
        else:
            messagebox.showerror(
                    'Account Exists',
                    'Another user with this email already exist.\nTry another email perhaps.'
                )
        return

    role.set(0)
    name.delete(0, tk.END)
    uname.delete(0, tk.END)
    pw.delete(0, tk.END)
    phone.delete(0, tk.END)
    addr.delete(0, tk.END)
    mail.delete(0, tk.END)

    controller.show_frame('LoginPage')

def user_forgot(controller, role, uname, mail, newpw, renewpw):
    """USER FORGOT PASSWORD"""
    if newpw.get() != renewpw.get():
        messagebox.showerror(
                'Does Not Match',
                'The password didn\'t match.\nPlease try again.'
            )
        renewpw.delete(0, tk.END)
        return

    if role.get() == 0:
        return
    result = main.forgot(role.get(), uname.get(), mail.get(), newpw.get())

    if result:
        messagebox.showerror(
                'Log In Error',
                'Couldn\'t find your Account.\nPlease try again'
            )
        newpw.delete(0, tk.END)
        renewpw.delete(0, tk.END)
        return

    role.set(0)
    uname.delete(0, tk.END)
    mail.delete(0, tk.END)
    newpw.delete(0, tk.END)
    renewpw.delete(0, tk.END)

    controller.show_frame('LoginPage')


#"""MAIN APP"""
class BukuBocil(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Build window.
        tk.Tk.__init__(self, *args, **kwargs)
        # Set title.
        self.title('  ' + title)
        self.option_add('*Dialog.msg.font', 'Arial 10')
        # Set icon.
        if 'nt' == os_name:
            self.wm_iconbitmap(bitmap='logo/logo_jadi2an.ico')
        else:
            self.wm_iconbitmap(bitmap='@logo/logo_jadi2an.xbm')
        # App theme.
        # To use this theme for widget, use `ttk` instead of `tk`.
        ThemedStyle(self).set_theme('adapta')
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')
        style.configure('TNotebook', sticky='w', fill=tk.X)

        # Contaioner for stack every frames on top of each other,
        # then the main frame will be raised above the others.
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=False)
        container.grid_rowconfigure(0, weight=1, minsize=600)
        container.grid_columnconfigure(0, weight=1, minsize=800)

        #"""LIST FONT"""
        self.fonts = {
                'h1': tkFont.Font(family='URW Gothic', size=37),
                'h2': tkFont.Font(family='URW Gothic', size=30),
                'h3': tkFont.Font(family='URW Gothic', size=24),
                'h4': tkFont.Font(family='URW Gothic', size=19),
                'h5': tkFont.Font(family='URW Gothic', size=15),
                'h6': tkFont.Font(family='URW Gothic', size=12),
                'p' : tkFont.Font(family='URW Gothic', size=10),
            }

        #"""LIST PAGES"""
        pages = (
                StartPage,         #SAFE
                RegisterPage,      #SAFE
                LoginPage,         #SAFE
                ForgotPage,        #SAFE
                HomePage,          #SAFE
                ProfilePage,       #SAFE

                StudentClassPage,  #SAFE
                TeacherClassPage,  #SAFE
                AddClassPage,      #SAFE

                StudentAssignPage, #SAFE
                AddSubmissionPage, #SAFE

                TeacherAssignPage, #SAFE
                SeeAssessPage,     #SAFE
                AddAssessPage,     #SAFE

                GiveAlertPage,         #SAFE
                MyChildrenPage,        #SAFE
                MyChildAssignmentPage, #SAFE
            )

        # Add all frames to window.
        self.frames = {}
        for page in pages:
            page_name = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[page_name] = frame

            # Put all of the pages in the same location.
            frame.grid(row=0, column=0, sticky='nsew')

        # Show start frame.
        self.show_frame('StartPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


#"""START PAGE"""
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        lbl_welcome = tk.Label(
                self,
                text='Welcome to\n'+title,
                font=controller.fonts['h1'],
                anchor='center',
                justify='center',
                fg='deepskyblue',
                bg='white',
            )
        lbl_description = tk.Label(
                self,
                text='connect with your\nteachers, parents, and students more easily!',
                font=tkFont.Font(
                    family='URW Gothic',
                    size=12,
                    weight='bold',
                    slant='italic',
                ),
                anchor='center',
                bg='deepskyblue',
                fg='white',
                pady=5,
            )
        btn_register = ttk.Button(
                self,
                text='Register',
                command=lambda: controller.show_frame('RegisterPage'),
            )
        btn_login = ttk.Button(
                self,
                text='Login',
                command=lambda: controller.show_frame('LoginPage'),
            )
        lbl_or = tk.Label(
                self,
                text='or',
                justify='center',
                bg='white',
                fg='lightskyblue',
            )

        lbl_welcome.place(y=150, width=800)
        lbl_description.place(y=270, width=800)
        btn_register.place(x=250, y=400)
        lbl_or.place(x=395, y=410)
        btn_login.place(x=450, y=400)


#"""LOGIN PAGE"""
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        btn_navbar = tk.Button(
                self,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                pady=5,
                command=lambda: controller.show_frame('StartPage')
            )
        lbl_title = tk.Label(
                self,
                text='Login to Buku Penghubung',
                font=controller.fonts['h1'],
                justify='center',
                bg='white',
                fg='deepskyblue',
            )
        lbl_role = tk.Label(
                self,
                text='My Role',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        var_role = tk.IntVar()
        rdo_student = ttk.Radiobutton(
                self,
                text='Student',
                variable=var_role,
                value=1,
            )
        rdo_teacher = ttk.Radiobutton(
                self,
                text='Teacher',
                variable=var_role,
                value=2,
            )
        rdo_parent = ttk.Radiobutton(
                self,
                text='Parent',
                variable=var_role,
                value=3,
            )
        lbl_username = tk.Label(
                self,
                text='Username',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_password = tk.Label(
                self,
                text='Password',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        ent_username = ttk.Entry(self, width=45)
        ent_password = ttk.Entry(self, width=45, show='●')
        btn_login = ttk.Button(
                self,
                text='Login',
                command=lambda: user_login(
                        controller,
                        var_role,
                        ent_username,
                        ent_password
                ),
            )
        btn_forgot = tk.Button(
                self,
                text='forgot your password?',
                highlightthickness=0,
                relief=tk.FLAT,
                font=tkFont.Font(size=10, slant='italic'),
                bg='white',
                fg='paleturquoise',
                activebackground='white',
                command=lambda: controller.show_frame('ForgotPage')
            )

        btn_navbar.place(width=800, height=40)
        lbl_title.place(y=150, width=800)

        lbl_role.place(x=0, y=270, width=230)
        rdo_student.place(x=260, y=264)
        rdo_teacher.place(x=403, y=264)
        rdo_parent.place(x=545, y=264)

        lbl_username.place(x=0, y=330, width=230)
        ent_username.place(x=250, y=324)
        lbl_password.place(x=0, y=380, width=230)
        ent_password.place(x=250, y=374)

        btn_login.place(x=350, y=480)
        btn_forgot.place(x=450, y=410)


#"""FORGOT PASSWORD PAGE"""
class ForgotPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        btn_navbar = tk.Button(
                self,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                pady=5,
                command=lambda: controller.show_frame('StartPage')
            )
        lbl_title = tk.Label(
                self,
                text='Create New Password',
                font=controller.fonts['h1'],
                justify='center',
                bg='white',
                fg='deepskyblue',
            )
        lbl_role = tk.Label(
                self,
                text='My Role',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        var_role = tk.IntVar()
        rdo_student = ttk.Radiobutton(
                self,
                text='Student',
                variable=var_role,
                value=1,
            )
        rdo_teacher = ttk.Radiobutton(
                self,
                text='Teacher',
                variable=var_role,
                value=2,
            )
        rdo_parent = ttk.Radiobutton(
                self,
                text='Parent',
                variable=var_role,
                value=3,
            )
        lbl_username = tk.Label(
                self,
                text='Username',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_mail = tk.Label(
                self,
                text='Email',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_newpass = tk.Label(
                self,
                text='New Password',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_renewpass = tk.Label(
                self,
                text='Re-New Password',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        ent_username  = ttk.Entry(self, width=45)
        ent_mail      = ttk.Entry(self, width=45)
        ent_newpass   = ttk.Entry(self, width=45, show='●')
        ent_renewpass = ttk.Entry(self, width=45, show='●')
        btn_forgot = ttk.Button(
                self,
                text='Change Password',
                command=lambda: user_forgot(
                        controller,
                        var_role,
                        ent_username,
                        ent_mail,
                        ent_newpass,
                        ent_renewpass,
                ),
            )
        btn_back = tk.Button(
                self,
                text='Back',
                highlightthickness=0,
                relief=tk.FLAT,
                font=tkFont.Font(size=10, slant='italic'),
                bg='white',
                fg='paleturquoise',
                activebackground='white',
                command=lambda: controller.show_frame('StartPage')
            )

        btn_navbar.place(width=800, height=40)
        lbl_title.place(y=120, width=800)

        lbl_role.place(x=0, y=190, width=230)
        rdo_student.place(x=260, y=184)
        rdo_teacher.place(x=403, y=184)
        rdo_parent.place(x=545, y=184)

        lbl_username.place(x=0, y=250, width=230)
        lbl_mail.place(x=0, y=290, width=230)
        lbl_newpass.place(x=0, y=330, width=230)
        lbl_renewpass.place(x=0, y=370, width=230)

        ent_username.place(x=250, y=244)
        ent_mail.place(x=250, y=284)
        ent_newpass.place(x=250, y=324)
        ent_renewpass.place(x=250, y=364)

        btn_forgot.place(x=353, y=455)
        btn_back.place(x=545, y=405)


#"""REGISTER PAGE"""
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        btn_navbar = tk.Button(
                self,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                pady=5,
                command=lambda: controller.show_frame('StartPage')
            )
        lbl_title = tk.Label(
                self,
                text='Create Account',
                font=controller.fonts['h1'],
                justify='center',
                bg='white',
                fg='deepskyblue',
            )
        lbl_role = tk.Label(
                self,
                text='My Role',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        var_role = tk.IntVar()
        rdo_student = ttk.Radiobutton(
                self,
                text='Student',
                variable=var_role,
                value=1,
            )
        rdo_teacher = ttk.Radiobutton(
                self,
                text='Teacher',
                variable=var_role,
                value=2,
            )
        rdo_parent = ttk.Radiobutton(
                self,
                text='Parent',
                variable=var_role,
                value=3,
            )
        lbl_realname = tk.Label(
                self,
                text='Name',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_username = tk.Label(
                self,
                text='Username',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_password = tk.Label(
                self,
                text='Password',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_phone = tk.Label(
                self,
                text='Phone Number',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_addr = tk.Label(
                self,
                text='Address',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        lbl_mail = tk.Label(
                self,
                text='Email',
                font=controller.fonts['h6'],
                anchor='e',
                bg='white',
            )
        ent_realname = ttk.Entry(self, width=45)
        ent_username = ttk.Entry(self, width=45)
        ent_password = ttk.Entry(self, width=45)
        ent_phone    = ttk.Entry(self, width=45)
        ent_addr     = ttk.Entry(self, width=45)
        ent_mail     = ttk.Entry(self, width=45)
        btn_regist = ttk.Button(
                self,
                text='Register',
                command=lambda: user_regist(
                        controller,
                        var_role,
                        ent_realname,
                        ent_username,
                        ent_password,
                        ent_phone,
                        ent_addr,
                        ent_mail,
                ),
            )
        btn_login = tk.Button(
                self,
                text='Already have an account?',
                highlightthickness=0,
                relief=tk.FLAT,
                font=tkFont.Font(size=10, slant='italic'),
                bg='white',
                fg='paleturquoise',
                activebackground='white',
                command=lambda: controller.show_frame('LoginPage')
            )

        btn_navbar.place(width=800, height=40)
        lbl_title.place(y=100, width=800)

        lbl_role.place(x=0, y=180, width=230)
        rdo_student.place(x=260, y=174)
        rdo_teacher.place(x=403, y=174)
        rdo_parent.place(x=545, y=174)

        lbl_realname.place(x=0, y=230, width=230)
        lbl_username.place(x=0, y=270, width=230)
        lbl_password.place(x=0, y=310, width=230)
        lbl_phone.place(x=0, y=350, width=230)
        lbl_addr.place(x=0, y=390, width=230)
        lbl_mail.place(x=0, y=430, width=230)

        ent_realname.place(x=250, y=224)
        ent_username.place(x=250, y=264)
        ent_password.place(x=250, y=304)
        ent_phone.place(x=250, y=344)
        ent_addr.place(x=250, y=384)
        ent_mail.place(x=250, y=424)

        btn_regist.place(x=353, y=510)
        btn_login.place(x=440, y=460)


#"""HOME PAGE"""
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        lbl_navbar = tk.Label(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        lbl_greeting = tk.Label(
                self,
                font=controller.fonts['h1'],
                anchor='center',
                justify='center',
                fg='gray64',
                bg='white',
            )
        global home_fourth
        home_fourth = lbl_greeting
        btn_profile = ttk.Button(
                self,
                text='My Profile',
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = ttk.Button(
                self,
            )
        global home_first
        home_first = btn_classes
        btn_assessments = ttk.Button(
                self,
            )
        global home_second
        home_second = btn_assessments
        btn_addClass = ttk.Button(
                self,
            )
        global home_third
        home_third = btn_addClass
        btn_faq = ttk.Button(
                self,
                text='FAQ',
                #command=lambda: controller.show_frame('StartPage')
            )
        btn_help = ttk.Button(
                self,
                text='Help',
                #command=lambda: controller.show_frame('StartPage')
            )
        lbl_quote = tk.Label(
                self,
                text='indeed with hardship will be ease',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                fg='dodgerblue',
            )

        btn_logout.place(x=700, width=100, height=40)
        lbl_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_greeting.place(x=30, y=100)
        btn_profile.place(x=20, y=210, width=240, height=150)      #x=80, y=300, width=160)
        btn_classes.place(x=280, y=210, width=240, height=150)      #x=320, y=300, width=160)
        btn_assessments.place(x=540, y=210, width=240, height=150)  #x=560, y=300, width=160)
        btn_addClass.place(x=20, y=380, width=240, height=150)     #x=80, y=380, width=160)
        btn_faq.place(x=280, y=380, width=240, height=150)          #x=320, y=380, width=160)
        btn_help.place(x=540, y=380, width=240, height=150)         #x=560, y=380, width=160)
        lbl_quote.place(y=560, width=800, height=40)


#"""PROFILE PAGE"""
class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                activebackground='white',
                fg='deepskyblue',
                activeforeground='deepskyblue',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        global profile_sixth
        profile_sixth = btn_classes
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        global profile_seventh
        profile_seventh = btn_assign
        lbl_title = tk.Label(
                self,
                text='My Profile',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )
        frmlbl_name = tk.LabelFrame(
                self,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=3,
            )
        ent_name = tk.Label(
                frmlbl_name,
                bg='white',
            )
        frmlbl_uname = tk.LabelFrame(
                self,
                text='Username',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        lbl_uname = tk.Label(
                frmlbl_uname,
                bg='white',
            )
        frmlbl_mail = tk.LabelFrame(
                self,
                text='Email',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        lbl_mail = tk.Label(
                frmlbl_mail,
                bg='white',
            )
        frmlbl_phone = tk.LabelFrame(
                self,
                text='Phone Number',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        ent_phone = tk.Label(
                frmlbl_phone,
                bg='white',
            )
        frmlbl_addr = tk.LabelFrame(
                self,
                text='Address',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        txt_addr = tk.Label(
                frmlbl_addr,
                bg='white',
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )

        global profile_first, profile_second, profile_third, profile_fourth, profile_fifth
        profile_first = ent_name
        profile_second = lbl_uname
        profile_third = lbl_mail
        profile_fourth = ent_phone
        profile_fifth = txt_addr

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=75, width=800)

        ent_name.place(x=15, y=3, width=470)
        frmlbl_name.place(x=150, y=150, width=500, height=60)
        lbl_uname.place(x=15, y=3, width=470)
        frmlbl_uname.place(x=150, y=220, width=500, height=60)
        lbl_mail.place(x=15, y=3, width=470)
        frmlbl_mail.place(x=150, y=290, width=500, height=60)
        ent_phone.place(x=15, y=3, width=470)
        frmlbl_phone.place(x=150, y=360, width=500, height=60)
        txt_addr.place(x=15, y=3, width=470, height=60)
        frmlbl_addr.place(x=150, y=430, width=500, height=90)

        btn_back.place(x=350, y=542, width=100)


#"""CLASS PAGE"""
class StudentClassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                activebackground='white',
                fg='deepskyblue',
                activeforeground='deepskyblue',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StudentAssignPage')
            )
        lbl_title = tk.Label(
                self,
                text='My Classes',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        # List Classes
        frm_list = tk.LabelFrame(
                self,
                text='List Classes',
                font=controller.fonts['h5'],
                bg='white',
                bd=3,
            )
        self.tree = ttk.Treeview(
                frm_list,
                selectmode='browse',
                show='tree',
            )
        global studclass_first
        studclass_first = self.tree
        self.tree.bind("<Double-1>", self.choose_class)
        scroll = ttk.Scrollbar(
                frm_list,
                orient=tk.VERTICAL,
                command=self.tree.yview,
            )

        self.frmlbl_cls = tk.LabelFrame(
                self,
                bg='white',
                bd=3,
            )
        frmlbl_name = tk.LabelFrame(
                self.frmlbl_cls,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_name = tk.Label(
                frmlbl_name,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_tchr = tk.LabelFrame(
                self.frmlbl_cls,
                text='Teacher',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_tchr = tk.Label(
                frmlbl_tchr,
                font=controller.fonts['p'],
                bg='white',
            )
        self.frmlbl_mbrs = tk.LabelFrame(
                self.frmlbl_cls,
                text='Total Members',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_mbrs = tk.Label(
                self.frmlbl_mbrs,
                font=controller.fonts['p'],
                bg='white',
            )
        self.frmlbl_assg = tk.LabelFrame(
                self.frmlbl_cls,
                text='Total Assignments',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_assg = tk.Label(
                self.frmlbl_assg,
                font=controller.fonts['p'],
                bg='white',
            )
        btn_add = ttk.Button(
                self,
                text='Sign New Class',
                command=lambda: controller.show_frame('AddClassPage')
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        self.tree.place(width=200, height=270)
        frm_list.place(x=30, y=180, width=240, height=300)
        scroll.place(x=210, height=270)

        self.lbl_name.place(x=15, width=390)
        frmlbl_name.place(x=15, y=10, width=420, height=45)
        self.lbl_tchr.place(x=15, width=390)
        frmlbl_tchr.place(x=15, y=65, width=420, height=45)

        self.lbl_mbrs.place(x=15, width=390)
        self.frmlbl_mbrs.place(x=15, y=120, width=420, height=45)
        self.lbl_assg.place(x=15, width=390)
        self.frmlbl_assg.place(x=15, y=175, width=420, height=45)
        self.frmlbl_cls.place(x=300, y=200, width=450, height=240)

        btn_back.place(x=290, y=528, width=100)
        btn_add.place(x=410, y=528, width=150)

    def choose_class(self, event):
        index = int(self.tree.selection()[0])

        global stud_list_class
        self.lbl_name.configure(text=stud_list_class[index]['name'])
        self.lbl_tchr.configure(text=stud_list_class[index]['teacher'])
        self.lbl_mbrs.configure(text=stud_list_class[index]['totalmember'])
        self.lbl_assg.configure(text=stud_list_class[index]['totalassignments'])


class TeacherClassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                activebackground='white',
                fg='deepskyblue',
                activeforeground='deepskyblue',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherAssignPage')
            )
        lbl_title = tk.Label(
                self,
                text='List Classes',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        # List Classes
        frm_list = tk.LabelFrame(
                self,
                text='List Classes',
                font=controller.fonts['h5'],
                bg='white',
                bd=3,
            )
        self.tree = ttk.Treeview(
                frm_list,
                selectmode='browse',
                show='tree',
            )
        global tchrclass_first
        tchrclass_first = self.tree
        self.tree.bind("<Double-1>", self.choose_class)
        scroll = ttk.Scrollbar(
                frm_list,
                orient=tk.VERTICAL,
                command=self.tree.yview,
            )

        self.frmlbl_cls = tk.LabelFrame(
                self,
                bg='white',
                bd=3,
            )
        frmlbl_name = tk.LabelFrame(
                self.frmlbl_cls,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_name = tk.Label(
                frmlbl_name,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_tchr = tk.LabelFrame(
                self.frmlbl_cls,
                text='Teacher',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_tchr = tk.Label(
                frmlbl_tchr,
                font=controller.fonts['p'],
                bg='white',
            )
        self.frmlbl_mbrs = tk.LabelFrame(
                self.frmlbl_cls,
                text='List Members',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_mbrs = tk.Label(
                self.frmlbl_mbrs,
                font=controller.fonts['p'],
                bg='white',
            )
        self.frmlbl_assg = tk.LabelFrame(
                self.frmlbl_cls,
                text='Total Assignments',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_assg = tk.Label(
                self.frmlbl_assg,
                font=controller.fonts['p'],
                bg='white',
            )
        btn_add = ttk.Button(
                self,
                text='Add New Class',
                command=lambda: controller.show_frame('AddClassPage')
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )
        btn_assign = ttk.Button(
                self,
                text='Add New Assignment',
                command=lambda: controller.show_frame('AddAssessPage')
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        self.tree.place(width=200, height=270)
        frm_list.place(x=30, y=180, width=240, height=300)
        scroll.place(x=210, height=270)

        self.lbl_name.place(x=15, width=390)
        frmlbl_name.place(x=15, y=10, width=420, height=45)
        self.lbl_tchr.place(x=15, width=390)
        frmlbl_tchr.place(x=15, y=65, width=420, height=45)

        self.lbl_mbrs.place(x=15, width=390)
        self.frmlbl_mbrs.place(x=15, y=120, width=420, height=140)
        self.lbl_assg.place(x=15, width=390)
        self.frmlbl_assg.place(x=15, y=270, width=420, height=45)
        self.frmlbl_cls.place(x=300, y=150, width=450, height=340)

        btn_assign.place(x=180, y=528, width=170)
        btn_back.place(x=360, y=528, width=100)
        btn_add.place(x=470, y=528, width=150)

    def choose_class(self, event):
        index = int(self.tree.selection()[0])

        global tchr_list_class, tchr_class_name
        tchr_class_name = tchr_list_class[index]['namakelas']
        self.lbl_name.configure(text=tchr_class_name)
        self.lbl_tchr.configure(text='Ibu '+user.getName())
        students = ''
        for i in range(len(tchr_list_class[index]['listmurid'])):
            students += (tchr_list_class[index]['listmurid'][i][0]['nama'] + '\n')
        self.lbl_mbrs.configure(text=students)
        self.lbl_assg.configure(text=str(len(tchr_list_class[index]['listtugas'])))


#"""ADD CLASS PAGE"""
class AddClassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        global addcls_first
        addcls_first = btn_classes
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        global addcls_second
        addcls_second = btn_assign
        lbl_title = tk.Label(
                self,
                text='Add New Class',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        frmlbl_cls = tk.LabelFrame(
                self,
                bg='white',
                text='Class Name',
                font=controller.fonts['h6'],
            )
        ent_class = ttk.Entry(
                frmlbl_cls,
            )
        frmlbl_enr = tk.LabelFrame(
                self,
                bg='white',
                text='Enrollment Key',
                font=controller.fonts['h6'],
            )
        var_enroll = tk.IntVar()
        rdo_yesenroll = ttk.Radiobutton(
                frmlbl_enr,
                text='Yes',
                variable=var_enroll,
                value=1,
            )
        rdo_noenroll = ttk.Radiobutton(
                frmlbl_enr,
                text='No',
                variable=var_enroll,
                value=0,
            )
        ent_enroll = ttk.Entry(
                frmlbl_enr,
            )
        btn_add = ttk.Button(
                self,
                text='Add',
                command=lambda: add_class(
                                    ent_class,
                                    var_enroll,
                                    ent_enroll
                    )
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=150, width=800)

        ent_class.place(x=15, y=10, width=400)
        frmlbl_cls.place(x=185, y=240, width=430, height=70)
        rdo_yesenroll.place(x=25)
        rdo_noenroll.place(x=90)
        ent_enroll.place(x=15, y=40, width=400)
        frmlbl_enr.place(x=185, y=330, width=430, height=110)

        btn_add.place(x=350, y=480, width=100)


#"""ASSIGNMENT PAGE"""
class StudentAssignPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StudentClassPage')
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                activebackground='white',
                fg='deepskyblue',
                activeforeground='deepskyblue',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        lbl_title = tk.Label(
                self,
                text='My Assignments',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        # List Assessment
        frm_list = tk.LabelFrame(
                self,
                text='List Assessment',
                font=controller.fonts['h5'],
                bg='white',
                bd=3,
            )
        self.tree = ttk.Treeview(
                frm_list,
                selectmode='browse',
                show='tree',
            )
        global studassign_first
        studassign_first = self.tree
        self.tree.bind("<Double-1>", self.choose_assessment)
        scroll = ttk.Scrollbar(
                frm_list,
                orient=tk.VERTICAL,
                command=self.tree.yview,
            )

        frmlbl_assg = tk.LabelFrame(
                self,
                bg='white',
                bd=3,
            )
        frmlbl_name = tk.LabelFrame(
                frmlbl_assg,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_name = tk.Label(
                frmlbl_name,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_desc = tk.LabelFrame(
                frmlbl_assg,
                text='Description',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_desc = tk.Label(
                frmlbl_desc,
                font=controller.fonts['p'],
                anchor='w',
                justify='left',
                bg='white',
            )
        frmlbl_dl = tk.LabelFrame(
                frmlbl_assg,
                text='Deadline',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_dl = tk.Label(
                frmlbl_dl,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_stat = tk.LabelFrame(
                frmlbl_assg,
                text='Status',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_stat = tk.Label(
                frmlbl_stat,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_score = tk.LabelFrame(
                frmlbl_assg,
                text='Score',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_score = tk.Label(
                frmlbl_score,
                font=controller.fonts['p'],
                bg='white',
            )
        self.prg_score = ttk.Progressbar(
                frmlbl_assg,
                maximum=100,
                value=0,
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )
        btn_submit = ttk.Button(
                self,
                text='Submission',
                command=lambda: controller.show_frame('AddSubmissionPage')
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=75, width=800)

        self.tree.place(width=200, height=270)
        frm_list.place(x=30, y=180, width=240, height=300)
        scroll.place(x=210, height=270)

        self.lbl_name.place(x=15, width=390)
        frmlbl_name.place(x=15, y=10, width=420, height=45)
        self.lbl_desc.place(x=15, y=5, width=390)
        frmlbl_desc.place(x=15, y=65, width=420, height=200)

        self.lbl_dl.place(x=15, width=130)
        frmlbl_dl.place(x=15, y=275, width=160, height=45)
        self.lbl_stat.place(x=15, width=115)
        frmlbl_stat.place(x=190, y=275, width=145, height=45)
        self.lbl_score.place(x=15, width=40)
        frmlbl_score.place(x=350, y=275, width=70, height=45)
        self.prg_score.place(x=15, y=335, width=420)

        frmlbl_assg.place(x=300, y=140, width=450, height=360)

        btn_back.place(x=285, y=528, width=100)
        btn_submit.place(x=415, y=528, width=100)

    def choose_assessment(self, event):
        index = int(self.tree.selection()[0])

        global list_assess, name_asses_submit
        name_asses_submit = str(list_assess[index]['nama'])
        self.lbl_name.configure(text=name_asses_submit)
        self.lbl_desc.configure(text=str(list_assess[index]['deskripsi']))
        self.lbl_dl.configure(text=str(list_assess[index]['deadline']))
        self.lbl_stat.configure(text=str(list_assess[index]['submission']))

        score = user.getNilai(list_assess[index]['nama'])
        self.lbl_score.configure(text=score)
        self.prg_score.configure(value=int(score))


class TeacherAssignPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherClassPage')
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='white',
                activebackground='white',
                fg='deepskyblue',
                activeforeground='deepskyblue',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        lbl_title = tk.Label(
                self,
                text='My Assignments',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        # List Assessment
        frm_list = tk.LabelFrame(
                self,
                text='List Assessment',
                font=controller.fonts['h5'],
                bg='white',
                bd=3,
            )
        self.tree = ttk.Treeview(
                frm_list,
                selectmode='browse',
                show='tree',
            )
        global tchrassign_first
        tchrassign_first = self.tree
        self.tree.bind("<Double-1>", self.choose_assessment)
        scroll = ttk.Scrollbar(
                frm_list,
                orient=tk.VERTICAL,
                command=self.tree.yview,
            )

        frmlbl_assg = tk.LabelFrame(
                self,
                bg='white',
                bd=3,
            )
        frmlbl_name = tk.LabelFrame(
                frmlbl_assg,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_name = tk.Label(
                frmlbl_name,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_desc = tk.LabelFrame(
                frmlbl_assg,
                text='Description',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_desc = tk.Label(
                frmlbl_desc,
                font=controller.fonts['p'],
                anchor='w',
                justify='left',
                bg='white',
            )
        frmlbl_dl = tk.LabelFrame(
                frmlbl_assg,
                text='Deadline',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_dl = tk.Label(
                frmlbl_dl,
                font=controller.fonts['p'],
                bg='white',
            )
        frmlbl_stat = tk.LabelFrame(
                frmlbl_assg,
                text='Nama Kelas',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_stat = tk.Label(
                frmlbl_stat,
                font=controller.fonts['p'],
                bg='white',
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )
        btn_submit = ttk.Button(
                self,
                text='See Assignments',
                command=lambda: see_assess(
                        tchr_class_name,
                        tchr_assess_name,
                        controller
                    )
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=75, width=800)

        self.tree.place(width=200, height=270)
        frm_list.place(x=30, y=180, width=240, height=300)
        scroll.place(x=210, height=270)

        self.lbl_name.place(x=15, width=390)
        frmlbl_name.place(x=15, y=10, width=420, height=45)
        self.lbl_desc.place(x=15, y=5, width=390)
        frmlbl_desc.place(x=15, y=65, width=420, height=200)

        self.lbl_dl.place(x=15, y=15, width=172)
        frmlbl_dl.place(x=15, y=275, width=202, height=70)
        self.lbl_stat.place(x=15, y=15, width=172)
        frmlbl_stat.place(x=233, y=275, width=202, height=70)

        frmlbl_assg.place(x=300, y=140, width=450, height=360)

        btn_back.place(x=285, y=528, width=100)
        btn_submit.place(x=415, y=528, width=150)

    def choose_assessment(self, event):
        i, j = self.tree.selection()[0].split(' ')
        i, j = int(i), int(j)

        global tchr_list_assess, tchr_class_name, tchr_assess_name
        tchr_assess_name = tchr_list_assess[i][j][0]['nama']
        tchr_class_name = tchr_list_class[i]['namakelas']
        self.lbl_name.configure(text=tchr_assess_name)
        self.lbl_desc.configure(text=tchr_list_assess[i][j][0]['deskripsi'])
        self.lbl_dl.configure(text=tchr_list_assess[i][j][0]['deadline'])
        self.lbl_stat.configure(text=tchr_class_name)


#"""ADD ASSESSMENT PAGE"""
class AddSubmissionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StudentClassPage')
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StudentAssignPage')
            )
        lbl_title = tk.Label(
                self,
                text='Add Submission',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        frmlbl_asg = tk.LabelFrame(
                self,
                bg='white',
                text='Assignment Name',
                font=controller.fonts['h6'],
            )
        ent_assign = ttk.Entry(
                frmlbl_asg,
            )
        global submitassess_first
        submitassess_first = ent_assign
        frmlbl_sub = tk.LabelFrame(
                self,
                bg='white',
                text='Submission File',
                font=controller.fonts['h6'],
            )
        lbl_submit = tk.Label(
                frmlbl_sub,
            )
        global submitassess_second
        submitassess_second = lbl_submit
        btn_add = ttk.Button(
                frmlbl_sub,
                text='Add File',
                command=select_file
            )
        btn_submit = ttk.Button(
                self,
                text='Submit',
                command=lambda: submit_assess(ent_assign.get(), link_file)
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=150, width=800)

        ent_assign.place(x=15, y=10, width=400)
        frmlbl_asg.place(x=185, y=240, width=430, height=70)
        lbl_submit.place(x=15, y=15, width=400, height=50)
        btn_add.place(x=315, y=75, width=100, height=50)
        frmlbl_sub.place(x=185, y=330, width=430, height=150)

        btn_submit.place(x=350, y=520, width=100)



#"""SEE ASSESSMENT PAGE"""
class SeeAssessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherClassPage')
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherAssignPage')
            )
        lbl_title = tk.Label(
                self,
                text='See Assignment',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        # List Members
        frm_list = tk.LabelFrame(
                self,
                text='List Members',
                font=controller.fonts['h5'],
                bg='white',
                bd=3,
            )
        self.tree = ttk.Treeview(
                frm_list,
                selectmode='browse',
                show='tree',
            )
        global seeassess_second
        seeassess_second = self.tree
        self.tree.bind("<Double-1>", self.choose_class)
        scroll = ttk.Scrollbar(
                frm_list,
                orient=tk.VERTICAL,
                command=self.tree.yview,
            )

        frmlbl_asg = tk.LabelFrame(
                self,
                bg='white',
                bd=3,
            )
        frmlbl_name = tk.LabelFrame(
                frmlbl_asg,
                text='Name',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.ent_name = ttk.Entry(
                frmlbl_name,
            )
        frmlbl_file = tk.LabelFrame(
                frmlbl_asg,
                text='Submission File',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.lbl_file = tk.Label(
                frmlbl_file,
                font=controller.fonts['p'],
                bg='white',
            )
        global seeassess_first
        seeassess_first = self.lbl_file
        btn_file = ttk.Button(
                frmlbl_file,
                text='Open File',
                command=open_file
            )
        frmlbl_scr = tk.LabelFrame(
                frmlbl_asg,
                text='Score',
                font=controller.fonts['h6'],
                bg='white',
                bd=2,
            )
        self.ent_score = ttk.Entry(
                frmlbl_scr,
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('TeacherAssignPage')
            )
        btn_save = ttk.Button(
                self,
                text='Save',
                command=lambda: add_score(
                    self.ent_name.get(),
                    self.ent_score.get()
                )
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        self.tree.place(width=200, height=270)
        frm_list.place(x=30, y=180, width=240, height=300)
        scroll.place(x=210, height=270)

        self.ent_name.place(x=15, width=390)
        frmlbl_name.place(x=15, y=10, width=420, height=60)
        self.lbl_file.place(x=15, width=390)
        btn_file.place(x=300, y=30, width=100, height=50)
        frmlbl_file.place(x=15, y=70, width=420, height=110)
        self.ent_score.place(x=15, width=390)
        frmlbl_scr.place(x=15, y=190, width=420, height=60)

        frmlbl_asg.place(x=300, y=200, width=450, height=270)

        btn_back.place(x=290, y=528, width=100)
        btn_save.place(x=410, y=528, width=100)

    def choose_class(self, event):
        index = int(self.tree.selection()[0])

        global tchr_list_class
        self.ent_name.delete(0, tk.END)
        self.ent_name.insert(tk.END, tchr_list_full[index]['namamurid'])
        self.lbl_file.configure(text=tchr_list_full[index]['file'])


#"""ADD ASSESSMENT PAGE"""
class AddAssessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherClassPage')
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('TeacherAssignPage')
            )
        lbl_title = tk.Label(
                self,
                text='Add Assignment',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )

        frmlbl_asg = tk.LabelFrame(
                self,
                bg='white',
                text='Assignment Name',
                font=controller.fonts['h6'],
            )
        ent_assign = ttk.Entry(
                frmlbl_asg,
            )
        frmlbl_dl = tk.LabelFrame(
                self,
                bg='white',
                text='Deadline',
                font=controller.fonts['h6'],
            )
        ent_deadline = ttk.Entry(
                frmlbl_dl,
            )
        frmlbl_desc = tk.LabelFrame(
                self,
                bg='white',
                text='Description',
                font=controller.fonts['h6'],
            )
        txt_description = tk.Text(
                frmlbl_desc,
                relief=tk.FLAT,
            )
        btn_submit = ttk.Button(
                self,
                text='Submit',
                command=lambda: add_assign(
                            tchr_class_name,
                            ent_assign.get(),
                            txt_description.get('1.0', tk.END),
                            ent_deadline.get()
                    )
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        ent_assign.place(x=15, y=10, width=400)
        frmlbl_asg.place(x=185, y=200, width=430, height=70)
        ent_deadline.place(x=15, y=10, width=400)
        frmlbl_dl.place(x=185, y=280, width=430, height=70)
        txt_description.place(x=15, y=10, width=400, height=80)
        frmlbl_desc.place(x=185, y=360, width=430, height=120)

        btn_submit.place(x=350, y=500, width=100)


#"""GIVE ALERT PAGE"""
class GiveAlertPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        lbl_title = tk.Label(
                self,
                text='Give Alert',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )
        frmlbl_name = tk.LabelFrame(
                self,
                text='Name',
                bg='white',
            )
        ent_name = ttk.Entry(
                frmlbl_name,
            )
        global givealert_first
        givealert_first = ent_name
        frmlbl_msg = tk.LabelFrame(
                self,
                text='Message',
                bg='white',
            )
        txt_msg = tk.Text(
                frmlbl_msg,
                relief=tk.FLAT,
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )
        btn_send = ttk.Button(
                self,
                text='Send Alert',
                command=lambda: send_alert(
                    ent_name.get(),
                    txt_msg.get('1.0', tk.END)
                )
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        ent_name.place(x=15, y=10, width=400)
        frmlbl_name.place(x=185, y=200, width=430, height=70)
        txt_msg.place(x=15, y=15, width=400, height=110)
        frmlbl_msg.place(x=185, y=290, width=430, height=160)

        btn_back.place(x=270, y=510, width=100)
        btn_send.place(x=380, y=510, width=150)


#"""ADD CHILDREN PAGE"""
class MyChildrenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        lbl_title = tk.Label(
                self,
                text='My Childs',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )
        lbl_list = tk.Label(
                self,
                text='dummy',
                bg='white',
                bd=2,
            )
        global prntchild_first
        prntchild_first = lbl_list
        frmlbl_add = tk.LabelFrame(
                self,
                text='Add Child',
                bg='white',
            )
        lbl_new = tk.Label(
                frmlbl_add,
                text='New Child Name',
                bg='white',
            )
        ent_new = ttk.Entry(
                frmlbl_add,
            )
        btn_add = ttk.Button(
                frmlbl_add,
                text='Add',
                command=lambda: add_child(
                    ent_new.get(),
                )
            )
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=100, width=800)

        lbl_list.place(x=185, y=180, width=430, height=120)
        lbl_new.place(x=15, y=15, width=120, height=30)
        ent_new.place(x=145, y=15, width=270, height=30)
        btn_add.place(x=320, y=60, width=100, height=40)
        frmlbl_add.place(x=185, y=310, width=430, height=135)

        btn_back.place(x=350, y=510, width=100)


#"""CHILDREN'S ASSIGNMENTS PAGE"""
class MyChildAssignmentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        frm_navbar = tk.Frame(
                self,
                bg='deepskyblue',
                height=40,
            )
        btn_navbar = tk.Button(
                frm_navbar,
                text=title,
                font=controller.fonts['h6'],
                anchor='center',
                bg='deepskyblue',
                activebackground='deepskyblue',
                fg='white',
                activeforeground='white',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('HomePage')
            )
        btn_logout = tk.Button(
                frm_navbar,
                text='Logout',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('StartPage')
            )
        btn_profile = tk.Button(
                frm_navbar,
                text='Profile',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
                command=lambda: controller.show_frame('ProfilePage')
            )
        btn_classes = tk.Button(
                frm_navbar,
                text='Classes',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        btn_assign = tk.Button(
                frm_navbar,
                text='Assignment',
                font=controller.fonts['p'],
                anchor='center',
                bg='deepskyblue',
                activebackground='white',
                fg='white',
                activeforeground='black',
                highlightthickness=0,
                relief=tk.FLAT,
            )
        lbl_title = tk.Label(
                self,
                text='My Child\'s Assignments',
                font=controller.fonts['h2'],
                fg='gray64',
                bg='white',
            )
        frmlbl_name = tk.LabelFrame(
                self,
                text='Name',
                bg='white',
            )
        global var_name
        var_name = tk.StringVar()
        cmb_name = ttk.Combobox(
                frmlbl_name,
                textvariable=var_name
            )
        cmb_name.bind('<<ComboboxSelected>>', select_child)
        global prntasg_first
        prntasg_first = cmb_name
        frmlbl_asg = tk.LabelFrame(
                self,
                text='Assignments',
                bg='white',
            )
        global var_asg
        var_asg = tk.StringVar()
        cmb_asg = ttk.Combobox(
                frmlbl_asg,
                textvariable=var_asg
            )
        cmb_asg.bind('<<ComboboxSelected>>', select_assess)
        global prntasg_second
        prntasg_second = cmb_asg
        frmlbl_detail = tk.LabelFrame(
                self,
                text='Detail',
                bg='white',
            )
        frmlbl_desc = tk.LabelFrame(
                frmlbl_detail,
                text='Description',
                bg='white',
            )
        lbl_desc = tk.Label(
                frmlbl_desc,
                bg='white',
            )
        global prntasg_third
        prntasg_third = lbl_desc
        frmlbl_dl = tk.LabelFrame(
                frmlbl_detail,
                text='Deadline',
                bg='white',
            )
        lbl_dl = tk.Label(
                frmlbl_dl,
                bg='white',
            )
        global prntasg_fourth
        prntasg_fourth = lbl_dl
        frmlbl_stat = tk.LabelFrame(
                frmlbl_detail,
                text='Status',
                bg='white',
            )
        lbl_stat = tk.Label(
                frmlbl_stat,
                bg='white',
            )
        global prntasg_fifth
        prntasg_fifth = lbl_stat
        btn_back = ttk.Button(
                self,
                text='Back',
                command=lambda: controller.show_frame('HomePage')
            )
        btn_alert = ttk.Button(
                self,
                text='Alert',
                command=lambda: controller.show_frame('GiveAlertPage')
            )

        btn_logout.place(x=700, width=100, height=40)
        btn_profile.place(x=0, width=100, height=40)
        btn_classes.place(x=100, width=100, height=40)
        btn_assign.place(x=200, width=100, height=40)
        btn_navbar.place(x=300, width=200, height=40)
        frm_navbar.place(width=800)

        lbl_title.place(y=80, width=800)

        cmb_name.place(x=15, width=400, height=40)
        frmlbl_name.place(x=185, y=150, width=430, height=70)
        cmb_asg.place(x=15, width=400)
        frmlbl_asg.place(x=185, y=230, width=430, height=70)

        lbl_desc.place(x=15, width=370, height=70)
        frmlbl_desc.place(x=15, width=400, height=100)
        lbl_dl.place(x=15, width=160, height=30)
        frmlbl_dl.place(x=15, y=110, width=190, height=60)
        lbl_stat.place(x=15, width=160, height=30)
        frmlbl_stat.place(x=225, y=110, width=190, height=60)
        frmlbl_detail.place(x=185, y=310, width=430, height=200)

        btn_back.place(x=290, y=540, width=100)
        btn_alert.place(x=410, y=540, width=100)


#"""RUN APP"""
if __name__ == '__main__':
    window = BukuBocil()
    window.resizable(0, 0)
    window.mainloop()
