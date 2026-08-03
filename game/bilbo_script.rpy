default stupka = 0
default edgar = 0
default sperma = 0
default kaput = 0
default macanko = 0
default balbo = 0
transform jump_left_arc:
    xalign 0.5
    yalign 1.0

    parallel:
        ease 1.2 xalign -1.4

    parallel:
        easeout 0.6 yalign -0.35
        easein 0.6 yalign 1.25


label bilbo:
    label bilbo1:
        play music "audio/music/natura.mp3"
        scene bg przystanek_noc with fade
        show luszcz neutral at center
        luszcz "Ktoś tutaj śpi nie będę mu przeszkadzał."
        luszcz "Chociarz… ma gołe stopy…"
        menu:
            "{i}pogilgaj stupki{/i}":
                luszcz "giligiligiligili"
                nikt "hihihihi przestań przestań… hrrrrrrr… *honk mimimimi*"
                luszcz "hehe"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump sloneczna
            
            "{i}niet{/i}":
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump sloneczna
    
    label bilbo2:
        play music "audio/music/natura.mp3"
        scene bg przystanek with fade
        show luszcz neutral at slightleft
        show bilbo neutral at slightright
        luszcz "Serwus wyglądasz jakbyś czegoś szukał"

        bilbo "Dzień dobry. Istotnie czegoś szukam, i jest to transport."
        bilbo "Ja, na imię mam Bilbo, i mój brat Dilbo próbujemy dostać się do Pustelni Błogosławionej Salmonelli na tun tun tun zachód stąd."
        bilbo "Jednakże nie ma szans że będziemy tam iść całą drogę na nogach. Bo nam się nie chce. I nie chciałbym podrażnić moich wrażliwych stópek."
        bilbo "Więc jakbyś miał nas czym podwieźć to byłoby wyśmienicie."

        luszcz "A co was tam sprowadza"

        bilbo "Wybieramy się na epicką przygodę aby utrzeć noska somogowi o imieniu Smoug"
        bilbo "Gdyż winny jest za odebranie nam naszych drogich braci"
        bilbo "Ailbo i Cilbo"
        bilbo "Mieli jeszcze tyle życia przed sobą…"
        bilbo "Musimy tam dojechać a dużo jest przeszkód po drodze i Dilbo często musi isć siurać więc to nie jest takie hop siup, pewnie spora porcja dnia zejdzie"
        bilbo "Ale wiesz dostaniesz część skarbu smoga na pewno więc jest to raczej uczciwa wymiana."

        luszcz "Okej… mamy tótaj smoka?"

        bilbo "Nie smoka tylko smoga tego jakby wiesz tego z Krakowa"
        bilbo "W sumie nie wiem co tu robi ale wysoki czarodziej ezoteriusz powiedział nam że jest w pustelni."

        luszcz "A jak mielibyście pokonać smog?"
        
        bilbo "Pomyślałem że wymyślimy coś po drodzę"

        luszcz "oo okej"

        bilbo "To jak zabrałbyś się z nami? Swoją drogą nie mamy żadnych predyspozycji do walki będziemy raczej stać obok i patrzeć gdyby coś się działo. Nie chciałbym też podrażnić moich wrażliwych stópek."

        $ config.menu_include_disabled = True
        menu:
            "{i}tak mam czym jechać i możemy to zrobić (5h){/i}" if cybertruck == 1:
                $ balbo = 2
                $ config.menu_include_disabled = False
                if timer > 9805 and timer <= 9840:
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna
                
                if timer > 11352 and timer <= 11377:
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna

                if timer >= 360 and timer <= 990 or timer >= 1800 and timer <= 2430 or timer >= 3240 and timer <= 3870 or timer >= 4680 and timer <= 5310 or timer >= 6120 and timer <= 6750 or timer >= 7560 and timer <= 8190 or timer >= 9000 and timer <= 9630 or timer >= 10440 and timer <= 10980:
                    $ timer += 300
                    $ bilbo_social_link = 1
                    luszcz "Wiesz co akurat skołowałem sobie takiego grata na kółkach może się tutaj dobrze zmarnować"

                    bilbo "Ojej na poważnie? Ale klasa"
                    bilbo "Jesteśmy ci sromotnie wdzięczni. To ja pójdę wyciągnąć brata z krzaków a ty przygotuj furę"
                    jump bilbo5

                else:
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna
            
            "{i}nuh uh{/i}":
                $ balbo = 1
                $ config.menu_include_disabled = False
                luszcz "Nie nie biorę was nigdzie sorki"
                bilbo "Dobra to będę tu stał cały czas aż ktoś się będzie chciał i mógł"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump sloneczna

    label bilbo6:
        play music "audio/music/natura.mp3"
        scene bg przystanek with fade
        show luszcz neutral at slightleft
        show bilbo neutral at slightright
        bilbo "O wróciłeś, masz już furę?"

        $ config.menu_include_disabled = True
        menu:
            "{i}tak mam czym jechać i możemy to zrobić (5h){/i}" if cybertruck == 1:
                $ config.menu_include_disabled = False
                if timer > 9805 and timer <= 9840:
                    $ balbo = 2
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna
                
                if timer > 11352 and timer <= 11377:
                    $ balbo = 2
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna

                if timer >= 360 and timer <= 990 or timer >= 1800 and timer <= 2430 or timer >= 3240 and timer <= 3870 or timer >= 4680 and timer <= 5310 or timer >= 6120 and timer <= 6750 or timer >= 7560 and timer <= 8190 or timer >= 9000 and timer <= 9630 or timer >= 10440 and timer <= 10980:
                    $ timer += 300
                    $ bilbo_social_link = 1
                    luszcz "Akurat skołowałem sobie takiego grata na kółkach może się tutaj dobrze zmarnować"

                    bilbo "Ojej na poważnie? Ale klasa"
                    bilbo "Jesteśmy ci sromotnie wdzięczni. To ja pójdę wyciągnąć brata z krzaków a ty przygotuj furę"
                    jump bilbo5

                else:
                    $ balbo = 2
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump sloneczna
            
            "{i}Mam ale nie dam{/i}":
                $ config.menu_include_disabled = False
                luszcz "Nie nie biorę was nigdzie sorki"
                bilbo "Dobra to będę tu stał cały czas aż ktoś się będzie chciał i mógł"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump sloneczna

    label bilbo4:
        play music "audio/music/natura.mp3"
        scene bg przystanek with fade
        show luszcz neutral at slightleft
        show bilbo neutral at slightright
        bilbo "O wróciłeś, możemy wyruszać?"

        luszcz "Tak jest!!!"

        bilbo "No i sigma"
        bilbo "Jesteśmy ci sromotnie wdzięczni. To ja pójdę wyciągnąć brata z krzaków a ty przygotuj furę"
        jump bilbo5
                
    label bilbo5:
        scene bg black with fade
        scene bg przystanek2 with fade
        show luszcz neutral at slightleft
        show bilbo neutral at slightright

        bilbo "Dilbo! Dawaj no tutaj!"

        show dilbo neutral at center
        show luszcz neutral at left
        show bilbo neutral at right

        bilbo "To jest ten dobry pan który z nami będzie szponcił przygodę"

        luszcz "Witam jestem Łószczu aka bogaty seksista miło mi cię poznać"

        dilbo "Nie powiem bo się kurwa nie rymuje"

        bilbo "Weź no wymyśl coś bez przesady"

        show dilbo neutral:
            xalign 0.50
            yalign 1.0
            easeout 0.2 xalign 1.0
        show luszcz neutral at left
        show bilbo neutral:
            xalign 1.0
            yalign 1.0
            easeout 0.35 xalign 0.5

        bilbo "Zapomniałem ostrzec.. Dilbo jest w 3/4 niemy i mówi tylko jeśli wymyśli coś co się rymuje."
        luszcz "🤯"

        show dilbo neutral:
            xalign 1.0
            yalign 1.0
            easeout 0.2 xalign 0.5
        show luszcz neutral at left
        show bilbo neutral:
            xalign 0.50
            yalign 1.0
            easeout 0.35 xalign 1.0

        dilbo "Dilbo mam na imie dodaj mnie na steamie 🔥🔥🔥"

        bilbo "Pięknie powiedziane"

        luszcz "Dodam puźniej może"
        luszcz "To chodźcie do fury jedziemy"

        play sound "audio/sfx/car.mp3"

        scene bg tesla with fade

        bilbo "Oki! Gotowi!"
        luszcz "(... nie wiem gdzie jechać…)"

        menu:
            "{b}przed siebie{/b}":
                luszcz "Ah no przecież"

            "{b}spytaj gdzie jechać{/b}":
                luszcz "Ej a gdzie mam jechać"

                bilbo "Przed siebie a gdzie"

                luszcz "A rzeczywiście"

        scene bg black with fade

        $ renpy.pause(0.5)

        scene bg tesla with fade

        play music "audio/music/radio.mp3"

        luszcz "Okej a dokąd teraz zmierzamy bo czuję się jakbym sam siebie porywał"

        bilbo "Do ciemnego lasu i tam cię wykorzystamy a potem odjedziemy twoją furą"

        luszcz "ehh… no tródno"
        luszcz "Dobra ale w zamian pomożecie mi w ogarnięciu małej dywersji w kościele"

        bilbo "Nie no żartowałem sobie jak coś"
        bilbo "Jedziemy do Ostatniej Przyjaznej Żabki"
        bilbo "A z tą dywersją jeśli serio mówisz to raczej uczciwe abyśmy ci pomogli jak ty nam pomogłeś"
        bilbo "Co nie Dilbo?"

        scene bg tesla4

        "{i}Dilbo podnosi swojego siura do gory w aprobacie{/i}"

        luszcz "Najs"

        scene bg tesla
        
        play sound "audio/sfx/boom.mp3"

        with hpunch

        $ renpy.music.set_volume(0.1, delay=0.3)

        luszcz "Googly moogly co to ma być"
        luszcz "Wiedziałem że ten grat nic nie potrafi"

        scene bg tesla2

        goblin "Jebać melona trzaska!!!!"
        goblin "Wypierdalać z tego śmiecia zanim go roztrzaskam o (cokolwiek o co bedzie mozna roztrzaskac co bedzie w tle)"

        luszcz "Nie no weź czekaj!!!"
        luszcz "Eeeeeeeee"

        menu: 
            "{b}Jebać go fr queen slay!!!!!{/b}":
                luszcz "Jebać go fr queen slay!!!!!"

                goblin "No właśnie to planuje robić moja droga"
                goblin "Więc szybko wynocha zanim stracę cierpliwość"
            
            "{b}Nie rób tego, kolega z tyłu rodzi!!{/b}":
                luszcz "Nie rób tego, kolega z tyłu rodzi!!"

                goblin "A nie może urodzić tutaj czy coś"
                goblin "Ja bardzo chcę rozpierdolić to auto"

                scene bg tesla3

                dilbo "Nie powiem bo się kurwa nie rymuje"

                goblin "Dobra sory boże"

                luszcz "No właśnie weź czasem pomyśl "

                bilbo "No właśnie tego typu"

                luszcz "Jedziemy z tąd. Do nowego szpitala w olkuszu."

                goblin "Spokojnej drogi moi drodzy!"

                jump bilbo3
                            
            "{b}Szczerze to to nie jest taka zła fóra{/b}":
                luszcz "Szczerze to to nie jest taka zła fóra"
                luszcz "Można dźwiami marchewki strugać albo palce odcinać"

                goblin "Gówno z tego ja mam do tego narządy w domu"

                luszcz "Dobra a masz np GOŁE BABY pod schowkiem w swoim autku??"

                goblin "Co jest serio gołe baby tu macie"
                goblin "Myślałem że melon lubi tylko dzieci"

                bilbo "Co ty godosz on się nawet na wyspę nie dostał"

                luszcz "Chcesz zobaczyć? Mogę ci pokazać"

                goblin "Hm no pewnie okej"

                bilbo "(co ty wgl robisz halo….)"

                luszcz "Dobra to otwieram ci drzwi"
                luszcz "Po prostu kliknij tutaj guzik do schowka i zobaczysz sam"

                goblin "Hue hue hue type shi hohoho"
                goblin "ejj nie ma tu gołych bab-"

                play sound "audio/sfx/car.mp3"

                luszcz "I cyk zamykamy drzwiczki"

                play sound "audio/sfx/krzyk.mp3"

                goblin "WOKFPOEWJFIEORGJEROIGJEWJFWEOFJWOEPGJRPOGJPOJPJPOVJ"
                goblin "Moja rączka!!!!"

                luszcz "Nie ma rączki łatwo z tobą"
                luszcz "Jedziemy stąd dowidzenia"

                jump bilbo3
            
            "{b}Nie masz prawa nic zrobić z moim pojazdem!{/b}":
                luszcz "Nie masz prawa nic zrobić z moim pojazdem!"

                goblin "zignoruję twą wypowiedź i zrobię co mi się podoba!!!"

                luszcz "Widzisz i ty sobie myślisz że możesz robić co chcesz ale w Zbrodni Ikara było tak samo i tak mu ładnie poszła zbrodnia a i tak się na końcu oddał służbą"

                goblin "Szkoda szczępić ryja"
                goblin "Nie wychodzicie to kończycie tak jak fura"

        bilbo "Dobra ho no tu kolego"

        play sound "audio/sfx/car.mp3"
        $ renpy.music.set_volume(0.0, delay=0.3)

        scene bg black with fade
        "{i}bilbo wychodzi i wybombia swoją stupką goblina{/i}"
        $ stupka += 1

        play sound "audio/sfx/car.mp3"
        scene bg tesla with fade
        $ renpy.music.set_volume(0.1, delay=0.3)
        bilbo "I do pieca"
        bilbo "Możemy jechać dalej"

        luszcz "Najs"

        label bilbo3:
            $ renpy.music.set_volume(0.0, delay=0.3)
            scene bg black with fade
            
            $ renpy.pause(0.5)

            scene bg tesla with fade
            $ renpy.music.set_volume(0.1, delay=0.3)

            bilbo "Okej jesteśmy to tutaj"

            stop music
            play sound "audio/sfx/car.mp3"
            scene bg zabka with fade

            show dilbo neutral at right
            show luszcz neutral at left
            show bilbo neutral at center

            $ renpy.music.set_volume(1.0, delay=0.3)
            play music "audio/music/natura.mp3"

            bilbo "W ogóle zapomniałem wspomnieć ale wysoki czarodziej dał mi taki skibidi papierek który ma nam jakoś pomóc w podróży"
            bilbo "I fajnie ale jest napisany w jakimś starożytnym języku"
            bilbo "“Pis yaoi miau fide yurisi” Ja nie umiem po takiemu mówić"

            luszcz "Ja też"

            bilbo "I właśnie w tej żabce pracuje Elrondo i on jest mądry to on nam rozszyfruje i nas naprowadzi na dobrą drogę (i przy okazji Dilbo się wysiura)"

            luszcz "No dobra oby"
            luszcz "To chodźmy"

            scene bg zabka2 with fade

            show dilbo neutral right at left
            show luszcz neutral at center
            show bilbo neutral right at slightleft
            show elrondo neutral at right

            play music "audio/music/zabka.mp3"

            elrondo "Witam was w żabce w której pracuję"

            luszcz "Dzień dobry"

            show dilbo happy right 

            "{i}dilbo podnosi siura{/i}"

            show dilbo neutral right

            show luszcz neutral at slightleft
            show bilbo neutral right at center

            bilbo "Witaj Elrondo my tu o pomoc"
            bilbo "Czy mógłbyś wyczytać nam ten skibidi papierek? Bo my chcemy się wybrać do Pustelni Błogosławionej Salmonelli aby utrzeć noska smogowi Smougowi."

            elrondo "O kurcze ciężkie zadanko przed wami."
            elrondo "Ale umm sory nie chcę stracić fuchy. Jak chcecie jakiekolwiek usługi to musicie coś kupić w sklepie."

            bilbo "Spoko wiem wiem kupimy naszemu towarzyszowi Łuszczowi hot doga. Też Dilbo musi iść się załatwić."

            show bilbo neutral at center
            bilbo "Masz tutaj chajsiwo"

            luszcz "O kurcze dzięki nie trzeba było"

            bilbo "Możesz mi później wymasować stopy za to"

            show luszcz neutral at center
            show bilbo neutral right at slightleft

            elrondo "Najs to dobra"
            elrondo "Jaka parówa wariacie?"

            menu:
                "{b}szybka{/b}":
                    luszcz "szybka"
                
                "{b}wolna{/b}":
                    luszcz "wolna"
                
                "{b}z długopisem{/b}":
                    luszcz "z długopisem"

            elrondo "Spoko robi się"

            dilbo "Siurać musze bo sie udusze 😣"

            bilbo "Tak tak spoko możesz iść już"
            
            hide dilbo 
            show luszcz neutral at center

            luszcz "Dobra to jak się robi paruwa to poczytaj nam ten papierek"

            elrondo "O racja"

            show luszcz neutral at slightleft
            show bilbo neutral right at slightright

            "{i}Bilbo przekazuje Elrondo papierek{/i}"

            show luszcz neutral at left
            show bilbo neutral right at center

            elrondo "Danke"
            elrondo "hmm….."

            elrondo "“pis nekoni drip aura lolili yaoi a fide skibidziaki rizza yuri tax big ass gjat larp chungus fideni yellow smiling friends dochodzi amabatukam. Rizz niskokluczowo miaupi tung tung tung sachura, skibidi tripple t. Neko to miau, sad roblox frfr. Ohio rizz nekoni noce fanum taxi.”"
            elrondo "Wysoki czarodziej musiał być bardzo rozgadany"
            elrondo "Ogółem sprawa wygląda tak:"
            elrondo "Aby dostać się do Pustelni będziecie musieli się przedrzeć przez mroczną puszczę"
            elrondo "niepołomice"
            elrondo "Mroczną puszczę niepołomice"
            elrondo "Uważajcie, jest tam taka siara że można zasnąć z nudów"
            elrondo "Aczkolwiek muszę przyznać że są tam bardzo fajne duże badyle"
            elrondo "I możecie sie pobić nimi na miecze itp"

            luszcz "Omg"
            luszcz "Musimy to zrobić"

            bilbo "Dobra to może zróbmy sobie tam przerwę na piknik i się pobawimy"

            luszcz "Epicko"

            elrondo "Tak i jeszcze niby tam są żubry ale ja nwm wybombione"
            elrondo "O!"
            elrondo "Hot dog dla ciebie"

            show luszcz neutral at center
            show bilbo neutral right at left

            elrondo "Tylko powiedz jaki sos chcesz"

            menu:
                "{b}Własny{/b}":
                    $ sperma = 1
                    luszcz "Własny"

                    elrondo "Oki daj chwilę"
                    elrondo "rrrrhhhgggggggg"
                    elrondo "aahghgghggghhhhh"
                    elrondo "Proszę"

                    luszcz "Dziękuję ślicznie"
                    luszcz "Am am am"

                    n "{i}Zjadłeś hot doga z sosem własnym! Masz teraz energię do końca dnia!{/i}"

                    luszcz "Pychotka"
                
                "{b}sos który zmienia hot doga w Jabola{/b}":
                    luszcz "sos który zmienia hot doga w Jabola"

                    elrondo "Dobrze trzymaj"

                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 1

                    n "{i}*Jabol został dodany do ekwipunku*{/i}" 

                    luszcz "Dziękuję serdecznie"

            
            elrondo "Okej eee na czym skończyłem…"

            elrondo "Ah tak pod drziwami aby zostać wpuszczeni musicie powiedzieć “Pis yaoi miau fide yurisi” inaczej was nie wpuszczą bo tak było zawsze i tak jest dziś"

            luszcz "Dobrze będę pamiętać"

            bilbo "Uff dobrze że to powiedziałeś bo już się bałem że ja będę musiał"

            luszcz "Musiała w to nie wciągaj"

            bilbo "Dziękujemy L-rondo! Ty i twoje usługi nigdy nie zawodzą."

            elrondo "Spoko cacy nie ma problemu"
            elrondo "W ogóle po co ucieracie noska Smougowi? On nie jest jakiś przepotężny?"

            bilbo "To jest sprawa najcięższej wagi!"
            bilbo "Ailbo i Cilbo, moi bracia, zginęli z jego ręki spacerując w nowej hucie zimą!"

            elrondo "Ojej to straszne!"

            bilbo "Tak i byli tacy młodzi"
            bilbo "Oh jak ja będę za nimi tęsknił… chciałbym ich jeszcze raz zobaczyć…"
            bilbo "Miałem razem z Cilbo dokończyć dywan nad którym wspólnie pracowaliśmy… I iść w góry… i załatwił nam rzucanie siekierami w jakimś lokalu… Zresztą tak niedawno zaznajomił się z jakąś grupką offroadowców i teraz ciągle się pytają kiedy następny wypad… to samo z jego fanami którzy czekają na jego nowy album… nie wiem jak im wszystkim odpowiedzieć."
            bilbo "Ailbo też był okej ig"

            elrondo "To takie przykre biedni ajajajaj"

            luszcz "(hm… coś długo tam ten Dilbo siedzi.)"
            luszcz "(morze przejdę myślami do jego miejsca i zobaczę jak u niego…)"

            $ renpy.music.set_volume(0.0, delay=0.3)
            scene bg black with fade
            scene bg kibloza with fade

            show dilbo neutral right at slightleft

            dilbo "Coś duża ta toaleta"
            dilbo "Muszę szczać a nie ma gdzie"
            dilbo "Dobra siura jest zaleta"
            dilbo "zaraz walnę tam gdzie chce"

            show pier at slightright

            dilbo "Nie powiem bo się kurwa nie rymuje"

            show dilbo neutral right at center

            dilbo "ściągam gacie nie mów tacie 🚬"

            play sound "audio/sfx/glaz.mp3"
            
            dilbo "???"

            show golem neutral at right

            golem "MOJE."

            dilbo "……………"
            dilbo "…………………"
            dilbo "Nie powiem bo się kurwa nie rymuje."

            "{i}Dilbo siura na Golema{/i}"

            golem "SŁUCHAJ NO TY MAŁY-"

            dilbo "Nie mów słucham bo cię wyrucham!"
            dilbo "ZMIAŻDŻĘ CIĘ."

            dilbo "😣😣😣"

            menu:
                "{b}walcz jak waleczny wojownik którym jesteś{/b}":
                    show dilbo neutral:
                        xalign 0.5
                        yalign 1.0
                        easeout 0.4 xalign -0.5
                    n "{i}Dilbo dzielnie uciekł szukając wyjścia z toalety.{/i}"

                "{b}walcz jak gópi gej{/b}":
                    $ edgar = 1
                    hide dilbo
                    play sound "audio/sfx/upgrade.mp3"
                    show mk neutral:
                        xalign 0.4
                        yalign 1.0

                    $ renpy.pause(1.2)
                    play sound "audio/sfx/mk.mp3"

                    show mk neutral:
                        xalign 0.4
                        yalign 1.0
                        easeout 0.4 xalign 0.8
                    
                    $ renpy.pause(1.2)

                    play sound "audio/sfx/grab_key.mp3"
                    hide pier

                    $ renpy.pause(0.8)

                    show mk neutral right:
                        xalign 0.8
                        yalign 1.0
                        easeout 0.3 xalign 0.5
                    
                    $ renpy.pause(0.5)
                    
                    hide mk 
                    play sound "audio/sfx/upgrade.mp3"

                    show edgar neutral:
                        xalign 0.5
                        yalign 1.0
                    
                    $ renpy.pause(1.2)

                    play sound "audio/sfx/ult.mp3"

                    $ renpy.pause(1.0)

                    show edgar neutral2 at jump_left_arc

                    $ renpy.pause(2.35)

            scene bg zabka2 with fade
            $ renpy.music.set_volume(1.0, delay=0.3)
            show luszcz neutral at left
            show bilbo neutral right at center
            show elrondo neutral at right

            bilbo "I jakby… ja rozumiem czemu to jest problematyczne ale nie mogę nie czuć do niego sympatii."

            show bilbo neutral

            bilbo "A ty Łuszczu? Gdybyś był młodym zagubionym mężczyzną to też byś to zrobił co nie?"

            menu:
                "{b}oczywiście{/b}":
                    luszcz "O czym my mówiliśmy…?"

                "{b}że nie{/b}":
                    luszcz "O czym my mówiliśmy…?"
            
            show dilbo neutral right at left
            show luszcz neutral right at center
            show bilbo neutral at slightright

            dilbo "Elo elo 3 2 0"

            bilbo "O jest i Dilbo"

            elrondo "Długo tam siedziałeś mam nadzieję że nie ma za dużo do sprzątania."

            dilbo "Nie powiem bo się kurwa nie rymuje"

            luszcz "Dobra bo jak czas leci to papierz dzieci, myślę rze będziemy się zbierać"

            bilbo "Dziękujemy za gościnę! Do zobaczenia!"

            elrondo "Powodzenia w waszej przygodzie!"

            scene bg zabka with fade
            play music "audio/music/natura.mp3"

            show luszcz neutral at left
            show bilbo neutral at center
            show dilbo neutral at right

            luszcz "To co, do (mrocznej) puszczy niepołomickiej 🤢🤮🤢🤮🤢🤮🤮🤮🤮🤮🤮"

            if edgar == 1:
                show bilbo neutral right
                bilbo "O kurcze Dilbo nie wiedziałem że jesteś zaręczony"

                dilbo "Znalezione nie kradzione"

                bilbo "Oh. To może daj Łuszczowi bo i tak on jest od walczenia to mu się może bardziej przyda mały pierścionek na palec."

                show bilbo neutral right:
                    xalign 0.50
                    yalign 1.0
                    easeout 0.3 xalign 1.0

                show dilbo neutral:
                    xalign 1.0
                    yalign 1.0
                    easeout 0.5 xalign 0.25
                
                $ renpy.pause(0.3)

                show bilbo neutral
                
                $ renpy.pause(0.15)

                $ ring = 1
                "{i}*Pierścień z Władców Pierścieni został dodany do ekwipunku*{/i}"

                luszcz "Dziękuję bardzo"
                luszcz "Jedźmy"

            play sound "audio/sfx/car.mp3"

            scene bg tesla with fade

            cybertruck3 "Brum brum brum-"
            cybertruck3 "O boże puszcza fuj"

            bilbo "Weź może coś puść bo nie chcę słuchać tego grata"

            luszcz "Real"

            play music "audio/music/napaleniec.mp3"

            bilbo "Ojej kocham ten kawałek"

            luszcz "Ja też"

            "{i}Łuszcz i Bilbo patrzą sobie w oczy{/i}"
            "{i}A następnie Łuszcz łapie Bilbo za udo{/i}"

            scene bg tesla5 with fade
            $ renpy.music.set_volume(0.3, delay=0.3)

            cybertruck3 "Brum brum brum"

            scene bg black with fade
            
            $ renpy.pause(0.5)

            scene bg tesla with fade
            $ renpy.music.set_volume(1.0, delay=0.3)

            bilbo "Ej stop!"
            bilbo "Myślę że to dobre miejsce na piknik"

            luszcz "Dobrze zrubmy piknik"

            play sound "audio/sfx/car.mp3"
            scene bg piknik with fade
            play music "audio/music/natura.mp3"

            luszcz "…"
            luszcz "Ale tu jest kurcze siara"

            bilbo "hmm…"
            bilbo "O właśnie mieliśmy szukać patyków przecież!"

            luszcz "O boże rzeczywiście"
            luszcz "Dilbo pilnuj domu zaraz wrócimy"

            play sound "audio/sfx/traveling.mp3"
            scene bg piknik2

            cybertruck3 "…"
            cybertruck3 "Masz może ulubioną markę"

            $ renpy.music.set_volume(0.0, delay=0.3)
            scene bg black with fade
            scene bg lasik with fade
            $ renpy.music.set_volume(1.0, delay=0.3)
            show luszcz neutral at slightleft
            show bilbo neutral at slightright

            luszcz "Gdzie są te badyle?!"
            luszcz "Ale scam"

            bilbo "Może spytajmy na forum patykarzy"

            luszcz "Nie nie rub tego! Za takie pytania trafiasz na liście gończym"

            bilbo "Huh okej"

            luszcz "Dupa sraka a tak sie cieszyłem"

            bilbo "No nic to wracamy"

            $ renpy.music.set_volume(0.0, delay=0.3)
            play sound "audio/sfx/traveling.mp3"
            scene bg black with fade
            scene bg piknik3 with fade
            $ renpy.music.set_volume(1.0, delay=0.3)
            show luszcz neutral at slightleft
            show bilbo neutral right at left

            bilbo "Ojej a oni gdzie"

            luszcz "Czy oni serio poszli się miziać"

            bilbo "Co ty skąd to się wzieło"

            show luszcz neutral at slightleft
            show bilbo neutral at slightright

            luszcz "Nie mów że nie widziałeś przez całą drogę było czuć między nimi iskrę"
            luszcz "Zresztą ani jednego słowa złego o niej nie powiedział"

            bilbo "Ale on prawie nic nie mówi…"
            bilbo "Nie wiem może masz racje boże nie wiedziałem że taki szpont ma miejsce"

            luszcz "To chyba mósimy na nich poczekać arz skończą i przyjdą… eh…."

            bilbo "To się rozłóżmy wygodnie i poczekajmy…"

            scene bg piknik4
            hide luszcz
            hide bilbo

            "{i}Czeku czeku{/i}"
            "{i}Czeku czeku czeku{/i}"

            luszcz "Boże ale nódno w tej puszczy zaraz chyba zasnę"

            bilbo "" 

            luszcz "Bilbo?"

            bilbo "Zzz"

            luszcz "Ah"
            luszcz "Rel"
            luszcz "Zzz"

            $ renpy.music.set_volume(0.0, delay=0.3)
            scene bg black with fade
            scene bg pajenczyna with fade
            $ renpy.music.set_volume(1.0, delay=0.3)

            luszcz "Ahhh wtf co to ma być"

            bilbo "O nie śpisz"
            bilbo "Ej oni chyba nie uprawiali seksu"
            bilbo "Patrz też tu są"
            bilbo "I koszyk piknikowy też"
            bilbo "Nwm czy dostrzegłeś ale na ciebie nie zostało im wystarczająco klejącego białego płynu"
            bilbo "Możesz nas perchance uratować korzystając ze swojej mobilności? Nie chciałbym podrażniać moich cennych stupek. Proszę dbaj o moje stopy…."

            luszcz "No no spoko okej niech tylko pomyślę…"

            luszcz "(Muszę wybawić ich wszystkich z pajęczyny zanim skończy mi sie staminka…)"

            if sperma == 1:
                luszcz "(Na szczęście sos własny z żabki sprawił że mam więcej siły do działania!)"

            luszcz "(Bilbo jest najbliżej mnie… Tesla nie jest daleko ale jest w ciul ciul ciul ciężka… Dilbo jest na najdalszej pajęczynie… Koszyka raczej nie muszę brać, ale może się przydać)"
            luszcz "Oki gdyby to przedstawić na chłopski rozum"

            if sperma == 1:
                luszcz "To ja mam 5 energii" 
            else:
                luszcz "To ja mam 4 energii"  

            luszcz "Tesla, Bilbo i koszyk zabiora mi po jednej energii to uratowania"
            luszcz "A Dilbo zabierze dwie energie"

            if sperma == 1:
                luszcz "to mogę uratować wszystkich"
                luszcz "To tak jak w spiderwers"

                bilbo "Fajnie super analiza"
                bilbo "To do roboty"

                $ renpy.music.set_volume(0.0, delay=0.3)
                play sound "audio/sfx/pajak.mp3"
                scene bg black with fade
                "{i}Łuszczu uwalnia wszystkich z klejącego białego płynu{/i}"

                if piknik == 0:
                    $ ile_item += 1
                $ piknik += 1
                "{i}*Kosz piknikowy został dodany do ekwipunku*{/i}"

                scene bg piknik3 with fade

                show luszcz neutral zorder 10 at left
                show tesla neutral:
                    xalign 0.4
                    yalign 1.0
                show bilbo neutral zorder 10 at slightright
                show dilbo neutral zorder 11 at right
            
            else:
                menu:
                    "{b}W takim razie takie kombinacje są mi dostępne{/b}"

                    "{b}Uratuj Teslę Bilbo i koszyk{/b}":
                        luszcz "Dobra zostawiamy Dilbo"

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        play sound "audio/sfx/pajak.mp3"
                        scene bg black with fade
                        "{i}Łuszczu uwalnia wszystkich oprócz Dilbo{/i}"

                        if piknik == 0:
                            $ ile_item += 1
                        $ piknik += 1
                        "{i}*Kosz piknikowy został dodany do ekwipunku*{/i}"

                        scene bg piknik3 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)
                        show luszcz neutral zorder 10 at left
                        show tesla neutral:
                            xalign 0.4
                            yalign 1.0
                        show bilbo neutral zorder 10 at right

                        bilbo "Co ty wgl sobie myślisz idę mu pomóc"

                        $ stupka += 1

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        scene bg black with fade
                        
                        $ renpy.pause(0.5)

                        scene bg piknik3 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)

                        show luszcz neutral zorder 10 at left
                        show tesla neutral:
                            xalign 0.4
                            yalign 1.0
                        show bilbo neutral zorder 10 at slightright
                        show dilbo neutral zorder 11 at right

                        bilbo "Ałć… moje stupki"

                        dilbo "Braci się nie traci"

                        luszcz "Sorki ktoś musiał zostać z tyłu i nie był to koszyk"

                    
                    "{b}Uratuj Dilbo Teslę i Bilbo{/b}":
                        luszcz "Dobra to zostawiamy koszyk"

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        play sound "audio/sfx/pajak.mp3"
                        scene bg black with fade
                        "{i}Łuszczu uwalnia wszystko oprócz koszyka{/i}"

                        scene bg piknik3 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)

                        show luszcz neutral zorder 10 at left
                        show tesla neutral:
                            xalign 0.4
                            yalign 1.0
                        show bilbo neutral zorder 10 at slightright
                        show dilbo neutral zorder 11 at right

                        bilbo "Biedny koszyk no trudno"
                        bilbo "Niech się nim upchają"

                    
                    "{b}Uratuj Dilbo Teslę i koszyk{/b}":
                        luszcz "Dobra to zostawiamy Bilbo da se radę"

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        play sound "audio/sfx/pajak.mp3"
                        scene bg black with fade
                        "{i}Łuszczu uwalnia wszystkich oprócz Bilbo{/i}"

                        if piknik == 0:
                            $ ile_item += 1
                        $ piknik += 1
                        "{i}*Kosz piknikowy został dodany do ekwipunku*{/i}"

                        scene bg piknik3 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)
                        show luszcz neutral zorder 10 at left
                        show tesla neutral:
                            xalign 0.4
                            yalign 1.0
                        show dilbo neutral zorder 10 at right

                        luszcz "Cieszę się że udało się nam wszystkim zejść"
                        
                        show luszcz neutral zorder 10 at left
                        show tesla neutral:
                            xalign 0.4
                            yalign 1.0
                        show dilbo neutral zorder 10:
                            xalign 1.0
                            yalign 1.0
                            easeout 0.3 xalign 0.75

                        show bilbo neutral zorder 11:
                            xalign 1.3
                            yalign 1.0
                            easeout 0.3 xalign 1.0

                        $ stupka += 1

                        bilbo "Ale chujnia"
                        bilbo "Moje biende stupki"
                    
                    "{b}Uratuj Dilbo Bilbo i koszyk{/b}":
                        $ kaput = 1
                        luszcz "Dobra to zostawiamy Teslę nie potrzebuję tego śmiecia"

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        play sound "audio/sfx/pajak.mp3"
                        scene bg black with fade
                        "{i}Łuszczu uwalnia wszystkich oprócz Tesli{/i}"

                        if piknik == 0:
                            $ ile_item += 1
                        $ piknik += 1
                        "{i}*Kosz piknikowy został dodany do ekwipunku*{/i}"

                        scene bg piknik3 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)
                        show luszcz neutral zorder 10 at left
                        show bilbo neutral zorder 10 at slightright
                        show dilbo neutral zorder 11 at right

                        bilbo "Ej a co z autem?"

                        luszcz "Idziemy na nogach"

                        bilbo "Nie no aż tyle to nie"

                        show tesla neutral:
                            xalign 0.4
                            yalign -5.0
                            easeout 0.6 yalign 1.0
                        
                        $ renpy.pause(0.5)
                        with hpunch
                        play sound "audio/sfx/boom.mp3"
                        
                        show tesla neutral2:
                            xalign 0.4
                            yalign 1.0

                        cybertruck3 "Nie chcieli mnie bo jestem ze wsi"

                        luszcz "O no i cacy auto jest"
                        luszcz "Troche uszkodzone ale jest"
                
            luszcz "To dobra jedziemy dalej cnie ekipa"

            bilbo "Jedziemy jedziemy"

            dilbo "Nie powiem bo się kurwa nie rymuje"

            play sound "audio/sfx/car.mp3"
            stop music

            if kaput == 1:
                scene bg tesla6 with fade
            else:
                scene bg tesla with fade
            
            play music "audio/music/zbrodnie.mp3"
            
            cybertruck3 "Brum brum brum"
            cybertruck3 "Brum brum brum"
            cybertruck3 "Trzask bum zderzenie!"

            with hpunch
            play sound "audio/sfx/boom.mp3"

            luszcz "Ojej ups musiałem za długo patrzeć w stopy Bilbo i w coś wjechać"

            play sound "audio/sfx/car.mp3"
            $ renpy.music.set_volume(0.3, delay=0.3)

            if kaput == 1:
                scene bg sw2 with fade
            else:
                scene bg sw with fade
            
            show luszcz neutral right at center

            luszcz "Ojej przepraszam. Jesteście cali?"

            sw "Nie no spoko nic mi nie jest bo jestem ze skały"

            luszcz "Ale zbieg okoliczności ja terz! Jak masz na imię?"

            sw "Skamieniały wędrowiec"

            luszcz "O okej ma sens chyba nie jesteś ze Skały skały"

            sw "a ty?"

            luszcz "na mnie muwią mędrzec ze skały"

            sw "A okej spoko"
            sw "Dobra będę szczery nie bądź zły"
            sw "Miałem się na ciebie wkurzyć o coś i z tobą walczyć ale starczy czasu na dodawanie kolejnych walk więc z tobą nie powalcze okej"

            luszcz "Spoko nic się nie dzieje i tak będę walczył ze Smogiem zaraz"

            sw "Heh… ano tak haha lol"
            sw "To dobra to dowidzenia"

            luszcz "Dowidzenia miło było poznać"

            $ renpy.music.set_volume(1.0, delay=0.3)
            stop music

            play sound "audio/sfx/car.mp3"
            scene bg black with fade

            $ renpy.pause(0.5)

            scene bg pustelnia with fade
            play music "audio/music/natura.mp3"

            show luszcz neutral zorder 10 at center 
            if kaput == 1:
                show tesla neutral2 at right
            else:
                show tesla neutral at right
            
            show bilbo neutral right zorder 11 at slightleft
            show dilbo neutral right zorder 12 at left
           
            bilbo "Dobra jesteśmy"
            bilbo "Teraz powiedz to skibidi zaklęcie jakie miałeś zapamiętać"

            nikt "No no właśnie zrób to booo bo inaczej nwm co się stanie"

            luszcz "Ojej teraz zrobiło się poważnie"

            menu:
                "{b}Podaj Hasło:{/b}"

                "{b}Pis yuri sigmali plo{/b}":
                    $ macanko = 1
                    nikt "Dupa pieprzyć to nie to ale ok wchodźcie i tak"
                    nikt "Już otwieram bramę"
                
                "{b}Sus baka plo neko yuri{/b}":
                    $ macanko = 1
                    nikt "Dupa pieprzyć to nie to ale ok wchodźcie i tak"
                    nikt "Już otwieram bramę"               

                "{b}Po dripisi bakasini loli yaoisi{/b}":
                    $ macanko = 1
                    nikt "Dupa pieprzyć to nie to ale ok wchodźcie i tak"
                    nikt "Już otwieram bramę"
                
                "{b}Pis yaoi miau fide yurisi{/b}":
                    nikt "Dupa pieprzyć to nie to ale ok wchodźcie i tak"
                    nikt "Już otwieram bramę"
                
                "{b}Po rizzisi skibidisipi loli{/b}":
                    $ macanko = 1
                    nikt "No i klasa bardzo lubię jak młodzi utrzymują tradycje"
                    nikt "Juz otwieram bramę kochani"
            
            luszcz "Dobra to ty Tesla Cybertruck czekaj grzecznie my wszystko ogarniemy"

            cybertruck3 "Bez sensu ja też chcę"

            luszcz "No i dupa jakoś musimy wrucić spowrotem zostajesz"
            luszcz "Nie daj się porwać"

            cybertruck3 "Ok big guy"

            scene bg pustelnia2 with fade
            play music "audio/music/hobit1.mp3"
            show luszcz neutral at center
            show salmonella neutral at right
            show bilbo neutral right at slightleft
            show dilbo neutral right at left

            nikt "Witajcie moi drodzy w mojej skibidi pustelni"

            salmonella "Mam na imię Salmonella i jestem błogosławiona"
            salmonella "Co was tu sprowadza?"

            bilbo "Może na taki bezpieczny wstęp powiedzmy że jesteśmy żądnymi przygód bohaterami"

            luszcz "Dobra zrubmy to"
            luszcz "Jesteśmy rządnymi przygud bohaterami"

            salmonella "O okej"
            salmonella "Ale po co tu przyszliście"

            luszcz "(grrrr co jak ona jest przeciw nam co wtedy nwm co powiedzieć)"

            bilbo "Aghhh Dilbo wymyśl coś"

            show dilbo zly right
            dilbo "Nie powiem bo się kurwa nie rymuje"

            salmonella "Dobra panowie czy jesteście tu po S - M - O - G - A"

            show dilbo neutral right

            luszcz "Czemu to tak dziwnie mówisz"

            salmonella "B - O  J - E - S - T  P - O - D  N - A - M - I  I   N - I - E  R - O - Z - U - M - I - E  P - R - Z - E - L - I - T - E - R - O - W - Y - W - O - W - A - N - I - A"

            luszcz "ooo okej"

            bilbo "No to dokładnie tak"
            bilbo "Przyszliśmy tu po pizzę"

            salmonella "W takim razie pewnie słyszeliście o tym że pizza zabrała najcenniejszy skarb tej puszczy czyli fajne salami i horduje je w olbrzymiej jaskini pod nami?"

            luszcz "Nie nie słyszeliśmy nic takiego"

            salmonella "salami to P - A - T - Y - K - I"

            luszcz "ah"

            salmonella "Cała społeczność zbierania salami jest zdruzgotana bo pizza wzięła je wszystkie dla siebie"
            salmonella "A mnie nie tylko zabrał kolekcję, ale też moją giga tuff jaskinię"

            bilbo "To my jesteśmy tu aby zjeść tą pizzę raz na zawsze!!!"

            luszcz "A czemu w sumie tó się usadowiła?"

            salmonella "Chyba dlatego że planuje zasmogować skałę w związku z tym całym dołączaniem do Krakowa cnie"

            bilbo "Ojej takie coś się dzieje?"

            luszcz "No no a właśnie"
            luszcz "Miałem spytać czy za to że pomogę wam zjeść pizzę pomożecie mi w tworzeniu opozycji wobec przyłączania Skały do Krakowa? Utrzemy noska pizzy a później księdzu"

            bilbo "No spoko"

            dilbo "spoko loko"

            luszcz "Dzięki ziomale"
            luszcz "o chodźmy morze do tej jaskinii"

            if macanko == 1:
                salmonella "Jak najbardziej ale najpierw"

                scene bg black
                "{i}Salmonella molestuje Łuszcza, potem Bilbo, potem Dilbo{/i}"

                scene bg pustelnia2 with fade
                show luszcz neutral at center
                show salmonella neutral at right
                show bilbo neutral right at slightleft
                show dilbo zly right at left

                luszcz "!"

                bilbo "!"

                dilbo "!"

                salmonella "Proszę bardzo."

                luszcz "Co to miało być!"

                $ stupka += 1

                salmonella "Kara za wypowiedzenie złego hasła sory takie są zasady"
                salmonella "Teraz wszyscy macie salmonellę"
                salmonella "Btw, ty niski, fajne stopy"
                salmonella "Czy masz jakieś social media albo inne fajne linki?"

                bilbo "NIE ale teraz mam zarażone stopy 😡"

                salmonella "Życie"

                show dilbo neutral right
            
            salmonella "Dobra chodźcie tutaj"
            salmonella "Tędy w lewo w dól potem trzecia drabina z prawej, na dole wpisać kod 67 i wejść do pieca, przez piec zjeżdżalnią w dół i potem prosto"

            luszcz "Dobrze dziękujemy"

            salmonella "Powodzenia… myślę że raczej zginiecie ale zawsze są jakieś szanse"

            luszcz "Tego typó benc"

            scene bg pustelnia3 with fade
            show luszcz neutral right at center
            show bilbo neutral at slightright
            show dilbo neutral at right

            luszcz "…"

            bilbo "…"

            dilbo "…"

            luszcz "…to co"

            bilbo "co co"

            luszcz "miałeś wymyślić jak go pokonamy po drodze"
            luszcz "i jak?"

            bilbo "No erm nie wiem"
            bilbo "A ty co "

            luszcz "Nie moja przygoda nie czułem się odpowiedzialny"

            bilbo "Siara"

            luszcz "Dobra to na czuja w takim razie"
            luszcz "Chodźcie"

            bilbo "Nie no nie pamiętasz"
            bilbo "My nie walczymy, mówiłem ci na początku"
            bilbo "Stópki nie rosną na drzewach (poza tym i tak jestem słaby)"
            bilbo "Cnie Dilbo?"

            dilbo "Tak srak"

            luszcz "Ehhhh"
            luszcz "Dobra to umm"

            hide bilbo 
            hide dilbo 
            show luszcz neutral right at slightright
            play music "audio/music/hobit2.mp3"


            luszcz "SMOGU WYZYWAM CIĘ NA POJEDYNEK!!!!"

            scene bg pustelnia4
            show luszcz neutral right at slightright

            "{i}smog się budzi i patrzy na łuszcza{/i}"
            play sound "audio/sfx/gitara.mp3"
            "{i}łuszczu zadaje cios ze wszystkich swoich sił zadając 1 dmg{/i}"
            play sound "audio/sfx/ryk.mp3"
            "{i}smog dmucha w łuszcza zadając mu 99%% hp{/i}"

            luszcz "Oh nie… zdycham… gdybym miał jakiś rug to bym w niego dmóchnął…."
            luszcz "Nienawidzę smogu type shi… to gówno niszczy nasze płóca… jest moim wrogiem numer jeden…"
            luszcz "Mugłbym poprosić Bilbo i Dilbo o pomoc ale tego nie zrobię bo tak…"
            luszcz "Wyciągam rękę do Skały… mojej ojczyzny… tak bardzo chciałem cie óratować… ale wolę umrzeć z honorem…. Kocham cię Skało…. Nie mów żadnej gotce…."
            luszcz "*kaszlu* *kaszlu*"
            luszcz "…."

            nikt "*WRRRRRRR*"

            luszcz "Cóż to takiego?"

            if kaput == 1:
                show tesla neutral2 at center
            else:
                show tesla neutral at center
            show luszcz neutral right at right

            cybertruck3 "To ja tesla cybertruck"

            if kaput == 1:
                show tesla neutral2:
                    xalign 0.5
                    yalign 1.0
                    easeout 0.3 xalign 0.2
            else:
                show tesla neutral:
                    xalign 0.5
                    yalign 1.0
                    easeout 0.3 xalign 0.2
            
            $ renpy.pause(0.25)
            play sound "audio/sfx/boom.mp3"
            with hpunch

            "{i}nagle tersla cybertruck wjezdza w smog{/i}"

            luszcz "Nieeeeeee!!!! Tesla Cybertruck…!"

            bilbo "o ja pierdole! Zielona energia Tesli Cybertrucka niszczy Smouga od środka…!"

            "{i}Pojawia sie salmonella{/i}"

            salmonella "Panowie!"
            salmonella "O Boże udaje wam się!"
            salmonella "Społeczność zbierania fajnych patyków gdy tylko dowiedziała się, że będziecie ucierać noska smougowi przyszła pomóc!"

            show patykarz neutral at center
            show luszcz neutral right at right

            patykarz "Dobra kociaki, robimy to!"
            patykarz "Okrążyć wroga!"
            patykarz "Gobliny! przygotować bony zakupowe za kaucje!"

            gobliny "Gotowe!"

            patykarz "Wargowie! Niemieckie drzewka z warszawy!"

            wargowie "Gotowe!"

            patykarz "Krasnoludy! Paragoniki opłaty emisyjnej za wjazd do Strefy Czystego Transportu w Krakowie!"

            krasnoludy "Gotowe!"

            patykarz "Elfy! Nakrętki które są przytentegowane do plastikowych butelek!"

            elfy "Gotowe!"

            patykarz "Ludzie! Nie wiem nie mam pomysłu dobre chęci!"

            ludzie "Gotowe!"

            patykarz "ATAAAAAK!!!!!!!!!"

            play music "audio/music/bitwak.mp3"

            scene bg black with fade

            "{i}ziu ziu bum bum bam{/i}"

            scene bg pustelnia5 with fade

            play music "audio/music/hobit1.mp3"

            show luszcz neutral right at slightleft

            luszcz "…udało się…?"
            luszcz "udało się!!!"

            all "Wiwat!!!!!!!!!!!!!"

            show luszcz neutral
            show bilbo neutral at center
            show dilbo neutral at slightright

            bilbo "Brawo! Zrobiliście to!"
            bilbo "Utarliście Smougowi noska!"

            show salmonella neutral at right
            
            salmonella "Brawo! Zrobiliście to!"
            salmonella "Utarliście Smougowi noska!"

            bilbo "Nie nie, to tylko on zrobił"

            luszcz "Nie nie, to tak na prawdę zasługa Cybertrucka"
            luszcz "Kto by pomyślał, że taki skończony śmieć okaże się użyteczny do czegoś…"
            luszcz "Musimy ją znaleźć!"

            random1 "Tutaj jest!"
            
            scene bg pustelnia6 with fade
            if kaput == 1:
                show tesla neutral2 at center
            else:
                show tesla neutral at center
            show dilbo neutral at slightright
            show luszcz neutral at left
            show bilbo neutral at right

            if kaput == 1:
                bilbo "O nie… jest kompletnie rozbombiona!"

                luszcz "Nieeeee… tesla… nie……."

                cybertruck3 "Nam Cybertruckom zawsze zależało tylko na tym, aby wywołać jakąś pozytywną zmianę… jestem spełniona… ale chciałabym jeszcze raz w życiu… poczuć dotyk mojego ukochanego… zanim odejdę z tego świata…"
                
                dilbo "moja przyjaciółko godowa"
                dilbo "nie musisz mówić ani słowa"

                "{i}Dilbo siura na tesle{/i}"

                luszcz "Dobra chodźmy stąd"

                $ cybertruck = 0
                $ ile_item_fabularne -= 1

            else:
                luszcz "Tesla! Żyjesz!?"

                cybertruck3 "Żyje"
                cybertruck3 "Już zasługuję na emeryturę ale żyje"

                luszcz "Ale nas odwieziesz cnie"

                cybertruck3 "No.. dobra.."

                luszcz "I git"

            scene bg pustelnia5 with fade
            show salmonella neutral at slightleft
            show luszcz neutral right at center
            show bilbo neutral at right

            salmonella "Łuszczu!"
            salmonella "Za to że pokonałeś Smouga (pomijając zasługi samochodu) chciałabym ci podarować najgorszy fajny patyk z mojej kolekcji fajnych patyków. Zasłużyłeś na niego."

            $ patyk = 1
            "{i}*Fajny Patyk został dodany do ekwipunku*{/i}" 

            luszcz "Ale supi fajny patyk"

            patykarz "EKHEM."

            show patykarz neutral at center
            show luszcz neutral right at slightright

            patykarz "Ta sterta zawiera wszystkie patyki z całej krainy. Nie jesteśmy w stanie ustalić który należał do kogo. Jak chcemy rozporządzać tymi dobrami pani Salmonello?"

            salmonella "Odpowiedź jest prosta"
            salmonella "Wszystkie są moje proszę się wynosić"

            patykarz "…!"
            patykarz "To niedopuszczalne!"

            salmonella "Sralne"
            salmonella "Macie minutę na wyjście albo zrobi się niemiło"

            patykarz "Masz minutę na ogarnięcie się albo moi ludzie rozerwą cię na strzępy!"

            bilbo "(Łuszczu… może wynośmy się stąd zanim dostaniemy gigantyczną dawkę bakterii salmonelli do naszego organizmu type shi..)"

            salmonella "Tak się do was wszystkich spuszczę że ta jaskinia stanie się zbiorowym grobowcem!"

            luszcz "(Dobra spadamy)"

            scene bg pustelnia with fade
            play music "audio/music/bitwak.mp3"
            $ renpy.music.set_volume(0.3, delay=0.3)

            show luszcz neutral right zorder 10 at center 
            if kaput == 0:
                show tesla neutral at right
            
            show bilbo neutral right zorder 11 at slightleft
            show dilbo neutral right zorder 12 at left

            bilbo "Ah… zadanie wykonane."
            bilbo "Nie ma to jak ryzykować życie dla nienawistnej zemsty."

            show dilbo happy right 

            dilbo "Nie powiem bo się kurwa nie rymuje"

            luszcz "Tak tak, so true"

            show dilbo neutral right 
            show luszcz neutral

            n "{i}Nagle…!{/i}"
            n "{i}Z nieba przychodzi duch…!{/i}"

            show ailbo duch:
                xalign 0.8
                yalign 0.2

            ailbo "Dzięki że utarliście noska cwelowi"
            ailbo "Okazało się że ten “czyn” był tak “nienawistny” że dał nam przepustkę na odwiedzenie was… nwm czy jako nagroda czy przestroga czy cos innego."

            bilbo "Ailbo…!!!"
            bilbo "A gdzie jest Cilbo…?"

            ailbo "No przepustka była jedna a ja pierwszy wszedłem to masz tylko mnie"
            ailbo "toooo ummm jak tam u ciebie"

            bilbo "A nie wiem jest okej"
            bilbo "Jadłem piknik"

            ailbo "A to fajnie fajnie."
            ailbo "W niebie jest całkiem fajnie można prelitować zajkusy cały dzień"
            ailbo "O sory bo wy nie wiecie co to"
            ailbo "Bo jakby w niebie są takie zajkusy to jest jakby… pinezki ale takie duże i całe niebieskie i jakby. Zamiast czubka mają taki jakby mix kozy z woskiem."
            ailbo "I jak to coś prelitujesz. W sensie. Dobra nie będę tłumaczył. To to robi taki fajny dym o zapachu prawdy. Mocny shit."
            ailbo "Eeee w każdym razie Cilbo mówił że nie może się doczekać zobaczenia z tobą i miał jakieś instrukcje co do tego co masz zrobić z jego albumem czy innymi rzeczami ale troche nie pamiętam"
            ailbo "Myślę że sobie poradzisz"

            bilbo "Haha no dobra coś ogarnę"

            ailbo "Dobra to ja spadam"
            ailbo "Bo gadanie o zajkusach dało mi na nie chrapkę…"
            ailbo "To nara"
            ailbo "O nie chwila"
            ailbo "Właśnie Dilbo"
            ailbo "Bóg mówił że jesteś od urodzenia jesteś skazany na wieczne cieprienie w piekle"

            dilbo "Nie powiem bo się kurwa nie rymuje"

            ailbo "Dobra nara"

            bilbo "Cześć"

            dilbo "Dobranoc pchły na noc"

            hide ailbo
            show luszcz neutral right

            luszcz "ah."

            bilbo "Ten Ailbo. Taki z niego zgrywus."

            if kaput == 1:
                luszcz "Dobra to możemy już wyruszać"

                bilbo "O no tak… nie ma auta…"
                bilbo "To musisz mnie nosić na rękach"
                bilbo "Moi subskrybenci nie zasługują na podrażnione stopy"

                luszcz "Eh…."
                luszcz "To chyba będzie długa podróż…"

                stop music
                play sound "audio/sfx/car.mp3"
                scene bg black with fade

                n "{i}Ma rację! Powrót na nogach zajął dużą ilość czasu!{/i}"

                scene bg przystanek with fade
                play music "audio/music/natura.mp3"
                $ renpy.music.set_volume(1.0, delay=0.3)
                
            else:
                luszcz "Dobra to możemy już jechać myślę"

                bilbo "Jedźmy jedźmy."

                stop music
                play sound "audio/sfx/car.mp3"
                scene bg black with fade

                $ renpy.pause(0.5)

                scene bg przystanek2 with fade
                play music "audio/music/natura.mp3"
                $ renpy.music.set_volume(1.0, delay=0.3)

            show bilbo neutral at center
            show luszcz neutral at left
            show dilbo neutral at right

            bilbo "Dobra to jak już po wszystkim"
            bilbo "Chcielibyśmy ci ostatecznie złożyć dzięki za twoja przysługę"
            bilbo "Miałem ci coś pomóc przeciw księdzu tak?"

            luszcz "Po prostu przy każdej okazji mów przeciw włączaniu Skały do Krakowa"

            bilbo "Okej jestem w stanie to zrobić"

            if stupka >= 2:
                $ bilbo_social_link = 1
                bilbo "Jeszcze chciałbym dodać"
                bilbo "Że nic kurwa nie potrafisz dbać o moje spiękne stópki i że są teraz usrane całe po tej przygodzie"
                bilbo "Bardzo mnie to drażni i mimo mojej wdzięczności nie będę ukrywał swojego niezadowolenia. Miałeś jedno zadanie i jednego side questa i udało ci się go zawalić. Tego side questa"

                luszcz "Co ja mogę powiedzieć"
                luszcz "Nic nie powiem"

                bilbo "No może się tu rozstańmy"
            
            else:
                $ bilbo_social_link = 2
            
            luszcz "To dobra to papatki dowidzenia widzimy się kiedyś może dobrze się robiło z wami biznes"

            bilbo "Dziękuję pozdrawiam nazwajem ppapapapapapa"

            dilbo "Żegnam serdecznie ciebie nie ma dla mnie miejsca w niebie"

            $ bilbo_social_link = 1

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



















            

            





















