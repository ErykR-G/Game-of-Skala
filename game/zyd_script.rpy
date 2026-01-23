default lethalc12 = 0
default lethalc13 = 0
default lethalc21 = 0
default lethalc22 = 0
default lethalc23 = 0
default gaz = 1


label zyd:
    label zyd1:
        $ zyd_social_link = 1
        play music "audio/music/monopolowy.mp3"
        scene bg monopolowy with fade
        show luszcz neutral at left
        show braun neutral at right

        braun "Szczęść boże"
        luszcz "Ojacie Grzegorz Braun"
        braun "Kłaniam się"
        luszcz "Od kiedy pan prowadzi monopol w Skale?"
        braun "Od momentu gdy odkryłem że moja żona ma korzenie żydowskie i identyfikuje się jako mężczyzna"
        braun "Postanowiłem zrobić sobie przerwę od polityki i zacząłem prowadzić ot taki skromny sklepik monopolowy"
        braun "Skała jest bardzo pięknym miastem gdyż o ile mi dobrze wiadomo żydzi znajdują się tu tylko na cmentarzu"
        luszcz "Fajnie fajnie"
        braun "I jeszcze jak"

        show luszcz neutral at center
        show zyd neutral at left

        zyd "Szalom alejhem!"
        zyd "Nawet państwo nie wiedzą jak bardzo potrzebuję dobrych tanich jaboli"

        braun "Cóż to za szyderstwo losu! Pan nie tylko jest żydem"
        braun "Ja pana kojarzę!"

        zyd "O mój żydowski boże (Jahwe)!"
        zyd "Panie Grzegorzu czy mogę pana zainteresować nie pojawianiem się regularnie w moim życiu?"

        braun "Mam dla pana dobrą wiadomość"
        braun "Może pan niezwłocznie opuścić ten sklep i nic nikomu się nie stanie"
        braun "Myślałem że do tego nie dojdzie, ale będę musiał zawiesić zakaz wchodzenia dla żydów"

        zyd "Nie no ale jabole bym sobie i tak kupił"
        zyd "Pieniądz to pieniądz, zapłacę jak każdy inny!"

        braun "Proszę mnie nie prowokować"
        braun "W sklepie znajduje się jeszcze osoba trzecia. Proszę stąd wyjść aby mogła dokonywać zakupów w spokoju"

        zyd "Niedorzeczne! A co ja niby takiego robię. Trzy butelki i mnie nie ma"
        zyd "Czy ja panu w czymkolwiek swoją obecnością przeszkadzam?"

        menu:
            "{b}Wynoś się stąd głupi żydzie!!!{/b}":
                luszcz "Wynoś się stąd głópi żydzie!!!"

                braun "Ah, ta Polska młodzież…"
                braun "Muzyka dla moich uszu"

                zyd "Jak panśtwo mogą!? To bezprawie! Nie było żadnego zakazu wstępu!"

                braun "Proszę migiem stąd znikać. Nikt tu pana nie chce"

                luszcz "Bo jeszcze z monopolowego zrobisz monopol!"

                braun "Dokładnie tak! Prosze nie polepszać mojej sytuacji finansowej!"
                braun "Znikaj stąd prowokatorze!"

                zyd "dobra okej"
                zyd "Niemiło…"

                hide zyd
                show luszcz neutral at left
                show braun smile at right
                $ zyd_social_link = 10
                $ zyd_wybory = 0
                $ braun_wybory = 2

                braun "Dziękuję za pomoc w pozbyciu się tej łachudry"
                luszcz "Nie ma problemu, nienawidzę żyduw"

                braun "Ma pan tu ode mnie mały upominek pieniężny"
                braun "Na te gwałtowne zmiany w systemie płatniczym"

                $ money += 1
                "{i}*do ekwipunku został dodany 1 portfel*{/i}"

                luszcz "Dziękuję, nie tszeba było"
                braun "Cóż, co pan chce kupić?"

                jump sklep_monopolowy2
            
            "{b}Panie Braun pan przesadza{/b}":
                luszcz "Panie Braun panu się coś w dópie poprzewracało"
                zyd "Klasa"
                braun "Ah, ta Polska młodzież…"
                braun "To są jakieś drwiny"
                braun "Każdy kto stoi po stronie żydów jest w moich oczach żydem"
                braun "Jako iż są państwo w mojej domenie, dokonuję na was zatrzymania"
                braun "Ta zniewaga krwi wymaga. Będą państwo wisieć!"

                $ zyd_sojusznik = 1
                $ liczba_sojusznikow += 1

                jump fight21
            
        label after_fight21:
            scene bg monopolowy
            play music "audio/music/monopolowy.mp3"
            show zyd neutral at left
            show luszcz neutral at center
            show braun neutral at right
            $ zyd_sojusznik = 0
            $ liczba_sojusznikow -= 1
            braun "Awięc to tak"
            braun "Jestem w stanię uszanować dobre bicie"
            braun "Zwracam panu honor. Jest pan tu mile widziany"

            luszcz "Zlałbym panu dupsko przy każdej możliwej okazji"

            braun "Ale pana żyda nie chcę nigdy więcej widzieć na oczy"

            zyd "Myślę że przed wyjściem wywalczyłem sobie dwie flaszki"

            braun "Znikaj stąd prowokatorze!"

            hide zyd
            show luszcz neutral at left

            braun "Ty możesz je posiąść"

            if jabole == 0:
                $ ile_item += 1

            $ jabole += 2

            "{i}*2 Jabole zostały dodane do twojego ekwipunku*{/i}"

            luszcz "Dzięki"

            braun "Mój sklep jest dla pana zawsze otwarty"

            luszcz "Do widzenia Panie Braun"

            braun "Żegnam pana"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"

            scene bg alejka
            hide zyd
            show luszcz neutral at slightleft
            show zyd neutral right at slightright

            zyd "Nie cierpię tego frajera"
            zyd "Jeszcze zanim Kraków umiastowił mój sklep, Braun kręcił się wokół i odstraszał moich klientów"
            zyd "Ale pieniądz się jakoś zgadzał. Teraz nie ma niczego"
            zyd "Znaczy pieniądze są, ale się nie mnożą. Na razie rozglądam się za noclegiem"

            luszcz "A czemu akurat w Skale?"

            zyd "Tu są moje korzenie"

            luszcz "okay"
            luszcz "Chcesz Jabola?"

            zyd "Pewnie"

            $ jabole -= 1

            "{i}*Tracisz 1 Jabola*{/i}"

            zyd "Wiesz co"
            zyd "Wydaje mi się że interesują cię problemy żydowskiego narodu"

            luszcz "eeee powiedzmy"

            zyd "Jest taka jedna sprawa którą od dawna chciałem się zająć. Myślę że z partnerem mógłbym się za nią zabrać"
            zyd "Gdybyś był zainteresowany pomocą, przyjdź na cmentarz, ale nie ten dla pospólstwa, tylko prawilny"
            zyd "Dam ci namiary"

            luszcz "Dobrze, jak bende miał czas to przyjdę"

            zyd "Toda. Lehitraot"

            hide zyd 
            show luszcz neutral at center

            luszcz "(Hm… mogę poszukać cmentarza rzydowskiego i dowiedzieć się co pan żyd chce szpącić)"

            $ zyd_social_link = 1
            $ zyd_wybory = 1
            $ braun_wybory = 1
            hide luszcz
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
    
    label zyd2:
        scene bg cmentarz_zydowski with fade
        play music "audio/music/natura.mp3"
        $ zyd_social_link = 2
        show zyd neutral right at slightright
        show luszcz neutral at left

        luszcz "Alerz tu klimacik"

        zyd "O! Szalom alehjem"
        zyd "Właśnie o tobie myślałem"

        luszcz "Szalom, jaką miałeś do mnie sprawę?"

        zyd "Tak, dziękuję że przyszedłeś!"
        zyd "Jak już ci mówiłem, moi przodkowie mieszkali w tych okolicach"
        zyd "Wszyscy są tu pochowani"
        zyd "Wszyscy poza moim pra-pra-dziadkiem"
        zyd "Walczył w 1 wojnie światowej i jego ciało zostało przemycone do jakiegoś grobowca zbiorowego na pogańskim cmentarzu"
        zyd "Nigdzie nie zgadzał się na takie potraktowanie. Chciałbym się mylić ale obawiam się, że gnije w gehennie (judaizmowym czyśćcu). To nie jest w porządku"
        zyd "Chciałbym pójść pod kwaterę żołnierzy 1 wojny światowej i wydobyć jego ciało aby dać mu godny pochówek!!"
        zyd "..."
        zyd "Myślisz że to… dobry pomysł?"

        menu:
            "{b}Świetny{/b}":
                luszcz "Tak myślę że jest świetny"
                luszcz "Chętnie pomogę ci wykopać arcy stare ludzkie ciało z grobu do grobu"
                
                zyd "Toda! Dziękuję!"
                zyd "Niech Jahwe będzie Ci litościwy za troskę o naród żydowski"
                zyd "Niestety raczej nie ma dla ciebie nadziei, bo nie jesteś wierzący i nie jesteś żydem, więc będziesz płonął w piekle"

                luszcz "Jestem w stanie to zaakceptować jeśli będę mógł spotkać wujka Stalina"

                zyd "Cieszę się że znajdujesz pozytywy"
                zyd "W takim razie widzimy się pod grobowcem! Pradziadek wreszcie wróci do domu!"
                zyd "Lehitraot!"

                luszcz "Lechii tarot"

                hide zyd 
                show luszcz neutral at center

                luszcz "Doszpącone"
                luszcz "Ale cel uświęca środki. To nawet nie jest nekrofilia"
                luszcz "Cóż, mogę teraz iść poszukać kwatery żołnierzy 1 wojny światowej"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump lipowa
            
            "{b}Okropny{/b}":
                luszcz "O czym ty pierdolisz"
                luszcz "To nie jest jakaś nekrofilia czy coś?"

                zyd "Nie actually nie jest"
                zyd "Nie będę wykorzystywał jego ciała seksualnie"

                luszcz "Dobra niewarzne sory"
                luszcz "Nie pomogę ci grzebać w grobach arz tyle to nie"

                zyd "Smutne ale zrozumiałe"

                luszcz "Możesz sobie sam to zrobić, nikomu nie powiem"
                luszcz "Śmierć konfidentom"

                zyd "Nooo… zrobię, na pewno"
                zyd "pewnie"
                zyd "jasne"
                zyd "zobaczymy"
                zyd "Czas pokaże"

                hide zyd 
                show luszcz neutral at center

                luszcz "Freakass"

                $ zyd_social_link = 10
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
    
    label zyd3:
        scene bg cmentarz with fade
        play music "audio/music/natura.mp3"
        $ zyd_social_link = 3
        show zyd neutral right at slightright
        show luszcz neutral at left

        zyd "Szalom alehjem!"
        zyd "Rozejrzałem się, i myślę że dałbym radę wykopać tu ukryte przejście"
        zyd "Jestem jednak żałośnie spłukany… czy mógłbyś nabyć skądś coś do kopania?"

        menu:
            "{b}Tak{/b}":
                luszcz "Spoko git, wrócę tu z czymś do siedmiu dni roboczych"

                zyd "Yay"

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

            "{b}Nie{/b}":
                luszcz "nie"

                zyd "szkoda :("
                zyd "ale jak znajdziesz to przynieś"

                luszcz "okej"

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

    label zyd4:
        scene bg cmentarz with fade
        play music "audio/music/natura.mp3"
        $ zyd_social_link = 4
        show zyd neutral right at slightright
        show luszcz neutral at left

        zyd "Szalom, przyniosłeś coś do kopania?"

        luszcz "Ano mam"

        $ ile_item_fabularne -= 1
        $ lopatka = 0

        zyd "Ah! Łopatka! Wyśmienicie!"
        zyd "Czas wziąć się do roboty!"

        "{i}<kopu kopu kopu kopu…>{/i}"
        "{i}<kopu kopu kopu kopu…>{/i}"
        "{i}<kopu kopu kopu kopu…>{/i}"
        "{i}<kopu kopu kopu kopu…>{/i}"
        "{i}<kopu kopu kopu kopu…>{/i}"

        zyd "Gotowe!"

        luszcz "Fajny entuzjazm na chwilę go skopiuję"
        luszcz "To co? Wchodzimy?"

        zyd "Jeszcze jak!"

        scene bg lethal1
        stop music
        luszcz "Alerz ciemnica"

        zyd "Wejdźmy głębiej, może znajdziemy jakieś światło"

        luszcz "Czekaj, serjo nie wziąłeś latarki?"

        zyd "Nie stać mnie na takie przywileje"

        luszcz "Dobrze, to szukajmy po ciemku"

        ""

        zyd "O, czekaj, tu coś jest!"

        play sound "audio/sfx/light_on.mp3"
        "{i}*pstryk*{/i}"

        scene bg lethal2
        show zyd neutral right at slightright
        show luszcz neutral at slightleft
        play music "audio/music/lethal.mp3"
        

        zyd "Ja cie"
        zyd "Nie spodziewałem się takiej przestrzeni"

        luszcz "To twój pierwszy raz?"
        luszcz "Ja miałem już okazję eksplorować podziemne urbeksy"

        zyd "To może ty prowadź"
        zyd "Powiem gdy coś będzie wyglądało jak pra pra dziadek"

        luszcz "btw. Skąd wierz jak wygląda? Masz jakieś stare zdjęcia czy coś?"

        zyd "Nie. Ale wyczuję jego aurę"
        zyd "Nie martw się, umiem wyczuć swoich braci"

        luszcz "hm… okej"
        luszcz "gdzie iść?"

        label lethalc1:
            $ config.menu_include_disabled = False
            $ config.menu_include_disabled = True
            scene bg lethal2
            show zyd neutral right at slightright
            show luszcz neutral at slightleft
            menu:
                "{b}Przód{/b}":
                    play sound "audio/sfx/walk.mp3"
                    jump lethalc2
                
                "{b}Lewo{/b}" if lethalc12 == 0:
                    scene bg lethal3
                    play sound "audio/sfx/door.mp3"
                    queue sound "audio/sfx/walk.mp3"
                    show loli at center
                    zyd "Nic tu nie ma"
                    luszcz "Bez sensu"
                    $ lethalc12 = 1
                    play sound "audio/sfx/walk.mp3"
                    queue sound "audio/sfx/door2.mp3"
                    jump lethalc1
                
                "{b}Prawo{/b}" if lethalc13 == 0 or gaz == 0:
                    play sound "audio/sfx/walk.mp3"
                    if gaz == 1:
                        play music "audio/music/gaz.mp3"
                        scene bg lethal4
                        zyd "Ja tu nie wchodzę…"
                        $ lethalc13 = 1
                        play music "audio/music/lethal.mp3"
                        play sound "audio/sfx/walk.mp3"
                        jump lethalc1
                    else:
                        $ config.menu_include_disabled = False
                        scene bg lethal13
                        show zyd neutral right at slightright
                        show luszcz neutral at slightleft
                        luszcz "O patrz drzwi"

                        zyd "patrzę"

                        play sound "audio/sfx/door.mp3"
                        queue sound "audio/sfx/walk.mp3"

                        scene bg lethal14
                        
                        show luszcz neutral:
                            xalign 0.05
                            yalign 1.0
                        show zyd neutral at left:
                            xalign -0.2
                            yalign 1.0

                        zyd "To jest jak jakiś zakład psychiatryczny…"

                        luszcz "No dosłownie to jest jak w Choroszczy"
                        luszcz "Mam flashbacki…"

                        hide luszcz
                        play sound "audio/sfx/jump.mp3"
                        "{i}.{/i}"
                        "{i}.{/i}"
                        "{i}.{/i}"
                        play sound "audio/sfx/jump.mp3"
                        show luszcz neutral right:
                            xalign 1.2
                            yalign 1.0

                        luszcz "o"
                        luszcz "nie spadnij przypadkiem"

                        hide zyd
                        play sound "audio/sfx/jump.mp3"
                        ""
                        play sound "audio/sfx/jump.mp3"
                        show zyd neutral right:
                            xalign 0.999
                            yalign 1.0

                        zyd "Okej"

                        play sound "audio/sfx/walk.mp3"

                        scene bg black with fade

                        "{i}dużo chodzenia dalej…{/i}"

                        scene bg lethal15 with fade
                        play sound "audio/sfx/walk.mp3"
                        show zyd neutral right at slightright
                        show luszcz neutral at slightleft

                        luszcz "Ale tu jasno i ciepło"
                        zyd "Ej przyjacielu"
                        zyd "Czuję go…"
                        zyd "To musi być on"

                        luszcz "Gdzie?"

                        zyd "Tu, na ścianie"
                        zyd "Nigdy nie czułem czyjejś obecności tak mocno… to musi być on"

                        luszcz "Mam wrażenie że to promieniowanie"

                        scene bg lethal16
                        show zyd lampa right at slightright
                        show luszcz neutral at slightleft
                        play sound "audio/sfx/lampa.mp3"

                        luszcz "O boże ty na serio"

                        zyd "Nie na niby"
                        zyd "Dobra teraz ja prowadzę, trzymaj się blisko"

                        play sound "audio/sfx/walk.mp3"

                        scene bg black with fade

                        "{i}dużo chodzenia dalej…?{/i}"

                        scene bg lethal17 with fade
                        play sound "audio/sfx/walk.mp3"
                        show zyd lampa at slightleft
                        show luszcz neutral at left

                        luszcz "Ciemno tu jak w dupie murzyna"

                        zyd "Ej bo widzę jakieś oczy"

                        luszcz "Gdzie?"

                        zyd "Dobra teraz już nie"

                        show czarny neutral at slightright
                        $ renpy.pause(1.5)

                        $ zyd_sojusznik = 1
                        $ liczba_sojusznikow += 1

                        jump fight41
                                      
            
        label lethalc2:
            $ config.menu_include_disabled = False
            $ config.menu_include_disabled = True
            scene bg lethal5
            show zyd neutral right at slightright
            show luszcz neutral at slightleft
            menu:
                "{b}Przód{/b}" if lethalc21 == 0:
                    play sound "audio/sfx/walk.mp3"
                    scene bg lethal11
                    zyd "Spójrz klucz!"

                    luszcz "wow jakoś dziwnie blisko"
                    luszcz "Bieremy"

                    play sound "audio/sfx/grab_key.mp3"

                    scene bg lethal12

                    $ ile_item_fabularne += 1
                    $ klucz = 1
                    "{i}*Klucz został dodany do ekwipunku*{/i}"

                    play sound "audio/sfx/yippee.mp3"
                    queue sound "audio/sfx/yippee.mp3" fadein 1.0

                    show yippee1 neutral at slightright
                    show yippee2 neutral at slightleft

                    zyd "Ej robale się na nas patrzą"
                    luszcz "Dobra przejdź spokojnie naokoło"

                    show yippee1 zly at slightright
                    show yippee2 zly at slightleft
                    play sound "audio/sfx/yippee1_weapon.mp3"
                    $ renpy.pause(1.5)

                    $ zyd_sojusznik = 1
                    $ liczba_sojusznikow += 1
                    $ config.menu_include_disabled = False
                    jump fight31
                    
                    label after_fight31:
                        scene bg lethal12
                        play music "audio/music/lethal.mp3"
                        luszcz "skurczybyki"
                        $ zyd_sojusznik = 0
                        $ liczba_sojusznikow -= 1
                        $ lethalc21 = 1
                        play sound "audio/sfx/walk.mp3"
                        jump lethalc2

                
                "{b}Lewo{/b}" if lethalc22 == 0 or klucz == 1 and lethalc22 <= 1:
                    scene bg lethal6
                    play sound "audio/sfx/walk.mp3"
                    if klucz == 0: 
                        zyd "Bez klucza nie da rady..."
                        $ lethalc22 = 1
                        play sound "audio/sfx/walk.mp3"
                        jump lethalc2
                    else:
                        scene bg lethal6
                        queue sound "audio/sfx/key.mp3"
                        $ klucz = 0
                        $ ile_item_fabularne -= 1
                        "{i}*otwieracie drzwi za pomocą klucza*"
                        play sound "audio/sfx/door.mp3"
                        scene bg lethal7

                        luszcz "O patż znak drogowy!"

                        scene bg lethal8
                        play sound "audio/sfx/grab_stop.mp3"

                        "{i}*Łuszcz podnosi znak drogowy*{/i}"

                        luszcz "Wydaje mi się rze dobrze by działał jako broń…"

                        $ stop = 1
                        "{i}*Znak drogowy został dodany do ekwipunku*{/i}"

                        zyd "hel je"
                        zyd "szkoda że nic tu dalej nie ma"
                        play sound "audio/sfx/walk.mp3"

                        $ lethalc22 = 2
                        jump lethalc2

                
                "{b}Prawo{/b}" if lethalc23 == 0:
                    play sound "audio/sfx/walk.mp3"
                    scene bg lethal9
                    play music "audio/music/gaz.mp3"
                    luszcz "Ale tu dymi…"

                    zyd "Czekaj widzisz to koło?"
                    zyd "Chyba z niego gaz się puścił, spróbuję je zakręcić"
                    zyd "mmmmmmggggghghhhhhhghghghhhhmhmhmmmmmmhmhmh"

                    play sound "audio/sfx/gaz_stop.mp3"
                    play music "audio/music/lethal.mp3"

                    scene bg lethal10
                    $ gaz = 0
                    $ lethalc23 = 1

                    zyd "cyk udało się"

                    luszcz "najs"
                    luszcz "łał, tó też nic nie ma"

                    play sound "audio/sfx/walk.mp3"

                    jump lethalc2
                
                "{b}Powrót{/b}":
                    play sound "audio/sfx/walk.mp3"
                    jump lethalc1

        label after_fight41:  
            scene bg lethal17  
            show zyd lampa at slightleft
            show luszcz neutral at left
            show czarny neutral at slightright
            $ zyd_sojusznik = 0
            $ liczba_sojusznikow -= 1

            zyd "Czuję pulsującą nienawiść wobec tego czegoś"

            luszcz "O czym ty muwisz"
            luszcz "To weź na to poświedź zobatczmy co to"
            zyd "Dobra"

            play sound "audio/sfx/light_on.mp3"

            show czarny true at slightright

            luszcz "O kurcze adolf hitler"

            zyd "Chyba go sobie wezmę na pamiątkę"

            luszcz "Super pomysł"
            luszcz "Dobra chodźmy stąd"

            play sound "audio/sfx/walk.mp3"
            
            scene bg cmentarz
            show zyd lampa right at slightright
            show luszcz neutral at slightleft

            zyd "Bracie złowiliśmy dwie porządne rybunie"
            zyd "Dzięki twojej pomocy mój pra pra dziadek może spać spokojnie"
            zyd "A Fuhrer wisieć zamiast liści"
            zyd "Czy mógłbym w jakiś sposób ci się odpłacić?"

            menu:
                "{b}akszuli...{b}":
                    luszcz "W zasadzie to tak"
                    luszcz "Widzialem jak dobrze radzisz sobie w walce, nie chciałbys może pomóc mi w walce z ksiendzem który chce włonczyć Skałę do Krakowa?"

                    zyd "Włączenie Skały do Krakowa? To okropne!"
                    zyd "Biedne prywatne biznesy… miasto wszystko ukradnie i zbezcześci"
                    zyd "Nawet mi się zrobiło żal pana Brauna…"
                    zyd "Oczywiście że do ciebie dołączę!"

                    luszcz "Wybornie"

                    $ zyd_sojusznik = 1
                    $ liczba_sojusznikow += 1
                    $ zyd_wybory = 2
                
                "{b}Nie trzeba{/b}":
                    luszcz "Naprawdę nie musisz mi sie odpłacać w żaden sposób"

                    zyd "Na pewno?"
                    zyd "cóż jeśli kiedyś będziesz potrzebował pomocy to możesz na mnie liczyć"

                    hide zyd
                    $ zyd_wybory = 2
                    show luszcz neutral at center

                    luszcz "..."
                
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







