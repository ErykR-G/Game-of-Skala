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