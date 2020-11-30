#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Nov 30, 2020 08:30:50 AM +07  platform: Windows NT
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
    wm geometry $top 600x500+654+111
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
    wm title $top "Student - My Profile"
    vTcl:DefineAlias "$top" "student_myprofile" vTcl:Toplevel:WidgetProc "" 1
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
        -command {#} -foreground black -label {Add Class} 
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
        -command {#} -foreground black -label {My Assignment} 
    frame $top.fra49 \
        -borderwidth 2 -background #05bff5 -height 35 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 605 
    vTcl:DefineAlias "$top.fra49" "navbar" vTcl:WidgetProc "student_myprofile" 1
    set site_3_0 $top.fra49
    button $site_3_0.but51 \
        -activebackground white -activeforeground #000000 -background white \
        -disabledforeground black \
        -font {-family {Arcon Rounded-} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #05bff5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -relief flat -text Logout 
    vTcl:DefineAlias "$site_3_0.but51" "logout_butt" vTcl:WidgetProc "student_myprofile" 1
    label $site_3_0.lab55 \
        -activebackground #05bff5 -activeforeground white -background #05bff5 \
        -disabledforeground black \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground white -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Buku Penghubung} 
    vTcl:DefineAlias "$site_3_0.lab55" "app_name" vTcl:WidgetProc "student_myprofile" 1
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.9 -y 0 -width 60 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -y 0 -width 0 -relwidth 0.2 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    labelframe $top.lab57 \
        -borderwidth 4 \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground black -relief flat -text {My Profile} -background white \
        -height 470 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 580 
    vTcl:DefineAlias "$top.lab57" "main_profile" vTcl:WidgetProc "student_myprofile" 1
    set site_3_0 $top.lab57
    labelframe $site_3_0.lab58 \
        -font TkDefaultFont -foreground black -text Name \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 150 
    vTcl:DefineAlias "$site_3_0.lab58" "get_name" vTcl:WidgetProc "student_myprofile" 1
    set site_4_0 $site_3_0.lab58
    entry $site_4_0.ent64 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 330 
    vTcl:DefineAlias "$site_4_0.ent64" "entry_name" vTcl:WidgetProc "student_myprofile" 1
    place $site_4_0.ent64 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.357 -width 330 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab59 \
        -font TkDefaultFont -foreground black -text Username \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 360 
    vTcl:DefineAlias "$site_3_0.lab59" "get_username" vTcl:WidgetProc "student_myprofile" 1
    set site_4_0 $site_3_0.lab59
    entry $site_4_0.ent65 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 330 
    vTcl:DefineAlias "$site_4_0.ent65" "entry_username" vTcl:WidgetProc "student_myprofile" 1
    place $site_4_0.ent65 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.327 -width 330 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab60 \
        -font TkDefaultFont -foreground black -text Email \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 360 
    vTcl:DefineAlias "$site_3_0.lab60" "get_email" vTcl:WidgetProc "student_myprofile" 1
    set site_4_0 $site_3_0.lab60
    entry $site_4_0.ent66 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 330 
    vTcl:DefineAlias "$site_4_0.ent66" "entry_email" vTcl:WidgetProc "student_myprofile" 1
    place $site_4_0.ent66 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.327 -width 330 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab61 \
        -font TkDefaultFont -foreground black -text {Phone Number} \
        -background $vTcl(actual_gui_bg) -height 60 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 360 
    vTcl:DefineAlias "$site_3_0.lab61" "get_phone_number" vTcl:WidgetProc "student_myprofile" 1
    set site_4_0 $site_3_0.lab61
    entry $site_4_0.ent67 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 330 
    vTcl:DefineAlias "$site_4_0.ent67" "entry_phone_number" vTcl:WidgetProc "student_myprofile" 1
    place $site_4_0.ent67 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.339 -width 330 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab62 \
        -font TkDefaultFont -foreground black -text Address \
        -background $vTcl(actual_gui_bg) -height 110 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 360 
    vTcl:DefineAlias "$site_3_0.lab62" "get_address" vTcl:WidgetProc "student_myprofile" 1
    set site_4_0 $site_3_0.lab62
    entry $site_4_0.ent68 \
        -background white -disabledforeground #bfbfbf -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 330 
    vTcl:DefineAlias "$site_4_0.ent68" "entry_address" vTcl:WidgetProc "student_myprofile" 1
    place $site_4_0.ent68 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.171 -width 330 \
        -relwidth 0 -height 80 -relheight 0 -anchor nw -bordermode ignore 
    button $site_3_0.but63 \
        -activebackground #05bff5 -activeforeground white -background white \
        -disabledforeground #bfbfbf \
        -font {-family {Arcon Rounded-} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #05bff5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text back 
    vTcl:DefineAlias "$site_3_0.but63" "back_butt" vTcl:WidgetProc "student_myprofile" 1
    place $site_3_0.lab58 \
        -in $site_3_0 -x 0 -relx 0.198 -y 0 -rely 0.085 -width 0 \
        -relwidth 0.603 -height 0 -relheight 0.128 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 0 -relx 0.198 -y 0 -rely 0.213 -width 0 \
        -relwidth 0.603 -height 0 -relheight 0.128 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 0 -relx 0.198 -y 0 -rely 0.34 -width 0 \
        -relwidth 0.603 -height 0 -relheight 0.128 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.198 -y 0 -rely 0.468 -width 0 \
        -relwidth 0.603 -height 0 -relheight 0.128 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.198 -y 0 -rely 0.596 -width 0 \
        -relwidth 0.603 -height 0 -relheight 0.234 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but63 \
        -in $site_3_0 -x 0 -relx 0.448 -y 0 -rely 0.894 -width 60 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra49 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 0.056 \
        -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.075 -width 0 -relwidth 0.967 \
        -height 0 -relheight 0.904 -anchor nw -bordermode ignore 
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

