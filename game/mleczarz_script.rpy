default krowko_limit = 0
label mleczarz:
    label mleczarz1:
        scene bg mleczarnia with fade
        play music "audio/music/mleczarnia.mp3"
        show luszcz neutral at left
        show mleczarz at slightright

        if mleczarz_social_link == 0:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            luszcz "Dzień Dobry, mógłbym może kupić trochę sławnych krówek? Mógłbym nimi dokonać haraczu."

            mleczarz "Nie. Wszystkie sprzedane."

            luszcz "Agh!!! Dzień jak codzień!"

            mleczarz "Możesz pracować. Dostarczyć krówki. Klienci zapłacą!"

            luszcz "Hm… w sumie, potrzebuję pieniędzy."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie na granicy. Wielki mur. Chyba."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 1:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie na Słonecznej. Różowy dom."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 2:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."
            mleczarz "Chcesz kremówkę?"

            menu:
                "{b}Tak{/b}":
                    luszcz "Zawsze"
                    mleczarz "masz"
                    $ ile_item_fabularne += 1
                    $ kremowka = 1
                    "{i}*Kremówka została dodana do ekwipunku*{/i}"
                
                "{b}Nie{/b}":
                    luszcz "Nie"
                    mleczarz "nie to nie."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie na Bohaterów Września. Czerwony dom."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 3:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie koło Parkingu. Stomatolog."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 4:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie koło Parkingu. Przyjdź nocą."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 5:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie koło podstawówki."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Do widzenia{/b}":
                    luszcz "Do widzenia."

                    mleczarz "Do widzenia."

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 6:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."
            mleczarz "Dziękuję, Maciej Łuszcz."
            mleczarz "Dostarczyłeś wszystkie moje krówki."
            mleczarz "Teraz ja mogę dostarczyć siebie."
            mleczarz "Na emeryturę."
            mleczarz "Dziękuję."
            mleczarz "Żegnaj."

            hide mleczarz

            luszcz "Będę tęsknić, kruwkomleczażu."
            $ mleczarz_social_link = 7
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska

    label mleczarz2:
        play music "audio/music/usa.mp3"
        show luszcz neutral zorder 15:
            xalign 0.6
            yalign 1.0

        show trump neutral zorder 16 at right
        luszcz "Dostawa krówek dla pana Trumpa!"

        $ krowka = 0

        trump "To są przepiękne, przepiękne krówki."
        trump "Mam nadzieję że zrobią dobrą robotę, jako klocki budowlane."
        trump "Ewentualnie, jako smakołyki dla pracowników."
        trump "Tu masz pieniądze."

        $ money += 2
        $ mleczarz_social_link = 1

        "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

        luszcz "Dziękuję do widzenia!"

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            play music "audio/music/pole.mp3"
        else:
            play music "audio/music/pole_noc.mp3"
        hide luszcz 
        hide trump 
        jump granica2
    
    label mleczarz3:
        scene bg musial with fade
        show luszcz neutral at left

        luszcz "*puk* *puk*"

        nikt "Kto tam?"

        luszcz "Dostawa krówek!"

        show musial neutral at slightright

        musial "Ah, no tak"

        $ krowka = 0

        musial "Pychotka, dziękuję"
        musial "Tutaj masz pieniądze"

        $ money += 2
        $ mleczarz_social_link = 2

        "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

        musial "Miłego dnia!"

        luszcz "Miłego dnia!"

        hide luszcz 
        hide musial 
        jump sloneczna

label mleczarz4:
        scene bg stomatolog with fade
        show luszcz neutral at left
        show tata neutral at slightright

        luszcz "Tata zamawiałeś krówki?"

        tata "Zamawiałem."

        $ krowka = 0

        tata "Czekaj, to ty masz pr*cę?"

        luszcz "Tak ojcze"
        luszcz "Dostarczam krówki"

        tata "Jestem z ciebie taki dumny synu. Masz pieniążka kup sobie lody."

        $ money += 3
        $ mleczarz_social_link = 4

        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

        luszcz "Dzięki tatku"

        hide luszcz 
        hide tata
        jump parking

label mleczarz5:
        play music "audio/music/ddlc.mp3"
        scene bg sayori
        show luszcz skinwalker at left

        luszcz ""
        luszcz ""
        luszcz ""

        $ krowka = 0

        nikt ":"
        luszcz ">>>"
        nikt "$"

        $ money += 2
        $ mleczarz_social_link = 5

        "{i}*++++++*{/i}"
        luszcz "."

        stop music
        hide luszcz 
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            play music "audio/music/pole.mp3"
        else:
            play music "audio/music/pole_noc.mp3"
        jump parking

label mleczarz6:
        play music "audio/music/natura.mp3"
        scene bg szkola
        show luszcz neutral at left

        luszcz "Dostawa krówek!!"
        luszcz "Kto zamawiał krówki!!"

        show obi neutral at slightright

        $ krowka = 0

        obi "To ja, Obi Wan Kenobi, zamawiałem krówki"

        luszcz "O Dzień dobry co pan tu robi"

        obi "Nie twój interes"
        obi "Oto pieniądze"

        $ money += 2
        $ mleczarz_social_link = 6

        "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

        luszcz "Dziękuję, do widzenia"

        obi "Do widzenia."

        hide luszcz 
        hide obi
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            play music "audio/music/pole.mp3"
        else:
            play music "audio/music/pole_noc.mp3"
        if rynek == 1:
            jump rynek
        if sloneczna == 1:
            jump sloneczna 
        if alejka == 1:
            jump alejka 
        if parking == 1:
            jump parking
        if wolbromska == 1:
            jump wolbromska
        if bohaterow_wrzesnia == 1:
            jump bohaterow_wrzesnia 
        if lipowa == 1:
            jump lipowa 
        if granica == 1:
            jump granica