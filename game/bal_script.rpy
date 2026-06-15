default stol = 0
default eminem_gadka = 0
default kazuma_gadka = 0
default yusuke_gadka = 0
default zyd_gadka = 0
default urban_gadka = 0
default tarczownik_gadka = 0
default gadka = 0
default l1 = 0

default bomba = 1
default urban_spotkanie = 0
default alko_lvl = 0
default bralus = 0

default btask1 = 0
default btask2 = 0
default btask3 = 0
default btask4 = 0

default zapro = 0

define fastfade = Fade(0.35, 0.0, 0.35)

default putinp = 0
default kalachp = 0
default maciakp = 0

label bal:
    label bal1:
        $ zapro = 1
        hide screen secret_choice
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
        $ timer = 9870
        stop music
        scene bg black with fade

        $ renpy.pause(0.5)

        scene bg bal1 with fade
        play music "audio/music/bal.mp3"
        $ renpy.music.set_volume(0.25, delay=0.3)
        show luszcz bal at slightleft
        show tata neutral at slightright

        luszcz "Łooo, tatek nie mówiłeś, że to aż tak ekstrawagancko będzie!"

        tata "No widzisz synek, ma się układy (cała Skała została zaproszona btw)"

        luszcz "(hmmm może jednak ten Bal nie będzie taki zły...)"

        tata "To co wchodzimy?"

        scene bg bal2 with fade
        $ renpy.music.set_volume(0.5, delay=0.3)
        show luszcz bal at slightleft
        show tata neutral at slightright

        luszcz "Dobry Wieczór wszystkim!!!!!!"

        show shinobu neutral at center
        show luszcz bal at left
        show tata neutral at right

        shinobu "Nie drzyj japy tak, nie jesteś tutaj sam!"

        luszcz "O jezu tate, nie mówiłeś, że lecimy na wyspę!!!"

        luszcz "O kurczaczki eeee yyy ile masz lat piękna?"
        luszcz "Albo nie chwila, nie odpowiadaj, lepiej żebym nie wiedział, by móc się bronić w sądzie, że ja nie chcioł ja nie wiedział!"

        shinobu "Jezus maria kolejny pedofil się znalazł!"
        shinobu "Wszyscy chłopcy w twoim wieku tak reagują, gdy widzą LEKKO niższą kobietę?"

        luszcz "jak to wszyscy?"

        shinobu "A i tak dla twojej świadomości to ja mam ponad 500 lat!"

        luszcz "WHAT??? 🤯🤯🤯"

        show shinobu neutral right

        shinobu "Panie tato Łuszcza, Pana na pańskie miejsce odprowadzi moja hmmmm “przyjaciółka” Akane."

        show shinobu neutral right:
            xalign 0.35
            yalign 1.0
        show akane neutral:
            xalign 0.65
            yalign 1.0
        show luszcz bal at left
        show tata neutral at right

        akane "Dzień dobry, to ja pana odprowadzę na miejsce."

        tata "To będzie zaszczyt."
        tata "Synu, nie nabrój niczego, jasne?"

        luszcz "Tak tato, nic nie narozrabiam."

        tata "Dobrze"
        tata "Możemy iść"

        hide tata
        hide akane 

        show shinobu neutral at slightright
        show luszcz bal at slightleft

        shinobu "No cóż, mi przypada “zaszczyt” odprowadzenia CIEBIE do miejsca, bo mój pan stwierdził, że przez mój wygląd świetnie nadam się do NIAŃCZENIA DZIECI"

        luszcz "..."
        luszcz "sory pani loli, ale ja nie rozróżniam loli od dzieci..."

        shinobu "Idź nie gadaj!"

        scene bg black with fade
        scene bg bal3 with fade
        $ renpy.music.set_volume(1.0, delay=0.3)

        if eminem_sojusznik == 1:
            $ stol += 1
            show eminem stol zorder 10

        if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
            $ stol += 1
            show kazuma stol zorder 9

        if yusuke_social_link >= 1 and yusuke_social_link < 6:
            $ stol += 1
            show yusuke stol zorder 8

        if zyd_sojusznik == 1:
            $ stol += 1
            show zyd stol zorder 7

        if urban_sojusznik == 1:
            $ stol += 1
            show urban stol zorder 6

        if tarczownik_sojusznik == 1:
            $ stol += 1
            show tarczownik stol zorder 5
        
        show luszcz bal zorder 12 at left
        show shinobu neutral zorder 12 at center

        shinobu "Te pedofil"

        luszcz "co?"

        shinobu "Gówno"
        shinobu "To po pierwsze"
        shinobu "A po drugie"
        shinobu "To twoje miejsce"

        if stol == 0:
            luszcz "Emmmm, a yyy kto będzie siedział przy tym stole oprócz mnie?"

            shinobu "nikt, ha ha ha jesteś takim przegrywem, że nie masz przyjaciół więc siedzisz sam XD XD XD"

            luszcz "smutne"

            shinobu "smutne, ale prawdziwe"

            luszcz "..."

            shinobu "dobra to ja spadam, nie zepsuj niczego!"

            luszcz "yhym"

            hide shinobu
            show luszcz bal zorder 12 at slightleft    

            luszcz "No cóż chyba nie pozostaje mi nic innego jak usiąść"

            hide luszcz bal

            show luszcz stol zorder 11

            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "on nie mógł wiedzieć..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "gdyby wiedział to by powstrzymał przecież..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "Tak! Adolf Hitler jest niewinny!"

            $ renpy.music.set_volume(0.0, delay=0.3)
            scene bg black with fade
            "{i}*15 minut później*{/i}"
            $ timer += 15

            scene bg bal3 with fade
            $ renpy.music.set_volume(1.0, delay=0.3)
            show luszcz stol zorder 11

            luszcz "Stalin pewnie też nie wiedział..."

            luszcz "..."

            play sound "audio/sfx/mik.mp3"

            shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
            shinobu "dobra mikrofon działa"
            shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

            nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

            shinobu "ahhh ale"

            nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

            shinobu "no okeej"

            shinobu "eee to więc"
            shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali balowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
            
            nikt "Shinobu!!!"

            shinobu "No tak, wiem wiem"
            shinobu "...gdzie się znajdujecie nasi najszanowniejsi goście ❤️!"
            shinobu "Mój Pan wygłosi tam przemówienie po, którym wszyscy będziecie płakać, bo jak nie..."

            nikt "Dobrze już, już wystraczy"

            all "..."

            luszcz "..."
            luszcz "No cóż, czas się udać na rozpoczęcie Balu!"
    
        else:
            if stol == 1:
                if eminem_sojusznik == 1:
                    luszcz "Hej Cid!"

                    cid "Cześć Łuszczu"

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    luszcz "Hej Kazuma!"

                    kazuma "Nazywam się Kazuma."

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    luszcz "Hej Yusuke!"

                    yusuke "Witaj Łuszczu"

                if zyd_sojusznik == 1:
                    luszcz "Szalom alejchem!"

                    zyd "Alejchem szalom"

                if urban_sojusznik == 1:
                    luszcz "Cześć Urban!"

                    urban "Witam Łuszczu"

                if tarczownik_sojusznik == 1:
                    luszcz "Hej Naofumi!"

                    tarczownik "Witam Łuszczu"
                
                shinobu "no to ja sobie spadam, naura"
                hide shinobu
                show luszcz bal zorder 12 at slightleft  

                luszcz "Emmm to ja sobie usiąde..."

                hide luszcz bal

                show luszcz stol zorder 11  

                luszcz "Ohhh, od razu wygodniej"

                if eminem_sojusznik == 1:
                    luszcz "To mów Cid co tam u Ciebie!?"

                    cid "A po staremu!"
                    cid "Ręki jak nie było tak nie ma."

                    luszcz "Jezu aaaa sory sory sory ja nie chciał, nie bądź już taki wież ze cie mega lubie i nie zrobiłbym czegos takiego specjalnie!?!?!?!??!"

                    cid "Yhy napewno"

                    cid "(A mialem być nareszcie niepokonany... po tylu latach treningu)"

                    luszcz "sory, przepraszam"

                    cid "Nie no stary wszystko jest git"

                    luszcz "TAK?"

                    cid "NIE!"

                    luszcz "..."

                    cid "..."

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    luszcz "To mów Kazuma co tam u Ciebie!?"
                    luszcz "Gonił cię urząd skarbowy od naszego ostatniego spotkania?"

                    kazuma "Emmm, naszczęście nie"

                    luszcz "To świetnie wieźci!"
                    luszcz "A kiedy się wyprowadzasz?"

                    kazuma "emmm no nie wiem no daj jeszcze chwilke"

                    luszcz "Kazuma! Jesteś dorosłym mężczyzną i musisz w końcu wyprowadzić się na swoje!"

                    kazuma "Tak wiem tatooo"

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    luszcz "To mów Yusuke co tam u Ciebie!?"

                    yusuke "Maluje obraz!"

                    luszcz "To wiem, a coś innego robisz?"

                    yusuke "Emmmm maluje obraz?"

                    luszcz "A coś innego OPRÓCZ MALOWANIA robisz!?"

                    yusuke "hmmmmmm"

                    luszcz "..?"

                    yusuke "Wiem! Już wiem co robię innego!"

                    luszcz "co?"

                    yusuke "Myślę!"

                    luszcz "Oooo a nad czym myślisz?"

                    yusuke "Nad obrazem!!!"

                    luszcz "japididi!"

                if zyd_sojusznik == 1:
                    luszcz "To mów Żydzie co tam u Ciebie!?"
                    luszcz "Prześladują cię narodowcy?"

                    zyd "Ahhh czasami się zdaża..."
                    zyd "I pan Braun groźnie na mnie patrzy, gdy mijam go na ulicy..."
                    zyd "I raz jak się modliłem to dzieci zaczeły mnie obrzucać gównem"
                    zyd "O o i była też taka sytuacja, że kilku kiboli powiesiło mnie na szaliku pod mostem i wisiałem tak przez kilka dni i dopiero mega wichura mnie zwiała."
                    zyd "A i byłbym zapomniał, kiedyś jeszcze taki Niemiec..."

                    luszcz "DOŚĆ!"
                    luszcz "Nie ja już nie chce słuchać"

                    zyd "..."

                    luszcz "..."

                if urban_sojusznik == 1:
                    $ urban_spotkanie = 1
                    luszcz "To mów Urban co tam u Ciebie!?"

                    urban "Ahh w porządeczku!"
                    urban "Od kiedy umarli moi przeciwnicy z PZPRu moje wpływy drastycznie wzrosły"
                    urban "Nawet ostatnio udało mi się przeprowadzić moją właśną osobistą czystkę w partii!"

                    luszcz "Eeee gratuluje, jej ale super!"
                    luszcz "A jakieś plany na przyszłość?"

                    urban "Ależ oczywiście!"
                    urban "Planuję odmłodzenie kadr, aby zwiększyc konkurencyjność PRL (i zwiększyc moje wpływy)"
                    urban "Oraz planuję rozszerzyć jego wpływy!"

                    urban "A właśnie, co do tego to ma do Ciebie sprawę."
                    
                    luszcz "Jaką?"

                    urban "Nie tutaj, przyjdź po 1 w nocy do toalety to to obgadamy"

                    luszcz "Oke doke, spróbuję nie zapomnieć"

                    urban "Trzymam cię za słowo"

                    luszcz "..."

                    urban "..."

                if tarczownik_sojusznik == 1:
                    luszcz "To mów Naofumi co tam u Ciebie!?"

                    tarczownik "nic mój piesek nadal nie wrócił, a życie nie ma sensu"

                    luszcz "oj tam, oj tam nie może być tak źle"

                    tarczownik "każdego wieczoru przed spaniem wyciągam gnata i przykładam go sobie do głowy mając nadzieję, że mój palec się ześlizgnie i zakończy me bezwartościowe życie "

                    luszcz "Jezus maria!"
                    luszcz "Aeeee próbowałeś z tym iść do terapeuty!?"

                    tarczownik "kiedyś byłem u terapeuty z jakąś inną sprawą, ale po 3 wspólnych sesjach znaleźli go martwego we własnym mieszkaniu"
                    tarczownik "prawdopodbnie popelnił seppuku kręgosłupem swojego dziecka, które wcześniej zabił"
                    
                    luszcz "Japierdole"
                    luszcz "Ja nie chcę tu być"

                    tarczownik "A i zapomniałem dodać, że..."
                
                $ renpy.music.set_volume(0.0, delay=0.3)
                scene bg black with fade
                "{i}*15 minut później*{/i}"
                $ timer += 15

                scene bg bal3 with fade
                show luszcz stol zorder 11
                if eminem_sojusznik == 1:
                    show eminem stol zorder 10

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    show kazuma stol zorder 9

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    show yusuke stol zorder 8

                if zyd_sojusznik == 1:
                    show zyd stol zorder 7

                if urban_sojusznik == 1:
                    show urban stol zorder 6

                if tarczownik_sojusznik == 1:
                    show tarczownik stol zorder 5

                $ renpy.music.set_volume(1.0, delay=0.3)

                        
                luszcz "(Emmmm zaczynają już oni te impreze czy co)"
                luszcz "(ja już nie chcem tótaj siedźiedź)"

                play sound "audio/sfx/mik.mp3"

                shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
                shinobu "dobra mikrofon działa"

                shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

                nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

                shinobu "ahhh ale"

                nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

                shinobu "no okeej"

                shinobu "eee to więc"
                shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali balowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
                
                nikt "Shinobu!!!"

                shinobu "No tak, wiem wiem"
                shinobu "...gdzie się znajdujecie nasi najszanowniejsi goście ❤️!"
                shinobu "Mój Pan wygłosi tam przemówienie po, którym wszyscy będziecie płakać, bo jak nie..."

                nikt "Dobrze już, już wystraczy"

                all "..."

                luszcz "..."
                luszcz "No cóż, czas się udać na rozpoczęcie Balu!"

            else:
                luszcz "Hej chłopaki!"

                if eminem_sojusznik == 1:
                    cid "Cześć Łuszczu"

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    kazuma "Hejo Łuszczu"

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    yusuke "Witaj Łuszczu"

                if zyd_sojusznik == 1:
                    zyd "Szalom alejchem!"

                if urban_sojusznik == 1:
                    urban "Witam Łuszczu"

                if tarczownik_sojusznik == 1:
                    tarczownik "Hej Łuszczu"
                
                shinobu "no to ja sobie spadam, naura"
                hide shinobu
                show luszcz bal zorder 12 at slightleft    

                luszcz "Emmm to ja sobie usiąde..."

                hide luszcz bal

                show luszcz stol zorder 11  

                luszcz "Ohhh, od razu wygodniej"
                luszcz "..."
                luszcz "(Z kim tu pogadać?)"

                label gadanko:
                    menu:
                        "{b}Z kim pogadać?{/b}"

                        "{b}Cid{/b}" if eminem_sojusznik == 1 and eminem_gadka == 0:
                            $ eminem_gadka = 1
                            $ gadka += 1
                            luszcz "To mów Cid co tam u Ciebie!?"

                            cid "A po staremu!"
                            cid "Ręki jak nie było tak nie ma."

                            luszcz "Jezu aaaa sory sory sory ja nie chciał, nie bądź już taki wież ze cie mega lubie i nie zrobiłbym czegos takiego specjalnie!?!?!?!??!"

                            cid "Yhy napewno"

                            cid "(A mialem być nareszcie niepokonany... po tylu latach treningu)"

                            luszcz "sory, przepraszam"

                            cid "Nie no stary wszystko jest git"

                            luszcz "TAK?"

                            cid "NIE!"

                            luszcz "..."

                            cid "..."

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                jump gadanko


                        "{b}Kazuma{/b}"if kazuma_social_link >= 1 and kazuma_social_link < 3 and kazuma_gadka == 0 or kazuma_sojusznik == 1 and kazuma_gadka == 0:
                            $ kazuma_gadka = 1
                            $ gadka += 1

                            luszcz "To mów Kazuma co tam u Ciebie!?"
                            luszcz "Gonił cię urząd skarbowy od naszego ostatniego spotkania?"

                            kazuma "Emmm, naszczęście nie"

                            luszcz "To świetnie wieźci!"
                            luszcz "A kiedy się wyprowadzasz?"

                            kazuma "emmm no nie wiem no daj jeszcze chwilke"

                            luszcz "Kazuma! Jesteś dorosłym mężczyzną i musisz w końcu wyprowadzić się na swoje!"

                            kazuma "Tak wiem tatooo"

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                luszcz "..."
                                kazuma "..."
                                jump gadanko

                        "{b}Yusuke{/b}" if yusuke_social_link >= 1 and yusuke_social_link < 6 and yusuke_gadka == 0:
                            $ yusuke_gadka = 1
                            $ gadka += 1
                            luszcz "To mów Yusuke co tam u Ciebie!?"

                            yusuke "Maluje obraz!"

                            luszcz "To wiem, a coś innego robisz?"

                            yusuke "Emmmm maluje obraz?"

                            luszcz "A coś innego OPRÓCZ MALOWANIA robisz!?"

                            yusuke "hmmmmmm"

                            luszcz "..?"

                            yusuke "Wiem! Już wiem co robię innego!"

                            luszcz "co?"

                            yusuke "Myślę!"

                            luszcz "Oooo a nad czym myślisz?"

                            yusuke "Nad obrazem!!!"

                            luszcz "japididi!"

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                yusuke "..."
                                luszcz "..."
                                jump gadanko
                        
                        "{b}Żyd{/b}" if zyd_sojusznik == 1 and zyd_gadka == 0:
                            $ zyd_gadka = 1
                            $ gadka += 1
                            luszcz "To mów Żydzie co tam u Ciebie!?"
                            luszcz "Prześladują cię narodowcy?"

                            zyd "Ahhh czasami się zdaża..."
                            zyd "I pan Braun groźnie na mnie patrzy, gdy mijam go na ulicy..."
                            zyd "I raz jak się modliłem to dzieci zaczeły mnie obrzucać gównem"
                            zyd "O o i była też taka sytuacja, że kilku kiboli powiesiło mnie na szaliku pod mostem i wisiałem tak przez kilka dni i dopiero mega wichura mnie zwiała."
                            zyd "A i byłbym zapomniał, kiedyś jeszcze taki Niemiec..."

                            luszcz "DOŚĆ!"
                            luszcz "Nie ja już nie chce słuchać"

                            zyd "..."

                            luszcz "..."

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                jump gadanko
                        
                        "{b}Urban{/b}" if urban_sojusznik == 1 and urban_gadka == 0:
                            $ urban_gadka = 1
                            $ gadka += 1
                            $ urban_spotkanie = 1
                            luszcz "To mów Urban co tam u Ciebie!?"

                            urban "Ahh w porządeczku!"
                            urban "Od kiedy umarli moi przeciwnicy z PZPRu moje wpływy drastycznie wzrosły"
                            urban "Nawet ostatnio udało mi się przeprowadzić moją właśną osobistą czystkę w partii!"

                            luszcz "Eeee gratuluje, jej ale super!"
                            luszcz "A jakieś plany na przyszłość?"

                            urban "Ależ oczywiście!"
                            urban "Planuję odmłodzenie kadr, aby zwiększyc konkurencyjność PRL (i zwiększyc moje wpływy)"
                            urban "Oraz planuję rozszerzyć jego wpływy!"

                            urban "A właśnie, co do tego to ma do Ciebie sprawę."
                            
                            luszcz "Jaką?"

                            urban "Nie tutaj, przyjdź po 1 w nocy do toalety to to obgadamy"

                            luszcz "Oke doke, spróbuję nie zapomnieć"

                            urban "Trzymam cię za słowo"

                            luszcz "..."

                            urban "..."

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                jump gadanko
                        
                        "{b}Naofumi{/b}" if tarczownik_sojusznik == 1 and tarczownik_gadka == 0:
                            $ tarczownik_gadka = 1
                            $ gadka += 1

                            luszcz "To mów Naofumi co tam u Ciebie!?"

                            tarczownik "nic mój piesek nadal nie wrócił, a życie nie ma sensu"

                            luszcz "oj tam, oj tam nie może być tak źle"

                            tarczownik "każdego wieczoru przed spaniem wyciągam gnata i przykładam go sobie do głowy mając nadzieję, że mój palec się ześlizgnie i zakończy me bezwartościowe życie "

                            luszcz "Jezus maria!"
                            luszcz "Aeeee próbowałeś z tym iść do terapeuty!?"

                            tarczownik "kiedyś byłem u terapeuty z jakąś inną sprawą, ale po 3 wspólnych sesjach znaleźli go martwego we własnym mieszkaniu"
                            tarczownik "prawdopodbnie popelnił seppuku kręgosłupem swojego dziecka, które wcześniej zabił"
                            
                            luszcz "Japierdole"
                            luszcz "(Ja nie chcę tu być)"

                            tarczownik "A i zapomniałem dodać, że..."

                            if gadka == 3 or gadka == 2 and stol == 2:
                                jump pogadka
                            else:
                                luszcz "DOŚĆ!"

                                tarczownik "..."
                                jump gadanko
                    

                label pogadka:
                    $ renpy.music.set_volume(0.0, delay=0.3)
                    scene bg black with fade
                    "{i}*15 minut później*{/i}"
                    $ timer += 15

                    scene bg bal3 with fade
                    show luszcz stol zorder 11
                    if eminem_sojusznik == 1:
                        show eminem stol zorder 10

                    if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                        show kazuma stol zorder 9

                    if yusuke_social_link >= 1 and yusuke_social_link < 6:
                        show yusuke stol zorder 8

                    if zyd_sojusznik == 1:
                        show zyd stol zorder 7

                    if urban_sojusznik == 1:
                        show urban stol zorder 6

                    if tarczownik_sojusznik == 1:
                        show tarczownik stol zorder 5

                    $ renpy.music.set_volume(1.0, delay=0.3)

                            
                    luszcz "(Emmmm zaczynają już oni te impreze czy co)"
                    luszcz "(ja już nie chcem tótaj siedźiedź)"

                    play sound "audio/sfx/mik.mp3"

                    shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
                    shinobu "dobra mikrofon działa"

                    shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

                    nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

                    shinobu "ahhh ale"

                    nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

                    shinobu "no okeej"

                    shinobu "eee to więc"
                    shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali balowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
                    
                    nikt "Shinobu!!!"

                    shinobu "No tak, wiem wiem"
                    shinobu "...gdzie się znajdujecie nasi najszanowniejsi goście ❤️!"
                    shinobu "Mój Pan wygłosi tam przemówienie po, którym wszyscy będziecie płakać, bo jak nie..."

                    nikt "Dobrze już, już wystraczy"

                    all "..."

                    luszcz "..."
                    luszcz "No cóż, czas się udać na rozpoczęcie Balu!"

        scene bg bal4 with fade
        if stol == 0:
            show luszcz bal zorder 12 at center
        else:
            if stol == 1:
                show luszcz bal zorder 12 at slightleft

                if eminem_sojusznik == 1:
                    show eminem neutral zorder 5 at slightright

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    show kazuma neutral zorder 5 at slightright

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    show yusuke neutral right zorder 5 at slightright

                if zyd_sojusznik == 1:
                    show zyd neutral right zorder 5 at slightright

                if urban_sojusznik == 1:
                    show urban neutral zorder 5 at slightright

                if tarczownik_sojusznik == 1:
                    show tarczownik neutral right zorder 5 at slightright
                
            else:
                show luszcz bal zorder 12 at center
                $ l1 = 0

                if eminem_sojusznik == 1:
                    $ l1 += 1
                    show eminem neutral zorder 5 at right

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    if l1 == 0:
                        show kazuma neutral zorder 5 at right
                    else:
                        if l1 == 1:    
                            show kazuma neutral right zorder 5 at left
                    $ l1 += 1

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    if l1 == 0:
                        show yusuke neutral right zorder 5 at right
                    else:
                        if l1 == 1:    
                            show yusuke neutral zorder 5 at left
                        
                        else:
                            if l1 == 2:    
                                show yusuke neutral right zorder 3 at slightright  
                    $ l1 += 1

                if zyd_sojusznik == 1:
                    if l1 == 0:
                        show zyd neutral right zorder 5 at right
                    else:
                        if l1 == 1:    
                            show zyd neutral zorder 5 at left
                        
                        else:
                            if l1 == 2:    
                                show zyd neutral right zorder 3 at slightright
                            else:
                                if l1 == 3:    
                                    show zyd neutral zorder 3 at slightleft
                    
                    $ l1 += 1

                if urban_sojusznik == 1:
                    if l1 == 0:
                        show urban neutral zorder 5 at right
                    else:
                        if l1 == 1:    
                            show urban neutral right zorder 5 at left
                        
                        else:
                            if l1 == 2:    
                                show urban neutral zorder 3 at slightright
                            else:
                                if l1 == 3:    
                                    show urban neutral right zorder 3 at slightleft   
                    $ l1 += 1

                if tarczownik_sojusznik == 1:
                    if l1 == 0:
                        show tarczownik neutral right zorder 5 at right
                    else:
                        if l1 == 1:    
                            show tarczownik neutral zorder 5 at left
                        
                        else:
                            if l1 == 2:    
                                show tarczownik neutral right zorder 3 at slightright
                            else:
                                if l1 == 3:    
                                    show tarczownik neutral zorder 3 at slightleft
                    $ l1 += 1
        
        if stol == 0:
            luszcz "Łooo, ale duża sala"
            luszcz "ciekawe, czy Trump, będzie miał większą..."
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "zaczną bo troche nudy"
            luszcz "..."
            luszcz "..."
            luszcz "..."
            luszcz "halooo dzisiaj?"

            play sound "audio/sfx/mik.mp3"

            shinobu "raz, dwa, trzy, raz, dwa, trzy!"

            luszcz "nareszcie!"

            shinobu "wszystko działa mistrzu, zaczynajmy!"

        else:
            if stol == 1:
                luszcz "Łooo, ale duża sala"
                luszcz "ciekawe, czy Trump, będzie miał większą..."

                if eminem_sojusznik == 1:
                    cid "pewnie tak choć i tak ta sala robi wrażenie"
                    cid "Mógłbym tu się bawić w eminecje w cieniu i zapraszać jakiś ważnych ludzi na spotkania czy coś"

                    luszcz "Nooo to, by było cool"

                    cid "edgy!"

                    luszcz "Tak dokładnie to słowo chciałem użyć!"
                    luszcz "edgy"

                    cid "..."
                    luszcz "..."
                    luszcz "niech zaczną bo troche nudy"

                    cid "real"

                    luszcz "..."
                    luszcz "..."
                    luszcz "..."
                    luszcz "halooo dzisiaj?"

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    kazuma "Ahhhh taka sala to by pokryła moje długi i to kilkaset razy..."
                    kazuma "A gdybym coś ukradł..."

                    luszcz "Kazuma! Zachowuj się!"

                    kazuma "tylko głośno myślę"

                    luszcz "To pomyśl o czymś innym!"

                    kazuma "..."
                    kazuma "..."

                    kazuma "Długo jeszcze!?"

                    luszcz "Mnie się pytasz!? Skąd mam wiedzieć!?"

                    kazuma "jezu sory"
                    kazuma "tylko zadałem pytanie"

                    kazuma "..."
                    kazuma "..."
                    kazuma "..."

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    yusuke "Ahhh, oby potrzebował do niej artystów!"
                    yusuke "Od razu, bym wyjechał do Ameryki!"

                    luszcz "Fuj Ameryka"

                    yusuke "No jest fuj to prawda"

                    yusuke "Ale posiadanie własnego dzieła w Białym Domu!?!?"

                    luszcz "Nie wiem czy to warte tej ceny..."
                    luszcz "btw to się nie wydarzy, więc cała dyskusja jest bezowocna"

                    yusuke "smutne"

                    luszcz "smutne, ale prawdziwe"

                    yusuke "..."

                    luszcz "..."
                    luszcz "Może, by zaczeli czy coś?"
                    
                    yusuke "true, niech już to zaczną i pozwolą mi malować"

                    luszcz "Bedziesz malował przemówienie!?"

                    yusuke "No tak! Przecież to taki podniosły moment!"

                    luszcz "wtf, w sensie rub co chceż"

                    yusuku "Dzięki mistrzu!"

                    luszcz "..."

                    yusuke "..."

                    luszcz "halooo dzisiaj?"

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"

                if zyd_sojusznik == 1:
                    zyd "Tyle pieniędzy, tyle pieniędzy na niego pójdzie!"
                    zyd "Ja bym je zainwestował!"
                    zyd "A nie wydawał na takie głupoty!"

                    luszcz "Dobrze gadasz, ja też"

                    zyd "Przecież jak chce robić imprezy to ma już od tego wyspę!"

                    luszcz "Dokładnie tak! Mega relujesz Żydzie!"

                    zyd "A po za tym, a po za tym..."

                    luszcz "A po za tym?"

                    zyd "a po za tym mam bombę i się zaraz wysadzę w imię państwa Izrael!"

                    luszcz "Jezus maria, gdzie?"

                    zyd "W dupie"

                    luszcz "Oddawaj ją natychmiast!"

                    zyd "Przykro mi, ale jeśli będziesz chciał mnie powstrzymać to musisz to zrobić własnoręcznie!"

                    luszcz "Awhhh shit!"

                    $ renpy.music.set_volume(0.0, delay=0.3)
                    scene bg black with fade
                    $ bomba = 2
                    "{i}Łuszczu ściągnął spodnie Żyda i wyciągnął z jego dupy bombę, a następnie ją rozbroił i włożył do swojej{/i}"

                    scene bg bal4 with fade
                    $ renpy.music.set_volume(1.0, delay=0.3)
                    show luszcz bal zorder 12 at slightleft
                    show zyd neutral right zorder 5 at slightright

                    luszcz "Ahhh, jak dobrze"

                    zyd "No mówiłem, że dobrze!"

                    luszcz "Ty już lepiej nic nie mów!"

                    zyd "..."

                    luszcz "..."

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"

                if urban_sojusznik == 1:
                    urban "Za starego dobrego PRL my też mieliśmy takie sale!"
                    urban "I organizowaliśmy sobie na nich bankiety"
                    urban "A potem wchodziła tajna policja i aresztowała tych, którzy zostali uznani za wrogów"
                    urban "No, ale jak to mówią ”Bez ryzyka nie ma zabawy”"

                    luszcz "he he..."
                    luszcz "A znasz taką gre planszową Ryzyko?"

                    urban "Nie, a co?"

                    luszcz "A no bo tam właśnie też się pozbywa wrogów"
                    luszcz "i jest ryzyko"
                    luszcz "i trzeba byc śliskim"

                    urban "crazy"
                    urban "musimy kiedyś zagrać"

                    luszcz "no"

                    urban "..."

                    luszcz "..."

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"

                if tarczownik_sojusznik == 1:
                    tarczownik "Nie wiem skąd mam wiedzieć"
                    tarczownik "Tak szczerze to ten cały Trump mnie gówno obchodzi!"

                    luszcz "ostro"
                    luszcz "tak kociaki lubią najbardziej"

                    tarczownik "..!?"

                    luszcz "nieważne"

                    tarczownik "..."

                    luszcz "..."

                    tarczownik "..."

                    luszcz "..."

                    luszcz "niech zaczną bo troche nudy"

                    tarczownik "no niech zaczną"

                    luszcz "..."
                    luszcz "..."
                    luszcz "..."
                    luszcz "halooo dzisiaj?"

                    play sound "audio/sfx/mik.mp3"

                    shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                    luszcz "nareszcie!"

                    shinobu "wszystko działa mistrzu, zaczynajmy!"
            
            else:
                luszcz "Łooo, ale duża sala"

                if eminem_sojusznik == 1:
                    cid "..."

                if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                    kazuma "..."

                if yusuke_social_link >= 1 and yusuke_social_link < 6:
                    yusuke "..."

                if zyd_sojusznik == 1:
                    zyd "..."

                if urban_sojusznik == 1:
                    urban "..."

                if tarczownik_sojusznik == 1:
                    tarczownik "..."
                
                luszcz "(hmmmm, powinienem wybrać z kim chce pogadać)"
                menu:
                    "{b}Z kim pogadać?{/b}"

                    "{b}Cid{/b}" if eminem_sojusznik == 1:
                        hide yusuke
                        hide kazuma 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show eminem neutral at slightright
                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        cid "pewnie tak choć i tak ta sala robi wrażenie"
                        cid "Mógłbym tu się bawić w eminecje w cieniu i zapraszać jakiś ważnych ludzi na spotkania czy coś"

                        luszcz "Nooo to, by było cool"

                        cid "edgy!"

                        luszcz "Tak dokładnie to słowo chciałem użyć!"
                        luszcz "edgy"

                        cid "..."
                        luszcz "..."
                        luszcz "niech zaczną bo troche nudy"

                        cid "real"

                        luszcz "..."
                        luszcz "..."
                        luszcz "..."
                        luszcz "halooo dzisiaj?"

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"

                    "{b}Kazuma{/b}" if kazuma_social_link >= 1 and kazuma_social_link < 3 or kazuma_sojusznik == 1:
                        hide yusuke
                        hide eminem 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show kazuma neutral at slightright

                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        kazuma "Ahhhh taka sala to by pokryła moje długi i to kilkaset razy..."
                        kazuma "A gdybym coś ukradł..."

                        luszcz "Kazuma! Zachowuj się!"

                        kazuma "tylko głośno myślę"

                        luszcz "To pomyśl o czymś innym!"

                        kazuma "..."
                        kazuma "..."

                        kazuma "Długo jeszcze!?"

                        luszcz "Mnie się pytasz!? Skąd mam wiedzieć!?"

                        kazuma "jezu sory"
                        kazuma "tylko zadałem pytanie"

                        kazuma "..."
                        kazuma "..."
                        kazuma "..."

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"

                    "{b}Yusuke{/b}" if yusuke_social_link >= 1 and yusuke_social_link < 6:
                        hide eminem
                        hide kazuma 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show yusuke neutral right at slightright

                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        yusuke "Ahhh, oby potrzebował do niej artystów!"
                        yusuke "Od razu, bym wyjechał do Ameryki!"

                        luszcz "Fuj Ameryka"

                        yusuke "No jest fuj to prawda"

                        yusuke "Ale posiadanie własnego dzieła w Białym Domu!?!?"

                        luszcz "Nie wiem czy to warte tej ceny..."
                        luszcz "btw to się nie wydarzy, więc cała dyskusja jest bezowocna"

                        yusuke "smutne"

                        luszcz "smutne, ale prawdziwe"

                        yusuke "..."

                        luszcz "..."
                        luszcz "Może, by zaczeli czy coś?"
                        
                        yusuke "true, niech już to zaczną i pozwolą mi malować"

                        luszcz "Bedziesz malował przemówienie!?"

                        yusuke "No tak! Przecież to taki podniosły moment!"

                        luszcz "wtf, w sensie rub co chceż"

                        yusuku "Dzięki mistrzu!"

                        luszcz "..."

                        yusuke "..."

                        luszcz "halooo dzisiaj?"

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"
                    
                    "{b}Żyd{/b}" if zyd_sojusznik == 1:
                        hide eminem
                        hide kazuma 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show zyd neutral right at slightright

                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        zyd "Tyle pieniędzy, tyle pieniędzy na niego pójdzie!"
                        zyd "Ja bym je zainwestował!"
                        zyd "A nie wydawał na takie głupoty!"

                        luszcz "Dobrze gadasz, ja też"

                        zyd "Przecież jak chce robić imprezy to ma już od tego wyspę!"

                        luszcz "Dokładnie tak! Mega relujesz Żydzie!"

                        zyd "A po za tym, a po za tym..."

                        luszcz "A po za tym!?"

                        zyd "a po za tym mam bombę i się zaraz wysadzę w imię państwa Izrael!"

                        luszcz "Jezus maria, gdzie?"

                        zyd "W dupie"

                        luszcz "Oddawaj ją natychmiast!"

                        zyd "Przykro mi, ale jeśli będziesz chciał mnie powstrzymać to musisz to zrobić własnoręcznie!"

                        luszcz "Awhhh shit!"

                        $ renpy.music.set_volume(0.0, delay=0.3)
                        scene bg black with fade
                        $ bomba = 2
                        "{i}Łuszczu ściągnął spodnie Żyda i wyciągnął z jego dupy bombę, a następnie ją rozbroił i włożył do swojej{/i}"

                        scene bg bal4 with fade
                        $ renpy.music.set_volume(1.0, delay=0.3)
                        show luszcz bal zorder 12 at slightleft
                        show zyd neutral right zorder 5 at slightright

                        luszcz "Ahhh, jak dobrze"

                        zyd "No mówiłem, że dobrze!"

                        luszcz "Ty już lepiej nic nie mów!"

                        zyd "..."

                        luszcz "..."

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"
                    
                    "{b}Urban{/b}" if urban_sojusznik == 1:
                        hide eminem
                        hide kazuma 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show urban neutral at slightright

                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        urban "Za starego dobrego PRL my też mieliśmy takie sale!"
                        urban "I organizowaliśmy sobie na nich bankiety"
                        urban "A potem wchodziła tajna policja i aresztowała tych, którzy zostali uznani za wrogów"
                        urban "No, ale jak to mówią ”Bez ryzyka nie ma zabawy”"

                        luszcz "he he..."
                        luszcz "A znasz taką gre planszową Ryzyko?"

                        urban "Nie, a co?"

                        luszcz "A no bo tam właśnie też się pozbywa wrogów"
                        luszcz "i jest ryzyko"
                        luszcz "i trzeba byc śliskim"

                        urban "crazy"
                        urban "musimy kiedyś zagrać"

                        luszcz "no"

                        urban "..."

                        luszcz "..."

                        if urban_spotkanie == 0:
                            $ urban_spotkanie = 1
                            urban "Ej mam do Ciebie sprawę."

                            luszcz "Jaką?"

                            urban "nie tutaj"
                            urban "Przyjdź do kibla po 1 w nocy"

                            luszcz "spróbuję"

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"
                    
                    "{b}Naofumi{/b}" if tarczownik_sojusznik == 1:
                        hide eminem
                        hide kazuma 
                        hide zyd
                        hide urban 
                        hide tarczownik 
                        show luszcz bal at slightleft
                        show tarczownik neutral at slightright

                        luszcz "ciekawe, czy Trump, będzie miał większą salę?"

                        tarczownik "Nie wiem skąd mam wiedzieć"
                        tarczownik "Tak szczerze to ten cały Trump mnie gówno obchodzi!"

                        luszcz "ostro"
                        luszcz "tak kociaki lubią najbardziej"

                        tarczownik "..!?"

                        luszcz "nieważne"

                        tarczownik "..."

                        luszcz "..."

                        tarczownik "..."

                        luszcz "..."

                        luszcz "niech zaczną bo troche nudy"

                        tarczownik "no niech zaczną"

                        luszcz "..."
                        luszcz "..."
                        luszcz "..."
                        luszcz "halooo dzisiaj?"

                        play sound "audio/sfx/mik.mp3"

                        shinobu "raz, dwa, trzy, raz, dwa, trzy!"

                        luszcz "nareszcie!"

                        shinobu "wszystko działa mistrzu, zaczynajmy!"

        scene bg bal5 with fade
        show shinobu neutral right at center
        shinobu "emmhmm proszę wszystkich o łaskawe zamknięcie mordy!"

        nikt "!"

        shinobu "no o uciszenie się, jezu to samo"

        stop music

        shinobu "no"

        show eryk neutral at right 

        eryk "zaczynajmny w takim razie"

        show eryk neutral at center
        show shinobu neutral right at left 

        eryk "Szanowni Państwo!"
        eryk "Witam was serdecznie na Balu Ambosadora Japonii w Polsce!"

        play sound "audio/sfx/klask.mp3"

        all "brawo, brawo, brawo"

        eryk "Zorganizowanie tego Balu oraz zaproszenie na niego mieszkańców tak znakomitego miasta jak Skała stanowi dla mnie ogromny zaszczyt!"

        play sound "audio/sfx/klask.mp3"

        all "brawo, brawo, brawo"

        eryk "Skała to świetny symbol przemiany jaką po 1989 roku przeszła Polska!"

        play sound "audio/sfx/klask.mp3"

        all "brawo, brawo, brawo"

        eryk "Kiedyś tu nie było nic, zero, a teraz? "
        eryk "Teraz jest tu kasyno!"

        play sound "audio/sfx/klask.mp3"

        all "brawo, brawo, brawo"

        luszcz "(Jezus maria, czuję się jak w Korei)"

        eryk "Ale wracając do tematu"
        eryk "Dziś na tym Balu, w tym symbolicznym miejscu jakim jest Skała, Polska i Japonia podpiszę nową umowę gospodarczą, która wzmocni gospodarki obydwu naszych wspaniałych krajów!"

        play sound "audio/sfx/klask.mp3"

        all "brawo, brawo, brawo"

        eryk "Dlatego teraz poprosiłbym o głos premiera Polski, Donalda Tuska!"

        show tusk neutral at right
        tusk "Dziękuję Panie Ambasadorze"

        show tusk neutral:
            xalign 0.6
            yalign 1.0
        show eryk neutral right zorder 1 at left
        show shinobu neutral right zorder 2:
            xalign 0.1
            yalign 1.0

        tusk "Guten Tag wszyscy!"
        tusk "Zebraliśmy się tutaj, aby rozpocząć całkowicie nowy rozdział w histori Polski!"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        tusk "Dzięki wynegocjowanemu przezemnie dealu z Japonią, Polska zyska, dużo zyska i nic nie straci!"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        tusk "Dlatego, prosze głosujcie na KO w kolejnych wyborach UwU"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        tusk "Dziękuję to wszystko"

        hide tusk
        show eryk neutral right zorder 1 at center
        show shinobu neutral right zorder 2 at left

        eryk "Dziękuję bardzo za te ciepłe słowa."
        eryk "A teraz poprosiłbym prezydenta Karola Nawrockiego o zabranie głosu"

        show nawrocki neutral at right
        nawrocki "Dziękuję Panie Ambasadorze"

        show nawrocki neutral:
            xalign 0.6
            yalign 1.0
        show eryk neutral right zorder 1 at left
        show shinobu neutral right zorder 2:
            xalign 0.1
            yalign 1.0

        nawrocki "Drodzy państwo!"
        nawrocki "Tusk niszczy Polskę i wszyscy to wiemy!"
        nawrocki "I tak również było w przypadku tej umowy gospodarczej z Japonią!"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        nawrocki "Tusk tak naprawdę początkowo chciał zawrzeć umowę z Niemcami!"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        nawrocki "Jedynie me dzielne weto i sprawne negocjacje z Japonią pozwoliły, aby Polska zamiast ssać niemieckiego kutasa mogła ssać japońskiego!"

        play sound "audio/sfx/cisza.mp3"

        all "..."

        nawrocki "Dziękuję to wszystko"

        hide nawrocki
        show eryk neutral right zorder 1 at center
        show shinobu neutral right zorder 2 at left

        eryk "Dziękuję bardzo panie Prezydeńcie"

        eryk "Drodzy goście, wznieśmy teraz toast za nasze dwa bratnie narody i rozpocznijmy Bal!"

        nikt "Dla pana szampan?"
        
        luszcz "kurcze eeeee"

        menu:
            "{b}Tak{/b}":
                $ alko_lvl += 1
                luszcz "Tak, poproszę"

                nikt "proszę"

                luszcz "dziękuję"

                eryk "Na zdrowie!"

                all "Na zdrowie!"

                play sound "audio/sfx/toast.mp3"

                "{i}Łuszczu wypił szampan{/i}"

                eryk "Ahhh, a teraz niech rozpocznie się bal!"

            
            "{b}Tak, ale bezalkoholowy{/b}":
                luszcz "Tak, ale bezalkoholowy"

                nikt "już podaję"
                nikt "prosze"

                luszcz "dziękuję"

                eryk "Na zdrowie!"

                all "Na zdrowie!"

                play sound "audio/sfx/toast.mp3"

                "{i}Łuszczu wypił swój bezalkoholowy szampan{/i}"

                eryk "Ahhh, a teraz niech rozpocznie się bal!"

            "{b}Nie{/b}":
                luszcz "Nie dziękuję"

                eryk "Na zdrowie!"

                all "Na zdrowie!"

                play sound "audio/sfx/toast.mp3"

                "{i}Łuszczu przygląda się jak inni piją szampana{/i}"

                eryk "Ahhh, a teraz niech rozpocznie się bal!"
        
        scene bg bal4 with fade
        play music "audio/music/polonez.mp3"
        show luszcz bal at center

        "{i}Muzyka rozpoczeła grać, a ludzie zaczeli dobierać się w pary do pierwszego tańca{/i}"

        if lilith_social_link == 2 and toxic_pea_social_link >= 2 and toxic_pea_social_link < 6 and gotka_szpont == 1 and gotka_social_link < 10:
            show luszcz bal at slightleft
            show gotka neutral right at slightright

            gotka "Zatańczymy moja świnko morska?"

            show lilith neutral5 at left
            show luszcz bal right at center
            show gotka neutral right at right

            with vpunch
            lilith "Łuszczu, co to za kobieta?"

            show toxic_pea neutral at slightright
            show gotka neutral right at right
            show luszcz bal at center
            show lilith neutral5 at left

            toxic "EMMMMM WHAT THE SIGMA!!!!?"
            toxic "Co to za baby Łuszczu?"

            with vpunch
            gotka "Dokładnie, Łuszczu co to za ludzie?"

            luszcz "(awww fuck!)"

            menu:
                "{b}Co robić?{/b}"

                "{b}Graj o pełną stawkę{/b}":
                    luszcz "emmm, bo wiecie..."

                    show luszcz bal right

                    luszcz "Ja kiedyś oglądałem takie jedno animu..."

                    show luszcz bal

                    luszcz "i w tym animu był własnie taki wątek, że..."

                    show luszcz bal right

                    luszcz "chłopowi ujebało ręke i ojca, a matka stała się bardziej upośledzona niż była"

                    show luszcz bal

                    luszcz "i chłop miał załamkę"

                    show luszcz bal right

                    luszcz "i żone"

                    show luszcz bal

                    luszcz "ale żona była w domu"

                    show luszcz bal right

                    luszcz "a załamka była teraz"

                    show luszcz bal

                    luszcz "i wtedy do tego gościa przyszła jego 40 letnia mistrzyni, która ma tak naprawde 20 lat, bo jej rasa stażeje sie 2 razy wolniej nirz ludzie"

                    show luszcz bal right

                    luszcz "i ona go wyruchała na pocieszenie!"

                    show luszcz bal

                    luszcz "i on ją też wziął za żone!"

                    show luszcz bal right

                    luszcz "i od teraz miał dużą 3 osobową familje i żyli długo i szczęśliwie! KONIEC"

                    show luszcz bal

                    gotka "..."

                    show luszcz bal right

                    lilith "..."

                    show luszcz bal

                    toxic "..."

                    luszcz "To co powiecie na taki rozszerzony trójkącik?"

                    gotka "A spierdalaj z nami koniec!"

                    $ gotka_social_link = 9
                    $ gotka_wybory = 0
                    hide gotka
                    show toxic_pea neutral at right

                    luszcz "..."
                    show luszcz bal right 

                    lilith "Z nami kurwa też, idę się zajebać"

                    hide lilith
                    $ lilith_social_link = 10

                    show luszcz bal

                    toxic "z nami również"

                    play sound "audio/sfx/plucie.mp3"

                    "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                    toxic "spierdalaj"

                    hide toxic_pea 
                    show luszcz bal at center

                    "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                    luszcz "“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”"
                    luszcz "…"
                    luszcz "Heh, pżynajmniej chociaż tyle."
                    luszcz "Niech ja to tylko wyczyszczę"

                    "{i}*siioooooooorb*{/i}"

                    luszcz "Jest szansa rze będę tęsknić za tym smakiem."

                    $ toxic_pea_social_link = 6
                    $ toxic_pea_wybory = 2
                    $ toxic_limit = 1
                    $ timer += 15

                    if zyd_social_link > 0:
                        show luszcz bal at slightleft
                        show shinobu neutral at slightright

                        shinobu "Emmm halo"

                        luszcz "..."

                        shinobu "Widziałam, widziałam tą scene i eeee wszystko okej?"

                        luszcz "emmm"
                        luszcz "..."

                        luszcz "nieee, znaczy tak oki, dzięki pani Loli"

                        shinobu "Shinobu się nazywam"

                        luszcz "shinobu"

                        shinobu "..."

                        luszcz "..."

                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                        luszcz "emmm do mnie?"

                        shinobu "Też mnie to dziwi"

                        luszcz "..."

                        shinobu "..."

                        luszcz "..."
                        luszcz "zobaczę może przyjdę"

                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                        shinobu "fajnie jakbyś przyszedł!"

                        hide shinobu
                        show luszcz bal at center

                        luszcz "ciekawe o co może chodzić"

                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                        tarczownik "O hej Łuszczu mam sprawę!"

                        show luszcz bal at slightleft
                        show tarczownik neutral at slightright

                        luszcz "O co chodzi?"

                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                        luszcz "Jakiego towaru!?!?"

                        tarczownik "A czy to ważne?"

                        luszcz "TAK!"

                        tarczownik "zobaczysz na miejscu"
                        tarczownik "To pójdziesz ze mną?"

                        luszcz "eeee zobaczę"

                        tarczownik "To jak coś czekam przy toaletach."

                        hide tarczownik
                        show luszcz bal at center

                        luszcz "WTF? mega crazy"
                    
                    luszcz "..."

                    jump bal3

                "{b}Gotka{/b}":
                    luszcz "Nie mam pojęcia mój ty wilku alfa"

                    show luszcz bal right

                    luszcz "sio, idźcie sobie, nie znam was!"

                    lilith "ahh tak się bawimy?"
                    lilith "to! to!"
                    lilith "to idę się zabić, dowidzenia"

                    hide lilith
                    $ lilith_social_link = 10

                    show luszcz bal

                    toxic "spierdalaj"

                    play sound "audio/sfx/plucie.mp3"

                    "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                    toxic "Nara."

                    hide toxic_pea 
                    show luszcz bal at slightleft
                    show gotka neutral right at slightright

                    "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                    luszcz "(“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”)"
                    luszcz "…"
                    luszcz "(Heh, pżynajmniej tyle)"
                    luszcz "(Niech ja to tylko wyczyszczę)"

                    "{i}*siioooooooorb*{/i}"

                    luszcz "(Jest szansa rze będę tęsknić za tym smakiem.)"

                    $ toxic_pea_social_link = 6
                    $ toxic_pea_wybory = 2
                    $ toxic_limit = 1

                    luszcz "Jezu co za wariaci"

                    gotka "..."

                    luszcz "No serio ja ich nie znam, przecież WTF co to w ogóle było!"

                    gotka "..."

                    luszcz "eee yyyyy ee TAŃCZYMY?"

                    gotka "..."
                    gotka "niech będzie"
                    gotka "ale od teraz mam cię cały czas na oku"

                    scene bg black with fade
                    "{i}Łuszczu i Gotka dołączyli się do reszty tańczących na sali{/i}"
                    "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                    "{i}Po chwili zmieniła się muzyka, a Łuszczu i Gotka jak najszybciej zeszli z parkietu{/i}"

                    scene bg bal4 with fade
                    $ timer += 15
                    show luszcz bal at slightleft
                    show gotka neutral right at slightright

                    gotka "To było...!"
                    gotka "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                    luszcz "Emmm no sorki no..."

                    gotka "ehhh szkoda strzępić ryja"
                    
                    if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                        gotka "A właśnie Łuszczu, jest sprawa"
                        gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"
                        gotka "Nie wystawisz przecież MNIE, swojej dziewczyny co nie?"

                        luszcz "emmm sorki jeszcze zobaczę mój alfa wilku"

                        gotka "Łuszczu!"

                        luszcz "No spróbuję, no raczej tak..."

                        gotka "To czekam przy toaletach"
                        gotka "Jak będziesz gotowy to przyjdź"

                        hide gotka
                        show luszcz bal at center

                        luszcz "ufff"
                    
                    else:
                        luszcz "..."

                        gotka "..."
                        gotka "To ja wracam do naszego stolika"
                        gotka "Idziesz ze mną?"

                        luszcz "emmmm, jeszcze zobaczę"

                        gotka "Dobrze to jak coś wiesz gdzie mnie szukać"

                        hide gotka
                        show luszcz bal at center

                        luszcz "..."
                    
                    if zyd_social_link > 0:
                        show luszcz bal at slightleft
                        show shinobu neutral at slightright

                        shinobu "O tu jesteś!"
                        shinobu "Widziałam twój taniec i eeeee widać po tobie"

                        luszcz "..?"

                        luszcz "Co po mnie widać pani Loli?"

                        shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                        luszcz "shinobu"

                        shinobu "bardzo ładnie"

                        luszcz "..."

                        shinobu "..."

                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                        luszcz "emmm do mnie?"

                        shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                        luszcz "niemiłe"

                        shinobu "niemiłe, ale prawdziwe"

                        luszcz "..."
                        luszcz "zobaczę może przyjdę"

                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                        shinobu "lepiej żebyś przyszedł!"

                        hide shinobu
                        show luszcz bal at center

                        luszcz "ehhh, ciekawe o co może chodzić"

                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                        tarczownik "O hej Łuszczu mam sprawę!"

                        show luszcz bal at slightleft
                        show tarczownik neutral at slightright

                        luszcz "O co chodzi?"

                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                        luszcz "Jakiego towaru!?!?"

                        tarczownik "A czy to ważne?"

                        luszcz "TAK!"

                        tarczownik "zobaczysz na miejscu"
                        tarczownik "To pójdziesz ze mną?"

                        luszcz "eeee zobaczę"

                        tarczownik "To jak coś czekam przy toaletach."

                        hide tarczownik
                        show luszcz bal at center

                        luszcz "WTF? mega crazy"
                    
                    luszcz "..."

                    jump bal3

                "{b}Lilith{/b}":
                    show luszcz bal right

                    luszcz "Nie wiem kim są ci ludzie!"

                    show luszcz bal

                    luszcz "Coś wy za jedni!?"
                    luszcz "Sio odemnie, bo, bo"
                    luszcz "sio"

                    gotka "..!?"
                    gotka "Czyli tak się bawimy!!!?"
                    gotka "To wiesz co!?"

                    luszcz "jajco boom (przepraszam pani gotko...)"

                    gotka "..!"
                    gotka "spierdalaj!"

                    $ gotka_social_link = 9
                    $ gotka_wybory = 0

                    hide gotka
                    show toxic_pea neutral at right
                    toxic "dokładnie tak"
                    toxic "spierdalaj"

                    play sound "audio/sfx/plucie.mp3"

                    "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                    toxic "Nara."

                    hide toxic_pea 
                    show luszcz bal right at slightright
                    show lilith neutral5 at slightleft

                    "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                    luszcz "(“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”)"
                    luszcz "…"
                    luszcz "(Heh, pżynajmniej tyle)"
                    luszcz "(Niech ja to tylko wyczyszczę)"

                    "{i}*siioooooooorb*{/i}"

                    luszcz "(Jest szansa rze będę tęsknić za tym smakiem.)"

                    $ toxic_pea_social_link = 6
                    $ toxic_pea_wybory = 2
                    $ toxic_limit = 1

                    show luszcz bal right 
                    luszcz "Jezu co za wariaty"

                    lilith "..."

                    luszcz "No serio ich nie znam, przecież WTF co to są za ludzie!"

                    lilith "..."

                    luszcz "To eee... tańczymy Lilith?"

                    lilith "zatańczmy"

                    scene bg black with fade
                    "{i}Łuszczu i Lilith dołączyli się do reszty tańczących na sali{/i}"
                    "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                    "{i}Po chwili zmieniła się muzyka, a Łuszczu i Lilith jak najszybciej zeszli z parkietu{/i}"

                    scene bg bal4 with fade
                    $ timer += 15

                    show luszcz bal at slightleft
                    show lilith neutral2 right at slightright

                    lilith "To było...!"
                    lilith "Tak jakby okej"

                    luszcz "Emmm no sorki no nie umiem tanczyć"

                    lilith "emm nie no jest okej"
                    
                    luszcz "..."

                    lilith "..."
                    lilith "To ja wracam do naszego stolika"
                    lilith "Idziesz ze mną?"

                    luszcz "emmmm, jeszcze zobaczę"

                    lilith "Dobrze to jak coś wiesz gdzie mnie szukać"

                    hide lilith
                    show luszcz bal at center

                    luszcz "..."
                
                    if zyd_social_link > 0:
                        show luszcz bal at slightleft
                        show shinobu neutral at slightright

                        shinobu "O tu jesteś!"
                        shinobu "Widziałam twój taniec i eeeee widać po tobie"

                        luszcz "..?"

                        luszcz "Co po mnie widać pani Loli?"

                        shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                        luszcz "shinobu"

                        shinobu "bardzo ładnie"

                        luszcz "..."

                        shinobu "..."

                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                        luszcz "emmm do mnie?"

                        shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                        luszcz "niemiłe"

                        shinobu "niemiłe, ale prawdziwe"

                        luszcz "..."
                        luszcz "zobaczę może przyjdę"

                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                        shinobu "lepiej żebyś przyszedł!"

                        hide shinobu
                        show luszcz bal at center

                        luszcz "ehhh, ciekawe o co może chodzić"

                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                        tarczownik "O hej Łuszczu mam sprawę!"

                        show luszcz bal at slightleft
                        show tarczownik neutral at slightright

                        luszcz "O co chodzi?"

                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                        luszcz "Jakiego towaru!?!?"

                        tarczownik "A czy to ważne?"

                        luszcz "TAK!"

                        tarczownik "zobaczysz na miejscu"
                        tarczownik "To pójdziesz ze mną?"

                        luszcz "eeee zobaczę"

                        tarczownik "To jak coś czekam przy toaletach."

                        hide tarczownik
                        show luszcz bal at center

                        luszcz "WTF? mega crazy"
                    
                    luszcz "..."

                    jump bal3

                "{b}Toxic Pea{/b}":
                    show luszcz bal

                    luszcz "Nie wiem kim są te kobiety!"

                    show luszcz bal right

                    luszcz "Coś wy za jedne!?"

                    show luszcz bal

                    luszcz "Sio odemnie, bo mi chłopaka straszycie"

                    show luszcz bal right

                    luszcz "akysz"

                    show luszcz bal

                    gotka "..!?"
                    gotka "Czyli tak się bawimy!!!?"
                    gotka "To wiesz co!?"

                    luszcz "jajco boom (przepraszam pani gotko...)"

                    gotka "..!"
                    gotka "spierdalaj!"

                    $ gotka_social_link = 9
                    $ gotka_wybory = 0

                    hide gotka
                    show toxic_pea neutral at right
                    show luszcz bal right

                    lilith "..!?"
                    lilith "ah, czyli to tak..."
                    lilith "Co za wstyd na całą rodzinę"
                    lilith "Tylko moja śmierć jest w stanie zmazać tą hańbe."

                    $ lilith_social_link = 10

                    hide lilith
                    show luszcz bal at slightleft
                    show toxic_pea neutral at slightright

                    toxic "..."

                    luszcz "To eee... tańczymy tatusiu?"

                    toxic "..."
                    toxic "tańczymy..."

                    scene bg black with fade
                    "{i}Łuszczu i Toxic Pea dołączyli się do reszty tańczących na sali{/i}"
                    "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                    "{i}Po chwili zmieniła się muzyka, a Łuszczu i Toxic Pea jak najszybciej zeszli z parkietu{/i}"

                    scene bg bal4 with fade
                    $ timer += 15

                    show luszcz bal at slightleft
                    show toxic_pea neutral at slightright

                    toxic "To było...!"
                    toxic "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                    luszcz "Emmm no sorki no..."

                    toxic "ehhh szkoda strzępić ryja"
                    
                    luszcz "..."

                    toxic "..."
                    toxic "To ja wracam do naszego stolika"
                    toxic "Idziesz ze mną?"

                    luszcz "emmmm, jeszcze zobaczę"

                    toxic "Dobrze to jak coś wiesz gdzie mnie szukać"

                    hide toxic_pea
                    show luszcz bal at center

                    luszcz "..."
                    
                    if zyd_social_link > 0:
                        show luszcz bal at slightleft
                        show shinobu neutral at slightright

                        shinobu "O tu jesteś!"
                        shinobu "Widziałam twój taniec i eeeee widać po tobie"

                        luszcz "..?"

                        luszcz "Co po mnie widać pani Loli?"

                        shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                        luszcz "shinobu"

                        shinobu "bardzo ładnie"

                        luszcz "..."

                        shinobu "..."

                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                        luszcz "emmm do mnie?"

                        shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                        luszcz "niemiłe"

                        shinobu "niemiłe, ale prawdziwe"

                        luszcz "..."
                        luszcz "zobaczę może przyjdę"

                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                        shinobu "lepiej żebyś przyszedł!"

                        hide shinobu
                        show luszcz bal at center

                        luszcz "ehhh, ciekawe o co może chodzić"

                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                        tarczownik "O hej Łuszczu mam sprawę!"

                        show luszcz bal at slightleft
                        show tarczownik neutral at slightright

                        luszcz "O co chodzi?"

                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                        luszcz "Jakiego towaru!?!?"

                        tarczownik "A czy to ważne?"

                        luszcz "TAK!"

                        tarczownik "zobaczysz na miejscu"
                        tarczownik "To pójdziesz ze mną?"

                        luszcz "eeee zobaczę"

                        tarczownik "To jak coś czekam przy toaletach."

                        hide tarczownik
                        show luszcz bal at center

                        luszcz "WTF? mega crazy"
                    
                    luszcz "..."

                    jump bal3

        else:
            if lilith_social_link == 2 and toxic_pea_social_link >= 2 and toxic_pea_social_link < 6:
                show luszcz bal at slightleft
                show lilith neutral3 right at slightright

                lilith "Zatańczymy mój kochany?"

                show toxic_pea neutral right at left
                show luszcz bal right at center
                show lilith neutral2 right at right

                toxic "EMMMMM WHAT THE SIGMA!!!!?"
                toxic "Co to za baba Łuszczu?"

                show luszcz bal at center
                show lilith neutral5 right
                with vpunch
                lilith "Co to za nie miły facet Łuszczu!!?!?"

                luszcz "(oj joj)"

                menu:
                    "{b}Co robić?{/b}"

                    "{b}Graj o pełną stawkę{/b}":
                        luszcz "emmm, bo wiecie..."

                        show luszcz bal right

                        luszcz "Ja kiedyś oglądałem takie jedno animu..."

                        show luszcz bal

                        luszcz "i w tym animu był własnie taki wątek, że..."

                        show luszcz bal right

                        luszcz "chłopowi ujebało ręke i ojca, a matka stała się bardziej upośledzona niż była"

                        show luszcz bal

                        luszcz "i chłop miał załamkę"

                        show luszcz bal right

                        luszcz "i żone"

                        show luszcz bal

                        luszcz "ale żona była w domu"

                        show luszcz bal right

                        luszcz "a załamka była teraz"

                        show luszcz bal

                        luszcz "i wtedy do tego gościa przyszła jego 40 letnia mistrzyni, która ma tak naprawde 20 lat, bo jej rasa stażeje sie 2 razy wolniej nirz ludzie"

                        show luszcz bal right

                        luszcz "i ona go wyruchała na pocieszenie!"

                        show luszcz bal

                        luszcz "i on ją też wziął za żone!"

                        show luszcz bal right

                        luszcz "i od teraz miał dużą 3 osobową familje i żyli długo i szczęśliwie! KONIEC"

                        show luszcz bal

                        lilith "..."

                        show luszcz bal right

                        toxic "..."

                        show luszcz bal

                        luszcz "To co powiecie na trójkącik?"

                        lilith "Aaa aaa"
                        lilith "A idę się zajebać"

                        $ lilith_social_link = 10
                        hide lilith

                        luszcz "..."
                        show luszcz bal right 

                        toxic "NIE"

                        play sound "audio/sfx/plucie.mp3"

                        "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                        toxic "spierdalaj"

                        hide toxic_pea 
                        show luszcz bal right at center

                        "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                        luszcz "“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”"
                        luszcz "…"
                        luszcz "Heh, pżynajmniej chociaż tyle."
                        luszcz "Niech ja to tylko wyczyszczę"

                        "{i}*siioooooooorb*{/i}"

                        luszcz "Jest szansa rze będę tęsknić za tym smakiem."

                        $ toxic_pea_social_link = 6
                        $ toxic_pea_wybory = 2
                        $ toxic_limit = 1
                        $ timer += 15

                        luszcz "..."

                        if zyd_social_link > 0:
                            show luszcz bal at slightleft
                            show shinobu neutral at slightright

                            shinobu "Emmm halo"

                            luszcz "..."

                            shinobu "Widziałam, widziałam tą scene i eeee wszystko okej?"

                            luszcz "emmm"
                            luszcz "..."

                            luszcz "nieee, znaczy tak oki, dzięki pani Loli"

                            shinobu "Shinobu się nazywam"

                            luszcz "shinobu"

                            shinobu "..."

                            luszcz "..."

                            shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                            luszcz "emmm do mnie?"

                            shinobu "Też mnie to dziwi"

                            luszcz "..."

                            shinobu "..."

                            luszcz "..."
                            luszcz "zobaczę może przyjdę"

                            shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                            shinobu "fajnie jakbyś przyszedł!"

                            hide shinobu
                            show luszcz bal at center

                            luszcz "ciekawe o co może chodzić"

                        if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                            gotka "Ej Łuszczu!"
                            
                            show luszcz bal at slightleft
                            show gotka neutral right at slightright

                            gotka "Masz dla mnie chwilkę?"

                            luszcz "Ja!?"

                            gotka "Tak, ty!"
                            gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                            luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                            gotka "Dobrze, będę czekała przy toaletach"

                            hide gotka
                            show luszcz bal at center

                            luszcz "crazy timing!"

                        if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                            tarczownik "O hej Łuszczu mam sprawę!"

                            show luszcz bal at slightleft
                            show tarczownik neutral at slightright

                            luszcz "O co chodzi?"

                            tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                            tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                            luszcz "Jakiego towaru!?!?"

                            tarczownik "A czy to ważne?"

                            luszcz "TAK!"

                            tarczownik "zobaczysz na miejscu"
                            tarczownik "To pójdziesz ze mną?"

                            luszcz "eeee zobaczę"

                            tarczownik "To jak coś czekam przy toaletach."

                            hide tarczownik
                            show luszcz bal at center

                            luszcz "WTF? mega crazy"
                        
                        luszcz "..."

                        jump bal3

                    "{b}Lilith{/b}":
                        luszcz "Nie mam pojęcia moja kochana"

                        show luszcz bal right

                        luszcz "sio, akysz ty, ty głupi clankerze"

                        toxic "ahh tak się bawimy?"

                        play sound "audio/sfx/plucie.mp3"

                        "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                        toxic "Nara."

                        hide toxic_pea 
                        show luszcz bal at slightleft
                        show lilith neutral5 right at slightright

                        "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                        luszcz "(“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”)"
                        luszcz "…"
                        luszcz "(Heh, pżynajmniej tyle)"
                        luszcz "(Niech ja to tylko wyczyszczę)"

                        "{i}*siioooooooorb*{/i}"

                        luszcz "(Jest szansa rze będę tęsknić za tym smakiem.)"

                        $ toxic_pea_social_link = 6
                        $ toxic_pea_wybory = 2
                        $ toxic_limit = 1

                        show luszcz bal 
                        luszcz "Jezu co za wariat"

                        lilith "..."

                        luszcz "No serio go nie znam, przecież WTF co za człwowiek z niego!"

                        lilith "..."

                        luszcz "To eee... tańczymy Lilith?"

                        lilith "..."

                        show lilith neutral3 right

                        lilith "zatańczmy"

                        scene bg black with fade
                        "{i}Łuszczu i Lilith dołączyli się do reszty tańczących na sali{/i}"
                        "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                        "{i}Po chwili zmieniła się muzyka, a Łuszczu i Lilith jak najszybciej zeszli z parkietu{/i}"

                        scene bg bal4 with fade
                        $ timer += 15

                        show luszcz bal at slightleft
                        show lilith neutral2 right at slightright

                        lilith "To było...!"
                        lilith "Tak jakby okej"

                        luszcz "Emmm no sorki no nie umiem tanczyć"

                        lilith "emm nie no jest okej"
                        
                        luszcz "..."

                        lilith "..."
                        lilith "To ja wracam do naszego stolika"
                        lilith "Idziesz ze mną?"

                        luszcz "emmmm, jeszcze zobaczę"

                        lilith "Dobrze to jak coś wiesz gdzie mnie szukać"

                        hide lilith
                        show luszcz bal at center

                        luszcz "..."
                        
                        if zyd_social_link > 0:
                            show luszcz bal at slightleft
                            show shinobu neutral at slightright

                            shinobu "O tu jesteś!"
                            shinobu "Widziałam twój taniec i eeeee widać po tobie"

                            luszcz "..?"

                            luszcz "Co po mnie widać pani Loli?"

                            shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                            luszcz "shinobu"

                            shinobu "bardzo ładnie"

                            luszcz "..."

                            shinobu "..."

                            shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                            luszcz "emmm do mnie?"

                            shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                            luszcz "niemiłe"

                            shinobu "niemiłe, ale prawdziwe"

                            luszcz "..."
                            luszcz "zobaczę może przyjdę"

                            shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                            shinobu "lepiej żebyś przyszedł!"

                            hide shinobu
                            show luszcz bal at center

                            luszcz "ehhh, ciekawe o co może chodzić"

                        if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                            gotka "Ej Łuszczu!"
                            
                            show luszcz bal at slightleft
                            show gotka neutral right at slightright

                            gotka "Masz dla mnie chwilkę?"

                            luszcz "Ja!?"

                            gotka "Tak, ty!"
                            gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                            luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                            gotka "Dobrze, będę czekała przy toaletach"

                            hide gotka
                            show luszcz bal at center

                            luszcz "crazy!"

                        if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                            tarczownik "O hej Łuszczu mam sprawę!"

                            show luszcz bal at slightleft
                            show tarczownik neutral at slightright

                            luszcz "O co chodzi?"

                            tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                            tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                            luszcz "Jakiego towaru!?!?"

                            tarczownik "A czy to ważne?"

                            luszcz "TAK!"

                            tarczownik "zobaczysz na miejscu"
                            tarczownik "To pójdziesz ze mną?"

                            luszcz "eeee zobaczę"

                            tarczownik "To jak coś czekam przy toaletach."

                            hide tarczownik
                            show luszcz bal at center

                            luszcz "WTF? mega crazy"
                        
                        luszcz "..."

                        jump bal3

                    "{b}Toxic Pea{/b}":
                        show luszcz bal right

                        luszcz "Nie wiem kim jest ta kobieta!"

                        show luszcz bal

                        luszcz "Coś ty za jedna!?"
                        luszcz "Sio odemnie, bo mi chłopaka straszysz"
                        luszcz "akysz"

                        lilith "..!?"
                        lilith "ah, czyli to tak..."
                        lilith "Co za wstyd na całą rodzinę"
                        lilith "Tylko moja śmierć jest w stanie zmazać tą hańbe."

                        $ lilith_social_link = 10

                        hide lilith
                        hide toxic_pea 
                        show luszcz bal right at slightright
                        show toxic_pea neutral right at slightleft

                        luszcz "..!?"

                        toxic "..."

                        show luszcz bal right at slightright

                        luszcz "To eee... tańczymy tatusiu?"

                        toxic "..."
                        toxic "tańczymy..."

                        scene bg black with fade
                        "{i}Łuszczu i Toxic Pea dołączyli się do reszty tańczących na sali{/i}"
                        "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                        "{i}Po chwili zmieniła się muzyka, a Łuszczu i Toxic Pea jak najszybciej zeszli z parkietu{/i}"

                        scene bg bal4 with fade
                        $ timer += 15

                        show luszcz bal at slightleft
                        show toxic_pea neutral at slightright

                        toxic "To było...!"
                        toxic "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                        luszcz "Emmm no sorki no..."

                        toxic "ehhh szkoda strzępić ryja"
                        
                        luszcz "..."

                        toxic "..."
                        toxic "To ja wracam do naszego stolika"
                        toxic "Idziesz ze mną?"

                        luszcz "emmmm, jeszcze zobaczę"

                        toxic "Dobrze to jak coś wiesz gdzie mnie szukać"

                        hide toxic_pea
                        show luszcz bal at center

                        luszcz "..."
                        
                        if zyd_social_link > 0:
                            show luszcz bal at slightleft
                            show shinobu neutral at slightright

                            shinobu "O tu jesteś!"
                            shinobu "Widziałam twój taniec i eeeee widać po tobie"

                            luszcz "..?"

                            luszcz "Co po mnie widać pani Loli?"

                            shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                            luszcz "shinobu"

                            shinobu "bardzo ładnie"

                            luszcz "..."

                            shinobu "..."

                            shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                            luszcz "emmm do mnie?"

                            shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                            luszcz "niemiłe"

                            shinobu "niemiłe, ale prawdziwe"

                            luszcz "..."
                            luszcz "zobaczę może przyjdę"

                            shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                            shinobu "lepiej żebyś przyszedł!"

                            hide shinobu
                            show luszcz bal at center

                            luszcz "ehhh, ciekawe o co może chodzić"

                        if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                            gotka "Ej Łuszczu!"
                            
                            show luszcz bal at slightleft
                            show gotka neutral right at slightright

                            gotka "Masz dla mnie chwilkę?"

                            luszcz "Ja!?"

                            gotka "Tak, ty!"
                            gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                            luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                            gotka "Dobrze, będę czekała przy toaletach"

                            hide gotka
                            show luszcz bal at center

                            luszcz "crazy!"

                        if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                            tarczownik "O hej Łuszczu mam sprawę!"

                            show luszcz bal at slightleft
                            show tarczownik neutral at slightright

                            luszcz "O co chodzi?"

                            tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                            tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                            luszcz "Jakiego towaru!?!?"

                            tarczownik "A czy to ważne?"

                            luszcz "TAK!"

                            tarczownik "zobaczysz na miejscu"
                            tarczownik "To pójdziesz ze mną?"

                            luszcz "eeee zobaczę"

                            tarczownik "To jak coś czekam przy toaletach."

                            hide tarczownik
                            show luszcz bal at center

                            luszcz "WTF? mega crazy"
                        
                        luszcz "..."

                        jump bal3

            else:
                if lilith_social_link == 2 and gotka_szpont == 1 and gotka_social_link < 10:
                    show luszcz bal at slightleft
                    show gotka neutral right at slightright

                    gotka "Zatańczymy moja świnko morska?"

                    show lilith neutral5 at left
                    show luszcz bal right at center
                    show gotka neutral right at right

                    with vpunch
                    toxic "Łuszczu, co to za kobieta?"

                    show luszcz bal at center
                    with vpunch
                    gotka "Dokładnie, Łuszczu co to za kobieta?"

                    luszcz "(oj joj)"

                    menu:
                        "{b}Co robić?{/b}"

                        "{b}Graj o pełną stawkę{/b}":
                            luszcz "emmm, bo wiecie..."

                            show luszcz bal right

                            luszcz "Ja kiedyś oglądałem takie jedno animu..."

                            show luszcz bal

                            luszcz "i w tym animu był własnie taki wątek, że..."

                            show luszcz bal right

                            luszcz "chłopowi ujebało ręke i ojca, a matka stała się bardziej upośledzona niż była"

                            show luszcz bal

                            luszcz "i chłop miał załamkę"

                            show luszcz bal right

                            luszcz "i żone"

                            show luszcz bal

                            luszcz "ale żona była w domu"

                            show luszcz bal right

                            luszcz "a załamka była teraz"

                            show luszcz bal

                            luszcz "i wtedy do tego gościa przyszła jego 40 letnia mistrzyni, która ma tak naprawde 20 lat, bo jej rasa stażeje sie 2 razy wolniej nirz ludzie"

                            show luszcz bal right

                            luszcz "i ona go wyruchała na pocieszenie!"

                            show luszcz bal

                            luszcz "i on ją też wziął za żone!"

                            show luszcz bal right

                            luszcz "i od teraz miał dużą 3 osobową familje i żyli długo i szczęśliwie! KONIEC"

                            show luszcz bal

                            gotka "..."

                            show luszcz bal right

                            lilith "..."

                            show luszcz bal

                            luszcz "To co powiecie na trójkącik?"

                            gotka "A spierdalaj z nami koniec!"

                            $ gotka_social_link = 9
                            $ gotka_wybory = 0
                            hide gotka

                            luszcz "..."
                            show luszcz bal right 

                            lilith "Z nami kurwa też, idę się zajebać"

                            hide lilith
                            $ lilith_social_link = 10
                            show luszcz bal right at center

                            luszcz "..."
                            luszcz "emmm, plan troszkę nie wypalił"

                            $ timer += 15

                            if zyd_social_link > 0:
                                show luszcz bal at slightleft
                                show shinobu neutral at slightright

                                shinobu "Emmm halo"

                                luszcz "..."

                                shinobu "Widziałam, widziałam tą scene i eeee wszystko okej?"

                                luszcz "emmm"
                                luszcz "..."

                                luszcz "nieee, znaczy tak oki, dzięki pani Loli"

                                shinobu "Shinobu się nazywam"

                                luszcz "shinobu"

                                shinobu "..."

                                luszcz "..."

                                shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                luszcz "emmm do mnie?"

                                shinobu "Też mnie to dziwi"

                                luszcz "..."

                                shinobu "..."

                                luszcz "..."
                                luszcz "zobaczę może przyjdę"

                                shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                shinobu "fajnie jakbyś przyszedł!"

                                hide shinobu
                                show luszcz bal at center

                                luszcz "ciekawe o co może chodzić"

                            if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                tarczownik "O hej Łuszczu mam sprawę!"

                                show luszcz bal at slightleft
                                show tarczownik neutral at slightright

                                luszcz "O co chodzi?"

                                tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                luszcz "Jakiego towaru!?!?"

                                tarczownik "A czy to ważne?"

                                luszcz "TAK!"

                                tarczownik "zobaczysz na miejscu"
                                tarczownik "To pójdziesz ze mną?"

                                luszcz "eeee zobaczę"

                                tarczownik "To jak coś czekam przy toaletach."

                                hide tarczownik
                                show luszcz bal at center

                                luszcz "WTF? mega crazy"
                            
                            luszcz "..."

                            jump bal3

                        "{b}Gotka{/b}":
                            luszcz "Nie mam pojęcia mój ty wilku alfa"

                            show luszcz bal right

                            luszcz "sio, idź sobie, nie znam Cię!"

                            lilith "ahh tak się bawimy?"
                            lilith "to! to!"
                            lilith "to idę się zabić, dowidzenia"

                            hide lilith
                            $ lilith_social_link = 10
                            show luszcz bal at slightleft
                            show gotka neutral right at slightright

                            show luszcz bal 
                            luszcz "Jezu co za wariatka"

                            gotka "..."

                            luszcz "No serio jej nie znam, przecież WTF co to w ogóle było!"

                            gotka "..."

                            luszcz "eee yyyyy ee TAŃCZYMY?"

                            gotka "..."
                            gotka "niech będzie"
                            gotka "ale od teraz mam cię cały czas na oku"

                            scene bg black with fade
                            "{i}Łuszczu i Gotka dołączyli się do reszty tańczących na sali{/i}"
                            "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                            "{i}Po chwili zmieniła się muzyka, a Łuszczu i Gotka jak najszybciej zeszli z parkietu{/i}"

                            scene bg bal4 with fade
                            $ timer += 15
                            show luszcz bal at slightleft
                            show gotka neutral right at slightright

                            gotka "To było...!"
                            gotka "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                            luszcz "Emmm no sorki no..."

                            gotka "ehhh szkoda strzępić ryja"
                            
                            if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                gotka "A właśnie Łuszczu, jest sprawa"
                                gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"
                                gotka "Nie wystawisz przecież MNIE, swojej dziewczyny co nie?"

                                luszcz "emmm sorki jeszcze zobaczę mój alfa wilku"

                                gotka "Łuszczu!"

                                luszcz "No spróbuję, no raczej tak..."

                                gotka "To czekam przy toaletach"
                                gotka "Jak będziesz gotowy to przyjdź"

                                hide gotka
                                show luszcz bal at center

                                luszcz "ufff"
                            
                            else:
                                luszcz "..."

                                gotka "..."
                                gotka "To ja wracam do naszego stolika"
                                gotka "Idziesz ze mną?"

                                luszcz "emmmm, jeszcze zobaczę"

                                gotka "Dobrze to jak coś wiesz gdzie mnie szukać"

                                hide gotka
                                show luszcz bal at center

                                luszcz "..."
                            
                            if zyd_social_link > 0:
                                show luszcz bal at slightleft
                                show shinobu neutral at slightright

                                shinobu "O tu jesteś!"
                                shinobu "Widziałam twój taniec i eeeee widać po tobie"

                                luszcz "..?"

                                luszcz "Co po mnie widać pani Loli?"

                                shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                                luszcz "shinobu"

                                shinobu "bardzo ładnie"

                                luszcz "..."

                                shinobu "..."

                                shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                luszcz "emmm do mnie?"

                                shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                luszcz "niemiłe"

                                shinobu "niemiłe, ale prawdziwe"

                                luszcz "..."
                                luszcz "zobaczę może przyjdę"

                                shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                shinobu "lepiej żebyś przyszedł!"

                                hide shinobu
                                show luszcz bal at center

                                luszcz "ehhh, ciekawe o co może chodzić"

                            if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                tarczownik "O hej Łuszczu mam sprawę!"

                                show luszcz bal at slightleft
                                show tarczownik neutral at slightright

                                luszcz "O co chodzi?"

                                tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                luszcz "Jakiego towaru!?!?"

                                tarczownik "A czy to ważne?"

                                luszcz "TAK!"

                                tarczownik "zobaczysz na miejscu"
                                tarczownik "To pójdziesz ze mną?"

                                luszcz "eeee zobaczę"

                                tarczownik "To jak coś czekam przy toaletach."

                                hide tarczownik
                                show luszcz bal at center

                                luszcz "WTF? mega crazy"
                            
                            luszcz "..."

                            jump bal3

                        "{b}Lilith{/b}":
                            show luszcz bal right

                            luszcz "Nie wiem kim jest ta kobieta!"

                            show luszcz bal

                            luszcz "Coś ty za jedna!?"
                            luszcz "Sio odemnie, bo, bo"
                            luszcz "sio"

                            gotka "..!?"
                            gotka "Czyli tak się bawimy!!!?"
                            gotka "To wiesz co!?"

                            luszcz "jajco boom (przepraszam pani gotko...)"

                            gotka "..!"
                            gotka "spierdalaj!"

                            $ gotka_social_link = 9
                            $ gotka_wybory = 0

                            hide gotka
                            hide lilith 
                            show luszcz bal right at slightright
                            show lilith neutral2 at slightleft

                            lilith "..."

                            luszcz "To eee... tańczymy Lilith?"

                            lilith "zatańczmy"

                            scene bg black with fade
                            "{i}Łuszczu i Lilith dołączyli się do reszty tańczących na sali{/i}"
                            "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                            "{i}Po chwili zmieniła się muzyka, a Łuszczu i Lilith jak najszybciej zeszli z parkietu{/i}"

                            scene bg bal4 with fade
                            $ timer += 15

                            show luszcz bal at slightleft
                            show lilith neutral2 right at slightright

                            lilith "To było...!"
                            lilith "Tak jakby okej"

                            luszcz "Emmm no sorki no nie umiem tanczyć"

                            lilith "emm nie no jest okej"
                            
                            luszcz "..."

                            lilith "..."
                            lilith "To ja wracam do naszego stolika"
                            lilith "Idziesz ze mną?"

                            luszcz "emmmm, jeszcze zobaczę"

                            lilith "Dobrze to jak coś wiesz gdzie mnie szukać"

                            hide lilith
                            show luszcz bal at center

                            luszcz "..."

                            if zyd_social_link > 0:  
                                show luszcz bal at slightleft
                                show shinobu neutral at slightright

                                shinobu "O tu jesteś!"
                                shinobu "Widziałam twój taniec i eeeee widać po tobie"

                                luszcz "..?"

                                luszcz "Co po mnie widać pani Loli?"

                                shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                                luszcz "shinobu"

                                shinobu "bardzo ładnie"

                                luszcz "..."

                                shinobu "..."

                                shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                luszcz "emmm do mnie?"

                                shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                luszcz "niemiłe"

                                shinobu "niemiłe, ale prawdziwe"

                                luszcz "..."
                                luszcz "zobaczę może przyjdę"

                                shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                shinobu "lepiej żebyś przyszedł!"

                                hide shinobu
                                show luszcz bal at center

                                luszcz "ehhh, ciekawe o co może chodzić"

                            if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                tarczownik "O hej Łuszczu mam sprawę!"

                                show luszcz bal at slightleft
                                show tarczownik neutral at slightright

                                luszcz "O co chodzi?"

                                tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                luszcz "Jakiego towaru!?!?"

                                tarczownik "A czy to ważne?"

                                luszcz "TAK!"

                                tarczownik "zobaczysz na miejscu"
                                tarczownik "To pójdziesz ze mną?"

                                luszcz "eeee zobaczę"

                                tarczownik "To jak coś czekam przy toaletach."

                                hide tarczownik
                                show luszcz bal at center

                                luszcz "WTF? mega crazy"
                            
                            luszcz "..."

                            jump bal3

                else:
                    if toxic_pea_social_link >= 2 and toxic_pea_social_link < 6 and gotka_szpont == 1:
                        show luszcz bal at slightleft
                        show gotka neutral right at slightright

                        gotka "Zatańczymy moja świnko morska?"

                        show toxic_pea neutral right at left
                        show luszcz bal right at center
                        show gotka neutral right at right

                        toxic "EMMMMM WHAT THE SIGMA!!!!?"
                        toxic "Co to za baba Łuszczu?"

                        show luszcz bal at center
                        with vpunch
                        gotka "Co to za nie miły facet Łuszczu!!?!?"

                        luszcz "(oj joj)"

                        menu:
                            "{b}Co robić?{/b}"

                            "{b}Graj o pełną stawkę{/b}":
                                luszcz "emmm, bo wiecie..."

                                show luszcz bal right

                                luszcz "Ja kiedyś oglądałem takie jedno animu..."

                                show luszcz bal

                                luszcz "i w tym animu był własnie taki wątek, że..."

                                show luszcz bal right

                                luszcz "chłopowi ujebało ręke i ojca, a matka stała się bardziej upośledzona niż była"

                                show luszcz bal

                                luszcz "i chłop miał załamkę"

                                show luszcz bal right

                                luszcz "i żone"

                                show luszcz bal

                                luszcz "ale żona była w domu"

                                show luszcz bal right

                                luszcz "a załamka była teraz"

                                show luszcz bal

                                luszcz "i wtedy do tego gościa przyszła jego 40 letnia mistrzyni, która ma tak naprawde 20 lat, bo jej rasa stażeje sie 2 razy wolniej nirz ludzie"

                                show luszcz bal right

                                luszcz "i ona go wyruchała na pocieszenie!"

                                show luszcz bal

                                luszcz "i on ją też wziął za żone!"

                                show luszcz bal right

                                luszcz "i od teraz miał dużą 3 osobową familje i żyli długo i szczęśliwie! KONIEC"

                                show luszcz bal

                                gotka "..."

                                show luszcz bal right

                                toxic "..."

                                show luszcz bal

                                luszcz "To co powiecie na trójkącik?"

                                gotka "A spierdalaj z nami koniec!"

                                $ gotka_social_link = 9
                                $ gotka_wybory = 0
                                hide gotka

                                luszcz "..."
                                show luszcz bal right 

                                toxic "z nami również"

                                play sound "audio/sfx/plucie.mp3"

                                "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                                toxic "spierdalaj"

                                hide toxic_pea 
                                show luszcz bal right at center

                                "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                                luszcz "“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”"
                                luszcz "…"
                                luszcz "Heh, pżynajmniej chociaż tyle."
                                luszcz "Niech ja to tylko wyczyszczę"

                                "{i}*siioooooooorb*{/i}"

                                luszcz "Jest szansa rze będę tęsknić za tym smakiem."

                                $ toxic_pea_social_link = 6
                                $ toxic_pea_wybory = 2
                                $ toxic_limit = 1
                                $ timer += 15

                                luszcz "..."

                                if zyd_social_link > 0:
                                    show luszcz bal at slightleft
                                    show shinobu neutral at slightright

                                    shinobu "Emmm halo"

                                    luszcz "..."

                                    shinobu "Widziałam, widziałam tą scene i eeee wszystko okej?"

                                    luszcz "emmm"
                                    luszcz "..."

                                    luszcz "nieee, znaczy tak oki, dzięki pani Loli"

                                    shinobu "Shinobu się nazywam"

                                    luszcz "shinobu"

                                    shinobu "..."

                                    luszcz "..."

                                    shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                    luszcz "emmm do mnie?"

                                    shinobu "Też mnie to dziwi"

                                    luszcz "..."

                                    shinobu "..."

                                    luszcz "..."
                                    luszcz "zobaczę może przyjdę"

                                    shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                    shinobu "fajnie jakbyś przyszedł!"

                                    hide shinobu
                                    show luszcz bal at center

                                    luszcz "ciekawe o co może chodzić"

                                if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                    tarczownik "O hej Łuszczu mam sprawę!"

                                    show luszcz bal at slightleft
                                    show tarczownik neutral at slightright

                                    luszcz "O co chodzi?"

                                    tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                    tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                    luszcz "Jakiego towaru!?!?"

                                    tarczownik "A czy to ważne?"

                                    luszcz "TAK!"

                                    tarczownik "zobaczysz na miejscu"
                                    tarczownik "To pójdziesz ze mną?"

                                    luszcz "eeee zobaczę"

                                    tarczownik "To jak coś czekam przy toaletach."

                                    hide tarczownik
                                    show luszcz bal at center

                                    luszcz "WTF? mega crazy"
                                
                                luszcz "..."

                                jump bal3

                            "{b}Gotka{/b}":
                                luszcz "Nie mam pojęcia mój ty wilku alfa"

                                show luszcz bal right

                                luszcz "sio, akysz ty, ty głupi clankerze"

                                toxic "ahh tak się bawimy?"

                                play sound "audio/sfx/plucie.mp3"

                                "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

                                toxic "Nara."

                                hide toxic_pea 
                                show luszcz bal at slightleft
                                show gotka neutral right at slightright

                                "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

                                luszcz "(“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”)"
                                luszcz "…"
                                luszcz "(Heh, pżynajmniej tyle)"
                                luszcz "(Niech ja to tylko wyczyszczę)"

                                "{i}*siioooooooorb*{/i}"

                                luszcz "(Jest szansa rze będę tęsknić za tym smakiem.)"

                                $ toxic_pea_social_link = 6
                                $ toxic_pea_wybory = 2
                                $ toxic_limit = 1

                                show luszcz bal 
                                luszcz "Jezu co za wariat"

                                gotka "..."

                                luszcz "No serio go nie znam, przecież WTF co za człwowiek z niego!"

                                gotka "..."

                                luszcz "eee yyyyy ee TAŃCZYMY?"

                                gotka "..."
                                gotka "niech będzie"
                                gotka "ale od teraz mam cię cały czas na oku"

                                scene bg black with fade
                                "{i}Łuszczu i Gotka dołączyli się do reszty tańczących na sali{/i}"
                                "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                                "{i}Po chwili zmieniła się muzyka, a Łuszczu i Gotka jak najszybciej zeszli z parkietu{/i}"

                                scene bg bal4 with fade
                                $ timer += 15
                                show luszcz bal at slightleft
                                show gotka neutral right at slightright

                                gotka "To było...!"
                                gotka "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                                luszcz "Emmm no sorki no..."

                                gotka "ehhh szkoda strzępić ryja"
                                
                                if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                    gotka "A właśnie Łuszczu, jest sprawa"
                                    gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"
                                    gotka "Nie wystawisz przecież MNIE, swojej dziewczyny co nie?"

                                    luszcz "emmm sorki jeszcze zobaczę mój alfa wilku"

                                    gotka "Łuszczu!"

                                    luszcz "No spróbuję, no raczej tak..."

                                    gotka "To czekam przy toaletach"
                                    gotka "Jak będziesz gotowy to przyjdź"

                                    hide gotka
                                    show luszcz bal at center

                                    luszcz "ufff"
                                
                                else:
                                    luszcz "..."

                                    gotka "..."
                                    gotka "To ja wracam do naszego stolika"
                                    gotka "Idziesz ze mną?"

                                    luszcz "emmmm, jeszcze zobaczę"

                                    gotka "Dobrze to jak coś wiesz gdzie mnie szukać"

                                    hide gotka
                                    show luszcz bal at center

                                    luszcz "..."
                                
                                if zyd_social_link > 0:
                                    show luszcz bal at slightleft
                                    show shinobu neutral at slightright

                                    shinobu "O tu jesteś!"
                                    shinobu "Widziałam twój taniec i eeeee widać po tobie"

                                    luszcz "..?"

                                    luszcz "Co po mnie widać pani Loli?"

                                    shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                                    luszcz "shinobu"

                                    shinobu "bardzo ładnie"

                                    luszcz "..."

                                    shinobu "..."

                                    shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                    luszcz "emmm do mnie?"

                                    shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                    luszcz "niemiłe"

                                    shinobu "niemiłe, ale prawdziwe"

                                    luszcz "..."
                                    luszcz "zobaczę może przyjdę"

                                    shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                    shinobu "lepiej żebyś przyszedł!"

                                    hide shinobu
                                    show luszcz bal at center

                                    luszcz "ehhh, ciekawe o co może chodzić"

                                if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                    tarczownik "O hej Łuszczu mam sprawę!"

                                    show luszcz bal at slightleft
                                    show tarczownik neutral at slightright

                                    luszcz "O co chodzi?"

                                    tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                    tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                    luszcz "Jakiego towaru!?!?"

                                    tarczownik "A czy to ważne?"

                                    luszcz "TAK!"

                                    tarczownik "zobaczysz na miejscu"
                                    tarczownik "To pójdziesz ze mną?"

                                    luszcz "eeee zobaczę"

                                    tarczownik "To jak coś czekam przy toaletach."

                                    hide tarczownik
                                    show luszcz bal at center

                                    luszcz "WTF? mega crazy"
                                
                                luszcz "..."

                                jump bal3

                            "{b}Toxic Pea{/b}":
                                show luszcz bal right

                                luszcz "Nie wiem kim jest ta kobieta!"

                                show luszcz bal

                                luszcz "Coś ty za jedna!?"
                                luszcz "Sio odemnie, bo mi chłopaka straszysz"
                                luszcz "akysz"

                                gotka "..!?"
                                gotka "Czyli tak się bawimy!!!?"
                                gotka "To wiesz co!?"

                                luszcz "jajco boom (przepraszam pani gotko...)"

                                gotka "..!"
                                gotka "spierdalaj!"

                                $ gotka_social_link = 9
                                $ gotka_wybory = 0

                                hide gotka
                                hide toxic_pea 
                                show luszcz bal right at slightright
                                show toxic_pea neutral right at slightleft

                                toxic "..."

                                luszcz "To eee... tańczymy tatusiu?"

                                toxic "..."
                                toxic "tańczymy..."

                                scene bg black with fade
                                "{i}Łuszczu i Toxic Pea dołączyli się do reszty tańczących na sali{/i}"
                                "{i}Jednakże ich ruchu były wykonywane jakby od niechcenia i z odrazą{/i}"
                                "{i}Po chwili zmieniła się muzyka, a Łuszczu i Toxic Pea jak najszybciej zeszli z parkietu{/i}"

                                scene bg bal4 with fade
                                $ timer += 15

                                show luszcz bal at slightleft
                                show toxic_pea neutral at slightright

                                toxic "To było...!"
                                toxic "Doprawdy żałosne, jezus maria jak można tak wszystko zjebać!"

                                luszcz "Emmm no sorki no..."

                                toxic "ehhh szkoda strzępić ryja"
                                
                                luszcz "..."

                                toxic "..."
                                toxic "To ja wracam do naszego stolika"
                                toxic "Idziesz ze mną?"

                                luszcz "emmmm, jeszcze zobaczę"

                                toxic "Dobrze to jak coś wiesz gdzie mnie szukać"

                                hide toxic_pea
                                show luszcz bal at center

                                luszcz "..."

                                if zyd_social_link > 0:
                                    show luszcz bal at slightleft
                                    show shinobu neutral at slightright

                                    shinobu "O tu jesteś!"
                                    shinobu "Widziałam twój taniec i eeeee widać po tobie"

                                    luszcz "..?"

                                    luszcz "Co po mnie widać pani Loli?"

                                    shinobu "Aggghhhh, SHI-NO-BU, Shinobu się nazywam"

                                    luszcz "shinobu"

                                    shinobu "bardzo ładnie"

                                    luszcz "..."

                                    shinobu "..."

                                    shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                    luszcz "emmm do mnie?"

                                    shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                    luszcz "niemiłe"

                                    shinobu "niemiłe, ale prawdziwe"

                                    luszcz "..."
                                    luszcz "zobaczę może przyjdę"

                                    shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                    shinobu "lepiej żebyś przyszedł!"

                                    hide shinobu
                                    show luszcz bal at center

                                    luszcz "ehhh, ciekawe o co może chodzić"

                                if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                    tarczownik "O hej Łuszczu mam sprawę!"

                                    show luszcz bal at slightleft
                                    show tarczownik neutral at slightright

                                    luszcz "O co chodzi?"

                                    tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                    tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                    luszcz "Jakiego towaru!?!?"

                                    tarczownik "A czy to ważne?"

                                    luszcz "TAK!"

                                    tarczownik "zobaczysz na miejscu"
                                    tarczownik "To pójdziesz ze mną?"

                                    luszcz "eeee zobaczę"

                                    tarczownik "To jak coś czekam przy toaletach."

                                    hide tarczownik
                                    show luszcz bal at center

                                    luszcz "WTF? mega crazy"
                                
                                luszcz "..."

                                jump bal3

                    else:
                        if lilith_social_link == 2:
                            show luszcz bal at slightleft
                            show lilith neutral2 right at slightright

                            lilith "Zatańczymy mój kochany?"

                            luszcz "Z przyjemnością!"
                            scene bg black with fade
                            "{i}Łuszczu i Lilith zaczęli sunąć po sali tanecznym krokiem{/i}"
                            "{i}Ich ruchu były wykonywane z taką gracją, iż cała sala zamarła w zachwycie i zdziwieniu nad nimi{/i}"
                            "{i}Po chwili jednak ludzie zaczeli się dołączać, a Łuszczu i Lilith mogli ich prowadzić w tańcu{/i}"

                            scene bg bal4 with fade
                            $ timer += 15
                            show luszcz bal at slightleft
                            show lilith neutral3 right at slightright

                            lilith "Ohhhh, to było takie cudowne Łuszczu!"
                            lilith "Nie wiedziałam, że potrafisz tak dobrze tańczyć!"

                            if duda_social_link >= 1:
                                luszcz "Emmm nie umiem, ale pewnego razu jeden bardzo madry człowiek powiedział mi, że trzeba się uczyć wszędzie i w każdej sytuacji"
                                luszcz "Więc kopiowałem twoje ruchy i jakoś wyszło..."

                                lilith "To musiałbyć naprawdę mądry człowiek!"

                            else:
                                luszcz "Emmm no coś tam troszkę umiem"

                                lilith "To było wyśmienite, musisz mieć talent!"

                            luszcz "no tak"

                            lilith "..."
                            lilith "To ja wracam do naszego stolika"
                            lilith "Idziesz ze mną?"

                            luszcz "emmmm, jeszcze zobaczę"

                            lilith "Dobrze to jak coś wiesz gdzie mnie szukać"

                            hide lilith
                            show luszcz bal at center

                            luszcz "..."

                            if zyd_social_link > 0:
                                show luszcz bal at slightleft
                                show shinobu neutral at slightright

                                shinobu "O tu jesteś!"
                                shinobu "Widziałam twój taniec i eeee wyglądał troche dziwnie, ale napewno nie był zły"

                                luszcz "yyy eee dziękuje pani Loli?"

                                shinobu "Ehhhh, SHI-NO-BU, Shinobu się nazywam"

                                luszcz "shinobu"

                                shinobu "bardzo ładnie"

                                luszcz "..."

                                shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                luszcz "emmm do mnie?"

                                shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                luszcz "niemiłe"

                                shinobu "niemiłe, ale prawdziwe"

                                luszcz "..."
                                luszcz "zobaczę może przyjdę"

                                shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                shinobu "lepiej żebyś przyszedł!"

                                hide shinobu
                                show luszcz bal at center

                                luszcz "ehhh, ciekawe o co może chodzić"

                            if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                gotka "Ej Łuszczu!"
                                
                                show luszcz bal at slightleft
                                show gotka neutral right at slightright

                                gotka "Masz dla mnie chwilkę?"

                                luszcz "Ja!?"

                                gotka "Tak, ty!"
                                gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                                luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                                gotka "Dobrze, będę czekała przy toaletach"

                                hide gotka
                                show luszcz bal at center

                                luszcz "crazy!"

                            if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                tarczownik "O hej Łuszczu mam sprawę!"

                                show luszcz bal at slightleft
                                show tarczownik neutral at slightright

                                luszcz "O co chodzi?"

                                tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                luszcz "Jakiego towaru!?!?"

                                tarczownik "A czy to ważne?"

                                luszcz "TAK!"

                                tarczownik "zobaczysz na miejscu"
                                tarczownik "To pójdziesz ze mną?"

                                luszcz "eeee zobaczę"

                                tarczownik "To jak coś czekam przy toaletach."

                                hide tarczownik
                                show luszcz bal at center

                                luszcz "WTF? mega crazy"
                            
                            luszcz "..."

                            jump bal3
                        else:
                            if toxic_pea_social_link >= 2 and toxic_pea_social_link < 6:
                                show luszcz bal at slightleft
                                show toxic_pea neutral at slightright

                                toxic "Zatańczymy Macieju_Rel?"

                                luszcz "Emmmm"
                                luszcz "(Trochę to gejowe, ale chyba nie mogę wybżydzać)"
                                luszcz "Jasne"

                                scene bg black with fade
                                "{i}Łuszczu i Toxic Pea zaczęli sunąć po sali tanecznym krokiem{/i}"
                                "{i}Ich ruchu były wykonywane z taką gracją, iż cała sala zamarła w zachwycie nad nimi{/i}"
                                "{i}Po chwili jednak ludzie zaczeli się dołączać, a Łuszczu i Toxic Pea mogli ich prowadzić w tańcu{/i}"

                                scene bg bal4 with fade
                                $ timer += 15
                                show luszcz bal at slightleft
                                show toxic_pea neutral at slightright

                                toxic "Ohhhh, to było takie cudowne mój ty kociaku!"
                                toxic "Nie wiedziałam, że potrafisz tak dobrze tańczyć!"

                                if duda_social_link >= 1:
                                    luszcz "Emmm nie umiem, ale pewnego razu jeden bardzo madry człowiek powiedział mi, że trzeba się uczyć wszędzie i w każdej sytuacji"
                                    luszcz "Więc kopiowałem twoje ruchy i jakoś wyszło..."

                                    toxic "To musiałbyć naprawdę mądry człowiek!"

                                else:
                                    luszcz "Emmm no coś tam troszkę umiem"

                                    toxic "To było wyśmienite, musisz mieć talent!"
                                
                                luszcz "no tak"

                                toxic "..."
                                toxic "To ja wracam do naszego stolika stolika czy coś"
                                toxic "Idziesz ze mną?"

                                luszcz "emmmm, jeszcze zobaczę"

                                toxic "Dobrze to jak coś wiesz gdzie mnie szukać"
                                
                                show toxic_pea at center

                                "{i}Toxic Pea klepnął Łuszczu w pośladek{/i}"

                                hide toxic_pea
                                show luszcz bal at center

                                luszcz "eghhh"

                                if zyd_social_link > 0:
                                    show luszcz bal at slightleft
                                    show shinobu neutral at slightright

                                    shinobu "O tu jesteś!"
                                    shinobu "Widziałam twój taniec i eeee nie wiedziałam, że jednak gustujesz w facetach, ale no taniec napewno nie był zły"

                                    luszcz "yyy eee dziękuje pani Loli?"

                                    shinobu "Ehhhh, SHI-NO-BU, Shinobu się nazywam"

                                    luszcz "shinobu"

                                    shinobu "bardzo ładnie"

                                    luszcz "..."

                                    shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                    luszcz "emmm do mnie?"

                                    shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                    luszcz "niemiłe"

                                    shinobu "niemiłe, ale prawdziwe"

                                    luszcz "..."
                                    luszcz "zobaczę może przyjdę"

                                    shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                    shinobu "lepiej żebyś przyszedł!"

                                    hide shinobu
                                    show luszcz bal at center

                                    luszcz "ehhh, ciekawe o co może chodzić"

                                if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                    gotka "Ej Łuszczu!"
                                    
                                    show luszcz bal at slightleft
                                    show gotka neutral right at slightright

                                    gotka "Masz dla mnie chwilkę?"

                                    luszcz "Ja!?"

                                    gotka "Tak, ty!"
                                    gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                                    luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                                    gotka "Dobrze, będę czekała przy toaletach"

                                    hide gotka
                                    show luszcz bal at center

                                    luszcz "crazy!"

                                if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                    tarczownik "O hej Łuszczu mam sprawę!"

                                    show luszcz bal at slightleft
                                    show tarczownik neutral at slightright

                                    luszcz "O co chodzi?"

                                    tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                    tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                    luszcz "Jakiego towaru!?!?"

                                    tarczownik "A czy to ważne?"

                                    luszcz "TAK!"

                                    tarczownik "zobaczysz na miejscu"
                                    tarczownik "To pójdziesz ze mną?"

                                    luszcz "eeee zobaczę"

                                    tarczownik "To jak coś czekam przy toaletach."

                                    hide tarczownik
                                    show luszcz bal at center

                                    luszcz "WTF? mega crazy"
                                
                                luszcz "..."

                                jump bal3
                            else:
                                if gotka_szpont == 1 and gotka_social_link < 10:
                                    show luszcz bal at slightleft
                                    show gotka neutral right at slightright

                                    gotka "Zatańczymy moja świnko morska?"

                                    luszcz "Oczywiście, że tak gigasigmo!"
                                    scene bg black with fade
                                    "{i}Łuszczu i Gotka zaczęli sunąć po sali tanecznym krokiem{/i}"
                                    "{i}Ich ruchu były wykonywane z taką gracją, iż cała sala zamarła w zachwycie nad nimi{/i}"
                                    "{i}Po chwili jednak ludzie zaczeli się dołączać, a Łuszczu i Gotka mogli ich prowadzić w tańcu{/i}"

                                    scene bg bal4 with fade
                                    $ timer += 15
                                    show luszcz bal at slightleft
                                    show gotka neutral right at slightright

                                    gotka "Ohhhh, to było takie cudowne Łuszczu!"
                                    gotka "Nie wiedziałam, że potrafisz tak dobrze tańczyć!"

                                    if duda_social_link >= 1:
                                        luszcz "Emmm nie umiem, ale pewnego razu jeden bardzo madry człowiek powiedział mi, że trzeba się uczyć wszędzie i w każdej sytuacji"
                                        luszcz "Więc kopiowałem twoje ruchy i jakoś wyszło..."

                                        gotka "To musiałbyć naprawdę mądry człowiek!"

                                    else:
                                        luszcz "Emmm no coś tam troszkę umiem"

                                        gotka "To było wyśmienite, musisz mieć talent!"
                                    
                                    if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                        gotka "A właśnie Łuszczu, jest sprawa"
                                        gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"
                                        gotka "Nie wystawisz przecież swojej dziewczyny co nie?"

                                        luszcz "emmm sorki jeszcze zobaczę mój alfa wilku"

                                        gotka "Łuszczu!"

                                        luszcz "No spróbuję, no raczej tak..."

                                        gotka "To czekam przy toaletach"
                                        gotka "Jak będziesz gotowy to przyjdź"

                                        hide gotka
                                        show luszcz bal at center

                                        luszcz "ufff"
                                    
                                    else:
                                        luszcz "no tak"

                                        gotka "..."
                                        gotka "To ja wracam do naszego stolika"
                                        gotka "Idziesz ze mną?"

                                        luszcz "emmmm, jeszcze zobaczę"

                                        gotka "Dobrze to jak coś wiesz gdzie mnie szukać"

                                        hide gotka
                                        show luszcz bal at center

                                        luszcz "..."

                                    if zyd_social_link > 0:
                                        show luszcz bal at slightleft
                                        show shinobu neutral at slightright

                                        shinobu "O tu jesteś!"
                                        shinobu "Widziałam twój taniec i nie powiem, był niezły"

                                        luszcz "Dziękuje pani Loli"

                                        shinobu "Ehhhh, SHI-NO-BU, Shinobu się nazywam"

                                        luszcz "shinobu"

                                        shinobu "bardzo ładnie"

                                        luszcz "..."

                                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                        luszcz "emmm do mnie?"

                                        shinobu "Też mnie dziwi, że mój pan chce się zadawać z kimś takim jak ty"

                                        luszcz "niemiłe"

                                        shinobu "niemiłe, ale prawdziwe"

                                        luszcz "..."
                                        luszcz "zobaczę może przyjdę"

                                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                        shinobu "lepiej żebyś przyszedł!"

                                        hide shinobu
                                        show luszcz bal at center

                                        luszcz "ehhh, ciekawe o co może chodzić"

                                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                        tarczownik "O hej Łuszczu mam sprawę!"

                                        show luszcz bal at slightleft
                                        show tarczownik neutral at slightright

                                        luszcz "O co chodzi?"

                                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                        luszcz "Jakiego towaru!?!?"

                                        tarczownik "A czy to ważne?"

                                        luszcz "TAK!"

                                        tarczownik "zobaczysz na miejscu"
                                        tarczownik "To pójdziesz ze mną?"

                                        luszcz "eeee zobaczę"

                                        tarczownik "To jak coś czekam przy toaletach."

                                        hide tarczownik
                                        show luszcz bal at center

                                        luszcz "WTF? mega crazy"
                                    
                                    luszcz "..."

                                    jump bal3


                                else:
                                    luszcz "troszke siara, nie ma z kim tańczyć :("
                                    luszcz "Emmm to ja chyba wrócę do stołu..."

                                    $ timer += 15

                                    if zyd_social_link > 0:
                                        shinobu "Stój gdzie stoisz patałachu!"

                                        show luszcz bal at slightleft
                                        show shinobu neutral at slightright

                                        luszcz "O pani Loli."

                                        shinobu "Ehhhh, SHI-NO-BU, Shinobu się nazywam"

                                        luszcz "shinobu"

                                        shinobu "bardzo ładnie"

                                        luszcz "..."

                                        shinobu "Mój Pan Cię wzywa na spotkanie. Ma do Ciebie pewną poufną sprawę."

                                        luszcz "emmm do mnie?"

                                        shinobu "Też mnie dziwi, że mój pan chce się zadawać z takim śmieciem jak ty"

                                        luszcz "niemiłe"

                                        shinobu "niemiłe, ale prawdziwe"

                                        luszcz "..."
                                        luszcz "zobaczę może przyjdę"

                                        shinobu "mój pan będzie w strefie ViP w sali jadalnej"
                                        shinobu "lepiej żebyś przyszedł!"

                                        hide shinobu
                                        show luszcz bal at center

                                    if gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                                        gotka "Ej Łuszczu!"
                                        
                                        show luszcz bal at slightleft
                                        show gotka neutral right at slightright

                                        gotka "Masz dla mnie chwilkę?"

                                        luszcz "Ja!?"

                                        gotka "Tak, ty!"
                                        gotka "Potrzebuję, żebyś gdzieś ze mną poszedł"

                                        luszcz "emmm zobaczę mamo, bo mam coś innego jeszcze do zrobienia"

                                        gotka "Dobrze, będę czekała przy toaletach"

                                        hide gotka
                                        show luszcz bal at center

                                        luszcz "crazy!"
                                    
                                    if tarczownik_sojusznik == 1 and gotka_social_link < 10:
                                        tarczownik "Hej Łuszczu mam sprawę!"

                                        show luszcz bal at slightleft
                                        show tarczownik neutral at slightright

                                        luszcz "O co chodzi?"

                                        tarczownik "Eeeeem załatwiłem sobię troszkę towaru..."
                                        tarczownik "ale trochę boję się od kogo go dostanę i eee byłbym wdzięczny jeśli poszedłbyś ze mną..."

                                        luszcz "Jakiego towaru!?!?"

                                        tarczownik "A czy to ważne?"

                                        luszcz "TAK!"

                                        tarczownik "zobaczysz na miejscu"
                                        tarczownik "To pójdziesz ze mną?"

                                        luszcz "eeee zobaczę"

                                        tarczownik "To jak coś czekam przy toaletach."

                                        hide tarczownik
                                        show luszcz bal at center

                                        luszcz "WTF? mega crazy"
                                    
                                    luszcz "..."

                                    jump bal3
 
    label bal3:
        menu:
            "{b}Co, by tu zrobić?{/b}"

            "{b}Spotkaj się z Ambasadorem{/b}" if 9900 <= timer <= 9915 and zyd_social_link > 0 and btask1 == 0:
                luszcz "(Pójdę zobaczyć po co wzywa mnie Ambasador)"
                jump btask1
            
            "{b}Spotkaj się z Gotką{/b}" if 9900 <= timer <= 9915 and gotka_social_link >= 1 and gotka_social_link < 10 and tarczownik_social_link >= 1 and tarczownik_social_link <= 2:
                ""
                jump btask2
            
            "{b}Spotkaj się z Naofumim{/b}" if 9900 <= timer <= 9915 and tarczownik_sojusznik == 1 and gotka_social_link < 10:
                ""
                jump btask3
            
            "{b}Spotkaj się z Żydem{/b}" if timer >= 9915 and timer <= 9930 and zyd_sojusznik == 1 and grzegorz == 1:
                ""
                jump btask4
            
            "{b}Wróć do stolika{/b}":
                scene bg black with fade
                jump bal4

    label bal4:
        




    label btask1:
        $ btask1 = 1
        stop music
        scene bg black with fade
        scene bg bal6 with fade
        $ timer += 15
        play music "audio/music/sonata11.mp3"
        $ renpy.music.set_volume(1.0, delay=0.3)
        
        show luszcz bal zorder 12 at left

        luszcz "Emmmm to chyba tutaj..."

        show shinobu neutral at center

        shinobu "o przyszedłeś!"
        shinobu "poczekaj jeszcze chwilkę, mój pan kończy własnie negocjacje"

        scene bg bal6 with fastfade

        show eryk neutral at right
        show tusk neutral right at center
        show nawrocki neutral right at left 

        eryk "No to co, mamy deal?"

        tusk "Mamy deal"
        tusk "Współpraca z Panem to czysta przyjemność"

        show tusk neutral right:
            xalign 0.5
            yalign 1.0
            easeout 0.2 xalign 0.0
        show nawrocki neutral right:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign 0.5

        nawrocki "Nie, nie możliwość współpracy z Panem to dar od niebios"

        show tusk neutral right:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign 0.5
        show nawrocki neutral right:
            xalign 0.5
            yalign 1.0
            easeout 0.2 xalign 0.0

        tusk "Nein, nein możliwość rozmowy z Panem to dla mnie łaska, na którą nie zasługuję."

        eryk "dobra, dobra już"
        eryk "Macie tu umowę, podpiszcie ją i mi dostarczcie do końca balu"
        
        "{i}Eryk przekazuje umowę gospodarczą Tuskowi{/i}"

        tusk "Tak będzie Panie Ambasadorze"
        nawrocki "Twe życzenie mym rozkazem"

        show tusk neutral:
            xalign 0.5
            yalign 1.0
            easeout 0.35 xalign -0.5

        show nawrocki neutral:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign -0.5

        eryk "ehhh, co ja z nimi mam..."

        show shinobu neutral right at center
        show luszcz bal at left

        eryk "Ohhhh Shinobu!"

        shinobu "Przyprowadziłam tego o którego prosiłeś"

        eryk "Witaj Macieju Łuszczu!"

        show luszcz bal:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign 0.5

        show shinobu neutral right:
            xalign 0.5
            yalign 1.0
            easeout 0.2 xalign 0.0

        luszcz "Skąd znasz moje imię!?"

        eryk "Dużo o tobie słyszałem Macieju"
        eryk "Podobno nawet zaprzyjaźniłeś się z samym Grzegorzem"

        luszcz "Grzegorzem?"

        eryk "Braunem!"

        if zly_zyd == 1:
            luszcz "Ahhh nie no ja tam tylko z nim wypędziełem jakiegoś głupiego żyda ze sklepu"
            luszcz "Jestem zwolenikiem liberalizmu gospodarczego więc uważam, że jeśli ktoś nie chce komuś czegoś sprzedać to ma do tego pełne prawo!"
        
        else:
            luszcz "Emmmm, nie wiem czy można to nazwać przyjaźnią"
            luszcz "Obiłem mu mordę broniąc jakiegoś żyda przed dyskriminacją i mu to troche zaimponowało."
        
        eryk "Oj tam, oj tam, nie umniejszaj sobie!"

        luszcz "..."

        eryk "A, a, a jaki on teraz jest!?"

        luszcz "Eeeee Braun?"

        luszcz "No nie wiem no zachowuje się jak Braun no"

        eryk "..."

        show shinobu neutral right:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign 0.5

        show luszcz bal:
            xalign 0.5
            yalign 1.0
            easeout 0.2 xalign 0.0

        shinobu "Panie, powinieneś mu powiedzieć!"

        eryk "Ale emmm, ale napewno?"

        shinobu "Jeżeli chcesz go odzyskać to będzie potrzebował pomocy tego człowieka"

        eryk "ehhh"

        show luszcz bal:
            xalign 0.0
            yalign 1.0
            easeout 0.2 xalign 0.5

        show shinobu neutral right:
            xalign 0.5
            yalign 1.0
            easeout 0.2 xalign 0.0
        
        eryk "Macieju, prawda jest taka, że ja jestem w związku małżeńskim z Grzegorzem!"

        luszcz "chwila co!???"

        if zly_zyd == 0:
            luszcz "(hmmm choć w sumie podczas naszej walki coś o tym wspomniał)"
        
        eryk "Znaczy jesteśmy teorytycznie w związku małżeńskim"
        eryk "Bo już po ślubie, gdy Grzegorz dowiedział się, że mam korzenie żydowskie i że jestem facetem zostawił mnie i przyleciał tu do Skały"

        luszcz "Jezus maria, co za powalona historia"

        eryk "No trochę rel"
        eryk "Ale wracając do tematu, to mam do Ciebie ogromną prośbę"
        eryk "Czy pomógłbyś mi przekonać Brauna do powrotu do mnie?"

        menu:
            "{b}Czy pomóc Erykowi?{/b}"

            "{b}Tak{/b}":
                luszcz "Dobrze, pomogę Ci"

                eryk "Oh, dziękuję Ci Macieju"

                show shinobu neutral right:
                    xalign 0.0
                    yalign 1.0
                    easeout 0.2 xalign 0.5

                show luszcz bal:
                    xalign 0.5
                    yalign 1.0
                    easeout 0.2 xalign 0.0

                shinobu "W takim razie skoro wszystko ustalone to pospieszmy się zanim Braun opuści Bal!"

                luszcz "Chwila on tu jest!?"

                show shinobu neutral

                shinobu "Tak, użyliśmy podstępu, żeby go zwabić, ale pewnie już wie kto organizuje ten Bal"

                luszcz "To w drogę!"

                stop music
                scene bg black with fade
                scene bg bal2 with fade 
                show luszcz bal at center
                show shinobu neutral right at left 
                show eryk neutral at right

                luszcz "Gdzie on jest!?"
                luszcz "..."
                luszcz "Tam widzę go!"

                scene bg bal2 with fastfade 
                play music "audio/music/bal.mp3"
                $ renpy.music.set_volume(0.5, delay=0.3)
                $ timer += 15

                show luszcz bal at slightleft
                show braun neutral right at right

                luszcz "Panie Braun niech pan zaczeka!"

                show braun neutral 

                braun "O co chodzi Łuszczu?"

                show shinobu neutral right zorder 3:
                    xalign -0.75
                    yalign 1.0
                    easeout 0.4 xalign 0.0

                show luszcz bal zorder 5:
                    xalign 0.25
                    yalign 1.0
                    easeout 0.2 xalign 0.5

                show eryk neutral right zorder 4:
                    xalign -0.5
                    yalign 1.0
                    easeout 0.4 xalign 0.25

                braun "..."
                braun "Muszę iść."

                show braun neutral right

                luszcz "Braun zaczekaj!"
                luszcz "On się zmienił!"

                show braun neutral

                if zly_zyd == 1:
                    with vpunch
                    braun "Tego nie da się zmienić!"
                    $ renpy.pause(0.2)
                    show braun neutral right zorder 4:
                        xalign 1.0
                        yalign 1.0
                        easeout 0.4 xalign 1.5
                    luszcz "..."
                    show luszcz bal right at right 
                    show eryk neutral at center
                    luszcz "Emmm, chyba naprawdę nie chcę Ciebie znać..."

                    eryk "Ahhh wiedziałem, wiedziałem..."
                    eryk "On jest dla mnie za dobry"
                    eryk "To wszystko moja wina!"
                    eryk "..."
                    eryk "..."
                    eryk "..."
                    eryk "Dziękuje Macieju za chęci, ale muszę na chwile pobyć sam"

                    hide eryk 
                    show shinobu neutral right at slightleft
                    show luszcz bal right at slightright
                    shinobu "..."
                    shinobu "ja, ja chyba za nim pójdę..."
                    shinobu "to eee ja spadam"
                    hide shinobu 
                    show luszcz bal right at center

                    luszcz "..."
                    luszcz "nie wyszły troszke te mediacje"
                    luszcz "..."

                else:
                    $ bralus = 1
                    braun "ahhh czyli już wiesz?"

                    luszcz "Powiedzieli mi..."
                    luszcz "On się naprawde zmienił"
                    luszcz "Daj mu chociaż szansę się wytłumaczyć"

                    braun "..."

                    braun "Gdyby ktoś inny mnie o to spytał to bym odmówił..."
                    braun "Ale dla Ciebie Łuszczu zrobię wyjątek"

                    show luszcz bal zorder 3:
                        xalign 0.5
                        yalign 1.0
                        easeout 0.4 xalign 1.0

                    show braun neutral zorder 5:
                        xalign 1.0
                        yalign 1.0
                        easeout 0.2 xalign 0.75
                    
                    $ renpy.pause(0.3)

                    show luszcz bal right zorder 3

                    eryk "..."

                    braun "..."

                    eryk "proszę wróć"

                    braun "nie mogę"
                    braun "moje przekonania nie pozwalają mi być w związku z żydem"

                    eryk "A jeśli bym nim nie był?"

                    braun "..!?"
                    braun "Jak to?"

                    eryk "Po tym jak nas opuściłeś zacząłem starania o obywatelstwo japońskie..."
                    eryk "i tak się stało, teraz jestem japończykiem."

                    braun "naprawde!?!?!?"
                    braun "..."
                    braun "ale nadal jesteś mężczyzną..."

                    eryk "a co do tego..."

                    show eryk neutral2

                    eryk "to, to też się zmieniło!"

                    luszcz "(Jezus maria, co się dzieje!?)"

                    braun "Ohhh, Eryk..."
                    braun "Eryka..."

                    eryk "Grzegorzu..."

                    show eryk neutral3

                    eryk "Czy wrócisz do mnie?"

                    braun "..."
                    braun "Tak!"

                    eryk "Kocham Cię Grzegorzu!"
                    braun "Też Cię kocham Eryko!"

                    show eryk neutral4 zorder 6:
                        xalign 0.25
                        yalign 1.0
                        easeout 0.5 xalign 0.40
                    
                    show braun neutral zorder 5:
                        xalign 0.75
                        yalign 1.0
                        easeout 0.5 xalign 0.60
                    
                    $ renpy.pause(0.5)

                    scene bg black with fade
                    "{i}Grzegorz Braun i Eryk (Eryka?) pocałowali się{/i}"
                    scene bg bal2 with fade
                    show shinobu neutral right at left 
                    show eryk neutral2 zorder 3:
                        xalign 0.32
                        yalign 1.0
                    show braun neutral zorder 2:
                        xalign 0.68
                        yalign 1.0
                    show luszcz bal right at right 

                    braun "Idę spakować moję rzeczy skarbie"

                    eryk "Dobrze kochany, będe oczekiwała twojego powrotu!"
                    hide braun
                    show eryk neutral2 at center
                    luszcz "emmmm, nie wiedziałem, ze jesteś kobietą..."

                    eryk "Wiedziałem, że Braun ma problem z moją płcią"
                    eryk "Dlatego przeszedłem dla niego korektę płci"

                    luszcz "..."
                    luszcz "Musisz go bardzo kochać"

                    eryk "to prawda"
                    eryk "..."

                    luszcz "..."
                    
                    eryk "To eeee my sobie pójdziemy"
                    eryk "Dzięki za pomoc Macieju"

                    luszcz "emmm nie ma za co"

                    hide shinobu 
                    hide eryk 
                    show luszcz bal right at center

                    luszcz "troche"
                    luszcz "crazy"
                
                if timer >= 9930 and timer <= 9945:
                    tusk "Nein, nein, nein"

                    luszcz "..?"
                    show tusk neutral right at slightleft

                    with hpunch

                    if slownik == 1:
                        "{i}Donald Tusk uderzył Łuszcza z bara wytrącając z jego kieszeni rozmówki polsko-chińskie{/i}"

                        show tusk neutral right at left

                        tusk "Ohhh, Entschuldigung. Ich werde es hochheben."

                        "{i}Donald Tusk pochylił się, by podnieść rozmówki polsko-chińskie, gdy nagle zamarł w miejscu{/i}"

                        tusk "Co... co to jest?"

                        luszcz "Eeeee, a to jedynie moje rozmówki polsko-chiń..."

                        tusk "Tak! Tego potrzebujemy!"

                        if crac == 1:
                            tusk "Młody człowieku, jak się nazy..."
                            tusk "Ohhh, to ty..."

                            luszcz "Tak to ja Panie Premierze"
                            luszcz "Człowiek, którego chcial Pan pobić w lesie!"

                            tusk "..."
                            tusk "Słuchaj młody"
                            tusk "Okazuje się, że bardzo pilnie Ciebie potrzebuję w tym momeńcie"
                            tusk "Dlatego co ty na to, że dam Ci z 2 portfele, a ty w zamian za to zapomnisz o wszystkim i mi pomożesz?"

                            menu:
                                "{b}Zgódź się{/b}":
                                    luszcz "Niech będzie"

                                    tusk "Dobra to masz tu jeden portfel, a drugi dostaniesz po wykonaniu zadania"

                                    $ money += 1
                                    "{i}*do ekwipunku został dodany 1 portfel*{/i}"

                                    tusk "Czekam na Ciebie w sali jadalnej Vip"
                                    tusk "Lepiej żebyś przyszedł!"

                                    hide tusk

                                    luszcz "wtf? co to było?"
                                
                                "{b}Nie zgadzaj się{/b}":
                                    luszcz "Nie"

                                    tusk "Jak to nie?"
                                    tusk "Przecież zapłacę Ci!"

                                    luszcz "Nie i huj"

                                    tusk "Ahhh tak?"
                                    tusk "TO! TO!"
                                    tusk "to dowidzenia"

                                    hide tusk
                                    
                                    luszcz "wtf? co to było?"
                                
                                "{b}Negocjuj{/b}":
                                    luszcz "To za mało, więcej to ja dostaje kieszonkowego"
                                    luszcz "4 portfele i ci pomoge"

                                    tusk "Niech będzie"
                                    tusk "Masz tu 2 portfele z góry"

                                    $ money += 2
                                    "{i}*do ekwipunku zostały dodane 2 portfele*{/i}"

                                    tusk "A pozostałe 2 dostaniesz po robocie"
                                    tusk "Czekam na Ciebie w sali jadalnej Vip"
                                    tusk "Lepiej żebyś przyszedł!"

                                    hide tusk

                                    luszcz "wtf? co to było?"
                        
                        else:
                            tusk "Młody człowieku, jak się nazywasz?"

                            luszcz "Maciej Łuszcz?"

                            tusk "Macieju, państwo Polskie Ciebie potrzebuje!"

                            luszcz "mnie?"

                            tusk "Tak Ciebie!"

                            tusk "Przyjdź jak najszybciej do strefy Vip w jadalni"
                            tusk "Mam dla ciebie misję od której zależą losy kraju!"

                            hide tusk

                            luszcz "wtf? co to było?"


                    else:   
                        "{i}Donald Tusk uderzył Łuszcza z bara{/i}"

                        show tusk neutral right at left

                        tusk "Ohhh, Entschuldigung. Es war nichts Besonderes."

                        if crac == 1 or smolensklil == 1:
                            luszcz "Mr. Tusk? I have a question for you."

                            menu:
                                "{b}Co zrobić?{/b}"

                                "{b}Zaszantażuj Tuska{/b}":
                                    if smolensklil == 1:
                                        luszcz "Co robił Pan 10 kwietnia 2010 roku?"

                                        tusk "Emmmm, nic niezwykłego"

                                        luszcz "Panie Tusku ja wiem"
                                        luszcz "To Pan zasadził niewidzialne brzozy, w które uderzył Tupolew!"

                                        tusk "Jezus maria"
                                        tusk "ciszej, ciszej!"
                                        tusk "Czego chcesz? Dam ci wszystko!"

                                        luszcz "Hajs"
                                        luszcz "Dużo Hajsu!"

                                        tusk "Dobra już, już daje"

                                        $ money += 5
                                        "{i}*do ekwipunku zostało dodane 5 portfeli*{/i}"

                                        tusk "No to eeee ja idę i pamietaj ty o niczym nie wiesz!"

                                        hide tusk

                                        luszcz "kocham szantaż"
                                    else:
                                        if crac == 1:
                                            luszcz "Czemu bije Pan ludzi w lesie?"

                                            tusk "Awwww shit, to ty!"

                                            luszcz "Tak to ja"

                                            tusk "Emmm, emmm słuchaj no młody"
                                            tusk "Każdy musi się czasami jakoś wyluzować tak?"

                                            luszcz "..."

                                            tusk "Dobra zapłacę ci"
                                            tusk "2 portfele i nie ma sprawy"

                                            luszcz "..."
                                            luszcz "niech będzie"

                                            $ money += 2
                                            "{i}*do ekwipunku zostały dodane 2 portfele*{/i}"

                                            tusk "No to ja idę i pamietaj ty o niczym nie wiesz!"

                                            hide tusk

                                            luszcz "kocham szantaż"

                                "{b}Lepiej nie{/b}":
                                    luszcz "jednak nic"

                                    tusk "..?"

                                    hide tusk 

                                    luszcz "debil"

                        else:
                            luszcz "Ez is niet pasat"

                            tusk "..?"

                            hide tusk 

                            luszcz "Aghhhh, wiedziałem, że powinienem bardziej uważać na niemieckim..."

                if timer == 9930 and zyd_sojusznik == 1 and grzegorz == 1:
                    zyd "Łuszczu! Łuszczu!"

                    show zyd neutral at slightleft
                    show luszcz bal right at slightright
                    zyd "Łuszczu jest sprawa!"
                    zyd "Potrzebuję twojej pomocy z pewną sprawą"

                    luszcz "Jaką sprawą?"

                    zyd "Mam interes, duży interes i potrzebuję twojej pomocy!"

                    luszcz "Ahhh rozumiem potrzebujesz, żebym Ci pomógł w negocjacjach!"

                    zyd "Nie, nie co ty"
                    zyd "Potrzebuję jedynie słupa"

                    luszcz "aha..."

                    zyd "To co pomożesz?"

                    luszcz "zobaczę"

                    zyd "To jakby co czekam przy wyjściu"

                    zyd "Nie zawiedź mnie!"

                    hide zyd 
                    show luszcz bal right at center

                    luszcz "że co, że ja niby nie umiem negocjować!?"
                    luszcz "ehhh mega nie miłe"
                
                if timer == 9930:
                    play sound "audio/sfx/door2.mp3"
                    with hpunch
                    "{i}Nagle usłyszałeś dźwięk otwieranych drzwi i zauważyłeś, że ktoś zszedł do piwnicy{/i}"
                    luszcz "WTF? Ciekawe co jest w piwnicy..."
                    luszcz "anyway"

                if timer == 9945 and eminem_sojusznik == 1:
                    cid "Łuszczu! Łuszczu!"

                    show eminem neutral right at slightleft
                    show luszcz bal right at slightright
                    cid "Łuszczu jest turniej!"

                    luszcz "turniej?"
                    luszcz "jaki turniej?"

                    cid "Turniej rycerski!"
                    cid "Na dziedzincu będą walki!"

                    luszcz "Fajnie"
                    luszcz "Bierzesz udział?"

                    cid "Chciałbym, ale nie mogę się ujawniać z moją potęgą"

                    luszcz "A gdybyś był pod przykrywką?"

                    cid "Mysłałem o tym"
                    cid "ale moja BRAKUJĄCA RĘKA za bardzo zdradza kim jestem!"

                    luszcz "..."
                    luszcz "sory"

                    cid "..."
                    cid "Już wiem!"
                    cid "W ramach zadośćuczynienia ty możesz wziąć udział zamiast mnie!"

                    luszcz "Emmm po co?"
                    
                    cid "Bo to fajne jest"
                    cid "ekscytujące"

                    cid "no zobaczysz no będzie bomba!"

                    luszcz "Emmm no nie wiem"
                    luszcz "jeszcze zobaczę"

                    cid "Dobra to jak coś to czekam na dziedzińcu!"

                    hide eminem
                    show luszcz bal right at center

                    luszcz "skibidi gyat"

                luszcz "..."
                jump bal3

            "{b}Nie{/b}":
                luszcz "Emmm nie chciałbym się mieszać w sprawy innych..."

                eryk "Ehhh, no cóż rozumiem"

                eryk "W takim razie żegnaj Macieju"

                luszcz "Dowidzenia, Panie Ambasadorze"

                scene bg bal7 with fade
                play music "audio/music/bal.mp3"
                $ renpy.music.set_volume(0.75, delay=0.3)
                show luszcz bal at center

                luszcz "emmm co, by tu teraz..."

                if timer >= 9930 and timer <= 9945:
                    tusk "Nein, nein, nein"

                    luszcz "..?"
                    show tusk neutral at slightright

                    with hpunch

                    if slownik == 1:
                        "{i}Donald Tusk uderzył Łuszcza z bara wytrącając z jego kieszeni rozmówki polsko-chińskie{/i}"

                        show tusk neutral at right

                        tusk "Ohhh, Entschuldigung. Ich werde es hochheben."

                        "{i}Donald Tusk pochylił się, by podnieść rozmówki polsko-chińskie, gdy nagle zamarł w miejscu{/i}"

                        tusk "Co... co to jest?"

                        luszcz "Eeeee, a to jedynie moje rozmówki polsko-chiń..."

                        tusk "Tak! Tego potrzebujemy!"

                        if crac == 1:
                            tusk "Młody człowieku, jak się nazy..."
                            tusk "Ohhh, to ty..."

                            luszcz "Tak to ja Panie Premierze"
                            luszcz "Człowiek, którego chcial Pan pobić w lesie!"

                            tusk "..."
                            tusk "Słuchaj młody"
                            tusk "Okazuje się, że bardzo pilnie Ciebie potrzebuję w tym momeńcie"
                            tusk "Dlatego co ty na to, że dam Ci z 2 portfele, a ty w zamian za to zapomnisz o wszystkim i mi pomożesz?"

                            menu:
                                "{b}Zgódź się{/b}":
                                    luszcz "Niech będzie"

                                    tusk "Dobra to masz tu jeden portfel, a drugi dostaniesz po wykonaniu zadania"

                                    $ money += 1
                                    "{i}*do ekwipunku został dodany 1 portfel*{/i}"

                                    tusk "Czekam na Ciebie w sali jadalnej Vip"
                                    tusk "Lepiej żebyś przyszedł!"

                                    hide tusk

                                    luszcz "wtf? co to było?"
                                
                                "{b}Nie zgadzaj się{/b}":
                                    luszcz "Nie"

                                    tusk "Jak to nie?"
                                    tusk "Przecież zapłacę Ci!"

                                    luszcz "Nie i huj"

                                    tusk "Ahhh tak?"
                                    tusk "TO! TO!"
                                    tusk "to dowidzenia"

                                    hide tusk
                                    
                                    luszcz "wtf? co to było?"
                                
                                "{b}Negocjuj{/b}":
                                    luszcz "To za mało, więcej to ja dostaje kieszonkowego"
                                    luszcz "4 portfele i ci pomoge"

                                    tusk "Niech będzie"
                                    tusk "Masz tu 2 portfele z góry"

                                    $ money += 2
                                    "{i}*do ekwipunku zostały dodane 2 portfele*{/i}"

                                    tusk "A pozostałe 2 dostaniesz po robocie"
                                    tusk "Czekam na Ciebie w sali jadalnej Vip"
                                    tusk "Lepiej żebyś przyszedł!"

                                    hide tusk

                                    luszcz "wtf? co to było?"
                        
                        else:
                            tusk "Młody człowieku, jak się nazywasz?"

                            luszcz "Maciej Łuszcz?"

                            tusk "Macieju, państwo Polskie Ciebie potrzebuje!"

                            luszcz "mnie?"

                            tusk "Tak Ciebie!"

                            tusk "Przyjdź jak najszybciej do strefy Vip w jadalni"
                            tusk "Mam dla ciebie misję od której zależą losy kraju!"

                            hide tusk

                            luszcz "wtf? co to było?"


                    else:   
                        "{i}Donald Tusk uderzył Łuszcza z bara{/i}"

                        show tusk neutral at right

                        tusk "Ohhh, Entschuldigung. Es war nichts Besonderes."

                        if crac == 1 or smolensklil == 1:
                            luszcz "Mr. Tusk? I have a question for you."

                            menu:
                                "{b}Co zrobić?{/b}"

                                "{b}Zaszantażuj Tuska{/b}":
                                    if smolensklil == 1:
                                        luszcz "Co robił Pan 10 kwietnia 2010 roku?"

                                        tusk "Emmmm, nic niezwykłego"

                                        luszcz "Panie Tusku ja wiem"
                                        luszcz "To Pan zasadził niewidzialne brzozy, w które uderzył Tupolew!"

                                        tusk "Jezus maria"
                                        tusk "ciszej, ciszej!"
                                        tusk "Czego chcesz? Dam ci wszystko!"

                                        luszcz "Hajs"
                                        luszcz "Dużo Hajsu!"

                                        tusk "Dobra już, już daje"

                                        $ money += 5
                                        "{i}*do ekwipunku zostało dodane 5 portfeli*{/i}"

                                        tusk "No to eeee ja idę i pamietaj ty o niczym nie wiesz!"

                                        hide tusk

                                        luszcz "kocham szantaż"
                                    else:
                                        if crac == 1:
                                            luszcz "Czemu bije Pan ludzi w lesie?"

                                            tusk "Awwww shit, to ty!"

                                            luszcz "Tak to ja"

                                            tusk "Emmm, emmm słuchaj no młody"
                                            tusk "Każdy musi się czasami jakoś wyluzować tak?"

                                            luszcz "..."

                                            tusk "Dobra zapłacę ci"
                                            tusk "2 portfele i nie ma sprawy"

                                            luszcz "..."
                                            luszcz "niech będzie"

                                            $ money += 2
                                            "{i}*do ekwipunku zostały dodane 2 portfele*{/i}"

                                            tusk "No to ja idę i pamietaj ty o niczym nie wiesz!"

                                            hide tusk

                                            luszcz "kocham szantaż"

                                "{b}Lepiej nie{/b}":
                                    luszcz "jednak nic"

                                    tusk "..?"

                                    hide tusk 

                                    luszcz "debil"

                        else:
                            luszcz "Ez is niet pasat"

                            tusk "..?"

                            hide tusk 

                            luszcz "Aghhhh, wiedziałem, że powinienem bardziej uważać na niemieckim..."

                if timer >= 9915 and timer <= 9930 and zyd_sojusznik == 1 and grzegorz == 1:
                    zyd "Łuszczu! Łuszczu!"

                    show zyd neutral right at slightright
                    show luszcz bal at slightleft
                    zyd "Łuszczu jest sprawa!"
                    zyd "Potrzebuję twojej pomocy z pewną sprawą"

                    luszcz "Jaką sprawą?"

                    zyd "Mam interes, duży interes i potrzebuję twojej pomocy!"

                    luszcz "Ahhh rozumiem potrzebujesz, żebym Ci pomógł w negocjacjach!"

                    zyd "Nie, nie co ty"
                    zyd "Potrzebuję jedynie słupa"

                    luszcz "aha..."

                    zyd "To co pomożesz?"

                    luszcz "zobaczę"

                    zyd "To jakby co czekam przy wyjściu"

                    zyd "Nie zawiedź mnie!"

                    hide zyd 
                    show luszcz bal at center

                    luszcz "że co, że ja niby nie umiem negocjować!?"
                    luszcz "ehhh mega nie miłe"
                
                if timer == 9930:
                    play sound "audio/sfx/door2.mp3"
                    with hpunch
                    "{i}Nagle usłyszałeś dźwięk otwieranych drzwi i zauważyłeś, że ktoś zszedł do piwnicy{/i}"
                    luszcz "WTF? Ciekawe co jest w piwnicy..."
                    luszcz "anyway"
                
                luszcz "..."
                jump bal3
    
    label btask2:
        $ btask2 = 1
        $ btask3 = 1
        stop music
        scene bg black with fade
        scene bg bal8 with fade
        $ timer += 15
        play music "audio/music/chopin.mp3"
        $ renpy.music.set_volume(1.0, delay=0.3)
        
        show luszcz bal zorder 12 at center

        if gotka_szpont == 1:
            luszcz "No i gdzie jest moja Gigasigma?"
        else:
            luszcz "No i gdzie jest Gotka?"

        show gotka neutral right at slightright
        show luszcz bal at slightleft

        gotka "O już jesteś!"
        gotka "Klient powinien być lada chwila"

        luszcz "Jaki klient?"

        gotka "A właśnie, bo zapomniałam Ci powiedzieć"
        gotka "Czasami dorabiam sobię sprzedając jakieś narkotyki po godzinach"
        gotka "i dziś jeden klientów umówił się ze mną na zakup podczas Balu"

        luszcz "Jezus maria"
        luszcz "mogłaś, mogłaś mówić wcześniej!"

        gotka "Nie bądź dziecko"
        gotka "Każdy kupuje dragi tylko nie każdy o tym wie"

        luszcz "(hmmmm, miałem kiedyś takiego nauczyciela co mówił, że telefon jest jak narkotyk, więc może to i prawda...)"

        show tarczownik neutral right at left 
        show luszcz bal at center
        show gotka neutral right at right

        tarczownik "tu tu ru tu tu"

        show luszcz bal right 

        luszcz "Naofumi? Co ty tu robisz!?"

        tarczownik "Cssssiiiii!"

        if tarczownik_social_link == 1:
            show tarczownik neutral right at slightleft

            tarczownik "Mam, mam tu pewien interes"

            luszcz "emmm, a czy może ten interes zaczyna się na d a kończy na ragi?"

            tarczownik "Skąd wiedziałeś!?"

            show luszcz bal 

            luszcz "To jest on, nasz kupiec"
        
        else:
            show tarczownik neutral right at slightleft

            tarczownik "Pamiętasz jak mówiłem Ci, że chcę sobie ogarnąć trochę towaru?"

            luszcz "Chwila, to ty jesteś tym kupcem!?"

            show luszcz bal

            luszcz "To jest on, nasz kupiec"
        
        show gotka neutral right zorder 5 at center
        show luszcz bal right at right 

        gotka "Hmmm spodziewałam się kogoś, jakby to powiedzieć..."
        gotka "“Bardziej umięśnionego”"

    label btask3:
        ""

    tata "O synu jesteś!"
    tata "Potrzebuję Cię na chwilę"

    luszcz "EHHHH, a muszę z tobą iść?"

    tata "TAK!"
    tata "Mam dla Ciebie zadanie bojowe!"
    tata "Czekam w sali konferencyjnej"
    tata "Nie zawiedź mnie!"

    hide tata 

    luszcz "kupa, siki, mocz"
    luszcz "Tu jest w ogóle taka sala?"
    luszcz "Ehhhh, sraka"

    label btask4:
        $ btask4 = 1
        stop music
        scene bg black with fade
        scene bg bal9 with fade
        $ timer += 15
        play music "audio/music/bal.mp3"
        $ renpy.music.set_volume(0.25, delay=0.3)
        
        show luszcz bal zorder 12 at left

        luszcz "To chyba tutaj..."

        show tata neutral at slightright

        tata "O synu jesteś!"
        tata "Przygotuj się, zaraz się zacznie!"

        luszcz "Co się zacznie?"

        tata "No debata oxfordzka!"
        tata "Jesteśmy drużyną opozycji jakby co"
        tata "A i jest nas tylko 3 więc harujesz na dwie zmiany"

        nikt "Proszę o zajęcie miejsc, zaraz zaczynamy debatę!"

        tata "Awwww shit to już!"
        tata "Dobra siadaj i spróbuj się dostosować do mnie i Pana Burmistrza"

        luszcz "Burmistrz jest w naszej drużynie!?"

        tata "przykro mi"
        tata "tak wyszło"

        luszcz "..."

        nikt "Zaczynamy!"

        hide luszcz 
        hide tata 
        show maciak neutral at center

        mac "Товарищи, мы собрались сегодня, чтобы..."
        mac "Oj sorki zapomniałem się troszke"
        mac "Za dużo hoia z Kałachem"

        show kalach neutral at right

        kalach "Ej, ej, ej prosze mnie nie pomawiać!"
        kalach "To ty zawsze przychodziłeś do mnie do pokoju i mówiłeś..."
        kalach "...“Kałach, kałach, zagrajmy na czerwonym seszele i fioletowym nauru na Modern Day'u!”"

        show putin neutral at left
        putin "Tak było, tym razem Kałach nie zmyśla"

        mac "Aghhh, cichość poproszę!"
        mac "Jesteśmy podczas debaty oksfordzkiej!"

        kalach "..."
        putin "..."

        mac "No, więc kontynuujmy!"
        mac "Towarzysze! Zebraliśmy się tutaj, aby przeprowadzić debatę oxfordzką na temat przyszłości polski!"
        mac "Temat dokładnie brzmi “Sen o Polsce czy sąd nad Polską?”"

        luszcz "Emmmm, a to nie powinno być tak, że temat jest tezą, a nie pytaniem?"

        mac "Cicho bądź, ja tu mówię!"

        mac "..."
        mac "No więc z racji braku zasobów ludzkich, ja oraz panowie po mojej lewej i prawej będziemy zarówno prowadzącymi debatę jak i sędziami"

        kalach "Witam szanownych towarzyszy!"

        putin "Również witam!"

        mac "Niestety braki w zasobach ludzkich sięgneły również klasy pracującej, dlatego jest was tylko po trzech w drużynach i ktoś będzie miał dwie role"
        mac "No cóż, niestety nic z tym nie zrobimy, więc przejdźmy do przedstawiania drużyn!"

        hide putin 
        hide kalach

        mac "Drużyne propozycji pokieruje Pan Mcłowicz!"

        show mclowicz neutral at right
        mclowicz "Witam Państwa!"
        hide mclowicz 
        mac "A drużyne opozycji pokieruje Pan Burmistrz!"

        show burmistrz neutral right at left
        burmistrz "Witam wszystkich serdecznie!"

        tata "..."
        luszcz "..."

        hide burmistrz
        mac "A więc zacznijmy debatę od mówcy pierwszego drużyny propozycji!"
        
        hide maciak 
        show mclowicz neutral at center
        mclowicz "Emghhhem, zatem Szanowny Panie Marszałku, drużyno opozycji, droga publiczności!"
        mclowicz "My jako drużyna propozycji uważamy, iż Polska powinna być jak gulasz"
        mclowicz "Gulasz jest potrawą, która łączy w sobie wiele składników, które razem tworzą coś wyjątkowego"
        mclowicz "Tak jak Austro-Węgry pod panowaniem Franciszka Józefa, które łączyły w sobie wiele narodów i kultur"
        mclowicz "Dlatego w naszych przemowach będziemy przekonywać do koncepcji odtworzenia Austro-Węgier i zreinkarnowania Franciszka Józefa!"
        mclowicz "Dziękuję bardzo za uwagę."

        hide mclowicz 
        show maciak neutral at center

        mac "Dziękuję bardzo za przemowę, teraz czas na drużyne opozycji!"

        hide maciak  
        show burmistrz neutral right at center 
        burmistrz "Dziękuję bardzo, Szanowny Panie Marszałku, drużyno propozycji, droga publiczności!"
        burmistrz "My jako drużyna opozycji fundamentalnie odrzucamy koncepcje odtworzenia Austro-Węgier i zreinkarnowania Franciszka Józefa!"
        burmistrz "Uważamy, iż Polaką wcale nie żyło się tak dobrze w Austro-Węgrach!"
        burmistrz "Była bieda i głód, a Polacy byli traktowani jak obywatele drugiej kategorii!"
        burmistrz "Jednakże nie będziemy tylko krytykować, ale również przedstawimy naszą koncepcje na przyszłość Polski!"
        burmistrz "Czy wiecie państwo w jakim kraju jeszcze żaden polak nie narzekał jak mu się żyje?"
        burmistrz "Otóż to! W Republice Rzymskiej!"
        burmistrz "Dlatego w naszych przemowach będziemy przekonywać do koncepcji przekształcenia Polski w Republicę Rzymską!"
        burmistrz "All Hail Republic!"
        burmistrz "A po za tym, uważam że Kartagina musi zostać zniszczona"

        hide burmistrz
        show maciak neutral at center 
        mac "Dziękuję bardzo pierwszym mówcą obu drużyn za przemowę!" 
        mac "Teraz przejdziemy do drugiego mówcy drużyny propozycji"

        hide maciak 
        show turek neutral at center

        turek "Dziękuję za głos, Szanowny Panie Marszałku, drużyno opozycji, droga publiczności!"
        turek "Austro-Węgry to było coś więcej niż państwo"
        turek "To była idea!"
        turek "Idea utworzenia państwa, w którzym wszyscy są mile widziani!"
        turek "W którym narodowość nie ma znaczenia!"
        turek "I czy nie takim państwem powinna stać się polska?"
        turek "Czy to nie jest piękne?"

        luszcz "(Jezus maria, co on pierdoli?)"
        luszcz "(Może powinienem mu przeszkodzić...)"

        menu: 
            "{b}Czy podnieść rękę?{/b}"
            
            "{b}Tak{/b}":
                mac "Tak Łuszczu?"
                show luszcz bal at slightleft
                show turek neutral at slightright
                luszcz "Emmm, przepraszam, ale..."

                menu:
                    "{b}Co z horymi dziećmi?{/b}":
                        $ maciakp += 1
                        luszcz "Co z horymi dziećmi? Czy one też będą mile widziane w Austro-Węgrzech?"

                        turek "smaczne"

                        luszcz "..?"
                        luszcz "..."
                        luszcz "..!"
                        luszcz "Okrótność!"

                        "{i}Zauważyłeś uznanie w oczach Macieja Maciaka{/i}"

                    "{b}Co z niepełnosprawnymi?{/b}":
                        $ kalachp += 1
                        luszcz "Co z niepełnosprawnymi? Czy oni też będą mile widziani?"

                        turek "Emmmm, zależy jacy, bo jak upośledzeni to bardzo chętnie przyjmiemy ich do wojska, ale jeśli np. chodzą o kulach, albo nie daj allah, nie mają nóg i jeżdżą na wózku inwalidzkim to niestety, ale nie ma takiej opcji!"

                        luszcz "Skandal!"

                        "{i}Zauważyłeś uznanie w oczach Klejnotu Wołgi{/i}"

                    "{b}Co z murzynami?{/b}":
                        luszcz "Co z murzynami? Czy oni też będą mile widziani?"

                        turek "Nie, nie murzyni mają wypierdalać!"
                        turek "Nasze Austro-Węgry będą czyste, bez murzynów!"

                        luszcz "Dziękuję to chciałem usłyszeć."

                        "{i}Nikt z rzyri nie zaaragował na to pytanie...{/i}"

                    "{b}Co ze zbrodniarzami wojennymi?{/b}":
                        $ putinp += 1
                        luszcz "Co ze zbrodniarzami wojennymi? Czy oni też będą mile widziani?"

                        turek "Niestety, ale nie planujemy rozbudowy ASP więc raczej nie..."

                        luszcz "Skandal!"

                        "{i}Zauważyłeś uznanie w oczach Władimir Władimirowicz Putin{/i}"
                
                hide luszcz bal
                show turek neutral at center
                turek "eghemm, wracając..."
            
            "{b}Nie{/b}":
                luszcz "(Lepiej się nie wychylać...)"
    
    turek "Czy wiecie, że nawet raz tam kiedyś na pół roku premierem Austro-Węgier został Polak?"
    turek "Czy to nie jest cudowne!?"
    turek "Przecież teraz rządzą wami tylko rosyjscy i niemieccy agenci pod przykrywką"
    turek "A w takich Austro-węgrzech nie będą się musieli z tym ukrywać!"
    turek "Zróbcie coś dobrego dla nich i wybierzcie Austro-Węgry!"
    turek "Dziękuję."

    hide turek 
    show maciak neutral at center 
    mac "Emmm, dziękujemy za tą przemowe i poprosimy teraz mówce drugiego drużyny opozycji"

    tata "Dajesz synek, wierzę w Ciebie!"
    
    hide maciak 
    show luszcz bal at center
    luszcz "Emmmm, eeeee"
    luszcz "Witam eee wszystkich?"
    luszcz "Jako drugi mówca eee drużyny opozycji przedstawię teraz nasze argumenty za utworzeniem Republiki Rzymskiej."
    
    menu: 
        "{b}Po pierwsze Republika Rzymska...{/b}"

        "{b}Co z horymi dziećmi?{/b}":
            ""