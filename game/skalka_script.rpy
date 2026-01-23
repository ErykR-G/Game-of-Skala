default samobojstwo = 0
label skalka:
    label skalka1:
        scene bg start with fade
        play music "audio/music/wiatr.mp3"
        show luszcz siedzi right at slightright
        luszcz "Ej a co jakbym się teraz zabił"
        luszcz "Morze bym sobie skoczył teraz z klifu i się zabił"
        luszcz "Taki ładny widok"
        luszcz "Ómrzeć przy ulóbionym widoku"

        show luszcz neutral right at slightright

        luszcz "Tak myślę że to zrobię"
        luszcz "Najwarzniejsza zasada na takie momenty"
        luszcz "Nie myśleć o konsekwencjach"
        luszcz "Me ostatnie słowa:"
        luszcz "Nie mam pomysłu"
        luszcz "Hopsasa"

        show luszcz neutral right:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        scene bg black with fade
        "{i}Łuszczu skoczył z klifu{/i}"
        "{i}ziuuuu{/i}"
        "{i}btż{/i}"
        $ samobojstwo = 1
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"
        jump gotka1

    label skalka2:
        scene bg start with fade
        play music "audio/music/wiatr.mp3"
        show luszcz siedzi right at right

        luszcz "Okej, Harambe kazał mi pomedytować w spokojnym miejscu i grać wężom muzykę."

        if gitara == 2:
            luszcz "Czas postawić wazon"
        else:
            luszcz "Tylko kurcze nie załorzyłem niczego do grania muzyki!"

            while not gitara == 2:
                $ renpy.pause(0.2, hard=True)
            
            luszcz "Czas postawić wazon"
        
        $ wazon_wezy = 0
        $ ile_item_fabularne -= 1
        show waza at slightright

        luszcz "Usiąść"
        luszcz "I otworzyć umysł…"

        play sound "audio/sfx/cyce.mp3"
        "{i}Łuszczu zaczyna grać na gitarze{/i}"

        scene bg black with fade
        scene bg start with fade
        show luszcz siedzi right at right
        stop sound

        luszcz "Uwielbiam muzykę…"
        luszcz "A jak tam wężę?"
        luszcz "O wow.. Cała bazooka?"
        luszcz "Najs."
        luszcz "Dzięki Harambe"

        $ bazooka = 1
        "{i}*Wężowa Bazooka została dodana do ekwipunku*{/i}" 

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