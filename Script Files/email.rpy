init python:

    
    email_reply = False
    
    class Email(store.object):
        def __init__(self, guest, msg, reply_label, read=False, msg_num=0,
                        failed=False, timeout_count=25, deliver_reply="wait",
                        reply=False, timeout=False):
            self.guest = guest # Guest variable
            self.msg = msg  # Email content
            self.reply_label = reply_label  # Name of the label to jump to when replying
            self.read = read    # Read/Unread
            self.msg_num = msg_num  # = 0, 1, 2, or 3; reply number. 0 is the first message
                                      # sent to you, and 3 is the email accepting your invite
            self.failed = failed    # Whether or not the email chain has been failed
            self.timeout_count = timeout_count  # This is somewhat arbitrary; essentially if the
                                    # player doesn't respond within 25 chatrooms (~3 days; can
                                    # be changed) of receiving the message it will be failed
            self.deliver_reply = deliver_reply   # How long to wait before the guest replies to your email
                                            # This should equal "wait" if it's your turn to reply
            self.reply = reply   # This contains the message to be delivered when the guest replies to you
            self.timeout = timeout
            self.sent_time = upTime()
                                   
        def deliver(self):
            global email_list
            
            # If you're waiting on a reply, decrease the timer
            if self.deliver_reply != "wait":
                self.deliver_reply -= 1
                
            # If the timer <= 0 and there's a reply to be delivered, deliver it
            if self.deliver_reply != "wait" and self.deliver_reply <= 0 and self.reply:
                self.read = False
                self.reply += "\n\n------------------------------------------------\n\n"
                self.msg = self.reply + self.msg
                self.reply = False
                self.sent_time = upTime()
                self.timeout_count = 25 # Sets the timeout counter
                self.deliver_reply = "wait"
                email_list.remove(self)
                email_list.insert(0, self) # Moves to the front of the list
                
            # If it's your turn to reply, decrease the timeout counter,
            # Unless this is the final message and there's no need to reply
            if self.deliver_reply == "wait" and self.msg_num <= 2:
                self.timeout_count -= 1
                
            # If the timeout counter reaches 0, timeout becomes True
            if self.timeout_count == 0 and self.msg_num <= 2 and not self.failed:
                self.timeout = True
         
        # Sets the guest's reply and randomly decides when it should be delivered
        def set_reply(self, iscorrect, deliver_reply=False):
            if iscorrect:
                if self.msg_num == 0:                    
                    self.reply = self.guest.reply1_good
                    self.reply_label = self.guest.label2
                elif self.msg_num == 1:
                    self.reply = self.guest.reply2_good
                    self.reply_label = self.guest.label3
                elif self.msg_num == 2:
                    self.reply = self.guest.reply3_good
                    self.reply_label = False
                self.add_msg(True)
            else:
                if self.msg_num == 0:
                    self.reply = self.guest.reply1_bad
                elif self.msg_num == 1:
                    self.reply = self.guest.reply2_bad
                elif self.msg_num == 2:
                    self.reply = self.guest.reply3_bad
                self.add_msg(False)
                self.failed = True
                self.reply_label = False

            # If a number is given, the reply will be delivered within that many
            # chatrooms. Otherwise, it will be delivered within the next 5-16 chatrooms
            if deliver_reply != False:
                self.deliver_reply = deliver_reply
            else:
                self.deliver_reply = renpy.random.randint(5, 16)
                
            self.sent_time = upTime()
            self.timeout_count = 2
            renpy.retain_after_load()
                
        # Adds the player's message to the guest to the email
        def add_msg(self, iscorrect):        
            the_msg = ""
        
            if iscorrect:
                if self.msg_num == 0:
                    the_msg = self.guest.msg1_good
                elif self.msg_num == 1:
                    the_msg = self.guest.msg2_good
                elif self.msg_num == 2:
                    the_msg = self.guest.msg3_good
            else:
                if self.msg_num == 0:
                    the_msg = self.guest.msg1_bad
                elif self.msg_num == 1:
                    the_msg = self.guest.msg2_bad
                elif self.msg_num == 2:
                    the_msg = self.guest.msg3_bad
                    
            self.msg_num += 1
            the_msg += "\n\n------------------------------------------------\n\n"
            self.msg = the_msg + self.msg
            
        # Returns True if the email chain has been successfully completed
        def completed(self):
            if self.failed or not self.read:
                return False            
            if self.msg_num == 3 and self.reply == False:
                return True
            else:
                return False
                
        # Returns True if the email chain was failed
        def is_failed(self):
            if self.failed and self.read and not self.reply:
                return True
            else:
                return False
                
        # These next three functions determine the icon for the three
        # email icons under the sender's name
        def first_msg(self):
            if self.msg_num <= 0:
                return 'email_inactive'
            elif self.msg_num == 1 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
        
        def second_msg(self):
            if self.msg_num <= 1:
                return 'email_inactive'
            elif self.msg_num == 2 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
        
        def third_msg(self):
            if self.msg_num <= 2:
                return 'email_inactive'
            elif self.msg_num == 3 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
                
        # Sends the email reply
        def send_reply(self):
            global email_reply
            email_reply = True
            renpy.call_in_new_context(self.reply_label)
            email_reply = False
       
    ## This class stores necessary information about the guest, including
    ## all of their email replies as well as their image thumbnail and name
    class Guest(store.object):
        def __init__(self, name, pic, start_msg,
                        msg1_good, reply1_good, msg1_bad, reply1_bad,
                        msg2_good, reply2_good, msg2_bad, reply2_bad,
                        msg3_good, reply3_good, msg3_bad, reply3_bad):
            
            # msg_good means it's the correct reply for that message, and
            # reply_good is what the guest will send after that message
            # msg_bad is the incorrect reply; reply_bad is the same as above but for the bad message
            # name is a string of the name of the guest
            # start_msg is the initial message you are sent after agreeing to invite them
            # pic = sender's contact thumbnail, ideally 155x155
            
            self.name = name
            self.pic = pic
            
            self.start_msg = start_msg
            self.msg1_good = msg1_good
            self.msg2_good = msg2_good
            self.msg3_good = msg3_good
            
            self.reply1_good = reply1_good
            self.reply2_good = reply2_good
            self.reply3_good = reply3_good
            
            self.reply1_bad = reply1_bad
            self.reply2_bad = reply2_bad
            self.reply3_bad = reply3_bad
            
            self.msg1_bad = msg1_bad
            self.msg2_bad = msg2_bad
            self.msg3_bad = msg3_bad
            
            self.label1 = name + '_reply1'
            self.label2 = name + '_reply2'
            self.label3 = name + '_reply3'
                
            
    def unread_emails():
        global email_list
        unread = [ x for x in email_list if not x.read]
        return len(unread)
                
    def deliver_emails():
        global email_list
        for e in email_list:
            e.deliver()
                
                
