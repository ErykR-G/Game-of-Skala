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

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
                    jump wolbromska
        
        if mleczarz_social_link == 1:
            mleczarz "Jestem mleczarzem. Moje mleko jest przepyszne."

            menu:
                "{b}Dostarczyć coś komuś?{/b}":
                    luszcz "Dostarczyć coś komuś?"
                    mleczarz "Zamówienie na Słonecznej. Fioletowy dom."

                    $ ile_item_fabularne += 1
                    $ krowka = 1
                    $ krowko_limit = 1
                    "{i}*Krówka została dodana do ekwipunku*{/i}"

                    luszcz "Dobrze, lecę dostarczyć"

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
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

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
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

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
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

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
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

                    play music "audio/music/pole.mp3"
                    jump wolbromska
                
                "{b}Dowidzenia{/b}":
                    luszcz "Dowidzenia."

                    mleczarz "Dowidzenia."

                    play music "audio/music/pole.mp3"
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
            play music "audio/music/pole.mp3"
            jump wolbromska