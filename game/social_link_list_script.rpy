# Mam wrażenie, że moja więź z Iwai staje się jeszcze głębsza.
# Poziom twojej więzi z Wisielcem wzrósł do rangi 9.


default social_links = {
    "burmistrz": {

        "name": "Burmistrz",
        "title": "Strażnik Republiki",
        "portrait": "images/social/burmistrz.png",
        
        "background_color": "#151515",

        "known": True,

        "rank": 1,

        "max_rank": 2,

        "description": "”Poprosił” mnie o pomoc przy rozmieszczeniu ochotniczej straży pożarnej. Choć słowo ”poprosił” raczej nie oddaje faktycznego stanu rzeczy...",

        "show_meeting": True,

        "location": "Plac Budowy",
        "time": "06:00 - 18:00"
    },

    "zyd": {

        "name": "Żyd",
        "title": "Starozakonny",
        "portrait": "images/social/zyd.png",
        
        "background_color": "#151515",

        "known": True,

        "rank": 1,

        "max_rank": 4,

        "description": "Po akcji z Braunem poprosił mnie o pomoc z pewną sprawą...",

        "show_meeting": True,

        "location": "Cmentarz Żydowski",
        "time": "06:00 - 20:00"
    },

}

init python:

    def lighten_color(hex_color, amount=30):

        hex_color = hex_color.lstrip("#")

        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        r = min(255, r + amount)
        g = min(255, g + amount)
        b = min(255, b + amount)

        return "#{:02x}{:02x}{:02x}".format(r, g, b)


    def portrait_color(hex_color):

        return lighten_color(hex_color, 15)

# ============================================================
# SOCIAL LINKS - SCREEN
# ============================================================

screen social_links():

    modal True

    zorder 200


    # ========================================================
    # TŁO
    # ========================================================

    add Solid("#080808")


    # ========================================================
    # NAGŁÓWEK
    # ========================================================

    text "WIĘZI":

        xpos 90
        ypos 55

        size 64
        bold True

        color "#ffffff"


    # LICZNIK ZNANYCH POSTACI

    $ known_count = sum(
        1 for character in social_links.values()
        if character["known"]
    )

    text "[known_count]":

        xpos 1720
        ypos 70

        size 24

        color "#888888"


    # ========================================================
    # LISTA POSTACI
    # ========================================================

    viewport:

        xpos 80
        ypos 160

        xsize 1760
        ysize 820

        mousewheel True
        draggable True


        vbox:

            spacing 18


            # ------------------------------------------------
            # POSTACIE
            # ------------------------------------------------

            for id, character in social_links.items():

                # JEŚLI POSTAĆ NIE JEST ZNANA,
                # CAŁKOWICIE POMIJAMY JĄ

                if character["known"]:

                    button:

                        xsize 1700
                        ysize 185

                        background Solid(character["background_color"])
                        hover_background Solid(
                            lighten_color(character["background_color"], 30)
                        )

                        action NullAction()

                        fixed:

                            # =================================
                            # PORTRET
                            # =================================

                            frame:

                                xpos 25
                                ypos 15

                                xsize 170
                                ysize 170

                                yoffset -13
                                xoffset -4

                                background Solid(
                                    portrait_color(character["background_color"])
                                )

                                if renpy.loadable(character["portrait"]):

                                    add character["portrait"]:

                                        xsize 160
                                        ysize 160


                            # =================================
                            # INFORMACJE O POSTACI
                            # =================================

                            vbox:

                                xpos 200
                                ypos 30

                                xsize 1480

                                spacing 4

                                yoffset -28
                                xoffset 4

                                text character["name"]:

                                    size 32
                                    bold True
                                    color "#ffffff"

                                text character["title"]:

                                    size 19
                                    color "#888888"

                                null height 8

                                hbox:

                                    spacing 3

                                    for i in range(1, character["max_rank"] + 1):

                                        if i <= character["rank"]:

                                            text "★":
                                                size 25
                                                color "#ffffff"

                                        else:

                                            text "☆":
                                                size 25
                                                color "#555555"

                                null height 8

                                text character["description"]:

                                    size 18
                                    color "#cccccc"


                            # =================================
                            # NASTĘPNE SPOTKANIE
                            # =================================

                            if character["show_meeting"]:

                                vbox:

                                    xpos 1470
                                    ypos 25

                                    xsize 350

                                    spacing 5

                                    yoffset -10

                                    text "NASTĘPNE SPOTKANIE":

                                        size 14
                                        bold True
                                        color "#777777"

                                    text "📍 [character['location']]":

                                        size 18
                                        color "#ffffff"

                                    text "🕐 [character['time']]":

                                        size 18
                                        color "#ffffff"


    # ========================================================
    # ZAMKNIĘCIE
    # ========================================================

    text "B  —  ZAMKNIJ":

        xpos 90
        ypos 1010

        size 18

        color "#777777"


    # ========================================================
    # KLAWISZ B
    # ========================================================

    key "b" action Hide("social_links")


# ============================================================
# OTWIERANIE SOCIAL LINKÓW
# ============================================================

screen social_links_key():

    key "b" action Show("social_links")


init python:

    config.overlay_screens.append("social_links_key")