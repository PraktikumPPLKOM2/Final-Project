#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Dec 03, 2020 10:39:58 AM +07  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #ffffff
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ffffff
set vTcl(actual_gui_menu_analog) #ffffff
set vTcl(actual_gui_menu_bg) #ffffff
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ffffff
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x322+613+115
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 729
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Teacher - Submission Check"
    vTcl:DefineAlias "$top" "teacher_sub_check" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground #ffffff -activeforeground #05bff5 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground #05bff5 -tearoff 0 
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add cascade \
        -menu "$top.m45.men46" -activebackground white \
        -activeforeground #05bff5 -background white -label Profile 
    set site_3_0 $top.m45
    menu $site_3_0.men46 \
        -activebackground white -activeforeground #05bff5 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground #05bff5 -tearoff 0 
    vTcl:DefineAlias "$site_3_0.men46" "navbar" vTcl:WidgetProc "" 1
    $site_3_0.men46 add command \
        -activebackground white -activeforeground #05bff5 -background white \
        -command {#} -foreground black -label {My Profile} 
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add cascade \
        -menu "$top.m45.men47" -label Classes 
    set site_3_0 $top.m45
    menu $site_3_0.men47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $site_3_0.men47 add command \
        -activebackground white -activeforeground #05bff5 -background white \
        -command {#} -foreground black -label {Create Class} 
    $site_3_0.men47 add command \
        -activebackground white -activeforeground #05bff5 -background white \
        -command {#} -foreground black -label {My Classes} 
    $top.m45 add separator \
        
    $top.m45 add separator \
        
    $top.m45 add cascade \
        -menu "$top.m45.men48" -label Assignment 
    set site_3_0 $top.m45
    menu $site_3_0.men48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $site_3_0.men48 add command \
        -activebackground white -activeforeground #05bff5 -background white \
        -command {#} -foreground black -label {Add Assignment} 
    $site_3_0.men48 add command \
        -activebackground white -activeforeground #05bff5 -background white \
        -command {#} -foreground black -label {Assignment List} 
    frame $top.fra49 \
        -borderwidth 2 -background #05bff5 -height 30 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 605 
    vTcl:DefineAlias "$top.fra49" "navbar" vTcl:WidgetProc "teacher_sub_check" 1
    set site_3_0 $top.fra49
    button $site_3_0.but51 \
        -activebackground white -activeforeground #000000 -background white \
        -disabledforeground black \
        -font {-family {Arcon Rounded-} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #05bff5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -relief flat -text Logout 
    vTcl:DefineAlias "$site_3_0.but51" "logout_butt" vTcl:WidgetProc "teacher_sub_check" 1
    label $site_3_0.lab55 \
        -activebackground #05bff5 -activeforeground white -background #05bff5 \
        -disabledforeground black \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground white -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Buku Penghubung} 
    vTcl:DefineAlias "$site_3_0.lab55" "app_name" vTcl:WidgetProc "teacher_sub_check" 1
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.9 -y 0 -width 60 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -y 0 -width 0 -relwidth 0.2 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    labelframe $top.lab57 \
        -borderwidth 4 \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground black -relief flat -text {Assignment Name} \
        -background white -height 370 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 580 
    vTcl:DefineAlias "$top.lab57" "get_assignment_name" vTcl:WidgetProc "teacher_sub_check" 1
    set site_3_0 $top.lab57
    button $site_3_0.but63 \
        -activebackground #05bff5 -activeforeground white -background white \
        -disabledforeground #bfbfbf \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #05bff5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text back 
    vTcl:DefineAlias "$site_3_0.but63" "back_butt" vTcl:WidgetProc "teacher_sub_check" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_3_0.scr71 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_3_0.scr71" "box_student" vTcl:WidgetProc "teacher_sub_check" 1

    $site_3_0.scr71.01 configure -background white \
        -cursor xterm \
        -disabledforeground #bfbfbf \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #ffffff \
        -highlightcolor #ffffff \
        -selectbackground white \
        -selectforeground #05bff5 \
        -width 10 \
        -listvariable student_name
    frame $site_3_0.fra73 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 410 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 350 
    vTcl:DefineAlias "$site_3_0.fra73" "class_detail" vTcl:WidgetProc "teacher_sub_check" 1
    set site_4_0 $site_3_0.fra73
    labelframe $site_4_0.lab75 \
        -font TkDefaultFont -foreground black -text Name \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 330 
    vTcl:DefineAlias "$site_4_0.lab75" "owner_name" vTcl:WidgetProc "teacher_sub_check" 1
    set site_5_0 $site_4_0.lab75
    text $site_5_0.tex80 \
        -background white -font TkTextFont -foreground black -height 4 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 -wrap word 
    $site_5_0.tex80 configure -font "TkTextFont"
    $site_5_0.tex80 insert end text
    vTcl:DefineAlias "$site_5_0.tex80" "get_student_name" vTcl:WidgetProc "teacher_sub_check" 1
    place $site_5_0.tex80 \
        -in $site_5_0 -x 0 -relx 0.031 -y 0 -rely 0.34 -width 0 \
        -relwidth 0.938 -height 0 -relheight 0.5 -anchor nw \
        -bordermode ignore 
    labelframe $site_4_0.lab77 \
        -font TkDefaultFont -foreground black -text {Submission File} \
        -background $vTcl(actual_gui_bg) -height 80 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 320 
    vTcl:DefineAlias "$site_4_0.lab77" "deadline" vTcl:WidgetProc "teacher_sub_check" 1
    set site_5_0 $site_4_0.lab77
    text $site_5_0.tex82 \
        -background white -font TkTextFont -foreground black -height 30 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 300 -wrap word 
    $site_5_0.tex82 configure -font "TkTextFont"
    $site_5_0.tex82 insert end text
    vTcl:DefineAlias "$site_5_0.tex82" "get_file_name" vTcl:WidgetProc "teacher_sub_check" 1
    button $site_5_0.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #bfbfbf \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {open file} 
    vTcl:DefineAlias "$site_5_0.but50" "file_butt" vTcl:WidgetProc "teacher_sub_check" 1
    place $site_5_0.tex82 \
        -in $site_5_0 -x 0 -relx 0.031 -y 0 -rely 0.25 -width 0 \
        -relwidth 0.938 -height 0 -relheight 0.313 -anchor nw \
        -bordermode ignore 
    place $site_5_0.but50 \
        -in $site_5_0 -x 0 -relx 0.781 -y 0 -rely 0.6 -width 55 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_4_0.lab84 \
        -font TkDefaultFont -foreground black -text Score \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 129 
    vTcl:DefineAlias "$site_4_0.lab84" "set_score" vTcl:WidgetProc "teacher_sub_check" 1
    set site_5_0 $site_4_0.lab84
    entry $site_5_0.ent49 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black \
        -textvariable score -width 10 
    vTcl:DefineAlias "$site_5_0.ent49" "entry_score" vTcl:WidgetProc "teacher_sub_check" 1
    place $site_5_0.ent49 \
        -in $site_5_0 -x 0 -relx 0.031 -y 0 -rely 0.333 -width 300 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab75 \
        -in $site_4_0 -x 0 -relx 0.03 -y 0 -rely 0.024 -width 0 \
        -relwidth 0.947 -height 0 -relheight 0.284 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab77 \
        -in $site_4_0 -x 0 -relx 0.03 -y 0 -rely 0.308 -width 0 \
        -relwidth 0.947 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab84 \
        -in $site_4_0 -x 0 -relx 0.03 -y 0 -rely 0.687 -width 0 \
        -relwidth 0.947 -height 0 -relheight 0.284 -anchor nw \
        -bordermode ignore 
    button $site_3_0.but45 \
        -activebackground #05bff5 -activeforeground white -background white \
        -disabledforeground #bfbfbf \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #05bff5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text save 
    vTcl:DefineAlias "$site_3_0.but45" "save_butt" vTcl:WidgetProc "teacher_sub_check" 1
    place $site_3_0.but63 \
        -in $site_3_0 -x 0 -relx 0.388 -y 0 -rely 0.854 -width 60 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr71 \
        -in $site_3_0 -x 0 -relx 0.033 -y 0 -rely 0.08 -width 0 \
        -relwidth 0.333 -height 0 -relheight 0.739 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra73 \
        -in $site_3_0 -x 0 -relx 0.383 -y 0 -rely 0.079 -width 0 \
        -relwidth 0.583 -height 0 -relheight 0.737 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 0 -relx 0.509 -y 0 -rely 0.854 -width 60 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra49 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 0.088 \
        -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.102 -width 0 -relwidth 0.967 \
        -height 0 -relheight 0.892 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

