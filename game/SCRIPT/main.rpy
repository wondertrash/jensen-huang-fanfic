label beginning:
    scene dark alley at fullscreen_cover with fade
    play music "ost.ogg"
    show jensen at center with dissolve

    "You have recently been divorced by your wife and kicked out of your mansion."

    "Your CEO position at Nvidia has been stripped away."

    "You lost half your money after your cheating on your faithful wife with Alice Huang."

    "You wander in a dark alley, ashamed of your actions."

    dd "Hey man, you look down. Take this and relax, free of charge."

    dd "(Hands you a suspicious red potion)"

    jh "Um... what is this?"

    dd "Just a little experiment I've been working on. Safe to say, it will turn ur life around, for better or for worse."

    jh "Well, my life can't get much worse..."

    jh "(Drinks red potion)"

    "You fall unconscious and drop to the floor."

    "The suspicious drug dealer quickly flees the scene."

    hide dd

    scene hospital at fullscreen_cover with fade

    play music "ost.ogg" if_changed

    "You wakes up in a delirious state."

    ls "Hey Jensen, I know you're going through a rough time right now, so I'll take care of you for the forseeable future."

    jh "How long was I out?"

    ls "For about half a day. I saw you lying on the ground in a dark alley, so I immediately dialed the emergency hotline."

    jh "I see. Thank y-"

    "Your ex-wife barges in the room."

    lh "JENSEN! I leave you alone for a SINGLE day and I come back to my ex-husband half-dead??"

    jh "Wow, you still care so much about me? :)"

    lh "Erm, well... i-it's not like I still like you or anything! Hmph!"

    "Alice Huang enters the room."

    lh "What on Earth is the Chinese spy doing here?!"

    ah "I'm here to collect Jensen's promised GPU designs."

    ls "I'm sorry, Jensen, but did you actually give up top-secret blueprints for..."

    jh "(I should change the subject before the three of them kill me. Figuratively, of course.)"

    "Talk to Lisa, Lori, or Alice?"

    menu:
        "Talk to Lisa":
            call talk_to_lisa from _call_talk_to_lisa

        "Talk to Lori":
            call talk_to_lori from _call_talk_to_lori
            
        "Talk to Alice":
            call talk_to_alice from _call_talk_to_alice
    return
    






