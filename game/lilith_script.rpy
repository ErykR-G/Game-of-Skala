define fast_push = PushMove(0.45, "pushleft")

label lilith:
    label lilith1:
        "{i}{/i}"
        "{i}Tej nocy pojawiła się Lilith{/i}"
        "{i}Leżę na łóżku, zagubiony w czasie-Nie wiem, jak długo próbowałem zasnąć i nawet nie pamiętam, kiedy ostatnio farmiłem na skyblocku{/i}"
        "{i}Jedyne co mi pozostało to umrzeć tutaj... i czekać aż moje ciało się rozłoży{/i}"
        "{i}i wtedy... ona pojawiła się obok mnie{/i}"

        scene bg gnoms with fade
        play music "audio/music/lilith1.mp3"
        scene bg lilith2 with fade

        lilith "..."

        show bg lilith1

        luszcz "..?"

        show bg lilith2

        lilith "..."

        show bg lilith1

        siostra "Słuchaj Joanna, nie uwierzysz co się stało!"
        siostra "znowu to zrobiliśmy…"
        siostra "nie wiem czemu cały czas to robimy skoro, na końcu zawsze mamy dość i mówimy nigdy więcej"
        siostra "I to zawsze jeszcze utrudniamy sobie na początku jak możemy"
        siostra "powalone to jest, mówię Ci teraz oficjalnie nigdy więcej tego nie zrobimy"
        siostra "no, ale wracając to ten ostatni raz to była taka sraka"
        siostra "chyba z 5 godzin nam to wszystko zajęło…"

        menu:
            "{b}...{/b}":
                $ ado += 1
                luszcz "..."
                show bg lilith2
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

        show bg lilith1

        siostra "i na początku było jeszcze git"
        siostra "zrobiłam przygotowania, znalazłam sobie przyjaciela ze wschodu i szukałam też z północy"
        siostra "aż tu nagle jeb kurwa wchodzi gwałciciel z zachodu i mnie rucha jak chce"
        siostra "a ja mu mówiłam wcześniej, że nie dziś nie mogę zły dzień"
        siostra "no i chuj się nie posłuchał"
        siostra "no ale na początku nie było tak źle miałam jakieś zabezpieczenie, więc popuszczałam powoli"
        siostra "o i wtedy jeszcze bo to ważne tego niedoszłego przyjaciela z północy też zaczęto gwałcić"
        siostra "choć go gwałcił mój jeszcze inny przyjaciel więc to nie był taki duży problem"
        siostra "Ale wracając to z pomocą z gwałcicielem przybiegł mój ten znajomy z wschodu co mówiłam co nie?"
        siostra "No i on troszkę pomógł, ale nie na tyle by zatrzymać gwałciciela"

        menu:
            "{b}...{/b}":
                $ ado += 1
                luszcz "..."
                show bg lilith2
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping
        
        show bg lilith1

        siostra "więc zacząłam szukać innych opcji"
        siostra "I wtedy odezwał się do mnie ten inny przyjaciel co gwałcił tego typa z północy"
        siostra "i wpadł na pomysł, że może jak mu się oddam dobrowolnie to ten chłop z zachodu mnie zostawi"
        siostra "no i z powodu braku innych pomysłów przystałam na tą propozycje…"
        siostra "początkowo myślałam, że nie będzie tak źle"
        siostra "szybko załatwi co ma załatwić i nawet tego nie poczuję"
        siostra "Ale okazało się że to nie jest takie proste…"
        siostra "Rany, które u mnie pozostawił nie chciały się zagoić…"
        siostra "A on jeszcze zażądał za wszystko zapłaty!"
        siostra "Bo mu się bardzo spodobał ten typ z zachodu i chciał dokonać kontrgwałtu na nim"
        siostra "Ale był za słaby, by zrobić to sam więc kazał MI mu z tym pomóc"
        siostra "No i pomogłam, co innego miałam niby zrobić?"
        siostra "ale nie poszło nam tak łatwo jak myśleliśmy…"

        menu:
            "{b}...{/b}":
                $ ado += 1
                luszcz "..."
                show bg lilith2
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

        show bg lilith1

        siostra "Ten gość z zachodu był silny"
        siostra "Bardzo silny"
        siostra "I do tego miał przyjaciół"
        siostra "A właśnie jak już o przyjaciołach mowa o przyjaciołach"
        siostra "To nam pomagał jeszcze jeden taki ziomuś"
        siostra "Choć pomaganie to duże słowo"
        siostra "Bardziej stał obok i się patrzył i jak koledzy chłopa z zachodu chcieli go tknąć to mówił, że on jest neutralny"
        siostra "Głupi chujek"
        siostra "Ale nie był całkowicie bezużyteczny"
        siostra "Kilka razy ochronił nas własnym ciałem"
        siostra "A właśnie, bo kontrgwałt się nie udał" 
        siostra "I to na nas był robiony kontrkontrgwałt"
        siostra "I jeszcze przeleciał jakiś typo z dalekiego wschodu"
        siostra "I też zaczął nas gwałcić"

        menu:
            "{b}...{/b}":
                $ ado += 1
                luszcz "..."
                show bg lilith2
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

        show bg lilith1

        siostra "Znaczy mnie nie"
        siostra "Jedynie tego mojego przyjaciela co mnie zmusił do próby kontrgwałtu"
        siostra "Więc nie było tak źle"
        siostra "Choć już trochę popuszczałam"
        siostra "I gdy myślałam, że już nie dam rady wydarzył się cud nad tą rzeką no jak ona się nazywała eeeee"
        siostra "Nie pamiętam no ale nad nią"
        siostra "I zrobiliśmy taki come back"
        siostra "Ale ten mój niby przyjaciel znów mnie wyruchał i nic mi nie dał w zamian za pomoc"
        siostra "Więc się zdenerwowałam i postanowiłam się zemścić"
        siostra "I gdy on się bawił z tym ziomeczkiem z dalekiego wschodu, ja wbiłam mu nuż kuchenny, w plecy"
        siostra "Lecz to i tak nic nie dało i tak"
        siostra "I znów mnie wykorzystano "
        siostra "i to był koniec"
        siostra "zmarnowane 5 godzin i trauma do końca życia"
        siostra "nienawidzę grać w hoia"

        "{i}...{/i}"

        menu:
            "{b}Kim jesteś?{/b}":
                jump after_yapping

        label after_yapping:
            luszcz "..."

            if yusuke_social_link >= 1 and yusuke_social_link <= 5:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        scene bg pokoj8 with fade
                    else:
                        scene bg pokoj7 with fade
                 

                else:
                    if drukowanko == 1:
                        scene bg pokoj4 with fade
                    else:
                        scene bg pokoj3 with fade
                    

            else:
                if yusuke_social_link >= 6:
                    if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                        if drukowanko == 1:
                            scene bg pokoj6 with fade
                        else:
                            scene bg pokoj5 with fade
                        
                        
                    else:
                        if drukowanko == 1:
                            scene bg pokoj2 with fade
                        else:
                            scene bg pokoj with fade

            show luszcz neutral right at slightright
            show lilith neutral2 at left
            play music "audio/music/lilith2.mp3"

            luszcz "Kim ty do kurwy jesteś? I jak dostałaś się do mojego domu?"

            lilith "Naprawdę chcesz to wiedzieć? Przecież to jest tylko gra komputerowa…."

            show layer master:
                zoom 1.0
                xalign 0.95 yalign 0.35
                linear 0.1 zoom 3.5

            gwiazda "Panie ona się Ciebie nie słucha"

            show layer master:
                zoom 3.5
                xalign 0.95 yalign 0.35
                easeout 0.1 zoom 3.5 xalign 1.0 yalign 0.82

            drukarka "Na pewno coś ukrywa!"

            show lilith neutral5

            show layer master:
                linear 0.1 zoom 1.0 xalign 0.5 yalign 0.5

            lilith "Haloo, ziemia do Łuszcza!"

            luszcz "...?"

            show lilith neutral3

            lilith "..."

            menu:
                "{b}Jesteś prostytutką?{/b}":
                    luszcz "Jesteś prostytutką?"

                    show lilith neutral4

                    lilith "Skoro tak o mnie myślisz to mogę być"
                    lilith "w sumie ej nawet o sobie nie myślałam w ten sposób, a to chyba najlepszy opis mojej pracy"
                    lilith "za pieniądze daję ci miłość"

                    show lilith neutral2

                    lilith "Dobra w takim razie skoro jestem już ze sobą szczera to chce kasy, albo spadam stąd"

                    menu:
                        "{b}Masz dychę i ma wystarczyć na wszystko (1 💰){/b}" if money >= 1:
                            luszcz "Masz dychę i ma wystarczyć na wszystko"
                            
                            $ money -= 1

                            show lilith neutral5

                            lilith "żałosne" 

                        "{b}Taaa? To spierdalaj{/b}":
                            stop music
                            luszcz "Taaa? To spierdalaj"

                            show lilith neutral5

                            lilith "Sam spierdalaj kurwa znalazł się jeden co, by chciałby bzykanko za darmo"
                            lilith "z takim kurwa brzydalem to kurwa nawet koń, by nie chciał"
                            lilith "Jeb się skurwysynie"

                            hide lilith
                            show luszcz neutral right at center

                            luszcz "ehh, a liczyłem, że zaliczę za darmo"
                            luszcz "idę spać dalej może przynajmniej w śnie mi się uda"

                            $ lilith_social_link = 10
                            scene bg black with fade
                            ""
                            jump spanko_bed
                
                "{b}Jesteś może gotką?{/b}":
                    luszcz "Jesteś może gotką?"

                    show lilith neutral2

                    lilith "Nie do końca, ale mogą dla Ciebie zostać jeśli chcesz"

                    luszcz "Ohhhh prosze, prosze, proszeeeee"

                    show lilith neutral5

                    lilith "Nie powinieneś się tak jawnie zdradzać ze swoim fantazjami seksualnymi przy kobietach!"
                    lilith "To może je zniechęcić do Ciebie"

                    menu:
                        "{b}Dobrze proszę Pani{/b}":
                            luszcz "Dobrze proszę Pani"
                            luszcz "a usiądzie mi Pani na mordzie?"

                            show lilith neutral1

                            lilith "iiiii juj jesteś dziwny…"
                            lilith "na pewno mam to zrobić?"

                            luszcz "TAK"

                            show lilith neutral5

                            lilith "jesteś obrzydliwy kurwa japierdole masz te 14 złotych za kickstartera i nie chcę Ciebie więcej widzieć na oczy"

                            $ money += 1

                            "{i}*dostajesz 1 portfel do ekwipunku*{/i}"

                            hide lilith
                            show luszcz neutral right at center

                            luszcz "No i trudno, hajs ponad suki 🤑🤑🤑"
                            luszcz "A teraz wracam do spanka"

                            $ lilith_social_link = 10
                            scene bg black with fade
                            ""
                            jump spanko_bed
                                                    
                        "{b}Jeśli nie dostanę gotki…{/b}":
                            luszcz "jeśli nie dostanę gotki, to nie potrzebuję kobiet"
                            luszcz "więc to nie jest problem"

                            show lilith neutral3

                            lilith "dobrze dobrze będę twoją gotką"

                            luszcz "LETS GO!"

                                    
                "{b}Mamo?{/b}":
                    luszcz "Mamo?"

                    show lilith neutral4

                    lilith "Czyli tak na mnie patrzysz…"

                    show lilith neutral3

                    lilith "No cóż jeśli tego ode mnie oczekujesz"

                    show lilith neutral1

                    lilith "W takim razie Macieju posprzątaj pokój w tej chwili! Co to za szmata w kącie pokoju! Masz 5 minut, a jak nie to dostaniesz szlaban na komputra!"

                    luszcz "przepraszam mamusiu już biorę się do sprzątania"
                                    
                "{b}Japierdole znów mam zwidy{/b}":
                    luszcz "Japierdole znów mam zwidy, mogłem nie wdychać tyle kadzidła podczas mszy…"

                    show layer master:
                        zoom 1.0
                        xalign 0.95 yalign 0.35
                        linear 0.1 zoom 3.5

                    gwiazda "Panie, nic panu nie jest … to normalne w tym wieku"

                    show layer master:
                        zoom 3.5
                        xalign 0.95 yalign 0.35
                        easeout 0.1 zoom 3.5 xalign 1.0 yalign 0.82

                    drukarka "dokładnie, dokładnie jest pan całkowicie normalny"

                    show layer master:
                        linear 0.1 zoom 1.0 xalign 0.5 yalign 0.5

                    luszcz "a okej"
                    luszcz "to jak masz na imię?"

                    show lilith neutral2

                    lilith "Lilith"

                    show lilith neutral3

                    luszcz "spoko"

            show lilith neutral3

            "{i}…{/i}"

            show lilith neutral2

            lilith "Dobra to skoro już się poznaliśmy to opowiedz coś o sobie"

            show lilith neutral3

            luszcz "A moze być ciekawostka z wiedzy ogólnej?"

            lilith "Jeżeli to jest to co chcesz mi powiedzieć to powiedz"

            luszcz "to w takim razie czy wiesz, że..."
            menu:
                "{b}Czy wiesz, że...{/b}"

                "{b}...Adolf Hitler tak naprawdę uciekł do Argentyny?{/b}":
                    luszcz "...Adolf Hitler tak naprawdę uciekł do Argentyny?"
                    luszcz "Bo ja grałem w Hoia i tam właśnie jest specjalna droga na Argentyne"
                    luszcz ", że jak Hitlera obalą to możesz go sobie na lidera kraju wybrać"
                    luszcz 'Więć jest to niezbity dowud na to, że Hitler uciekl do Argentyny'
                    luszcz "Trust me bro"
                
                "{b}...Wielko Lechici podpisali pakt z Kosmitami?{/b}":
                    luszcz "...Wielko Lechici podpisali pakt z Kosmitami?"
                    luszcz "No, bo lechici są Bogami tak btw"
                    luszcz "I kosmitą to mega imponowało"
                    luszcz "I stwierdzili, że oni chcą być z tak potężnym narodem w sojuszu"
                    luszcz "I podpisali, dlatego pakt z Wielką Lechią"

                "{b}...na Placu Tiananmen w 1989r. nic się nie stało?{/b}":
                    luszcz "...na Placu Tiananmen w 1989r. nic się nie stało?"
                    luszcz "No bo jakby co niby miałoby się wydarzyć?"
                    luszcz "gdyby coś się wydarzyło to napewno ktoś, by o tym mówił co nie!?"
                    luszcz "Ja naprzykład ostatnio spytałem o to DeepSeek AI"
                    luszcz "I to go aż tak bardzo znudziło, że w połowie pisania stwierdził, że mi oszczędzi nudów i usunął wiadomość"
                    luszcz "więc no literalnie nic się tam nie stało"
                
                "{b}...Jezus tak naprawdę nie umarł na krzyżu?{/b}":
                    luszcz "...Jezus tak naprawdę nie umarł na krzyżu?"
                    luszcz "no, bo jakby to miało niby działać?"
                    luszcz "Przecież on jest synem Boga, a Bóg jest nieśmiertelny"
                    luszcz "więc Jezus też musi być"
                    luszcz "Pewnie fake'ował pod publikę"
                    luszcz "No, ale chyba był w tym dobry skoro wszyscy mu do dziś wierzą"

                "{b}...Stalin tak naprawdę nie umarł na udar?{/b}":
                    luszcz "...Stalin tak naprawdę nie umarł na udar?"
                    luszcz "Bo ja oglądałem taki film dokumentalny o tym"
                    luszcz "I tam była właśnie taka scena, że Stalin dostał liścik z pogruszkami"
                    luszcz "I sie zaczoł śmiac tak glośno"
                    luszcz "I się niestety zaksztusił i ómarł"
                    luszcz "ale nie na udar tak jak się mówi tylko na szczęście"
            
            show lilith neutral4

            lilith "eeeee"
            lilith "hehehe"

            show lilith neutral1

            lilith "cool"
            lilith "…"

            show lilith neutral2

            lilith "Upieczmy tort!"

            luszcz "teraz?"

            with vpunch
            show lilith neutral3

            lilith "TERAZ"

            luszcz "Człowieku jest środek nocy!"
            luszcz "Wszyscy w domu śpią i nie będę ich budzić!"

            show lilith neutral1

            lilith "ej Noo weeeeź"
            lilith "będzie fajnieee"

            menu:
                "{b}Niech będzie{/b}":
                    luszcz "niech bendzie"
                    luszcz "upiękę z tobą ten tort"

                    show lilith neutral3
                    with vpunch

                    lilith "yuppi!"

                    luszcz "ale masz być cicho!"   

                    lilith "dobrze dobrze"
                    lilith "w takim razie marsz do kuchni!"
                
                "{b}Nie ma opcji ide spać{/b}":
                    luszcz "nie ma opcji idę spać"
                    luszcz "a i btw ty nie istniejesz czy coś"

                    show lilith neutral4

                    lilith "na serio tak uważasz…?"

                    menu:
                        "{b}Tak{/b}":
                            stop music
                            luszcz "tak"

                            lilith "…"

                            show lilith neutral5 zorder 1

                            lilith "to zabij mnie w końcu!"
                            lilith "zabij mnie dajesz wiem że to chcesz!"

                            luszcz "eeee nie ja tylko chce spa…"

                            lilith "zrób to!"
                            lilith "teraz dajesz!"

                            show lilith neutral5 zorder 1:
                                xalign 0.0
                                yalign 1.0
                                easeout 0.3 xalign 0.5
                            show luszcz neutral right zorder 2

                            $ renpy.pause(0.3)
                            show luszcz nuz zorder 2
                            play sound "audio/sfx/kat.mp3"
                            $ renpy.pause(0.1)

                            show lilith neutral5:
                                xalign 0.5
                                yalign 1.0
                                easeout 0.3 xalign 0.0

                            "{i}Lilith wyciąga nóż i wkłada go w ręce łuszcza{/i}"

                            lilith "masz broń co cie powstrzymuje!"
                            lilith "dajesz!"

                            luszcz "nie ja…"

                            lilith "chcesz i oboje to wiemy!"


                            show lilith neutral5 zorder 1:
                                xalign 0.0
                                yalign 1.0
                                easeout 0.3 xalign 0.5
                            show luszcz nuz zorder 2
                            
                            play sound "audio/sfx/nuz1.mp3"
                            queue sound "audio/sfx/nuz2.mp3"
                            $ renpy.pause(0.4)

                            show luszcz wtf right zorder 2
                            show lilith ranny:
                                xalign 0.5
                                yalign 1.0
                                easeout 0.3 xalign 0.0

                            luszcz "o kurwa coś ty odjebala!"

                            lilith "nic… to twoja ręka trzymała nóż"

                            luszcz "ale to ty się na niego specjalnie nabilaś!"

                            lilith "nie oszukuj się"
                            lilith "sam tego dokonałeś"
                            lilith "to był twój wybórrrr…"

                            show lilith dead

                            luszcz "japierdziele ona nie żyje"
                            luszcz "ci ja teraz zrobię!?!?"

                            menu: 
                                "{b}Jeszcze jest ciepla…{/b}":
                                    show luszcz blush right
                                    luszcz "Jeszcze jest ciepła..."
                                    luszcz "Muszę ją wykorzystać!"

                                    scene bg black with fade

                                    n "{i}I jak Łuszczu powiedział tak zrobił{/i}"
                                    n "{i}Dokonał swojego haniebnego czynnu poczym schował ciało do szafy{/i}"
                                    n "{i}Od teraz służyło mu jako seks zabawka po wsze czasy{/i}"

                                    $ lilith_social_link = 10
                                    jump spanko_bed

                                "{b}Muszę ją wykorzystać{/b}":
                                    show luszcz sigma right
                                    luszcz "Muszę ją wykorzystać"
                                    luszcz "..."
                                    luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                    scene bg black with fade

                                    n "{i}I jak Łuszczu powiedział tak zrobił{/i}"
                                    n "{i}Poszedł do lokalnego rzeźnika i zaproponował sprzedanie ciała{/i}"
                                    n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                    n "{i}Po wszystkim Łuszcz wrócił do domu i poszedł spać{/i}"

                                    $ money += 3
                                    "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                    $ lilith_social_link = 10
                                    jump spanko_bed

                        "{b}Nie{/b}":
                            luszcz "Dobra żartuję"
                            luszcz "upiękę z tobą ten tort"

                            show lilith neutral3
                            with vpunch

                            lilith "yuppi!"
                            lilith "to do kuchni marsz!"

                            luszcz "dobrze dobrze"

            play music "audio/music/lilith2.mp3"
            scene bg kuchnia 
            with fast_push
            $ renpy.pause(0.1)
            show luszcz neutral right at slightright
            show lilith neutral1 at left

            lilith "…aaa na koniec dodajesz trochę miłości ❤️"

            show lilith neutral2

            lilith "Powtórzyć czy możemy zaczynać?"

            menu:
                "{b}Powtórzyć{/b}":
                    show lilith neutral3

                    lilith "Na początku oddziel {font=fonts/NotoSansTC-Regular.ttf}蛋{/font} na {font=fonts/NotoSansTC-Regular.ttf}蛋白質{/font} i {font=fonts/NotoSansTC-Regular.ttf}蛋黃{/font}. {font=fonts/NotoSansTC-Regular.ttf}蛋白質{/font} ubij na sztywną {font=fonts/NotoSansTC-Regular.ttf}泡棉{/font} ze szczyptą {font=fonts/NotoSansTC-Regular.ttf}鹽{/font}, następnie stopniowo dodawaj {font=fonts/NotoSansTC-Regular.ttf}糖{/font}, cały czas miksując."

                    luszcz "Aww shit, co to za chińskie znaczki!?"
                    luszcz "Jak ja mam to niby zrozumieć!?"

                    if slownik == 1:
                        luszcz "Chwila wait przecież mam rozmówki polsko chińskie!"
                        show luszcz slownik
                        luszcz "Ej możesz zacząć od początku, bo trochę nie słuchałem?"

                        show lilith neutral5

                        lilith "strzelam! gr gr grrr"

                        show lilith neutral3

                        lilith "{cps=65}Na początku oddziel jajka na białko i żółtko. Białka ubij na sztywną pianę ze szczyptą soli, następnie stopniowo dodawaj cukru, cały czas miksując.{nw=0.5}{/cps}"
                        lilith "{cps=65}Gdy masa będzie lśniąca i gęsta, dodawaj po jednym żółtku, delikatnie miksując na niskich obrotach. Na koniec przesiej do masy 150 g mąki pszennej i delikatnie wymieszaj szpatułką, aby nie zniszczyć piany.{nw=0.5}{/cps}"
                        lilith "{cps=65}Przelej ciasto do tortownicy o średnicy około 24 cm wyłożonej papierem do pieczenia i piecz w temperaturze 170–175°C przez około 30–35 minut, do suchego patyczka. W międzyczasie przygotuj krem. Ubij 500 ml dobrze schłodzonej śmietanki kremówki z 2–3 łyżkami cukru pudru.{nw=0.5}{/cps}"
                        lilith "{cps=65}Pod koniec ubijania dodaj serka mascarpone i krótko zmiksuj do połączenia składników. Jeśli chcesz, możesz dodać łyżeczkę ekstraktu waniliowego. Przygotuj około 500–700 g świeżych truskawek – umyj je, usuń szypułki i pokrój większe truskawki na połówki lub plasterki.{nw=0.5}{/cps}"
                        lilith "{cps=65}Aby złożyć tort, pierwszy blat biszkoptu nasącz delikatnie ostudzoną wodą z odrobiną soku z cytryny, następnie wyłóż część kremu i równomiernie rozprowadź. Na kremie ułóż warstwę truskawek.{nw=0.5}{/cps}"
                        lilith "{cps=65}Przykryj kolejnym blatem i powtórz czynność. Wierzch oraz boki tortu posmaruj pozostałym kremem i udekoruj świeżymi truskawkami według uznania.{nw=0.5}{/cps}"

                    else:
                        luszcz "Przecież nie ma tu Eryka, żeby to przetłumaczył!"

                        show lilith neutral5

                        lilith "Ale typie to jest Chiński Tradycyjny, a nie Japoński więc Eryk i tak go nie zna!"
                        lilith "Więc sklej japę i się skup, bo powtarzać nie będę!"

                        show lilith neutral3

                        lilith "{cps=65}Gdy {font=fonts/NotoSansTC-Regular.ttf}大量的{/font} będzie lśniąca i gęsta, dodawaj po jednym {font=fonts/NotoSansTC-Regular.ttf}蛋黃{/font}, delikatnie miksując na niskich obrotach. Na koniec przesiej do {font=fonts/NotoSansTC-Regular.ttf}大量的{/font} 150 g {font=fonts/NotoSansTC-Regular.ttf}麵粉{/font} i delikatnie wymieszaj szpatułką, aby nie zniszczyć {font=fonts/NotoSansTC-Regular.ttf}泡棉{/font}.{nw=0.5}{/cps}"
                        lilith "{cps=65}Przelej {font=fonts/NotoSansTC-Regular.ttf}蛋糕{/font} do {font=fonts/NotoSansTC-Regular.ttf}蛋糕罐{/font} o średnicy około 24 cm wyłożonej {font=fonts/NotoSansTC-Regular.ttf}烘焙紙{/font} i piecz w temperaturze 170–175°C przez około 30–35 minut, do suchego patyczka. W międzyczasie przygotuj {font=fonts/NotoSansTC-Regular.ttf}奶油{/font}. Ubij 500 ml dobrze schłodzonej {font=fonts/NotoSansTC-Regular.ttf}鮮奶油{/font} z 2–3 łyżkami {font=fonts/NotoSansTC-Regular.ttf}糖粉{/font}.{nw=0.5}{/cps}"
                        lilith "{cps=65}Pod koniec ubijania dodaj {font=fonts/NotoSansTC-Regular.ttf}馬斯卡彭起司{/font} i krótko zmiksuj do połączenia składników. Przygotuj około 500–700 g świeżych {font=fonts/NotoSansTC-Regular.ttf}草莓{/font} – umyj je, usuń szypułki i pokrój większe {font=fonts/NotoSansTC-Regular.ttf}草莓{/font}  na połówki lub plasterki.{nw=0.5}{/cps}"
                        lilith "{cps=65}Aby złożyć tort, pierwszy blat {font=fonts/NotoSansTC-Regular.ttf}海綿蛋糕{/font} nasącz delikatnie ostudzoną {font=fonts/NotoSansTC-Regular.ttf}水{/font} z odrobiną {font=fonts/NotoSansTC-Regular.ttf}檸檬汁{/font}, następnie wyłóż część {font=fonts/NotoSansTC-Regular.ttf}奶油{/font}  i równomiernie rozprowadź. Na {font=fonts/NotoSansTC-Regular.ttf}奶油{/font} ułóż warstwę {font=fonts/NotoSansTC-Regular.ttf}草莓{/font}.{nw=0.5}{/cps}" 
                        lilith "{cps=65}Przykryj kolejnym blatem i powtórz czynność. Wierzch oraz boki {font=fonts/NotoSansTC-Regular.ttf}蛋糕{/font} posmaruj pozostałym {font=fonts/NotoSansTC-Regular.ttf}奶油{/font} i udekoruj świeżymi {font=fonts/NotoSansTC-Regular.ttf}奶油{/font} według uznania.{nw=0.5}{/cps}"

                    show lilith neutral2

                    lilith "No i na koniec dodaj trochę miłości ❤️"

                    show luszcz neutral right

                    luszcz "yyyeeeh"
                    luszcz "a może byś powtórzyła jeszcze raz?"

                    show lilith neutral5

                    lilith "Nie, nie tak nie można!"
                    lilith "Gdybym powtórzyła to moja cała wcześniejsza wypowiedź straciłaby sens!"

                    luszcz "ale przecież teraz też powtarzałaś przepis!?"

                    show lilith neutral2

                    lilith "oh no ale ty/gracz nie widziałeś jak mówiłam przepis za pierwszym razem"
                    lilith "bo autor tej gry stwierdził, że będzie zabawnie jeśli skipniesz powtórzenie i będziesz musiał gotować po chińsku w ciemno"
                    lilith "ale akurat ty byłeś tak przenikliwy, że się tego domyśliłeś i poprosiłeś mnie bym powtórzyła"
                    lilith "lub ewentualnie oszukałeś i wczytałeś save’a!"
                    lilith "tak czy siak nie powtórzę, bo nie i elo"

                    luszcz "…"
                    luszcz "Nie łam 4 ściany"

                    show lilith neutral3

                    lilith "…"

                    luszcz "…"
                    luszcz "dobra to gotuję"

                "{b}Zaczynajmny{/b}":
                    luszcz "zaczynajmy"

            luszcz "(Na początku muszę dodać)"






