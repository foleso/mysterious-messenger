########################################################
## This file contains the three tabs found on the
## Settings screen. It's organized as follows:
##   screen settings_tabs
##   screen profile_pic
##     screen input_popup
##   screen other_settings
##     label restart_game
##   screen preferences
##     screen voice_buttons
##     screen ringtone_drowdown
########################################################

init python:

    ## This lets you change the MC's profile picture by clicking on it
    ## The player can upload their own images as well
    def MC_pic_change():
        global m, persistent
        
        # If we're not using a custom pic, check if one's available
        # Populate the list with the file names
        file_list = renpy.list_files()
        # This now has a list of the available images
        user_pic_list = [ pic for pic in file_list 
                if 'Drop Your Profile Picture Here/' in pic and isImg(pic)]
        # Now we check if there are indeed available files
        if user_pic_list:
            if persistent.MC_pic in user_pic_list:
                # Now we go through the pics and set the pic to the
                # next available image
                # We assume the image provided is square (this is
                # the responsibility of the user)
                for i, pic in enumerate(user_pic_list):
                    if persistent.MC_pic == pic:
                        if i < len(user_pic_list) - 1:
                            persistent.MC_pic = user_pic_list[i+1]
                            break
                        elif i == len(user_pic_list) - 1:
                            persistent.MC_pic = user_pic_list[0]
                            break
            else:
                persistent.MC_pic = user_pic_list[0]
        else:
            persistent.MC_pic = 'Profile Pics/MC/MC-1.png'
            
        m.prof_pic = persistent.MC_pic
        renpy.retain_after_load()
            
    
    ## Checks for common image extensions
    def isImg(pic):
        if '.png' or '.PNG' or '.jpg' or '.jpeg' in pic:
            return True
        elif '.JPG' or '.JPEG' or '.gif' or '.GIF' in pic:
            return True
        else:
            return False
        
    
default email_tone_dict = { 'Default 1': 'sfx/Ringtones etc/email_basic_1.wav', 
                            'Default 2': 'sfx/Ringtones etc/email_basic_2.wav',     
                            'Default 3': 'sfx/Ringtones etc/email_basic_3.wav'
                          }
                          
default text_tone_dict = {  'Default': 'sfx/Ringtones etc/text_basic_1.wav', 
                            'Jumin Han': 'sfx/Ringtones etc/text_basic_ju.wav',     
                            'Jaehee Kang': 'sfx/Ringtones etc/text_basic_ja.wav',
                            '707': 'sfx/Ringtones etc/text_basic_s.wav',
                            'Yoosung★': 'sfx/Ringtones etc/text_basic_y.wav',
                            'ZEN': 'sfx/Ringtones etc/text_basic_z.wav'
                         }
                            
default ringtone_dict = {   'Default': 'sfx/Ringtones etc/phone_basic_1.wav', 
                            'Jumin Han': 'sfx/Ringtones etc/phone_basic_ju.wav',     
                            'Jaehee Kang': 'sfx/Ringtones etc/phone_basic_ja.wav',
                            '707': 'sfx/Ringtones etc/phone_basic_s.wav',
                            'Yoosung★': 'sfx/Ringtones etc/phone_basic_y.wav',
                            'ZEN': 'sfx/Ringtones etc/phone_basic_z.wav'
                        }
                        
# This is organized as a list of lists. The first item is the name of
# the category. The second item is a list of the names of the tones
# as you defined them above in the dictionary. To define more categories,
# put a comma after the second-last bracket and define another list like
# shown below
default email_tone_list = [ ["Basic", ['Default 1', 'Default 2', 'Default 3' ]]
                          ]
                          
default text_tone_list = [ ["Basic", ['Default', 'Jumin Han', 'Jaehee Kang', 
                            '707', 'Yoosung★', 'ZEN' ]]
                          ]
                          
default ringtone_list = [ ["Basic", ['Default', 'Jumin Han', 'Jaehee Kang', 
                            '707','Yoosung★', 'ZEN' ]]
                          ]
                          
