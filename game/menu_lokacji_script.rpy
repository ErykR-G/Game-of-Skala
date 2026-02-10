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
default klubx = 0
default dom_tasmyx = 0
default szkolax = 0
default czerwony_domx = 0
default piwnicax = 0
default fioletowy_domx = 0
default stomatologx = 0
default toxic_domx = 0
default bunkierx = 0

default spanko = 0
default ewento = 0
default info = 0
default muzyczka = 0

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
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        label rynek2:
            menu:
                "{i}{image=a} Alejka (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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

                "{i}{image=wa} Słoneczna (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{i}{image=d} Parking (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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

                "{i}{image=sd} Bohaterów Września (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🏛️ Urząd Gminy | 7-15{/b}": 
                    $ urzad_gminyx = 0
                    if timer >= 420 and timer <= 900 or timer >= 1860 and timer <= 2340 or timer >= 3300 and timer <= 3780 or timer >= 4740 and timer <= 5220 or timer >= 6180 and timer <= 6660 or timer >= 7620 and timer <= 8100 or timer >= 9060 and timer <= 9540 or timer >= 10500 and timer <= 10980:
                        $ ado += 1
                    else:
                        "{i}Urząd gminy jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump rynek2
                         
                    if burmistrz_social_link == 0:
                        $ urzad_gminyx += 1
                        "{i}W ratuszu trwają obecnie burzliwe obrady na temat budżetu Skały{/i}"
                    
                    if urzad_gminyx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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
        
                "{b}⛪ Kościół | 7-20{/b}": 
                    $ kosciolx = 0
                    if timer >= 420 and timer <= 1200 or timer >= 1860 and timer <= 2640 or timer >= 3300 and timer <= 4080 or timer >= 4740 and timer <= 5520 or timer >= 6180 and timer <= 6960 or timer >= 7620 and timer <= 8400 or timer >= 9060 and timer <= 9840 or timer >= 10500 and timer <= 11280:
                        $ ado += 1
                    else:
                        "{i}Kościół jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump rynek2

                    if kosc_social_link == 0 and koscielny_zyje == 0:
                        $ kosciolx += 1
                        "{i}Mógłbym porozmawiać z tym kościelnym ze mszy…{i}"
                        "{i}Nie wydawał się taki zły, morze mogłbym przekabacić go na moją stronę...{i}"
                    
                    if timer >= 6120 and timer < 6660 and info == 0:
                        $ info = 1
                        "{i}Dziś w kościele ma się odbyć koncert zenka martyniuka{/i}"
                        "{i}Jeśli chcę w nim wziąć udział powinienem przyjść tu PO 15:00{/i}"
                    
                    if timer >= 6660 and timer <= 6960:
                        $ kosciolx += 1
                        "{i}Właśnie w kościele trwa koncert Zenka Martyniuka{/i}"


                    if kosciolx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump rynek2

                    else:
                        if kosciolx == 1:
                            if kosc_social_link == 0 and koscielny_zyje == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Kościelnym? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2
                            
                            if timer >= 6660 and timer <= 6960:
                                menu:
                                    "{b}Czy chcę wziąć udział w koncercie Zenka Martyniuka? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2

                        else:
                            if kosciolx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Kościelnym (1h){/b}" if kosc_social_link == 0 and koscielny_zyje == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc1
                                    
                                    "{b}Weź udział w koncercie Zenka Martyniuka (1h){/b}" if timer >= 6660 and timer <= 6960:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc3
                                    
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
            if silver_sextape_social_link == 3 and ewento == 0 and tasma_spotkanko == 0:
                $ ewento += 1
                jump silver_sextape4
                
        else:
            scene bg black with fade
            scene bg sloneczna_noc with fade
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        label sloneczna2:
            menu:      
                "{i}{image=sd} Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🏗️ Plac Budowy | 6-18 {/b}":
                    $ placx = 0
                    if timer >= 360 and timer <= 1080 or timer >= 1800 and timer <= 2520 or timer >= 3240 and timer <= 3960 or timer >= 4680 and timer <= 5400 or timer >= 6120 and timer <= 6840 or timer >= 7560 and timer <= 8280 or timer >= 9000 and timer <= 9720 or timer >= 10440 and timer <= 11160:
                        $ ado += 1
                    else:
                        "{i}Plac Budowy jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump sloneczna2

                    if burmistrz_social_link == 1:
                        $ placx += 1
                        "{i}Przy placu budowy czeka na mnie Burmistrz, który chce mi pokazać gdzie powstanie nowe centrum szkolenia dla strażaków{/i}"
                        "{i}Nie chcę tam iść{/i}"
                    
                    if allozaur_social_link == 0:
                        $ placx += 1
                        "{i}Słyszę głośne ryki, brzmiące jakby wydawało je jakieś dzikie zwierzę{/i}"
                    
                    if allozaur_social_link == 1:
                        $ placx += 1
                        "{i}Słyszę głośne ryki, Allozaura{/i}"

                    if placx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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
                            
                            if allozaur_social_link == 0:
                                menu:
                                    "{b}Czy chcę sprawdzic co wydaje te ryki? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump allozaur1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                            
                            if allozaur_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Allozaurem? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump allozaur1

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

                                    "{b}Sprawdź co wydaje te ryki (15min){/b}" if allozaur_social_link == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump allozaur1
                                    
                                    "{b}Spotkaj się z Allozaurem (15min){/b}" if allozaur_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump allozaur1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
        
                "{b}🪩 Klub Seniora GROTA | 16-22{/b}":
                    $ klubx = 0
                    if silver_sextape_social_link == 1:
                        $ klubx  += 1
                        "{i}W klubie czeka na mnie Taśma, którą spotkałem przed monopolowym{/i}"
                        "{i}Ma chyba do mnie jakąś ważną sprawę{/i}"

                    if klubx  == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump sloneczna2

                    else:
                        if klubx == 1:
                            if silver_sextape_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Taśmą? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump silver_sextape2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                        
                        else:
                            if klubx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Taśmą (1h){/b}" if silver_sextape_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump silver_sextape2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2

                "{b}🏡 Różowy Dom | 9-20 {/b}" if mleczarz_social_link > 1 or mleczarz_social_link == 1 and krowka == 1:
                    $ fioletowy_domx = 0
                    if mleczarz_social_link == 1 and krowka == 1:
                        $ fioletowy_domx += 1
                        "{i}Mam dostraczyć do tego domu krówkę...{/i}"
                    
                    if fioletowy_domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump sloneczna2

                    else:
                        if fioletowy_domx == 1:
                            if mleczarz_social_link == 1 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2

                        else:
                            if fioletowy_domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Dostarcz Krówkę (15min){/b}" if mleczarz_social_link == 1 and krowka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz3
                                    
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
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2      
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        label alejka2:
            menu:      
                "{i}{image=d} Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🛒 Sklep Monopolowy (60min) | 6-23{/b}" if zyd_social_link == 0:
                    if timer >= 360 and timer <= 1380 or timer >= 1800 and timer <= 2820 or timer >= 3240 and timer <= 4260 or timer >= 4680 and timer <= 5700 or timer >= 6120 and timer <= 7140 or timer >= 7560 and timer <= 8580 or timer >= 9000 and timer <= 10020 or timer >= 10440 and timer <= 11460:
                        $ ado += 1
                    else:
                        "{i}Sklep Monopolowy jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump alejka2
                    $ monopoleks += 1
                    $ timer += 60
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump zyd1
                
                "{b}🛒 Sklep Monopolowy (15min) | 6-23{/b}" if zyd_social_link > 0:
                    if timer >= 360 and timer <= 1380 or timer >= 1800 and timer <= 2820 or timer >= 3240 and timer <= 4260 or timer >= 4680 and timer <= 5700 or timer >= 6120 and timer <= 7140 or timer >= 7560 and timer <= 8580 or timer >= 9000 and timer <= 10020 or timer >= 10440 and timer <= 11460:
                        $ ado += 1
                    else:
                        "{i}Sklep Monopolowy jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump alejka2
                    if monopoleks == 2 and silver_sextape_social_link == 0:
                        jump silver_sextape1
                    $ monopoleks += 1
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump sklep_monopolowy
                
                "{b}🏛️ Urząd Gminy | 7-15{/b}": 
                    $ urzad_gminyx = 0
                    if timer >= 420 and timer <= 900 or timer >= 1860 and timer <= 2340 or timer >= 3300 and timer <= 3780 or timer >= 4740 and timer <= 5220 or timer >= 6180 and timer <= 6660 or timer >= 7620 and timer <= 8100 or timer >= 9060 and timer <= 9540 or timer >= 10500 and timer <= 10980:
                        $ ado += 1
                    else:
                        "{i}Urząd gminy jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump alejka2

                    if burmistrz_social_link == 0:
                        $ urzad_gminyx += 1
                        "{i}W ratuszu trwają obecnie burzliwe obrady na temat budżetu Skały{/i}"
                    
                    if urzad_gminyx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump alejka2

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
                                        jump alejka2

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
                                        jump alejka2
                
                "{b}🏡 Dom Taśmy | 20-24{/b}" if silver_sextape_social_link >= 2 and silver_sextape_social_link < 10: 
                    $ dom_tasmyx = 0
                    if silver_sextape_social_link == 2:
                        $ dom_tasmyx += 1
                        "{i}Taśma czeka na mnie, by przedłużyć wspólnie gatunek{/i}"
                    
                    if dom_tasmyx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump alejka2

                    else:
                        if dom_tasmyx == 1:
                            if silver_sextape_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Taśmą (4h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump silver_sextape3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2

                        else:
                            if dom_tasmyx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Taśmą (4h){/b}" if silver_sextape_social_link == 2:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump silver_sextape3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2

                "{b}🕳️ Piwnica Eminema | 24/7{/b}": 
                    $ piwnicax = 0
                    if harambe_social_link == 2 and kosc_social_link == 3 and cialo == 0:
                        $ piwnicax += 1
                        "{i}Piwnica eminema, w której go pokonalismy i uratowaliśmy Cida{/i}"
                        "{i}Może jego zwłoki się nadadzą do rytuału...{/i}"
                    
                    if piwnicax == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump alejka2

                    else:
                        if piwnicax == 1:
                            if harambe_social_link == 2 and kosc_social_link == 3 and cialo == 0: 
                                menu:
                                    "{b}Czy chcę zabrać zwłoki Eminema? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump harambe2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2

                        else:
                            if piwnicax > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Zabierz zwłoki eminema (15min){/b}"  if harambe_social_link == 2 and kosc_social_link == 3 and cialo == 0: 
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump harambe2
                                    
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
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if mleczarz_social_link == 4 and krowka == 1:
            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                "{i}Mam dostraczyć gdzieś tutaj krówkę...{/i}"
                jump mleczarz5

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2          
        label parking2:
            menu:
                "{i}{image=wa} Wolbromska (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{i}{image=a} Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🩺 Apteka (15min) | 8-20{/b}":
                    if timer >= 480 and timer <= 1200 or timer >= 1920 and timer <= 2640 or timer >= 3360 and timer <= 4080 or timer >= 4800 and timer <= 5520 or timer >= 6240 and timer <= 6960 or timer >= 7680 and timer <= 8400 or timer >= 9120 and timer <= 9840 or timer >= 10560 and timer <= 11280:
                        $ ado += 1
                    else:
                        "{i}Apteka jest obecnie zamknięta{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump parking2

                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    if gotka_szpan > 0 or gotka_social_link > 0:
                        jump gotka2
                    else:
                        jump gotka1

                "{b}🏡 Dom | 24/7{/b}": 
                    $ domx = 0        
                    if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                        $ domx += 1
                        "{i}Robię się trochę śpiący...{/i}"
                    
                    else:
                        if babcia_social_link == 1:
                            $ domx += 1
                            "{i}Mam dla Babci przynieść memy, by uszyła mi z nich szalik...{/i}"

                    if domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump parking2

                    else:
                        if domx == 1:
                            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                menu:
                                    "{b}Czy chcę iść spać?{/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                            if babcia_social_link == 1:
                                menu:
                                    "{b}Czy chcę pobrać memy? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2

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
                                    
                                    "{b}Pobierz memy{/b}" if babcia_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                "{b}🦷 Stomatolog | 12-19{/b}" if mleczarz_social_link > 3 or mleczarz_social_link == 3 and krowka == 1:
                    $ stomatologx = 0
                    if mleczarz_social_link == 3 and krowka == 1:
                        $ stomatologx += 1
                        "{i}Mam dostraczyć tutaj krówkę...{/i}"
                    
                    if stomatologx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump parking2

                    else:
                        if stomatologx == 1:
                            if mleczarz_social_link == 3 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                        else:
                            if stomatologx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Dostarcz Krówkę (15min){/b}" if mleczarz_social_link == 3 and krowka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz4
                                    
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

        if timer >= 360 and timer <= 900 or timer >= 1800 and timer <= 2340 or timer >= 3240 and timer <= 3780 or timer >= 4680 and timer <= 5220 or timer >= 6120 and timer <= 6660 or timer >= 7560 and timer <= 8100 or timer >= 9000 and timer <= 9540 or timer >= 10440 and timer <= 10980:
            if tarczownik_social_link == 0:
                scene bg black with fade
                jump tarczownik1

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg wolbromska with fade
        else:
            scene bg black with fade
            scene bg wolbromska_noc with fade
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2          
        
        label wolbromska2:
            menu:
                "{i}{image=sd} Parking (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🏠 Dom | 24/7{/b}": 
                    $ domx = 0        
                    if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                        $ domx += 1
                        "{i}Robię się trochę śpiący...{/i}"
                    
                    else:
                        if babcia_social_link == 1:
                            $ domx += 1
                            "{i}Mam dla Babci przynieść memy, by uszyła mi z nich szalik...{/i}"

                    if domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if domx == 1:
                            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                menu:
                                    "{b}Czy chcę iść spać?{/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if babcia_social_link == 1:
                                menu:
                                    "{b}Czy chcę pobrać memy? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2

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
                                    
                                    "{b}Pobierz memy{/b}" if babcia_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                
                "{b}🏡 Dom Toxic Pea | 20–6{/b}" if toxic_pea_social_link > 0 and toxic_pea_social_link < 10:
                    $ toxic_domx = 0        
                    if toxic_pea_social_link == 1 and toxic_limit == 0:
                        $ toxic_domx += 1
                        "{i}Tutaj mieszka Toxic Pea, którego spotkałem na Kebabie{/i}"
                        "{i}Zaproponował mi byśmy razem pozabijali zombiaczki...{/i}"
                    
                    if toxic_pea_social_link == 2 and toxic_limit == 0:
                        $ toxic_domx += 1
                        "{i}Ostatnio zabijałem tutaj zombiaczki razem z Toxic Pea{/i}"
                        "{i}Zaproponował mi byśmy zrobili to jeszcze raz...{/i}"

                    if toxic_domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if toxic_domx == 1:
                            if toxic_pea_social_link == 1 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump toxic_pea1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if toxic_pea_social_link == 2 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump toxic_pea2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2


                        else:
                            if toxic_domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"
                                    
                                    "{b}Spotkaj się z Toxic Pea (3h){/b}" if toxic_pea_social_link == 1 and toxic_limit == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump toxic_pea1
                                    
                                    "{b}Spotkaj się z Toxic Pea (3h){/b}" if toxic_pea_social_link == 2 and toxic_limit = 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump toxic_pea2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                "{b}🐄 Mleczarnia (15min) | 8–16{/b}": 
                    if mleczarz_social_link == 7:
                        "{i}Mleczarz już tutaj nie pracuje{/i}"
                        "{i}Dzięki mnie mógł w spokoju przejść na emeryture{/i}"
                        jump wolbromska2
                    
                    if timer >= 460 and timer <= 960 or timer >= 1920 and timer <= 2400 or timer >= 3360 and timer <= 3840 or timer >= 4800 and timer <= 5280 or timer >= 6240 and timer <= 6720 or timer >= 7680 and timer <= 8160 or timer >= 9120 and timer <= 9600 or timer >= 10560 and timer <= 11040:
                        $ ado += 1
                    else:
                        "{i}Mleczarnia jest obecnie zamknięta{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump wolbromska2

                    if krowka == 1:
                        "{i}Nie dostarczyłem jescze krówki...{/i}"
                        "{i}Muszę ją dostarczyć zanim tu wrócę{/i}"
                        jump wolbromska2
                    
                    if krowko_limit == 1:
                        "{i}Mleczarz nie ma dziś więcej krówek do rozdania{/i}"
                        "{i}Powinienem wrócić tutaj jutro...{/i}"
                        jump wolbromska2
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump mleczarz1
                
                "{b}🪨 Skała widokowa | 6–18{/b}": 
                    $ skalax = 0        
                    if timer >= 360 and timer <= 1080 or timer >= 1800 and timer <= 2520 or timer >= 3240 and timer <= 3960 or timer >= 4680 and timer <= 5400 or timer >= 6120 and timer <= 6840 or timer >= 7560 and timer <= 8280 or timer >= 9000 and timer <= 9720 or timer >= 10440 and timer <= 11160:
                        $ ado += 1
                    else:
                        "{i}Obecnie jest zbyt niebezpiecznie, by iść na skałkę{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump wolbromska2

                    if samobojstwo == 0:
                        $ skalax += 1
                        "{i}Mógłbym popełnić samobójstwo z tej skały widokowej...{/i}"
                    
                    if wazon_wezy == 1:
                        $ skalax += 1
                        "{i}Harambe kazał pomedytować w spokojnym miescu z wazonem z wężami{/i}"
                        "{i}Może ta skałka, by sie nadała...{/i}"

                    if skalax == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if skalax == 1:           
                            if samobojstwo == 0:
                                menu:
                                    "{b}Czy chcę popełnić samobójstwo? (30min){/b}" 

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump skalka1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if wazon_wezy == 1:
                                menu:
                                    "{b}Czy chcę pomedytować z wazonem z wężami? (15min){/b}" 

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump skalka2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                        
                        else:
                            if skalax > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"
                                    
                                    "{b}Popełnij Samobójstwo (30min){/b}" if samobojstwo == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump skalka1
                                    
                                    "{b}Pomedytuj z wazonem z wężami (15min){/b}" if wazon_wezy == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump skalka2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                "{b}🌀 Portal | 6–20{/b}": 
                    $ portalx = 0
                    if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                        $ portalx += 1
                        "{i}Przy portalu zapewne czeka na mnie Naofumi...{/i}"
                    
                    if portalx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        label bohaterow_wrzesnia2:
            menu:
                "{i}{image=wa} Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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

                "{i}{image=sa} Lipowa (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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
        
                "{b}🛒 Kebab (15min) | 11–23{/b}":
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump kebab
                
                "{b}🏡 Czerwony Dom | 8–20{/b}" if mleczarz_social_link > 2 or mleczarz_social_link == 2 and krowka == 1:
                    $ czerwony_domx = 0        
                    if mleczarz_social_link == 2 and krowka == 1:
                        $ czerwony_domx += 1
                        "{i}Mam dostraczyć do tego domu krówkę...{/i}"

                    if czerwony_domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump bohaterow_wrzesnia2

                    else:
                        if czerwony_domx == 1:           
                            if mleczarz_social_link == 2 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kibole1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2


                        else:
                            if czerwony_domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"
                                    
                                    "{b}Dostarcz Krówkę (1h){/b}" if mleczarz_social_link == 2 and krowka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kibole1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                "{b}🎭 Dom Kultury | 7–19{/b}": 
                    $ dom_kulturyx = 0
                    if timer >= 420 and timer <= 1140 or timer >= 1860 and timer <= 2580 or timer >= 3300 and timer <= 4020 or timer >= 4740 and timer <= 5460 or timer >= 6180 and timer <= 6900 or timer >= 7620 and timer <= 8340 or timer >= 9060 and timer <= 9780 or timer >= 10500 and timer <= 11220:
                        $ ado += 1
                    else:
                        "{i}Dom Kultury jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump bohaterow_wrzesnia2

                    if urban_social_link == 0:
                        $ dom_kulturyx += 1
                        "{i}W domu kultury trwa właśnie spotkanie seniorów{/i}"
                        "{i}znam właściciela budynku, więc może dałbym radę porozmawiać z seniorami i przekonać ich do mojej sprawy...{/i}"
                    
                    if urban_social_link > 0 and babcia_social_link == 0 and akcja1 == 0:
                        $ dom_kulturyx += 1
                        "{i}Po ostatniej akcji z czarodziejem w domu kultury nastał chaos{/i}"
                        "{i}może mógłbym tam pójść i zobaczyć czy mogę coś z tym zrobić...{/i}"
                    
                    if babcia_social_link == 1:
                        "{i}W domu kultury czeka na mnie Babcia,{/i}"
                        "{i}ale zanim się z nią spotkam muszę przynieśc jej materiał do szycia...{/i}"
                    
                    if babcia_social_link == 2:
                        $ dom_kulturyx += 1
                        "{i}W domu kultury czeka na mnie Babcia{/i}"
                        "{i}mam dla niej materiał, z którego uszyje mi szalik{/i}"
                    
                    if dom_kulturyx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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
                        
                        if urban_social_link > 0 and babcia_social_link == 0 and akcja1 == 0:
                                menu:
                                    "{b}Czy chcę sprawdzić sytuacje w domu kultury? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2
                        
                        if babcia_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Babcią? (30min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia3

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
                                    
                                    "{b}Sprawdź sytuacje w domu kultury (30min){/b}" if urban_social_link > 0 and babcia_social_link == 0 and akcja1 == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia1
                                    
                                    "{b}Spotkaj się z Babcią (30min){/b}" if babcia_social_link == 2:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                "{b}⛪ Kościół | 7–20{/b}": 
                    $ kosciolx = 0
                    if timer >= 420 and timer <= 1200 or timer >= 1860 and timer <= 2640 or timer >= 3300 and timer <= 4080 or timer >= 4740 and timer <= 5520 or timer >= 6180 and timer <= 6960 or timer >= 7620 and timer <= 8400 or timer >= 9060 and timer <= 9840 or timer >= 10500 and timer <= 11280:
                        $ ado += 1
                    else:
                        "{i}Kościół jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump bohaterow_wrzesnia2
                        
                    if kosc_social_link == 0 and koscielny_zyje == 0:
                        $ kosciolx += 1
                        "{i}Mógłbym porozmawiać z tym kościelnym ze mszy…{i}"
                        "{i}Nie wydawał się taki zły, morze mogłbym przekabacić go na moją stronę...{i}"
                    
                    if timer >= 6120 and timer < 6660 and info == 0:
                        $ info = 1
                        "{i}Dziś w kościele ma się odbyć koncert zenka martyniuka{/i}"
                        "{i}Jeśli chcę w nim wziąć udział powinienem przyjść tu PO 15:00{/i}"
                    
                    if timer >= 6660 and timer <= 6960:
                        $ kosciolx += 1
                        "{i}Właśnie w kościele trwa koncert Zenka Martyniuka{/i}"
                    
                    if kosciolx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump bohaterow_wrzesnia2

                    else:
                        if kosciolx == 1:
                            if kosc_social_link == 0 and koscielny_zyje == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Kościelnym? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2
                            
                            if timer >= 6660 and timer <= 6960:
                                menu:
                                    "{b}Czy chcę wziąć udział w koncercie Zenka Martyniuka? (1h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                        else:
                            if kosciolx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Kościelnym (1h){/b}" if kosc_social_link == 0 and koscielny_zyje == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc1
                                    
                                    "{b}Weź udział w koncercie Zenka Martyniuka (1h){/b}" if timer >= 6660 and timer <= 6960:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc3
                                    
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
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        label lipowa2:
            menu:
                "{i}{image=wd} Bohaterów Września (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 15)
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

                "{i}{image=s} Granica Skały (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🪦 Cmentarz | 24/7{/b}":
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
                    
                    if harambe_social_link == 0:
                        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                            $ cmentarzx += 1
                            "{i}Spacer po cmentarzu nocą to świetny pomysł{/i}"
                    
                    if harambe_social_link == 1 and kosc_social_link == 3:
                        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                            $ cmentarzx += 1
                            "{i}Na cmentarzu jest duch Harambe{/i}"
                            "{i}może mógłbym go poprosić o pomoc w skrzeszeniu kościelnego...{/i}"
                    
                    if harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 0 or harambe_social_link == 2 and kosc_social_link == 3 and glowa == 0 and cialo == 0:
                        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                            "{i}Muszę przynieść ailbiB i ciało do Harambe{/i}"
                            "{i}Jak narazie jeszcze tego nie mam...{/i}"
                    
                    if harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or harambe_social_link == 2 and kosc_social_link == 3 and cialo == 1 and ailbib == 1:
                        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                            $ cmentarzx += 1
                            "{i}Muszę przynieść ailbiB i ciało do Harambe{/i}"
                            "{i}Chyba mam już wszystko co potrzebne...{/i}"

                    if cmentarzx == 0:
                        if zyd_social_link == 3 and lopatka == 0:
                            jump lipowa2

                        "{i}Nie ma tu teraz nic do roboty{/i}"
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
                            
                            if harambe_social_link == 0:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy chcę iść na spacer? (30min){/b}"

                                        "{b}Tak{/b}":
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 30
                                            jump harambe1

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump lipowa2

                            if harambe_social_link == 1 and kosc_social_link == 3:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy poprosić Harambe o pomoc? (30min){/b}"

                                        "{b}Tak{/b}":
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 30
                                            jump kosc4

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump lipowa2
                            
                            if harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or harambe_social_link == 2 and kosc_social_link == 3 and cialo == 1 and ailbib == 1:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy wskrzesić Kościelnego? (1h){/b}"

                                        "{b}Tak{/b}":
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 60
                                            jump kosc5

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

                                    "{b}Idź na spacer (30min){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 0 or timer > 2640 and timer < 3240 and harambe_social_link == 0 or timer > 4080 and timer < 4680 and harambe_social_link == 0 or timer > 5520 and timer < 6120 and harambe_social_link == 0 or timer > 6960 and timer < 7560 and harambe_social_link == 0 or timer > 8400 and timer < 9000 and harambe_social_link == 0 or timer > 9840 and timer < 10440 and harambe_social_link == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump harambe1
                                    
                                    "{b}Poproś o pomoc Harambe (30min){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 2640 and timer < 3240 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 4080 and timer < 4680 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 5520 and timer < 6120 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 6960 and timer < 7560 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 8400 and timer < 9000 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 9840 and timer < 10440 and harambe_social_link == 1 and kosc_social_link == 3:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump kosc4
                                    
                                    "{b}Wskrześ Kościelnego (1h){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 2640 and timer < 3240 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 4080 and timer < 4680 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 5520 and timer < 6120 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 6960 and timer < 7560 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 8400 and timer < 9000 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 9840 and timer < 10440 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 1200 and timer < 1800 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 2640 and timer < 3240 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 4080 and timer < 4680 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 5520 and timer < 6120 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 6960 and timer < 7560 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 8400 and timer < 9000 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 9840 and timer < 10440 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump kosc5
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                "{b}🕯️ Cmentarz Żydowski | 24/7{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        $ cmentarz_zydowskix += 1
                        "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                        "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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

                "{b}🏫 Szkoła | 8–15{/b}":
                    $ szkolax = 0
                    if kosc_social_link == 1 and koscielny_zyje == 0:
                        $ szkolax += 1
                        "{i}W szkole czeka na mnie kościelny{/i}"
                        "{i}mam wysłuchać jego lekcji religii...{/i}"
                    
                    if kibole_social_link == 1:
                        $ szkolax += 1
                        "{i}Na szkolnym boisku Piotrek i Krystian mają zagrać w piłke nożną{/i}"
                        "{i}i teorytycznie powinienem być na tym meczu...{/i}"

                    if mleczarz_social_link == 5 and krowka == 1:
                        $ szkolax += 1
                        "{i}Mam dostraczyć krówkę koło szkoły...{/i}"

                    if szkolax == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump lipowa2

                    else:
                        if szkolax == 1:
                            if kosc_social_link == 1 and koscielny_zyje == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Kościelnym? (3h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump kosc2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if kibole_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Piotrkiem i Krystianem? (2h){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump kibole2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if mleczarz_social_link == 5 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (15min){/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz6

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                        else:
                            if szkolax > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Kościelnym (3h){/b}" if kosc_social_link == 1 and koscielny_zyje == 0:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump kosc2
                                    
                                    "{b}Spotkaj się z Piotrkiem i Krystianem (3h){/b}" if kibole_social_link == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump kibole2
                                    
                                    "{b}Dostarcz Krówkę (15min){/b}" if mleczarz_social_link == 5 and krowka == 1:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz6
                                    
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
        if timer >= 360 and timer <= 1200:       
            scene bg black with fade
            scene bg granica with fade

        if timer >= 1800 and timer <= 2640:
            scene bg black with fade
            scene bg granica2 with fade

        if timer >= 3240 and timer <= 4080:
            scene bg black with fade
            scene bg granica3 with fade

        if timer >= 4680 and timer <= 5520:
            scene bg black with fade
            scene bg granica4 with fade

        if timer >= 6120 and timer <= 6960:
            scene bg black with fade
            scene bg granica5 with fade

        if timer >= 7560 and timer <= 8400:
            scene bg black with fade
            scene bg granica6 with fade

        if timer >= 9000 and timer <= 9840:
            scene bg black with fade
            scene bg granica7 with fade

        if timer >= 10440 and timer <= 11280:
            scene bg black with fade
            scene bg granica8 with fade

        if timer > 1200 and timer < 1800:       
            scene bg black with fade
            scene bg granica_noc with fade

        if  timer > 2640 and timer < 3240:
            scene bg black with fade
            scene bg granica2_noc with fade

        if  timer > 4080 and timer < 4680:
            scene bg black with fade
            scene bg granica3_noc with fade

        if  timer > 5520 and timer < 6120:
            scene bg black with fade
            scene bg granica4_noc with fade

        if  timer > 6960 and timer < 7560:
            scene bg black with fade
            scene bg granica5_noc with fade

        if  timer > 8400 and timer < 9000:
            scene bg black with fade
            scene bg granica6_noc with fade

        if  timer > 9840 and timer < 10440:
            scene bg black with fade
            scene bg granica7_noc with fade

        if  timer > 11280:
            scene bg black with fade
            scene bg granica8_noc with fade

        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            luszcz "Nie, nie dam rady"
                            jump spanko2  
                            
        if trump_social_link == 0:
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                jump trump1
        
        if trump_social_link == 1 and lopatka == 1:
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/usa.mp3"
                jump trump3
        
        if mleczarz_social_link == 0 and krowka == 1:
            jump mleczarz1
        
        if trump_social_link == 1 and lopatka == 0:
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                jump trump2

        label granica2:
            menu:
                "{i}{image=w} Lipowa (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 15)
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
                
                "{b}🕯️ Cmentarz Żydowski | 24/7{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        $ cmentarz_zydowskix += 1
                        "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                        "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
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

                "{b}🎣 Jezioro (15min) | 24/7{/b}": 
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump jezioro1

                "{b}🏰 Bunkier | 6-20{/b}": 
                    $ bunkierx = 0
                    if urban_social_link == 1:
                        $ bunkierx += 1
                        "{i}Znalazłem przy jeziorze stary bunkier{/i}"
                        "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                    
                    if bunkierx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump granica2

                    else:
                        if bunkierx == 1:
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
                            if bunkierx > 1:
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

        jump fight151

    label after_fight151:
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
    
    label fightx3:
        "po walce 3"
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