default email_list = []
            
# The idea here is that if the user picks the option to invite
# this guest, you'll include a line `call invite(guest_var)` and
# it will trigger them to email you
label invite(guest):
    if not observing: # So you can't re-invite someone when replaying a chatroom
        $ guest.sent_time = upTime()
        $ email_list.insert(0, Email(guest, guest.start_msg, guest.label1)) # Moves them to the front of the list
    return
    
default current_email = None  

########################################################
## This screen shows a list of the emails you've 
## received
########################################################
screen email_hub:
    
    tag menu
        
    default current_page = 0
    default num_pages = (len(email_list) + 7 - 1) // 7
    
    use starry_night
    
    use menu_header('Email', Show('chat_home', Dissolve(0.5)))
    
    window:
        background 'left_corner_menu' padding(20,20)
        xysize (685, 1100)
        align (0.5, 0.75)
        has vbox
        spacing 40
        align (0.5, 0.0)
        null height -15
        
        if len(email_list) == 0:
            text "Inbox is empty" color '#fff' xalign 0.5 yalign 0.0
        for e in email_list[current_page*7:current_page*7+7]:      
            use email_button(e)
                
        
    hbox:
        align (0.5, 0.99)
        spacing 15
        imagebutton:
            idle im.Flip("Email/main03_email_next_button.png", horizontal=True)
            align (0.5, 0.5)
            if current_page > 0:
                action SetScreenVariable('current_page', current_page-1)     
            
        for index in range(num_pages):
            textbutton _(str(index+1)):
                text_color '#fff' 
                align (0.5, 0.5)
                action SetScreenVariable('current_page', index)
            
        imagebutton:
            idle "Email/main03_email_next_button.png"
            align (0.5, 0.5)
            if current_page < num_pages - 1:
                action SetScreenVariable('current_page', current_page+1)
            