default persistent.phone_tone = 'sfx/Ringtones etc/phone_basic_1.wav'
default persistent.text_tone = "sfx/Ringtones etc/text_basic_1.wav"
default persistent.email_tone = 'sfx/Ringtones etc/email_basic_1.wav'
default persistent.phone_tone_name = "Default"
default persistent.text_tone_name = "Default"
default persistent.email_tone_name = "Default 1"


########################################################
## The three tabs on the Settings screen
########################################################

screen settings_tabs(active_tab):

    style_prefix "settings_tabs"
    # "Backgrounds" of the different panels
    hbox:
        # Account / Sound / Others tab
        textbutton _('Profile'):            
            if active_tab == "Profile":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"
                action Show("profile_pic", Dissolve(0.5))
                
        textbutton _('Sound'):
            if active_tab == "Sound":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"                
                action Show("preferences", Dissolve(0.5))                
            
        textbutton _('Others'):
            if active_tab == "Others":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"
                action Show("other_settings", Dissolve(0.5))                
                
style settings_tabs_hbox is empty
style settings_tabs_button is empty
style settings_tabs_button_text is default


style settings_tabs_hbox:
    spacing 10

style settings_tabs_button:
    xsize 231
    ysize 57
    activate_sound 'sfx/UI/settings_tab_switch.mp3'
    hover_background "menu_tab_inactive_hover"

style settings_tabs_button_text:
    color '#fff'
    font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
    text_align 0.5
    xalign 0.5
    yalign 0.5
        
########################################################
## The "Profile" tab of Settings. Allows you to change
## your profile pic, name, and preferred pronouns
########################################################

screen profile_pic():
    
    tag settings_screen
    modal True

    if persistent.first_boot:
        use menu_header("Customize your Profile", MainMenu(False))
    else:
        use menu_header("Settings", Hide('profile_pic', Dissolve(0.5)))

    if not persistent.first_boot:
        use settings_tabs("Profile")  
    
    window:        
        style 'profile_pic_window'
        has vbox
        # MC's profile picture
        imagebutton:
            focus_mask True
            xalign 0.055
            idle Transform(persistent.MC_pic, size=(363,363))
            action [Function(MC_pic_change),
                    renpy.restart_interaction]
        # Edit MC's Name
        fixed:
            add "name_line" xalign 0.079 yalign 0.9        
            text persistent.name style 'profile_pic_text'
            
            imagebutton:
                style 'profile_pic_imagebutton'
                idle "menu_edit"            
                hover Transform("Phone UI/Main Menu/menu_pencil_long.png", 
                                                                    zoom=1.03)
                action Show('input_popup', prompt='Please input a name.') 
        
      
    # Pick your pronouns
    window:
        style 'pronoun_window'
        style_prefix "pronoun_window"
    
        has vbox        
        text "Preferred Pronouns"
        button:     
            action [SetField(persistent, "pronoun", "female"), 
                    Function(set_pronouns)] 
            has hbox
            spacing 10
            if persistent.pronoun == "female":
                add "radio_on"
            else:
                add "radio_off"
            text 'she/her' style 'pronoun_radio_text'
            
        button:
            action [SetField(persistent, "pronoun", "male"), 
                    Function(set_pronouns)]
            has hbox
            spacing 10
            if persistent.pronoun == "male":
                add "radio_on"
            else:
                add "radio_off"
            text 'he/him' style 'pronoun_radio_text'
            
            
        button:
            action [SetField(persistent, "pronoun", "non binary"), 
                    Function(set_pronouns)]
            has hbox
            spacing 10
            if persistent.pronoun == "non binary":
                add "radio_on"
            else:
                add "radio_off"
            text 'they/them' style 'pronoun_radio_text'
             
        
        if not persistent.first_boot and not main_menu:                
            # Save / Load
            imagebutton:
                style_prefix None
                yalign 0.978
                xalign 0.66
                idle "save_btn"
                hover Transform("Phone UI/Main Menu/menu_save_btn.png", zoom=1.1)
                action Show("save", Dissolve(0.5))
                
            imagebutton:
                style_prefix None
                yalign 0.978
                xalign 0.974
                idle "load_btn"
                hover Transform("Phone UI/Main Menu/menu_load_btn.png", zoom=1.1)
                action Show("load", Dissolve(0.5))
            
                
            # Shows how many heart points you've earned with
            # each character. To display properly, this needs to
            # be a character variable, and there must be an image
            # defined called 'greet ja' if the character's file_id
            # is ja, for example
            $ heart_point_chars = [ja, ju, sa, ri, s, v, y, z]
            grid 4 2:
                xalign 0.5
                yalign 0.8
                for c in heart_point_chars:
                    use heart_point_grid(c)

