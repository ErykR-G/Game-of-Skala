default monopoleks = 0
default napojko = 0
default tasma_romans = 0

label silver_sextape:
    label silver_sextape1:
        scene bg alejka
        show luszcz neutral at center 
        show tasma neutral at right
        ""
        tasma "przepraszam…"
        tasma "Ekhem Dzień dobry!"
        tasma "Przepraszam, czy jest pan jakkolwiek zainteresowany usługami seksualnymi?"

        menu:
            "{b}Tak{/b}":
                luszcz "Tak, lóbię sobie czasem zapłacić za dobry seks."

                tasma "A gdybym to ja panu płaciła?"

                luszcz "To spadła mi pani z nieba!"
            
            "{b}Nie{/b}":
                luszcz "Nie, mam lepsze rzeczy do roboty."

                tasma "O-okej, to teraz pytanie z innej beczki:"
                tasma "Czy zależy panu na prezerwacji zagrożonych gatunków?"
                tasma "Na przykład... gdyby mógł pan powstrzymać dinozaury przed wyginięciem, zrobiłby pan to?"

                show luszcz dinozaur

                luszcz "damn, skąd ona wiedziała że kocham dinozaury?"

                menu:
                    "{b}Zależy mi na prezerwacji{/b}":
                        show luszcz neutral
                        luszcz "Tó mnie pani ma, i ten przykład z dinozaurami, skąd pani wiedziała rze je kocham?"
                        tasma "Wyczytałam panu z oczu."
                    
                    "{b}Nie zależy mi{/b}":
                        show luszcz neutral
                        luszcz "Nie, nie jest to mój interes."
                        luszcz "A dinożaury wyginęły dawno zanim mieliśmy o tym cokolwiek do powiedzenia."
                        luszcz "Dowidzenia."

                        tasma "Proszę poczekać!"
                        tasma "Ostatnie pytanko…"
                        tasma "Czy gdybym pani zapłaciła... w miarę srogo... powiedzmy 3 💰?"

                        tasma "Czy pan byłby zainteresowany wysluchaniem mojej oferty?"
                        luszcz "To jest, istotnie, dużo pieniędzy..."
        
                        menu:
                            "{b}Tak{/b}":
                                luszcz "Dobrze, dla pieniędzy zrobię bardzo dużo."
                            
                            "{b}Nie{/b}":
                                luszcz "Ale mnie to w ogóle nie interesuje."
                                luszcz  ""
        
        tasma "Cóż, cudownie!"
        tasma "Ale… trochę wstyd o tym rozmawiać tak na otwartym powietrzu, utrzymajmy trochę kultury."
        tasma "Byłby pan w stanie zobaczyć się ze mną w barze seniora?"

        luszcz "Myślę że tak."

        tasma "Okej, to jesteśmy umówieni."
        tasma "A jak ma pan na imię?"

        luszcz "Moje imie…?"
        luszcz "Maciej."
        luszcz "Maciej Łuszcz."

        tasma "W takim razie do zobaczenia, Macieju."

        $ silver_sextape_social_link = 1
        $ silver_sextape_wybory = 0

        play music "audio/music/pole.mp3"

        jump sklep_monopolowy
    
    label silver_sextape2:
        play music "audio/music/klub.mp3"
        scene bg klub with fade
        show luszcz neutral at left
        luszcz "Dobra, jestem."
        luszcz "Powinna gdzieś tu być…"
        luszcz "O, macha mi."
        
        show luszcz neutral at center
        show tasma neutral at right

        tasma "Dzień dobry Macieju! Dziękuję że przyszedłeś."
        tasma "Pijesz coś?"
        menu:
            "{b}Jabola Full{/b}":
                $ napojko = 1
                luszcz "Poproszę Jabole Full"

            "{b}Jabola Mega{/b}":
                $ napojko = 1
                luszcz "Poproszę Jabole Mega"

            "{b}Jabola Max{/b}":
                $ napojko = 1
                luszcz "Poproszę Jabole Max"

            "{b}Royal Cola{/b}":
                $ napojko = 2
                luszcz "Poproszę Royal Colę"
            
            "{b}Dr Pepper{/b}":
                $ napojko = 3
                luszcz "Poproszę napój naukowców"

        tasma "Dobrze, pójdę zamówić."
        hide tasma
        luszcz "(hmm... nie powinienem za siebie zapłacić?)"
        $ config.menu_include_disabled = True
        menu:
            "{b}Zapłać za obu (1 💰){/b}" if money >= 1:
                $ config.menu_include_disabled = False
                luszcz "Dobra, postawie portfele po jej stronie."

                $ money -= 1

                show tasma neutral at right

                tasma "Hejka wróciłam"

                if napojko == 1:
                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 1
                    "{i}*Jabola została dodana do ekwipunku*{/i}"
                else:
                    if napojko == 2:
                        if royal == 0:
                            $ ile_item += 1
                        $ royal += 1
                        "{i}*Royal Cola została dodana do ekwipunku*{/i}"
                    else:
                        if napojko == 3:
                            if drpepper == 0:
                                $ ile_item += 1
                            $ drpepper += 1
                            "{i}*Dr Pepper został dodany do ekwipunku*{/i}"


                show tasma blush
                tasma "Oh..? To płacisz za nas obu...?"

                show luszcz sigma

                luszcz "Tak"

                show tasma neutral

                tasma "To bardzo miłe, tak nie trzeba, my tu tylko biznes Macieju…"

                luszcz "Nie ma problemu."
                show luszcz neutral
            
            "{b}Zapłać za siebie (1 💰){/b}" if money >= 1:
                $ config.menu_include_disabled = False
                luszcz "Dobra, postawie portfele po jej stronie."

                $ money -= 1

                show tasma neutral at right

                tasma "Hejka wróciłam"

                if napojko == 1:
                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 1
                    "{i}*Jabola została dodana do ekwipunku*{/i}"
                else:
                    if napojko == 2:
                        if royal == 0:
                            $ ile_item += 1
                        $ royal += 1
                        "{i}*Royal Cola została dodana do ekwipunku*{/i}"
                    else:
                        if napojko == 3:
                            if drpepper == 0:
                                $ ile_item += 1
                            $ drpepper += 1
                            "{i}*Dr Pepper został dodany do ekwipunku*{/i}"
                
                show tasma blush

                tasma "Jejku, płacisz za mnie?"

                show tasma neutral

                tasma "O, znaczy, za siebie."
                
                luszcz "Istotnie, płacę."
            
            "{b}Niet{/b}":
                $ config.menu_include_disabled = False
                luszcz "Nie stać mnie na takie bajerowanie jestem na misji"

                show tasma neutral at right

                tasma "Hejka wróciłam"

                if napojko == 1:
                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 1
                    "{i}*Jabola została dodana do ekwipunku*{/i}"
                else:
                    if napojko == 2:
                        if royal == 0:
                            $ ile_item += 1
                        $ royal += 1
                        "{i}*Royal Cola została dodana do ekwipunku*{/i}"
                    else:
                        if napojko == 3:
                            if drpepper == 0:
                                $ ile_item += 1
                            $ drpepper += 1
                            "{i}*Dr Pepper został dodany do ekwipunku*{/i}"

                tasma "Proszę. To dla ciebie."
                luszcz "Dziękuję bardzo."
            
        luszcz "To jaka jest sprawa?"

        tasma "Więc… może trochę tła"
        tasma "Moja rodzina, w tym daleka, nigdy nie liczyła wielu członków."
        tasma "Mieszkaliśmy dość blisko siebie, w okolicach Krakowa."
        tasma "Nagle przyszła powódź tysiąclecia, zostawiając przy życiu tylko tych z nas, którzy byli wodoodporni,"
        tasma "Jednakże zamiast odbudować gatunek, wszyscy postanowili pokupować sobie psy i koty!!"
        tasma "W sensie, ja też mam psa."
        tasma "Ale znalazłam się w sytuacji, w której jestem ostatnią przedstawicielką swojego gatunku."
        tasma "Jednakże z Twoją pomocą, Macieju!"
        tasma "Moglibyśmy wykonać razem rytuał godowy!"
        tasma "I dać nasienie nadziei!"
        tasma "Życia, oraz przyszłości."
        tasma "Czy pomógłbyś mi wydłużyć moją rodzinę o jeszcze jednego członka, Macieju?"

        luszcz "Haha, wow, haha"
        luszcz "Um, jakby…"

        menu:
            "{b}Dla ciebie wszystko{/b}":
                $ tasma_romans = 1
                luszcz "Dla ciebie wszystko"

                show tasma blush

                tasma "…"
                tasma "Macieju……"
                tasma "a nie miałam tego na myśli w taki sposób… ale…"
                tasma "Jeśli tak mówisz…"

                show tasma neutral
            
            "{b}Jestem w stanie to zrobić.{/b}":
                luszcz "Jestem w stanie to zrobić."

                tasma "Dziękuję ci."
                tasma "Nawet nie wiesz ile to dla mnie znaczy."
                tasma "O-oczywiście, zapłacę ci za to. I nie ponosisz żadnej odpowiedzialności za dziecko."
            
            "{b} Może jednak lepiej nie{/b}":
                luszcz "Może jednak lepiej nie."

                tasma "A było tak blisko…"
                tasma "Dobrze, respektuję twoją decyzję."
                tasma "Idę powoli umierać oglądając anime i zapijając smutki."

                luszcz "Serwus."
                play music "audio/music/pole.mp3"

                $ silver_sextape_social_link = 10
                $ silver_sextape_wybory = 0

                jump sloneczna

        tasma "Aby wykonać akt, spotkajmy się w moim domu, niedaleko monopolowego."
        tasma "Przyjdź nocą."
        tasma "Jeszcze raz dziękuję."

        tasma "Przyjemność po mojej stronie."

        $ silver_sextape_social_link = 2
        $ silver_sextape_wybory = 1

        play music "audio/music/pole.mp3"
        jump sloneczna

    label silver_sextape3:
        play music "audio/music/redsun.mp3"
        scene bg dom_tasma with fade
        show luszcz neutral at left
        show tasma neutral at center

        tasma "Dobry wieczór"
        tasma "Zapraszam do środka"
        scene bg dom_tasma2
        show luszcz neutral at slightright
        show tasma neutral at slightleft

        luszcz "Dobry wieczur"
        luszcz "To będzie tutaj…? Bardzo ładny pokój."

        tasma "Tak, wszystko gotowe"
        tasma "Chciałbyś wziąć jeszcze przed prysznic?"

        luszcz "Nie, ja się ogółem nie myje."

        tasma "W takim razie nie przedłużajmy."

        scene bg dom_tasma3
        show luszcz neutral right at slightright
        show tasma neutral at slightleft

        luszcz "Chwila, to będzie kamerowane?"

        tasma "Oh… nienie, znaczy, tak, ale to ważne do rytuału."
        tasma "Mam nadzieję że to dla ciebie okej? Nikt tego nie zobaczy. Obiecuję."

        luszcz "Hm. Dobra, niech się dzieje wola nieba."

        tasma "Dziękuję Macieju."
        tasma "Dobrze. Pozwól, że przyciemnię światło…"

        scene bg black with fade
        "{i}S S S S S S S S S S S::{/i}"
        tasma "Hm.. Jakby tu zacząć.."

        luszcz "Ej nie wiem czy to się przyda, ale pżyniosłem autko Marka Maruche i model ronda grzegórzeckiego."

        tasma "Oh!!! Uwielbiam te zabawki to moje ulubione zabawki!!!"
        tasma "Pobawmy się nimi!"

        luszcz "Dobra to ty masz rondo a ja autko"

        menu:
            "{b}Powoli wjedź na rondo{/b}":
                tasma "Oh Macieju! Cóż za wjazd!"
            
            "{b}Postaw maruchę na północnej krawędzi{/b}":
                tasma "awghh… Macieju…"
                tasma "Tak od razu…"
            
            "{b}Posmyraj białe linie na drodze{/b}":
                tasma "Oh..! Oh, Macieju!"
        
        "{i}*Łuszczu powoli robi kółka po rondzie*{/i}"
        luszcz "Ziuuu…."

        tasma "Tak… tak…."
        tasma "Jeszcze, proszę, szybciej! Pokaż jak szybko jeździsz!"

        luszcz "Ziuuuuuum ziuuuuum"

        tasma "Oh! Proszę! Tak! Proszę! Daj mi tego więcej!"

        menu:
            "{b}Zrób skok nad środkiem ronda{/b}":
                tasma "Ah! Dziękuję! Skacz! Skacz! Skacz!"
            
            "{b}Gwałtownie zmień kierunek jazdy{/b}":
                tasma "AHh0- Dziękuję! dziękuję! Co za zawrot!"
            
            "{b}Walnij drifta (ostrożnie!{/b}":
                tasma "Mmh… AHhhhahAHhhh To takie dobrwe!!"
        
        luszcz "(to chyba dobry moment…)"

        menu:
            "{b}Skocz maruchą przez środek ronda{/b}":
                tasma "aghhhh!!!!! AłŁ Ał… oh…"
                tasma "mAcieju… Macieju… koniec,.. Już… tak… wystarczy.."
        
        "{i}S S S S S S S S S S S::{/i}"
        scene bg dom_tasma3
        show luszcz neutral at slightright
        show tasma neutral at right

        tasma "Macieju, to było cudowne!"

        luszcz "haha, bez przesady, hehe"

        tasma "Nie, serio. Nie spodziewałam się że to będzie takie przyjemne."

        luszcz "Ty… również.. Byłaś świetna."

        tasma "hihihiha"
        tasma "Ojej, ależ przecież!"

        show luszcz neutral at slightleft
        show tasma neutral at slightright

        tasma "Oto twoja zapłata. Jestem ci nieskończenie wdzięczna."

        $ money += 3
        "{i}*do ekwipunku zostały dodane 3 portfele*{/i}"

        tasma "Dziękuję ci za usługę zarówno jak i za przeżycie, Macieju."

        luszcz "Potwór czy nie potwór, ważne że ma otwór."
        luszcz "Dobrze, to ja się będę powoli zbierał"

        play sound "audio/sfx/baby.mp3"

        nikt "ŁEEEEEEEE.."
        nikt "WA   WA    WA WAAAAAh…"

        tasma "Ojej!! Tak szybko?!"
        tasma "yay!"

        luszcz "??? huh???"

        show luszcz neutral right at slightright
        show tasma neutral at slightleft

        "{i}*Taśma otwiera kamerę i wyjmuje sextape, trzyma je w dloniach*{/i}"

        show tasma tasma at slightleft

        tasma "Spójrz! Nagrała się!"
        tasma "Czy nie jest piękna?"

        luszcz "tak oczywiście"
        luszcz "przepiękna"

        tasma "Ale się cieszę, Macieju, mam córkę!"

        luszcz "Wyśmienicie"
        luszcz "To ja już wyjdę"

        tasma "Dziękuję! Dobrej nocy!"

        luszcz "Tak, nawzajem."

        $ silver_sextape_social_link = 3
        $ silver_sextape_wybory = 2
        $ tasma_spotkanko = 2

        play music "audio/music/pole.mp3"
        jump alejka
    
    label silver_sextape4:
        show luszcz neutral at slightleft
        show tasma tasma at slightright

        if tasma_romans == 1:
            tasma "Oh, Macieju! Tutaj!!"

            luszcz "(ojć…)"
            luszcz "Dzień dobry, jak się pani ma"
            luszcz "Oraz… nasza… curka?"

            tasma "Dobrze. Złotko, przywitaj się z tausiem!"

            sex "{{tekst przywitaniowy}"

            tasma "Pamięta cię :)"

            luszcz "Jak miło"

            tasma "Jestem ci taka wdzięczna… dzieci to cudna sprawa"
            tasma "Ale po tym co mówiłeś myślałam, że jesteś nam trochę bardziej dedykowany?"

            luszcz "Nie wiem o czym mówisz. Miałem ci pomóc i dostać opłatę."

            tasma "A gdy powiedziałeś mi w restauracji, że zrobisz dla mnie wszystko?"

            luszcz "Powiedziałem tak…? Nie pamiętam."

            tasma "Nie pierdol się ze mną! Bardzo dobrze pamiętam!"

            sex "Oh! Proszę! Tak! Proszę! Daj mi tego więcej!"

            tasma "Piciu? Już ci daję"

            sex "{{tekst dziękujący}"

            tasma "Nie ma za co."
            tasma "I dziś rano jej zeszła pierwsza tasiemka!"
            tasma "A od ciebie ani słowa!"

            luszcz "Nie mam pojęcia co to znaczy."
            
            sex "aghhhh!!!!! AłŁ Ał… oh…"

            tasma "Wiem kochanie, troszkę bolało."
            tasma "Nie zdajesz sobie sprawy jakie to ważne wydarzenie w jej życiu!"
            tasma "Zero prezentu, zero odzewu, zero niszego!"
            tasma "Jesteś najgorszym ojcem! I mężem!"

            $ config.menu_include_disabled = True
            menu:
                "{b}Mam prezent{/b}" if kartka == 1:
                    $ config.menu_include_disabled = False
                    luszcz "Ale wiesz… tak na prawdę to mam dla niej prezent."
                    luszcz "Po prostu… nie było was w domu, więc przyszedłem tótaj."
                    luszcz "Widzisz?"

                    $ kartka = 0
                    "{i}Łuszcz wyjmuje kartkę urodzinową i daje ja taśmie{/i}"

                    tasma "(((cytowanie życzeń…)))"
                    tasma "(((cytowanie życzeń…)))"
                    tasma "Ale to w ogóle nie jest dla niej!"
                    tasma "Ktoś wysłał to tobie! Przecież masz tu napisane debilu!"
                    tasma "Co ty sobie w ogóle myślisz! My nawet nie dożywamy osiemnastu lat!"

                    luszcz "Jezus maria czemu dopiero teraz mi to mówisz"

                    tasma "To się jakoś skaluje deklu"
                    tasma "Jak z latami psimi"

                    luszcz "Niby tak ale pies się nie porównuje do tej sytuacji"

                    tasma "Dobra wiesz co weź stąd spadaj"
                    tasma "Nie chcę cię więcej widzieć na oczy!!"

                    sex "mAcieju… Macieju… koniec,.. Już… tak… wystarczy.."

                    tasma "Nie mów tak, to nie jest twój ojciec."

                    luszcz "eh…."

                    jump sloneczna2
                
                "{b}Idę stąd{/b}":
                    $ config.menu_include_disabled = False
                    luszcz "Wiesz co, bo ja mam sprawy do załatwienia, to może pójdę."

                    tasma "Ależ oczywiście! Bo co to dziecko! Co to samotna matka!"

                    sex "mAcieju… Macieju… koniec,.. Już… tak… wystarczy.."

                    luszcz "eh…"

                    jump sloneczna2

        else:
            tasma "Oh, Macieju! Macieju!! Tutaj!!"

            luszcz "(ojć…)"
            luszcz "Dzień dobry, jak się pani ma"
            luszcz "Oraz… nasza… curka?"

            tasma "Cudownie! Złotko, przywitaj się z ojcem!"

            sex "{{tekst przywitaniowy}"

            tasma "Pamięta cię :)"

            luszcz "Jak miło"

            tasma "Jestem ci taka wdzięczna… dzieci to cudna sprawa"
            tasma "Jak już ustalaliśmy, zajmę się nią sama. Nasz kontrakt jest spełniony."

            luszcz "Fakt."

            tasma "Jednakże, czy to nie urocze…"
            tasma "Ile już słów zna"

            sex "Oh! Proszę! Tak! Proszę! Daj mi tego więcej!"

            tasma "Piciu? Już ci daję"

            sex "{{tekst dziękujący}"

            tasma "Nie ma za co."
            tasma "I dziś rano jej zeszła pierwsza tasiemka!"

            luszcz "Nie mam pojęcia co to znaczy."

            sex "aghhhh!!!!! AłŁ Ał… oh…"

            tasma "Wiem kochanie, troszkę bolało."
            tasma "Taka sprawa biologiczna u młodych u nas"
            tasma "Nieprzyjemne, ale ważne. Znaczy że jest zdrowa!"
            tasma "Ale no, nieważne."

            luszcz "Wiesz co, bo ja mam sprawy do załatwienia, to morze pójdę."

            tasma "Pewnie, miłego dnia!"

            sex "mAcieju… Macieju… koniec,.. Już… tak… wystarczy.."

            luszcz "dowidzenia, powodzenia z młodą."

            hide luszcz
            hide tasma 
            jump sloneczna2
            






