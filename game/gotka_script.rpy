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
                scene bg klinika3 with fade
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                hide gotka 
                hide eminem 
                show luszcz neutral right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."
            
            if gotka_social_link == 4:
                scene bg klinika with fade

                gotka "Ej czekaj!"

                luszcz "(oo hel je hel je)"

                gotka "Cały czas Chodzisz tu  z jakimiś losowymi sprawami, niektóre cię nawet nie dotyczą!"
                gotka "Czy ty coś próbujesz szpącić?!"

                menu:
                    "{b}Szpont{/b}":
                        luszcz "Erm tak robię ci szpont"
                        luszcz "Zawsze mażyłem o takiej gotce jak ty"

                        gotka "Dziecko drogie fajnie się bawisz ale nie będę się hajtać z dzieckiem"
                        gotka "Nie mogę cię przyjmować o najmniejsze pierdoły bo mnie jeszcze zamkną"

                        luszcz "Alerz gotko"
                        luszcz "Ja jestem duży chłopak pełnoletni"

                        gotka "To zmienia postać rzeszy"
                        gotka "Btw przestań do mnie mówić gotko mam imię"

                        luszcz "Gotko, jak masz na imię?"

                        gotka "Takemi"

                        luszcz "“Takemi”"
                        luszcz "W takim razie “Takemi”"
                        luszcz "Czy zostaniesz moją gotką?"

                        gotka "Niech się zastanowię…"
                        gotka "…"
                        gotka "Tylko jeśli zgodzisz się na powyższe:"
                        gotka "1) Nazywam cię moją świnką morską."
                        gotka "2) Sesje peggowania we wtorki wieczór"
                        gotka "3) Kastracja"
                        gotka "4) Zwracasz się do mnie per “Alfa wilk” lub “Gigasigma”"
                        gotka "5) Zakaz patrzenia się innym kobietom w oczy"
                        gotka "6) Szczekasz na inne kobiety"
                        gotka "7) Zakaz śmiania się z żartów 67"
                        gotka "8) Obowiązkowo przechodzisz ze mną wszystkie yaoi visual novelki które chcę"
                        gotka "9) Jak mnie zdradzisz mogę zrobić z twoim ciałem cokolwiek co sobie zażyczę."
                        gotka "10) Przestajesz myśleć o męskich siurach"

                        luszcz "(cholera…)"

                        gotka "Zgadzasz się na te warunki?"

                        menu:
                            "{b}Tak alfa wilku{/b}":
                                luszcz "Zgadzam się Alfa Wilku"

                                gotka "Słusznie świnko morska"
                                gotka "W takim razie chodź na buzi"

                                luszcz "Tak jest Gigasigmo"

                                scene bg klinika5
                                play sound "audio/sfx/kiss.mp3"

                                $ renpy.pause(33.0)

                                scene bg klinika

                                luszcz "(jupi mam dziewczyne gotke thats crazy)"

                                gotka "Na razie Alfa Wilk ma ręce pełne roboty, ale na pewno znajdzie czas we wtoreczek wieczorkiem <3"
                                gotka "Albo w sumie nie, przyjdź po południu, od razu cię wykastrujemy"
                                gotka "A potem pogramy w jakiś gay seks"

                                luszcz "Dobrze Gigasigmo"

                                gotka "Heh"

                                luszcz "O właśnie a jest sprawa"
                                luszcz "W niedzielę w kościele podpisują papierek przyjmójący Skałę do Krakowa"
                                luszcz "Przyszłabyś pomóc to ogarnąć? Alfa Wilku?"

                                gotka "Tylko jak ładnie poproszisz"

                                luszcz "Miał miał miał proszęęę miał"

                                gotka "Dobrze, pewnie że cię wesprę w twoich zabawach świnko morsko"
                                gotka "A teraz papatki"
                                gotka "Jesteś wolny"

                                luszcz "Dziękuję Gigasigmo!!! Papatki!"
                                
                                scene bg klinika4

                                gotka "Ah… wreszcie mam na kim wykorzystać mojego 5m potwora.."

                                scene bg klinika3 with fade
                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                show luszcz neutral at center

                                luszcz "Całe szczęście że nie żyjemy w 1984"
                                luszcz "Mogę popełniać myślozbrodnię i łamać 10 punkt ile mi się podoba"

                                jump parking

                            
                            "{b}Nie no aż tyle to nie{/b}":
                                luszcz "Nie no, aż tyle to nie"

                                gotka "To nie zostanę twoją gotką"

                                luszcz "A… gdyby odjąć ten ostatni punkt?"

                                gotka "Nie ja znam swoje potrzeby i wymagania i niczego nie zmieniam"

                                luszcz "Ok ja też znam swoje potrzeby i wymagania"
                                luszcz "I bez tego ani rósz"
                                luszcz "W takim razie pozdrawiam cię Takemi"
                                luszcz "Obyś znalazła sobie lojalną świnkę doświadczalną"

                                gotka "Obyś znalazł sobie wielkiego męskiego kutasa"

                                luszcz "Oj znajdę znajdę"

                                scene bg klinika4

                                gotka "(Ah.. gdyby tylko wiedział że 5m potwór o którym marzy stał tuż przed nim…)"

                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                jump parking

                                        
                    "{b}Bez szpontu{/b}":
                        luszcz "Ja nic nie szponce"
                        luszcz "Ja tylko wspieram lokalny biznes i pomagam lódziom w potrzebie"

                        gotka "To bardzo miłe z twojej strony"
                        gotka "(W takim razie mój 5m potwór będzie musiał poczekać na inną ofiarę…)"
                        gotka "To miłego dnia życzę"

                        luszcz "Miłego"

                        scene bg klinika3 with fade
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        show luszcz neutral at center
                        
                        luszcz "Ah… farewell gotko"
                        luszcz "farewell.."

                        jump parking

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
                scene bg klinika3 with fade
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                hide gotka 
                hide tarczownik
                show luszcz neutral right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."
            
            if gotka_social_link == 4:
                scene bg klinika with fade

                gotka "Ej czekaj!"

                luszcz "(oo hel je hel je)"

                gotka "Cały czas Chodzisz tu  z jakimiś losowymi sprawami, niektóre cię nawet nie dotyczą!"
                gotka "Czy ty coś próbujesz szpącić?!"

                menu:
                    "{b}Szpont{/b}":
                        luszcz "Erm tak robię ci szpont"
                        luszcz "Zawsze mażyłem o takiej gotce jak ty"

                        gotka "Dziecko drogie fajnie się bawisz ale nie będę się hajtać z dzieckiem"
                        gotka "Nie mogę cię przyjmować o najmniejsze pierdoły bo mnie jeszcze zamkną"

                        luszcz "Alerz gotko"
                        luszcz "Ja jestem duży chłopak pełnoletni"

                        gotka "To zmienia postać rzeszy"
                        gotka "Btw przestań do mnie mówić gotko mam imię"

                        luszcz "Gotko, jak masz na imię?"

                        gotka "Takemi"

                        luszcz "“Takemi”"
                        luszcz "W takim razie “Takemi”"
                        luszcz "Czy zostaniesz moją gotką?"

                        gotka "Niech się zastanowię…"
                        gotka "…"
                        gotka "Tylko jeśli zgodzisz się na powyższe:"
                        gotka "1) Nazywam cię moją świnką morską."
                        gotka "2) Sesje peggowania we wtorki wieczór"
                        gotka "3) Kastracja"
                        gotka "4) Zwracasz się do mnie per “Alfa wilk” lub “Gigasigma”"
                        gotka "5) Zakaz patrzenia się innym kobietom w oczy"
                        gotka "6) Szczekasz na inne kobiety"
                        gotka "7) Zakaz śmiania się z żartów 67"
                        gotka "8) Obowiązkowo przechodzisz ze mną wszystkie yaoi visual novelki które chcę"
                        gotka "9) Jak mnie zdradzisz mogę zrobić z twoim ciałem cokolwiek co sobie zażyczę."
                        gotka "10) Przestajesz myśleć o męskich siurach"

                        luszcz "(cholera…)"

                        gotka "Zgadzasz się na te warunki?"

                        menu:
                            "{b}Tak alfa wilku{/b}":
                                luszcz "Zgadzam się Alfa Wilku"

                                gotka "Słusznie świnko morska"
                                gotka "W takim razie chodź na buzi"

                                luszcz "Tak jest Gigasigmo"

                                scene bg klinika5
                                play sound "audio/sfx/kiss.mp3"

                                $ renpy.pause(33.0)

                                scene bg klinika

                                luszcz "(jupi mam dziewczyne gotke thats crazy)"

                                gotka "Na razie Alfa Wilk ma ręce pełne roboty, ale na pewno znajdzie czas we wtoreczek wieczorkiem <3"
                                gotka "Albo w sumie nie, przyjdź po południu, od razu cię wykastrujemy"
                                gotka "A potem pogramy w jakiś gay seks"

                                luszcz "Dobrze Gigasigmo"

                                gotka "Heh"

                                luszcz "O właśnie a jest sprawa"
                                luszcz "W niedzielę w kościele podpisują papierek przyjmójący Skałę do Krakowa"
                                luszcz "Przyszłabyś pomóc to ogarnąć? Alfa Wilku?"

                                gotka "Tylko jak ładnie poproszisz"

                                luszcz "Miał miał miał proszęęę miał"

                                gotka "Dobrze, pewnie że cię wesprę w twoich zabawach świnko morsko"
                                gotka "A teraz papatki"
                                gotka "Jesteś wolny"

                                luszcz "Dziękuję Gigasigmo!!! Papatki!"
                                
                                scene bg klinika4

                                gotka "Ah… wreszcie mam na kim wykorzystać mojego 5m potwora.."

                                scene bg klinika3 with fade
                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                show luszcz neutral at center

                                luszcz "Całe szczęście że nie żyjemy w 1984"
                                luszcz "Mogę popełniać myślozbrodnię i łamać 10 punkt ile mi się podoba"

                                jump parking

                            
                            "{b}Nie no aż tyle to nie{/b}":
                                luszcz "Nie no, aż tyle to nie"

                                gotka "To nie zostanę twoją gotką"

                                luszcz "A… gdyby odjąć ten ostatni punkt?"

                                gotka "Nie ja znam swoje potrzeby i wymagania i niczego nie zmieniam"

                                luszcz "Ok ja też znam swoje potrzeby i wymagania"
                                luszcz "I bez tego ani rósz"
                                luszcz "W takim razie pozdrawiam cię Takemi"
                                luszcz "Obyś znalazła sobie lojalną świnkę doświadczalną"

                                gotka "Obyś znalazł sobie wielkiego męskiego kutasa"

                                luszcz "Oj znajdę znajdę"

                                scene bg klinika4

                                gotka "(Ah.. gdyby tylko wiedział że 5m potwór o którym marzy stał tuż przed nim…)"

                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                jump parking
                                        
                    "{b}Bez szpontu{/b}":
                        luszcz "Ja nic nie szponce"
                        luszcz "Ja tylko wspieram lokalny biznes i pomagam lódziom w potrzebie"

                        gotka "To bardzo miłe z twojej strony"
                        gotka "(W takim razie mój 5m potwór będzie musiał poczekać na inną ofiarę…)"
                        gotka "To miłego dnia życzę"

                        luszcz "Miłego"

                        scene bg klinika3 with fade
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        show luszcz neutral at center
                        
                        luszcz "Ah… farewell gotko"
                        luszcz "farewell.."

                        jump parking
            
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
                scene bg klinika3 with fade
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                hide gotka 
                show luszcz neutral  right at center
                luszcz "Sposób w jaki patrzyła mi w oczy..."
                luszcz "lbo do gardła..."
                luszcz "Potrzebuję gotki lekarza dziewczyny"
                luszcz "Ona mnie naprawi"
                luszcz "Muszę ogarnąć sobie jak najwięcej powodów żeby spędzać z nią czas!!!"
                luszcz "Nie będzie mogła się oprzeć mojej nieustępliwości i hot wilkołak osobowości."
            
            if gotka_social_link == 4:
                scene bg klinika with fade

                gotka "Ej czekaj!"

                luszcz "(oo hel je hel je)"

                gotka "Cały czas Chodzisz tu  z jakimiś losowymi sprawami, niektóre cię nawet nie dotyczą!"
                gotka "Czy ty coś próbujesz szpącić?!"

                menu:
                    "{b}Szpont{/b}":
                        luszcz "Erm tak robię ci szpont"
                        luszcz "Zawsze mażyłem o takiej gotce jak ty"

                        gotka "Dziecko drogie fajnie się bawisz ale nie będę się hajtać z dzieckiem"
                        gotka "Nie mogę cię przyjmować o najmniejsze pierdoły bo mnie jeszcze zamkną"

                        luszcz "Alerz gotko"
                        luszcz "Ja jestem duży chłopak pełnoletni"

                        gotka "To zmienia postać rzeszy"
                        gotka "Btw przestań do mnie mówić gotko mam imię"

                        luszcz "Gotko, jak masz na imię?"

                        gotka "Takemi"

                        luszcz "“Takemi”"
                        luszcz "W takim razie “Takemi”"
                        luszcz "Czy zostaniesz moją gotką?"

                        gotka "Niech się zastanowię…"
                        gotka "…"
                        gotka "Tylko jeśli zgodzisz się na powyższe:"
                        gotka "1) Nazywam cię moją świnką morską."
                        gotka "2) Sesje peggowania we wtorki wieczór"
                        gotka "3) Kastracja"
                        gotka "4) Zwracasz się do mnie per “Alfa wilk” lub “Gigasigma”"
                        gotka "5) Zakaz patrzenia się innym kobietom w oczy"
                        gotka "6) Szczekasz na inne kobiety"
                        gotka "7) Zakaz śmiania się z żartów 67"
                        gotka "8) Obowiązkowo przechodzisz ze mną wszystkie yaoi visual novelki które chcę"
                        gotka "9) Jak mnie zdradzisz mogę zrobić z twoim ciałem cokolwiek co sobie zażyczę."
                        gotka "10) Przestajesz myśleć o męskich siurach"

                        luszcz "(cholera…)"

                        gotka "Zgadzasz się na te warunki?"

                        menu:
                            "{b}Tak alfa wilku{/b}":
                                luszcz "Zgadzam się Alfa Wilku"

                                gotka "Słusznie świnko morska"
                                gotka "W takim razie chodź na buzi"

                                luszcz "Tak jest Gigasigmo"

                                scene bg klinika5
                                play sound "audio/sfx/kiss.mp3"

                                $ renpy.pause(33.0)

                                scene bg klinika

                                luszcz "(jupi mam dziewczyne gotke thats crazy)"

                                gotka "Na razie Alfa Wilk ma ręce pełne roboty, ale na pewno znajdzie czas we wtoreczek wieczorkiem <3"
                                gotka "Albo w sumie nie, przyjdź po południu, od razu cię wykastrujemy"
                                gotka "A potem pogramy w jakiś gay seks"

                                luszcz "Dobrze Gigasigmo"

                                gotka "Heh"

                                luszcz "O właśnie a jest sprawa"
                                luszcz "W niedzielę w kościele podpisują papierek przyjmójący Skałę do Krakowa"
                                luszcz "Przyszłabyś pomóc to ogarnąć? Alfa Wilku?"

                                gotka "Tylko jak ładnie poproszisz"

                                luszcz "Miał miał miał proszęęę miał"

                                gotka "Dobrze, pewnie że cię wesprę w twoich zabawach świnko morsko"
                                gotka "A teraz papatki"
                                gotka "Jesteś wolny"

                                luszcz "Dziękuję Gigasigmo!!! Papatki!"
                                
                                scene bg klinika4

                                gotka "Ah… wreszcie mam na kim wykorzystać mojego 5m potwora.."

                                scene bg klinika3 with fade
                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                show luszcz neutral at center

                                luszcz "Całe szczęście że nie żyjemy w 1984"
                                luszcz "Mogę popełniać myślozbrodnię i łamać 10 punkt ile mi się podoba"

                                jump parking

                            
                            "{b}Nie no aż tyle to nie{/b}":
                                luszcz "Nie no, aż tyle to nie"

                                gotka "To nie zostanę twoją gotką"

                                luszcz "A… gdyby odjąć ten ostatni punkt?"

                                gotka "Nie ja znam swoje potrzeby i wymagania i niczego nie zmieniam"

                                luszcz "Ok ja też znam swoje potrzeby i wymagania"
                                luszcz "I bez tego ani rósz"
                                luszcz "W takim razie pozdrawiam cię Takemi"
                                luszcz "Obyś znalazła sobie lojalną świnkę doświadczalną"

                                gotka "Obyś znalazł sobie wielkiego męskiego kutasa"

                                luszcz "Oj znajdę znajdę"

                                scene bg klinika4

                                gotka "(Ah.. gdyby tylko wiedział że 5m potwór o którym marzy stał tuż przed nim…)"

                                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                                    play music "audio/music/pole.mp3"
                                else:
                                    play music "audio/music/pole_noc.mp3"
                                jump parking

                                        
                    "{b}Bez szpontu{/b}":
                        luszcz "Ja nic nie szponce"
                        luszcz "Ja tylko wspieram lokalny biznes i pomagam lódziom w potrzebie"

                        gotka "To bardzo miłe z twojej strony"
                        gotka "(W takim razie mój 5m potwór będzie musiał poczekać na inną ofiarę…)"
                        gotka "To miłego dnia życzę"

                        luszcz "Miłego"

                        scene bg klinika3 with fade
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        show luszcz neutral at center
                        
                        luszcz "Ah… farewell gotko"
                        luszcz "farewell.."

                        jump parking
            
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump parking

        label gotka7:
            play sound "audio/sfx/traveling.mp3"
            scene bg klinika2 with fade
            play music "audio/music/klinika.mp3"
            show luszcz neutral right at right
            show kazuma strzal at center
            show gotka neutral at left

            kazuma "Ałaaaa ale boli ała ała krewka"

            luszcz "Pani gotko znaczy pani doktór pani musi mu pomóc!"

            gotka "No dobrze dobrze zobaczę co można zrobić"

            hide gotka neutral
            show kazuma strzal right

            kazuma "Po co na niego skończyłeś głupi clankerze"

            luszcz "No myślałem że mamy plot armor!!"

            kazuma "Gówno nie plot armor!! Jeśli się przez ciebie wykrwawię to cię zabiję w simsach!!"

            show gotka neutral at left

            gotka "Ej panowie bez takich"

            show kazuma strzal

            kazuma "Ale to on zaczął"

            gotka "Nieważne kto zaczął! Znalazłam domowy sposób na zatamowanie dziury!!"

            show gotka neutral at slightleft
            show kazuma lody 
            with vpunch

            $ renpy.pause(0.5)

            show gotka neutral at left

            gotka "A ty do końca po-jutra masz mi znaleźć księgę czarnej magii albo cię wykastruje!"

            









                            

