
label harambe:
    label harambe1:
        scene bg cmentarz_noc with fade
        play music "audio/music/natura.mp3"
        show luszcz neutral at left

        nikt "ŁuuuUuuu"

        luszcz "Co to??"

        nikt "ŁuuuUuuuuuU"

        luszcz "Pokaż się potworze!"

        show harambe duch at slightright

        harambe "Przepraszam. Żarcik."

        luszcz "Dóch Harambe???"

        harambe "Tak."

        luszcz "Co ty tu robisz, Harambe?"

        harambe "Czarna. Magia."
        harambe "Twoja. Pamięć. Przywołała."
        harambe "Pyszne. Krówki."

        luszcz "Tak krówki są smakuwa"
        luszcz "Jaką czarną magię praktykujesz?"

        harambe "Teraz? Taniec. Węży."
        harambe "Nie Działa."
        harambe "Harambe. Instrument. Brzydko."
        harambe "Chcesz? Wazon?"

        luszcz "Wazon z węrzami? Ale na co mi?"

        harambe "Oswoić."

        luszcz "Hm... może mogłyby mi pomuc."
        luszcz "A jak je konkretnie oswoić?"

        harambe "Spokojne Miejsce. Medytować."
        harambe "Instrument. Lalala."
        harambe "Węże Tańczyć."

        $ wazon_wezy = 1
        $ ile_item_fabularne += 1
        "{i}*Wazon Węży została dodana do ekwipunku*{/i}" 

        luszcz "Aha dobra dość typowo."

        harambe "Powodzenia."

        $ harambe_social_link = 1

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
    
    label harambe2:
        scene bg alejka3v2 with fade
        play music "audio/music/alejka3.mp3"
        show luszcz neutral at slightleft
        show emina dead at right
        luszcz "Halooo"
        luszcz "O nadal są i nie odpowiadają..."

        show luszcz neutral at slightright
        hide emina dead

        $ cialo = 1
        $ ile_item_fabularne += 1
        "{i}*Zwłoki Eminema zostały dodane do ekwipunku*{/i}" 

        luszcz "No i po robocie"

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