screen heart_point_grid(c):
    vbox:
        xysize (150,200)
        align (.5, .5)
        add 'greet ' + c.file_id
        text str(c.heart_points) + " {image=header_heart}":
            style "point_indicator"

style profile_pic_window is empty
style profile_pic_text is default
style profile_pic_imagebutton is empty

style profile_pic_window:
    yalign 0.32
    xalign 0.05
    xysize(370, 440)

style profile_pic_text:
    color "#fff"
    text_align 0.0
    hover_color "#d7d7d7"
    font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
    xalign 0.06
    yalign 0.455

style profile_pic_imagebutton:
    focus_mask None
    xalign 0.06
    yalign 0.453

style pronoun_window_text is empty
style pronoun_window_vbox is empty
style pronoun_window_text is empty
style pronoun_radio_text is default
style pronoun_window_vbox is default

style pronoun_window:
    background Frame("Phone UI/Main Menu/greeting_panel.png", 20, 20)
    maximum(340,400)
    xalign 0.99
    yalign 0.32
    padding (20,20)
    xfill True
    yfill True

style pronoun_window_vbox:
    spacing 15
    xalign 0.5
    yalign 0.5

style pronoun_window_text:
    size 40
    color "#fff"
    text_align 0.5

style pronoun_radio_text:
    color '#fff' 
    hover_color '#ddd'
            
style pronoun_window_vbox:
    xysize (240,300)
    xalign 0.5
    yalign 0.5

########################################################
## The Input Prompt to get text from the user
########################################################
                
screen input_popup(prompt=''):

    python:
        # We save this so we can reset it if they don't want to change it
        old_name = persistent.name    
        input = Input(value=NameInput(), 
                style="my_input", length=20)
                
    zorder 100
    modal True
    key 'K_RETURN' action Hide('input_popup')
    key 'K_KP_ENTER' action Hide('input_popup')

    style_prefix "my_input"
    window:      
        imagebutton: 
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'           
            action [SetField(m, 'name', old_name), 
                    SetVariable('name', old_name), 
                    SetField(persistent, 'name', old_name), 
                    renpy.retain_after_load, Hide('input_popup')]
        vbox:            
            text prompt 
            fixed:                
                add 'input_square'
                add input xalign 0.5 yalign 0.5
            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'my_input_textbutton'                
                action [Hide('input_popup')]

style my_input_window:
    is empty
    xalign 0.5
    yalign 0.4
    xysize(550,313)
    background 'input_popup_bkgr'       

style my_input_vbox:
    is empty
    spacing 20
    xalign 0.5
    yalign 0.5

style my_input_text:
    is default
    color '#fff' 
    xalign 0.5 
    text_align 0.5

style my_input_fixed:
    is empty
    xsize 500 
    ysize 75
    xalign 0.5

style my_input_textbutton:
    is default
    xalign 0.5
    xsize 240
    ysize 80
    background 'menu_select_btn' padding(20,20)
    hover_background 'menu_select_btn_hover'