########################################################  
## This shows the buttons you can click on in order to 
## open and read your emails   
########################################################
screen email_button(e):
    button:
        align (0.5, 0.5)
        if e.read:
            background 'email_panel'
        else:
            background 'email_mint'
            
        xysize (644, 111)
        hover_foreground 'white_transparent'
        action [SetVariable("current_email", e), SetField(e, 'read', True), Show('open_email', e=e)]
          
        hbox:
            align (0.0, 0.0)
            spacing 10
            fixed:
                xysize (80,111)
                align (0.5, 0.5)
                if not e.read:
                    add 'email_unread' align(1.0, 0.5)
                elif e.reply_label:
                    add 'email_read' align(1.0, 0.5)
                else:
                    add 'email_replied' align(1.0, 0.5)
            add Transform(e.guest.pic, zoom=0.61) align(0.5, 0.3)
            null width -10
            vbox:
                align(0.5, 0.4)
                spacing 15
                window:
                    align(0.0, 0.0)
                    xysize(190, 30)
                    text '@' + e.guest.name style 'email_address'
                hbox:
                    align(0.3, 0.5)
                    spacing 8
                    add e.first_msg()
                    add e.second_msg()
                    add e.third_msg()
            window:
                xysize(240,111)
                align (0.0, 0.0)
                if e.completed():
                    add 'email_completed' align(0.5, 0.5)
                elif e.is_failed():
                    add 'email_failed' align(0.5, 0.5)
                elif e.timeout:
                    add 'email_timeout' align(0.5, 0.5)
     
########################################################    
## This is the screen that displays the email you've 
## selected, and lets you reply
########################################################
screen open_email(e):
    modal True
    zorder 100
    
    add "Phone UI/choice_dark.png"
        
    window:
        maximum(685, 800)
        background 'left_corner_menu_dark' padding(20,20)
        align (0.5, 0.5)
        imagebutton:
            align (1.0, 0.0)
            xoffset 20
            yoffset -20
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('open_email')
            
        vbox:
            spacing 15
            align (0.0, 0.0)
            hbox:
                spacing 10
                align (0.0, 0.0)
                add e.guest.pic
                
                vbox:
                    align(0.0, 0.0)
                    spacing 10
                    fixed:
                        align (0.0, 0.0)
                        xsize 280
                        ysize 80
                        text 'From: ' + e.guest.name color '#fff'
                    text '[[Date] ' + e.sent_time.month_num + '/' + e.sent_time.day color '#fff' size 27
                    text '[[Time] ' + e.sent_time.twelve_hour + ':' + e.sent_time.minute + ' ' + e.sent_time.am_pm size 27 color '#fff'
                
                textbutton _('Reply'):
                    text_style 'mode_select'
                    align (0.5, 1.0)
                    xsize 170
                    ysize 70
                    text_size 28
                    background 'menu_select_btn' padding(20,20)
                    hover_background 'menu_select_btn_hover'
                    if e.reply_label and not e.reply and not e.timeout:
                        action e.send_reply
                    else:
                        foreground 'menu_select_btn_inactive'

            window:
                background 'email_open_transparent' padding(20,20)
                xysize (625, 585)
                align (0.5,0.5)
                viewport:
                    align (0.5, 0.5)
                    xysize (585, 545)
                    scrollbars 'vertical'
                    mousewheel True
                    draggable True
                    
                    text e.msg size 28
            



