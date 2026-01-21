
label trump:
    label trump1:
        play music "audio/music/usa.mp3"
        show luszcz neutral zorder 15:
            xalign 0.6
            yalign 1.0
        luszcz "Chwila, od kiedy tu stoi mur?"

        show trump neutral zorder 16 at right

        trump "Od dzisiaj!"
        trump "Budujemy piękny, wielki mur!"
        trump "Będzie taki duży, i taki wielki,"
        trump "Że Kraków nie zabierze nam ani jednej latynoski!"

        luszcz "Ale w Skale nie ma latynosek…"

        trump "No widzisz, jednak gdy ja pobiegnę na prezydenta…"
        trump "W Skale będą latynoski."
        trump "Luigi! Kup więcej budulca!"

        show luigi neutral right at left
        luigi "Mamma mia!"
        show luigi neutral at left

        trump "Maduro! Wal dużo zaprawy! Niech zaprawa cieknie!"

        show maduro neutral right at slightleft

        maduro "Dobrze szefuniu."

        show maduro neutral at slightleft

        trump "Ufff…"
        trump "Budowanie muru jest takie męczące…"
        trump "Te młody, nie pomógłbyś nam? Dobrze ci za to zapłacę."

        menu:
            "{b}Pomóż{/b}":
                if lopatka == 1:
                    $ trump_social_link = 2
                    jump trump3
                else:
                    $ trump_social_link = 1
                    luszcz "Czas zrobić skałę wielką znowu"

                    trump "Dokładnie tak! To weź swoją łopatkę i…"
                    trump "Chwila, ty nie masz łopatki."
                    trump "Co sobie myślisz, że dam ci do rączki za darmo zabawki do pracy?"
                    trump "Może jeszcze ci ogarnę opiekę zdrowotną?"

                    luszcz "Pewnie"

                    trump "Nie!! Niepewnie! Nie pokazuj się tu bez łopatki!"
                    trump "Znikaj mi z oczu!"

                    if mleczarz_social_link == 0 and krowka == 1:
                        luszcz "Jeszcze jedna sprawa panie Trump!"
                        luszcz "Mam dla pana dostawę krówek"

                        $ krowka = 0
                        trump "Ohh to są przepiękne, przepiękne krówki."
                        trump "Mam nadzieję że zrobią dobrą robotę, jako klocki budowlane."
                        trump "Ewentualnie, jako smakołyki dla pracowników."
                        trump "Tu masz pieniądze."

                        $ money += 2
                        $ mleczarz_social_link = 1

                        "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

                        luszcz "Dziękuję dowidzenia!"

                    hide trump 
                    hide luigi 
                    hide luszcz 
                    hide maduro
                    play music "audio/music/pole.mp3"
                    jump granica2

            "{b}Nie pomagaj{/b}":
                $ trump_social_link = 10

                luszcz "W tyłku mam nie pomagam"

                trump "Dobrze, jeśli nie chcesz moich fajnych nagród…"
                trump "Mam taką fajną nagrodę za pomoc…"
                trump "Ale zatrzymam ją dla siebie…"

                if mleczarz_social_link == 0 and krowka == 1:
                    luszcz "A jeszcze jedna sprawa panie Trump"
                    luszcz "Mam dla pana dostawę krówek"

                    $ krowka = 0
                    trump "Ohh to są przepiękne, przepiękne krówki."
                    trump "Mam nadzieję że zrobią dobrą robotę, jako klocki budowlane."
                    trump "Ewentualnie, jako smakołyki dla pracowników."
                    trump "Tu masz pieniądze."

                    $ money += 2
                    $ mleczarz_social_link = 1

                    "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

                    luszcz "Dziękuję dowidzenia!"
                hide trump 
                hide luigi 
                hide luszcz 
                hide maduro
                play music "audio/music/pole.mp3"
                jump granica2

    label trump2:
        play music "audio/music/usa.mp3"
        show trump neutral zorder 16 at right
        show luigi neutral at left
        show luszcz neutral zorder 15:
            xalign 0.6
            yalign 1.0
        show maduro neutral at slightleft
        luszcz "Morze jednak kupisz mi jedną łopatkę?"
        luszcz "Me ręce są gotowe do pracy"

        trump "Nie! Wróć jak będziesz miał własną!"
        play music "audio/music/pole.mp3"
        hide trump 
        hide luigi 
        hide luszcz
        hide maduro 
        jump granica2

    
    label trump3:
        show trump neutral zorder 16 at right
        show luigi neutral at left
        show luszcz neutral zorder 15:
            xalign 0.6
            yalign 1.0
        show maduro neutral at slightleft
        $ trump_social_link = 2
        luszcz "Dobra mam łopatkę"

        trump "To dobrze, podbuduj trochę, bo Luigi i Manduro mają przerwę na lunch"

        luszcz "Fundujesz im jedzenie?"

        trump "Oczywiście że nie, pewnie znów poszli zjadać koty."
        trump "Do roboty!"

        scene bg black with fade

        luszcz "Praca, praca."
        luszcz "Praca, praca, praca."
        luszcz "Praca, praca, praca, praca."

        if timer >= 360 and timer <= 1200:       
            scene bg granica with fade

        if timer >= 1800 and timer <= 2640:
            scene bg granica2 with fade

        if timer >= 3240 and timer <= 4080:
            scene bg granica3 with fade

        if timer >= 4680 and timer <= 5520:
            scene bg granica4 with fade

        if timer >= 6120 and timer <= 6960:
            scene bg granica5 with fade

        if timer >= 7560 and timer <= 8400:
            scene bg granica6 with fade

        if timer >= 9000 and timer <= 9840:
            scene bg granica7 with fade

        if timer >= 10440 and timer <= 11280:
            scene bg granica8 with fade
        
        show trump neutral zorder 16 at right
        show luigi neutral at left
        show luszcz neutral zorder 15:
            xalign 0.6
            yalign 1.0
        show maduro neutral at slightleft

        luszcz "Dobrze, skończyłem!"
        luszcz "Oczekuję wypłaty."

        trump "O nie, nie mam przy sobie żadnych pieniędzy!"
        trump "Jakkolwiek inaczej mógłbym ci się odpłacić…"
        trump "Hm…"
        trump "Może weź moją Cybertruck Tesle. Już jej nie potrzebuję."

        luszcz "Dzięki i guess…"

        $ cybertruck = 1
        $ ile_item_fabularne += 1
        "{i}*Cybertruck został dodany do ekwipunku*{/i}" 

        if mleczarz_social_link == 0 and krowka == 1:
            luszcz "A jeszcze jedna sprawa panie Trump"
            luszcz "Mam dla pana dostawę krówek"

            $ krowka = 0
            trump "Ohh to są przepiękne, przepiękne krówki."
            trump "Mam nadzieję że zrobią dobrą robotę, jako klocki budowlane."
            trump "Ewentualnie, jako smakołyki dla pracowników."
            trump "Tu masz pieniądze."

            $ money += 2
            $ mleczarz_social_link = 1

            "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"
        
        luszcz "Pzdr"
        play music "audio/music/pole.mp3"



        $ trump_wybory = 1
        hide trump 
        hide luigi 
        hide luszcz
        hide maduro 
        jump granica2