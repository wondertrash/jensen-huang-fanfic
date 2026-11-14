label talk_to_lisa:
    #"Talk to Lisa"

    jh "Hey ladies, can I talk to Lisa one-on-one for now?"

    lh "YOU JUST FAINTED AND THE FIRST PERSON U WANT TO TALK TO IS YOUR COUSIN AND MAIN COMPETITOR!?"

    ah "Alright Jensen, but don't you dare forget to send those GPU blueprints~"

    lh "!!"

    lh "Take your hands off me, you Chinese spy!"

    "Alice drags Lori out of the room."

    jh "So, how are ur company doing, lisa?"

    ls "Oh... it's doing fine, I suppose. Is that all you wanted to ask?"
    
    jh "No, there was something else..."

    ls "Wait, your face is still a little dirty. Let me wipe that... ahh!"

    "Lisa trips on nothing and faceplants onto your tummy wummy."

    ls "Woah, your abs are so... prominent. (blushes)"

    jh "If you want more of this, you should hire me as AMD's vice president."

    ls "W-what?? You as vice president? But the Board..."

    jh "It's okay, I have supporters in your company who would vote for such a decision."

    jh "Besides... I've always admired you, Lisa."

    lh "...Same, Jensen."

    lh "You know, I've always been jealous of Nvidia's technological advancements in ray tracing and machine learning."

    lh "I know my company will profit from your affair, but still-"

    "You wrap your cool leather jacket around Lisa."

    ls "W-what is this?"

    jh "Lisa... I want to be with you. I've liked you ever since I found out we were related."

    jh "No one will find out about this. I've learned from my past mistakes, i swear."

    ls "Alright, I trust you."

    "You lean in for a kiss. Lisa does as well."

    scene amd hq at fullscreen_cover with fade

    "(Time Skip)"

    jh "Ahh, it feels so good to make boatloads of money again!"

    ls "So..., are we getting back to where we left off?"

label talk_to_lori:
    #"Talk to Lori"

    jh "Hey ladies, can I talk to my wife, er, ex-wife in a one-on-one conversation?"

    ls "Of course. Make sure you get well soon."

    "Lisa exits the room."

    ah "Alright, but don't forget about those GPU blueprints as promised!"

    "Alice gives you a wink on her way out."

    jh "I'm sorry, Lori."

    lh "You oughtta be! Do you know how sad I was knowing that MY HUSBAND OF 40 YEARS CHEATED ON ME WITH 2 OTHER WOMEN??"

    jh "(It was 3 actually...)"

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

    "You walk away, waving goodbye to your wife of 40 years."

    scene nvidia hq at fullscreen_cover with fade

    "(Time Skip)"

    "You managed to reclaim your position as CEO of Nvidia with the help of your loyal workers."

label talk_to_alice:
    #"Talk to Alice"

    jh "Hey ladies, can I talk to Alice in a one-on-one?"

    lh "Y-you just fainted, and the first person you want to talk to is the DAMN CHINESE SPY?!"

    ls "C'mon Lori, we should let him clear things up with her."

    "Lisa drags a reluctant Lori out of the room."

    ah "So, about those GPU blueprints..."

    "Should I hand the blueprints over or not? (This action will have consequences)"
    menu:
        "Hand blueprints over":
            call hand_over_blueprints_true
        "Don't hand blueprints over":
            call hand_over_blueprints_false 

label hand_over_blueprints_true:
    jh "I'm a man of my word. I'll send them over tonight."
    
    jh "It's not like I have anything to lose, anyway."

    ah "Good choice."
    
    ah "Also, if you wish to continue being a leader in the AI industry, I could pull some strings for you to be CEO of Moonshot AI."

    jh "The company that owns Kimi?"

    ah "That's right."

    "Accept or Decline? (This action will have consequences)"

    menu:
        "Accept":
            call moonshot_ai_accept
        "Decline":
            call moonshot_ai_decline

label hand_over_blueprints_false:
    ah "Oh well. I'm sorry it had to end this way."

    "Alice takes out a loaded pistol from her pocket."

    jh "Wait, wait please-"

    "Alice pulls the trigger."

label moonshot_ai_accept:
    jh "I accept."

    scene beijing at fullscreen_cover with fade

    "(Time skip)"

    "You are the new CEO of Moonshot AI."
    
    "You are tight with Xi Jinping, while your relationship with Donald Trump has deteriorated."

label moonshot_ai_decline:
    call hand_over_blueprints_false