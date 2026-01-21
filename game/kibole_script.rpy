default nie_mam = 0
label kibole:
    label kibole1:
        scene bg czerwony with fade
        show luszcz neutral at center
        luszcz "puk puk"
        nikt "Kto tam?"
        luszcz "Dostawa krówek!"

        show piotrek neutral at slightright
        show luszcz neutral at slightleft

        piotrek "Oooo, dawaj mi to"
        piotrek "Krystian, słuchaj, krówki przyszły!"

        show piotrek neutral at right
        show luszcz neutral at left
        show krystian neutral at center

        krystian "Jezus wreszcie kocham to gówno"
        krystian "Dziękujemy bardzo oto zapłata"

        $ krowka = 0
        $ mleczarz_social_link = 3
        $ money += 2
        "{i}*do ekwipunku zostały dodane 2 portfele*{/i}"

        luszcz "A dziękuję"

        piotrek "Ej a może napiwek damy"

        krystian "Jaki napiwek to nie jest restauracja"

        piotrek "Ale to jest usługa i on nam przynosi rzeczy"
        piotrek "Patrz jak chłop wygląda, ewidentnie jest w potrzebie"

        krystian "W tyłku mam problemy dostawców po to ziomkom płacą żeby mi robili dobrze!"
        krystian "A nie na odwrót!"

        luszcz "ekhem"

        piotrek "Ej, bracie, brzmisz teraz jak potężny red flag."

        krystian "Jakby rozłożyć na niej białe paski to by się wszystko zgadzało"
        krystian "A, właśnie"
        krystian "Kolego, pytanko"
        krystian "Wisła czy Cracovia?"

        piotrek "Cracovia czy Wisła?"

        label kibole_wybory:
            menu:
                "{b}Wisła{/b}":
                    luszcz "Wisła"

                    krystian "Aahhhh tak jest!!"
                    krystian "30 - 29 cieniasie!"

                    piotrek "Dobra nie napawaj się tak"
                    piotrek "Oczywiście że nikt tu nie lubi Cracovi, jeśli nie lubi krakowa"

                    krystian "Sami se wybraliście taką lame-ass nazwę, Wisełka sobie pływa po całej polsce!"

                    piotrek "Dobra nieważne, fajnie, jak chcesz."

                    krystian "Nie no, pamiętasz zakład"
                    krystian "Pierwszy do 30 zbiera cały dom!"

                    piotrek "Nie no bez przesady"

                    krystian "Z!"
                    krystian "Jesteś moim niewolnikiem, albo lądujesz pod mostem!"

                    piotrek "…"
                    piotrek "Wybieram niewolę."

                    krystian "Bardzo dobrze. To co, może ogarnij kuchnię?"
                    krystian "A potem wyprasuj ubrania."
                    krystian "Jak zdążysz to będziesz mógł obejrzeć ze mną mecz masując moje stopy."

                    piotrek "Dobra, ale on nie musi tego słyszeć"

                    krystian "To ja tu decyduję czy musi czy nie."
                    krystian "Do Widzenia, niezmiernie dziękuję."

                    luszcz "Dowidzenia"

                    hide krystian
                    hide piotrek

                    luszcz "Ah te kluby."

                    $ krystian_wybory = 2
                    $ piotrek_wybory = 0

                    play music "audio/music/pole.mp3"
                    jump bohaterow_wrzesnia 
                
                "{b}Cracovia{/b}":
                    luszcz "Cracovia"

                    piotrek "Tak jest!!!"
                    piotrek "Jak ja się martwiłem…"
                    piotrek "30 do 29, wygrałem zakład!"
                    piotrek "Cracovia zawsze wygrywa!"

                    krystian "Pierdole…"
                    krystian "Z tą całą ekspansją to oczywiście, że wszystko wygrywa!"
                    krystian "Przecież za niedługo i Skałe pochłonie!"
                    krystian "Wszystko schodzi na psy…"

                    piotrek "Ja tam się cieszę. Może klub na tym zyska. Nazwy mają znaczenie."
                    piotrek "Ale pozwól że będę bezpośredni."
                    piotrek "Zgodnie z założeniami zakładu, to już nie jest twój dom"

                    krystian "Ale mogę z tobą mieszkać?"

                    piotrek "Nie. potrzebuję miejsca i warunków na wynajem"
                    piotrek "Nie wiem jak odnajdę się finansowo gdy Kraków zajmie się tą okolicą więc od teraz można wynająć sobie ze mną mieszkanie."

                    krystian "Halo a ja co?? Ulica?!"

                    piotrek "Tak kończą przegrani."
                    piotrek "Plus, w po dziurki w nosie mam ciągłego słuchania o twoim obsranym klubie i zajmowaniem się tobą gdy wracasz z ustawek."
                    piotrek "Dowidzenia!"

                    hide piotrek
                    show luszcz neutral at slightleft
                    show krystian neutral at slightright

                    krystian "…"

                    luszcz "Szczerze okropne z jego strony"

                    krystian "Ziomuś, to twoja wina."
                    krystian "Masz wpierdol"

                    jump fight112
                    label after_fight121:
                        luszcz "Nienawidzę piłki nożnej."
                        $ krystian_wybory = 0
                        $ piotrek_wybory = 2

                        play music "audio/music/pole.mp3"
                        jump bohaterow_wrzesnia 
                
                "{b}Piernik{/b}"if piernik == 1:
                    show luszcz piernik at slightleft
                    luszcz "Ej patrzcie jaki mam fajny piernik"

                    piotrek "…"
                    piotrek "Ej Krystian ten piernik jest dowalony"

                    krystian "Jak ty taki piernik zrobiłeś fajny"
                    krystian "Sztama chłopie za taki piernik chłopie…"

                    piotrek "Nic dodać nic ująć."
                    piotrek "A dasz gryza?"

                    luszcz "Nie"

                    piotrek "A to się pierdol"

                    krystian "Rel"

                    hide piotrek
                    show luszcz neutral at center
                    hide krystian 

                    luszcz "Chryste, ale dodge."

                    $ krystian_wybory = 0
                    $ piotrek_wybory = 0

                    play music "audio/music/pole.mp3"
                    jump bohaterow_wrzesnia 
                
                "{b}Biblia{/b}" if biblia == 1 if nie_mam == 0:
                    luszcz "Chłopaki, kochacie Boga?"

                    krystian "Tak"
                    
                    piotrek "Ja też"

                    luszcz "To morze poszukajmy odpowiedzi na wasze pytanie w biblii?"

                    "{i}Łuszcz wyjmuje biblie{/i}"

                    luszcz "Hm…"
                    luszcz "O! Tutaj!"
                    luszcz "“Dwa kluby powinny wziąć się w garść i zrobić sobie mecz o to który jest lepszy”,"

                    "{i}Łuszcz chowa biblie{/i}"

                    luszcz "powiedział jezus nazarejczykom."

                    krystian "Piotrek to jest w biblii."

                    piotrek "Noooo prawda.. Święta prawda.."

                    krystian "Ale jest problem, nie mamy piłki?"
                    krystian "Może weź.. Jak taki cwany jesteś to.."

                    piotrek "Daj nam jakąś piłkę to zagramy mecza."

                    krystian "Tak, dokładnie"

                    menu:
                        "{b}Nie mam{/b}":
                            luszcz "Nie mam piłki..."

                            krystian "To nie ma meczu!"

                            $ nie_mam = 1
                            jump kibole_wybory
                        
                        "{b}Zielona Kula{/b}":
                            luszcz "Macie to coś."

                            $ zielona_kula = 0

                            krystian "Fuj chłopie to jest całe wilgotne"

                            piotrek "Ale wymiarami się zgadza. Niech będzie."
                            piotrek "Ciężkie czasy wymagają ciężkich ludzi."
                            piotrek "Dzięki, to co, widzimy się na boisku pod szkołą?"

                            krystian "W sumie racja, potrzebujemy świadka."

                            luszcz "Może przyjdę, może nie."
                            luszcz "Czas pokaże."
                            luszcz "Żegnam was"

                            kip "Serwus"

                            $ kibole_social_link = 1
                            $ krystian_wybory = 1
                            $ piotrek_wybory = 1

                            play music "audio/music/pole.mp3"
                            jump bohaterow_wrzesnia 
                        
                        "{b}Głowa Nemeczka{/b}":
                            luszcz "Macie to coś."

                            $ glowa = 0
                            piotrek "Czy to nie jest czyjaś głowa?"
                            piotrek "Krystian dzwonimy na policję"

                            krystian "Piotrek czy coś ci się nie pomyliło?"
                            krystian "Śmierć konfidentom!"

                            luszcz "Śmierć konfidentą!"

                            piotrek "Śmierć konfidentom!"
                            piotrek "Racja, sory chłopaki"
                            piotrek "W miarę… działa jak piłka"

                            krystian "Ojoj, bo jeszcze przegrasz"
                            krystian "To co, widzimy się na boisku?"

                            piotrek "No tak, potrzebujemy świadka."

                            luszcz "Może przyjdę, może nie."
                            luszcz "Czas pokaże."
                            luszcz "Żegnam was."

                            kip "Siema"

                            $ kibole_social_link = 1
                            $ krystian_wybory = 1
                            $ piotrek_wybory = 1

                            play music "audio/music/pole.mp3"
                            jump bohaterow_wrzesnia 

    label kibole2:
        scene bg boisko with fade
        show piotrek neutral at right
        show luszcz neutral at left
        show krystian neutral at center

        krystian "Dobrze że jesteś. Właśnie zaczynamy"

        piotrek "Zgadza się!"

        luszcz "Dobra, to ja tu usiądę i będę stąd oglądać"

        krystian "Okej"

        hide piotrek
        hide krystian

        krystian "Dobra, start!"

        "{i}Łuszcz zasypia{/i}"

        scene bg bLACK with fade
        scene bg boisko with fade
        piotrek "Ej, bracie, wstawaj!"

        krystian "Gra się już dawno skończyła a ty tak leżysz i chrapiesz."

        luszcz "Oh, em, haha, sory"
        luszcz "Piłka nożna jest taka kurde interesująca."
        luszcz "Jak mogłem."
        luszcz "To… kto wygrał?"

        piotrek "…"

        krystian "…"

        piotrek "Ej Krystian liczyłeś punkty?"

        krystian "Nie a ty?"

        piotrek "Deklu jak mogłeś zapomnieć…"
        piotrek "Znaczy ja też zapomniałem…"

        krystian "To co, gramy od nowa?"

        piotrek "Heh pewnie!"

        luszcz "Nie, czekajcie!"
        luszcz "Mam jurz werdykt"

        krystian "?"

        piotrek "?"

        luszcz "Bawiliście się tak dobże, że zapomnieliście po co gracie."
        luszcz "W mojej skromnej opinii, kluby ssają pałę"
        luszcz "Prawdziwa frajda w piłce, jest w piłce samej w sobie"
        luszcz "Wygrywa… miłość, panowie."
        luszcz "Miłość do gry."

        krystian "…"

        piotrek "…"

        krystian "Piotr, przelizałbym się z tobą gdybym był gejem"

        piotrek "Miałem powiedzieć dokładnie to samo!"

        krystian "To co, gramy jeszcze meczyk? For fun?"

        piotrek "Tak brachu, for fun."
        
        hide piotrek
        hide krystian

        luszcz "Ah… te piłkarzyki…"
        luszcz "Tak szybko dorastają…"
        luszcz "Dobże rze nie muszę jóż oglądać tych gierek."

        $ kibole_social_link = 2
        $ krystian_wybory = 2
        $ piotrek_wybory = 2

        play music "audio/music/pole.mp3"
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
