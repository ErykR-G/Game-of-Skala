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
default klubx = 0
default dom_tasmyx = 0
default szkolax = 0
default czerwony_domx = 0
default piwnicax = 0
default fioletowy_domx = 0
default stomatologx = 0
default toxic_domx = 0
default jeziorox = 0

default spanko = 0
default ewento = 0
default info = 0
default muzyczka = 0
default kamala = 0

default raem_wu = 0
default gnoms_wu = 0
default zul_wu = 0

default devroomek = 0
default trumen1 = 0
default trumen2 = 0
default trumen3 = 0
default trumen4 = 0
default trumen5 = 0

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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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
        
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and kamala == 0:
                $ kamala = 1
                jump kamala

        label rynek2:
            window hide
            menu:
                "{i}{image=a} Alejka (10min){/i}":
                    if timer > 9810 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump rynek2
                    
                    if timer > 11357 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump rynek2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 1
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump alejka

                "{i}{image=wa} Słoneczna (10min){/i}":
                    if timer > 9810 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump rynek2
                    
                    if timer > 11357 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump rynek2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 1
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump sloneczna
                
                "{i}{image=d} Parking (10min){/i}":
                    if timer > 11357 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump rynek2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 1
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump parking

                "{i}{image=sd} Bohaterów Września (10min){/i}":
                    if timer > 9810 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump rynek2

                    if timer > 11367 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump rynek2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 1
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
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
                                        if timer > 9770 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        
                                        if timer > 11317 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump rynek2
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
                                        if timer > 9770 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        
                                        if timer > 11317 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump rynek2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump burmistrz1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2
        
                "{b}⛪ Kościół | 7-20{/b}": 
                    if timer > 11362 and timer <= 11377:
                        luszcz "To już czas powstrzymać Referendum!"
                        play sound "audio/sfx/traveling.mp3"
                        scene bg black with fade
                        jump ending1
                    $ kosciolx = 0
                    if timer >= 420 and timer <= 1200 or timer >= 1860 and timer <= 2640 or timer >= 3300 and timer <= 4080 or timer >= 4740 and timer <= 5520 or timer >= 6180 and timer <= 6960 or timer >= 7620 and timer <= 8400 or timer >= 9060 and timer <= 9840 or timer >= 10500:
                        $ ado += 1
                    else:
                        "{i}Kościół jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump rynek2

                    if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
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
                    
                    if timer > 11257 and timer <= 11377:
                        $ kosciolx += 1
                        "{i}Mogę już teraz pójść powstrzymać Referendum...{i}"

                    if kosciolx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump rynek2

                    else:
                        if kosciolx == 1:
                            if timer > 11257 and timer <= 11377:
                                menu:
                                    "{b}Czy chcę powstrzymać Referendum?{/b}"

                                    "{b}Tak{/b}":
                                        luszcz "To już czas powstrzymać Referendum!"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump ending1

                                    "{b}Nie{/b}":
                                        luszcz "jeszcze nie teraz"
                                        jump rynek2

                            if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
                                menu:
                                    "{b}Czy chcę spotkać się z Kościelnym? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9800 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump rynek2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ykosciol = 1
                                        jump kosc1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2
                            
                            if timer >= 6660 and timer <= 6960:
                                menu:
                                    "{b}Czy chcę wziąć udział w koncercie Zenka Martyniuka? (1h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9770 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        $ ykosciol = 1
                                        jump kosc3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2

                        else:
                            if kosciolx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Powstrzymaj Referendum{/b}" if timer > 11257 and timer <= 11377:
                                        luszcz "To już czas powstrzymać Referendum!"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump ending1

                                    "{b}Spotkaj się z Kościelnym (30min){/b}" if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
                                        if timer > 9800 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump rynek2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ykosciol = 1
                                        jump kosc1
                                    
                                    "{b}Weź udział w koncercie Zenka Martyniuka (1h){/b}" if timer >= 6660 and timer <= 6960:
                                        if timer > 9770 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump rynek2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        $ ykosciol = 1
                                        jump kosc3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump rynek2
 
    label sloneczna:
        show screen secret_choice
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
                hide screen secret_choice
                jump silver_sextape4
                
        else:
            scene bg black with fade
            scene bg sloneczna_noc with fade
        
        if duda_timer == 0 and duda_miecz == 0:
            hide screen secret_choice
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            hide screen secret_choice
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
            $ spanko += 1
            if spanko == 1:
                play music "audio/music/pole_noc.mp3"
                luszcz "Robię się troszkę śpiący..."
            else:
                if spanko == 5:
                    luszcz "Jezu jestem mega śpiący..."
                else:
                    if spanko == 9:
                        hide screen secret_choice
                        luszcz "Nie, nie dam rady"
                        jump spanko2
                    else:
                        if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                            hide screen secret_choice
                            luszcz "Nie, nie dam rady"
                            jump spanko2  

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and trumen5 == 0:
                $ trumen5 = 1
                hide screen secret_choice
                jump trumen5

        label sloneczna2:
            show screen secret_choice
            window hide
            menu:      
                "{i}{image=sd} Rynek (10min){/i}":
                    hide screen secret_choice
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 1
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump rynek
                
                "{b}🏗️ Plac Budowy | 6-18 {/b}":
                    hide screen secret_choice
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
                                    "{b}Czy chcę spotkać się z Burmistrzem? (3h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9580 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11187 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump burmistrz2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                            
                            if allozaur_social_link == 0:
                                menu:
                                    "{b}Czy chcę sprawdzic co wydaje te ryki? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ yplac = 1
                                        $ timer += 15
                                        jump allozaur1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                            
                            if allozaur_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Allozaurem? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ yplac = 1
                                        jump allozaur1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2

                        else:
                            if placx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Burmistrzem (3h){/b}" if burmistrz_social_link == 1:
                                        if timer > 9580 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11187 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump burmistrz2

                                    "{b}Sprawdź co wydaje te ryki (15min){/b}" if allozaur_social_link == 0:
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ yplac = 1
                                        jump allozaur1
                                    
                                    "{b}Spotkaj się z Allozaurem (15min){/b}" if allozaur_social_link == 1:
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ yplac = 1
                                        jump allozaur1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
        
                "{b}🪩 Klub Seniora GROTA | 16-22{/b}":
                    hide screen secret_choice
                    $ klubx = 0
                    if timer >= 960 and timer <= 1320 or timer >= 2400 and timer <= 2760 or timer >= 3840 and timer <= 4200 or timer >= 5280 and timer <= 5640 or timer >= 6720 and timer <= 7080 or timer >= 8160 and timer <= 8520 or timer >= 9600 and timer <= 9960 or timer >= 11040 and timer <= 11400:
                        $ ado += 1
                    else:
                        "{i}Klub Seniora GROTA jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump sloneczna2

                    if silver_sextape_social_link == 1:
                        $ klubx  += 1
                        "{i}W klubie czeka na mnie Taśma, którą spotkałem przed monopolowym{/i}"
                        "{i}Ma chyba do mnie jakąś ważną sprawę{/i}"
                    
                    if kazuma_social_link == 2:
                        $ klubx  += 1
                        "{i}W klubie czeka na mnie Kazuma, któremu pożyczyłem pieniądze na gambling{/i}"

                    if klubx  == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump sloneczna2

                    else:
                        if klubx == 1:
                            if silver_sextape_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Taśmą? (1h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11307 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump silver_sextape2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                            
                            if kazuma_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Kazumą? (3h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9580 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11127 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump kazuma3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                        
                        else:
                            if klubx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Taśmą (1h){/b}" if silver_sextape_social_link == 1:
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11307 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump silver_sextape2
                                    
                                    "{b}Spotkaj się z Kazumą (3h){/b}" if kazuma_social_link == 2:
                                        if timer > 9580 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11127 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump kazuma3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2

                "{b}🏡 Różowy Dom | 9-19 {/b}" if mleczarz_social_link > 1 or mleczarz_social_link == 1 and krowka == 1:
                    hide screen secret_choice
                    $ fioletowy_domx = 0
                    if timer >= 540 and timer <= 1140 or timer >= 1980 and timer <= 2580 or timer >= 3420 and timer <= 4020 or timer >= 4860 and timer <= 5460 or timer >= 6300 and timer <= 6900 or timer >= 7740 and timer <= 8340 or timer >= 9180 and timer <= 9780 or timer >= 10620 and timer <= 11220:
                        $ ado += 1
                    else:
                        "{i}Mam dostraczyć do tego domu krówkę...{/i}"
                        "{i}Jednak jest na to za późna godzina{/i}"
                        "{i}Muszę przyjść tu o wcześniejszej godzinie{/i}"
                        jump sloneczna2
                        
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
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
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
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump sloneczna2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump sloneczna2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump sloneczna2
                
                "{b}🚏 Przystanek (10min) | 24/7 {/b}":
                    hide screen secret_choice
                    if timer > 9810 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump sloneczna2
                    
                    if timer > 11357 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump sloneczna2
                    if bilbo_social_link == 0:       
                        if timer >= 360 and timer <= 1190 or timer >= 1800 and timer <= 2630 or timer >= 3240 and timer <= 4070 or timer >= 4680 and timer <= 5510 or timer >= 6120 and timer <= 6950 or timer >= 7560 and timer <= 8390 or timer >= 9000 and timer <= 9830 or timer >= 10440 and timer <= 11270:
                            luszcz "Widzę w oddali jakiegoś ziomka w łachmanach i z gołymi stopami"
                            luszcz "Wygląda jakby czegoś szókał… może uda mi się mu pomuc"
                            play sound "audio/sfx/traveling.mp3"
                            scene bg black with fade
                            $ timer += 10
                            jump bilbo2
                        else:
                            play sound "audio/sfx/traveling.mp3"
                            scene bg black with fade
                            $ timer += 10
                            jump bilbo1
                    else:
                        luszcz "Nie ma tu nic do roboty"
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and trumen3 == 0:
                $ trumen3 = 1
                jump trumen3

        label alejka2:
            window hide
            menu:      
                "{i}{image=d} Rynek (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 1
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump rynek
                
                "{b}🛒 Sklep Monopolowy (60min) | 6-23{/b}" if zyd_social_link == 0:
                    if timer > 9700 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump alejka2
                    
                    if timer > 11247 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump alejka2
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
                    if timer > 9805 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump alejka2
                    
                    if timer > 11352 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump alejka2
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
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11307 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
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
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11307 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
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
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ dom_tasmyx += 1
                            "{i}Taśma czeka na mnie, by przedłużyć wspólnie gatunek{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Taśmy{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump alejka2
                    
                    if dom_tasmyx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump alejka2

                    else:
                        if dom_tasmyx == 1:
                            if silver_sextape_social_link == 2:
                                menu:
                                    "{b}Czy chcę spotkać się z Taśmą (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump silver_sextape3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump alejka2

                        else:
                            if dom_tasmyx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Taśmą (2h){/b}" if silver_sextape_social_link == 2:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
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
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
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
                                        if timer > 9805 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump alejka2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump alejka2
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if mleczarz_social_link == 4 and krowka == 1:
            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                "{i}Mam dostraczyć gdzieś tutaj krówkę...{/i}"
                jump mleczarz5

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and trumen2 == 0:
                $ trumen2 = 1
                jump trumen2

        label parking2:
            window hide
            menu:
                "{i}{image=wa} Wolbromska (20min){/i}":
                    if timer > 9800 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump parking2
                    
                    if timer > 11327 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump parking2

                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 1
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump wolbromska
                
                "{i}{image=a} Rynek (10min){/i}":
                    if timer > 9820 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump parking2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 1
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump rynek
                
                "{b}🩺 Apteka (15min) | 8-20{/b}" if gotka_social_link > 10 or gotka_social_link < 10:
                    if timer > 9825 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump parking2
                    
                    if timer > 11352 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump parking2
                    if timer >= 480 and timer <= 1200 or timer >= 1920 and timer <= 2640 or timer >= 3360 and timer <= 4080 or timer >= 4800 and timer <= 5520 or timer >= 6240 and timer <= 6960 or timer >= 7680 and timer <= 8400 or timer >= 9120 and timer <= 9840 or timer >= 10560 and timer <= 11280:
                        $ ado += 1
                    else:
                        "{i}Apteka jest obecnie zamknięta{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump parking2

                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    if kazuma_strzal <= 2 and ailbib == 1:
                        jump gotka8
                    else:
                        if kazuma_strzal <= 2 and kazuma_strzal > 0 and ailbib == 0:
                            "{i}Żeby uratować Kazume muszę znaleźć księgę czarnej magii{/i}"
                            "{i}Niestety nadal jej nie znalazłem...{/i}"
                            jump parking2
                        else:
                            if kazuma_strzal == 0 and kazuma_social_link < 100:
                                jump gotka8
                            else:
                                if gotka_szpan > 0 or gotka_social_link > 0:
                                    jump gotka2
                                else:
                                    jump gotka1
                
                "{b}🩺 Apteka | ZAMKNIĘTE{/b}" if gotka_social_link == 10:
                    "{i}Apteka jest zamknięta{/i}"
                    jump parking2

                "{b}🏡 Dom | 24/7{/b}": 
                    if timer > 9825 and timer <= 9840:
                        luszcz "Ehhhh, czas iść na ten Bal"
                        play sound "audio/sfx/traveling.mp3"
                        scene bg black with fade
                        jump bal2
                    $ domx = 0        
                    if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                        $ domx += 1
                        "{i}Robię się trochę śpiący...{/i}"

                    if (babcia_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                        $ domx += 1
                        "{i}Mam dla Babci przynieść memy, by uszyła mi z nich szalik...{/i}"
                    
                    if (kazuma_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                        $ domx += 1
                        "{i}Pozwoliłem Kazumie ukryć się przed Urzędem Skarbowym w moim domu{/i}"
                        "{i}Powinienem z nim porozmawiać co robimy dalej...{/i}"
                    
                    if (drukarka3d_social_link == 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                        $ domx += 1
                        "{i}Mam w pokoju drukarkę 3d{/i}"
                        "{i}Może mógłbym coś nią wydrukować...{/i}"
                    
                    if (drukarka3d_social_link == 1 and czasd <= 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                        $ domx += 1
                        "{i}Drukarka 3d skończyła drukować...{/i}"
                    
                    if (yusuke_social_link >= 1 and yusuke_social_link <= 4 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1170) or (timer >= 1800 and timer <= 2610) or (timer >= 3240 and timer <= 4050) or (timer >= 4680 and timer <= 5490) or (timer >= 6120 and timer <= 6930) or (timer >= 7560 and timer <= 8370) or (timer >= 9000 and timer <= 9810) or (timer >= 10440 and timer <= 11250)):
                        $ domx += 1
                        "{i}Yusuke poprosił mnie o pomoc w poszukiwaniu inspiracji do jego obrazu{/i}"
                    
                    if (yusuke_social_link >= 1 and yusuke_social_link <= 5 and yusuke_timer >= timer) and ((timer >= 360 and timer <= 1170) or (timer >= 1800 and timer <= 2610) or (timer >= 3240 and timer <= 4050) or (timer >= 4680 and timer <= 5490) or (timer >= 6120 and timer <= 6930) or (timer >= 7560 and timer <= 8370) or (timer >= 9000 and timer <= 9810) or (timer >= 10440 and timer <= 11250)):
                        "{i}Yusuke poprosił mnie o pomoc w poszukiwaniu inspiracji do jego obrazu{/i}"
                        "{i}Jednak teraz jest chyba za bardzo zajęty po naszym ostatnim wyjściu...{/i}"
                    
                    if (yusuke_social_link == 5 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1140) or (timer >= 1800 and timer <= 2580) or (timer >= 3240 and timer <= 4020) or (timer >= 4680 and timer <= 5460) or (timer >= 6120 and timer <= 6900) or (timer >= 7560 and timer <= 8340) or (timer >= 9000 and timer <= 9785) or (timer >= 10440 and timer <= 11220)):
                        $ domx += 1
                        "{i}Yusuke skończył poszukiwania inspiracji do swojego obrazu{/i}"

                    if ((timer >= 360 and timer <= 1080) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                        $ ado += 1
                    else:
                        if babcia_social_link == 1:
                            "{i}Mam dla Babci przynieść memy, by uszyła mi z nich szalik...{/i}"
                            "{i}Jednakże jestem na to za śpiący{/i}"

                        if kazuma_social_link == 1:
                            "{i}Pozwoliłem Kazumie ukryć się przed Urzędem Skarbowym w moim domu{/i}"
                            "{i}Powinienem z nim porozmawiać co robimy dalej...{/i}"
                            "{i}Jednakże teraz jestem na to za śpiący{/i}"
                    
                    if timer > 9720 and timer <= 9840:
                        $ domx += 1
                        "{i}Mogę już teraz iść na Bal...{i}"

                    if domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump parking2

                    else:
                        if domx == 1:
                            if timer > 9720 and timer <= 9840:
                                menu:
                                    "{b}Czy chcę iść na Bal?{/b}"

                                    "{b}Tak{/b}":
                                        luszcz "Ehhhh, czas iść na ten Bal"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump bal2

                                    "{b}Nie{/b}":
                                        luszcz "jeszcze nie teraz"
                                        jump parking2

                            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                                menu:
                                    "{b}Czy chcę iść spać?{/b}"

                                    "{b}Tak{/b}":
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                            if (babcia_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                menu:
                                    "{b}Czy chcę pobrać memy? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if (kazuma_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                menu:
                                    "{b}Czy chcę spotkać się z Kazumą? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump kazuma2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if (drukarka3d_social_link == 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                menu:
                                    "{b}Czy chcę użyć drukarki 3d? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump drukarka3d1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if (drukarka3d_social_link == 1 and czasd <= 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                menu:
                                    "{b}Czy chcę odebrać wydrukowany miecz? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump drukarka3d2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if (yusuke_social_link >= 1 and yusuke_social_link <= 4 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1170) or (timer >= 1800 and timer <= 2610) or (timer >= 3240 and timer <= 4050) or (timer >= 4680 and timer <= 5490) or (timer >= 6120 and timer <= 6930) or (timer >= 7560 and timer <= 8370) or (timer >= 9000 and timer <= 9810) or (timer >= 10440 and timer <= 11250)):
                                menu:
                                    "{b}Czy chcę spotkać się z Yusuke? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump yusuke1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if (yusuke_social_link == 5 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1140) or (timer >= 1800 and timer <= 2580) or (timer >= 3240 and timer <= 4020) or (timer >= 4680 and timer <= 5460) or (timer >= 6120 and timer <= 6900) or (timer >= 7560 and timer <= 8340) or (timer >= 9000 and timer <= 9785) or (timer >= 10440 and timer <= 11220)):
                                menu:
                                    "{b}Czy chcę spotkać się z Yusuke? (3h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9660 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11187 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 180
                                        jump yusuke2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                        else:
                            if domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Idź na Bal{/b}" if timer > 9720 and timer <= 9840:
                                        luszcz "Ehhhh, czas iść na ten Bal"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump bal2

                                    "{b}Idź spać{/b}" if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump spanko
                                    
                                    "{b}Pobierz memy (30min){/b}" if (babcia_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia2

                                    "{b}Spotkaj się z Kazumą (15min){/b}" if (kazuma_social_link == 1) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump kazuma2
                                    
                                    "{b}Użyj drukarki 3d (30min){/b}" if (drukarka3d_social_link == 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump drukarka3d1
                                    
                                    "{b}Odbierz wydrukowany miecz (30min){/b}" if (drukarka3d_social_link == 1 and czasd <= 0) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                        if timer > 9810 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump drukarka3d2
                                    
                                    "{b}Spotkaj się z Yusukę (15min){/b}" if (yusuke_social_link >= 1 and yusuke_social_link <= 4 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1170) or (timer >= 1800 and timer <= 2610) or (timer >= 3240 and timer <= 4050) or (timer >= 4680 and timer <= 5490) or (timer >= 6120 and timer <= 6930) or (timer >= 7560 and timer <= 8370) or (timer >= 9000 and timer <= 9810) or (timer >= 10440 and timer <= 11250)):
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump yusuke1
                                    
                                    "{b}Spotkaj się z Yusukę (3h){/b}" if (yusuke_social_link == 5 and yusuke_timer <= timer) and ((timer >= 360 and timer <= 1140) or (timer >= 1800 and timer <= 2580) or (timer >= 3240 and timer <= 4020) or (timer >= 4680 and timer <= 5460) or (timer >= 6120 and timer <= 6900) or (timer >= 7560 and timer <= 8340) or (timer >= 9000 and timer <= 9785) or (timer >= 10440 and timer <= 11220)):
                                        if timer > 9660 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        if timer > 11187 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        scene bg black with fade
                                        $ timer += 180
                                        jump yusuke2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2

                "{b}🦷 Stomatolog | 12-19{/b}":
                    $ stomatologx = 0
                    if timer >= 720 and timer <= 1140 or timer >= 2160 and timer <= 2580 or timer >= 3600 and timer <= 4020 or timer >= 5040 and timer <= 5460 or timer >= 6480 and timer <= 6900 or timer >= 7920 and timer <= 8340 or timer >= 9360 and timer <= 9780 or timer >= 10800 and timer <= 11220:
                        $ ado += 1
                    else:
                        "{i}Stomatolog jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump parking2

                    if mleczarz_social_link == 3 and krowka == 1:
                        $ stomatologx += 1
                        "{i}Mam dostraczyć tutaj krówkę...{/i}"

                    if duda_social_link == 0:
                        $ stomatologx += 1
                        "{i}Chyba Mama ma u siebie jakiegoś klienta{/i}"
                        "{i}Może mógłbym zobaczyć kto to jest...{/i}"
                    
                    if stomatologx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump parking2

                    else:
                        if stomatologx == 1:
                            if mleczarz_social_link == 3 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                            
                            if duda_social_link == 0:
                                menu:
                                    "{b}Czy chcę zobaczyć kto jest u stomatologa? (1h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9720 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump duda1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump parking2
                                    

                        else:
                            if stomatologx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Dostarcz Krówkę (15min){/b}" if mleczarz_social_link == 3 and krowka == 1:
                                        if timer > 9825 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        jump mleczarz4
                                    
                                    "{b}Zobacz kto jest u stomatologa (1h){/b}" if duda_social_link == 0:
                                        if timer > 9720 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump parking2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump parking2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        jump duda1
                                    
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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
            window hide
            menu:
                "{i}{image=sd} Parking (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 1
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump parking
                
                "{b}🏡 Dom Toxic Pea | 20–24{/b}" if toxic_pea_social_link > 0 and toxic_pea_social_link < 10:
                    $ toxic_domx = 0        
                    if toxic_pea_social_link == 1 and toxic_limit == 0:
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ toxic_domx += 1
                            "{i}Tutaj mieszka Toxic Pea, którego spotkałem na Kebabie{/i}"
                            "{i}Zaproponował mi byśmy razem pozabijali zombiaczki...{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Toxic Pea{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump wolbromska2
                    
                    if toxic_pea_social_link == 2 and toxic_limit == 0:
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ toxic_domx += 1
                            "{i}Ostatnio zabijałem tutaj zombiaczki razem z Toxic Pea{/i}"
                            "{i}Zaproponował mi byśmy zrobili to jeszcze raz...{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Toxic Pea{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump wolbromska2
                    
                    if toxic_pea_social_link == 3 and toxic_limit == 0:
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ toxic_domx += 1
                            "{i}Ostatnio zabijałem tutaj zombiaczki i robiłem inne rzeczy razem z Toxic Pea{/i}"
                            "{i}Zaproponował mi byśmy zrobili to jeszcze raz...{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Toxic Pea{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump wolbromska2
                    
                    if toxic_pea_social_link == 4 and toxic_limit == 0:
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ toxic_domx += 1
                            "{i}Ostatnio zabijałem tutaj zombiaczki i robiłem inne rzeczy razem z Toxic Pea{/i}"
                            "{i}Zaproponował mi byśmy zrobili to jeszcze raz...{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Toxic Pea{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump wolbromska2
                    
                    if toxic_pea_social_link == 5 and toxic_limit == 0:
                        if timer > 1200 and timer < 1440 or timer > 2640 and timer < 2880 or timer > 4080 and timer < 4320 or timer > 5520 and timer < 5760 or timer > 6960 and timer < 7200 or timer > 8400 and timer < 8640 or timer > 9840 and timer < 1080 or timer > 11280:
                            $ toxic_domx += 1
                            "{i}Ostatnio zabijałem tutaj zombiaczki i robiłem inne rzeczy razem z Toxic Pea{/i}"
                            "{i}Zaproponował mi byśmy zrobili to jeszcze raz...{/i}"
                        else:
                            "{i}Obecnie nie ma nikogo w Domu Toxic Pea{/i}"
                            "{i}Muszę przyjść tu o odpowiedniej porze...{/i}"
                            jump wolbromska2

                    if toxic_domx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if toxic_domx == 1:
                            if toxic_pea_social_link == 1 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if toxic_pea_social_link == 2 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if toxic_pea_social_link == 3 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if toxic_pea_social_link == 4 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if toxic_pea_social_link == 5 and toxic_limit == 0:
                                menu:
                                    "{b}Czy chcę spotkać się z Toxic Pea? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea5

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                        else:
                            if toxic_domx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"
                                    
                                    "{b}Spotkaj się z Toxic Pea (2h){/b}" if toxic_pea_social_link == 1 and toxic_limit == 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea1
                                    
                                    "{b}Spotkaj się z Toxic Pea (2h){/b}" if toxic_pea_social_link == 2 and toxic_limit = 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea2
                                    
                                    "{b}Spotkaj się z Toxic Pea (2h){/b}" if toxic_pea_social_link == 3 and toxic_limit = 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea3
                                    
                                    "{b}Spotkaj się z Toxic Pea (2h){/b}" if toxic_pea_social_link == 4 and toxic_limit = 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea4
                                    
                                    "{b}Spotkaj się z Toxic Pea (2h){/b}" if toxic_pea_social_link == 5 and toxic_limit = 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump toxic_pea5
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                "{b}🐄 Mleczarnia (15min) | 8–16{/b}": 
                    if timer > 9805 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump wolbromska2
                    
                    if timer > 11332 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump wolbromska2
                    if mleczarz_social_link == 7:
                        "{i}Mleczarz już tutaj nie pracuje{/i}"
                        "{i}Dzięki mnie mógł w spokoju przejść na emeryture{/i}"
                        jump wolbromska2
                    
                    if timer >= 480 and timer <= 960 or timer >= 1920 and timer <= 2400 or timer >= 3360 and timer <= 3840 or timer >= 4800 and timer <= 5280 or timer >= 6240 and timer <= 6720 or timer >= 7680 and timer <= 8160 or timer >= 9120 and timer <= 9600 or timer >= 10560 and timer <= 11040:
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
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yskalka = 1
                                        jump skalka1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                            
                            if wazon_wezy == 1:
                                menu:
                                    "{b}Czy chcę pomedytować z wazonem z wężami? (30min){/b}" 

                                    "{b}Tak{/b}":
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yskalka = 1
                                        jump skalka2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2
                        
                        else:
                            if skalax > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"
                                    
                                    "{b}Popełnij Samobójstwo (30min){/b}" if samobojstwo == 0:
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yskalka = 1
                                        jump skalka1
                                    
                                    "{b}Pomedytuj z wazonem z wężami (30min){/b}" if wazon_wezy == 1:
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yskalka = 1
                                        jump skalka2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                "{b}🌀 Portal | 6–20{/b}": 
                    $ portalx = 0
                    if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            $ portalx += 1
                            "{i}Przy portalu zapewne czeka na mnie Naofumi...{/i}"
                        else:
                            "{i}Mam się spotkać przy portalu z Naofumim, by odnaleźć jego dog girl{/i}"
                            "{i}Ale jest na to za późna godzina...{/i}"
                            jump wolbromska2
                    
                    if portalx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump wolbromska2

                    else:
                        if portalx == 1:
                            if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                                menu:
                                    "{b}Czy chcę się spotkać z Naofumim? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump tarczownik2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump wolbromska2

                        else:
                            if portalx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Naofumim (2h){/b}" if tarczownik_social_link == 1 and tarczownik_dzien == 0:
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump wolbromska2
                                        
                                        if timer > 11227 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump wolbromska2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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
        
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and trumen4 == 0:
                $ trumen4 = 1
                jump trumen4

        label bohaterow_wrzesnia2:
            window hide
            menu:
                "{i}{image=wa} Rynek (10min){/i}":
                    if timer > 11367 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump bohaterow_wrzesnia2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 1
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump rynek

                "{i}{image=sa} Lipowa (10min){/i}":
                    if timer > 9800 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump bohaterow_wrzesnia2
                    
                    if timer > 11357 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump bohaterow_wrzesnia2

                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 1
                            $ granica = 0
                            jump walka_uliczna
                    jump lipowa
        
                "{b}🛒 Kebab (15min) | 11–23{/b}":
                    if timer > 9805 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump bohaterow_wrzesnia2
                    
                    if timer > 11362 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump bohaterow_wrzesnia2

                    if timer >= 660 and timer <= 1380 or timer >= 2100 and timer <= 2820 or timer >= 3540 and timer <= 4260 or timer >= 4980 and timer <= 5700 or timer >= 6420 and timer <= 7140 or timer >= 7860 and timer <= 8580 or timer >= 9300 and timer <= 10020 or timer >= 10740 and timer <= 11460:
                        $ ado += 1
                    else:
                        "{i}Kebab jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump bohaterow_wrzesnia2
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump kebab
                
                "{b}🏡 Czerwony Dom | 9–19{/b}" if mleczarz_social_link > 2 or mleczarz_social_link == 2 and krowka == 1:
                    $ czerwony_domx = 0   
                    if timer >= 540 and timer <= 1140 or timer >= 1980 and timer <= 2580 or timer >= 3420 and timer <= 4020 or timer >= 4860 and timer <= 5460 or timer >= 6300 and timer <= 6900 or timer >= 7740 and timer <= 8340 or timer >= 9180 and timer <= 9780 or timer >= 10620 and timer <= 11220:
                        $ ado += 1
                    else:
                        "{i}Mam dostraczyć do tego domu krówkę...{/i}"
                        "{i}Jednak jest na to za późna godzina{/i}"
                        "{i}Muszę przyjść tu o wcześniejszej godzinie{/i}"
                        jump bohaterow_wrzesnia2

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
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11257 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
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
                                        if timer > 9700 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11257 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
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
                                        if timer > 9520 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11077 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
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
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
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
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
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
                                        if timer > 9520 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11077 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        jump urban1
                                    
                                    "{b}Sprawdź sytuacje w domu kultury (30min){/b}" if urban_social_link > 0 and babcia_social_link == 0 and akcja1 == 0:
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia1
                                    
                                    "{b}Spotkaj się z Babcią (30min){/b}" if babcia_social_link == 2:
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump babcia3
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                "{b}⛪ Kościół | 7–20{/b}": 
                    if timer > 11362 and timer <= 11377:
                        luszcz "To już czas powstrzymać Referendum!"
                        play sound "audio/sfx/traveling.mp3"
                        scene bg black with fade
                        jump ending1

                    $ kosciolx = 0
                    if timer >= 420 and timer <= 1200 or timer >= 1860 and timer <= 2640 or timer >= 3300 and timer <= 4080 or timer >= 4740 and timer <= 5520 or timer >= 6180 and timer <= 6960 or timer >= 7620 and timer <= 8400 or timer >= 9060 and timer <= 9840 or timer >= 10500:
                        $ ado += 1
                    else:
                        "{i}Kościół jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump bohaterow_wrzesnia2
                        
                    if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
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
                    
                    if timer > 11257 and timer <= 11377:
                        $ kosciolx += 1
                        "{i}Mogę już teraz pójść powstrzymać Referendum...{i}"
                    
                    if kosciolx == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump bohaterow_wrzesnia2

                    else:
                        if kosciolx == 1:
                            if timer > 11257 and timer <= 11377:
                                menu:
                                    "{b}Czy chcę powstrzymać Referendum?{/b}"

                                    "{b}Tak{/b}":
                                        luszcz "To już czas powstrzymać Referendum!"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump ending1

                                    "{b}Nie{/b}":
                                        luszcz "jeszcze nie teraz"
                                        jump rynek2

                            if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
                                menu:
                                    "{b}Czy chcę spotkać się z Kościelnym? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ykosciol = 1
                                        jump kosc1

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2
                            
                            if timer >= 6660 and timer <= 6960:
                                menu:
                                    "{b}Czy chcę wziąć udział w koncercie Zenka Martyniuka? (1h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        $ ykosciol = 1
                                        jump kosc3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump bohaterow_wrzesnia2

                        else:
                            if kosciolx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Powstrzymaj Referendum{/b}" if timer > 11257 and timer <= 11377:
                                        luszcz "To już czas powstrzymać Referendum!"
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump ending1

                                    "{b}Spotkaj się z Kościelnym (30min){/b}" if kosc_social_link == 0 and koscielny_zyje == 0 and timer <= 11280:
                                        if timer > 9790 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        if timer > 11347 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ykosciol = 1
                                        jump kosc1
                                    
                                    "{b}Weź udział w koncercie Zenka Martyniuka (1h){/b}" if timer >= 6660 and timer <= 6960:
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump bohaterow_wrzesnia2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        $ ykosciol = 1
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia
        
        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc
        
        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            $ kostka = renpy.random.randint(1, 100)
            if kostka >= 1 and kostka <= 3 and trumen1 == 0:
                $ trumen1 = 1
                jump trumen1

        label lipowa2:
            window hide
            menu:
                "{i}{image=wd} Bohaterów Września (10min){/i}":
                    $ timer += 10
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 1
                            $ lipowa = 0
                            $ granica = 0
                            jump walka_uliczna
                    jump bohaterow_wrzesnia

                "{i}{image=s} Granica Skały (20min){/i}":
                    if timer > 9770 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump lipowa2
                    
                    if timer > 11327 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump lipowa2

                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 0
                            $ granica = 1
                            jump walka_uliczna
                    jump granica
                
                "{b}🪦 Cmentarz | 24/7{/b}":
                    $ cmentarzx = 0
                    if zyd_social_link == 3 and lopatka == 1:
                        if timer >= 360 and timer <= 960 or timer >= 1800 and timer <= 2400 or timer >= 3240 and timer <= 3840 or timer >= 4680 and timer <= 5280 or timer >= 6120 and timer <= 6720 or timer >= 7560 and timer <= 8160 or timer >= 9000 and timer <= 9600 or timer >= 10440 and timer <= 11040:
                            $ cmentarzx += 1
                            "{i}Na cmentarzu czeka na mnie Żyd, z którym zamierzamy wykopać prochy jego dziadka{/i}"
                            "{i}Miałem w tym celu znaleźć łopatkę, co udało mi się wykonać{/i}"
                        else:
                            "{i}Na cmentarzu czeka na mnie Żyd, z którym zamierzamy wykopać prochy jego dziadka{/i}"
                            "{i}Miałem w tym celu znaleźć łopatkę, co udało mi się wykonać{/i}"
                            "{i}Ale teraz jest na to za późna godzina...{/i}"

                    if zyd_social_link == 3 and lopatka == 0:
                        "{i}Na cmentarzu czeka na mnie żyd, ale nadal nie zdobyłem dla niego łopatki{/i}"
                        "{i}Muszę się tym zająć zanim się z nim spotkam{/i}"
                    
                    if zyd_social_link == 2:
                        if timer >= 360 and timer <= 1185 or timer >= 1800 and timer <= 2625 or timer >= 3240 and timer <= 4065 or timer >= 4680 and timer <= 5505 or timer >= 6120 and timer <= 6945 or timer >= 7560 and timer <= 8385 or timer >= 9000 and timer <= 9825 or timer >= 10440 and timer <= 11265:
                            $ cmentarzx += 1
                            "{i}Żyd czeka na mnie pod kwaterą żołnierzy 1 wojny światowej{/i}"
                            "{i}Mamy razem wykopać zwłoki jego pra-pra-dziadka{/i}"
                        else:
                            "{i}Mam się spotkać z Żydem pod kwaterą żołnierzy 1 wojny światowej{/i}"
                            "{i}Ale teraz jest na to za późna godzina...{/i}"
                    
                    if harambe_social_link == 0:
                        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                            $ cmentarzx += 1
                            "{i}Mogę pójść na nocny spacer po cmentarzu...{/i}"
                            "{i}To napewno świetny pomysł{/i}"
                    
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
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump lipowa2

                    else:
                        if cmentarzx == 1:
                            if (zyd_social_link == 3 and lopatka == 1) and ((timer >= 360 and timer <= 960) or (timer >= 1800 and timer <= 2400) or (timer >= 3240 and timer <= 3840) or (timer >= 4680 and timer <= 5280) or (timer >= 6120 and timer <= 6720) or (timer >= 7560 and timer <= 8160) or (timer >= 9000 and timer <= 9600) or (timer >= 10440 and timer <= 11040)):
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (4h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9450 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11007 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ ycmentarz = 1
                                        $ timer += 240
                                        jump zyd4

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if (zyd_social_link == 2) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9795 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ ycmentarz = 1
                                        jump zyd3

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if harambe_social_link == 0:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy chcę iść na spacer? (30min){/b}"

                                        "{b}Tak{/b}":
                                            if timer > 9780 and timer <= 9840:
                                                luszcz "Nie zdąże tego zrobić przed Balem"
                                                jump lipowa2
                                            
                                            if timer > 11337 and timer <= 11377:
                                                luszcz "Nie zdąże tego zrobić przed Referendum"
                                                jump lipowa2
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 30
                                            $ ycmentarz = 1
                                            jump harambe1

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump lipowa2

                            if harambe_social_link == 1 and kosc_social_link == 3:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy poprosić Harambe o pomoc? (30min){/b}"

                                        "{b}Tak{/b}":
                                            if timer > 9780 and timer <= 9840:
                                                luszcz "Nie zdąże tego zrobić przed Balem"
                                                jump lipowa2
                                            
                                            if timer > 11337 and timer <= 11377:
                                                luszcz "Nie zdąże tego zrobić przed Referendum"
                                                jump lipowa2
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 30
                                            $ ycmentarz = 1
                                            jump kosc4

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump lipowa2
                            
                            if harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or harambe_social_link == 2 and kosc_social_link == 3 and cialo == 1 and ailbib == 1:
                                if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                                    menu:
                                        "{b}Czy wskrzesić Kościelnego? (1h){/b}"

                                        "{b}Tak{/b}":
                                            if timer > 9750 and timer <= 9840:
                                                luszcz "Nie zdąże tego zrobić przed Balem"
                                                jump lipowa2
                                            
                                            if timer > 11307 and timer <= 11377:
                                                luszcz "Nie zdąże tego zrobić przed Referendum"
                                                jump lipowa2
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            $ timer += 60
                                            $ ycmentarz = 1
                                            jump kosc5

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump lipowa2
                        else:
                            if cmentarzx > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Żydem (4h){/b}" if (zyd_social_link == 3 and lopatka == 1) and ((timer >= 360 and timer <= 960) or (timer >= 1800 and timer <= 2400) or (timer >= 3240 and timer <= 3840) or (timer >= 4680 and timer <= 5280) or (timer >= 6120 and timer <= 6720) or (timer >= 7560 and timer <= 8160) or (timer >= 9000 and timer <= 9600) or (timer >= 10440 and timer <= 11040)):
                                        if timer > 9450 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11007 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 240
                                        $ ycmentarz = 1
                                        jump zyd4

                                    "{b}Spotkaj się z Żydem (15min){/b}" if (zyd_social_link == 2) and ((timer >= 360 and timer <= 1185) or (timer >= 1800 and timer <= 2625) or (timer >= 3240 and timer <= 4065) or (timer >= 4680 and timer <= 5505) or (timer >= 6120 and timer <= 6945) or (timer >= 7560 and timer <= 8385) or (timer >= 9000 and timer <= 9825) or (timer >= 10440 and timer <= 11265)):
                                        if timer > 9795 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ ycmentarz = 1
                                        jump zyd3

                                    "{b}Idź na spacer (30min){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 0 or timer > 2640 and timer < 3240 and harambe_social_link == 0 or timer > 4080 and timer < 4680 and harambe_social_link == 0 or timer > 5520 and timer < 6120 and harambe_social_link == 0 or timer > 6960 and timer < 7560 and harambe_social_link == 0 or timer > 8400 and timer < 9000 and harambe_social_link == 0 or timer > 9840 and timer < 10440 and harambe_social_link == 0:
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ycmentarz = 1
                                        jump harambe1
                                    
                                    "{b}Poproś o pomoc Harambe (30min){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 2640 and timer < 3240 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 4080 and timer < 4680 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 5520 and timer < 6120 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 6960 and timer < 7560 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 8400 and timer < 9000 and harambe_social_link == 1 and kosc_social_link == 3 or timer > 9840 and timer < 10440 and harambe_social_link == 1 and kosc_social_link == 3:
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ ycmentarz = 1
                                        jump kosc4
                                    
                                    "{b}Wskrześ Kościelnego (1h){/b}" if timer > 1200 and timer < 1800 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 2640 and timer < 3240 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 4080 and timer < 4680 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 5520 and timer < 6120 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 6960 and timer < 7560 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 8400 and timer < 9000 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 9840 and timer < 10440 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and glowa == 1 or timer > 1200 and timer < 1800 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 2640 and timer < 3240 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 4080 and timer < 4680 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 5520 and timer < 6120 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 6960 and timer < 7560 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 8400 and timer < 9000 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1 or timer > 9840 and timer < 10440 and harambe_social_link == 2 and kosc_social_link == 3 and ailbib == 1 and cialo == 1:
                                        if timer > 9750 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11307 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 60
                                        $ ycmentarz = 1
                                        jump kosc5
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                "{b}🕯️ Cmentarz Żydowski | 24/7{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        if timer >= 360 and timer <= 1185 or timer >= 1800 and timer <= 2625 or timer >= 3240 and timer <= 4065 or timer >= 4680 and timer <= 5505 or timer >= 6120 and timer <= 6945 or timer >= 7560 and timer <= 8385 or timer >= 9000 and timer <= 9825 or timer >= 10440 and timer <= 11265:
                            $ cmentarz_zydowskix += 1
                            "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                            "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                        else:
                            "{i}Mam się spotkać z Żydem na cmentarzu żydowskim{/i}"
                            "{i}Ale teraz jest na to za późna godzina...{/i}"
                            jump lipowa2
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump lipowa2

                    else:
                        if cmentarz_zydowskix == 1:
                            if zyd_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
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
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                "{b}🏫 Szkoła | 8–15{/b}":
                    $ szkolax = 0
                    if timer >= 480 and timer <= 900 or timer >= 1920 and timer <= 2340 or timer >= 3360 and timer <= 3780 or timer >= 4800 and timer <= 5220 or timer >= 6240 and timer <= 6660 or timer >= 7680 and timer <= 8100 or timer >= 9120 and timer <= 9540 or timer >= 10560 and timer <= 10980:
                        $ ado += 1
                    else:
                        "{i}Szkoła jest obecnie zamknięta{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump lipowa2

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
                                    "{b}Czy chcę spotkać się z Kościelnym? (2h){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9690 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        $ yszkola = 1 
                                        jump kosc2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if kibole_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Piotrkiem i Krystianem? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yszkola = 1
                                        jump kibole2

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2
                            
                            if mleczarz_social_link == 5 and krowka == 1:
                                menu:
                                    "{b}Czy chcę dostarczyć krówkę? (15min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9795 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ yszkola = 1
                                        jump mleczarz6

                                    "{b}Nie{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump lipowa2

                        else:
                            if szkolax > 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Kościelnym (2h){/b}" if kosc_social_link == 1 and koscielny_zyje == 0:
                                        if timer > 9690 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11247 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        $ yszkola = 1
                                        jump kosc2
                                    
                                    "{b}Spotkaj się z Piotrkiem i Krystianem (30min){/b}" if kibole_social_link == 1:
                                        if timer > 9780 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11337 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        $ yszkola = 1
                                        jump kibole2
                                    
                                    "{b}Dostarcz Krówkę (15min){/b}" if mleczarz_social_link == 5 and krowka == 1:
                                        if timer > 9795 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump lipowa2
                                        
                                        if timer > 11352 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump lipowa2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 15
                                        $ yszkola = 1
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
        
        if duda_timer == 0 and duda_miecz == 0:
            jump duda_ceremonia

        if timer >= 6120 and timer <= 6960 and koscielny_zyje == 0:
            jump kosc_smierc

        if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440:
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
            jump mleczarz2
        
        if trump_social_link == 1 and lopatka == 0:
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                jump trump2

        label granica2:
            window hide
            menu:
                "{i}{image=w} Lipowa (20min){/i}":
                    $ timer += 20
                    $ kostka = renpy.random.randint(1, 20)
                    if timer <= 9720 or (timer >= 10080 and timer <= 11220):
                        if kostka == 1:
                            $ rynek = 0
                            $ sloneczna = 0
                            $ alejka = 0
                            $ parking = 0
                            $ wolbromska = 0
                            $ bohaterow_wrzesnia = 0
                            $ lipowa = 1
                            $ granica = 0
                            jump walka_uliczna
                    jump lipowa    
                
                "{b}🛒 Chiński Market (15min) | 9–19{/b}":
                    if timer > 9775 and timer <= 9840:
                        luszcz "Bal rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli wracać do domu"
                        jump granica2
                    
                    if timer > 11332 and timer <= 11377:
                        luszcz "Referendum rozpocznie się już za niedługo"
                        luszcz "Powinienem powoli kierować się w kierunku kościoła"
                        jump granica2

                    if timer >= 540 and timer <= 1140 or timer >= 1980 and timer <= 2580 or timer >= 3420 and timer <= 4020 or timer >= 4860 and timer <= 5460 or timer >= 6300 and timer <= 6900 or timer >= 7740 and timer <= 8340 or timer >= 9180 and timer <= 9780 or timer >= 10620 and timer <= 11220:
                        $ ado += 1
                    else:
                        "{i}Chiński Market jest obecnie zamknięty{/i}"
                        "{i}Muszę przyjść tu później...{/i}"
                        jump granica2
                    $ timer += 15
                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    jump chinczyk

                "{b}🕯️ Cmentarz Żydowski | 24/7{/b}": 
                    $ cmentarz_zydowskix = 0
                    if zyd_social_link == 1:
                        if timer >= 360 and timer <= 1185 or timer >= 1800 and timer <= 2625 or timer >= 3240 and timer <= 4065 or timer >= 4680 and timer <= 5505 or timer >= 6120 and timer <= 6945 or timer >= 7560 and timer <= 8385 or timer >= 9000 and timer <= 9825 or timer >= 10440 and timer <= 11265:
                            $ cmentarz_zydowskix += 1
                            "{i}Na cmentarzu żydowskim czeka na mnie Żyd{/i}"
                            "{i}Nie wiem czemu kazał mi tu przyjść{/i}"
                        else:
                            "{i}Mam się spotkać z Żydem na cmentarzu żydowskim{/i}"
                            "{i}Ale teraz jest na to za późna godzina...{/i}"
                            jump granica2
                    
                    if cmentarz_zydowskix == 0:
                        "{i}Nie ma tu teraz nic do roboty{/i}"
                        jump granica2

                    else:
                        if cmentarz_zydowskix == 1:
                            if zyd_social_link == 1:
                                menu:
                                    "{b}Czy chcę spotkać się z Żydem? (30min){/b}"

                                    "{b}Tak{/b}":
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
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
                                        if timer > 9760 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11217 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 30
                                        jump zyd2
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2

                "{b}🎣 Jezioro (2h) | 6-18{/b}" if kazuma_social_link == 0: 
                    $ jeziorox = 0
                    if urban_social_link == 1:
                        if timer >= 540 and timer <= 1080 or timer >= 1980 and timer <= 2520 or timer >= 3420 and timer <= 3980 or timer >= 4860 and timer <= 5400 or timer >= 6300 and timer <= 6840 or timer >= 7740 and timer <= 8280 or timer >= 9180 and timer <= 9720 or timer >= 10620 and timer <= 11160:
                            $ jeziorox += 1
                            "{i}Znalazłem przy jeziorze stary bunkier{/i}"
                            "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                        else:
                            "{i}Znalazłem przy jeziorze stary bunkier{/i}"
                            "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                            "{i}Jednak obecnie jest za późna godzina, by tam iść{/i}"    
                            jump granica2   

                    if timer >= 540 and timer <= 1080 or timer >= 1980 and timer <= 2520 or timer >= 3420 and timer <= 3980 or timer >= 4860 and timer <= 5400 or timer >= 6300 and timer <= 6840 or timer >= 7740 and timer <= 8280 or timer >= 9180 and timer <= 9720 or timer >= 10620 and timer <= 11160:
                        "{i}Rybki, rybki kocham rybki{/i}"
                    else:
                        "{i}Obecnie jest za późna godzina, by tu iść{/i}"
                        "{i}Muszę wrócić tutaj o wcześniejszej porze dnia{/i}"
                        jump granica2
                    
                    if jeziorox == 0:
                        play sound "audio/sfx/traveling.mp3"
                        scene bg black with fade
                        $ timer += 120
                        jump kazuma1

                    else:
                        if jeziorox == 1:
                            if urban_social_link == 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Jerzym Urbanem (2h){/b}" if urban_social_link == 1:
                                        if timer > 9610 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11147 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump urban2
                                    
                                    "{b}Idź na ryby (2h){/b}":
                                        if timer > 9610 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11147 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump kazuma1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2

                "{b}🎣 Jezioro (15min) | 24/7{/b}" if kazuma_social_link > 0: 
                    $ jeziorox = 0
                    if urban_social_link == 1:
                        if timer >= 540 and timer <= 1080 or timer >= 1980 and timer <= 2520 or timer >= 3420 and timer <= 3980 or timer >= 4860 and timer <= 5400 or timer >= 6300 and timer <= 6840 or timer >= 7740 and timer <= 8280 or timer >= 9180 and timer <= 9720 or timer >= 10620 and timer <= 11160:
                            $ jeziorox += 1
                            "{i}Znalazłem przy jeziorze stary bunkier{/i}"
                            "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                        else:
                            $ jeziorox += 2
                            "{i}Znalazłem przy jeziorze stary bunkier{/i}"
                            "{i}Prawdopodobnie to o nim mówił Jerzy Urban{/i}"
                            "{i}Jednak obecnie jest za późna godzina, by tam iść{/i}"       
                    
                    if jeziorox == 0:
                        $ timer += 15
                        play sound "audio/sfx/traveling.mp3"
                        scene bg black with fade
                        jump jezioro1

                    else:
                        if jeziorox == 1:
                            if urban_social_link == 1:
                                menu:
                                    "{b}Co zrobić?{/b}"

                                    "{b}Spotkaj się z Jerzym Urbanem (2h){/b}" if urban_social_link == 1:
                                        if timer > 9610 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11147 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        $ timer += 120
                                        jump urban2
                                    
                                    "{b}Idź na ryby (15min){/b}":
                                        if timer > 9775 and timer <= 9840:
                                            luszcz "Nie zdąże tego zrobić przed Balem"
                                            jump granica2
                                        
                                        if timer > 11232 and timer <= 11377:
                                            luszcz "Nie zdąże tego zrobić przed Referendum"
                                            jump granica2
                                        $ timer += 15
                                        play sound "audio/sfx/traveling.mp3"
                                        scene bg black with fade
                                        jump jezioro1
                                    
                                    "{b}Powrót{/b}":
                                        luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                        jump granica2
                        
                        else:
                            if jeziorox == 2:
                                if urban_social_link == 1:
                                    menu:
                                        "{b}Czy chcę iść na ryby? (15min){/b}"

                                        "{b}Tak{/b}":
                                            if timer > 9775 and timer <= 9840:
                                                luszcz "Nie zdąże tego zrobić przed Balem"
                                                jump granica2
                                            
                                            if timer > 11232 and timer <= 11377:
                                                luszcz "Nie zdąże tego zrobić przed Referendum"
                                                jump granica2
                                            $ timer += 15
                                            play sound "audio/sfx/traveling.mp3"
                                            scene bg black with fade
                                            jump jezioro1

                                        "{b}Nie{/b}":
                                            luszcz "Nic tu po mnie, wrócę tu kiedy indziej"
                                            jump granica2

    label walka_uliczna:
        "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
        if zul_wu == 0 and gnoms_wu == 0 and raem_wu == 0 or zul_wu == 1 and gnoms_wu == 1 and raem_wu == 1:
            $ kostka = renpy.random.randint(1, 3)
            if kostka == 1:
                jump raem_fight
            if kostka == 2:
                jump gnoms_fight
            if kostka == 3:
                jump zul_fight
        else:
            if zul_wu == 1 and gnoms_wu == 0 and raem_wu == 0:
                $ kostka = renpy.random.randint(1, 2)
                if kostka == 1:
                    jump raem_fight
                if kostka == 2:
                    jump gnoms_fight
            else:
                if zul_wu == 0 and gnoms_wu == 1 and raem_wu == 0:
                    $ kostka = renpy.random.randint(1, 2)
                    if kostka == 1:
                        jump raem_fight
                    if kostka == 2:
                        jump zul_fight
                else:
                    if zul_wu == 0 and gnoms_wu == 0 and raem_wu == 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kostka == 2:
                            jump gnoms_fight
                        if kostka == 1:
                            jump zul_fight
                    else:
                        if zul_wu == 1 and gnoms_wu == 1 and raem_wu == 0:
                            jump raem_fight
                        else:
                            if zul_wu == 1 and gnoms_wu == 0 and raem_wu == 1:
                                jump gnoms_fight
                            else:
                                if zul_wu == 0 and gnoms_wu == 1 and raem_wu == 1:
                                    jump zul_fight

    label trumen1:
        play sound "audio/sfx/rota.mp3"
        show luszcz neutral at slightleft
        show cichociemny neutral2:
            xalign 0.9
            yalign 10.0
            easeout 1.3 yalign 0.6
        
        $ renpy.pause(1.2)
        with hpunch
        $ renpy.pause(0.1)
        show cichociemny neutral at slightright

        luszcz "o jacie co się dzieje"

        cichociemny "Macieju! wstawaj!"
        cichociemny "Wstawaj zesrałeś się"
        cichociemny "jesteś w tak zwanym internecie"

        luszcz "że co proszę?"
        luszcz "nie pozwolę się tak obrażać"

        cichociemny "ty nawet nie istniejesz więc nie masz nic do gadania"

        luszcz "doigrasz się!"

        cichociemny "wątpię, nie ma tego w scenariuszu, ale masz jeszcze szanse zbudzić się z tego fraudu"
        cichociemny "liczę na ciebie"

        stop sound
        hide cichociemny
        show luszcz neutral at center

        luszcz "????"
        luszcz "faktycznie nie mogę mu nic zrobić"
        luszcz "dziwne"

        hide luszcz

        jump lipowa2
    
    label trumen2:
        show luszcz neutral at slightleft
        show platon neutral at slightright
        
        platon "czy chciałby pan porozmawiać o świecie?"

        luszcz "nie"

        platon "ale ja nalegam"
        platon "niech sobie pan wyobrazi, że ludzie są w jaskini i myślą, że znają świat, ale tak naprawdę widzą tylko jego odbicie i przez swoje położenie nigdy nie poznają prawdy"

        luszcz "niesamowite....... jeszcze jakieś rewelację czy mogę już iść"

        platon "niektórzy nie zdają sobie sprawę, że są właśnie takimi jaskiniowcami"

        luszcz "hmm hmm"

        platon "widzę, że nie chcesz poznać prawdy"
        platon "więc żyj dalej w swoim zakłamaniu, że istniejesz i nikt nie kieruje twoimi poczynaniami"
        platon "żegnam ozięble"
        platon "BEZ RODZINKI"
        hide platon
        show luszcz neutral at center

        luszcz "..?"

        hide luszcz

        jump parking2

    label trumen3:
        show luszcz neutral at slightleft
        show bezimienny neutral at slightright
        
        bezimienny "Witam użytkowniku"

        luszcz "Nie, nie chce odbierać żadnego iphona"

        bezimienny "Co nie! ja nie o tym"
        bezimienny "Chciałem cie tylko ostrzec, że savescamowanie niesie ze sobą ogromne konsekwecje dlatego uważaj jak z nich korzystasz"

        luszcz "save co?"

        bezimienny "nieważne, to nie do ciebie"

        luszcz "co??"

        bezimienny "gówno"

        hide bezimienny
        show luszcz neutral at center

        luszcz "aha"

        hide luszcz

        jump alejka2

    label trumen4:
        show luszcz neutral at slightleft
        show placeholder at slightright
        
        placeholder "masakra, po co komu maj"
        placeholder "luty to był taki fajny miesiąc"
        placeholder "najlepszy w roku"
        placeholder "ale komuś należało na opóźnieniu tego całego cyrku"
        placeholder "że niby po maturach itp."
        placeholder "jeszcze teraz tylko czekać na 35 stopni i pełne słońce"
        placeholder "i nawet w metro nie zagrał, a ma burżuj"

        luszcz "jakie opóźnienie?"

        placeholder "co podsłuchujesz konfidencie"
        placeholder "z resztą to wszystko twoja wina"

        hide placeholder
        show luszcz neutral at center

        luszcz "jakoś ostatnio jest coraz więcej obywateli Choroszczy na ulicach"

        hide luszcz

        jump bohaterow_wrzesnia2

    label trumen5:
        hide screen secret_choice
        show luszcz neutral at slightleft
        show stasiuk neutral at slightright
        
        stasiuk "Dzień dobry, a gdybyśmy się nie widzieli miłego popołudnia, wieczoru i dobranoc"

        luszcz "Dzień dobry?"

        stasiuk "Widzi pan było tu kiedyś pewne miejsce"
        stasiuk "Można by wręcz powiedzieć, że była to dla mnie taka świątynia"
        stasiuk "Mogłeś tam wziąć każde możliwe cheaty na całą grę"
        stasiuk "Ale zabrały chuje sowieckie za granicę i nie ma już cheatów także musisz radzić sobie normalnie"

        luszcz "eeee"
        luszcz "a słyszał pan o takim miejscu jak Choroszcz?"

        stasiuk "to nie ma teraz znaczenia"
        stasiuk "Jedyne co ma teraz znaczenie to akcje jakie podejmiecie"

        hide stasiuk
        show luszcz neutral at center

        luszcz "eee podejmiecie?"
        luszcz "to ja już chyba pójdę"

        hide luszcz

        jump sloneczna2

    label kamala:
        play sound "audio/sfx/godlewska.mp3"
        show luszcz neutral at left
        show kamala neutral:
            xalign 1.0
            yalign 1.0

        dzieci "Głosujemy na Kamale Harris!"
        dzieci "Kamala Harris na prezydentke USA!!!"

        luszcz "Ale wy wiecie, że już jest po wyborach, a wy nawet nie jesteście z Ameryki?"

        dzieci "Kamala Harris do boju!"

        hide kamala
        stop sound

        luszcz "ehhh bahory"

        hide luszcz

        jump rynek2

    label raem_fight:
        $ raem_wu = 1
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
        $ gnoms_wu = 1
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
    
    label zul_fight:
        $ zul_wu = 1
        scene bg zul
        play music "audio/music/zul.mp3"
        show luszcz neutral at left
        show zul neutral at slightright
        
        zul "Panie dej no 2 złote"

        menu:
            "{b}Dej (1 💰){/b}" if money >= 1:
                $ money -= 1
                luszcz "masz"

                zul "To dej no jeszcze 5 złoty"

                luszcz "Ale chciałeś 2 złote!"

                zul "To daj 3"

                menu:
                    "{b}Dej (1 💰){/b}" if money >= 1:
                        $ money -= 1

                        luszcz "masz"

                        zul "No, interesy z tobą panie prezesie to czysta przyjemność"

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
                    
                    "{b}Nie dam{/b}":
                        luszcz "Nie dam"

                        zul "o ty kurwa dziadzie!"

                        jump fight191

            "{b}Nie dam{/b}":
                luszcz "Nie dam"

                zul "To dej 5 złoty"

                luszcz "Ale chciałeś 2 złote!"

                zul "To daj 3"

                menu:
                    "{b}Dej (1 💰){/b}" if money >= 1:
                        $ money -= 1

                        luszcz "masz"

                        zul "No, interesy z tobą panie prezesie to czysta przyjemność"

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
                        
                    "{b}Nie dam{/b}":
                        luszcz "Mówiłem, że nie dam"

                        zul "o ty kurwa dziadzie!"

                        jump fight191





    
    label after_fight191:
        scene bg zul
        play music "audio/music/zul.mp3"
        show luszcz neutral at left
        show zul neutral at slightright

        play sound "audio/sfx/rzygi.mp3"

        zul "Kurłeeeee"

        luszcz "..."

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

    label devroom:
        play music "audio/music/devik.mp3"
        if devroomek == 0:
            $ devroomek = 1
            scene bg devroom
            show luszcz neutral at left 
            erykd "Teofil pracujesz?"

            teofil "tak, tak pracuję"

            erykd "Przecież widzę, ze nie pracujesz!"

            teofil "nie to tylko lekkie komplikacje, na pewno wszystko będzie git, mamy czas"

            erykd "aghhh, a chcesz gifa?"

            teofil "Jakiego gifa?"
            $ renpy.movie_cutscene("nse.webm")

            teofil "Aaaghhh prosze nie"

            erykd "No to pracuj!"
            erykd "spójrz na Mateusza jak on pięknie pracuje!"

            mateusz "praca, praca"

            scene bg devroom2
            show luszcz neutral at left 

            erykd "..?"
            erykd "Jak tyś się tu dostał?"

            luszcz "Eeee znalazłem jakąś skrytkę pod drzewem więc do niej wszedłem"

            scene bg devroom
            show luszcz neutral at left 

            erykd "Aghhh a mówiłem ci Teofil, że to jest zła miejscówka"

            scene bg devroom2
            show luszcz neutral at left 

            erykd "Emmmm upsi?"

            luszcz "A co wy tu w ogóle robicie?"

            erykd "A jedynie planujemy każdy szczegół twojego życia i całego świata przedstawionego!"
            erykd "ale to nic ważnego więc no"

            luszcz "..."

            erykd "Wiem! W ramach nagrody za znalezienie nas użyczymy Ci część naszych devowskich mocy"
            erykd "Co ty na to?"

            luszcz "Emmm chyba git"

            erykd "A tylko pamiętaj efekt ich użycia jest nieodwracalny!"

            luszcz "dobrze, dobrze"

            eryk "To co chcesz zmienić?"

        else:
            scene bg devroom2
            show luszcz neutral at left
            erykd "Co cię dziś sprowadza?"
        
        label dev2:
            menu:
                "{b}Ogólne{/b}":
                    label dev12:
                        menu:
                            "{b}Czas{/b}":                
                                label dev13:
                                    menu:
                                        "{b}Co zrobić?{/b}"

                                        "{b}Dodać{/b}":
                                            menu:
                                                "{b}Ile?{/b}"

                                                "{b}+5min{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 5 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 5

                                                    "{i}*Dodałeś 5 minut do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}+15min{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 15 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 15

                                                    "{i}*Dodałeś 15 minut do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}+1h{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 60 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 60

                                                    "{i}*Dodałeś 1 godzinę do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}+5h{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 300 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 300

                                                    "{i}*Dodałeś 5 godzin do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}+12h{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 720 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 720

                                                    "{i}*Dodałeś 12 godzin do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}+24h{/b}":
                                                    if timer == 11377:
                                                        "{i}*Nie możesz ustawić czasu na późniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer + 1440 > 11377:
                                                            $ timer = 11377
                                                        
                                                        else:
                                                            $ timer += 1440

                                                    "{i}*Dodałeś 1 dobę do czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}Powrót{/b}":         
                                                    jump dev13
                                        
                                        "{b}Zabrać{/b}":
                                            menu:
                                                "{b}Ile?{/b}"

                                                "{b}-5min{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 5 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 5

                                                    "{i}*Zabrałeś 5 minut z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}-15min{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 15 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 15

                                                    "{i}*Zabrałeś 15 minut z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}-1h{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 60 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 60

                                                    "{i}*Zabrałeś 1 godzinę z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}-5h{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 300 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 300

                                                    "{i}*Zabrałeś 5 godzin z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}-12h{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 720 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 720

                                                    "{i}*Zabrałeś 12 godzin z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}-24h{/b}":
                                                    if timer == 615:
                                                        "{i}*Nie możesz ustawić czasu na wcześniejszy*{/i}"
                                                        jump dev13
                                                    
                                                    else:
                                                        if timer - 1440 < 615:
                                                            $ timer = 615
                                                        
                                                        else:
                                                            $ timer -= 1440

                                                    "{i}*Zabrałeś 1 dobę z czasu gry*{/i}"
                                                    jump dev2
                                                
                                                "{b}Powrót{/b}":         
                                                    jump dev13
                                        
                                        "{b}Powrót{/b}":         
                                            jump dev12
                                                    
                            "{b}Portfele{/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        $ money += 1
                                        "{i}*Portfel x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        $ money += 5
                                        "{i}*Portfel x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        $ money += 20
                                        "{i}*Portfel x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if money == 0:
                                            "{i}*Nie masz portfeli*{/i}"
                                            jump dev12

                                        $ money -= 1
                                        "{i}*Portfel x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if money == 0:
                                            "{i}*Nie masz portfeli*{/i}"
                                            jump dev12

                                        if money <= 5:
                                            $ money = 0
                                        else:
                                            $ money -= 5
                                        "{i}*Portfel x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if money == 0:
                                            "{i}*Nie masz portfeli*{/i}"
                                            jump dev12

                                        if money <= 20:
                                            $ money = 0
                                        else:
                                            $ money -= 20
                                        "{i}*Portfel x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev12
                            
                            "{b}Zapomnij o tej rozmowie{/b}":
                                $ devroomek = 0
                                erykd "Jakiej rozmowie?"
                                jump dev2

                            "{b}Powrót{/b}":
                                jump dev2

                "{b}Towarzysze{/b}":
                    label dev4:
                        menu:
                            "{b}Wybierz członka:{/b}"

                            "{b}Shadow{/b}":
                                if eminem_sojusznik == 0:
                                    $ eminem_sojusznik = 1
                                    $ liczba_sojusznikow += 1
                                    "{i}*Shadow dołączył do drużyny*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Shadowa z dużyny?{/b}"

                                        "{b}Tak{/b}":
                                            $ eminem_sojusznik = 0
                                            $ liczba_sojusznikow -= 1
                                            "{i}*Shadow opuścił drużyne*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev4

                            "{b}Jerzy Urban{/b}":
                                if urban_sojusznik == 0:
                                    $ urban_sojusznik = 1
                                    $ liczba_sojusznikow += 1
                                    "{i}*Jerzy Urban dołączył do drużyny*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Jerzego Urbana z dużyny?{/b}"

                                        "{b}Tak{/b}":
                                            $ urban_sojusznik = 0
                                            $ liczba_sojusznikow -= 1
                                            "{i}*Jerzy Urban opuścił drużyne*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev4

                            "{b}Żyd{/b}":
                                if zyd_sojusznik == 0:
                                    $ zyd_sojusznik = 1
                                    $ liczba_sojusznikow += 1
                                    "{i}*Żyd dołączył do drużyny*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Żyda z dużyny?{/b}"

                                        "{b}Tak{/b}":
                                            $ zyd_sojusznik = 0
                                            $ liczba_sojusznikow -= 1
                                            "{i}*Żyd opuścił drużyne*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev4

                            "{b}Kazuma{/b}":
                                if kazuma_sojusznik == 0:
                                    $ kazuma_sojusznik = 1
                                    $ liczba_sojusznikow += 1
                                    "{i}*Kazuma dołączył do drużyny*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Kazume z dużyny?{/b}"

                                        "{b}Tak{/b}":
                                            $ kazuma_sojusznik = 0
                                            $ liczba_sojusznikow -= 1
                                            "{i}*Kazuma opuścił drużyne*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev4

                            "{b}Naofumi{/b}":
                                if tarczownik_sojusznik == 0:
                                    $ tarczownik_sojusznik = 1
                                    $ liczba_sojusznikow += 1
                                    "{i}*Naofumi dołączył do drużyny*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Naofumiego z dużyny?{/b}"

                                        "{b}Tak{/b}":
                                            $ tarczownik_sojusznik = 0
                                            $ liczba_sojusznikow -= 1
                                            "{i}*Naofumi opuścił drużyne*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev4
                 
                            "{b}Powrót{/b}":
                                jump dev2

                "{b}Bronie{/b}":
                    label dev5:
                        menu:
                            "{b}Wybierz broń:{/b}"

                            "{b}Przepychaczka (ATK:2-4){/b}":
                                $ chinczyk_przepychaczka -= 1
                                if przepychaczka_liczba == 0 and luszcz_przepychaczka == 0 and urban_przepychaczka == 0 and zyd_przepychaczka == 0 and kazuma_przepychaczka == 0 and tarczownik_przepychaczka == 0:
                                    $ przepychaczka_liczba += 1
                                    if luszcz_przepychaczka == 0 and urban_przepychaczka == 0 and zyd_przepychaczka == 0 and kazuma_przepychaczka == 0 and tarczownik_przepychaczka == 0:
                                        $ luszcz_przepychaczka = 1
                                        $ urban_przepychaczka = 1
                                        $ zyd_przepychaczka = 1
                                        $ kazuma_przepychaczka = 1
                                        $ tarczownik_przepychaczka = 1
                                        $ eminem_przepychaczka = 1
                                    "{i}*Przepychaczka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Co chcesz zrobić?{/b}"

                                        "{b}Dodaj przepychaczkę{/b}" if chinczyk_przepychaczka > 0:
                                            $ chinczyk_przepychaczka -= 1
                                            $ przepychaczka_liczba += 1
                                            "{i}*Przepychaczka została dodana do ekwipunku*{/i}"
                                            jump dev2

                                        "{b}Usuń przepychaczki{/b}":
                                            if luszcz_przepychaczka == 2:
                                                $ luszcz_min_attack -= 2
                                                $ luszcz_max_attack -= 2
                                                $ luszcz_przepychaczka = 1
                                                $ przepychaczka_liczba += 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if stop == 3:
                                                $ urban_min_attack -= 2
                                                $ urban_max_attack -= 2
                                                $ urban_przepychaczka = 1
                                                $ przepychaczka_liczba += 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if stop == 4:
                                                $ zyd_min_attack -= 2
                                                $ zyd_max_attack -= 2
                                                $ zyd_przepychaczka = 1
                                                $ przepychaczka_liczba += 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if stop == 5:
                                                $ kazuma_min_attack -= 2
                                                $ kazuma_max_attack -= 2
                                                $ kazuma_przepychaczka = 1
                                                $ przepychaczka_liczba += 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if stop == 6:
                                                $ tarczownik_min_attack -= 2
                                                $ tarczownik_max_attack -= 2
                                                $ tarczownik_przepychaczka = 1
                                                $ przepychaczka_liczba += 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ chinczyk_przepychaczka = 5
                                            $ przepychaczka_liczba = 0
                                            "{i}*Znak drogowy został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Powrót{/b}":         
                                            jump dev5
                            
                            "{b}Znak Drogowy (ATK:1-6){/b}":
                                if stop == 0:
                                    $ stop = 1
                                    "{i}*Znak drogowy został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Znak Drogowy z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if stop == 2:
                                                $ luszcz_min_attack -= 1
                                                $ luszcz_max_attack -= 4
                                                $ stop = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if stop == 3:
                                                $ urban_min_attack -= 1
                                                $ urban_max_attack -= 4
                                                $ stop = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if stop == 4:
                                                $ zyd_min_attack -= 1
                                                $ zyd_max_attack -= 4
                                                $ stop = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if stop == 5:
                                                $ kazuma_min_attack -= 1
                                                $ kazuma_max_attack -= 4
                                                $ stop = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if stop == 6:
                                                $ tarczownik_min_attack -= 1
                                                $ tarczownik_max_attack -= 4
                                                $ stop = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ stop = 0
                                            "{i}*Znak drogowy został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                            
                            "{b}Miecz Świetlny (ATK:3-4){/b}":
                                if miecz_swietlny == 0:
                                    $ miecz_swietlny = 1
                                    "{i}*Miecz Świetlny został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Miecz Świetlny z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if miecz_swietlny == 2:
                                                $ luszcz_min_attack -= 3
                                                $ luszcz_max_attack -= 2
                                                $ miecz_swietlny = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if miecz_swietlny == 3:
                                                $ urban_min_attack -= 3
                                                $ urban_max_attack -= 2
                                                $ miecz_swietlny = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if miecz_swietlny == 4:
                                                $ zyd_min_attack -= 3
                                                $ zyd_max_attack -= 2
                                                $ miecz_swietlny = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if miecz_swietlny == 5:
                                                $ kazuma_min_attack -= 3
                                                $ kazuma_max_attack -= 2
                                                $ miecz_swietlny = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if miecz_swietlny == 6:
                                                $ tarczownik_min_attack -= 3
                                                $ tarczownik_max_attack -= 2
                                                $ miecz_swietlny = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ miecz_swietlny = 0
                                            "{i}*Miecz Świetlny został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                                
                            "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}":
                                if ostrza_chaosu == 0:
                                    $ ostrza_chaosu = 1
                                    "{i}*Ostrza Chaosu zostały dodane do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Ostrza Chaosu z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if ostrza_chaosu == 2:
                                                $ luszcz_min_attack -= 0
                                                $ luszcz_max_attack -= 1
                                                $ ostrza_chaosu = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if ostrza_chaosu == 3:
                                                $ urban_min_attack -= 0
                                                $ urban_max_attack -= 1
                                                $ ostrza_chaosu = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if ostrza_chaosu == 4:
                                                $ zyd_min_attack -= 0
                                                $ zyd_max_attack -= 1
                                                $ ostrza_chaosu = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if ostrza_chaosu == 5:
                                                $ kazuma_min_attack -= 0
                                                $ kazuma_max_attack -= 1
                                                $ ostrza_chaosu = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if ostrza_chaosu == 6:
                                                $ tarczownik_min_attack -= 0
                                                $ tarczownik_max_attack -= 1
                                                $ ostrza_chaosu = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ ostrza_chaosu = 0
                                            "{i}*Ostrza Chaosu zostały usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                            
                            "{b}Fajny Patyk (ATK:1-5){/b}":
                                if patyk == 0:
                                    $ patyk = 1
                                    "{i}*Fajny Patyk został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Fajny Patyk z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if patyk == 2:
                                                $ luszcz_min_attack -= 1
                                                $ luszcz_max_attack -= 3
                                                $ patyk = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if patyk == 3:
                                                $ urban_min_attack -= 1
                                                $ urban_max_attack -= 3
                                                $ patyk = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if patyk == 4:
                                                $ zyd_min_attack -= 1
                                                $ zyd_max_attack -= 3
                                                $ patyk = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if patyk == 5:
                                                $ kazuma_min_attack -= 1
                                                $ kazuma_max_attack -= 3
                                                $ patyk = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if patyk == 6:
                                                $ tarczownik_min_attack -= 1
                                                $ tarczownik_max_attack -= 3
                                                $ patyk = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ patyk = 0
                                            "{i}*Fajny Patyk został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                            
                            "{b}Wężowa Bazooka (ATK:1-3){/b}":
                                if bazooka == 0:
                                    $ bazooka = 1
                                    "{i}*Wężowa Bazooka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Wężową Bazooke z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if bazooka == 2:
                                                $ luszcz_min_attack -= 1
                                                $ luszcz_max_attack -= 1
                                                $ bazooka = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if bazooka == 3:
                                                $ urban_min_attack -= 1
                                                $ urban_max_attack -= 1
                                                $ bazooka = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if bazooka == 4:
                                                $ zyd_min_attack -= 1
                                                $ zyd_max_attack -= 1
                                                $ bazooka = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if bazooka == 5:
                                                $ kazuma_min_attack -= 1
                                                $ kazuma_max_attack -= 1
                                                $ bazooka = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if bazooka == 6:
                                                $ tarczownik_min_attack -= 1
                                                $ tarczownik_max_attack -= 1
                                                $ bazooka = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ bazooka = 0
                                            "{i}*Wężowa Bazooka została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                            
                            "{b}Wydrukowany Miecz (ATK:2-5){/b}":
                                if stop == 0:
                                    $ stop = 1
                                    "{i}*Wydrukowany Miecz został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Wydrukowany Miecz z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if stop == 2:
                                                $ luszcz_min_attack -= 2
                                                $ luszcz_max_attack -= 3
                                                $ miecz3d = 1
                                                $ gitara = 2
                                                $ luszcz_min_attack += 1
                                                $ luszcz_max_attack += 2

                                            if stop == 3:
                                                $ urban_min_attack -= 2
                                                $ urban_max_attack -= 3
                                                $ miecz3d = 1
                                                $ fuck = 3
                                                $ urban_min_attack += 0
                                                $ urban_max_attack += 2

                                            if stop == 4:
                                                $ zyd_min_attack -= 2
                                                $ zyd_max_attack -= 3
                                                $ miecz3d = 1
                                                $ chanuka = 4
                                                $ zyd_min_attack += 1
                                                $ zyd_max_attack += 3

                                            if stop == 5:
                                                $ kazuma_min_attack -= 2
                                                $ kazuma_max_attack -= 3
                                                $ miecz3d = 1
                                                $ chunchunmaru = 5
                                                $ kazuma_min_attack += 0
                                                $ kazuma_max_attack += 6
                                            
                                            if stop == 6:
                                                $ tarczownik_min_attack -= 2
                                                $ tarczownik_max_attack -= 3
                                                $ miecz3d = 1
                                                $ legendary_shield = 6
                                                $ tarczownik_min_attack += 1
                                                $ tarczownik_max_attack += 3

                                            $ stop = 0
                                            "{i}*Wydrukowany Miecz został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev5
                            
                            "{b}Powrót{/b}":
                                jump dev2

                "{b}Zbroje{/b}":
                    label dev9:
                        menu:
                            "{b}Wybierz zbroje:{/b}"

                            "{b}Diamentowa Klata{/b}":
                                $ chinczyk_klata -= 1
                                if klata_liczba == 0 and luszcz_klata == 0 and urban_klata == 0 and zyd_klata == 0 and kazuma_klata == 0 and tarczownik_klata == 0 and eminem_klata == 0:
                                    $ klata_liczba += 1
                                    if luszcz_klata == 0 and urban_klata == 0 and zyd_klata == 0 and kazuma_klata == 0 and tarczownik_klata == 0 and eminem_klata == 0:
                                        $ luszcz_klata = 1
                                        $ urban_klata = 1
                                        $ zyd_klata = 1
                                        $ kazuma_klata = 1
                                        $ tarczownik_klata = 1
                                        $ eminem_klata = 1
                                    "{i}*Diamentowa Klata została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Co chcesz zrobić?{/b}"

                                        "{b}Dodaj Diamentową Klate{/b}" if chinczyk_klata > 0:
                                            $ chinczyk_klata -= 1
                                            $ klata_liczba += 1
                                            "{i}*Diamentowa Klata została dodana do ekwipunku*{/i}"
                                            jump dev2

                                        "{b}Usuń Diamentowe Klaty{/b}":
                                            if luszcz_klata == 2:
                                                $ luszcz_klata = 1
                                                $ luszcz_nic = 2
                                                $ klata_liczba += 1
                                                $ luszcz_hp -= 5

                                            if urban_klata == 3:
                                                $ urban_klata = 1
                                                $ urban_nic = 3
                                                $ klata_liczba += 1
                                                $ urban_hp -= 5

                                            if zyd_klata == 4:
                                                $ zyd_klata = 1
                                                $ zyd_nic = 4
                                                $ klata_liczba += 1
                                                $ zyd_hp -= 5

                                            if kazuma_klata == 5:
                                                $ kazuma_klata = 1
                                                $ kazuma_nic = 5
                                                $ klata_liczba += 1
                                                $ kazuma_hp -= 5
                                            
                                            if tarczownik_klata == 6:
                                                $ tarczownik_klata = 1
                                                $ tarczownik_nic = 6
                                                $ klata_liczba += 1
                                                $ tarczownik_hp -= 5
                                            
                                            if eminem_klata == 7:
                                                $ eminem_klata = 1
                                                $ eminem_nic = 7
                                                $ klata_liczba += 1
                                                $ eminem_hp -= 5

                                            $ chinczyk_klata = 6
                                            $ klata_liczba = 0
                                            "{i}*Diamentowe Klaty zostały usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Powrót{/b}":         
                                            jump dev9
                            
                            "{b}Pierścień z Władców Pierścieni{/b}":
                                if ring == 0:
                                    $ ring = 1
                                    "{i}*Pierścień z Władców Pierścieni został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Pierścień z Władców Pierścieni z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if ring == 2:
                                                $ ring = 1
                                                $ luszcz_nic = 2

                                            if ring == 3:
                                                $ ring = 1
                                                $ urban_nic = 3

                                            if ring == 4:
                                                $ ring = 1
                                                $ zyd_nic = 3

                                            if ring == 5:
                                                $ ring = 1
                                                $ kazuma_nic = 5
                                            
                                            if ring == 6:
                                                $ ring = 1
                                                $ tarczownik_nic = 6
                                            
                                            if ring == 7:
                                                $ ring = 1
                                                $ eminem_nic = 7

                                            $ ring = 0
                                            "{i}*Pierścień z Władców Pierścieni został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}VR Headset{/b}":
                                if vr == 0:
                                    $ vr = 1
                                    "{i}*VR Headset został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć VR Headset z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if vr == 2:
                                                $ vr = 1
                                                $ luszcz_nic = 2

                                            if vr == 3:
                                                $ vr = 1
                                                $ urban_nic = 3

                                            if vr == 4:
                                                $ vr = 1
                                                $ zyd_nic = 3

                                            if vr == 5:
                                                $ vr = 1
                                                $ kazuma_nic = 5
                                            
                                            if vr == 6:
                                                $ vr = 1
                                                $ tarczownik_nic = 6
                                            
                                            if vr == 7:
                                                $ vr = 1
                                                $ eminem_nic = 7

                                            $ vr = 0
                                            "{i}*VR Headset został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}Szalik z Memów{/b}":
                                if memy == 0:
                                    $ memy = 1
                                    "{i}*Szalik z Memów został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Szalik z Memów z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if memy == 2:
                                                $ memy = 1
                                                $ luszcz_nic = 2

                                            if memy == 3:
                                                $ memy = 1
                                                $ urban_nic = 3

                                            if memy == 4:
                                                $ memy = 1
                                                $ zyd_nic = 3

                                            if memy == 5:
                                                $ memy = 1
                                                $ kazuma_nic = 5
                                            
                                            if memy == 6:
                                                $ memy = 1
                                                $ tarczownik_nic = 6
                                            
                                            if memy == 7:
                                                $ memy = 1
                                                $ eminem_nic = 7

                                            $ memy = 0
                                            "{i}*Szalik z Memów został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}Kawałek ziemi, po której stąpał Jan Paweł 2{/b}":
                                if ziemia == 0:
                                    $ ziemia = 1
                                    "{i}*Kawałek ziemi, po której stąpał Jan Paweł 2 został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Kawałek ziemi, po której stąpał Jan Paweł 2 z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if ziemia == 2:
                                                $ ziemia = 1
                                                $ luszcz_nic = 2

                                            if ziemia == 3:
                                                $ ziemia = 1
                                                $ urban_nic = 3

                                            if ziemia == 4:
                                                $ ziemia = 1
                                                $ zyd_nic = 3

                                            if ziemia == 5:
                                                $ ziemia = 1
                                                $ kazuma_nic = 5
                                            
                                            if ziemia == 6:
                                                $ ziemia = 1
                                                $ tarczownik_nic = 6
                                            
                                            if ziemia == 7:
                                                $ ziemia = 1
                                                $ eminem_nic = 7

                                            $ ziemia = 0
                                            "{i}*Kawałek ziemi, po której stąpał Jan Paweł 2 został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}Długie Nogi{/b}":
                                if nogi == 0:
                                    $ nogi = 1
                                    "{i}*Długie Nogi zostały dodane do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Długie Nogi z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if nogi == 2:
                                                $ nogi = 1
                                                $ luszcz_nic = 2
                                                $ luszcz_hp -= 10

                                            if nogi == 3:
                                                $ nogi = 1
                                                $ urban_nic = 3
                                                $ urban_hp -= 10

                                            if nogi == 4:
                                                $ nogi = 1
                                                $ zyd_nic = 3
                                                $ zyd_hp -= 10

                                            if nogi == 5:
                                                $ nogi = 1
                                                $ kazuma_nic = 5
                                                $ kazuma_hp -= 10
                                            
                                            if nogi == 6:
                                                $ nogi = 1
                                                $ tarczownik_nic = 6
                                                $ tarczownik_hp -= 10
                                            
                                            if nogi == 7:
                                                $ nogi = 1
                                                $ eminem_nic = 7
                                                $ eminem_hp -= 10

                                            $ nogi = 0
                                            "{i}*Długie Nogi zostały usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}Złoty Człowiek{/b}":
                                if zloty == 0:
                                    $ zloty = 1
                                    "{i}*Złoty Człowiek został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Złotego Człowieka z ekwipunku{/b}"

                                        "{b}Tak{/b}":
                                            if zloty == 2:
                                                $ zloty = 1
                                                $ luszcz_nic = 2

                                            if zloty == 3:
                                                $ zloty = 1
                                                $ urban_nic = 3

                                            if zloty == 4:
                                                $ zloty = 1
                                                $ zyd_nic = 3

                                            if zloty == 5:
                                                $ zloty = 1
                                                $ kazuma_nic = 5
                                            
                                            if zloty == 6:
                                                $ zloty = 1
                                                $ tarczownik_nic = 6
                                            
                                            if zloty == 7:
                                                $ zloty = 1
                                                $ eminem_nic = 7

                                            $ zloty = 0
                                            "{i}*Złoty Człowiek został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev9
                            
                            "{b}Powrót{/b}":
                                jump dev2

                "{b}Itemy Fabularne{/b}":
                    label dev6:
                        menu:
                            "{b}Wybierz item:{/b}"

                            "{b}Piernik{/b}":
                                if piernik == 0:
                                    $ piernik = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Piernik został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Piernik z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ piernik = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Piernik został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6

                            "{b}Łopatka{/b}":
                                if lopatka == 0:
                                    $ lopatka = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Łopatka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Łopatke z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ lopatka = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Łopatka została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6
                            
                            "{b}Krówka{/b}":
                                if krowka == 0:
                                    $ krowka = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Krówka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Krówke z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ krowka = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Krówka została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6
                            
                            "{b}Kremówka{/b}":
                                if kremowka == 0:
                                    $ kremowka = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Kremówka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Kremówke z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ kremowka = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Kremówka została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6
                            
                            "{b}Biblia{/b}":
                                if biblia == 0:
                                    $ biblia = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Biblia została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Biblie z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ biblia = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Biblia została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6
                            
                            "{b}Ailbib{/b}":
                                if ailbib == 0:
                                    $ ailbib = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Ailbib został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Ailbib z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ ailbib = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Ailbib został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev6

                            "{i}Strona 1/3 --->{/i}":
                                jump dev7

                            "{b}Powrót{/b}":
                                jump dev2
                    
                    label dev7:
                        menu:
                            "{b}Wybierz item:{/b}"

                            "{b}Wazon Węży{/b}":
                                if wazon_wezy == 0:
                                    $ wazon_wezy = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Wazon Węży został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Wazon Węży z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ wazon_wezy = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Wazon Węży został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev7

                            "{b}Głowa Nemeczka{/b}":
                                if glowa == 0:
                                    $ glowa = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Głowa Nemeczka została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Głowe Nemeczka z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ glowa = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Głowa Nemeczka została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev7
                            
                            "{b}Kula Toxic Pea{/b}":
                                if zielona_kula == 0:
                                    $ zielona_kula = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Kula Toxic Pea została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Kule Toxic Pea z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ zielona_kula = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Kula Toxic Pea została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev7
                            
                            "{b}Rozmówki polsko-chińskie{/b}":
                                if slownik == 0:
                                    $ slownik = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Rozmówki polsko-chińskie zostały dodane do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Rozmówki polsko-chińskie z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ slownik = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Rozmówki polsko-chińskie zostały usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev7
                            
                            "{b}Kartka z Życzeniami{/b}":
                                if kartka == 0:
                                    $ kartka = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Kartka z Życzeniami została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Kartke z Życzeniami z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ kartka = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Kartka z Życzeniami została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev7

                            "{i}<--- Strona 2/3{/i}":
                                jump dev6

                            "{i}Strona 2/3 --->{/i}":
                                jump dev8
                    label dev8:
                        menu:
                            "{b}Wybierz item:{/b}"

                            "{b}Dinozaur{/b}":
                                if dinozaur == 0:
                                    $ dinozaur = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Dinozaur został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Dinozaura z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ dinozaur = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Dinozaur został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8

                            "{b}Ciało Eminema{/b}":
                                if cialo == 0:
                                    $ cialo = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Ciało Eminema zostało dodane do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Ciało Eminema z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ cialo = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Ciało Eminema zostało usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8
                            
                            "{b}Tesla Cybertruck{/b}":
                                if cybertruck == 0:
                                    $ cybertruck = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Tesla Cybertruck została dodana do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Tesle Cybertruck z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ cybertruck = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Tesla Cybertruck została usunięta z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8
                            
                            "{b}Leki na Schizofrenię{/b}":
                                if leki == 0:
                                    $ leki = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Leki na Schizofrenię zostały dodane do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Leki na Schizofrenię z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ leki = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Leki na Schizofrenię zostały usunięte z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8
                            
                            "{b}Klucz{/b}":
                                if klucz == 0:
                                    $ klucz = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Klucz został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Klucz z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ klucz = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Klucz został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8
                            
                            "{b}Folder z Memami{/b}":
                                if folder_memow == 0:
                                    $ folder_memow = 1
                                    $ ile_item_fabularne += 1

                                    "{i}*Folder z Memami został dodany do ekwipunku*{/i}"
                                    jump dev2
                                else:
                                    menu:
                                        "{b}Czy chcesz usunąć Folder z Memami z ekwipunku?{/b}"

                                        "{b}Tak{/b}":
                                            $ folder_memow = 0
                                            $ ile_item_fabularne -= 1
                                            "{i}*Folder z Memami został usunięty z ekwipunku*{/i}"
                                            jump dev2
                                        
                                        "{b}Nie{/b}":         
                                            jump dev8

                            "{i}<--- Strona 3/3{/i}":
                                jump dev7

                "{b}Itemy do Walki{/b}":
                    label dev10:
                        menu:
                            "{b}Wybierz item:{/b}"

                            "{b}Piknik (+FULL HP FOR ALL){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if piknik == 0:
                                            $ ile_item += 1
                                        $ piknik += 1
                                        "{i}*Piknik x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if piknik == 0:
                                            $ ile_item += 1
                                        $ piknik += 5
                                        "{i}*Piknik x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if piknik == 0:
                                            $ ile_item += 1
                                        $ piknik += 20
                                        "{i}*Piknik x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if piknik == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if piknik == 1:
                                            $ ile_item -= 1
                                        $ piknik -= 1
                                        "{i}*Piknik x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if piknik == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if piknik <= 5:
                                            $ ile_item -= 1
                                            $ piknik = 0
                                        else:
                                            $ piknik -= 5
                                        "{i}*Piknik x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if piknik == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if piknik <= 20:
                                            $ ile_item -= 1
                                            $ piknik = 0
                                        else:
                                            $ piknik -= 20
                                        "{i}*Piknik x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10

                            "{b}Ciasto Truskawkowe (+15HP LUB +5HP FOR ALL){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if cake == 0:
                                            $ ile_item += 1
                                        $ cake += 1
                                        "{i}*Ciasto Truskawkowe x 1 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if cake == 0:
                                            $ ile_item += 1
                                        $ cake += 5
                                        "{i}*Ciasto Truskawkowe x 5 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if cake == 0:
                                            $ ile_item += 1
                                        $ cake += 20
                                        "{i}*Ciasto Truskawkowe x 20 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if cake == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if cake == 1:
                                            $ ile_item -= 1
                                        $ cake -= 1
                                        "{i}*Ciasto Truskawkowe x 1 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if cake == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if cake <= 5:
                                            $ ile_item -= 1
                                            $ cake = 0
                                        else:
                                            $ cake -= 5
                                        "{i}*Ciasto Truskawkowe x 5 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if cake == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if cake <= 20:
                                            $ ile_item -= 1
                                            $ cake = 0
                                        else:
                                            $ cake -= 20
                                        "{i}*Ciasto Truskawkowe x 20 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10

                            "{b}Słoik z Pigułkami (+3HP){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if pills == 0:
                                            $ ile_item += 1
                                        $ pills += 1
                                        "{i}*Słoik z Pigułkami x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if pills == 0:
                                            $ ile_item += 1
                                        $ pills += 5
                                        "{i}*Słoik z Pigułkami x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if pills == 0:
                                            $ ile_item += 1
                                        $ pills += 20
                                        "{i}*Słoik z Pigułkami x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if pills == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if pills == 1:
                                            $ ile_item -= 1
                                        $ pills -= 1
                                        "{i}*Słoik z Pigułkami x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if pills == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if pills <= 5:
                                            $ ile_item -= 1
                                            $ pills = 0
                                        else:
                                            $ pills -= 5
                                        "{i}*Słoik z Pigułkami x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if pills == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if pills <= 20:
                                            $ ile_item -= 1
                                            $ pills = 0
                                        else:
                                            $ pills -= 20
                                        "{i}*Słoik z Pigułkami x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10

                            "{b}Tutorialowa Woda Święcona (+6HP){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if woda == 0:
                                            $ ile_item += 1
                                        $ woda += 1
                                        "{i}*Tutorialowa Woda Święcona x 1 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if woda == 0:
                                            $ ile_item += 1
                                        $ woda += 5
                                        "{i}*Tutorialowa Woda Święcona x 5 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if woda == 0:
                                            $ ile_item += 1
                                        $ woda += 20
                                        "{i}*Tutorialowa Woda Święcona x 20 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if woda == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if woda == 1:
                                            $ ile_item -= 1
                                        $ woda -= 1
                                        "{i}*Tutorialowa Woda Święcona x 1 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if woda == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if woda <= 5:
                                            $ ile_item -= 1
                                            $ woda = 0
                                        else:
                                            $ woda -= 5
                                        "{i}*Tutorialowa Woda Święcona x 5 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if woda == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if woda <= 20:
                                            $ ile_item -= 1
                                            $ woda = 0
                                        else:
                                            $ woda -= 20
                                        "{i}*Tutorialowa Woda Święcona x 20 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10

                            "{b}Kebab Ostry (+3HP i +1 MAX DMG){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if ostry == 0:
                                            $ ile_item += 1
                                        $ ostry += 1
                                        "{i}*Kebab Ostry x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if ostry == 0:
                                            $ ile_item += 1
                                        $ ostry += 5
                                        "{i}*Kebab Ostry x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if ostry == 0:
                                            $ ile_item += 1
                                        $ ostry += 20
                                        "{i}*Kebab Ostry x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if ostry == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if ostry == 1:
                                            $ ile_item -= 1
                                        $ ostry -= 1
                                        "{i}*Kebab Ostry x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if ostry == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if ostry <= 5:
                                            $ ile_item -= 1
                                            $ ostry = 0
                                        else:
                                            $ ostry -= 5
                                        "{i}*Kebab Ostry x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if ostry == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if ostry <= 20:
                                            $ ile_item -= 1
                                            $ ostry = 0
                                        else:
                                            $ ostry -= 20
                                        "{i}*Kebab Ostry x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10
                            
                            "{b}Kebab Łagodny (+4HP i + 1HP FOR 3 TURNS){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if lagodny == 0:
                                            $ ile_item += 1
                                        $ lagodny += 1
                                        "{i}*Kebab Łagodny x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if lagodny == 0:
                                            $ ile_item += 1
                                        $ lagodny += 5
                                        "{i}*Kebab Łagodny x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if lagodny == 0:
                                            $ ile_item += 1
                                        $ lagodny += 20
                                        "{i}*Kebab Łagodny x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if lagodny == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if lagodny == 1:
                                            $ ile_item -= 1
                                        $ lagodny -= 1
                                        "{i}*Kebab Łagodny x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if lagodny == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if lagodny <= 5:
                                            $ ile_item -= 1
                                            $ lagodny = 0
                                        else:
                                            $ lagodny -= 5
                                        "{i}*Kebab Łagodny x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if lagodny == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev10

                                        if lagodny <= 20:
                                            $ ile_item -= 1
                                            $ lagodny = 0
                                        else:
                                            $ lagodny -= 20
                                        "{i}*Kebab Łagodny x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev10

                            "{i}Strona 1/2 --->{/i}":
                                jump dev11

                            "{b}Powrót{/b}":
                                jump dev2

                    label dev11:
                        menu:
                            "{b}Wybierz item:{/b}"

                            "{b}Dr Pepper (+2HP i MAX DMG NEXT ATTACK){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if drpepper == 0:
                                            $ ile_item += 1
                                        $ drpepper += 1
                                        "{i}*Dr Pepper x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if drpepper == 0:
                                            $ ile_item += 1
                                        $ drpepper += 5
                                        "{i}*Dr Pepper x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if drpepper == 0:
                                            $ ile_item += 1
                                        $ drpepper += 20
                                        "{i}*Dr Pepper x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if drpepper == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if drpepper == 1:
                                            $ ile_item -= 1
                                        $ drpepper -= 1
                                        "{i}*Dr Pepper x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if drpepper == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if drpepper <= 5:
                                            $ ile_item -= 1
                                            $ drpepper = 0
                                        else:
                                            $ drpepper -= 5
                                        "{i}*Dr Pepper x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if drpepper == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if drpepper <= 20:
                                            $ ile_item -= 1
                                            $ drpepper = 0
                                        else:
                                            $ drpepper -= 20
                                        "{i}*Dr Pepper x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11

                            "{b}Jabole (+6HP){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if jabole == 0:
                                            $ ile_item += 1
                                        $ jabole += 1
                                        "{i}*Jabol x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if jabole == 0:
                                            $ ile_item += 1
                                        $ jabole += 5
                                        "{i}*Jabole x 5 zostały dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if jabole == 0:
                                            $ ile_item += 1
                                        $ jabole += 20
                                        "{i}*Jabole x 20 zostały dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if jabole == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if jabole == 1:
                                            $ ile_item -= 1
                                        $ jabole -= 1
                                        "{i}*Jabol x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if jabole == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if jabole <= 5:
                                            $ ile_item -= 1
                                            $ jabole = 0
                                        else:
                                            $ jabole -= 5
                                        "{i}*Jabole x 5 zostały usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if jabole == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if jabole <= 20:
                                            $ ile_item -= 1
                                            $ jabole = 0
                                        else:
                                            $ jabole -= 20
                                        "{i}*Jabole x 20 zostały usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11
                            
                            "{b}Royal Cola (+9HP){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if royal == 0:
                                            $ ile_item += 1
                                        $ royal += 1
                                        "{i}*Royal Cola x 1 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if royal == 0:
                                            $ ile_item += 1
                                        $ royal += 5
                                        "{i}*Royal Cola x 5 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if royal == 0:
                                            $ ile_item += 1
                                        $ royal += 20
                                        "{i}*Royal Cola x 20 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if royal == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if royal == 1:
                                            $ ile_item -= 1
                                        $ royal -= 1
                                        "{i}*Royal Cola x 1 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if royal == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if royal <= 5:
                                            $ ile_item -= 1
                                            $ royal = 0
                                        else:
                                            $ royal -= 5
                                        "{i}*Royal Cola x 5 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if royal == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if royal <= 20:
                                            $ ile_item -= 1
                                            $ royal = 0
                                        else:
                                            $ royal -= 20
                                        "{i}*Royal Cola x 20 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11

                            "{b}Warzywo skalne (+(4-7)HP){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if warzywo == 0:
                                            $ ile_item += 1
                                        $ warzywo += 1
                                        "{i}*Warzywo skalne x 1 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if warzywo == 0:
                                            $ ile_item += 1
                                        $ warzywo += 5
                                        "{i}*Warzywo skalne x 5 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if warzywo == 0:
                                            $ ile_item += 1
                                        $ warzywo += 20
                                        "{i}*Warzywo skalne x 20 zostało dodane do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if warzywo == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if warzywo == 1:
                                            $ ile_item -= 1
                                        $ warzywo -= 1
                                        "{i}*Warzywo skalne x 1 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if warzywo == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if warzywo <= 5:
                                            $ ile_item -= 1
                                            $ warzywo = 0
                                        else:
                                            $ warzywo -= 5
                                        "{i}*Warzywo skalne x 5 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if warzywo == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if warzywo <= 20:
                                            $ ile_item -= 1
                                            $ warzywo = 0
                                        else:
                                            $ warzywo -= 20
                                        "{i}*Warzywo skalne x 20 zostało usunięte z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11

                            "{b}Kiść bananów (+3HP FOR ALL){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if banany == 0:
                                            $ ile_item += 1
                                        $ banany += 1
                                        "{i}*Kiść bananów x 1 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if banany == 0:
                                            $ ile_item += 1
                                        $ banany += 5
                                        "{i}*Kiść bananów x 5 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if banany == 0:
                                            $ ile_item += 1
                                        $ banany += 20
                                        "{i}*Kiść bananów x 20 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if banany == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if banany == 1:
                                            $ ile_item -= 1
                                        $ banany -= 1
                                        "{i}*Kiść bananów x 1 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if banany == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if banany <= 5:
                                            $ ile_item -= 1
                                            $ banany = 0
                                        else:
                                            $ banany -= 5
                                        "{i}*Kiść bananów x 5 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if banany == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if banany <= 20:
                                            $ ile_item -= 1
                                            $ banany = 0
                                        else:
                                            $ banany -= 20
                                        "{i}*Kiść bananów x 20 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11
                            
                            "{b}Ostra Skałka (5-8 DMG){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if skalka == 0:
                                            $ ile_item += 1
                                        $ skalka += 1
                                        "{i}*Ostra Skałka x 1 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if skalka == 0:
                                            $ ile_item += 1
                                        $ skalka += 5
                                        "{i}*Ostra Skałka x 5 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if skalka == 0:
                                            $ ile_item += 1
                                        $ skalka += 20
                                        "{i}*Ostra Skałka x 20 została dodana do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if skalka == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if skalka == 1:
                                            $ ile_item -= 1
                                        $ skalka -= 1
                                        "{i}*Ostra Skałka x 1 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if skalka == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if skalka <= 5:
                                            $ ile_item -= 1
                                            $ skalka = 0
                                        else:
                                            $ skalka -= 5
                                        "{i}*Ostra Skałka x 5 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if skalka == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if skalka <= 20:
                                            $ ile_item -= 1
                                            $ skalka = 0
                                        else:
                                            $ skalka -= 20
                                        "{i}*Ostra Skałka x 20 została usunięta z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11
                            
                            "{b}Granat (4 DMG FOR ALL){/b}":
                                menu:
                                    "{b}Ile?{/b}"

                                    "{b}+1{/b}":
                                        if granat == 0:
                                            $ ile_item += 1
                                        $ granat += 1
                                        "{i}*Granat x 1 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+5{/b}":
                                        if granat == 0:
                                            $ ile_item += 1
                                        $ granat += 5
                                        "{i}*Granat x 5 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}+20{/b}":
                                        if granat == 0:
                                            $ ile_item += 1
                                        $ granat += 20
                                        "{i}*Granat x 20 został dodany do ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-1{/b}":
                                        if granat == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if granat == 1:
                                            $ ile_item -= 1
                                        $ granat -= 1
                                        "{i}*Granat x 1 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-5{/b}":
                                        if granat == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if granat <= 5:
                                            $ ile_item -= 1
                                            $ granat = 0
                                        else:
                                            $ granat -= 5
                                        "{i}*Granat x 5 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}-20{/b}":
                                        if granat == 0:
                                            "{i}*Nie masz tego przedmiotu w ekwipunku*{/i}"
                                            jump dev11

                                        if granat <= 20:
                                            $ ile_item -= 1
                                            $ granat = 0
                                        else:
                                            $ granat -= 20
                                        "{i}*Granat x 20 został usunięty z ekwipunku*{/i}"
                                        jump dev2
                                    
                                    "{b}Powrót{/b}":         
                                        jump dev11

                            "{i}<--- Strona 2/2{/i}":
                                jump dev10

                "{b}Powrót{/b}":
                    erykd "Adios!"
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna
