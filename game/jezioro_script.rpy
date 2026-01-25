default dzien_lowionko = 0
default noc_lowionko = 0
default ailbib_odebrany = 0
default dinozaur_odebrany = 0
default vr_odebrany = 0
default spanko_ryby = 0

label jezioro:
    label jezioro1:
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            scene bg jezioro3 with fade
        else:
            scene bg jezioro5 with fade
        play music "audio/music/ryby.mp3"

        luszcz "Rybki dzwonią, muszę iść!"

        label jezioro12:
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                scene bg jezioro3
            else:
                scene bg jezioro5

            if timer > 1200 and timer < 1800 or timer > 2640 and timer < 3240 or timer > 4080 and timer < 4680 or timer > 5520 and timer < 6120 or timer > 6960 and timer < 7560 or timer > 8400 and timer < 9000 or timer > 9840 and timer < 10440 or timer > 11280:
                $ spanko_ryby += 1
                if spanko_ryby == 1:
                    $ spanko += 1
                if spanko_ryby == 3:
                    $ spanko += 1
                if spanko_ryby == 5:
                    $ spanko += 1
                if spanko_ryby == 7:
                    $ spanko += 1
                if spanko_ryby == 9:
                    $ spanko += 1
                if spanko_ryby == 11:
                    $ spanko += 1
                if spanko_ryby == 13:
                    $ spanko += 1
                if spanko_ryby == 15:
                    $ spanko += 1
                if spanko_ryby == 17:
                    $ spanko += 1

                if spanko == 1 and spanko_ryby == 1:
                    play music "audio/music/pole_noc.mp3"
                    luszcz "Robię się troszkę śpiący..."
                else:
                    if spanko == 5 and spanko_ryby == 9:
                        luszcz "Jezu jestem mega śpiący..."
                    else:
                        if spanko == 9 and spanko_ryby == 17:
                            luszcz "Nie, nie dam rady"
                            jump spanko2
                        else:
                            if timer > 1620 and timer < 1980 or timer > 3060 and timer < 3420 or timer > 4500 and timer < 4860 or timer > 5940 and timer < 6300 or timer > 7380 and timer < 7740 or timer > 8820 and timer < 9180 or timer > 10260 and timer < 10620 or timer > 11700:
                                luszcz "Nie, nie dam rady"
                                jump spanko2  

            menu:
                "{b}Łów (10min){/b}":
                    play sound "audio/sfx/start.mp3"
                    $ timer += 10
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        $ dzien_lowionko += 1
                        scene bg jezioro2
                    else:
                        $ noc_lowionko += 1
                        $ dzien_lowionko += 1
                        scene bg jezioro4
                    luszcz "…"

                "{b}Wyjdź{/b}":
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump granica
            
            $ kostka = renpy.random.randint(1, 15)
            if kostka == 1:
                luszcz "Życie by było piękne gdyby janiak zwalił erykowi konia"
            
            if kostka == 2:
                luszcz "Nie czuję … nie czuję mojego suta"
            
            if kostka == 3:
                luszcz "Julian to jest taka hela tylko mamy nad nią kontrole"
            
            if kostka == 4:
                luszcz "Założyłbym cię na wendkę i cię spuścił"
            
            if kostka == 5:
                luszcz "Jeśli miałbym mieć kiedyś body pillow to tylko z Allozaurem"
            
            if kostka == 6:
                luszcz "”to nie wejdzie!” ”to nie wejdzie!” i tak mówiliśmy przez pół godziny"
            
            if kostka == 7:
                luszcz "Margaryna"
            
            if kostka == 8:
                luszcz "Osama bin Laden mnie przeleciał"
            
            if kostka == 9:
                luszcz "Nie kupujcie lemoniady bo to sama woda z cytryną"
            
            if kostka == 10:
                luszcz "Zrobię Brawl Stars w pythonie tylko dodam sex"
            
            if kostka == 11:
                luszcz "Wait jak miał na imię Bartek?"
            
            if kostka == 12:
                luszcz "Umiem wyobrażać sobie ludzi w stroju ziemniaka"
            
            if kostka == 13:
                luszcz "Zawsze bądź sobą. Chyba że możesz być rybakiem."
            
            if kostka == 14:
                luszcz "Obracam wielkimi sumami."
            
            if kostka == 15:
                luszcz "Wszystkie gotki czekają na dobrego rybaka."

            luszcz "…"
            luszcz "…!"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                scene bg jezioro3
            else:
                scene bg jezioro5

            if noc_lowionko == 3 and ailbib_odebrany == 0:
                play sound "audio/sfx/powrot.mp3"
                $ ailbib_odebrany = 1
                show ailbib2 at ryba
                luszcz "O jacie złowroga księga"

                ai "Tak to jestem ja."
                ai "Jak mnie znalazłeś to możesz mnie sobie przywłaszczyć."

                luszcz "Fajnie"

                if biblia == 1:
                    bi "Ej hola hola"
                    bi "A może ja mam coś do powiedzenia?"
                    bi "To jest literalnie anty-ja"
                    bi "Nie bierz jej jest niebezpieczna"

                    ai "Sklej pizde nawet nie wiesz jaka w czeluściach piekła jest stypa"
                    ai "Prosze weź mnie ze sobą może się do czegoś przydam???"

                    luszcz "Biblio, to jest gra wideo, ja bym chciał zebrać w miarę morzliwości wszystkie itemki"

                    bi "Nie ma tak królu złoty"
                    bi "Bóg dał ci wolną wolę ale mi z jakiegoś powodu też."
                    bi "Jak chcesz to bierz tą wiedźmę ale wtedy ja stąd spadam"

                    ai "Ha bardzo dobrze! I tak nikt cię pewnie nawet w połowie nie przeczytał"

                    bi "Ok what ever jakby ciebie też"

                    ai "Dobra spadaj"

                    luszcz "Drogie panie, proszę się nie kłucić."

                    ai "Okej to może wybierz jedną z nas"

                    bi "No"

                    menu:
                        "{b}Wolę Biblię{/b}":
                            bi "Sigma sigma boy sigma boy sigma boy"
                            bi "Dobrze robisz synu"
                            bi "Po dobrej ścieżce wędrujesz"

                            ai "Ok walcie się spadam stąd!!"

                            hide ailbib2
                            play sound "audio/sfx/beta.mp3"

                            bi "Krótko z nią"
                        
                        "{b}Wolę Ęilbib{/b}":
                            ai "Hel jes"

                            bi "Nie tak nie można..! Do piekła za to pójdziesz!"

                            luszcz "Tam też mam paru ziomkuw do odwiedzenia"

                            bi "Ok ale masz też nieskończone cierpienie"

                            luszcz "Pżyzwyczaję się"

                            ai "Dosłownie nie jest arz tak źle"
                            ai "W piątki grupowo wymyślamy mokre sny dla śmiertelników"

                            bi "To jest dramat"
                            bi "Idę się poskarżyć Bogu!"

                            $ biblia = 0
                            $ ile_item_fabularne -= 1

                            ai "Krótko z nią"

                            $ ailbib = 1
                            $ ile_item_fabularne += 1
                            hide ailbib2
                            play sound "audio/sfx/beta.mp3"
                            "{i}*Ailbib został dodany do ekwipunku*{/i}" 
                else:
                    $ ailbib = 1
                    $ ile_item_fabularne += 1
                    hide ailbib2
                    play sound "audio/sfx/beta.mp3"
                    "{i}*Ailbib został dodany do ekwipunku*{/i}" 
            
                jump jezioro12

                            
            if dzien_lowionko >= 3 and dinozaur_odebrany == 0:
                $ dinozaur_odebrany = 1
                play sound "audio/sfx/powrot.mp3"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    show dinozaur at ryba
                else:
                    show dinozaur2 at ryba

                luszcz "wow jakiś dinożarł"

                d "rawr"

                luszcz "Ja ciebie też"
                luszcz "yay"
                luszcz "Myślę że może mi się do czegoś przydać."

                $ dinozaur = 1
                $ ile_item_fabularne += 1
                hide dinozaur
                hide dinozaur2
                play sound "audio/sfx/beta.mp3"
                "{i}*Dinożarł został dodany do ekwipunku*{/i}" 
                jump jezioro12
            

            if dzien_lowionko >= 7 and vr_odebrany == 0:
                $ vr_odebrany = 1
                play sound "audio/sfx/powrot.mp3"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    show vr at ryba
                else:
                    show vr2 at ryba

                luszcz "O kurcze to moje gogle vr"
                luszcz "Pewnie siostra chciała je umyć"
                luszcz "Myślę że noszenie ich podczas walki to dobry pomysł"

                $ vr = 1
                hide vr2
                hide v
                play sound "audio/sfx/beta.mp3"
                "{i}*VR Headset został dodany do ekwipunku*{/i}" 
        
                jump jezioro12
            
            label losowanko_jezioro12:
                $ kostka = renpy.random.randint(1, 112)
                if kostka == 1:
                    play sound "audio/sfx/powrot.mp3"
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        show granatr at ryba
                    else:
                        show granatr2 at ryba
                    
                    luszcz "Bombastycznie, granat"

                    if granat == 0:
                        $ ile_item += 1
                    $ granat += 1
                    hide granatr2
                    hide granatr
                    play sound "audio/sfx/beta.mp3"
                    "{i}*Granat został dodany do ekwipunku*{/i}" 

                    jump jezioro12
                
                if kostka == 2:
                    play sound "audio/sfx/powrot.mp3"
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        show banany at ryba
                    else:
                        show bananyr2 at ryba
                    
                    luszcz " Uuu uu aa aa iii uu u u"

                    if banany == 0:
                        $ ile_item += 1
                    $ banany += 1
                    hide bananyr2
                    hide bananyr
                    play sound "audio/sfx/beta.mp3"
                    "{i}*Kiść bananów została dodana do ekwipunku*{/i}" 

                    jump jezioro12









                jump jezioro12

