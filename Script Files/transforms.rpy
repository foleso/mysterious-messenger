init offset = -1

init 5:

    ####################################
    #***********************************
    ## Tranforms
    #***********************************
    ####################################
           
    # Used for animations that bounce
    # (glowing and special speech bubbles)
    transform incoming_message_bounce:
        alpha 0 zoom 0.5
        linear 0.1 alpha 0.8 zoom 1.1
        linear 0.1 alpha 1.0 zoom 1.0
        
    # Used for most other things (bubbles,
    # emojis, etc)
    transform incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 1.0 zoom 1.0
   
    # Used to make full-size CGs small enough
    # to post in a chatroom
    transform small_CG:
        alpha 0 zoom 0.175
        linear 0.2 alpha 1.0 zoom 0.35
        
    # Used on the 'NEW' sign for new messages
    transform new_fade:
        alpha 0.0
        linear 0.2 alpha 1.0
        0.5
        linear 0.5 alpha 0.0

    #***********************************
    # 'Anti' transformation for MysMe
    #***********************************
    
    transform anti_incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 0.0 zoom 0

    transform anti_incoming_message_bounce:
        alpha 0 zoom 0.6
        linear 0.1 alpha 0 zoom 0.0
        linear 0.1 zoom 0.1
        
    transform anti_small_CG:
        zoom 0.165 alpha 0
        linear 0.2 zoom 0 

            
    #***********************************
    # Spaceship/Chips Transforms
    #*********************************** 
    
    # for the spaceship wiggle
    transform spaceship_flight:
        parallel:
            linear 1.0 yoffset -15
            linear 1.0 yoffset 15
        parallel:
            linear 0.5 rotate -8
            linear 0.5 rotate 8
            linear 0.5 rotate -8
            linear 0.5 rotate 8
        parallel:
            function spaceship_xalign_func
            
        block:
            parallel:
                ease 1.35 yoffset -15
                ease 1.35 yoffset 15
                repeat
            parallel:                
                linear 0.35 rotate -8
                linear 0.25 rotate 0
                linear 0.35 rotate 8
                linear 0.25 rotate 0
                repeat
            
    # Animation that plays when the chips are available;
    # moves the ship over to the chips, then lands on the
    # chips
    transform spaceship_chips(intro=True):
        if intro:
            xalign 0.0
            parallel:
                linear 1.0 yoffset -15
                linear 1.0 yoffset 15
            parallel:
                linear 0.5 rotate -8
                linear 0.5 rotate 8
                linear 0.5 rotate -8
                linear 0.5 rotate 8
            parallel:
                linear 0.8 xalign 0.84
                0.8
                linear 0.4 xalign 0.96
            
        block:
            parallel:
                linear 1.0 yoffset -15
                linear 1.0 yoffset 15
                repeat
            parallel:
                linear 0.35 rotate -8
                linear 0.25 rotate 0
                linear 0.35 rotate 8
                linear 0.25 rotate 0
                repeat
        
    # Animation for the chips bursting out of the bag
    transform chip_anim(delay=True):
        if delay:
            alpha 0
            1.91
            alpha 1
        block:
            yoffset 0
            parallel:
                linear 0.5 yoffset -43
                linear 0.66 yoffset -43
            parallel:
                alignaround(0.5,0.5)
                linear 0.5 rotate 0
                linear 0.33 rotate 25
                linear 0.33 rotate 10
            parallel:
                zoom 1.0
                linear 0.5 zoom 1.0
                linear 0.33 zoom 1.15
                linear 0.33 zoom 1.0
            repeat
            
    # The wobble for the chip bag when the 'chip_tap' screen
    # is up
    transform chip_wobble:
        linear 0.9 rotate 5
        linear 0.7 rotate -5
        repeat
        
    # The wobble for the chip bag when the clouds are visible
    transform chip_wobble2:
        on show:
            linear 0.13 rotate 2
            linear 0.13 rotate -2
            repeat
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0
            
       
    # Transform for the smallest 'tap' sign
    transform small_tap:
        rotate -8
        zoom 0.67
        xpos 310
        ypos -40
        
    # transform for the medium 'tap' sign
    transform med_tap:
        rotate 47
        xpos 415
        ypos 40
        
    # transform for the largest 'tap' sign
    transform large_tap:
        rotate 28
        zoom 1.5
        xpos 360
        ypos -100
        
    # Below are the different 'shuffle' animations for the
    # clouds obscuring the chip bag
    transform cloud_shuffle1:
        zoom 1.0 xanchor 1.0 yanchor 1.0
        block:
            linear 0.4 zoom 0.95
            linear 0.6 zoom 1.05
            repeat
            
    transform cloud_shuffle2:
        zoom 1.0
        block:
            linear 0.5 zoom 1.04
            linear 0.3 zoom 1.0
            linear 0.3 zoom 0.94
            repeat
        
    transform cloud_shuffle3:
        zoom 1.0 yanchor 1.0
        block:
            linear 0.4 zoom 1.05
            linear 0.45 zoom 0.95
            linear 0.3 zoom 1.02
            repeat
        
    transform cloud_shuffle4:
        zoom 1.0 xanchor 1.0 yanchor 0.0
        block:
            linear 0.5 zoom 1.05
            linear 0.5 zoom 0.95
            repeat            
            
    transform cloud_shuffle5:
        zoom 1.0
        block:
            linear 0.45 zoom 1.05
            linear 0.65 zoom 0.95
            repeat
            
            
    # A solution for the odd animation issues surrounding
    # the chip bag; this hides the clouds after 2 seconds
    transform hide_dissolve:
            alpha 1.0
            linear 2.0 alpha 1.0
            linear 0.5 alpha 0.0
            
            
    #***********************************
    # Other Transforms
    #***********************************            
        
    # Used to display the chatroom speed message
    transform speed_msg:
        alpha 1
        0.4
        linear 0.4 alpha 0
        
    # Shows the heart icon
    transform heart:
        alpha 0.3
        xalign 0.3 yalign 0.3
        alignaround (.5, .55)
        linear 0.6 xalign .4 yalign .6 clockwise circles 0 alpha 1
        linear 0.02 alpha 0 xalign .35 yalign .55
           
           
    # The heartbreak icon
    transform heartbreak(wait_time):
        alpha 0.0
        pause wait_time
        alpha 0.7
        align (0.5, 0.5)
        zoom 2.0
        pause 0.12
        alpha 0    
    
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
        repeat
        
    # For timed menus
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
            
    # Makes the profile pictures bigger for the
    # profile picture page
    transform profile_zoom:
        zoom 2.85
        xalign 0.1
        yalign 0.675
        
    transform text_zoom:
        zoom 1.15
        
    # Scrolls the title of chatrooms that are too long
    transform chat_title_scroll:
        pause 3.5
        linear 5.0 xalign 1.0 xoffset -420
        xalign 0.0 xoffset 0
        repeat
        
    # Shuffles the participants list on a chatroom so you can
    # see all the participants
    transform participant_scroll:
        pause 3.5
        linear 2.0 xalign 1.0
        pause 3.5
        linear 2.0 xalign 0.0
        repeat
        
    transform null_anim:
        pass
        
    transform delayed_blink2(delay, cycle):
        alpha 0.0

        pause delay

        block:
            linear .2 alpha 1.0
            pause .2
            linear (cycle - .6) alpha 0.0
            pause .4
            repeat