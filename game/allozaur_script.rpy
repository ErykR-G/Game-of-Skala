default allozaur_jedzenie = 0
label allozaur:
    label allozaur1:
        scene bg poludnie2 with fade
        play music "audio/music/dinozaur.mp3"
        show luszcz neutral at left

        if allozaur_social_link == 0:
            $ allozaur_social_link = 1
            luszcz "O muj borze czy to!!! Allozaur???"

            allozaur "Raaawr"

            luszcz "Muszę się z nim koniecznie zaprzyjaźnić."
            luszcz "Co jedzą allozaury…?"

            menu:
                "{b}Stypa{/b}":
                    luszcz "Ale siara nie mam nic dla niego."
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna

                "{b}Dinozaur{/b}" if dinozaur == 1:
                    $ allozaur_jedzenie += 1
                    luszcz "Cip Cip!!"

                    allozaur "???"

                    luszcz "Łap!"

                    $ dinozaur = 0
                    $ ile_item_fabularne -= 1
                    "{i}Łuszcz rzuca dinozarła{/i}"

                    allozaur "!!!"

                    "{i}Allozaur zjada dinozarła{/i}"

                    allozaur "Mniam mniam mniam"
                    allozaur "Przepyszne."

                    luszcz "Hel jes."

                    "{i}Allozaur kopie w ziemi{/i}"
                    "{i}Allozaur wykopuje łopatkę{/i}"
                    "{i}Allozaur daje ci łopatkę{/i}"

                    $ ile_item_fabularne += 1
                    $ lopatka = 1

                    "{i}*Łopatka została dodana do ekwipunku*{/i}" 

                    luszcz "Dziękuję ci Allozaurze."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna

                "{b}Kremówka{/b}" if kremowka == 1:
                    luszcz "Wszyscy kochają kremówki."

                    "{i}Łuszczu zamachuje się do rzutu{/i}"

                    luszcz "iiii… rzut!"
                    $ kremowka = 0
                    $ ile_item_fabularne -= 1

                    show kremowka at slightleft
                    "{i}Nagle! Kremuwka zamiast polecieć do allozaura zaczęła dryfować w powietrzu{/i}"

                    luszcz "Ej!!! Kremówko!!! Wracaj tu!!!"

                    menu:
                        "{b}Biegnij za kremówką{/b}":
                            play music "audio/music/run.mp3"
                            show kremowka:
                                xalign 0.25
                                yalign 1.0
                                easeout 0.4 xalign 1.5

                            show luszcz neutral at center:
                                xalign 0.0
                                yalign 1.0
                                easeout 0.8 xalign 1.5
                            
                            $ renpy.pause(0.8)
                            
                            scene bg minecraft1

                            show kremowka:
                                xalign -0.5
                                yalign 1.0
                                easeout 0.6 xalign 1.5
                            
                            $ renpy.pause(0.3)
                            
                            show luszcz neutral at center:
                                xalign -0.5
                                yalign 1.0
                                easeout 0.4 xalign 0.5
                            
                            $ renpy.pause(0.4)
                            luszcz "Ile to morze lecieć!! HALO!!!!!! Zapracowałem na tą kremuwkę!!!"

                            show luszcz neutral at center:
                                xalign 0.5
                                yalign 1.0
                                easeout 0.4 xalign 1.5
                            
                            $ renpy.pause(0.4)

                            scene bg minecraft2

                            show kremowka 2 at right
                            $ renpy.pause(0.3)

                            show luszcz neutral at center:
                                xalign -0.5
                                yalign 1.0
                                easeout 0.2 xalign 0.25

                            luszcz "Ufff… Ah… Jezu."
                            luszcz "I co, warto było?"

                            hide kremowka
                            show papaj at right
                            play music "audio/music/barka.mp3"
                            papaj "Kremówka wzywa."
                            papaj "Więc zstąpił duch mój."
                            papaj "Jak się nazywasz, wybrany chłopcze?"

                            luszcz "Maciej Łuszcz"

                            papaj "Macieju, ziemia, po której stąpasz, miała kiedyś styczność z moimi nagimi stopami."
                            papaj "Czy to nie cudowne, Macieju?"
                            papaj "Czy to nie piękne?"

                            luszcz "Jeszcze jak."

                            papaj "Każdy wojownik w potrzebie zostaje tu przyprowadzony przez moje kremówki."
                            papaj "Możesz teraz wziąć kawałek tej ziemi i użyć go jako zbroję"
                            papaj "Nie daj się zwyciężyć złu, ale zło dobrem zwyciężaj."
                            papaj "Żegnaj, Łuszczu."

                            hide papaj

                            luszcz "Nienawidzę gdy to robi."
                            luszcz "Ale wziąć trochę ziemi nie zaszkodzi."

                            $ ziemia = 1

                            "{i}*Kawałek ziemi po której stąpał jp2 został dodany do ekwipunku*{/i}" 

                            luszcz "A teraz spowrotem."
                            
                            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                play music "audio/music/pole.mp3"
                            else:
                                play music "audio/music/pole_noc.mp3"
                            jump sloneczna
                        
                        "{b}Pożegnaj się z kremówką{/b}":
                            luszcz "Uszanuję twoją wolność kremówko…"
                            luszcz "Rzegnaj…"
                            show kremowka:
                                xalign 0.25
                                yalign 1.0
                                easeout 0.4 xalign 1.5

                            luszcz "To jednak allozaur nic nie dostanie."
                            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                play music "audio/music/pole.mp3"
                            else:
                                play music "audio/music/pole_noc.mp3"
                            jump sloneczna
        
        else:
            if allozaur_jedzenie == 2:
                luszcz "Witaj Allozaurze"

                allozaur "Raaawr"
                menu:
                    "{b}Pogłaskaj Allozaura{/b}":
                        "{i}Allozaur mruczeniem docenia głaskanie{/i}"
                        "{i}Chyba nic tutaj więcej nie zrobię...{/i}"
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        jump sloneczna

            
            else:
                luszcz "Witaj Allozaurze"

                allozaur "Raaawr"

                luszcz "Przyszedłem ciebie nakarmic."
                luszcz "Co by ci tu dać…?"

                menu:
                    "{b}Stypa{/b}":
                        luszcz "Ale siara nie mam jednak nic dla ciebie."
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        jump sloneczna

                    "{b}Dinozaur{/b}" if dinozaur == 1:
                        $ allozaur_jedzenie += 1
                        luszcz "Cip Cip!!"

                        allozaur "???"

                        luszcz "Łap!"

                        $ dinozaur = 0
                        $ ile_item_fabularne -= 1
                        "{i}Łuszcz rzuca dinozarła{/i}"

                        allozaur "!!!"

                        "{i}Allozaur zjada dinozarła{/i}"

                        allozaur "Mniam mniam mniam"
                        allozaur "Przepyszne."

                        luszcz "Hel jes."

                        "{i}Allozaur kopie w ziemi{/i}"
                        "{i}Allozaur wykopuje łopatkę{/i}"
                        "{i}Allozaur daje ci łopatkę{/i}"

                        $ ile_item_fabularne += 1
                        $ lopatka = 1

                        "{i}*Łopatka została dodana do ekwipunku*{/i}" 

                        luszcz "Dziękuję ci Allozaurze."

                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        jump sloneczna

                    "{b}Kremówka{/b}" if kremowka == 1:
                        luszcz "Wszyscy kochają kremówki."

                        "{i}Łuszczu zamachuje się do rzutu{/i}"

                        luszcz "iiii… rzut!"
                        $ kremowka = 0
                        $ ile_item_fabularne -= 1

                        show kremowka at slightleft
                        "{i}Nagle! Kremuwka zamiast polecieć do allozaura zaczęła dryfować w powietrzu{/i}"

                        luszcz "Ej!!! Kremówko!!! Wracaj tu!!!"

                        menu:
                            "{b}Biegnij za kremówką{/b}":
                                play music "audio/music/run.mp3"
                                show kremowka:
                                    xalign 0.25
                                    yalign 1.0
                                    easeout 0.4 xalign 1.5

                                show luszcz neutral at center:
                                    xalign 0.0
                                    yalign 1.0
                                    easeout 0.8 xalign 1.5
                                
                                $ renpy.pause(0.8)
                                
                                scene bg minecraft1

                                show kremowka:
                                    xalign -0.5
                                    yalign 1.0
                                    easeout 0.6 xalign 1.5
                                
                                $ renpy.pause(0.3)
                                
                                show luszcz neutral at center:
                                    xalign -0.5
                                    yalign 1.0
                                    easeout 0.4 xalign 0.5
                                
                                $ renpy.pause(0.4)
                                luszcz "Ile to morze lecieć!! HALO!!!!!! Zapracowałem na tą kremuwkę!!!"

                                show luszcz neutral at center:
                                    xalign 0.5
                                    yalign 1.0
                                    easeout 0.4 xalign 1.5
                                
                                $ renpy.pause(0.4)

                                scene bg minecraft2

                                show kremowka 2 at right
                                $ renpy.pause(0.3)

                                show luszcz neutral at center:
                                    xalign -0.5
                                    yalign 1.0
                                    easeout 0.2 xalign 0.25

                                luszcz "Ufff… Ah… Jezu."
                                luszcz "I co, warto było?"

                                hide kremowka
                                show papaj at right
                                play music "audio/music/barka.mp3"
                                papaj "Kremówka wzywa."
                                papaj "Więc zstąpił duch mój."
                                papaj "Jak się nazywasz, wybrany chłopcze?"

                                luszcz "Maciej Łuszcz"

                                papaj "Macieju, ziemia, po której stąpasz, miała kiedyś styczność z moimi nagimi stopami."
                                papaj "Czy to nie cudowne, Macieju?"
                                papaj "Czy to nie piękne?"

                                luszcz "Jeszcze jak."

                                papaj "Każdy wojownik w potrzebie zostaje tu przyprowadzony przez moje kremówki."
                                papaj "Możesz teraz wziąć kawałek tej ziemi i użyć go jako zbroję"
                                papaj "Nie daj się zwyciężyć złu, ale zło dobrem zwyciężaj."
                                papaj "Żegnaj, Łuszczu."

                                hide papaj

                                luszcz "Nienawidzę gdy to robi."
                                luszcz "Ale wziąć trochę ziemi nie zaszkodzi."

                                $ ziemia = 1

                                "{i}*Kawałek ziemi po której stąpał jp2 został dodany do ekwipunku*{/i}" 

                                luszcz "A teraz spowrotem."
                                
                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                jump sloneczna
                            
                            "{b}Pożegnaj się z kremówką{/b}":
                                luszcz "Uszanuję twoją wolność kremówko…"
                                luszcz "Rzegnaj…"
                                show kremowka:
                                    xalign 0.25
                                    yalign 1.0
                                    easeout 0.4 xalign 1.5

                                luszcz "To jednak allozaur nic nie dostanie."
                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                jump sloneczna