label menu_lokacji:
    label rynek:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg rynek
        else:
            show bg rynek_noc

        menu:
            "{b}<--- Alejka (10 min)":
                $ timer += 10
                jump alejka

            "{b}<--- Słoneczna (10 min)":
                $ timer += 10
                jump sloneczna
            
            "{b}Parking (10 min) --->":
                $ timer += 10
                jump parking

            "{b}Bohaterów Września (10 min) --->":
                $ timer += 10
                jump bohaterow_wrzesnia
    
    label sloneczna:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg sloneczna
        else:
            show bg sloneczna_noc

        menu:      
            "{b}Rynek (10 min) --->":
                $ timer += 10
                jump rynek
    
    label alejka:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg alejka
        else:
            show bg alejka_noc

        menu:      
            "{b}Rynek (10 min) --->":
                $ timer += 10
                jump rynek
    
    label parking:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg parking
        else:
            show bg parking_noc

        menu:
            "{b}<--- Wolbromska (20 min)":
                $ timer += 20
                jump wolbromska
            
            "{b}<--- Rynek (10 min)":
                $ timer += 10
                jump rynek
    
    label wolbromska:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg wolbromska
        else:
            show bg wolbromska_noc

        menu:
            "{b}Parking (20 min) --->":
                $ timer += 20
                jump parking
    
    label bohaterow_wrzesnia:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg bohaterow_wrzesnia
        else:
            show bg bohaterow_wrzesnia_noc

        menu:
            "{b}<--- Rynek (10 min)":
                $ timer += 10
                jump rynek

            "{b}<--- Lipowa (10 min)":
                $ timer += 10
                jump lipowa
    
    label lipowa:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg lipowa
        else:
            show bg lipowa_noc

        menu:
            "{b}Bohaterów Września (10 min) --->":
                $ timer += 10
                jump bohaterow_wrzesnia

            "{b}Granica Skały (20 min) --->":
                $ timer += 20
                jump granica
    
    label granica:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            show bg granica
        else:
            show bg granica_noc

        menu:
            "{b}<--- Lipowa (20 min)":
                $ timer += 20
                jump lipowa    

            "{b}TEST WALKA":
                jump faubla     










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