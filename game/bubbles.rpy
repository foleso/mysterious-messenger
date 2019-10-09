#************************************
# Special Bubbles
#************************************

### Note: you can find most of the gui values in the gui.rpy file
###  if you're looking to change them

####################################
## Speech bubbles - GLOW variant
####################################

## ****************************************
## Glow Speech Bubble Style
style glow_bubble:    
    xalign 0.0
    padding (25, 28, 25, 22)
    pos (138, 38)

    
####################################
## Speech bubbles - For TEXT
####################################
    
style bubble_text:
    line_spacing gui.phone_text_line_spacing
    xalign 0.0
    yalign 0.5
    
# This bubble is shown when the text wraps
# It forces the width to be a certain length
style bubble_text_long:
    line_spacing gui.phone_text_line_spacing
    xalign 0.0
    yalign 0.5
    xsize gui.phone_text_xsize_long
    
    
# This is for the "special" speech bubbles
# It's mostly just telling it to center the text
style special_bubble:
    text_align 0.5
    line_spacing gui.phone_text_line_spacing - 10
    ycenter 0.55
    xcenter 0.5
    #align (.5, .5)

####################################
## Speech bubbles - REGULAR variant
####################################

## ****************************************
## Regular Speech Bubble Style
style reg_bubble_MC:
    background Frame("Bubble/m-bubble.png", 18, 18, 25, 18)    
    padding (20, 15, 20, 9)
    pos (750-138-5,38)
    xanchor 1.0
        
style reg_bubble:  
    padding (20, 15, 20, 9)
    pos (138, 38)
    
# one-line variant (fixes spacing)
style reg_bubble_short: 
    padding (20, 9)
    
## TEXT MESSAGES
# MC's text speech bubble
style reg_bubble_MC_text:
    background Frame("Text Messages/msgsl_text_player.png", 60,60,60,10)
    #bottom_margin -55
    padding (20,12,60,12)
        
# Other characters' text speech bubble
style reg_bubble_text:        
    background Frame("Text Messages/msgsl_text_npc.png", 60,60,60,10)
    padding (60,12,20,12)
    
## ****************************************
## Style for the enter/exit bubble
style msg_bubble:
    background Frame("exit-enter.png", 0, 0)
    padding (5, 10)
    xalign 0.5
    xfill True
            
style msg_bubble_text:
    text_align 0.5
    font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
    size gui.text_size - 10
    color "#ffffff"
    xalign 0.5
    
## ****************************************
## Style for 'padding' dialogue that pushes
## text to the bottom
style filler_bubble:
    padding (5, 10)
            
style filler_bubble_text:
    size 35

    
####################################
## Super Special Bubbles
####################################
   
## SPIKE
style spike_s:
    padding gui.spike_s_padding
    pos gui.spike_s_pos
    xysize gui.spike_s_xysize
    
style spike_m:
    padding gui.spike_m_padding
    pos gui.spike_m_pos
    xysize gui.spike_m_xysize
    
style spike_l:
    padding gui.spike_l_padding
    pos gui.spike_l_pos
    xysize gui.spike_l_xysize
    
## CLOUD
style cloud_s:
    padding gui.cloud_s_padding
    pos gui.cloud_s_pos
    xysize gui.cloud_s_xysize
    
style cloud_m:
    padding gui.cloud_m_padding
    pos gui.cloud_m_pos
    xysize gui.cloud_m_xysize
    
style cloud_l:
    padding gui.cloud_l_padding
    pos gui.cloud_l_pos
    xysize gui.cloud_l_xysize
    
## SPECIAL BUBBLE 1 (ROUND)
style round_s:
    padding gui.round_s_padding
    pos gui.round_s_pos
    xysize gui.round_s_xysize
    
style round_m:
    padding gui.round_m_padding
    pos gui.round_m_pos
    xysize gui.round_m_xysize
    
style round_l:
    padding gui.round_l_padding
    pos gui.round_l_pos
    xysize gui.round_l_xysize
    
## SPECIAL BUBBLE 2 (SQUARE)
style square_s:
    padding gui.square_s_padding
    pos gui.square_s_pos
    xysize gui.square_s_xysize
    
style square_m:
    padding gui.square_m_padding
    pos gui.square_m_pos
    xysize gui.square_m_xysize
    
style square_l:
    padding gui.square_l_padding
    pos gui.square_l_pos
    xysize gui.square_l_xysize
    
## SIGH BUBBLE
style sigh_s:
    padding gui.sigh_s_padding
    pos gui.sigh_s_pos
    xysize gui.sigh_s_xysize
    
style sigh_m:
    padding gui.sigh_m_padding
    pos gui.sigh_m_pos
    xysize gui.sigh_m_xysize
    
style sigh_l:
    padding gui.sigh_l_padding
    pos gui.sigh_l_pos
    xysize gui.sigh_l_xysize
        
        
default bubble_list = [ ['Bubble/', '-Bubble.png'], ['Bubble/', '-Glow.png'],
                        ['Bubble/Special/', '_cloud_l.png'], 
                        ['Bubble/Special/', '_cloud_m.png'], 
                        ['Bubble/Special/', '_cloud_s.png'],
                        ['Bubble/Special/', '_round_l.png'], 
                        ['Bubble/Special/', '_round_m.png'], 
                        ['Bubble/Special/', '_round_s.png'],
                        ['Bubble/Special/', '_sigh_l.png'], 
                        ['Bubble/Special/', '_sigh_m.png'], 
                        ['Bubble/Special/', '_sigh_s.png'],
                        ['Bubble/Special/', '_square_l.png'], 
                        ['Bubble/Special/', '_square_m.png'], 
                        ['Bubble/Special/', '_square_s.png'],
                        ['Bubble/Special/', '_spike_l.png'], 
                        ['Bubble/Special/', '_spike_m.png'], 
                        ['Bubble/Special/', '_spike_s.png'],
                        ['Bubble/Special/', '_square2_l.png'], 
                        ['Bubble/Special/', '_square2_m.png'], 
                        ['Bubble/Special/', '_square2_s.png'],
                        ['Bubble/Special/', '_round2_l.png'], 
                        ['Bubble/Special/', '_round2_m.png'], 
                        ['Bubble/Special/', '_round2_s.png'] ]