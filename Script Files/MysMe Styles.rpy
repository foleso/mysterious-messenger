################################################################################
## Initialization
################################################################################

init offset = -1

init 5:

    ### Note: you can find most of the gui values in the gui.rpy file
    ###  if you're looking to change them

        
    ##************************************
    ## Custom Text Tags
    ##************************************
    
    ## Curly Font
    style curly is say_dialogue:
        size gui.text_size + 6
        font "00 fonts/Sandoll Misaeng (Curly Font).ttf"
    
    ## Serif Font 1
    style ser1 is say_dialogue:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"

    style ser1b is say_dialogue:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf"
 
    style ser1xb is say_dialogue:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf"
      
    ## Serif Font 2
    style ser2 is say_dialogue:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf"
        
    style ser2b is say_dialogue:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf"
        
    style ser2xb is say_dialogue:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf"
        
    ## Sans Serif Font 1
    style sser1 is say_dialogue:
        # this is the regular dialogue
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style sser1b is say_dialogue:
        # this is the regular dialogue
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    style sser1xb is say_dialogue:
        # this is the regular dialogue
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
    
    ## Sans Serif Font 2
    style sser2 is say_dialogue:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
        
    style sser2b is say_dialogue:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf"
        
    style sser2xb is say_dialogue:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf"
      
    ## Blocky Font
    style blocky is say_dialogue:
        font "00 fonts/BM-HANNA (Bold Font).ttf"
        
       

    ####################################
    ## Other Styles
    ####################################
    
    style phone_window is default
    style phone_entry is default

    style phone_label is say_label
    style phone_dialogue is say_dialogue

    style phone_button is button
    style phone_button_text is button_text

    # Position of images the characters post
    style phone_img:
        left_padding 5
        right_padding 5
        padding (5, 10)
        bottom_margin gui.phone_img_bottom_margin
        pos gui.phone_text_pos
        xanchor gui.phone_text_xalign
        xmaximum gui.phone_text_width
        min_width gui.phone_text_width
        text_align gui.phone_text_xalign
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    # Position of the characters' profile pictures
    style phone_profpic:
        xpos gui.phone_profpic_xpos
        xanchor gui.phone_profpic_xalign
        ypos gui.phone_profpic_ypos
        xsize gui.phone_profpic_width
        min_width gui.phone_profpic_width
        text_align gui.phone_profpic_xalign

    style phone_profpic_MC:
        xpos gui.phone_profpicMC_xpos
        xanchor gui.phone_profpicMC_xalign
        ypos gui.phone_profpicMC_ypos
        xsize gui.phone_profpicMC_width
        min_width gui.phone_profpicMC_width
        text_align gui.phone_profpicMC_xalign
        
    # Position of the characters' dialogue text
    style phone_label:
        xpos gui.phone_name_xpos
        xanchor gui.phone_name_xalign
        ypos gui.phone_name_ypos
        yanchor 0.0
        xsize gui.phone_name_width
        min_width gui.phone_name_width
        text_align gui.phone_name_xalign
        font gui.phone_name_font

    style phone_label_MC:
        xpos gui.phone_nameMC_xpos
        xanchor gui.phone_nameMC_xalign
        ypos gui.phone_nameMC_ypos
        yanchor 0.0
        xsize gui.phone_nameMC_width
        min_width gui.phone_nameMC_width
        text_align gui.phone_nameMC_xalign
        font gui.phone_name_font

    style phone_window:
        xfill True
        yfill True
        background "gui/nvl.png"
        padding gui.phone_borders.padding

    style phone_dialogue:
        pos gui.phone_text_pos
        xanchor gui.phone_text_xalign
        xsize gui.phone_text_width
        min_width gui.phone_text_width
        text_align gui.phone_text_xalign
        layout ("subtitle" if gui.phone_text_xalign else "tex")

    style phone_message_total:
        spacing 10
        
    style input_window:
        xalign 0.5
        yalign 0.2
            
    style input_prompt:
        xalign 0.5
        yalign 0.2
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
        
    style input_answer:
        xalign 0.5
        yalign 0.5

#*********************************************************************

    # Code leftover from when you could add the time to characters'
    # messages. Currently unused
    style phone_time is text:
        size 14
        color "#575757"
        xpos 410
        ypos 25

    style phone_time2 is text:
        size 14
        color "#575757"
        xpos 380
        ypos -100

    style phone_time3 is text:
        size 14
        color "#575757"
        xpos 160
        ypos -100


    ####################################
    ## Tranforms
    ####################################
           
    # Used for animations that bounce
    # (glowing and special speech bubbles)
    transform incoming_message_bounce:
        alpha 0 zoom 0.5
        linear 0.1 alpha 0.8 zoom 1.1
        linear 0.1 alpha 1.0 zoom 1.0
        on hide:
            hide_message
        
    # Used for most other things (bubbles,
    # emojis, etc)
    transform incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 1.0 zoom 1.0
        
    transform hide_message:
        linear 0.2 alpha 1.0 zoom 1.0
        alpha 0 zoom 0.5
        

    #***********************************
    # These are for MysMe animation
    #***********************************
    transform anti_incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 0.0 zoom 0

    transform anti_incoming_message_bounce:
        alpha 0 zoom 0.6
        linear 0.1 alpha 0 zoom 0.0
        linear 0.1 zoom 0.1
        
    transform anti_hide_message:
        linear 0.2 alpha 0.0 zoom 0
        alpha 0 zoom 0.5
        on hide:
            anti_hide_message      
        
    # Shows the heart icon
    transform heart:
        alpha 0.3
        xalign 0.3 yalign 0.3
        alignaround (.5, .55)
        linear 0.6 xalign .4 yalign .6 clockwise circles 0 alpha 1
        linear 0.02 alpha 0 xalign .35 yalign .55
           
    # The heartbreak icon
    transform heartbreak:
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0
        
    # Haven't been able to get this to work the way I want
    transform phone_message_NEW:
        xoffset 0
        yoffset 0
        
    # Used for the screen shake effect
    transform shake:    
        linear 0.12 xoffset -150 yoffset -200
        linear 0.12 xoffset 80 yoffset 60
        linear 0.14 xoffset -80 yoffset -60
        linear 0.14 xoffset 80 yoffset 60
        linear 0.16 xoffset 0 yoffset 0
        
    # Used for the hacker screen effect
    transform flicker:
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.02 alpha 1.0
