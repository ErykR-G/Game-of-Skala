define fight_on = 0
define eq_on = 0

screen global_eq_key():
    if fight_on == 0 and eq_on == 0:
        key "e" action Function(renpy.call_in_new_context, "eq")

screen clock():
    $ day, hour, minute = get_time(timer)

    $ days_of_week = ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"]
    $ day_name = days_of_week[(day - 1) % 7]

    frame:
        background "#0008"
        align (0.98, 0.02)

        vbox:
            xmaximum 90
            spacing 2
            text "[day_name]" size 18
            text "[hour:02d]:[minute:02d]" size 22

            frame:
                xfill True
                ysize 1
                background "#fff6"

            text "💰 [money]" size 18

    