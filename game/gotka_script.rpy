default gotka_szpan = 0
default wypadek1 = 0
default wypadek2 = 0

label gotka:
    label gotka1:
        scene bg klinika with fade
        play music "audio/music/klinika.mp3"
        gotka "Dzień dobry w czym mogę pomóc?"
        gotka "To twoja pierwsza wizyta tutaj?"

        luszcz "(o kurcze to gotka)"
        luszcz "(mószę to dobrze zagrać)"
        luszcz "Czy pani jest wolna?"
        luszcz "Znaczy, ma pani czas na wizytę?"
        luszcz "W sensie, czy mogę być tu przebadany?"

        gotka "..."
        gotka "Czy to pilne?"

        jump gotka3
    
    label gotka2:
        scene bg klinika with fade
        play music "audio/music/klinika.mp3"
        gotka "Dzień dobry w czym mogę pomóc?"

        jump gotka3

    label gotka3:
        menu:
            "{b}Shadow: Ręka{/b}" if wypadek1 == 1:
                $ wypadek1 = 2
                $ gotka_social_link += 1

                gotka "hm...."
                gotka "Dobrze, proszę się wybrać do gabinetu."


            "{b}Łuszcz: Kostka{/b}" if wypadek2 == 1:
                $ wypadek2 = 2
                $ gotka_social_link += 1

                gotka "hm...."
                gotka "Dobrze, proszę się wybrać do gabinetu."

                
            "{b}Wymyśl coś{/b}" if gotka_szpan == 0:
                $ gotka_szpan = 1

                luszcz "Trochę tak... w sesnie... zacząłem trochę, kaszleć i w ogule."

                gotka "To wez se jakieś przeciwbólowe, połóż się spać i wróć do mnie jak dostaniesz jakiś skibidi skrzep mózgowy."

                luszcz "Dobrze..."
                luszcz "(googly moogly muszę znaleźć powody rzeby się z nią widywać)"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking
            
            "{b}Wymyśl coś{/b}" if gotka_szpan == 1:
                $ gotka_szpan = 2
                luszcz "Mam wrażenie że moja dupa pękła."

                gotka "Dupy powinny być pęknięte"

                luszcz "Dobra to nieważne"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking
            
            "{b}Wymyśl coś{/b}" if gotka_szpan == 2:
                $ gotka_szpan = 3
                luszcz "Wydaje mi się, że mam autyzm."

                gotka "Wszystkiego najlepszego!"
                gotka "Tutaj nie praktykujemy lobotomii."

                luszcz "Siara"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking
            
            "{b}Wymyśl coś{/b}" if gotka_szpan == 3:
                $ gotka_szpan = 4
                luszcz "Mam potężne zatwardzenie."

                gotka "To masz tutaj jabola i kolke wiśniową, powinno pomóc"

                if jabole == 0:
                    $ ile_item += 1
                $ jabole += 1

                if drpepper == 0:
                    $ ile_item += 1
                $ drpepper += 1

                "{i}*Jabol i Dr Pepper zostały dodane do ekwipunku*{/i}" 

                luszcz "Dziękuję bardzo… to dowidzenia."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking
            
            "{b}Dowidzenia{/b}" if gotka_szpan == 4:
                luszcz "Proszę pani, cierpię na swf…"

                gotka "hm?"

                luszcz "Mówiłem, że cierpię na fgk.."

                gotka "Na co?"

                luszcz "Ufo!!! Essa"
                luszcz "Dowidzenia"

                gotka "Spierdalaj"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking

        label gotka4:
            scene bg klinika2
            show luszcz neutral right at right
            show eminem neutral at center
            show gotka neutral at left

            gotka "... więc odciął sobie rękę rzucając się na Twój miecz świetlny?"

            luszcz "Dokladnie tak."
            luszcz "Trzymałem go jako formę samoobrony."

            eminem "Tak... głupio się przyznać... źle oceniłem jego moc i umiejętności..."
            eminem "Gdybym wiedział że jest najpotężniejszym Jedi na świecie nigdy bym do niego nie podszedł."

            luszcz "Ależ bez przesady."
            luszcz "Mogę być najpotężniejszym Jedi na świecie ale nie sprawia to że nie jestem przyjazny"
            luszcz "Btw, ogląda pani star wars? czasem?"

            gotka "Jak byłam mała, trochę"
            gotka "Jeden ziom był zakochany w swojej siostrze czy coś?"

            luszcz "Noo coś takiego"
            luszcz "Ale ona w nim też "
            luszcz "A jak wiedzieli że są rodzeństwem to już nie"

            gotka "Twój kolega nie odzyska ręki"

            eminem "huh?!!?"

            gotka "Przynajmniej tutaj. Z takim czymś musicie się wybrać do Krakowa."

            eminem "Wolę umrzeć niż iść do Krakowa!"

            gotka "to Warszawka albo coś"

            eminem "kocham Warszawkę!"

            luszcz "Ja też kocham Warszawkę!"

            eminem "To się tam wybiorę za jakiś czas"

            gotka "Dobrze (kocham zwalać problemy na innych)"
            gotka "Dbajcie o siebie"

            luszcz "Ty też o siebie dbaj"

            eminem "dowidzenia"

            luszcz "(dzięki shadow)"

            eminem "(spoko)"

            if gotka_social_link == 1:
                hide gotka 
                hide eminem 
                show luszcz neutral right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump parking

        label gotka5:
            scene bg klinika2
            if tarczownik_sojusznik >= 1:
                show luszcz neutral right at center
                show tarczownik neutral at right
                show gotka neutral at left
                gotka "...czyli ten pan uderzył cię krawędzią tarczy w kostkę?"

                tarczownik "Sory bracie to było dla twojego dobra"

                luszcz "Tak... ała..."
                luszcz "ała si mi się tu zrobiło.."
                luszcz "Jakby ktoś mógł podmuchać moje ała si..."

                tarczownik "Jeju mogłeś tak od razu"

                "{i}*fiu fiu*{/i}"

                tarczownik "Czy czujesz się lepiej?"

                luszcz "Tak. Dzięki."
                luszcz "A w zasadzie to nie"
                luszcz "Jakby ktoś mógłby dać mi jeszcze kochające buzi w kolanko..."

                tarczownik "Bracie, czego ja dla ciebie nie zrobię"

                "{i}*cmok*{/i}"

                tarczownik "I co jak ci teraz"

                luszcz "Lepiej.."
                luszcz "Dzięki Tarczownik"
                luszcz "Za pomoc"

                tarczownik "Nie ma problemu"

                gotka "to ja widzę że z tym sobie radzicie beze mnie"
                gotka "I chwała bogu"
                gotka "Jak wszystko już okej to dowidzenia"

                tarczownik "Dowidzenia proszę pani"

                luszcz "Dowiedzenia.."
            
            else:
                luszcz "Widzi pani, jakiś głópi cwel walnął mnie bokiem tarczy w kostkę."

                gotka "Boże nienawidze"
                gotka "Jak byłam mała i jeździłam na hulajnodze to jak sie przypadkiem walnęło bokiem to tak boli"

                luszcz "Tak... ała..."
                luszcz "ała si mi się tu zrobiło.."
                luszcz "Jakby ktoś mugł podmuchać moje ała si..."

                gotka "Nie mam uprawnień do dmuchania twojego ała si."

                luszcz "To przynajmniej buzi w kolanko..?"

                gotka "Co ty sobie myślisz młody człowieku"
                gotka "Takie rzeczy robi rodzic dziecku a nie doktor pacjentowi"

                luszcz "Dobrze dobże"
                luszcz "To co mogę zrobić rzeby mniej bolało?"

                gotka "Nic nie da się na to porawdzić"
                gotka "Będzie cie bolało do końca życia i chuj"

                luszcz "A okej"
                luszcz "Dziękuję za poradę medyczną pani doktór"

                gotka "Do usług"
            
            if gotka_social_link == 1:
                hide gotka 
                hide tarczownik
                show luszcz neutral right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump parking

        
        label gotka6:
            scene bg klinika2 with fade
            play music "audio/music/klinika.mp3"
            $ gotka_social_link += 1
            show luszcz neutral right at right
            show gotka neutral at left
            if luszcz_nic == 2:
                $ luszcz_nic = 1
            if luszcz_klata == 2:
                $ luszcz_klata = 1
                $ klata_liczba += 1
            if ring == 2:
                $ ring = 1
            if vr == 2:
                $ vr = 1
            if memy == 2:
                $ memy = 1
            if ziemia == 2:
                $ ziemia = 1
            if zloty == 2:
                $ zloty = 1
            
            $ nogi = 2

            gotka "O, wreszcie się obudziłeś"

            luszcz "Czy... czy jestem... w niebie?"

            gotka "Nie, w gabinecie lekarskim."

            luszcz "To czemu widzę anioła?"

            gotka "Może masz schizofrenię, nie wiem"
            gotka "Znaleziono cię trochę dalej od mleczarni, wygląda na to że spadłeś z klifu"
            gotka "Procedura lekarska wymagała żebyśmy założyli specjalne sprężyny na twoje nogi..."
            gotka "Jednak wygląda na to że twoje nogi same bardzo szybko wróciły do zdrowia."
            gotka "Możesz jednak profilktycznie nosić te sprężyny. Ułatwiają chodzenie."

            luszcz "Dzięki mamo"
            luszcz "znaczy się"
            luszcz "mamo"
            luszcz "znaczy się"
            luszcz "proszę pani"

            gotka "... taka moja robota"

            if gotka_social_link == 1:
                hide gotka 
                show luszcz neutral  right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."
            
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump parking





                            

