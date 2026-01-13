label zyd:
    label zyd1:
        $ zyd_social_link = 1
        play music "audio/music/monopolowy.mp3"
        scene bg monopolowy
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

            luszcz "Dowidzenia Panie Braun"

            braun "Żegnam pana"

            play music "audio/music/pole.mp3"

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
            jump alejka
    
    label zyd2:
        scene bg cmentarz_zydowski
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

                play music "audio/music/pole.mp3"
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
                play music "audio/music/pole.mp3"
                jump lipowa
    
    label zyd3:
        scene bg cmentarz
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

                play music "audio/music/pole.mp3"
                jump lipowa

            "{b}Nie{/b}":
                luszcz "nie"

                zyd "szkoda :("
                zyd "ale jak znajdziesz to przynieś"

                luszcz "okej"

                play music "audio/music/pole.mp3"
                jump lipowa

    label zyd4:
        scene bg cmentarz
        play music "audio/music/natura.mp3"
        $ zyd_social_link = 4
        show zyd neutral right at slightright
        show luszcz neutral at left

        zyd "Szalom, przyniosłeś coś do kopania?"

        luszcz "Ano mam"

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


