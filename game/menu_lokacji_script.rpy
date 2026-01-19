default rynek = 0
default sloneczna = 0
default alejka = 0
default parking = 0
default wolbromska = 0
default bohaterow_wrzesnia = 0
default lipowa = 0
default granica = 0

default cmentarz_zydowskix = 0
default cmentarzx = 0
default urzad_gminyx = 0
default placx = 0
default lopatka_ukradnieta = 0
default portalx = 0
default domx = 0
default jeziorox = 0

default spanko = 0

label menu_lokacji:
    label rynek:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 1
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg rynek with fade
        else:
            scene bg black with fade
            scene bg rynek_noc with fade

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label rynek2:
            menu:
                "{i}<--- Alejka (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 1
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump alejka

                "{i}<--- Słoneczna (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 1
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump sloneczna
                
                "{i}Parking (10min) --->{/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 1
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump parking

                "{i}Bohaterów Września (10min) --->{/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 1
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump bohaterow_wrzesnia
                
                "{b}Urząd Gminy{/b}": 
                    $ urzad_gminyx = 0
                    if burmistrz_social_link == 0:
                        $ urzad_gminyx += 1
                        "{i}W ratuszu trwają obecnie burzliwe obrady na temat budżetu Skały{/i}"
                    
                    if urzad_gminyx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump rynek2

                    else:
                        if urzad_gminyx == 1:
                            if burmistrz_social_link == 0:
                                menu:
                                    "{b}Czy chcę wziać udział w obradach (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump burmistrz1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2

                        else:
                            if urzad_gminyx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Wziąć udział w obradach (1h){/b}" if burmistrz_social_link == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump burmistrz1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2
        
    label sloneczna:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 1
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg sloneczna with fade
        else:
            scene bg black with fade
            scene bg sloneczna_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label sloneczna2:
            menu:      
                "{i}Rynek (10min) --->{/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 1
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump rynek
                
                "{b}Plac Budowy{/b}":
                    $ placx = 0
                    if burmistrz_social_link == 1:
                        $ placx += 1
                        "{i}Przy placu budowy czeka na mnie Burmistrz, który chce mi pokazać gdzie powstanie nowe centrum szkolenia dla strażaków{/i}"
                        "{i}Nie chcę tam iść{/i}"
                    
                    if lopatka == 0 and lopatka_ukradnieta == 0:
                        $ placx += 1
                        "{i}Widzę leżacą na ziemi łopatkę{/i}"
                        "{i}Chyba dokładnie taką potrzebuje Żyd...{/i}"

                    if placx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump sloneczna2

                    else:
                        if placx == 1:
                            if burmistrz_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Burmistrzem? (4h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump burmistrz2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                            
                            if lopatka_ukradnieta == 0:
                                menu:
                                    "{b}Czy chcę ukraść łopatkę? (10min){/b}"

                                    "{b}Tak{/b}":
                                        $ timer += 10
                                        $ lopatka = 1
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ lopatka_ukradnieta = 1
                                        "{i}łopatka została dodana do ekwipunku{/i}"
                                        jump sloneczna

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2

                        else:
                            if placx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Burmistrzem (4h){/b}" if burmistrz_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump burmistrz2

                                    "{b}Ukradnij łopatkę (10min){/b}" if lopatka_ukradnieta == 0:
                                        $ timer += 10
                                        $ lopatka = 1
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ lopatka_ukradnieta = 1
                                        "{i}łopatka została dodana do ekwipunku{/i}"
                                        jump sloneczna
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
        
    label alejka:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 1
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg alejka with fade
        else:
            scene bg black with fade
            scene bg alejka_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label alejka2:
            menu:      
                "{i}Rynek (10min) --->{/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 1
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump rynek
                
                "{b}❓ Sklep Monopolowy (60min){/b}" if zyd_social_link == 0:
                    $ timer += 60
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump zyd1
                
                "{b}🛒 Sklep Monopolowy (15min){/b}" if zyd_social_link > 0:
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump sklep_monopolowy
                
                "{b}Urząd Gminy{/b}": 
                    $ urzad_gminyx = 0
                    if burmistrz_social_link == 0:
                        $ urzad_gminyx += 1
                        "{i}W ratuszu trwają obecnie burzliwe obrady na temat budżetu Skały{/i}"
                    
                    if urzad_gminyx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump alejka2

                    else:
                        if urzad_gminyx == 1:
                            if burmistrz_social_link == 0:
                                menu:
                                    "{b}Czy chcę wziać udział w obradach (5h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 300
                                        jump burmistrz1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2

                        else:
                            if urzad_gminyx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Wziąć udział w obradach (5h){/b}" if burmistrz_social_link == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 300
                                        jump burmistrz1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2
        
    label parking:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 1
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg parking with fade
        else:
            scene bg black with fade
            scene bg parking_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label parking2:
            menu:
                "{i}<--- Wolbromska (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 1
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump wolbromska
                
                "{i}<--- Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 1
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump rynek
                
                "{b}🏠 Dom{/b}": 
                    $ domx = 0        
                    if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                        $ domx += 1
                        "{i}Robię się trochę śpiący...{/i}"

                    if domx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump parking2

                    else:
                        if domx == 1:
                            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                                menu:
                                    "{b}Czy chcę iść spać?{/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                        else:
                            if domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Idź spać{/b}" if tarczownik_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
        
    label wolbromska:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 1
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 0
        if tarczownik_social_link == 0:
            scene bg black with fade
            jump tarczownik1

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg wolbromska with fade
        else:
            scene bg black with fade
            scene bg wolbromska_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label wolbromska2:
            menu:
                "{i}Parking (20min) --->{/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 1
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump parking
                
                "{b}🏠 Dom{/b}": 
                    $ domx = 0        
                    if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                        $ domx += 1
                        "{i}Robię się trochę śpiący...{/i}"

                    if domx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if domx == 1:
                            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                                menu:
                                    "{b}Czy chcę iść spać?{/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                        else:
                            if domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Idź spać{/b}" if tarczownik_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                
                "{b}Portal{/b}": 
                    $ portalx = 0
                    if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                        $ portalx += 1
                        "{i}Przy portalu zapewne czeka na mnie Naofumi...{/i}"
                    
                    if portalx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if portalx == 1:
                            if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                                menu:
                                    "{b}Czy chcę się spotkać z Naofumim? (4h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump tarczownik2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                        else:
                            if portalx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Naofumim (4h){/b}" if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump tarczownik2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

    label bohaterow_wrzesnia:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 1
        $ lipowa = 0
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg bohaterow_wrzesnia with fade
        else:
            scene bg black with fade
            scene bg bohaterow_wrzesnia_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label bohaterow_wrzesnia2:
            menu:
                "{i}<--- Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 1
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump rynek

                "{i}<--- Lipowa (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 1
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump lipowa
        
                "{b}🛒 Kebab (15min){/b}":
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump kebab
                
                "{b}Dom Kultury{/b}": 
                    $ dom_kulturyx = 0
                    if urban_social_link == 0:
                        $ dom_kulturyx += 1
                        "{i}W domu kultury trwa właśnie spotkanie seniorów{/i}"
                        "{i}znam właściciela budynku, więc może dałbym radę porozmawiać z seniorami i przekonać ich do mojej sprawy...{/i}"
                    
                    if dom_kulturyx == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump bohaterow_wrzesnia2

                    else:
                        if dom_kulturyx == 1:
                            if urban_social_link == 0:
                                menu:
                                    "{b}Czy chcę porozmawiać z seniorami? (4h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump urban1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                        else:
                            if dom_kulturyx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z seniorami (4h){/b}" if urban_social_link == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump urban1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

    label lipowa:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 1
        $ granica = 0
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg lipowa with fade
        else:
            scene bg black with fade
            scene bg lipowa_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label lipowa2:
            menu:
                "{i}Bohaterów Września (10min) --->{/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 1
                        $ lipowa = 0
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump bohaterow_wrzesnia

                "{i}Granica Skały (20min) --->{/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 1
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump granica
                
                "{b}Cmentarz Żydowski{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        $ cmentarz_zydowskix += 1
                        "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                        "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump lipowa2

                    else:
                        if cmentarz_zydowskix == 1:
                            if zyd_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                        else:
                            if cmentarz_zydowskix > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Żydem (30min){/b}" if zyd_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                
                "{b}Cmentarz{/b}":
                    $ cmentarzx = 0
                    if zyd_social_link == 3 and lopatka == 1:
                        $ cmentarzx += 1
                        "{i}Na cmentarzu czeka na mnie Żyd, z którym zamierzamy wykopać prochy jego dziadka{/i}"
                        "{i}Miałem w tym celu znaleźć łopatkę, co udało mi się wykonać{/i}"
                    
                    if zyd_social_link == 3 and lopatka == 0:
                        "{i}Na cmentarzu czeka na mnie żyd, ale nadal nie zdobyłem dla niego łopatki{/i}"
                        "{i}Muszę się tym zająć zanim się z nim spotkam{/i}"
                    
                    if zyd_social_link == 2:
                        $ cmentarzx += 1
                        "{i}Żyd czeka na mnie pod kwaterą żołnierzy 1 wojny światowej{/i}"
                        "{i}Mamy razem wykopać zwłoki jego pra-pra-dziadka{/i}"

                    if cmentarzx == 0:
                        if zyd_social_link == 3 and lopatka == 0:
                            jump lipowa2

                        "{i}Nie ma tu nic do roboty{/i}"
                        jump lipowa2

                    else:
                        if cmentarzx == 1:
                            if zyd_social_link == 3 and lopatka == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump zyd4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if zyd_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump zyd3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                        else:
                            if cmentarzx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Żydem (3h){/b}" if zyd_social_link == 3 and lopatka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump zyd4

                                    "{b}Spotkaj się z Żydem (15min){/b}" if zyd_social_link == 2:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump zyd3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
        
    label granica:
        play sound "audio/sfx/traveling.mp3" 
        $ rynek = 0
        $ sloneczna = 0
        $ alejka = 0
        $ parking = 0
        $ wolbromska = 0
        $ bohaterow_wrzesnia = 0
        $ lipowa = 0
        $ granica = 1
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg granica with fade
        else:
            scene bg black with fade
            scene bg granica_noc with fade
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or  timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2

        label granica2:
            menu:
                "{i}<--- Lipowa (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 11)
                    if kostka == 1:
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 1
                        $ granica = 0
                        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                        $ kostka = renpy.random.randint(1, 3)
                        if kostka == 1:
                            jump raem_fight
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 3:
                            jump fightx3
                    jump lipowa    
                
                "{b}Cmentarz Żydowski{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        $ cmentarz_zydowskix += 1
                        "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                        "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump granica2

                    else:
                        if cmentarz_zydowskix == 1:
                            if zyd_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2

                        else:
                            if cmentarz_zydowskix > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Żydem (30min){/b}" if zyd_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2
                
                "{b}Cmentarz{/b}":
                    $ cmentarzx = 0
                    if zyd_social_link == 3 and lopatka == 1:
                        $ cmentarzx += 1
                        "{i}Na cmentarzu czeka na mnie Żyd, z którym zamierzamy wykopać prochy jego dziadka{/i}"
                        "{i}Miałem w tym celu znaleźć łopatkę, co udało mi się wykonać{/i}"
                    
                    if zyd_social_link == 3 and lopatka == 0:
                        "{i}Na cmentarzu czeka na mnie żyd, ale nadal nie zdobyłem dla niego łopatki{/i}"
                        "{i}Muszę się tym zająć zanim się z nim spotkam{/i}"
                    
                    if zyd_social_link == 2:
                        $ cmentarzx += 1
                        "{i}Żyd czeka na mnie pod kwaterą żołnierzy 1 wojny światowej{/i}"
                        "{i}Mamy razem wykopać zwłoki jego pra-pra-dziadka{/i}"

                    if cmentarzx == 0:
                        if zyd_social_link == 3 and lopatka == 0:
                            jump granica2

                        "{i}Nie ma tu nic do roboty{/i}"
                        jump granica2

                    else:
                        if cmentarzx == 1:
                            if zyd_social_link == 3 and lopatka == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump zyd4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2
                            
                            if zyd_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump zyd3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2

                        else:
                            if cmentarzx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Żydem (3h){/b}" if zyd_social_link == 3 and lopatka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump zyd4

                                    "{b}Spotkaj się z Żydem (15min){/b}" if zyd_social_link == 2:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump zyd3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2


                "{b}Jezioro{/b}": 
                    $ jeziorox = 0
                    if urban_social_link == 1:
                        $ jeziorox += 1
                        "{i}Znalazłem przy jeiorze stary bunkier{/i}"
                        "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                    
                    if jeziorox == 0:
                        "{i}Nie ma tu nic do roboty{/i}"
                        jump granica2

                    else:
                        if jeziorox == 1:
                            if urban_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Jerzym Urbanem? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump urban2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2

                        else:
                            if jeziorox > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Jerzym Urbanem (3h){/b}" if urban_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump urban2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2



    label raem_fight:
        scene bg raem
        play music "audio/music/rezero.mp3"
        show luszcz freaky at left
        show ram neutral:
            xalign 0.55
            yalign 1.0
        show rem neutral:
            xalign 0.95
            yalign 1.0
        ram "Rem, Rem ten osobnik popatrzył się na mnie w dziwny sposób"
        rem "Siostrczyko, siostrzyczko ten osobnik musi być zboczeńcem w takim razie"

        show luszcz neutral at left

        luszcz "Ej, chwila nie patrzyłem sie na ciebie w dziwny sposób i nie jestem zboczeńcem!!!"

        rem "Siostrzyczko, siostrzyczko tego osobnika nie stać nawet na to by się przyznać"
        ram "Rem, Rem chyba sami będziemy musieli nauczyć tego śmiecia manier"

        jump fight51

    label after_fight51:
        scene bg raem
        play music "audio/music/rezero.mp3"
        show luszcz neutral at left
        show ram neutral:
            xalign 0.55
            yalign 1.0
        show rem neutral:
            xalign 0.95
            yalign 1.0
        rem "Siostrczyko, siostrzyczko chyba przegraliśmy ten pojedynek"
        ram "Rem, Rem niestety na to wygląda"
        rem "Siostrczyko, siostrzyczko teraz musimy się oddać popędą seksualnym tego zboczeńca"

        luszcz "Ej, ej po pierwsze nie jestem rzadnym zboczeńcem, a po drugie to wy zaczeliście ten pojedynek!"
        luszcz "Dlatego, teraz nie róbcie ze mnie jakiegoś potwora w oczach ludzi"

        ram "Rem, Rem teń śmieć powiedział, że zamierza nas zaraz wykorzystać, a potem zostawić bez płacenia alimentów"
        rem "Siostrzyczko, siostrzyczko ja będę płaciła Ci alimenty jeśli ten osobnik nie zamierza"

        luszcz "Ehhh, nie mogę z wami"

        play music "audio/music/pole.mp3"
        if rynek == 1:
            jump rynek
        if sloneczna == 1:
            jump slonneczna 
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

    label gnoms_fight:
        scene bg gnoms
        stop music
        show luszcz neutral at left
        show gnom1 neutral:
            xalign 0.55
            yalign 1.0
        show gnom2 neutral:
            xalign 0.95
            yalign 1.0
        show gnom3 neutral:
            xalign 0.75
            yalign 1.0
        play sound "audio/sfx/gnomowo.mp3"
        gnom "You've been gnomed!"

        jump fight61

    label after_fight61:
        scene bg gnoms
        stop music
        show luszcz neutral at left
        show gnom1 neutral:
            xalign 0.55
            yalign 1.0
        show gnom2 neutral:
            xalign 0.95
            yalign 1.0
        show gnom3 neutral:
            xalign 0.75
            yalign 1.0
        play sound "audio/sfx/gnomowo.mp3"
        gnom "We've been gnomed!"

        play music "audio/music/pole.mp3"
        if rynek == 1:
            jump rynek
        if sloneczna == 1:
            jump slonneczna 
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
    
    label fightx3:
        "po walce 3"
        play music "audio/music/pole.mp3"
        if rynek == 1:
            jump rynek
        if sloneczna == 1:
            jump slonneczna 
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

