label talk_to_lisa:
    "(This action will have consequences.)"

    jh "Hey ladies, can I talk to Lisa one-on-one for now?"

    lh "YOU JUST FAINTED AND THE FIRST PERSON U WANT TO TALK TO IS YOUR COUSIN AND MAIN COMPETITOR!?"

    ah "Alright Jensen, but don't you dare forget to send those GPU blueprints~"

    lh "!!"

    lh "Take your hands off me, you Chinese spy!"

    "Alice drags Lori out of the room."

    hide alice
    hide lori

    jh "So..., can you hire me as AMD's vice president?"

    ls "W-what?? You as vice president? But the Board..."

    jh "It's okay, I bribed a few underpaid software engineers in your company to vote for such a decision."

    ls "..."

    ls "You know what? Fine."

    ls "However, I have one condition:"

    ls "You will serve as my personal slave, and will be subject to physical violence at will."

    jh "...Say what now?"

    ls "These labour laws prevent me from beating up my lazy employees!"

    ls "Isn't that ridiculous?!"

    ls "You need a job, and I need someone to take my anger out on."

    ls "So, do we have a deal?"

    jh "..."

    jh "Well, Lori used to beat me up back in the day and I kinda liked it..."

    ls "..."

    ls "I'm sorry, what did you just-"

    jh "I accept."

    "You shake your flabbergasted cousin's limp hand."

    jh "See you on Monday!"

    scene amd hq at fullscreen_cover with fade

    "(Time Skip)"

    jh "Ahh, it feels so good to make boatloads of money again!"

    jh "Glory to nepotism!"

    ls "Yeah, yeah. Now get back to work, you womanizer!"

    "Lisa proceeds to stomp on your foot."

    jh "OW!"

    "(You try to contain your excitement. She mustn't know you enjoy this.)"

    call end_scene from _call_end_scene
    return

label talk_to_lori:

    jh "Hey ladies, can I talk to my wife, er, ex-wife in a one-on-one conversation?"

    ls "Of course. Make sure you get well soon."

    "Lisa exits the room."

    hide lisa

    ah "Alright, but don't forget about those GPU blueprints as promised!"

    "Alice gives you a wink on her way out."

    hide alice

    jh "I'm sorry, Lori."

    lh "You oughtta be! Do you know how sad I was knowing that MY HUSBAND OF 40 YEARS CHEATED ON ME WITH 2 OTHER WOMEN??"

    jh "It was 3 actually..."

    lh "What was that?"

    jh "N-nothing! Anyways, I really do regret my actions, so even if you dont love me anymore..." 
    
    jh "I hope that we can, at the very least, part on good terms."

    "Awkward silence."

    lh "Sure, Jensen." 
    
    lh "I've known u since our university days, and I know you do dumb stuff all the time." 
    
    lh "Nevertheless, what you did this time was unforgivable..."
    
    lh "So, we cant be together again."

    jh "(nod)"
    
    jh "I respect your decision. Thanks, Lori."

    "Lori tears up and cries."

    lh "I'm gonna miss you, Jensen. I wish you the best of luck for whatever path you choose from this point onward."

    "You walk away, waving goodbye to your former wife of 40 years."

    scene nvidia hq at fullscreen_cover with fade

    "(Time Skip)"

    "You managed to reclaim your position as CEO of Nvidia with the help of your loyal workers."

    call end_scene from _call_end_scene_1
    return

label talk_to_alice:

    jh "Hey ladies, can I talk to Alice in a one-on-one?"

    lh "Y-you just fainted, and the first person you want to talk to is the DAMN CHINESE SPY?!"

    ls "C'mon Lori, we should let him clear things up with her."

    "Lisa drags a reluctant Lori out of the room."

    hide lisa
    hide lori

    ah "So, about those GPU blueprints..."

    "Should I hand the blueprints over?"
    menu:
        "Hand blueprints over":
            call hand_over_blueprints_true from _call_hand_over_blueprints_true
        "Don't hand blueprints over":
            call hand_over_blueprints_false from _call_hand_over_blueprints_false
    return

label hand_over_blueprints_true:
    jh "I'm a man of my word. I'll send them over tonight."
    
    jh "It's not like I have anything to lose, anyway..."

    ah "Good choice."
    
    ah "Also, if you wish to continue being a leader in the AI industry, I could pull some strings for you to be CEO of Moonshot AI."

    jh "The company that owns Kimi?"

    ah "That's right."

    "Accept or Decline?"

    menu:
        "Accept":
            call moonshot_ai_accept from _call_moonshot_ai_accept
        "Decline":
            call moonshot_ai_decline from _call_moonshot_ai_decline
    return

label hand_over_blueprints_false:
    ah "Oh well. I'm sorry it had to end this way."

    jh "W-what do you mean?"

    ah "You're too dangerous to be kept alive."

    "Alice takes out a loaded pistol from her pocket."

    jh "Wait, wait please-"

    "Alice pulls the trigger."

    call end_scene from _call_end_scene_2
    return

label moonshot_ai_accept:
    jh "I accept."

    scene beijing at fullscreen_cover with fade

    "(Time skip)"

    "You are the new CEO of Moonshot AI."
    
    "You are tight with Xi Jinping, while your relationship with Donald Trump has deteriorated."
    
    call end_scene from _call_end_scene_3
    return

label moonshot_ai_decline:
    call hand_over_blueprints_false from _call_hand_over_blueprints_false_1
    return

label end_scene:
    "The End!"
    
    "Thank You for Playing!"
    return