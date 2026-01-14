label menu_lokacji:
    label rynek:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg rynek
        else:
            scene bg rynek_noc

        menu:
            "{i}<--- Alejka (10 min){/i}":
                $ timer += 10
                jump alejka

            "{i}<--- Słoneczna (10 min){/i}":
                $ timer += 10
                jump sloneczna
            
            "{i}Parking (10 min) --->{/i}":
                $ timer += 10
                $ kostka = renpy.random.randint(1, 10)
                if kostka == 1:
                    "{i}Podczas podróży napotykasz na niespodziewaną przeszkodę{/i}"
                    jump raem_fight
                jump parking

            "{i}Bohaterów Września (10 min) --->{/i}":
                $ timer += 10
                jump bohaterow_wrzesnia
    
    label sloneczna:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg sloneczna
        else:
            scene bg sloneczna_noc

        menu:      
            "{i}Rynek (10 min) --->{/i}":
                $ timer += 10
                jump rynek
            
            "{b}Plac Broni (10min){/b}":
                $ timer += 10
                $ lopatka = 1
                "{i}dostajesz łopatke{/i}"
                jump sloneczna
    
    label alejka:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg alejka
        else:
            scene bg alejka_noc

        menu:      
            "{i}Rynek (10 min) --->{/i}":
                $ timer += 10
                jump rynek
            
            "{b}Sklep Monopolowy (60 min){/b}" if zyd_social_link == 0:
                $ timer += 60
                jump zyd1
            
            "{b}Sklep Monopolowy (15 min){/b}" if zyd_social_link > 0:
                $ timer += 15
                jump sklep_monopolowy
    
    label parking:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg parking
        else:
            scene bg parking_noc

        menu:
            "{i}<--- Wolbromska (20 min){/i}":
                $ timer += 20
                jump wolbromska
            
            "{i}<--- Rynek (10 min){/i}":
                $ timer += 10
                jump rynek
    
    label wolbromska:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg wolbromska
        else:
            scene bg wolbromska_noc

        menu:
            "{i}Parking (20 min) --->{/i}":
                $ timer += 20
                jump parking
    
    label bohaterow_wrzesnia:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg bohaterow_wrzesnia
        else:
            scene bg bohaterow_wrzesnia_noc

        menu:
            "{i}<--- Rynek (10 min){/i}":
                $ timer += 10
                jump rynek

            "{i}<--- Lipowa (10 min){/i}":
                $ timer += 10
                jump lipowa
    
    label lipowa:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg lipowa
        else:
            scene bg lipowa_noc

        menu:
            "{i}Bohaterów Września (10 min) --->{/i}":
                $ timer += 10
                jump bohaterow_wrzesnia

            "{i}Granica Skały (20 min) --->{/i}":
                $ timer += 20
                jump granica
            
            "{b}Cmentarz Żydowski (30 min){/b}" if zyd_social_link == 1:
                $ timer += 30
                jump zyd2
            
            "{b}Cmentarz (15 min){/b}" if zyd_social_link == 2:
                $ timer += 15
                jump zyd3
            
            "{b}Cmentarz (3h){/b}" if zyd_social_link == 3:
                if lopatka == 1:
                    $ timer += 180
                    jump zyd4
                else:
                    "{i}Na cmentarzu czeka na mnie żyd, ale nadal nie zdobyłem dla niego łopatki{/i}"
                    "{i}Muszę się tym zająć zanim się z nim spotkam{/i}"
                    jump lipowa
    
    label granica:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg granica
        else:
            scene bg granica_noc

        menu:
            "{i}<--- Lipowa (20 min){/i}":
                $ timer += 20
                jump lipowa    
            
            "{b}Cmentarz Żydowski (30 min){/b}" if zyd_social_link == 1:
                $ timer += 30
                jump zyd2
            
            "{b}Cmentarz (15 min){/b}" if zyd_social_link == 2:
                $ timer += 15
                jump zyd3
            
            "{b}Cmentarz (3h){/b}" if zyd_social_link == 3 and lopatka == 1:
                if lopatka == 1:
                    $ timer += 180
                    jump zyd4
                else:
                    "{i}Na cmentarzu czeka na mnie żyd, ale nadal nie zdobyłem dla niego łopatki{/i}"
                    "{i}Muszę się tym zająć zanim się z nim spotkam{/i}"
                    jump lipowa

            "{b}TEST WALKA{/b}":
                jump faubla     






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





    label faubla:
        scene bg korytarz
        menu:
            "{b}Ilu masz przyjaciół?{/b}"

            "{b}DUŻO{/b}":
                $ liczba_sojusznikow += 3
                $ eminem_sojusznik += 1
                $ urban_sojusznik += 1
                $ zyd_sojusznik += 1
                $ kazuma_sojusznik += 1
                $ tarczownik_sojusznik += 1
                $ stop = 1
                $ miecz_swietlny = 1
                $ ostrza_chaosu = 1
                $ patyk = 1
                $ bazooka = 1
                $ miecz3d = 1
                $ przepychaczka_liczba = 3
                $ luszcz_przepychaczka = 1
                $ urban_przepychaczka = 1
                $ zyd_przepychaczka = 1
                $ kazuma_przepychaczka = 1
                $ tarczownik_przepychaczka = 1
                $ klata_liczba = 2
                $ luszcz_klata = 1
                $ urban_klata = 1
                $ zyd_klata = 1
                $ kazuma_klata = 1
                $ tarczownik_klata = 1
                $ eminem_klata = 1
                $ ring = 1
                $ vr = 1
                $ memy = 1
                $ ziemia = 1
                $ nogi = 1
                $ zloty = 1

                $ ile_item = 13
                $ piknik = 1
                $ cake = 1
                $ pills = 20
                $ woda = 2
                $ ostry = 2
                $ lagodny = 3
                $ drpepper = 5
                $ jabole = 5
                $ royal = 4
                $ warzywo = 3
                $ banany = 4
                $ skalka = 2
                $ granat = 3


            "{b}TROCHE{/b}":
                $ liczba_sojusznikow += 2
                $ eminem_sojusznik += 1
                $ zyd_sojusznik += 1
                $ stop = 1
                $ miecz_swietlny = 1
                $ ostrza_chaosu = 1
                $ patyk = 1
                $ bazooka = 1
                $ miecz3d = 1
                $ przepychaczka_liczba = 3
                $ luszcz_przepychaczka = 1
                $ zyd_przepychaczka = 1
                $ klata_liczba = 2
                $ luszcz_klata = 1
                $ zyd_klata = 1
                $ eminem_klata = 1
                $ ring = 1
                $ vr = 1
                $ memy = 1
                $ ziemia = 1
                $ nogi = 1
                $ zloty = 1

                $ ile_item = 13
                $ piknik = 1
                $ cake = 1
                $ pills = 20
                $ woda = 2
                $ ostry = 2
                $ lagodny = 3
                $ drpepper = 5
                $ jabole = 5
                $ royal = 4
                $ warzywo = 3
                $ banany = 4
                $ skalka = 2
                $ granat = 3

            "{b}MAM{/b}":
                $ liczba_sojusznikow += 1
                $ eminem_sojusznik += 1
                $ stop = 1
                $ miecz_swietlny = 1
                $ ostrza_chaosu = 1
                $ patyk = 1
                $ bazooka = 1
                $ miecz3d = 1
                $ przepychaczka_liczba = 3
                $ luszcz_przepychaczka = 1
                $ klata_liczba = 2
                $ luszcz_klata = 1
                $ eminem_klata = 1
                $ ring = 1
                $ vr = 1
                $ memy = 1
                $ ziemia = 1
                $ nogi = 1
                $ zloty = 1

                $ ile_item = 13
                $ piknik = 1
                $ cake = 1
                $ pills = 20
                $ woda = 2
                $ ostry = 2
                $ lagodny = 3
                $ drpepper = 5
                $ jabole = 5
                $ royal = 4
                $ warzywo = 3
                $ banany = 4
                $ skalka = 2
                $ granat = 3

                
            "{b}CO TO?{/b}":
                pass

        "{i}O bogowie walka{/i}"
        jump fight11

    label after_fight11:
        "{i}Gratulacje wygrałeś{/i}"
        jump rynek