style my_input:
    is default
    color "#000"
    text_align 0.5
    hover_color "#d7d7d7"
    font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"



########################################################
## The "Others" tab of the settings screen
## Includes VN options and Ringtone selection
########################################################
              
screen other_settings():

    tag settings_screen
    modal True

    #add "Phone UI/Main Menu/menu_settings_bg.png"
    
    use menu_header("Settings", Hide('other_settings', Dissolve(0.5))):
        use settings_tabs("Others")
            
        viewport:
            style 'other_settings_viewport'
            draggable True
            mousewheel True
            side_spacing 5
            style_prefix "other_settings"
            has vbox            
            window:
                xysize(675,320)
                background "menu_settings_panel"
                text "Other Settings" style "settings_style" xpos 55 ypos 5
                style_prefix "settings_slider"
                vbox:               
                    null height 30 # For the 'title'          
                    hbox:                        
                        textbutton _("Text Speed")                           
                        bar value Preference("text speed")
                        
                    hbox:
                        textbutton _("Auto-Forward Time")
                        bar value Preference("auto-forward time"):
                            bar_invert True
                    
                    null height 5
                    fixed:                        
                        style_prefix "check"
                        textbutton _("Custom UI changes"):
                            action ToggleField(persistent, "custom_footers")
                
            window:
                xysize(675,250)
                background "menu_settings_panel"
                text "VN Settings" style "settings_style" xpos 55 ypos 5

                vbox:
                    spacing 6
                    style_prefix "check"
                    null height 30
                    label _("Skip")
                    textbutton _("Unseen Text"):
                        action Preference("skip", "toggle")
                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))
                    
            window:
                xysize(675,280)
                background "menu_settings_panel"
                text "Variables for testing" style "settings_style" xpos 55 ypos 5

                vbox:
                    spacing 6
                    style_prefix "check"
                    null height 30
                    textbutton _("Testing Mode"):
                        action ToggleField(persistent, "testing_mode")
                    textbutton _("Real-Time Mode"):
                        action ToggleField(persistent, "real_time")
                    textbutton _("Hacked Effect"):
                        action ToggleVariable('hacked_effect')
                    textbutton _("Real-Time Texts"):
                        action ToggleField(persistent,'instant_texting')
                    
            
                    
                # Additional vboxes of type "radio_pref" or "check_pref" can be
                # added here, to add additional creator-defined preferences.
                
            
            
            window:
                style_prefix "other_settings_end"            
                has hbox
                textbutton _('Go to Mode Select'):          
                    action [ToggleVariable("greeted", False, False), 
                            renpy.full_restart]
                    
                textbutton _('Start Over'):
                    action Show("confirm", message="Are you sure you want to start over? You'll be unable to return to this point except through a save file.", 
                            yes_action=[Hide('confirm'), 
                            Jump("restart_game")], no_action=Hide('confirm'))


style other_settings_viewport:
    is empty
    xysize(700, 1070)
    xalign 0.5
    yalign 0.95

style other_settings_vbox:
    spacing 30
    xalign 0.5

style other_settings_frame is default
style other_settings_window is default

style other_settings_hbox:
    is default
    align (0.2, 0.7)
    box_wrap True

style settings_slider_vbox:
    is slider_vbox
    spacing 15
    xsize 625
    xalign 0.5
    yalign 0.5
style check_vbox is settings_slider_vbox

style settings_slider_hbox:
    is slider_hbox
    spacing 20
    xsize 600

style settings_slider_button:
    is slider_button
    xsize 200
    ysize 70
    background "menu_other_box"

style settings_slider_button_text is sound_tags

style settings_slider_slider:
    xsize 380 
    yalign 0.5 
    thumb_offset 18 
    left_gutter 18 

style check_fixed:
    is default
    yfit True
    xfit True
    xalign 0.15

style other_settings_end_window:
    is default
    xysize (520, 130)
    xalign 0.5

style other_settings_end_hbox:
    is default
    spacing 40

style other_settings_end_button:
    xsize 240
    ysize 120
    background 'menu_select_btn' padding(20,20)
    hover_background 'menu_select_btn_hover'

style other_settings_end_button_text:
    is mode_select


# *********************************
# Restart Game -- resets variables
# *********************************       
label restart_game():
    python:
        # removes heart points from all the characters
        for person in character_list:
            person.reset_heart()
        
        # presumably some more resets here as needed
        persistent.on_route = False
        renpy.full_restart()
        



## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##

screen preferences():

    tag settings_screen
    modal True

    use starry_night
    use menu_header("Settings", Hide('preferences', Dissolve(0.5))):
        use settings_tabs("Sound")
        
        viewport:
            style_prefix 'other_settings'
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 5
            has vbox
    
            window:
                xysize(675,400)
                background "menu_settings_panel" padding(10,10)
                text "Sound" style "settings_style" xpos 55
                style_prefix "sound_settings"
                vbox:                      
                    null height 30
                    hbox:                    
                        textbutton _("BGM") action ToggleMute("music")
                        bar value Preference("music volume")
                    hbox:
                        textbutton _("SFX") action ToggleMute("sfx")
                        bar value Preference("sound volume") 
                        if config.sample_sound:
                            textbutton _("Test"):
                                style 'default'
                                action Play("sound", config.sample_sound)
                    hbox:
                        textbutton _("Voice") action ToggleMute("voice")
                        bar value Preference("voice volume")
                        if config.sample_voice:
                            textbutton _("Test"):
                                style 'default'
                                action Play("voice", config.sample_voice)
                    hbox:
                        textbutton _("Voice SFX") action ToggleMute("voice_sfx")
                        bar value set_voicesfx_volume()
                        if sample_voice_sfx:
                            textbutton _("Test"):
                                style 'default'
                                action Play("voice_sfx", sample_voice_sfx)
                        
                    textbutton _("Mute All"):
                        style "mute_all_button" xalign 0.45
                        action Preference("all mute", "toggle")
                
            window:
                xysize(675,390)
                background "menu_settings_panel" padding(10,10)
                has vbox
                xalign 0.5
                yalign 0.5
                spacing 15
                text "Voice" style "settings_style" xpos 185 ypos -5
                
                ## There are few voiced lines in this program, so currently
                ## the effects of these buttons will not be very noticeable
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing -35
                    null width 165            
                    grid 2 5:                
                        transpose True
                        spacing 30
                        align (0.5, 0.0)
                        
                        text "Jumin Han" style "settings_style"
                        text "ZEN" style "settings_style"
                        text "707" style "settings_style"
                        text "Ray" style "settings_style"
                        text "Others" style "settings_style"
                        
                        use voice_buttons('jumin')
                        use voice_buttons('zen')
                        use voice_buttons('seven')
                        use voice_buttons('saeran')
                        use voice_buttons('other')
                        
                    
                    grid 2 4:
                        spacing 30
                        transpose True
                        align (0.5, 0.0)
                        text "Yoosung★" style "settings_style"
                        text "Jaehee Kang" style "settings_style"
                        text "V" style "settings_style"
                        text "Rika" style "settings_style"
                        
                        use voice_buttons('yoosung')
                        use voice_buttons('jaehee')
                        use voice_buttons('v')
                        use voice_buttons('rika')
                        
                        
            window:
                xysize(675,360)
                background "menu_settings_panel"
                align (0.5, 0.34)
                text "Ringtone" style "settings_style" xpos 55 ypos 5
                window:
                    align (0.5, 0.85)
                    xysize (640, 300)
                    has vbox
                    align (0.5, 0.5)
                    spacing 12
                    button:
                        xysize (300, 80)
                        background 'menu_ringtone_box'
                        hover_foreground 'menu_ringtone_box'
                        vbox:
                            align (0.5, 0.5)
                            text "Text Sound" style 'ringtone_change'
                            text persistent.text_tone_name style 'ringtone_description'
                        action Show('ringtone_dropdown', title='Text Sound', tone='text')
                    
                    button:
                        xysize (300, 80)
                        background 'menu_ringtone_box'
                        hover_foreground 'menu_ringtone_box'
                        vbox:
                            align (0.5, 0.5)
                            text "Email Sound" style 'ringtone_change'
                            text persistent.email_tone_name style 'ringtone_description'
                        action Show('ringtone_dropdown', title='Email Sound', tone='text')
                        
                    button:
                        xysize (300, 80)
                        background 'menu_ringtone_box'
                        hover_foreground 'menu_ringtone_box'
                        vbox:
                            align (0.5, 0.5)
                            text "Ringtone" style 'ringtone_change'
                            text persistent.phone_tone_name style 'ringtone_description'
                        action Show('ringtone_dropdown', title='Ringtone', tone='text')

