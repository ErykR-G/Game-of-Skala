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

label bal:
    label bal1:
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

                    urban "Nie tutaj, przyjdź po 24 do toalety to to obgadamy"

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

                            urban "Nie tutaj, przyjdź po 24 do toalety to to obgadamy"

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
                            urban "Przyjdź do kibla po 24"

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

        eryk "Kiedyś, kurwa tu nie było nic, zero, a teraz? Teraz jest tu kasyno!"

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

        "{i}Muzyka rozpoczeła grać, a ludzie zaczeli dopierać się w pary do pierwszego tańca{/i}"
        