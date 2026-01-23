
label babcia:
    label babcia1:
        scene bg dom_kultury with fade
        play music "audio/music/dom_kultury.mp3"
        show luszcz neutral at left
        show babcia neutral at center

        babcia "Oh… Witaj kochaniutki"

        luszcz "Dzień dobry, gdzie cała reszta?"

        babcia "Wszyscy odpuścili sobie dom kultury po całym incydencie z czarodziejem"
        babcia "Zostałam tylko ja, i szyję sobie szaliki."
        babcia "A potrzebujesz czegoś?"

        luszcz "Nie do końca, po prostu fajnie by było przekonać lódzi do walki o Skałę."

        babcia "Moje poparcie masz."

        luszcz "Dziękuję pani."

        babcia "Uszyć ci może szalik?"
        
        luszcz "Skąd się bieże pani uprzejmość?"

        babcia "Cóż, przede wszystkim, uprzejmość nie musi się skądś brać."
        babcia "Jestem tobie jednak bardzo wdzięczna za pokonanie tego czarodzieja."
        babcia "Bardzo go nielubiłam."
        babcia "Nigdy nie mogliśmy się dogadać."
        babcia "Nie dlatego że ma touretta, tylko dlatego że jest czarny."

        luszcz "Ah."
        luszcz "Anyway jeśli pani hce to chętnie przyjmę od pani szalik."

        babcia "Dobrze, tylko przynieś mi proszę jakiś materiał"
        babcia "Kończy mi się włóczka więc będziemy musieli szpącić dookoła."

        luszcz "Hm… materiał…"
        luszcz "Mam 5 terabajtuw memów na konkuterze, czy to zadziała?"

        babcia "Nie jestem pewna co to znaczy, ale chyba tak.."
        babcia "Zobaczymy, gdy je przyniesiesz."

        luszcz "W takim razie pójdę po nie."

        babcia "Dobrze mój drogi."

        $ babcia_wybory == 2
        $ babcia_social_link = 1
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
    
    label babcia2:
        scene bg pokoj with fade
        play music "audio/music/pokoj.mp3"
        show luszcz neutral at center
        luszcz "Okej, gdzie ja miałem folder z memami…"
        luszcz "O, jest!"
        luszcz "O, jest!"
        luszcz "O nie…"
        luszcz "Są dwa…"
        luszcz "Oj…………….."
        luszcz "Który folder wybrać…?"

        menu:
            "{b}memy{/b}":
                show mem zorder 50 at center

            "{b}Memy{/b}":
                show mem zorder 50 at center

        nikt "Fan fakt:"
        nikt "Czy wiecie że PopCap, studio które stworzyło pvz"
        nikt "Było oryginalnie stworzone pod nazwą “Sexy Action Cool”?"
        nikt "Ich pierwszą grą wideo był strip poker, który miał zarabiać pieniądze na ich późniejsze tytuły."

        hide mem

        luszcz "Okej, w takim razie to ten drugi folder."

        $ babcia_social_link = 2
        $ ile_item_fabularne += 1
        $ folder_memow = 1

        "{i}*Folder Memów został dodany do ekwipunku*{/i}" 

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

    label babcia3:
        scene bg dom_kultury with fade
        play music "audio/music/dom_kultury.mp3"
        show luszcz neutral at left
        show babcia neutral at center

        babcia "Czy masz materiał, o który prosiłam?"

        luszcz "Mam!"


        luszcz "Proszę, oto wszystkie memy kture posiadam."

        babcia "Dziękuję. Zamknij na chwilkę oczy."

        luszcz "Oki"
        
        scene bg black with fade
        scene bg dom_kultury with fade
        show luszcz neutral at left
        show babcia neutral at center

        babcia "Proszę, oto twój szalik"

        luszcz "Wow ale fajny"

        $ memy = 1
        "{i}*Szalik z Memów został dodany do ekwipunku*{/i}" 

        luszcz "Dziękuję, rasistowska babciu"

        babcia "Nie ma za co, bogaty seksisto"
        babcia "Skop księdzu dupsko"

        luszcz "Spk."

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




