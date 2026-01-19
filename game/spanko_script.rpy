default drukowanko = 0

label spanko:
    if drukowanko == 1:
        scene bg pokoj2 with fade
        play music "audio/music/drukowanie.mp3"
    else:
        scene bg pokoj with fade
        play music "audio/music/pokoj.mp3"

    show luszcz neutral at center 

    luszcz "ohhh jestem wyczerpany"
    luszcz "idę spać"

    scene bg black with fade
    stop music
    $ kostka = renpy.random.randint(1, 2)
    if kostka == 1:
        "{i}Łuszcz położył się spać{/i}"
        "{i}Podczas snu założył kilka haremów w innych światach{/i}"
        "{i}Niestety, po obudzeniu stracił wszystkie, które kochał{/i}"

    if drukowanko == 1:
        scene bg pokoj2 with fade
        play music "audio/music/drukowanie.mp3"
    else:
        scene bg pokoj with fade
        play music "audio/music/pokoj.mp3"

    label spanko_bed:
        if timer > 1200 and timer < 1800:
            $ timer = 1980
        
        else:
            if timer > 2640 and timer < 3240:
                $ timer = 3420
            
            else:
                if timer > 4080 and timer < 4680: 
                    $ timer = 4860
                
                else:
                    if timer > 5520 and timer < 6120: 
                        $ timer = 6300
                    
                    else:
                        if  timer > 6960 and timer < 7560: 
                            $ timer = 7740
                        
                        else:
                            if timer > 8400 and timer < 9000: 
                                $ timer = 9180
                            
                            else:
                                if timer > 9840 and timer < 10440:
                                    $ timer = 10620

        show luszcz neutral at center

        luszcz "Kurwa znowu w tej Polsce"
        luszcz "Nienawidzę tego syfu, tego państwa..."
        luszcz "Ehh dobra, czas brać się do roboty"

        $ luszcz_piguly = 0
        $ eminem_piguly = 0
        $ urban_piguly = 0
        $ zyd_piguly = 0
        $ kazuma_piguly = 0
        $ tarczownik_dzien = 0

        luszcz "Ooo rodzice zostawili mi kieszonkowe.."

        $ money += 3

        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

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


label spanko2:
    scene bg black with fade
    stop music
    play sound "audio/sfx/spadek.mp3"
    "{i}Oczy Łuszcza zamkneły się bez jego kontroli, a on upadł bezwładnie na ziemię{/i}"
    "{i}Podczas nieobecności jego świadomości został kilkukrotnie brutalnie zgwałcony przez 2 buldożery, które nie były zamknięte w kojcach{/i}"
    "{i}Na miejscu zdarzenia był również Owczarek Niemiecki, lecz on akurat powstrzymał się od jakikolwiek akcji{/i}"
    "{i}Po kilku godzinach snu Łuszczu otworzył oczy{/i}"

    if timer > 1200 and timer < 1800: 
            $ timer = 2100
        
    else:
        if timer > 2640 and timer < 3240: 
            $ timer = 3540
        
        else:
            if timer > 4080 and timer < 4680: 
                $ timer = 4980
            
            else:
                if timer > 5520 and timer < 6120: 
                    $ timer = 6420
                
                else:
                    if  timer > 6960 and timer < 7560: 
                        $ timer = 7860
                    
                    else:
                        if timer > 8400 and timer < 9000: 
                            $ timer = 9300
                        
                        else:
                            if timer > 9840 and timer < 10440:
                                $ timer = 10740

    $ luszcz_piguly = 0
    $ eminem_piguly = 0
    $ urban_piguly = 0
    $ zyd_piguly = 0
    $ kazuma_piguly = 0
    $ tarczownik_dzien = 0

    play music "audio/music/pole.mp3"
    if rynek == 1:
        scene bg rynek with fade
    if sloneczna == 1:
        scene bg slonneczna with fade
    if alejka == 1:
        scene bg alejka with fade
    if parking == 1:
        scene bg parking with fade
    if wolbromska == 1:
        scene bg wolbromska with fade
    if bohaterow_wrzesnia == 1:
        scene bg bohaterow_wrzesnia with fade
    if lipowa == 1:
        scene bg lipowa with fade
    if granica == 1:
        scene bg granica with fade

    show luszcz neutral at center
    
    luszcz "Ała, ale mnie dupa napierdala"
    luszcz "kurwa, ała japierdole wsyztsko boli"
    luszcz "japierdole dobra już muszę brać się do roboty..."

    hide luszcz

    if rynek == 1:
        jump rynek2
    if sloneczna == 1:
        jump slonneczna2 
    if alejka == 1:
        jump alejka2 
    if parking == 1:
        jump parking2
    if wolbromska == 1:
        jump wolbromska2
    if bohaterow_wrzesnia == 1:
        jump bohaterow_wrzesnia2 
    if lipowa == 1:
        jump lipowa2 
    if granica == 1:
        jump granica2
