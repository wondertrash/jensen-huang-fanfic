# [ TRANSFORMS ]

transform active_speaker:
    ease 0.2 matrixcolor BrightnessMatrix(0.0) zoom 1.02

transform dim_speaker:
    ease 0.2 matrixcolor BrightnessMatrix(-0.25) zoom 1.00

transform fullscreen_cover:
    xysize (1920, 1080)
    fit "cover"
    align (0.5, 0.5)

# [ SHOW CALLBACK ]

init python:
    characters = ["jensen", "lisa", "alice", "lori", "dd"]

    positions = {
        "jensen": center,
        "lisa": left,
        "alice": right,
        "lori": Position(xalign=0.27, yalign=0.75),
        "dd": right,
    }

    def speak_callback(event, interact=True, **kwargs):
        if event == "begin" and interact:
            speaker = renpy.get_say_image_tag()

            if speaker and not renpy.showing(speaker):
                pos = positions.get(speaker, center)
                renpy.show(speaker, at_list=[pos])
                renpy.with_statement(dissolve)

            for tag in characters:
                if renpy.showing(tag):
                    if tag == speaker:
                        renpy.show(tag, at_list=[active_speaker], zorder=10)
                    else:
                        renpy.show(tag, at_list=[dim_speaker], zorder=1)

# [ CHARACTERS ]

define jh = Character("Jensen Huang", color="#52B788", image="jensen", callback=speak_callback)
define ls = Character("Lisa Su", color="#FF9F1C", image="lisa", callback=speak_callback)
define ah = Character("Alice Huang", color="#FF595E", image="alice", callback=speak_callback)
define lh = Character("Lori Huang", color="#4CC9F0", image="lori", callback=speak_callback)
define dd = Character("Drug Dealer", color="#AAAAAA", image="dd", callback=speak_callback)

# [ IMAGE ]

image lisa:
    "lisa.png"
    zoom 0.25

# [ POSITIONS ]

define far_left = Position(xalign=0.1, yalign=1.0)
define mid_left = Position(xalign=0.35, yalign=1.0)
define mid_right = Position(xalign=0.65, yalign=1.0) # show x smile at y
define far_right = Position(xalign=0.9, yalign=1.0)

# [ STORY TRACKERS ]

default result_wife = 0

# [ CUSTOM SCREENS ]

image black = "#000000"
