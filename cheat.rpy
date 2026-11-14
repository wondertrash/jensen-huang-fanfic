# 1. Define characters and colors
define a = Character("Alex", color="#4cc9f0")
define m = Character("Morgan", color="#f72585")

# 2. Initialize variables (automatically saved/loaded with game saves)
default trust = 0
default has_flashdrive = False

# 3. Entry point of your game
label start:
    # Backgrounds & Music (files go in game/images/ and game/audio/)
    scene bg office_night with fade
    play music "synth_loop.ogg" fadein 1.5

    # Sprites (image named 'alex worried.png' is called with 'show alex worried')
    show alex worried at left with dissolve
    a "You're late. Did you get the drive?"

    # Player Choices (just like branching conditions)
    menu:
        "Hand over the flash drive.":
            $ trust += 1
            $ has_flashdrive = True
            play sound "item_pickup.wav"
            show alex happy at left
            a "Good work. I knew I could count on you."x

        "Lie and say you lost it.":
            $ trust -= 1
            show alex angry at left with hpunch  # 'hpunch' shakes the screen
            a "Are you serious right now?"

    # Standard Python conditionals
    if trust > 0:
        jump secret_ending
    else:
        jump bad_ending

label secret_ending:
    "You unlocked the good path!"
    return  # Ends the game and returns to main menu

label bad_ending:
    "Game Over."
    return