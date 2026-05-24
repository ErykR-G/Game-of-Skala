default stol = 0
default eminem_gadka = 0
default kazuma_gadka = 0
default yusuke_gadka = 0
default zyd_gadka = 0
default urban_gadka = 0
default tarczownik_gadka = 0
default gadka = 0

label bal:
    label bal1:
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

            shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
            shinobu "dobra mikrofon działa"
            shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

            nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

            shinobu "ahhh ale"

            nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

            shinobu "no okeej"

            shinobu "eee to więc"
            shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali baletowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
            
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

                $ renpy.music.set_volume(1.0, delay=0.3)

                        
                luszcz "(Emmmm zaczynają już oni te impreze czy co)"
                luszcz "(ja już nie chcem tótaj siedźiedź)"

                shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
                shinobu "dobra mikrofon działa"

                shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

                nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

                shinobu "ahhh ale"

                nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

                shinobu "no okeej"

                shinobu "eee to więc"
                shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali baletowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
                
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

                    $ renpy.music.set_volume(1.0, delay=0.3)

                            
                    luszcz "(Emmmm zaczynają już oni te impreze czy co)"
                    luszcz "(ja już nie chcem tótaj siedźiedź)"

                    shinobu "Hmmm, raz, dwa, trzy, raz, dwa trzy"
                    shinobu "dobra mikrofon działa"

                    shinobu "Halo, halo cwele, ruszcie swoje spasione dupska, bo za chwilę mój mistrz wygłosi przemowę!!!"

                    nikt "Shinobu! Co mówiłem!?!? Nie możesz tak traktować naszych szanownych gości"

                    shinobu "ahhh ale"

                    nikt "Bez ale mi tu tylko zaproś ich tak jak powinnaś"

                    shinobu "no okeej"

                    shinobu "eee to więc"
                    shinobu "Zapraszam was niezwykle serdecznie nasi szanowni goście na rozpoczęcie balu do sali baletowej, która jest na prawo od sali jadalnej, w której się zapewne znajdujecie wy spasione tłuste..."
                    
                    nikt "Shinobu!!!"

                    shinobu "No tak, wiem wiem"
                    shinobu "...gdzie się znajdujecie nasi najszanowniejsi goście ❤️!"
                    shinobu "Mój Pan wygłosi tam przemówienie po, którym wszyscy będziecie płakać, bo jak nie..."

                    nikt "Dobrze już, już wystraczy"

                    all "..."

                    luszcz "..."
                    luszcz "No cóż, czas się udać na rozpoczęcie Balu!"

        scene bg bal4 with fade
        ""

