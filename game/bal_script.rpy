label bal:
    label bal1:
        if gdzie_spisz == 0:
            show luszcz neutral at slightleft
            show tata neutral at slightright

            tata "Czego to synu nienawidzisz!?!?"

            luszcz "Eeee yyy eee"
            luszcz "Sorry tata, tak się wymskneło..."

            tata "No ja mam nadzieję!"
            tata "Ten kraj dał Ci wszystko co masz!!!"

            luszcz "Tak wiem tata..."

            tata "Noo, i żeby to się więcej nie powtórzyło!"

            luszcz "..."

            luszcz "A eee po coś przyszedłeś?"

            tata "A no tak"
            tata "Dostaliśmy zaproszenie na Bal u Ambasadora, który będzie dziś o 20:00 w naszej rodzimej Skale!"
            tata "Dlatego punkt 20:00 masz być już w domu gotowy do wyjścia!"

            luszcz "Ehhh, a muszę iść!?"

            tata "Musisz!"

            luszcz "dobrze tate"

            tata "O i byłbym zapomniał!"

            $ money += 3

            "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

            tata "Masz tu małe kieszonkowe i baw się dziś dobrze!"

            luszcz "Dzięki tate, tak zrobię"

            hide tata
            show luszcz neutral at center

            luszcz "(Ehhhh, no cóż chyba będzie trzeba udać się na ten głópi bal...)"

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
        
        else:
            show luszcz neutral at slightleft
            show tata neutral at slightright

            tata "Synu!??? Co ty tu robisz!?!?"

            luszcz "O cześć tata ja eeee..."

            tata "Wiesz jak się matka martwiła, że nie wróciłeś do domu!????"
            tata "Wydzwaniała chyba do drugiej w nocy, ale nie odbierałeś!!!!?!?!?!?"

            luszcz "Sorry tata, telefon mi się rozładował..."
            luszcz "To już się nie powtórzy."

            tata "No ja mam nadzieję!"

            luszcz "..."

            luszcz "A eee co tutaj robisz?"

            tata "Szukałem Ciebię, bo mam Ci coś do przekazania."
            tata "Dostaliśmy zaproszenie na Bal u Ambasadora, który będzie dziś o 20:00 w naszej rodzimej Skale!"
            tata "Dlatego punkt 20:00 masz być już w domu gotowy do wyjścia!"

            luszcz "Ehhh, a muszę iść!?"

            tata "Musisz!"

            luszcz "dobrze tate"

            tata "O i byłbym zapomniał!"

            $ money += 3

            "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

            tata "Masz tu małe kieszonkowe i baw się dziś dobrze!"

            luszcz "Dzięki tate, tak zrobię"

            hide tata
            show luszcz neutral at center

            luszcz "(Ehhhh, no cóż chyba będzie trzeba udać się na ten głópi bal...)"

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
    
    label bal2:
        scene bg chinczyk with fade
        show luszcz neutral at center
        luszcz "GÓWNO 1"