style sound_settings_vbox:
    is default
    xalign 0.5
    yalign 0.34
    spacing 15
    xsize 625

style sound_settings_hbox:
    spacing 30
    xsize 520

style sound_settings_button_text is sound_tags
style sound_settings_button:
    is default
    background "menu_sound_sfx"
    xsize 163
    ysize 50

style sound_settings_slider:
    is default
    ypos 15 
    thumb_offset 18
    left_gutter 18

## A helper screen to display the buttons for toggling
## each characters' voice on or off
screen voice_buttons(voice_char):

    $ voice_char = voice_char + '_voice'
    
    button:
        xysize (120, 30)
        idle_child Text("On", style="voice_toggle_on")
        hover_child Text("On", style="voice_toggle_on")
        selected_child Text("Off", style="voice_toggle_off")
        action ToggleVoiceMute(voice_char)
        
## A helper screen for displaying the choices you have for
## ringtones, email tones, and text tones
screen ringtone_dropdown(title, tone):

    modal True
    add "Phone UI/choice_dark.png"
    window:
        xysize(675,1000)
        background "menu_settings_panel_bright"
        align (0.5, 0.5)
        
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('ringtone_dropdown')
            
        text title style "settings_style" xpos 55 ypos 5
           
        viewport:
            xysize(600, 940)
            xalign 0.5
            yalign 0.85
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 5
            has vbox
            xsize 550
            spacing 15
            xalign 0.5
            yalign 0.5
            
            
            # Text message tones
            if title == 'Text Sound':
                $ the_list = text_tone_list
                $ the_dict = text_tone_dict
                $ p_field = 'text_tone'
            elif title == 'Email Sound':
                $ the_list = email_tone_list
                $ the_dict = email_tone_dict
                $ p_field = 'email_tone'
            elif title == 'Ringtone':
                $ the_list = ringtone_list
                $ the_dict = ringtone_dict
                $ p_field = 'phone_tone'
                
            for pair in the_list:
                # Name of the category
                null height 10
                text pair[0] color '#fff' xalign 0.5 text_align 0.5
                null height 10
                
                # List of the ringtones                
                for tone in pair[1]:
                    textbutton _(tone):
                        xysize(450, 60)
                        background '#fff'
                        text_color '#000' 
                        text_xalign 0.5 
                        text_align 0.5 
                        text_yalign 0.5
                        align (0.5, 0.5)
                        text_hover_color "#12736d"
                        selected_background "#d0d0d0"                    
                        selected getattr(persistent, p_field) == the_dict[tone]
                        if title != "Ringtone":
                            activate_sound the_dict[tone]
                            action [SetField(persistent, p_field, the_dict[tone]),
                                    SetField(persistent, p_field + '_name', tone)]
                        else:
                            activate_sound "<from 0 to 2>" + the_dict[tone]
                            action [renpy.music.stop(channel=config.play_channel),
                                    SetField(persistent, p_field, the_dict[tone]),
                                    SetField(persistent, p_field + '_name', tone)]
                    
                    
                    
                    
                    
                    