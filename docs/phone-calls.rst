===========
Phone Calls
===========

.. toctree::
    :caption: Navigation

    phone-calls


Creating a Regular Phone Call
=============================

.. note::
    Example files to look at:

    * tutorial_5_coffee.rpy
    * tutorial_11_story_call.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a label + the correct suffix for the phone call.

        #. ``my_label_outgoing_ja`` to make an outgoing call to the character ``ja`` available.
        #. ``my_label_incoming_ja`` to trigger an incoming call from the character ``ja`` after the corresponding timeline item has been played.
        #. ``my_label_story_call_ja`` to create a required Story Call after this timeline item from the character ``ja``.

    #. Write the phone call dialogue.
    #. End the phone call with ``return``

Phone calls that are tied to a particular timeline item follow a specific naming convention so the program can find them and make them available to the player. If you have a timeline item (i.e. a chatroom, Story Mode section, or Story Call) titled

::

    label day_1_4:

then an **incoming** call should be named::

    label day_1_4_incoming_z:

an **outgoing** call should be named::

    label day_1_4_outgoing_z:

and an attached Story Call should be named::

    label day_1_4_story_call_z:

where ``z`` is the variable of the character whom the player is calling or who is calling the player (see :ref:`Creating Characters` for a list of the existing characters).

The following section will cover **incoming** and **outgoing** calls to characters that are optional for continuing with the story. You can find more information on Story Calls at :ref:`Story Calls`.

Incoming Calls
--------------

Once the player is done playing through a timeline item, the program will automatically make any calls associated with that timeline item (through the naming convention mentioned above) available. If the program finds an **incoming call** label, then when the player finishes the timeline item they will receive an incoming call from the associated character. They have ten seconds to pick the phone call up, or they can reject the call and phone the character back later.

.. note::
    There can only be one incoming phone call after a given timeline item. However, it is possible to have both an incoming call after a chatroom as well as a different incoming call after an attached Story Mode.

**If the player rejects the incoming call** or lets the timer run out without answering it, it acts like an **outgoing** call and the player can phone the character back. The player can typically play one additional timeline item before the phone call "expires" and they cannot call the character back to receive that conversation.

Outgoing Calls
--------------

Once a player finishes playing through an item that has associated outgoing calls (linked through the naming conventions mentioned above), all the associated outgoing calls will be made available. The player must then click on the characters in their Contacts list or use the redial button next to a past phone call on the History tab to call the character.

An outgoing call is typically available immediately after its associated timeline item and for one additional timeline item following when it became available, after which it will "expire" and the player will be unable to view that conversation by calling the character.

.. note::
    There can be up to one outgoing call per character available after each timeline item. If a player misses an incoming call from a character who also has an outgoing call, both conversations will be added to the pool of available calls. The player can then call the character back multiple times to receive both conversations.

Missed Calls
------------

If the timer on an incoming phone call runs out, the phone call will be marked as "missed" and moved to the pool of available calls. The player can then call the character back to receive that conversation.

Phone calls can also be missed if real-time mode is turned on from the Developer settings. If an incoming call is scheduled to occur after a chatroom at 10:20 and the player opens the game after a new chatroom became available at 13:30, then they will receive a notification of a missed call at 13:30 (just before the new chatroom). If not too much time has passed since the missed call, they can then phone the character back to receive that conversation.

Additionally, if the player is using the game but has not yet played the 10:20 chatroom by 13:30, then if the game is open at 13:30 they will receive an incoming call which they can either accept or reject. This acts the same way as if the incoming call had been received immediately after playing the chatroom.


Creating a Story Call
=====================

Mysterious Messenger also includes "story calls", phone calls from the characters which the player must see before they can continue with the story. Story calls can be standalone, appearing on the timeline as their own story with a trigger time, or they can be attached to chatrooms or standalone story mode items as well and played after the main/parent timeline item is complete.

To create a standalone story call, see :ref:`Story Calls`. Otherwise, the program will automatically create a story call if a certain naming convention is used. If the label of the parent item (i.e. a chatroom or standalone story mode) is ``newyear_4_2``, then you can create a label with the suffix ``_story_call_`` + the file_id of the character who will be calling the player e.g.

::

    label newyear_4_2_story_call_ja:
        # This is a label for a story call from the character ja

Unlike story mode labels, there is no "generic" story call; all story calls must come from a particular character who will be calling the player.

.. tip::
    If you want to hide the identity of the caller, you can create a special "Anonymous" ChatCharacter whose file_id you can use for the story call label.

Story calls, like chatrooms, can also expire if the player is playing in real-time or if they hang up in the middle of the call. Expired story calls are treated as though the caller left the player a voicemail. As with chatrooms, the expired version of the story call is found at the name of the original story call label + ``_expired``::

    label newyear_4_2_story_call_ja_expired:
        # The expired version of the phone call

A player who misses a story call or hangs up in the middle of it will either be able to play the expired version to continue the story, or can "buy back" the story call to experience the participated version.

Story call dialogue is written the same way as regular phone calls.


Writing a Phone Call
====================

Phone call dialogue uses the regular character variables and doesn't have any special arguments such as ``(img=True)`` or special fonts. Just use the character variable and write out dialogue in quotations e.g.

::

    label day_1_4_incoming_z:
        z "Hi, [name]! This is phone call dialogue."
        z "You write it like this."
        return


Phone call labels end with ``return`` like all other labels.

You may also find Ren'Py's "monologue mode" helpful, since you won't be switching between expressions or different speakers very often. See ``tutorial_5_coffee.rpy`` for an example of this.


Providing Choices
=================

Menus for phone calls are written very similarly to menus in other parts of the game::

    menu:
        extend ''
        "I love cats.":
            ju "I do as well."
        "I like dogs better.":
            ju "Hmm. I will respectfully disagree with your opinion."

The only notable difference is that you should include the line ``extend ''`` right after the ``menu:`` statement and before the first choice. This will keep the dialogue said just before the menu on-screen while the choices are visible.

This menu, like others, also takes a ``paraphrased`` argument for either the menu as a whole or for an individual choice. For more information, see :ref:`Paraphrased Choices`.

Note also that if you are writing out the main character's dialogue directly after a choice, the first line **does not** require a ``(pauseVal=0)`` clause.

Changing a Character's Voicemail
================================

If the program determines there are no phone calls available for a character when the player phones them, it will automatically play the character's voicemail instead. You can change the character's voicemail whenever you like during a route.

To update a character's voicemail, use::

    $ ja.voicemail = "voicemail_1"

where ``ja`` is the variable of the character whose voicemail you're changing, and ``voicemail_1`` is the name of the label where the voicemail can be found. The default voicemail, "voicemail_1", can be found in ``01_mysme_engine/phonecall_system.rpy``.

Voicemails are written the same way as regular phone calls, though there are no restrictions on what a voicemail label can be called (but it's recommended you pick a descriptive name for it, probably including the word "voicemail").

You can use a character to say voicemail dialogue, or you can use the "generic" voicemail character, ``vmail_phone`` to say dialogue e.g.

::

    label voicemail_1():
        voice "voice files/voicemail_1.mp3"
        vmail_phone "The person you have called is unavailable right now. Please leave a message at the tone or try again."
        return

As shown above, you can also add voice files to the voicemail, which will be played during the next line of dialogue.

