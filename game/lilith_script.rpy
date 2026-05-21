define fast_push = PushMove(0.45, "pushleft")
default powtor = 0
default ciastol = 0

default texts = []
default score = 0
default max_time = 50.0
default game_time = 50.0

default hitlerlil = 0
default stalinlil = 0
default lechialil = 0
default kennedylil = 0
default placlil = 0
default jezuslil = 0
default smolensklil = 0

default klil = 0

init python:
    import random

    true_texts = [
        "Jesteś wehikułem czasu",
        "Możliwe, że nie jesteś piekarnikiem",
        "Nie jest wykluczone, że jesteś maszyną czasu",
        "Nie ma takie dowodu, że jesteś piekarnikiem",
        "Oczywiście, że jesteś maszyna czasu",
        "Oczywiście, ze nie jesteś piekarnikiem"
    ]

    false_texts = [
        "Nie jesteś wehikułem czasu",
        "Jesteś piekarnikiem",
        "Czym innym jesteś jak nie piekarnikiem",
        "Napewno nie jesteś wehikułem czasu",
        "Nie ma dowodu, że jesteś wehikułem czasu",
        "Piekarnik to ty"
    ]

    def spawn_text():
        is_true = renpy.random.choice([True, False])

        if is_true:
            label_text = renpy.random.choice(true_texts)
        else:
            label_text = renpy.random.choice(false_texts)

        texts.append({
            "id": renpy.random.randint(1000, 9999),
            "x": renpy.random.randint(50, 1250),
            "y": renpy.random.randint(150, 900),
            "time": 3.0,
            "correct": not is_true,  # poprawne = zaprzeczenie
            "label": label_text
        })

    def update_texts():
        global texts
        for t in texts[:]:
            t["time"] -= 0.1
            if t["time"] <= 0:
                texts.remove(t)

    def click_text(t):
        global score

        if t["correct"]:
            score += 1
        else:
            if score > 0:
                score -= 1

        if t in texts:
            texts.remove(t)

init:

    style oven_button_text:
        size 28
        color "#ffffff"
        hover_color "#ffff66"
        insensitive_color "#888888"

    style oven_button:
        background "#222222cc"
        hover_background "#444444dd"
        selected_background "#666666dd"
        padding (15, 10)

label lilith:
    label lilith1:
        "{i}{/i}"
        n "{i}Tej nocy pojawiła się Lilith{/i}"
        n "{i}Leżałeś na łóżku, zagubiony w czasie-Nie wiedząc, jak długo próbowałeś zasnąć i nawet nie pamiętając, kiedy ostatnio farmiłeś na skyblocku{/i}"
        n "{i}Jedyne co ci pozostało to umrzeć tutaj... i czekać aż twoje ciało się rozłoży{/i}"
        n "{i}i wtedy... ONA pojawiła się obok ciebie{/i}"

        window hide
        scene bg gnoms with fade
        play music "audio/music/lilith1.mp3"
        scene bg lilith2 with fade
        window show

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
                    $ hitlerlil = 1
                    luszcz "...Adolf Hitler tak naprawdę uciekł do Argentyny?"
                    luszcz "Bo ja grałem w Hoia i tam właśnie jest specjalna droga na Argentyne"
                    luszcz ", że jak Hitlera obalą to możesz go sobie na lidera kraju wybrać"
                    luszcz 'Więć jest to niezbity dowud na to, że Hitler uciekl do Argentyny'
                    luszcz "Trust me bro"
                
                "{b}...Wielko Lechici podpisali pakt z Kosmitami?{/b}":
                    $ lechialil = 1
                    luszcz "...Wielko Lechici podpisali pakt z Kosmitami?"
                    luszcz "No, bo lechici są Bogami tak btw"
                    luszcz "I kosmitą to mega imponowało"
                    luszcz "I stwierdzili, że oni chcą być z tak potężnym narodem w sojuszu"
                    luszcz "I podpisali, dlatego pakt z Wielką Lechią"

                "{b}...na Placu Tiananmen w 1989r. nic się nie stało?{/b}":
                    $ placlil = 1
                    luszcz "...na Placu Tiananmen w 1989r. nic się nie stało?"
                    luszcz "No bo jakby co niby miałoby się wydarzyć?"
                    luszcz "gdyby coś się wydarzyło to napewno ktoś, by o tym mówił co nie!?"
                    luszcz "Ja naprzykład ostatnio spytałem o to DeepSeek AI"
                    luszcz "I to go aż tak bardzo znudziło, że w połowie pisania stwierdził, że mi oszczędzi nudów i usunął wiadomość"
                    luszcz "więc no literalnie nic się tam nie stało"
                
                "{b}...Jezus tak naprawdę nie umarł na krzyżu?{/b}":
                    $ jezuslil = 1
                    luszcz "...Jezus tak naprawdę nie umarł na krzyżu?"
                    luszcz "no, bo jakby to miało niby działać?"
                    luszcz "Przecież on jest synem Boga, a Bóg jest nieśmiertelny"
                    luszcz "więc Jezus też musi być"
                    luszcz "Pewnie fake'ował pod publikę"
                    luszcz "No, ale chyba był w tym dobry skoro wszyscy mu do dziś wierzą"

                "{b}...Stalin tak naprawdę nie umarł na udar?{/b}":
                    $ stalinlil = 1
                    luszcz "...Stalin tak naprawdę nie umarł na udar?"
                    luszcz "Bo ja oglądałem taki film dokumentalny o tym"
                    luszcz "I tam była właśnie taka scena, że Stalin dostał liścik z pogruszkami"
                    luszcz "I sie zaczoł śmiac tak glośno"
                    luszcz "I się niestety zaksztusił i ómarł"
                    luszcz "ale nie na udar tak jak się mówi tylko na szczęście"
                
                "{b}...w Smoleńsku to był tak naprawdę zamach?{/b}":
                    $ smolensklil = 1
                    luszcz "...w Smoleńsku to był tak naprawdę zamach?"
                    luszcz "Bo ja oglądałem kiedyś w TVP taki reportaż"
                    luszcz "I tam był taki śmieszny pan co się chyba nazywał jakoś na m"
                    luszcz "mmmmmMario tak to był Mario"
                    luszcz "No i Mario właśnie mówił, że jego komisja zbadała sprawę"
                    luszcz "i, rze to był tak naprawdę zamach zaplanowany przez Tuska!"
            
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

                            n "{i}Lilith wyciąga nóż i wkłada go w twoje ręce{/i}"

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

                            luszcz "o kurwa coś ty odjebała!"

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

                                    n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                    n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                    n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                    $ lilith_social_link = 10
                                    jump spanko_bed

                                "{b}Muszę ją wykorzystać{/b}":
                                    show luszcz sigma right
                                    luszcz "Muszę ją wykorzystać"
                                    luszcz "..."
                                    luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                    scene bg black with fade

                                    n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                    n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                    n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                    n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

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
                    $ powtor = 1
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

            luszcz "Na początku muszę..."

            if powtor == 1 and slownik == 1:
                menu:
                    "{b}Na początku muszę oddzielić...{/b}"

                    "{b}Jajka na białko i żółtko{/b}":
                        $ ciastol += 1

                    "{b}Składniki na cukier i masło{/b}":
                        $ ciastol += 0
            
            else:
                menu:
                    "{b}Na początku muszę oddzielić...{/b}"

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}蛋{/font} na {font=fonts/NotoSansTC-Regular.ttf}蛋白質{/font} i {font=fonts/NotoSansTC-Regular.ttf}蛋黃{/font}{/b}":
                        $ ciastol += 1

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}原料{/font} na {font=fonts/NotoSansTC-Regular.ttf}糖{/font} i {font=fonts/NotoSansTC-Regular.ttf}黄油{/font}{/b}":
                        $ ciastol += 0
            
            if powtor == 0:
                luszcz "Aww shit, co to za chińskie znaczki!?"
                luszcz "Jak ja mam to niby zrozumieć!?"

                if slownik == 1:
                    luszcz "Chwila wait przecież mam rozmówki polsko chińskie!"
                    show luszcz slownik
                else:
                    luszcz "Przecież nie ma tu Eryka, żeby to przetłumaczył!"

                    show lilith neutral5

                    lilith "Ale typie to jest Chiński Tradycyjny, a nie Japoński więc Eryk i tak go nie zna!"
                    lilith "Więc sklej japę i się skup, przecież upieczenie tortu nie jest takie trudne!"

                    show lilith neutral3
            
            else:
                luszcz "Dobra, chyba to jest to"


            if slownik == 1:
                menu:
                    "{b}Następnie muszę ubić to na...{/b}"

                    "{b}Pianę ze szczyptą soli i dodać cukier{/b}":
                        $ ciastol += 1

                    "{b}Ciasto ze sodą i dodać miód{/b}":
                        $ ciastol += 0
            
            else:
                menu:
                    "{b}Następnie muszę ubić to na...{/b}"

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}泡棉{/font} ze {font=fonts/NotoSansTC-Regular.ttf}鹽{/font} i dodać {font=fonts/NotoSansTC-Regular.ttf}糖{/font}{/b}":
                        $ ciastol += 1

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}蛋糕{/font} ze {font=fonts/NotoSansTC-Regular.ttf}蘇打{/font} i dodać {font=fonts/NotoSansTC-Regular.ttf}蜂蜜{/font}{/b}":
                        $ ciastol += 0
            
            luszcz "Dobra, chyba to jest to"

            if slownik == 1:
                menu:
                    "{b}Potem muszę przesiać...{/b}"
                    
                    "{b}150g mąki pszennej do masła{/b}":
                        $ ciastol += 0

                    "{b}150g mąki pszennej do masy{/b}":
                        $ ciastol += 1
            
            else:
                menu:
                    "{b}Potem muszę przesiać...{/b}"

                    "{b}150g {font=fonts/NotoSansTC-Regular.ttf} 麵粉{/font} do {font=fonts/NotoSansTC-Regular.ttf}黄油{/font}{/b}":
                        $ ciastol += 0

                    "{b}150g {font=fonts/NotoSansTC-Regular.ttf} 麵粉{/font} do {font=fonts/NotoSansTC-Regular.ttf}大量的{/font}{/b}":
                        $ ciastol += 1
            
            luszcz "Dobra, chyba to jest to"

            if slownik == 1:
                menu:
                    "{b}W międzyczasie muszę ubić...{/b}"
                    
                    "{b}Śmietankę kremówkę z cukrem pudrem{/b}":
                        $ ciastol += 1

                    "{b}Masę z kakao{/b}":
                        $ ciastol += 0
            
            else:
                menu:
                    "{b}W międzyczasie muszę ubić...{/b}"

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}鮮奶油{/font} z {font=fonts/NotoSansTC-Regular.ttf}糖粉{/font}{/b}":
                        $ ciastol += 1

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}大量的{/font} z {font=fonts/NotoSansTC-Regular.ttf}可可{/font}{/b}":
                        $ ciastol += 0
            
            luszcz "Dobra, chyba to jest to"

            if slownik == 1:
                menu:
                    "{b}W dalszej kolejności muszę nasączyć...{/b}"
                    
                    "{b}Ciasto za pomocą mokrych składników z przyprawą do pieczenia{/b}":
                        $ ciastol += 0

                    "{b}Biszkopt za pomocą wody z sokiem z cytryny{/b}":
                        $ ciastol += 1
            
            else:
                menu:
                    "{b}W dalszej kolejności muszę nasączyć ...{/b}"

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}蛋糕{/font} za pomocą {font=fonts/NotoSansTC-Regular.ttf}濕成分{/font} z {font=fonts/NotoSansTC-Regular.ttf}烘焙香料{/font}{/b}":
                        $ ciastol += 0

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}海綿蛋糕{/font} za pomocą {font=fonts/NotoSansTC-Regular.ttf}水{/font} z {font=fonts/NotoSansTC-Regular.ttf}檸檬汁{/font}{/b}":
                        $ ciastol += 1
            
            luszcz "Dobra, chyba to jest to"

            if slownik == 1:
                menu:
                    "{b}I na koniec muszę udekorować...{/b}"
                    
                    "{b}Lukrem{/b}":
                        $ ciastol += 0

                    "{b}Truskawkami{/b}":
                        $ ciastol += 1
            
            else:
                menu:
                    "{b}I na koniec muszę udekorować...{/b}"

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}糖霜{/font}{/b}":
                        $ ciastol += 0

                    "{b}{font=fonts/NotoSansTC-Regular.ttf}奶油{/font}{/b}":
                        $ ciastol += 1

            luszcz "Dobra, chyba wszystko"

            show lilith neutral3:
                yoffset 0
                linear 0.15 yoffset -50
                linear 0.15 yoffset 0

            lilith "Nie zapomnij dodać trochę miłości ❤️!"

            show luszcz neutral right

            luszcz "Tak, tak dodałam na pewno, na pewno, pewnie, jasne, zobaczymy, czas pokaże"

            show lilith neutral2

            lilith "...?"

            luszcz "No dodałem no mówie, że dodałem"

            show lilith neutral5

            lilith "hmmmm"

            show lilith neutral3

            lilith "No dobra to teraz do piekarnika i poczekać 30 min i gotowe"

            menu:
                "{b}Włóż ciasto do piekarnika{/b}":
                    $ ado += 1

            hide luszcz 
            hide lilith 
            window hide
            show layer master:
                zoom 1.0
                xalign 0.34 yalign 0.865
                linear 0.0 zoom 3.4

            play music "audio/music/lilith4.mp3"

            call screen oven_text_game

            window show
            stop music
            play sound "audio/sfx/ding.mp3"
            "{i}*Ding*{/i}{nw=1.0}"

            menu:
                "{b}Otwórz piekarnik{b}":
                    $ ado += 1

            if score >= 25:
                show layer master:
                    linear 0.1 zoom 1.0 xalign 0.5 yalign 0.5

                show lilith neutral3 at left
                show luszcz neutral right at slightright
                play music "audio/music/lilith5.mp3"
            else:
                window hide
                hide screen clock
                if hitlerlil == 1:
                    scene hitlert
                if stalinlil == 1:
                    scene stalint
                if placlil == 1:
                    scene plact
                if lechialil == 1:
                    scene lechiat
                if jezuslil == 1:
                    scene jezust
                if kennedylil == 1:
                    scene kennedyt
                if smolensklil == 1:
                    scene smolenskt
                $ renpy.movie_cutscene("timee.webm")

                "{nw=0.5}"
                window show
                scene bg black with fade
                "{i}...{/i}"
                if hitlerlil == 1:
                    luszcz "(Jezu gdzie ja jestem)"
                    luszcz "(nic nie widzę)"
                    luszcz "(Moja głowa, moje oczy piekielnie bolą)"

                    glos "Wujku, wujku zobacz"

                    luszcz "(jaki wujku?)"

                    nikt "Już, już patrzę"

                    window hide
                    scene bg gnoms with fade
                    play music "audio/music/erika.mp3"
                    scene bg argentyna with fade
                    window show

                    show hitlerli at slightright
                    show wnuk at slightleft

                    adolf "co takiego chcesz pokazać wujkowi?"

                    chlopiec "patrz jaki obrazek narysowałem"

                    show holokaust zorder 50 at center
                    ""
                    hide holokaust

                    adolf "piękny, piękny, ale pamiętaj, żeby nie pokazywać nikomu innemu tego obrazka!"

                    chlopiec "czemó?"

                    adolf "bo świat nie jest jeszcze gotowy na takie arcydzieło"

                    chlopiec "dobrze wujku!"

                    hide wnuk
                    show hitlerli at center

                    adolf "ehhh jak te dzieci szybko rosną"

                    luszcz "(chwila, chwila co się dzieje czemu jestem w ciele Adolfa Hitlera?)"

                    luszcz "(I czemu jestem w Argentynie?)"

                    show mosad1 at left
                    show mosad2 at slightleft
                    show mosad3 at right
                    show hitlerli at center

                    mosad "Panie Adolfie, pan pójdzie z nami!"

                    adolf "Scheiße, nein, nein, nein! Ich gehe nirgendwohin!"

                    mosad "Nie ma tak, że nie! Pójdzie pan z nami nawet jeśli pan nie chce!"

                    play sound "audio/sfx/neck.mp3"
                    scene bg black
                    stop music

                    luszcz "(Ała, to bolało)"

                    mosad "Szefie co z nim robimy?"

                    glos "Przywieźcie go do Skały i zamknijcie w naszym skarbcu pod cmentarzem!"

                    glos "{cps=65}od teraz spędzi tam wieczność pilnując naszych skar…{/cps}{nw=0.2}"
                
                if jezuslil == 1:
                    luszcz "(Jezu gdzie ja jestem)"
                    luszcz "(czemu, czemu nic nie widzę?)"
                    luszcz "(moje oczy, bolą, piekielnie bolą)"

                    glos "ruszaj się, nie mamy całego dnia!"

                    luszcz "(dobra już idę)"

                    nikt "idę, idę!"

                    luszcz "(….?)"

                    "{i}*kilka minut później*{/i}"

                    glos "dobra kładź się tutaj"

                    glos "i rozłóż ręce na boki"

                    nikt "A to będzie boleć"

                    luszcz "(chwila co ma boleć?)"

                    glos "nie nie skądże?"
                    glos "ledwo poczujesz"

                    luszcz "(a to git)"

                    glos "dobra, zaczynam!"

                    play sound "audio/sfx/mlotek.mp3"
                    queue sound "audio/sfx/krzyk.mp3"
                    $ renpy.pause(1.0)

                    lunikt "Ała kurwaaaaaaaa japierdole, ale boli"

                    glos "dobra teraz druga"

                    lunikt "Jaka niby druga!?"

                    glos "no przykro mi ziomuś ale masz 2 ręce"

                    nikt "😢"

                    glos "dobra zaczynam"

                    play sound "audio/sfx/mlotek.mp3"
                    queue sound "audio/sfx/krzyk.mp3"
                    $ renpy.pause(1.0)

                    lunikt "Japierdole boli jak diabli kurwa kurwa aaaaaaa w chój +1"

                    glos "no a teraz nogi"

                    lunikt "że co kurwa!?"

                    play sound "audio/sfx/mlotek.mp3"
                    queue sound "audio/sfx/krzyk.mp3"
                    $ renpy.pause(1.0)

                    lunikt "Ahhhhh kurwa ty matko jebco pieerdolony, zajębię Cię, zajebię!!!"

                    glos "no a teraz podnosimy"
                    glos "raz, dwa, trzy i hop"

                    window hide
                    scene bg gnoms with fade
                    play music "audio/music/krzyz.mp3"
                    scene bg krzyz with fade
                    show legionista1 at left
                    window show

                    luszcz "(Jezu, gdzie ja jestem?)"
                    luszcz "(I czemu wiszę na krzyżu w ciele Jezusa!?)"

                    show legionista2 at right

                    legionista2 "I jak, skończyłeś?"

                    legionista1 "No niby tak, ale trochę krzywo mi się wydaję"

                    legionista2 "hmmm, no możę jak się lepiej przyglądnie to coś tam widać"

                    legionista1 "Widzisz! Mówiłem, że jest krzywo!"

                    legionista1 "Trzba, będzie to poprawić!"

                    lujezus "Nie kurwa, nie ruszajcie mnie, błagam tak jest dobrze!"
                    
                    jezus 'Ja się sam przesunę patrzcie, już bioderko lekko w lewo dam i będzie prosto!'

                    legionista1 "Nie no teraz to jest jeszcze gorzej!"
                    legionista2 "Sorry ziomuś, ale bez poprawki się nie obejdzie"

                    jezus "😢"

                    scene bg black with fade
                    play sound "audio/sfx/krzyk.mp3"
                    "{i}*kilka minut jęków później*{/i}"
                    scene bg krzyz with fade
                    show legionista1 at left
                    show legionista2 at right

                    legionista1 "No dobra, teraz to już jest prosto"
                    legionista2 "hmmm, no niby choć ta prawa noga tak lekko odcho.."

                    lujezus "Dość, jest git, nie ruszajcie mnie już, błagam!"

                    legionista1 "..."

                    legionista2 "..."

                    legionista1 "No dobra, niech Ci będzie"
                    
                    legionista1 "To co teraz robimy?"

                    legionista2 "Hmmm, chodźmy się nachlać!"

                    legionista1 "Marian, ty to masz łeb!"

                    hide legionista1
                    hide legionista2

                    luszcz "(...)"

                    jezus "..."

                    luszcz "(Ciekawe ile czasu będę tu wisiał zanim umrę?)"

                    jezus "około 6 godzin"

                    luszcz "(Jezus, maria!)"

                    jezus 'Skąd znasz moją matke?'

                    luszcz "(Ty mnie słyszysz!!!?)"

                    jezus "No tak, jestem synem Boga, oczywiście, że cię słyszę"

                    luszcz "(To czemu nie mówiłeś wcześniej!?)"

                    jezus "No, bo myślałem, że jesteś z ekipy filmowej czy coś"

                    luszcz "(Jakiej niby ekipy filmowej!?)"

                    jezus "No, nie wiem no myślałem, że w przyszłości stanę sie popularny i ktoś będzie chciał nakręcić film dokumentalny o mnie"
                    jezus "I nie chciałem zepsuć żadnego ujęcią więc nic nie mówiłem do Ciebie"

                    luszcz "(...)"
                    luszcz "(Nie jesteś w żadnym filmie)"

                    jezus "Wiem, ale ty jesteś"

                    luszcz "(Co?)"

                    jezus "Jajco boom"

                    luszcz "(...)"

                    jezus "..."
                    jezus "masz pomysł co możemy porobić?"

                    luszcz "(Wiem! Mam pomysł!)"

                    jezus "jaki!?"

                    luszcz "(Możemy powisieć na krzyżu)"
                    
                    jezus "hahaha mega zabawne"
                    jezus "A coś co możemy zrobić OPRÓCZ wiszenia na krzyżu?"

                    luszcz "(A to nie)"

                    jezus "wybornie"

                    luszcz "(...)"

                    jezus "..."

                    luszcz "(...)"

                    jezus "..."

                    luszcz "(...)"

                if lechialil == 1:
                    luszcz "(Auuuu co się staneło?)"
                    luszcz "(Głowa, głowa boli od pizzy)"
                    luszcz "(I oczy, nic nie widzę!)"

                    glos "…dlatego w imieniu Imperium Lechitów ja Lech V zawieram święty i nierozerwalny sojusz z kosmitami!"

                    glosy "…brawo niech żyje wielka lechia!"

                    glos "…i aby przypieczętować ten sojusz mój syn Lech VI pojmie za żonę tę oto córkę kosmitów Kunegundę!"

                    window hide
                    scene bg gnoms with fade
                    play music "audio/music/lechia.mp3"
                    scene bg sala_tronowa with fade
                    window show

                    show lechv at center
                    show lechvi at slightleft2
                    show kunegunda at slightright2

                    lechv "Lechu czy przyjmujesz tą oto Kunegundę za żonę?"

                    lechvi "Tak przyjmuję"

                    luszcz "(Łot de hel!?)"
                    luszcz "(Czemu jestem w ciele księcia lechitów!? 🤯)"

                    lechv "A czy ty Kunegundą przyjmujesz tego oto Lecha VI  za męża?"

                    kunegunda "||ᒷᓭ  ╎  ᔑᓵᓵᒷ!¡ℸ ̣"

                    lechv "nie wiem co ta jaszczura powiedziała, ale uznajmy, że tak!"

                    lechv "w takim razie ogłaszam was mężem i żoną! Możecie się bzyknąć"

                    lechvi "No i sigma"
                    lechvi "dobra jaszczur pakuj manatki i zapraszam na morenke u mnie"

                    luszcz "(!!!) "
                    luszcz "(Zaliczę!?!??!? 🤯🤯🤯)"
                    
                    scene bg black with fade
                    stop music

                    "{i}*15 minut później*{/i}"

                    play music "audio/music/sex.mp3"
                    scene bg lechon with fade
                    show lechvi at center

                    lechvi "ahhh i gdzie ona jest!?"

                    luszcz "(właśnie, gdzie ona się szwęda!?)"

                    show lechvi at slightleft
                    show kunegunda at slightright

                    kunegunda "ᓭ𝙹∷∷||  ╎'ᒲ  ꖎᔑℸ ̣ ᒷ,  ╎  ∴ᔑᓭ  ᓭ⍑╎ℸ ̣ ℸ ̣ ╎リ⊣"

                    lechvi "W końcu jesteś? Gdzieś ty była?"

                    kunegunda "∴ᒷꖎꖎ,  ╎'ᒲ  ℸ ̣ ᒷꖎꖎ╎リ⊣  ||𝙹⚍,  ╎  ᓭ⍑╎ℸ ̣"

                    lechvi "Nic nie rozumiem. Nie możesz gadać po ludzku?"

                    kunegunda "╎  ᓵᔑリ'ℸ ̣ ,  ʖ⚍ℸ ̣   ╎  ⍑ᔑ⍊ᒷ  ᓭ𝙹ᒲᒷℸ ̣ ⍑╎リ⊣  ℸ ̣ ⍑ᔑℸ ̣   ∴╎ꖎꖎ  ⍑ᒷꖎ!¡  ||𝙹⚍  ⚍リ↸ᒷ∷ᓭℸ ̣ ᔑリ↸  ᒲᒷ"

                    show kunegunda zorder 1:
                        xalign 0.75
                        yalign 1.0
                        easeout 0.2 xalign 0.50
                    show lechvi zorder 2

                    $ renpy.pause(0.2)
                    show lechvi ailbib zorder 2
                    $ renpy.pause(0.1)

                    show kunegunda:
                        xalign 0.50
                        yalign 1.0
                        easeout 0.2 xalign 0.75

                    "{i}*Kunegunda wręcza Lechowi VI tajemniczą książkę*{/i}"

                    lechvi "chwila co to jest?"

                    kunegunda "To księga spisana w języku mojego ludu. Kiedy masz ją w rękach to rozumiesz naszą mowę."

                    lechvi "Jezus maria ty mówisz!?"

                    kunegunda "No tak, a co myślałeś?"

                    lechvi "Nie wiem, nieważne chodźmy się ruchać"

                    kunegunda "z przyjemnością"

                    scene bg black with fade

                    kunegunda "Ahhh, jak dobrze ahhhh"

                    kunegunda "Ohh, ohhhh, Nie tutaj nie wkłada!"

                    play sound "audio/sfx/krzyk.mp3"
                    
                    llechvi "Aaaaghhhh!"

                    kunegunda "Tu mam trującego kolca w dupie..."

                    llechvi "Aarggghh czeeemu niee mówiłaś wczeeeśniej!?"

                    play sound "audio/sfx/spadek.mp3"

                    glos "Książe, co się dzieje!?"

                    glos "Jezus maria, jaszczur zabił księcia!"

                    kunegunda "Nie to nie tak, on sam sobie to zrobił"

                    glos "Zamilcz potworze i tak nie rozumiem co ty mówisz!"
                    glos "Wystarczy mi to co widzę, a widzę nagiego martwego księcia z jakąś skibidi książką pod pachą i z trującym kolcem wbitym w jego maczugę herkulesa!"

                    kunegunda "..."
                    kunegunda "No wiem, że to źle wygląda, ale no to jego wina"

                    glos "{cps=65}Straże, zabijcie ją i wyrzućcie tą piekielną księgę do jezio...{/cps}{nw=0.2}"
                
                if placlil == 1:
                    luszcz "(Jezu co się staneło?)"
                    luszcz "(I czemu, czemu nic nie widzę?)"
                    luszcz "(moje oczy bolą, bolą strasznie)"

                    "{i}…{/i}"
                    "{i}…{/i}"
                    "{i}…{/i}"

                    window hide
                    scene bg gnoms with fade
                    scene bg droga with fade
                    window show

                    luszcz "(Co to za śmieszne miejsce?)"
                    luszcz "(I czemu tu jest tak cicho?)"
                    luszcz "(I dlaczego jestem w ciele jakiegoś bing chillinga!?)"

                    "{i}…{/i}"

                    play music "audio/music/tank.mp3" volume 1.0
                    $ renpy.music.set_volume(0.1, delay=0.0)

                    "{i}…{/i}"

                    $ renpy.music.set_volume(0.2, delay=0.3)
                    
                    "{i}…{/i}"

                    luszcz "(Coś słyszę jakby się zbliżało)"

                    $ renpy.music.set_volume(0.3, delay=0.3)

                    "{i}…{/i}"

                    $ renpy.music.set_volume(0.4, delay=0.3)

                    "{i}…{/i}"

                    $ renpy.music.set_volume(0.5, delay=0.3)

                    "{i}…{/i}"

                    luszcz "(Ej bo coś tu jedzie!)"

                    $ renpy.music.set_volume(0.6, delay=0.3)

                    "{i}…{/i}"

                    $ renpy.music.set_volume(0.7, delay=0.3)

                    "{i}…{/i}"

                    $ renpy.music.set_volume(0.8, delay=0.3)

                    "{i}…{/i}"

                    scene bg droga2

                    $ renpy.music.set_volume(1.0, delay=0.3)

                    luszcz "(Jezus maria to czołg!)"

                    scene bg droga3

                    luszcz "(Nie zostaw mnie! Czemu jedziesz w moim kierunku!?)"

                    scene bg droga4

                    luszcz "(Siad, siad dobry czołg stój!)"

                    scene bg droga5

                    luszcz "(Chinolu spieprzaj stąd, bo nas zaraz rozjedzie!)"

                    scene bg droga6

                    luszcz "(Rusz dupe kurwa, bo umrzemy razem!)"

                    scene bg bloody

                    play sound "audio/sfx/krzyk.mp3"

                    luszcz "(Aaaaa kurwa aaaaaa)"
                    luszcz "(Moja noga japierdole jak boli kurwa!)"

                    play sound "audio/sfx/krzyk.mp3"

                    luszcz "(A kurwa nie! wciąga drugą aaaaaa japierdole aaa!!!)"
                    luszcz "{cps=65}(Japierdole nie moje jądra nie zostaw je tylko nie one aaaaaa kurwa aaaaaa…){/cps}{nw=0.2}"

                if smolensklil == 1:
                    luszcz "(Jezu co się wydarzyło!?)"
                    luszcz "(I czemu, czemu nic nie widzę?)"
                    luszcz "(moje oczy, bolą, piekielnie bolą)"

                    nikt "I tutaj jeszcze jedną zasadzić"
                    nikt "i tam kolejną można"

                    luszcz "(???)"

                    nikt "Oby tym razem mi się udało!"

                    window hide
                    scene bg gnoms with fade
                    play music "audio/music/natura.mp3"
                    scene bg las0 with fade
                    window show
                    show tusk at slightright

                    luszcz "(Gdzie ja jestem!?)"
                    luszcz "(Co to za skibidi las!?)"
                    luszcz "(I czemu jestem w ciele Donalda Tuska!?)"

                    tusk "Dobra tyle starczy, teraz wystarczy tylko czekać"

                    luszcz "(na co?)"

                    tusk "♪ Was ist des Deutschen Vaterland? ♪"
                    tusk "♪ Ist's Schlesierland? Mazowienland? ♪"
                    tusk "♪ Ist's wo am Bug die Rebe blüht? ♪"
                    tusk "♪ Ist's wo am San die Möwe zieht? ♪"

                    scene bg black with fade

                    "{i}*15 minut później*{/i}"

                    scene bg las0 with fade
                    show tusk at slightright

                    tusk "♪ O nein, nein, nein! ♪"

                    scene bg las2
                    show tusk at slightright
                    play sound "audio/sfx/lot.mp3" 

                    tusk "O leci!"

                    scene bg las3
                    show tusk at slightright

                    luszcz "(Nie panie pilocie niech pan nie leci tutaj, bo ma pan dziurę w samolocie!)"

                    play sound "audio/sfx/boom.mp3" 
                    show bu2 zorder 10:
                        xalign 1.0
                        yalign 1.0

                    $ renpy.pause(0.2)
                    scene bg las4
                    show tusk at slightright
                    hide bu2

                    luszcz "(awww shit to już nie jest dziura, z tego to nie ma co zbierać)"

                    scene bg las5
                    show tusk at slightright
                    $ renpy.pause(0.8)
                    play sound "audio/sfx/boom.mp3"
                    scene bg las0
                    show tusk at slightright

                    tusk "Ich habe gewonnen!"
                    tusk "Niewidzialne brzozy zadziałały!!!"
                    tusk "Po tylu latach nareszcie Niemcy odzyskają chwałę!"
                    tusk "{cps=65}A ja będę mógł znów jak za starych dobrych lat, pobić się w jakiejś usta...{/cps}{nw=0.2}"

                if stalinlil == 1:
                    luszcz "(Jezu co się wydarzyło!?)"
                    luszcz "(I czemu, czemu nic nie widzę?)"
                    luszcz "(moje oczy, bolą, piekielnie bolą)"

                    nikt "Heh… heh… heh…"
                    nikt "Hheh–khh… khh…"
                    nikt "HAA—khhhh—"

                    play sound "audio/sfx/kaszel.mp3"
                    queue sound "audio/sfx/spadek.mp3"

                    nikt "khh… ghh…"

                    luszcz "(???)"
                    luszcz "(Haloo, czy coś się stało?)"

                    "{i}...{/i}"
                    "{i}...{/i}"
                    "{i}...{/i}"

                    scene bg black with fade

                    "{i}*Kilka godzin później*{/i}"

                    glos "Jezu, ale jebie"
                    
                    luszcz "(..?)"

                    "{i}*szmery*{/i}"

                    window hide
                    scene bg gnoms with fade
                    play music "audio/music/sralin.mp3"
                    scene bg stalinka with fade
                    window show
                    show stalin duch right at left
                    show sralin dead at center
                    show beria neutral at right

                    luszcz "(Chwila, co się dzieje!?)"
                    luszcz "(Czemu jestem w ciele Józefa Stalina!?)"
                    luszcz "(I czemu Stalin nie żyje i żyje jednocześnie!?)"

                    stalin "(Ekhhh, gdybym nadał żył to on, by już wąchał kwiatki od dołu)"
                    stalin "(Choć w piekle to chyba nie ma za dużo kwiatków, więc no)"
                    stalin "(Tak czy siak jak śmiał mnie nie wpuścić do piekła!?)"
                    stalin "(No, bo tego, że Św. Piotr na sam widok mnie przed bramą wezwie cały hufiec aniołów i zarygluje bramę na 67 rygli to się spodziewałem)"
                    stalin "(Ale, że szatan mnie nie wpuści do piekła, bo obawia się o swoją posadę to się nie spodziewałem)"
                    stalin "(No nic, będę musiał tu zostać na trochę dłużej)"

                    luszcz "(Chwila, wtf co!?)"
                    luszcz "(Co tu się odwala!?)"
                    luszcz "(Stalin umarł, ale nie wpuścili go do nieba ani piekła, więc jest duchem, w którego ciela teraz jestem!?)"
                    luszcz "(crazy)"

                    with hpunch
                    beria "No gdzie one są! Gdzie są te pieprzone papiery!?"
                    beria "Gdzieś je ukrył stary cepie, nie mam dużo czasu zanim przyjedzie reszta!"

                    "{i}*puk puk*{/i}"

                    beria "Kto tam!?"

                    glos "Hipopotam, wpuszczaj Beria wszyscy jesteśmy w żałobie!"

                    beria "Ahhhh kurwa jest źle"

                    beria "gdzie one są!???"

                    glos "Beria! Bo wyważę drzwi!"

                    beria "Mam! Mam je! Mam te papiery!"
                    
                    beria "Już, już otwieram!"

                    play sound "audio/sfx/door.mp3"
                    show chruszczow neutral zorder 5 at slightright
                    show beria neutral zorder 5 at slightleft
                    show stalin duch right zorder 6 at left
                    show sralin dead zorder 10 at center 

                    show malenkov neutral zorder 6 at right

                    malenkov "Jezus maria, co tu sie staneło!?"

                    beria "Towarzysz Stalin odszedł dziś z naszego świata"

                    chruszczow "O nieeee to tragedia co, co my teraz zrobimy!?"

                    beria "Trzeba, trzeba go położyć na łóżku i wezwać lekarza"

                    chruszczow "Chwila nie wezwałeś jeszcze lekarza!?"

                    beria "No, bo wszyscy są martwi albo na syberii"

                    malenkov "Bo spiskowali przeciwko Towarzyszowi Stalinowi!"

                    chruszczow "Tak, tak oczywiście to sprowadźcie tych z syberii, ale szybko!"

                    beria "Dobra, dobra powiem moim ludzią, ale najpierw trzeba go położyć na łóżku"

                    malenkov "On ma rację, ja biorę za głowę!"

                    chruszczow "To ja zajmuję suty!"

                    chruszczow "Ty Beria masz dół"

                    beria "Czemu!? Ja nie chcę zamieńmy się!"

                    chruszczow "Nuh uh pierwsze słowo do dziennika drugie słowo do śmietnika!"

                    beria "Grrr, zobaczymy czy też tak będzie uważał jak ktoś przypadkiem zezna na Ciebie podczas przesłuchania!"

                    chruszczow "Nie strasz, nie strasz, bo się no wiesz co zrobisz..."

                    beria "..."

                    beria "za późno"

                    malenkov "Skończcie tą bezowocną dyskusję i pomóżcie mi go przenieść"

                    chruszczow "Dobra to na trzy"

                    chruszczow "raz, dwa, trzy..."

                    scene bg black with fade

                    beria "Jezu, ale on ciężki"

                    malenkov "Ciężki jak złoto, z którego było zrobione jego serce!"

                    chruszczow "To te serce musiał mieć zajebiście wielkie, bo moje plecy bolą w ciul"

                    beria "Nie chłopaki ja nie dam rady, muszę chwilę przerwy"

                    play sound "audio/sfx/spadek.mp3"

                    stalin "(Jezus, maria co oni robią z moim ciałem!???)"
                    stalin "(Rzygać mi się chcę jak widzę ich mordy!)"
                    stalin "(Nie, idę stąd tego już za dużo!)"

                    scene bg black with fade
                    stop music

                    "{i}*Kilkadziesiąt lat później*{/i}"

                    scene bg cmentarz_noc with fade
                    play music "audio/music/natura.mp3"
                    show stalin duch right at slightleft
                    show harambe duch at right

                    stalin "Uno!!!"

                    harambe "Dobierać"

                    stalin "I po unie! Bang widzisz Harambe!? To jest prawdziwa siła towarzysza Stalina!"

                    harambe "Stalin wygrać, stalin być nie miły"

                    stalin "Bo ty jesteś tylko głupią małpą Harambe, my w ZSRR takie małpy to wysyłamy w komos, by zdechły!"

                    harambe "Harambe smutny. Harambe mieć wyrzuty sumienia."
                    harambe "Harambe przestać mieć wyrzuty sumienia."

                    stalin "Chwila jakie wyrzuty sumienia!?"
                    
                    show gotka teen at left
                    show stalin duch at center
                    with vpunch

                    gotka "Oooo wielki Stalinie, dni twojej bezowocnej tułaczki nadeszły końca!"
                    gotka "Od teraz będziesz mieszkał w tej oto księdze strzeżąc historii!!!"

                    gotka "ꖎ𝙹⍊ᒷ  ⊣╎⊣ᔑリℸ ̣ ╎ᓵ  ᒲᔑꖎᒷ  ᓵ𝙹ᓵꖌᓭ  ╎  リᒷᒷ↸  ⊣╎⊣ᔑリℸ ̣ ╎ᓵ  ᒲᔑꖎᒷ  ᓵ𝙹ᓵꖌᓭ"

                    stalin "Aaaaaa, co ty ze mną robisz aaaa zostaw!?"

                    gotka "ᓭꖌ╎ʖ╎↸╎  !¡ꖎ𝙹"

                    scene bg black
                    stop music

                    luszcz "(Co się staneło, czemu nic nie widzę!?)"

                    gotka "Towarzyszu Macieju, może pan już wyjść z krzaków!"

                    mac "Ohhh nareszczcie, nogi mnie już zaczynały boleć od kucania"

                    mac "Udało się!?"

                    luszcz "(Chwila, co robi Maciek Maciak w Skale i co miało się udać!?)"

                    gotka "Udało, duch Stalina został zaklęty w tej księdze!"

                    mac "{cps=65}Wyśmienicie, teraz wreszcie będę mógł nauczać ludzi księgą opartą na PRAWDZIWEJ histor...{/cps}{nw=0.2}"





                scene dzis
                stop music
                $ renpy.movie_cutscene("timee.webm")

                "{nw=0.5}"
                window show
                scene bg kuchnia with fade
                play music "audio/music/lilith5.mp3"
                show screen clock
                show lilith neutral4 at left
                show luszcz neutral right at slightright
                luszcz "AAaaaaaaaaaa"

                lilith "Aaaaaa, jezus maria nie strasz!"

                luszcz "Ale, ale ja dopiero co..."

                show lilith neutral5

                lilith "Mam to gdzieś, ja prawie zawału przez Ciebie dostałam!"

                luszcz "ale"

                lilith "Za ale to w morde wale!"

                luszcz "dobrze"

                lilith "..."

                show lilith neutral3

                lilith "Dobra to ja już wróciłeś ze swojej małej podróży w czasie to zobaczmy nasz tort! ❤️"

                luszcz "Jej, zróbmy to!"
            
                menu:
                    "{b}Wyjmij wypiek z piekarnika{/b}":
                        $ ado += 1
            
            if ciastol >= 5:
                show luszcz ciasto 
                luszcz "Tadaaa"

                lilith "Jo udało Ci się!"
                lilith "Tak szczerzę to myślałam, że Ci sie nie uda więc kupiłam na wszelki zapas jeden torcik z cukierni z kotodziewczynkami, ale skoro Ci się udało..."

                luszcz "Aha, czyli masz, aż tak małą wiarę we mnie!?"

                show lilith neutral4

                lilith "To nie tak w sensie no spójrz na siebię."

                luszcz "Chwila co to miało znaczyć!?"

                lilith "Nie nic nie w sensie chodziło mi o to, że..."

                with vpunch

                luszcz "Co to ma znaczyć!?"
            else:
                show luszcz piernik 
                luszcz "Eeeeeeeee, to chyba nie jest tort..."

                show lilith neutral5

                lilith "Niemożliwe, geniusz się znalazł!"
                lilith "A ja myślałam, że to właśnie JEST tort, bo wygląda identycznie!!!"

                luszcz "Dobra no sorki, coś w przepisie musiałem lekko pomyleć"

                show lilith neutral5:
                    yoffset 0
                    linear 0.15 yoffset -50
                    linear 0.15 yoffset 0

                lilith "Lekko!??? Miałeś upiec tort a wyszedł Ci pieprzony piernik!"

                lilith "Szkoda, szkoda strzępić ryja"

            show tata neutral at right
            hide lilith
            show luszcz neutral at center
            with vpunch

            tata "Synu zamknij mordę wiesz, która jest godzina!?"

            luszcz "Wiem Tato, ale do mojego pokoju przyszła Lilith i bardzo nalegała bym upiekł z nią tort i nie chciałem jej wysta..."

            tata "Jaka kurwa Lilith!? Jedyna Lilith jaką znam to Lilith z gry Paper Lily - Chapter 1"
            tata "Fire gra tak btw zagraj w wolnym czasie"

            luszcz "No to to nie ta Lilith!"

            show luszcz neutral right

            luszcz "Chodzi mi o Lilith z gry The NOexistenceN of you AND me, która stoi właśnie za mną..."

            with vpunch
            luszcz "Chwila, gdzie ona znikneła!?"

            tata "Synu, byłeś tutaj sam przez cała czas..."

            show luszcz neutral

            luszcz "Nie tato na serio ona tutaj BYŁA ja to wie..."

            tata "Synu, synu"

            luszcz "Tak tato!?"

            tata "Obiecasz mi jedno?"

            luszcz "Ale co?"

            tata "obiecaj, że pójdziesz do gotki po leki na twoje schorzenie!"

            luszcz "ehhh dobrze obiecuję"

            tata "dobre dziecko"
            tata "A teraz do spania i pamiętaj, że jakby co zawsze będę przy tobie"

            luszcz "Tak, tato wiem"

            tata "No to dobranoc"

            luszcz "dobranoc"
            
            hide tata 

            luszcz "Głupiec, myśli, że że ja zwwwaaariooowałem czy coź!????"
            luszcz "Jaaaa jaaaa mu uddoooowodnie, rzeee Lilith istnieje!"

            if gotka_szpan > 0 or gotka_social_link > 0:
                luszcz "(hm…. Choć z drugiej strony mam pretekst, by iść do gotki hehe)"

            luszcz "Ale najpierw chyba rzeczywiście pójdę spać"

            $ wypadek3 = 1

            scene bg black with fade
            stop music

            if ciastol >= 5:
                $ cake += 1
                $ ile_item += 1

                "{i}*Ciasto Truskawkowe zostało dodane do ekwipunku*{/i}"

            else:
                $ piernik += 1
                $ ile_item_fabularne += 1

                "{i}*Piernik został dodany do ekwipunku*{/i}"

            $ lilith_social_link = 1
            jump spanko_bed

    label lilith2:
        "{i}{/i}"
        n "{i}Tej nocy piekielnie bolał Cię brzuch{/i}"
        n "{i}Zjadłem za dużo pizzy zapewne powiesz?{/i}"
        n "{i}I będziesz miał racje, zjadłeś podczas kolacji dużo za dużo pizzy{/i}"
        n "{i}i dlatego teraz rozbolał cię brzuszek{/i}"
        n "{i}Z tego powodu postanowiłeś udać się do toalety i ”srać”{/i}"
        n "{i}Lecz, gdy już miałeś to uczynić pojawiła się ONA...{/i}"

        window hide
        scene bg gnoms with fade
        play music "audio/music/lilith6.mp3"
        scene bg lilith6 with fade
        window show

        lilith "Ojoj, chyba ktoś tu zjadł za dużo pizzy"

        luszcz "Zejdź ze mnie kobieto! Muszę, muszę się szybko dostać do sracza."

        show bg lilith5

        lilith "Ahhh, nie przejmuj się tym, mam coś co Ci bardziej pomoże"

        show bg lilith3

        lilith "Ta daaa!"

        luszcz "Co to za piguły!? To dzięki nim Ciebie widzę!?"

        lilith "Spokojnie, spokojnie to nic groźnego"
        lilith "To piguły oczyszczające, które uleczą twój organizm"

        luszcz "Na serio!? To dawaj je szybko, bo już się zbliża!"

        lilith "Dam, ale najpierw musisz pamiętać, że co za dużo to nie zdrowo"
        lilith "I zarzycie więcej niż 3 pigułek na dzień może grozić nawet śmiercią!"
        lilith "Zrozumianio!?"

        luszcz "Tak, skończ już pierdolić i daj te piguły szybko błagam, bo już nie daję rady!!!"

        lilith "Dobrze w takim razie..."

        show bg lilith7

        lilith "...za mamusie!"

        luszcz "wooof"

        play sound "audio/sfx/lyk.mp3"
        show bg lilith3

        n "{i}Połknąłeś PIERWSZĄ pigułkę i od razu poczułeś rozluźnienie w swojej dolnej części ciała{/i}"

        luszcz "Ohhhhhh, jak dobrze ohhhhhh!"
        luszcz "Daj jeszcze jedną, jeszcze jedną!"

        lilith "No dobrze, ale pamiętaj, że to już druga!"

        luszcz "woof, woof!"

        show bg lilith8

        lilith "No, to teraz za najlepszą gotkę na świecie!"

        luszcz "woof, woof!"

        play sound "audio/sfx/lyk.mp3"
        show bg lilith3

        n "{i}Połknąłeś DRUGĄ pigułkę i po raz kolejny przez twoje ciało przetoczyła się fala ulgi{/i}"

        luszcz "Ohhhhh, ale bosko ahhhh"
        luszcz "Rób mi tak dalej!"

        lilith "Dobrze, ale pamiętaj że to już ostatnia!"

        luszcz "Tak jest Proszę Pani!"

        show bg lilith10

        lilith "No, to teraz za twoją najlepszą panią doktor!"

        if gotka_szpan == 0 and gotka_social_link == 0:
            luszcz "woof, woof pani Lilith!"
        else:
            luszcz "woof, woof pani aptekarko!"

        play sound "audio/sfx/lyk.mp3"
        show bg lilith5

        n "{i}Połknąłeś TRZECIĄ pigułkę i poczułeś jak niepowstrzymana siła przebija się przez nieporuszalne obiekty w twoich jelitach i wyrzuca je na zewnątrz{/i}"

        if gotka_szpan == 0 and gotka_social_link == 0:
            lilith "Chcesz może zostać moim chłopakiem?"

            n "{i}Phhh chwila co?{/i}"
            n "{i}Nie, nie, nie! Ty masz ją zabić a nie z nią randkować!{/i}"

            luszcz "(WTF Co się tu odjaniepawla!???)"
            luszcz "(Od kiedy ty możesz zwyczajnie gadać!???)"
            luszcz "(I co to kurcze za wyznanie z dupy!???)"

            n "{i}Od zawsze mogłem po prostu tego nie robiłem, by Ci nie przeszkadzać!{/i}"
            n "{i}Ale po usłyszeniu takiej głupoty już nie wytrzymałem!{/i}"

            lilith "To jak? Zostaniesz moim chłopakiem? Hę? Hę? HĘ?"

            n "{i}NIE! Musisz ją zabić, a nie z nią randkować!{/i}"
            n "{i}Wyciągnij swoje nieskaziltelne ostrze z kieszeni i zabij ją!{/i}"

            menu:
                "{b}Wyznaj miłość Lilith{/b}":
                    stop music
                    luszcz "Dobrze niech będzie, zostanę twoim chłopakiem."
                    
                    lilith "Yuppi..."

                    n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                    play music "audio/music/anakin.mp3"

                    n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                    luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                    luszcz "(Ja nie lękam się Lilith jak ty!)"

                    n "{i}...{/i}"

                    luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                    n "{i}Twojej głowy!?{/i}"

                    luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                    n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszemu kierunkowskazu!{/i}"

                    luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                    n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                    n "{i}Ja zrobię co muszę!{/i}"

                    luszcz "(Możesz spróbować!)"

                    luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                    with hpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                    luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                    n "{i}Łuszczu! Lilith jest zła!{/i}"

                    luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                    n "{i}Zatem jesteś zgubiony!{/i}"

                    luszcz "(To twój koniec mój mistrzu!)"

                    with hpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    with hpunch

                    $ renpy.pause(0.3)

                    with vpunch

                    $ renpy.pause(0.3)

                    luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                    n "{i}Nie doceniasz mojej mocy!{/i}"

                    luszcz "(Nie próbuj!)"

                    n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                    with vpunch

                    $ renpy.pause(0.3)
                    play sound "audio/sfx/krzyk.mp3" 
                    stop music

                    luszcz "(Nareszcie! Zwycięstwo jest moje!)"

                    lilith "Skończyłeś już z nim!?"

                    luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                    lilith "No nareszcie!"

                    scene bg black with fade

                    "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                    "{i}I żyli długo i szczęśliwie{/i}"
                    "{i}na pewno, na pewno{/i}"
                    "{i}pewnie, jasne{/i}"
                    "{i}zobaczymy, czas pokaże{/i}"

                    $ lilith_social_link = 2
                    jump spanko_bed



                "{b}Odrzuć zaloty Lilith{/b}":
                    stop music
                    luszcz "Sory babe, ale nie jestem zainteresowany"
                    show bg lilith4
                    lilith "eeeeee chwila cooooooooooooooooooooooooooooo"
                    lilith "oooooooooooooooooooooooooooooo"
                    play music "audio/music/mucha.mp3"
                    show mucha:
                        xalign 0.98
                        yalign 0.4

                    lilith "ooooooooooooooooooooooooooooooooooooooooooooooooooooo"
                    show mucha:
                        xalign 0.90
                        yalign 0.45
                    
                    lilith "ooooooooooooooo"
                    show mucha:
                        xalign 0.82
                        yalign 0.4
                    
                    lilith "oooooooooooooooooooooooooooooooooooooo"
                    show mucha:
                        xalign 0.74
                        yalign 0.35
                    
                    lilith "ooooooooooooooooooooo"
                    show mucha:
                        xalign 0.66
                        yalign 0.3
                    
                    lilith "oooooooooooooooooooooooooooooooooooo"
                    show mucha:
                        xalign 0.58
                        yalign 0.25
                    
                    lilith "ooooooooooooooooooooooooooooooooooooooooooooooooo"
                    show mucha:
                        xalign 0.475
                        yalign 0.20

                    $ renpy.pause(0.5)
                    hide mucha
                    play sound "audio/sfx/lyk.mp3"
                    stop music
                    $ renpy.pause(0.3)
                    queue sound "audio/sfx/spadek.mp3"
                    scene bg black
                    n "{i}Lilith połkneła muchę...{/i}"
                    n "{i}...i umarła!{/i}"

                    luszcz "(Chwila WTF Co!???)"
                    luszcz "(Od MUCHY!???)"

                    n "{i}No tak było, nie zmyślam{/i}"

                    luszcz "(No cóż skoro tak...)"
                    luszcz "(Tylko, że teraz muszę coś zrobić z tym ciałem...)"

                    menu: 
                        "{b}Jeszcze jest ciepla…{/b}":
                            luszcz "Jeszcze jest ciepła..."
                            luszcz "Muszę ją wykorzystać!"

                            n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                            n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                            n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                            $ lilith_social_link = 10
                            $ pills = 20
                            "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                            jump spanko_bed

                        "{b}Muszę ją wykorzystać{/b}":
                            luszcz "Muszę ją wykorzystać"
                            luszcz "..."
                            luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                            n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                            n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                            n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                            n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                            $ money += 3
                            "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                            $ lilith_social_link = 10
                            $ pills = 20
                            "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                            jump spanko_bed


                "{b}Posłuchaj się Narratora{/b}":
                    stop music
                    show pristine_blade

                    n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                    hide pristine_blade

                    play sound "audio/sfx/nuz1.mp3"
                    queue sound "audio/sfx/nuz2.mp3"

                    show bg lilith16

                    n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                    lilith "Ohhh, czyli to tak... czyli tak zginę..."
                    lilith "Skoro tak to musisz wiedzieć, że..."

                    show bg lilith17
                    play sound "audio/sfx/rzygi.mp3"
                    lilith "Blehhh"

                    n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                    luszcz "(No nic i tak była jakaś skibidi)"
                    luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                    menu: 
                        "{b}Jeszcze jest ciepla…{/b}":
                            luszcz "Jeszcze jest ciepła..."
                            luszcz "Muszę ją wykorzystać!"

                            scene bg black with fade

                            n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                            n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                            n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                            window hide
                            play music "audio/music/applause.mp3"
                            call screen full_click_screen("images/good_end.png")
                            stop music
                            window show

                            $ lilith_social_link = 10
                            $ pills = 20
                            "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                            jump spanko_bed

                        "{b}Muszę ją wykorzystać{/b}":
                            luszcz "Muszę ją wykorzystać"
                            luszcz "..."
                            luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                            scene bg black with fade

                            n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                            n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                            n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                            n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                            window hide
                            play music "audio/music/applause.mp3"
                            call screen full_click_screen("images/good_end.png")
                            stop music
                            window show

                            $ money += 3
                            "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                            $ lilith_social_link = 10
                            $ pills = 20
                            "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                            jump spanko_bed

        else:
            if gotka_szpont == 1:
                with vpunch
                gotka "Co tu się odpierdala!?"     
                if yusuke_social_link >= 1 and yusuke_social_link <= 5:
                    if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                        if drukowanko == 1:
                            scene bg pokoj8 
                        else:
                            scene bg pokoj7
                    
                    else:
                        if drukowanko == 1:
                            scene bg pokoj4 
                        else:
                            scene bg pokoj3          

                else:
                    if yusuke_social_link >= 6:
                        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                            if drukowanko == 1:
                                scene bg pokoj6 
                            else:
                                scene bg pokoj5 
                            
                            
                        else:
                            if drukowanko == 1:
                                scene bg pokoj2 
                            else:
                                scene bg pokoj 

                show luszcz neutral right at right
                show lilith neutral5 at left
                show gotka neutral right at slightright
                play music "audio/music/lilith7.mp3"
                gotka "Co to za dziwka na tobie leżała mój nadroższy?"

                luszcz "eee yyy eeee"

                lilith "TO NIE JEST TWÓJ NAJDROŻSZY TYLKO MÓJ!!!"
                lilith "Ja go kocham o wiele bardziej niż ty!"

                gotka "Nieprawda to ja go kocham bardziej!"

                show luszcz blush right
                luszcz "Oj kobiety naprawde nie trzeba"

                with vpunch
                gotka "Zamknij się Łuszczu! My jeszcze porozmawiamy o tym co się tu wydarzyło!"
                show luszcz neutral right
                gotka "Ale najpierw zajmę się tą suką!"

                show gotka noz
                play sound "audio/sfx/epsilon_weapon.mp3"
                n "{i}Gotka wyciągneła nóż.{/i}"

                lilith "Tylko spróbuj!"
                show lilith noz
                play sound "audio/sfx/epsilon_weapon.mp3"
                n "{i}Lilith również wyciągneła nóż{/i}"

                gotka "Aaghhhhh"
                show gotka noz at center:
                    xalign 0.75
                    yalign 1.0
                    easeout 0.4 xalign 0.33

                play music "audio/music/noze.mp3"

                n "{i}Gotka i Lilith starły się w pojedynku na noże{/i}"
                n "{i}TERAZ! TERAZ MUSISZ ZABIĆ LILITH, BY URATOWAĆ SWOJĄ DZIEWCZYNE!{/i}"

                luszcz "(WTF Narrator!??? Od kiedy ty możesz mówić co chcesz!?)"

                n "{i}Zawsze mogłem, ale nie zawsze była potrzeba!{/i}"
                n "{i}A teraz jest potrzeba! Musisz zabić Lilith!{/i}"

                luszcz "Emmm nawet jeśli to niby czym?"

                n "{i}Nieskazitelnym ostrzem! Masz je w kieszeni!{/i}"

                luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                play sound "audio/sfx/epsilon_weapon.mp3"
                show luszcz nuz

                n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                n "{i}Zabij JĄ i uratuj swoją dziewczynę!{/i}"

                label lilith8:
                    menu:
                        "{b}Zabij Lilith{/b}":
                            n "{i}Unosisz ostrze szykując się do ataku.{/i}"

                            stop music

                            show luszcz nuz zorder 12 at center:
                                xalign 0.9
                                yalign 1.0
                                easeout 0.4 xalign 0.33

                            show gotka noz at center:
                                xalign 0.33
                                yalign 1.0
                                easeout 0.4 xalign 0.9

                            $ renpy.pause(0.3)

                            play sound "audio/sfx/nuz1.mp3"
                            queue sound "audio/sfx/nuz2.mp3"

                            show luszcz neutral right

                            show lilith ranny:
                                xalign 0.0
                                yalign 1.0

                            n "{i}I wbijasz je w serce lilith!{/i}"

                            lilith "Ohhh, czyli to tak... czyli tak zginę..."
                            lilith "Skoro tak to musisz wiedzieć, że..."

                            show lilith dead
                            show gotka neutral right

                            n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                            luszcz "(No trudno tak się zdarza)"
                            
                            gotka "Jezus maria, skarbie coś ty odjebał!???"

                            show luszcz neutral

                            luszcz "..?"

                            gotka "JA CHCIAŁAM JĄ TYLKO NASTRASZYĆ, A NIE OD RAZU ZABIJAĆ!"

                            luszcz "..."
                            luszcz "upsi?"

                            show luszcz neutral zorder 12 at center:
                                xalign 0.33
                                yalign 1.0
                                easeout 0.4 xalign 0.9

                            show gotka neutral right at center:
                                xalign 0.9
                                yalign 1.0
                                easeout 0.4 xalign 0.33

                            $ renpy.pause(0.3)

                            show luszcz neutral right

                            gotka "Ehhhh, dobra trzeba się pozbyć ciała"
                            gotka "Mam kontakty powinno mi się udać bez zawiadamiania policji"

                            luszcz "..."

                            gotka "Dobra, to ja idę, a ty tu zostań i nie wpakuj się w żadne kłopoty!"

                            luszcz "Dobrze gigasigmo..."

                            gotka "A i pamiętaj..."
                            gotka "...kocham Cię!"

                            scene bg black with fade

                            n "{i}Gotka odeszła, a Ty zostałeś sam w pokoju razem z myślami{/i}"
                            n "{i}Przez wiele godzin nie mogłeś zmrużyć oczu, lecz ostatecznio udało Ci się zasnąć{/i}"

                            $ lilith_social_link = 10
                            jump spanko_bed

                        "{b}Zabij Gotkę{/b}":
                            n "{i}Unosisz ostrze szykując się do ataku.{/i}"

                            stop music

                            show luszcz nuz zorder 12 at center:
                                xalign 0.9
                                yalign 1.0
                                easeout 0.4 xalign 0.6
                            
                            $ renpy.pause(0.3)

                            play sound "audio/sfx/nuz1.mp3"
                            queue sound "audio/sfx/nuz2.mp3"

                            show luszcz neutral right zorder 12

                            show gotka ranny

                            n "{i}I wbijasz je w serce gotki!?!?!?{/i}"
                            n "{i}Coś, coś ty uczynił!?!?!?{/i}"

                            gotka "Ohhhh, i ta dziwka jest niby lepsza odemn..."

                            show gotka dead

                            n "{i}Gotka umarła nim zdążyła dokończyć.{/i}"
                            n "{i}Jezus maria, coś ty uczynił!?{/i}"

                            show lilith neutral2 zorder 12 at center:
                                xalign 0.0
                                yalign 1.0
                                easeout 0.4 xalign 0.15

                            lilith "Ohhh, kochany wiedziałam, że mnie wybierzesz!"
                            lilith "Teraz możemy być razem na zawsze!"
                            lilith "..."
                            lilith "Lecz najpierw trzeba się pozbyć tego robaka z twojej głowy!"

                            play sound "audio/sfx/krzyk.mp3" 

                            n "{i}Nie, nie co ty robisz aghhhhhh!{/i}"

                            scene bg black with fade

                            "{i}Narrator został unicestwiony, a ty i Lilith żyliście długo i szczęśliwie!"
                            "{i}na pewno, na pewno{/i}"
                            "{i}pewnie, jasne{/i}"
                            "{i}zobaczymy, czas pokaże{/i}"

                            $ lilith_social_link = 2
                            $ gotka_social_link = 10
                            jump spanko_bed
                        
                        "{b}Zabij Się{/b}":
                            luszcz "Eeeeeghhhh!"
                            luszcz "nie jednak nie"
                            jump lilith8

            else:
                stop music
                with vpunch
                show bg lilith4
                lilith "Coś ty właśnie powiedział!?"

                luszcz "No eeee, że pani z apteki jest najlepsza na świecie?"

                lilith "Jako kurwa kurwa z apteki!?!!?"
                lilith "Przecież to ja jestem NAJLEPSZĄ PANIĄ DOKTOR NA ŚWIECIE!!!"

                luszcz "Emmm, no chyba nie..."
                luszcz "Po pierwsze, nie jesteś nawet prawdziwom gotką!"
                luszcz "Po drógie, nie traktujesz mnie jak swoją świnkę doświadczalną i ostrzegaż mnie przed efektami óbocznymi lekó!"
                luszcz "A po trzecie, to ty nawet nie istniejeż!"

                show bg lilith5
                
                lilith "..."

                show bg lilith11
                lilith "zabiję cię"

                luszcz "chwila co?"

                show bg lilith12
                play music "audio/music/lilith7.mp3"

                n "{i}Lililth nie wachając się już ani chwili, wyciągneła ponownie słoik z pigułkami i zaczeła go otwierać{/i}"

                lilith "Zobaczmy co się stanie po zarzyciu 4 pigułek!"

                show bg lilith7

                lilith "Za twoją dziwke z apteki!"

                show bg lilith13

                n "{i}Nim zdążyłeś zareagować, Lilith włożyła Ci pigułkę do ust{/i}"

                luszcz "(Awww shit, muszę ją wypluć zanim ją połknę!)"
                luszcz "(Czuję ją gdzieś za moim prawym górnym siekaczem przyśrodkowym)"

                menu:
                    "{b}Skąd wypluć pigułkę?{/b}"

                    "{b}Zza drugiego siekacza{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza drugim siekaczem nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3

                    "{b}Zza siekacza centralnego{/b}":
                        play sound "audio/sfx/plucie.mp3"

                        n "{i}Dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                        lilith "Ahhh, czyli to tak się bawimy!?"
                        lilith "To zobaczymy jak sobie poradzisz z kolejną pigułką!"

                        show bg lilith18

                        if leki == 1:
                            luszcz "(Mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

                            menu:
                                "{b}Czy wziąść leki na schizofrenię?{/b}"

                                "{b}Tak{/b}":
                                    n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                                    n "{i}NIE! Nie zgadzam się!{/i}"

                                    luszcz "(Wtf!? Od kiedy ty możesz mieć własne zdanie!?)"

                                    n "{i}Próbowałem się nie wtrącać i tylko komentować wydarzenia, ale gdy usłyszałem tak głupi pomysł to nie wytrzymałem!{/i}"

                                    luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                                    n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                                    luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                                    play sound "audio/sfx/epsilon_weapon.mp3"
                                    show pristine_blade zorder 50 at center

                                    n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                                    luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                                    n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                                    luszcz "(Ej chwila skąd się ten koniec świata pojawił!? Nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                                    n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                                    n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                                    luszcz "(Yhy da da, zdemaskowałeś się!)"
                                    luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                                    luszcz "(Biorę te leki i elo!)"

                                    n "{i}Nie mogę Ci na to pozwolić!{/i}"
                                    n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                                    menu:
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Ostrzeż Lilith{/b}":
                                            $ klil = 0
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1

                                    if klil == 1:
                                        stop music
                                        n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                                        hide pristine_blade

                                        play sound "audio/sfx/nuz1.mp3"
                                        queue sound "audio/sfx/nuz2.mp3"

                                        show bg lilith16

                                        n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                                        lilith "Ohhh, czyli to tak... czyli tak zginę..."
                                        lilith "Skoro tak to musisz wiedzieć, że..."

                                        show bg lilith17
                                        play sound "audio/sfx/rzygi.mp3"
                                        lilith "Blehhh"

                                        n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                                        luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                                        luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                                        menu: 
                                            "{b}Jeszcze jest ciepla…{/b}":
                                                luszcz "Jeszcze jest ciepła..."
                                                luszcz "Muszę ją wykorzystać!"

                                                scene bg black with fade

                                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                                n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                                n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                                window hide
                                                play music "audio/music/applause.mp3"
                                                call screen full_click_screen("images/good_end.png")
                                                stop music
                                                window show

                                                $ lilith_social_link = 10
                                                $ pills = 20
                                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                                jump spanko_bed

                                            "{b}Muszę ją wykorzystać{/b}":
                                                luszcz "Muszę ją wykorzystać"
                                                luszcz "..."
                                                luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                                scene bg black with fade

                                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                                n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                                n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                                n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                                window hide
                                                play music "audio/music/applause.mp3"
                                                call screen full_click_screen("images/good_end.png")
                                                stop music
                                                window show

                                                $ money += 3
                                                "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                                $ lilith_social_link = 10
                                                $ pills = 20
                                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                                jump spanko_bed

                                    else:
                                        n "{i}Przestań.{/i}"

                                        show bg lilith3

                                        lilith "Ohhh, czyli to wszystko jest jego wina..."
                                        lilith "Przykro mi... Postaram się to zrobić szybko."

                                        show bg lilith15
                                        hide pristine_blade
                                        stop music

                                        play sound "audio/sfx/nuz1.mp3"
                                        queue sound "audio/sfx/nuz2.mp3"

                                        n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                                        lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                                        play sound "audio/sfx/spadek.mp3"
                                        scene bg black
                                        voice "audio/voice/narrator1.mp3"

                                        n "{i}Zapada ciemność i umierasz.{/i}"

                                        jump lilith4
                                
                                "{b}Nie{/b}":
                                    luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

                        lilith "smaczneeego!"

                        show bg lilith13

                        n "{i}Lilith po raz kolejny włożyła Ci pigułkę do ust{/i}"
                        n "{i}Tym razem jednak wyczułeś ją za swoim lewym górnym małym trzonowcem{/i}"
    
                    "{b}Zza dens molaris primus{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza dens molaris primus nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3

                menu:
                    "{b}Skąd wypluć pigułkę?{/b}"

                    "{b}Zza trzonowca pierwszego{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza pierwszym trzonowcem nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3
                    
                    "{b}Zza trzonowca drugiego{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza drugim trzonowcem nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3
                    
                    "{b}Zza przedtrzonowca pierwszego{/b}":
                        play sound "audio/sfx/plucie.mp3"

                        n "{i}Znowu dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                        lilith "Grrrr, dobry w to jesteś!"
                        lilith "Ale ja się tak szybko nie poddam!"

                        show bg lilith19

                        if leki == 1:
                            luszcz "(Nadal mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

                            menu:
                                "{b}Czy wziąść leki na schizofrenię?{/b}"

                                "{b}Tak{/b}":
                                    n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                                    n "{i}NIE! Nie zgadzam się!{/i}"

                                    luszcz "(Wtf!? Od kiedy ty możesz mieć własne zdanie!?)"

                                    n "{i}Próbowałem się nie wtrącać i tylko komentować wydarzenia, ale gdy usłyszałem tak głupi pomysł to nie wytrzymałem!{/i}"

                                    luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                                    n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                                    luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                                    play sound "audio/sfx/epsilon_weapon.mp3"
                                    show pristine_blade zorder 50 at center

                                    n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                                    luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                                    n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                                    luszcz "(Ej chwila skąd się ten koniec świata pojawił!? Nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                                    n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                                    n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                                    luszcz "(Yhy da da, zdemaskowałeś się!)"
                                    luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                                    luszcz "(Biorę te leki i elo!)"

                                    n "{i}Nie mogę Ci na to pozwolić!{/i}"
                                    n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                                    menu:
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Ostrzeż Lilith{/b}":
                                            $ klil = 0
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1
                                        "{b}Zabij Lilith{/b}":
                                            $ klil = 1

                                    if klil == 1:
                                        stop music
                                        n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                                        hide pristine_blade

                                        play sound "audio/sfx/nuz1.mp3"
                                        queue sound "audio/sfx/nuz2.mp3"

                                        show bg lilith16

                                        n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                                        lilith "Ohhh, czyli to tak... czyli tak zginę..."
                                        lilith "Skoro tak to musisz wiedzieć, że..."

                                        show bg lilith17
                                        play sound "audio/sfx/rzygi.mp3"
                                        lilith "Blehhh"

                                        n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                                        luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                                        luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                                        menu: 
                                            "{b}Jeszcze jest ciepla…{/b}":
                                                luszcz "Jeszcze jest ciepła..."
                                                luszcz "Muszę ją wykorzystać!"

                                                scene bg black with fade

                                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                                n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                                n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                                window hide
                                                play music "audio/music/applause.mp3"
                                                call screen full_click_screen("images/good_end.png")
                                                stop music
                                                window show

                                                $ lilith_social_link = 10
                                                $ pills = 20
                                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                                jump spanko_bed

                                            "{b}Muszę ją wykorzystać{/b}":
                                                luszcz "Muszę ją wykorzystać"
                                                luszcz "..."
                                                luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                                scene bg black with fade

                                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                                n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                                n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                                n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                                window hide
                                                play music "audio/music/applause.mp3"
                                                call screen full_click_screen("images/good_end.png")
                                                stop music
                                                window show

                                                $ money += 3
                                                "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                                $ lilith_social_link = 10
                                                $ pills = 20
                                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                                jump spanko_bed

                                    else:
                                        n "{i}Przestań.{/i}"

                                        show bg lilith3

                                        lilith "Ohhh, czyli to wszystko jest jego wina..."
                                        lilith "Przykro mi... Postaram się to zrobić szybko."

                                        show bg lilith15
                                        hide pristine_blade
                                        stop music

                                        play sound "audio/sfx/nuz1.mp3"
                                        queue sound "audio/sfx/nuz2.mp3"

                                        n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                                        lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                                        play sound "audio/sfx/spadek.mp3"
                                        scene bg black
                                        voice "audio/voice/narrator1.mp3"

                                        n "{i}Zapada ciemność i umierasz.{/i}"

                                        jump lilith4
                                
                                "{b}Nie{/b}":
                                    luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

                        lilith "adios żartownisiu!"

                        show bg lilith13

                        n "{i}Lilith po raz trzeci włożyła Ci pigułkę do ust{/i}"
                        n "{i}Tym razem jednak wyczułeś ją za swoim lewym dolnym dens incisivus lateralis{/i}"
                
                menu:
                    "{b}Skąd wypluć pigułkę?{/b}"

                    "{b}Zza zębem mądrości{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza zębem mądrości nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3
                    
                    "{b}Zza siekaczem bocznym{/b}":
                        play sound "audio/sfx/plucie.mp3"

                        n "{i}Kolejny raz dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                        lilith "Nie! Nie! Nie! Ty musisz umrzeć!"

                        n "{i}Lilith po raz kolejny sięgnęła do słoika, lecz tym razem utkneła jej w nim ręka!{/i}"

                        show bg lilith14

                        show deszcz zorder 15
                        play music "audio/music/deszcz.mp3"

                        n "{i}W dodatku z jakiegoś powodu zaczeło padać!?{/i}"

                        luszcz "(Chwila co!??? WTF jaki kurcze deszcz?!?)"
                        luszcz "(Przecież jesteśmy w środku pokoju!?)"

                        n "{i}Nie wiem noo ja jedynie stwierdzam fakty!!!"

                        luszcz "(Hmmm, dziwne)"
                        luszcz "(anyway, muszę coś z tym zrobić!)"

                        n "{i}Zauważasz leżący w końcie pokoju parasolkę{/i}"

                        luszcz "(O, parasolka! To może mi pomóc!)"

                        n "{i}NIE! Zostaw ją! Teraz musisz zabić Lilith póki masz okazję!{/i}"

                        luszcz "(Emmmm, no nie mówię, że nie masz całej racji, ale od razu zabić?)"
                        with hpunch 
                        $ renpy.pause(0.3)
                        with hpunch
                        $ renpy.pause(0.3)
                        luszcz "(Patrz jak ona się trzęsię z zimna i jest taka bezbronna! Nie mogę jej zabić!)"

                        n "{i}Musisz ją zabić!{/i}"

                        menu:
                            "{b}Posłuchaj się Narratora{/b}":
                                hide deszcz
                                stop music
                                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                                hide pristine_blade

                                play sound "audio/sfx/nuz1.mp3"
                                queue sound "audio/sfx/nuz2.mp3"

                                show bg lilith16

                                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                                lilith "Ohhh, czyli to tak... czyli tak zginę..."
                                lilith "Skoro tak to musisz wiedzieć, że..."

                                show bg lilith17
                                play sound "audio/sfx/rzygi.mp3"
                                lilith "Blehhh"

                                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                                luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                                luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                                menu: 
                                    "{b}Jeszcze jest ciepla…{/b}":
                                        luszcz "Jeszcze jest ciepła..."
                                        luszcz "Muszę ją wykorzystać!"

                                        hide deszcz
                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ lilith_social_link = 10
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                        jump spanko_bed

                                    "{b}Muszę ją wykorzystać{/b}":
                                        luszcz "Muszę ją wykorzystać"
                                        luszcz "..."
                                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                        hide deszcz
                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ money += 3
                                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"

                                        $ lilith_social_link = 10
                                        jump spanko_bed

                            "{b}Użyj parasola{/b}":
                                $ renpy.music.set_volume(0.25, delay=0.3)
                                hide deszcz
                                n "{i}Otworzyłeś parasolkę i schroniłeś się pod nią razem z Lilith!{/i}"
                                n "{i}Co ty wyprawiasz!? Miałeś ją zabić!{/i}"

                                show bg lilith3

                                lilith "..? Czemu? Czemu to zrobiłeś?"
                                lilith "Nie rozumiem... Przecież chciałam Cię zabić!?"

                                luszcz "Bo, bo ja Ciebie kocham Lilith!"
                                luszcz "Czy zostaniesz moją dziewczyną?"

                                lilith "Ohhh... Oczywiście, że tak!"
                                lilith "Oto, oto mi chodziło od początku!"

                                n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                                play music "audio/music/anakin.mp3"

                                n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                                luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                                luszcz "(Ja nie lękam się Lilith jak ty!)"

                                n "{i}...{/i}"

                                luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                                n "{i}Twojej głowy!?{/i}"

                                luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                                n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszemu kierunkowskazu!{/i}"

                                luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                                n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                                n "{i}Ja zrobię co muszę!{/i}"

                                luszcz "(Możesz spróbować!)"

                                luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                                with hpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                                luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                                n "{i}Łuszczu! Lilith jest zła!{/i}"

                                luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                                n "{i}Zatem jesteś zgubiony!{/i}"

                                luszcz "(To twój koniec mój mistrzu!)"

                                with hpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                with hpunch

                                $ renpy.pause(0.3)

                                with vpunch

                                $ renpy.pause(0.3)

                                luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                                n "{i}Nie doceniasz mojej mocy!{/i}"

                                luszcz "(Nie próbuj!)"

                                n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                                with vpunch

                                $ renpy.pause(0.3)
                                play sound "audio/sfx/krzyk.mp3" 
                                stop music

                                luszcz "(Nareszcie! Zwycięstwo jest moje!)"

                                lilith "Skończyłeś już z nim!?"

                                luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                                lilith "No nareszcie!"

                                scene bg black with fade

                                "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                                "{i}I żyli długo i szczęśliwie{/i}"
                                "{i}na pewno, na pewno{/i}"
                                "{i}pewnie, jasne{/i}"
                                "{i}zobaczymy, czas pokaże{/i}"

                                $ lilith_social_link = 2
                                jump spanko_bed
                    
                    "{b}Zza głównym zębem żującym{/b}":
                        stop music
                        n "{i}...{/i}"
                        n "{i}Niestety zza głównym zębem żującym nie było żadnej pigułki{/i}"

                        play sound "audio/sfx/lyk.mp3"

                        n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                        with vpunch
                        luszcz "NIE!"
                        luszcz "To nie może się tak skończyć!"

                        n "{i}Lecz twoje błagania nic nie dały{/i}"

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith3

    label lilith4:
        hide screen global_eq_key
        hide screen clock
        window hide
        $ renpy.pause(1.5)
        scene bg lilith3 with fade
        show screen global_eq_key
        show screen clock
        play music "audio/music/lilith1.mp3"
        n "{i}Jesteś na łóżku w twoim pokoju. Na tobie jest Lilith.{/i}"
        n "{i}Jesteś tu, żeby ją zabić. Jeśli tego nie zrobisz, to będzie koniec świata.{/i}"

        luszcz "(Aaaghhh, co ty nie powiesz!? Ostatnio też tak mówiłeś i co? I co?)"
        luszcz "(Umarłem przez ciebie!!!)"

        rizzler "(Dokładnie, ty ty barbarzyńco! Chciałeś zabić moją ukochaną Lilith!)"

        n "{i}Po pierwsze to nie jest żadna \"twoja ukochana\"{/i}"
        n "{i}A po drugie nie przypominam sobię, żeby coś takiego się wydarzyło!{/i}"

        luszcz "(Kiedy miałem wziąść leki na schizofrenię przejełeś kontrolę nad moim ciałem i próbowałeś zabić Lilith)"
        luszcz "(Lecz Ci na to nie pozwoliłem przez co Lilith mnie zabiła!)"

        n "{i}Nie pamiętam, by wydarzyło się coś takiego!{/i}"

        lilith "Ohhh, wróciłeś do mnie..."
        lilith "NIESTETY NADAL Z TYM OCHYDNYM ROBAKIEM!"

        n "{i}Chwila ONA też twierdzi, że to o czym mówiliście już się wydarzyło...!?{/i}"
        n "{i}Hmmmm, może to jednak jest prawda...{/i}"

        lilith "To jak skarbeńku? Pozbędziemy się tego robaka?"

        n "{i}Łuszczu, nie możesz się na to zgodzić!{/i}"
        n "{i}Nie wiem co wydarzyło się w poprzedniej rzeczywistości, ale wybranie Lilith sprawi, że świat się skończy!{/i}"
        n "{i}Musisz ją zabić!{/i}"

        rizzler "(Zabić mą ukochaną Lilith!? Nie, nie zabić to trzeba Ciebie w akcie pełnego, miłosnego oddania naszej najdroższej Lilith!)"

        menu:
            "{b}Posłuchaj się Głosu Rizzlera{/b}":
                stop music
                luszcz "Dobrze niech będzie kochanie"
                luszcz "Musimy się pozbyć tego karalucha!"
                
                lilith "Yuppi..."

                rizzler "(O tak, to będzie wspaniałe!)"
                rizzler "(W końcu zostaniemy sam na sam z naszą ukochaną, bez tego podżegacza!)"

                n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                play music "audio/music/anakin.mp3"

                n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                luszcz "(Ja nie lękam się Lilith jak ty!)"

                n "{i}...{/i}"

                luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                n "{i}Twojej głowy!?{/i}"

                luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszym wartością!{/i}"

                luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                n "{i}Ja zrobię co muszę!{/i}"

                luszcz "(Możesz spróbować!)"

                luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                n "{i}Łuszczu! Lilith jest zła!{/i}"

                luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                n "{i}Zatem jesteś zgubiony!{/i}"

                luszcz "(To twój koniec mój mistrzu!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                n "{i}Nie doceniasz mojej mocy!{/i}"

                luszcz "(Nie próbuj!)"

                n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                with vpunch

                $ renpy.pause(0.3)
                play sound "audio/sfx/krzyk.mp3" 
                stop music

                rizzler "(Nareszcie! Zwycięstwo jest nasze!)"

                lilith "Skończyłeś już z nim!?"

                luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                lilith "No nareszcie!"

                scene bg black with fade

                "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                "{i}I żyli długo i szczęśliwie{/i}"
                "{i}na pewno, na pewno{/i}"
                "{i}pewnie, jasne{/i}"
                "{i}zobaczymy, czas pokaże{/i}"

                $ lilith_social_link = 2
                jump spanko_bed

            "{b}Posłuchaj się Narratora{/b}":
                stop music
                show pristine_blade

                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                hide pristine_blade

                play sound "audio/sfx/nuz1.mp3"
                queue sound "audio/sfx/nuz2.mp3"

                show bg lilith16

                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                lilith "Ohhh, a myślałam, że jednak jesteś inny..."
                lilith "Cóż, skoro tak to zanim umrę musisz jeszcze wiedzieć, że..."

                show bg lilith17
                play sound "audio/sfx/rzygi.mp3"
                lilith "Blehhh"

                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                rizzler "(CÓŻ TY UCZYNIŁ! TY, TY POTWORZE! ZABIŁEŚ MOJĄ UKOCHANĄ LILITH!)"
                rizzler "(JAK MOGŁEŚ TO UCZYNIĆ!?)"

                luszcz "(Spoko ziomuś nie pultaj się mamy jeszcze gotkę)"

                rizzler "(ZABIŁEŚ MOJĄ UKOCHA... GOTKĘ?)"

                luszcz "(No w aptece nieopodal pracuje tak spoczko gotka, która mnie zawsze upodla i traktuje jak zwykłego śmiecia!)"

                rizzler "(HMMMM, no dobra przekonałeś mnie, to kiedy do niej idziemy?)"

                luszcz "(Można jutro jeśli tak bardzo chcesz)"

                luszcz "(Ale najpierw musimy coś zrobić z tym ciałem...)"

                menu: 
                    "{b}Jeszcze jest ciepla…{/b}":
                        luszcz "Jeszcze jest ciepła..."
                        luszcz "Muszę ją wykorzystać!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

                    "{b}Muszę ją wykorzystać{/b}":
                        luszcz "Muszę ją wykorzystać"
                        luszcz "..."
                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ money += 3
                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

    label lilith3:
        hide screen global_eq_key
        hide screen clock
        window hide
        $ renpy.pause(1.5)
        scene bg lilith6 with fade
        show screen global_eq_key
        show screen clock
        play music "audio/music/lilith7.mp3"
        n "{i}Jesteś na łóżku w twoim pokoju. Na tobie jest Lilith.{/i}"
        n "{i}Jesteś tu, żeby ją zabić. Jeśli tego nie zrobisz, to będzie koniec świata.{/i}"

        luszcz "(No spoko szkoda, że to ONA mnie zabiła!)"

        stomatolog "(Literalnie Panie Narratorze, proszę nie obrażać naszego intelektu.)"
        stomatolog "(Naszym najważniejszym zadaniem jest uniknięcie śmierci.)"
        stomatolog "(Później będziemy mogli prowadzić dysputy na temat tego co zrobić z Panną Lilith.)"

        n "{i}hmmmm???{/i}"
        n "{i}Jak to zgineliście? To nie jest pierwszy raz?{/i}"

        luszcz "(No nie)"
        luszcz "(Za pierwszym razem źle wyczułem miejsce piguły i umarłem!)"

        stomatolog "(Dlatego pojawiłem się ja, razem z moją specjalistyczną wiedzą, aby poprowadzić nas do zwycięstwa!)"

        lilith "Skończyliście już Bajdużyć?"

        show bg lilith7

        lilith "Zaczynamy zabawę od nowa!"

        show bg lilith13

        n "{i}Nim zdążyłeś zareagować, Lilith włożyła Ci pigułkę do ust{/i}"

        luszcz "(Awww shit, muszę ją wypluć zanim ją połknę!)"
        luszcz "(Czuję ją gdzieś za moją lewą górną ósemką)"

        stomatolog "(Hmmmm lewa górna ósemka...)"
        stomatolog "(To jest innaczej dens incisivus medialis)"
        stomatolog "(Wypluj pigułkę zza dens incisivus medialis!)"

        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza dens molaris tertius{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "(Mówiłeś, że jest zza dens incisivus medialis!)"

                stomatolog "(Sorki, coś tam musiało mi się pomylić...)"
                stomatolog "(Wiesz ile rzeczy trzeba pamiętać na tych studiach medycznych!? Każdemu może się zdarzyć coś zapomnieć!)"

                lilith "Ahhh, czyli to tak się bawimy!?"
                lilith "To zobaczymy jak sobie poradzisz z kolejną pigułką!"

                show bg lilith18

                if leki == 1:
                    luszcz "(Mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

                    menu:
                        "{b}Czy wziąść leki na schizofrenię?{/b}"

                        "{b}Tak{/b}":
                            n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                            n "{i}NIE! Nie zgadzam się!{/i}"

                            luszcz "(Ej ej ej to ja to rządze nie ty!)"

                            stomatolog "(Dokładnie! To szefunio wydaje polecenia!)"

                            n "{i}No, ale ja chcesz podjąć tak głupią decyzje to jak mam się nie wtrącać!???{/i}"

                            luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                            n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                            luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                            play sound "audio/sfx/epsilon_weapon.mp3"
                            show pristine_blade zorder 50 at center

                            n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                            luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                            n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                            luszcz "(A nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                            n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                            n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                            luszcz "(Yhy da da, zdemaskowałeś się!)"
                            luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                            luszcz "(Biorę te leki i elo!)"

                            n "{i}Nie mogę Ci na to pozwolić!{/i}"
                            n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                            stomatolog "(Co ty robisz!? Ty, ty barbarzyńco!)"

                            menu:
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Ostrzeż Lilith{/b}":
                                    $ klil = 0
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1

                            if klil == 1:
                                stop music
                                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                                hide pristine_blade

                                play sound "audio/sfx/nuz1.mp3"
                                queue sound "audio/sfx/nuz2.mp3"

                                show bg lilith16

                                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                                lilith "Ohhh, czyli to tak... czyli tak zginę..."
                                lilith "Skoro tak to musisz wiedzieć, że..."

                                show bg lilith17
                                play sound "audio/sfx/rzygi.mp3"
                                lilith "Blehhh"

                                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                                luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                                luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                                menu: 
                                    "{b}Jeszcze jest ciepla…{/b}":
                                        luszcz "Jeszcze jest ciepła..."
                                        luszcz "Muszę ją wykorzystać!"

                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ lilith_social_link = 10
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                        jump spanko_bed

                                    "{b}Muszę ją wykorzystać{/b}":
                                        luszcz "Muszę ją wykorzystać"
                                        luszcz "..."
                                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ money += 3
                                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                        $ lilith_social_link = 10
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                        jump spanko_bed

                            else:
                                n "{i}Przestań.{/i}"

                                show bg lilith3

                                lilith "Ohhh, czyli to wszystko jest jego wina..."
                                lilith "Przykro mi... Postaram się to zrobić szybko."

                                show bg lilith15
                                hide pristine_blade
                                stop music

                                play sound "audio/sfx/nuz1.mp3"
                                queue sound "audio/sfx/nuz2.mp3"

                                n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                                lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                                play sound "audio/sfx/spadek.mp3"
                                scene bg black
                                voice "audio/voice/narrator1.mp3"

                                n "{i}Zapada ciemność i umierasz.{/i}"

                                jump lilith6
                        
                        "{b}Nie{/b}":
                            luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

                lilith "smaczneeego!"

                show bg lilith13

                n "{i}Lilith po raz kolejny włożyła Ci pigułkę do ust{/i}"
                n "{i}Tym razem jednak wyczułeś ją za swoim prawym górnym pierwszym rozgniataczem{/i}"

                stomatolog "(Oooo to wiem napewno!!!)"
                stomatolog "(To jest innaczej siekacz przyśrodkowy!)"

            "{b}Zza dens incisivus medialis{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza dens incisivus medialis nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5

            "{b}Zza dens caninus{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza dens caninus nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5

        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza siekacza przyśrodkowego{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza siekaczem przyśrodkowym nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5
            
            "{b}Zza przedtrzonowca pierwszego{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza przedtrzonowcem pierwszym nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5
            
            "{b}Zza pierwszego molara{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Znowu dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "Stomatolog!!!! Znów pierdolisz głupoty!"

                stomatolog "(No, ale no to jest prawie to samo!)"
                stomatolog "(Serio jakby one wyglądają identycznie!)"

                lilith "Grrrr, dobry w to jesteś!"
                lilith "Ale ja się tak szybko nie poddam!"

                show bg lilith19

                if leki == 1:
                    luszcz "(Nadal mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

                    menu:
                        "{b}Czy wziąść leki na schizofrenię?{/b}"

                        "{b}Tak{/b}":
                            n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                            n "{i}NIE! Nie zgadzam się!{/i}"

                            luszcz "(Ej ej ej to ja to rządze nie ty!)"

                            stomatolog "(Dokładnie! To szefunio wydaje polecenia!)"

                            n "{i}No, ale ja chcesz podjąć tak głupią decyzje to jak mam się nie wtrącać!???{/i}"

                            luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                            n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                            luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                            play sound "audio/sfx/epsilon_weapon.mp3"
                            show pristine_blade zorder 50 at center

                            n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                            luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                            n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                            luszcz "(A nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                            n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                            n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                            luszcz "(Yhy da da, zdemaskowałeś się!)"
                            luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                            luszcz "(Biorę te leki i elo!)"

                            n "{i}Nie mogę Ci na to pozwolić!{/i}"
                            n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                            stomatolog "(Co ty robisz!? Ty, ty barbarzyńco!)"

                            menu:
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Ostrzeż Lilith{/b}":
                                    $ klil = 0
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1
                                "{b}Zabij Lilith{/b}":
                                    $ klil = 1

                            if klil == 1:
                                stop music
                                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                                hide pristine_blade

                                play sound "audio/sfx/nuz1.mp3"
                                queue sound "audio/sfx/nuz2.mp3"

                                show bg lilith16

                                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                                lilith "Ohhh, czyli to tak... czyli tak zginę..."
                                lilith "Skoro tak to musisz wiedzieć, że..."

                                show bg lilith17
                                play sound "audio/sfx/rzygi.mp3"
                                lilith "Blehhh"

                                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                                luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                                luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                                menu: 
                                    "{b}Jeszcze jest ciepla…{/b}":
                                        luszcz "Jeszcze jest ciepła..."
                                        luszcz "Muszę ją wykorzystać!"

                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ lilith_social_link = 10
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                        jump spanko_bed

                                    "{b}Muszę ją wykorzystać{/b}":
                                        luszcz "Muszę ją wykorzystać"
                                        luszcz "..."
                                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                        scene bg black with fade

                                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                        window hide
                                        play music "audio/music/applause.mp3"
                                        call screen full_click_screen("images/good_end.png")
                                        stop music
                                        window show

                                        $ money += 3
                                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                        $ lilith_social_link = 10
                                        $ pills = 20
                                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                        jump spanko_bed

                            else:
                                n "{i}Przestań.{/i}"

                                show bg lilith3

                                lilith "Ohhh, czyli to wszystko jest jego wina..."
                                lilith "Przykro mi... Postaram się to zrobić szybko."

                                show bg lilith15
                                hide pristine_blade
                                stop music

                                play sound "audio/sfx/nuz1.mp3"
                                queue sound "audio/sfx/nuz2.mp3"

                                n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                                lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                                play sound "audio/sfx/spadek.mp3"
                                scene bg black
                                voice "audio/voice/narrator1.mp3"

                                n "{i}Zapada ciemność i umierasz.{/i}"

                                jump lilith6
                        
                        "{b}Nie{/b}":
                            luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

                lilith "adios żartownisiu!"

                show bg lilith13

                n "{i}Lilith po raz trzeci włożyła Ci pigułkę do ust{/i}"
                n "{i}Tym razem jednak wyczułeś ją za swoim lewym dolnym dens incisivus lateralis{/i}"

                stomatolog "(Drugi trzonowiec!!!)"
                stomatolog "(100%% bro trust me!!!)"
        
        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza drugiego trzonowca{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza drugim trzonowcem nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5
            
            "{b}Zza siekaczem bocznym{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Kolejny raz dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "(Panie Stomatolog, pan tu już nie pracuje!!!)"

                stomatolog "(Tak, tak rozumiem...)"
                stomatolog "(...)"
                stomatolog "(dowidzenia)"

                luszcz "(dowidzenia)"

                lilith "Nie! Nie! Nie! Ty musisz umrzeć!"

                n "{i}Lilith po raz kolejny sięgnęła do słoika, lecz tym razem utkneła jej w nim ręka!{/i}"

                show bg lilith14

                show deszcz zorder 15
                play music "audio/music/deszcz.mp3"

                n "{i}W dodatku z jakiegoś powodu zaczeło padać!?{/i}"

                luszcz "(Chwila co!??? WTF jaki kurcze deszcz?!?)"
                luszcz "(Przecież jesteśmy w środku pokoju!?)"

                n "{i}Nie wiem noo ja jedynie stwierdzam fakty!!!"

                luszcz "(Hmmm, dziwne)"
                luszcz "(anyway, muszę coś z tym zrobić!)"

                n "{i}Zauważasz leżący w końcie pokoju parasolkę{/i}"

                luszcz "(O, parasolka! To może mi pomóc!)"

                n "{i}NIE! Zostaw ją! Teraz musisz zabić Lilith póki masz okazję!{/i}"

                luszcz "(Emmmm, no nie mówię, że nie masz całej racji, ale od razu zabić?)"
                with hpunch 
                $ renpy.pause(0.3)
                with hpunch
                $ renpy.pause(0.3)
                luszcz "(Patrz jak ona się trzęsię z zimna i jest taka bezbronna! Nie mogę jej zabić!)"

                n "{i}Musisz ją zabić!{/i}"

                menu:
                    "{b}Posłuchaj się Narratora{/b}":
                        hide deszcz
                        stop music
                        n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                        hide pristine_blade

                        play sound "audio/sfx/nuz1.mp3"
                        queue sound "audio/sfx/nuz2.mp3"

                        show bg lilith16

                        n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                        lilith "Ohhh, czyli to tak... czyli tak zginę..."
                        lilith "Skoro tak to musisz wiedzieć, że..."

                        show bg lilith17
                        play sound "audio/sfx/rzygi.mp3"
                        lilith "Blehhh"

                        n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                        luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                        luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                        menu: 
                            "{b}Jeszcze jest ciepla…{/b}":
                                luszcz "Jeszcze jest ciepła..."
                                luszcz "Muszę ją wykorzystać!"

                                hide deszcz
                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                            "{b}Muszę ją wykorzystać{/b}":
                                luszcz "Muszę ją wykorzystać"
                                luszcz "..."
                                luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                hide deszcz
                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ money += 3
                                "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                    "{b}Użyj parasola{/b}":
                        $ renpy.music.set_volume(0.25, delay=0.3)
                        hide deszcz
                        n "{i}Otworzyłeś parasolkę i schroniłeś się pod nią razem z Lilith!{/i}"
                        n "{i}Co ty wyprawiasz!? Miałeś ją zabić!{/i}"

                        show bg lilith3

                        lilith "..? Czemu? Czemu to zrobiłeś?"
                        lilith "Nie rozumiem... Przecież chciałam Cię zabić!?"

                        luszcz "Bo, bo ja Ciebie kocham Lilith!"
                        luszcz "Czy zostaniesz moją dziewczyną?"

                        lilith "Ohhh... Oczywiście, że tak!"
                        lilith "Oto, oto mi chodziło od początku!"

                        n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                        play music "audio/music/anakin.mp3"

                        n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                        luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                        luszcz "(Ja nie lękam się Lilith jak ty!)"

                        n "{i}...{/i}"

                        luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                        n "{i}Twojej głowy!?{/i}"

                        luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                        n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszemu kierunkowskazu!{/i}"

                        luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                        n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                        n "{i}Ja zrobię co muszę!{/i}"

                        luszcz "(Możesz spróbować!)"

                        luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                        with hpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                        luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                        n "{i}Łuszczu! Lilith jest zła!{/i}"

                        luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                        n "{i}Zatem jesteś zgubiony!{/i}"

                        luszcz "(To twój koniec mój mistrzu!)"

                        with hpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        with hpunch

                        $ renpy.pause(0.3)

                        with vpunch

                        $ renpy.pause(0.3)

                        luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                        n "{i}Nie doceniasz mojej mocy!{/i}"

                        luszcz "(Nie próbuj!)"

                        n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                        with vpunch

                        $ renpy.pause(0.3)
                        play sound "audio/sfx/krzyk.mp3" 
                        stop music

                        luszcz "(Nareszcie! Zwycięstwo jest moje!)"

                        lilith "Skończyłeś już z nim!?"

                        luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                        lilith "No nareszcie!"

                        scene bg black with fade

                        "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                        "{i}I żyli długo i szczęśliwie{/i}"
                        "{i}na pewno, na pewno{/i}"
                        "{i}pewnie, jasne{/i}"
                        "{i}zobaczymy, czas pokaże{/i}"

                        $ lilith_social_link = 2
                        jump spanko_bed
            
            "{b}Zza głównym zębem żującym{/b}":
                stop music
                n "{i}...{/i}"
                n "{i}Niestety zza głównym zębem żującym nie było żadnej pigułki{/i}"

                play sound "audio/sfx/lyk.mp3"

                n "{i}Przez co połknąłeś pigułkę i wydałeś na siebie wyrok...{/i}"

                with vpunch
                luszcz "NIE!"
                luszcz "To nie może się tak skończyć!"

                n "{i}Lecz twoje błagania nic nie dały{/i}"

                play sound "audio/sfx/spadek.mp3"
                scene bg black
                voice "audio/voice/narrator1.mp3"

                n "{i}Zapada ciemność i umierasz.{/i}"

                jump lilith5

    label lilith6:
        hide screen global_eq_key
        hide screen clock
        window hide
        $ renpy.pause(1.5)
        scene bg lilith3 with fade
        show screen global_eq_key
        show screen clock
        play music "audio/music/lilith1.mp3"
        n "{i}Jesteś na łóżku w twoim pokoju. Na tobie jest Lilith.{/i}"
        n "{i}Jesteś tu, żeby ją zabić. Jeśli tego nie zrobisz, to będzie koniec świata.{/i}"

        luszcz "(Aaaghhh, co ty nie powiesz!? Ostatnio i ostatnio też tak mówiłeś i co? I co?)"
        luszcz "(Umarłem przez ciebie!!!)"

        rizzler "(Dokładnie, ty ty barbarzyńco! Chciałeś zabić moją ukochaną Lilith!)"

        stomatolog "(Tak było nie zmyślają.)"

        n "{i}Okej po pierwsze to nie jest żadna \"twoja ukochana\"{/i}"
        n "{i}A po drugie nie przypominam sobię, żeby coś takiego się wydarzyło!{/i}"

        luszcz "(Na początku, źle wyczułem miejsce piguły i umarłem!)"
        luszcz "(A później kiedy miałem wziąść leki na schizofrenię przejełeś kontrolę nad moim ciałem i próbowałeś zabić Lilith)"
        luszcz "(Lecz Ci na to nie pozwoliłem przez co Lilith mnie zabiła!)"

        n "{i}Nie pamiętam, by wydarzyło się coś takiego!{/i}"

        lilith "Ohhh, wróciłeś do mnie..."
        lilith "NIESTETY NADAL Z TYM OCHYDNYM ROBAKIEM!"

        n "{i}Chwila ONA też twierdzi, że to o czym mówiliście już się wydarzyło...!?{/i}"
        n "{i}Hmmmm, może to jednak jest prawda...{/i}"

        lilith "To jak skarbeńku? Pozbędziemy się tego robaka?"

        n "{i}Łuszczu, nie możesz się na to zgodzić!{/i}"
        n "{i}Nie wiem co wydarzyło się w poprzedniej rzeczywistości, ale wybranie Lilith sprawi, że świat się skończy!{/i}"
        n "{i}Musisz ją zabić!{/i}"

        rizzler "(Zabić mą ukochaną Lilith!? Nie, nie zabić to trzeba Ciebie w akcie pełnego, miłosnego oddania naszej najdroższej Lilith!)"

        stomatolog "(Mi jest troche obojętnie, więc poprę każdą twoją decyzje szefuńciu!)"

        menu:
            "{b}Posłuchaj się Głosu Rizzlera{/b}":
                stop music
                luszcz "Dobrze niech będzie kochanie"
                luszcz "Musimy się pozbyć tego karalucha!"
                
                lilith "Yuppi..."

                rizzler "(O tak, to będzie wspaniałe!)"
                rizzler "(W końcu zostaniemy sam na sam z naszą ukochaną, bez tego podżegacza!)"

                n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                play music "audio/music/anakin.mp3"

                n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                luszcz "(Ja nie lękam się Lilith jak ty!)"

                n "{i}...{/i}"

                luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                n "{i}Twojej głowy!?{/i}"

                luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszym wartością!{/i}"

                luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                n "{i}Ja zrobię co muszę!{/i}"

                luszcz "(Możesz spróbować!)"

                luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                n "{i}Łuszczu! Lilith jest zła!{/i}"

                luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                n "{i}Zatem jesteś zgubiony!{/i}"

                luszcz "(To twój koniec mój mistrzu!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                n "{i}Nie doceniasz mojej mocy!{/i}"

                luszcz "(Nie próbuj!)"

                n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                with vpunch

                $ renpy.pause(0.3)
                play sound "audio/sfx/krzyk.mp3" 
                stop music

                rizzler "(Nareszcie! Zwycięstwo jest nasze!)"

                lilith "Skończyłeś już z nim!?"

                luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                lilith "No nareszcie!"

                scene bg black with fade

                "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                "{i}I żyli długo i szczęśliwie{/i}"
                "{i}na pewno, na pewno{/i}"
                "{i}pewnie, jasne{/i}"
                "{i}zobaczymy, czas pokaże{/i}"

                $ lilith_social_link = 2
                jump spanko_bed

            "{b}Posłuchaj się Narratora{/b}":
                stop music
                show pristine_blade

                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                hide pristine_blade

                play sound "audio/sfx/nuz1.mp3"
                queue sound "audio/sfx/nuz2.mp3"

                show bg lilith16

                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                lilith "Ohhh, a myślałam, że jednak jesteś inny..."
                lilith "Cóż, skoro tak to zanim umrę musisz jeszcze wiedzieć, że..."

                show bg lilith17
                play sound "audio/sfx/rzygi.mp3"
                lilith "Blehhh"

                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                rizzler "(CÓŻ TY UCZYNIŁ! TY, TY POTWORZE! ZABIŁEŚ MOJĄ UKOCHANĄ LILITH!)"
                rizzler "(JAK MOGŁEŚ TO UCZYNIĆ!?)"

                luszcz "(Spoko ziomuś nie pultaj się mamy jeszcze gotkę)"

                rizzler "(ZABIŁEŚ MOJĄ UKOCHA... GOTKĘ?)"

                luszcz "(No w aptece nieopodal pracuje tak spoczko gotka, która mnie zawsze upodla i traktuje jak zwykłego śmiecia!)"

                rizzler "(HMMMM, no dobra przekonałeś mnie, to kiedy do niej idziemy?)"

                luszcz "(Można jutro jeśli tak bardzo chcesz)"

                luszcz "(Ale najpierw musimy coś zrobić z tym ciałem...)"

                menu: 
                    "{b}Jeszcze jest ciepla…{/b}":
                        luszcz "Jeszcze jest ciepła..."
                        luszcz "Muszę ją wykorzystać!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

                    "{b}Muszę ją wykorzystać{/b}":
                        luszcz "Muszę ją wykorzystać"
                        luszcz "..."
                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ money += 3
                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

    label lilith5:
        hide screen global_eq_key
        hide screen clock
        window hide
        $ renpy.pause(1.5)
        scene bg lilith6 with fade
        show screen global_eq_key
        show screen clock
        play music "audio/music/lilith7.mp3"
        n "{i}Jesteś na łóżku w twoim pokoju. Na tobie jest Lilith.{/i}"
        n "{i}Jesteś tu, żeby ją zabić. Jeśli tego nie zrobisz, to będzie koniec świata.{/i}"

        luszcz "(No spoko szkoda, że to ONA mnie zabiła! DWA RAZY!!!)"

        stomatolog "(Literalnie Panie Narratorze, proszę nie obrażać naszego intele...)"

        dentysta "(Sklej pizdę ty pseudo-doktorku!)"
        dentysta "(To przez ciebie kurwa zgineliśmy!)"

        stomatolog "(Ale, ale ja nie chcioł, ja nie wiedzioł.)"

        luszcz "(Dobra, dobra koniec kłótni)"
        luszcz "(Tym razem musi nam się udać!)"

        n "{i}hmmm Początkowo chciałem zakwestionować waszą historię, ale chyba jednak nie kłamiecie...{/i}"

        luszcz "(No nie)"
        luszcz "(Za pierwszym razem źle wyczułem miejsce piguły i umarłem!)"

        stomatolog "(Dlatego pojawiłem się ja, razem z moją specjalistyczną wiedzą, aby poprowadzić nas do zwycięstwa!)"
        dentysta "(Której kurwa nie masz, bo jesteś zwykłym naciągaczem!)"

        luszcz "(A za drugim razem z powodu porad Stomatologa, znów źle wyczułem miejsce piguły i znów umarłem!)"

        lilith "Skończyliście już Bajdużyć?"

        show bg lilith7

        lilith "Zaczynamy zabawę od nowa!"

        show bg lilith13

        n "{i}Nim zdążyłeś zareagować, Lilith włożyła Ci pigułkę do ust{/i}"

        luszcz "(Awww shit, muszę ją wypluć zanim ją połknę!)"
        luszcz "(Czuję ją gdzieś za moim lewym górnym małym trzonowcem!)"

        stomatolog "(Hmmmm lewy górny mały trzonowiec...)"
        stomatolog "(To jest innaczej drugi trzonowiec cnie?)"

        dentysta "(Co ty pierdolisz!???)"
        dentysta "(Lewy górny mały trzonowiec to jest przedtrzonowiec pierwszy!)"

        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza przedtrzonowca pierwszego{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "(Miałeś rację Panie Lekarzu Dentysto!!!)"

                dentysta "(No a jak nie jak tak!)"
                dentysta "(67 lat studiów nie poszło na marne!)"

                stomatolog "(...)"

                
            "{b}Zza drugiego trzonowca{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"

            "{b}Zza pierwszego molara{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"
        
        lilith "Ahhh, czyli to tak się bawimy!?"
        lilith "To zobaczymy jak sobie poradzisz z kolejną pigułką!"

        show bg lilith18

        if leki == 1:
            luszcz "(Mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

            menu:
                "{b}Czy wziąść leki na schizofrenię?{/b}"

                "{b}Tak{/b}":
                    n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                    n "{i}NIE! Nie zgadzam się!{/i}"

                    luszcz "(Ej ej ej to ja to rządze nie ty!)"

                    stomatolog "(Dokładnie! To szefunio wydaje polecenia!)"
                    dentysta "(Daj kurwa młodziakowi wybierać, a nie się wpierdalsz w nie swoje sprawy!)"

                    n "{i}No, ale ja chcesz podjąć tak głupią decyzje to jak mam się nie wtrącać!???{/i}"

                    luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                    n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                    luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                    play sound "audio/sfx/epsilon_weapon.mp3"
                    show pristine_blade zorder 50 at center

                    n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                    luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                    n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                    luszcz "(A nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                    n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                    n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                    luszcz "(Yhy da da, zdemaskowałeś się!)"
                    luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                    luszcz "(Biorę te leki i elo!)"

                    n "{i}Nie mogę Ci na to pozwolić!{/i}"
                    n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                    stomatolog "(Co ty robisz!? Ty, ty barbarzyńco!)"
                    dentysta "(Narrator kurwa, zajębę Cię jak nie przestaniesz!)"

                    menu:
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Ostrzeż Lilith{/b}":
                            $ klil = 0
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1

                    if klil == 1:
                        stop music
                        n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                        hide pristine_blade

                        play sound "audio/sfx/nuz1.mp3"
                        queue sound "audio/sfx/nuz2.mp3"

                        show bg lilith16

                        n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                        lilith "Ohhh, czyli to tak... czyli tak zginę..."
                        lilith "Skoro tak to musisz wiedzieć, że..."

                        show bg lilith17
                        play sound "audio/sfx/rzygi.mp3"
                        lilith "Blehhh"

                        n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                        luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                        luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                        menu: 
                            "{b}Jeszcze jest ciepla…{/b}":
                                luszcz "Jeszcze jest ciepła..."
                                luszcz "Muszę ją wykorzystać!"

                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                            "{b}Muszę ją wykorzystać{/b}":
                                luszcz "Muszę ją wykorzystać"
                                luszcz "..."
                                luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ money += 3
                                "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                    else:
                        n "{i}Przestań.{/i}"

                        show bg lilith3

                        lilith "Ohhh, czyli to wszystko jest jego wina..."
                        lilith "Przykro mi... Postaram się to zrobić szybko."

                        show bg lilith15
                        hide pristine_blade
                        stop music

                        play sound "audio/sfx/nuz1.mp3"
                        queue sound "audio/sfx/nuz2.mp3"

                        n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                        lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith7
                
                "{b}Nie{/b}":
                    luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

        lilith "smaczneeego!"

        show bg lilith13

        n "{i}Lilith po raz kolejny włożyła Ci pigułkę do ust{/i}"
        n "{i}Tym razem jednak wyczułeś ją za swoim prawym górnym dens molaris tertius{/i}"

        stomatolog "(Oooo to wiem napewno!!!)"
        stomatolog "(To jest innaczej ząb kłowy!)"

        dentysta "(Stomatolog skończ pierdolić!)"
        dentysta "(Ząb mądrości 100%%)"

        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza zęba kłowego{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"

            "{b}Zza zęba mądrości{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Znowu dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "Joooo Dentysta!!! Ty to jednak jesteś mega!"

                dentysta "(HA, HA, HA! Raczej nie inaczej!)"
            
            "{b}Zza przedtrzonowca pierwszego{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"
        
        lilith "Grrrr, dobry w to jesteś!"
        lilith "Ale ja się tak szybko nie poddam!"

        show bg lilith19

        if leki == 1:
            luszcz "(Nadal mam leki na schizofrenię, które mogłyby mi teraz pomóc)"

            menu:
                "{b}Czy wziąść leki na schizofrenię?{/b}"

                "{b}Tak{/b}":
                    n "{i}Szybko sięgnąłeś po leki, otworzyłeś je i połk...{/i}"
                    n "{i}NIE! Nie zgadzam się!{/i}"

                    luszcz "(Ej ej ej to ja to rządze nie ty!)"

                    stomatolog "(Dokładnie! To szefunio wydaje polecenia!)"
                    dentysta "(Daj kurwa młodziakowi wybierać, a nie się wpierdalsz w nie swoje sprawy!)"

                    n "{i}No, ale ja chcesz podjąć tak głupią decyzje to jak mam się nie wtrącać!???{/i}"

                    luszcz "(Ej ej ej, czemó on jest niby głupi!? Przecież wystarczy, że wezmę te leki i będzie po sprawię!)"

                    n "{i}Nie to nie zadziała! Muisz ją zabić tym nieskazitelnym ostrzem który masz w kieszeni!{/i}"

                    luszcz "(Ej chwila przecież ja nie mam żadnego ostrza w kieszeni!?)"

                    play sound "audio/sfx/epsilon_weapon.mp3"
                    show pristine_blade zorder 50 at center

                    n "{i}Sięgnąłeś do kieszeni i wyciągnąłeś ostrze{/i}"

                    luszcz "(Ej wtf!? Przecież ja go tam nie wkładałem!?)"

                    n "{i}Musisz zabić ją swoim ostrzem, bo inaczej nastąpi koniec świata!{/i}"

                    luszcz "(A nie mogę po prostu wziąść tych pieprzonych leków i mieć z nią spokój!?)"

                    n "{i}Nie, nie możesz tego zrobić, bo ja też zniknę!{/i}"
                    n "{i}Emmmm, znaczy to nie zadziała, bo Lilith jest za potężna{/i}"

                    luszcz "(Yhy da da, zdemaskowałeś się!)"
                    luszcz "(Wcale nie chodzi Ci o moje dobro tylko twoje!)"
                    luszcz "(Biorę te leki i elo!)"

                    n "{i}Nie mogę Ci na to pozwolić!{/i}"
                    n "{i}Poczułeś jak tracisz kontrolę nad swoim ciałem, a twoja ręka unosi się do zadania cięcia{/i}"

                    stomatolog "(Co ty robisz!? Ty, ty barbarzyńco!)"
                    dentysta "(Narrator kurwa, zajębę Cię jak nie przestaniesz!)"

                    menu:
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Ostrzeż Lilith{/b}":
                            $ klil = 0
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1
                        "{b}Zabij Lilith{/b}":
                            $ klil = 1

                    if klil == 1:
                        stop music
                        n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                        hide pristine_blade

                        play sound "audio/sfx/nuz1.mp3"
                        queue sound "audio/sfx/nuz2.mp3"

                        show bg lilith16

                        n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                        lilith "Ohhh, czyli to tak... czyli tak zginę..."
                        lilith "Skoro tak to musisz wiedzieć, że..."

                        show bg lilith17
                        play sound "audio/sfx/rzygi.mp3"
                        lilith "Blehhh"

                        n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                        luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                        luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                        menu: 
                            "{b}Jeszcze jest ciepla…{/b}":
                                luszcz "Jeszcze jest ciepła..."
                                luszcz "Muszę ją wykorzystać!"

                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                                n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                            "{b}Muszę ją wykorzystać{/b}":
                                luszcz "Muszę ją wykorzystać"
                                luszcz "..."
                                luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                                scene bg black with fade

                                n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                                n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                                n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                                n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                                window hide
                                play music "audio/music/applause.mp3"
                                call screen full_click_screen("images/good_end.png")
                                stop music
                                window show

                                $ money += 3
                                "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                                $ lilith_social_link = 10
                                $ pills = 20
                                "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                                jump spanko_bed

                    else:
                        n "{i}Przestań.{/i}"

                        show bg lilith3

                        lilith "Ohhh, czyli to wszystko jest jego wina..."
                        lilith "Przykro mi... Postaram się to zrobić szybko."

                        show bg lilith15
                        hide pristine_blade
                        stop music

                        play sound "audio/sfx/nuz1.mp3"
                        queue sound "audio/sfx/nuz2.mp3"

                        n "{i}Lilith wyciąga ostrze z twojej ręki i wbija je w twoje serce{/i}"

                        lilith "Wybacz mi, zobaczymy się w przyszłym świecie."

                        play sound "audio/sfx/spadek.mp3"
                        scene bg black
                        voice "audio/voice/narrator1.mp3"

                        n "{i}Zapada ciemność i umierasz.{/i}"

                        jump lilith7
                
                "{b}Nie{/b}":
                    luszcz "(Nie, nie mogę ich wziąść, bo przecierz nie jestem chory czy coź!)"

        lilith "adios żartownisiu!"

        show bg lilith13

        n "{i}Lilith po raz trzeci włożyła Ci pigułkę do ust{/i}"
        n "{i}Tym razem jednak wyczułeś ją za swoim lewym dolnym siekaczem bocznym{/i}"

        stomatolog "(...)"
        dentysta "(Dens incisivus lateralis!)"
        
        menu:
            "{b}Skąd wypluć pigułkę?{/b}"

            "{b}Zza dens molaris secundus{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"
            
            "{b}Zza dens incisivus lateralis{/b}":
                play sound "audio/sfx/plucie.mp3"

                n "{i}Kolejny raz dobrze wyczułeś pigułkę i udało Ci się ją wypluć{/i}"

                luszcz "(LETS GO!!! UDAłO NAM SIĘ!!!)"

                dentysta "(I TO JEST KURWA INSTYNKT PRZETRWANIA!!!)"

                stomatolog "(...)"
            
            "{b}Zza dens premolaris secundus{/b}":
                dentysta "(NIE! Nie zgadzam się przyglądać naszej śmierci, gdy znam odpowiedź!)"
                play sound "audio/sfx/plucie.mp3"
                n "{i}Dentysta przejął kontrolę nad ciałem i wypluł pigułkę zza przedtrzonowca pierwszego{/i}"
        
        lilith "Nie! Nie! Nie! Ty musisz umrzeć!"

        n "{i}Lilith po raz kolejny sięgnęła do słoika, lecz tym razem utkneła jej w nim ręka!{/i}"

        show bg lilith14

        show deszcz zorder 15
        play music "audio/music/deszcz.mp3"

        n "{i}W dodatku z jakiegoś powodu zaczeło padać!?{/i}"

        luszcz "(Chwila co!??? WTF jaki kurcze deszcz?!?)"
        luszcz "(Przecież jesteśmy w środku pokoju!?)"

        dentysta "(Narrator, co tu się odpierdala!??)"

        n "{i}Nie wiem noo ja jedynie stwierdzam fakty!!!"

        luszcz "(Hmmm, dziwne)"
        luszcz "(anyway, muszę coś z tym zrobić!)"

        n "{i}Zauważasz leżący w końcie pokoju parasolkę{/i}"

        luszcz "(O, parasolka! To może mi pomóc!)"

        n "{i}NIE! Zostaw ją! Teraz musisz zabić Lilith póki masz okazję!{/i}"

        luszcz "(Emmmm, no nie mówię, że nie masz całej racji, ale od razu zabić?)"
        with hpunch 
        $ renpy.pause(0.3)
        with hpunch
        $ renpy.pause(0.3)
        luszcz "(Patrz jak ona się trzęsię z zimna i jest taka bezbronna! Nie mogę jej zabić!)"

        n "{i}Musisz ją zabić!{/i}"

        dentysta "Rób dzieciak co chcesz, nie musisz się słuchać tego kutasa!"

        menu:
            "{b}Posłuchaj się Narratora{/b}":
                hide deszcz
                stop music
                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                hide pristine_blade

                play sound "audio/sfx/nuz1.mp3"
                queue sound "audio/sfx/nuz2.mp3"

                show bg lilith16

                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                lilith "Ohhh, czyli to tak... czyli tak zginę..."
                lilith "Skoro tak to musisz wiedzieć, że..."

                show bg lilith17
                play sound "audio/sfx/rzygi.mp3"
                lilith "Blehhh"

                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                luszcz "(No nic nadal uważam, że gotka z apteki lepsza)"
                luszcz "(Tylko teraz muszę coś zrobić z tym ciałem...)"

                menu: 
                    "{b}Jeszcze jest ciepla…{/b}":
                        luszcz "Jeszcze jest ciepła..."
                        luszcz "Muszę ją wykorzystać!"

                        hide deszcz
                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

                    "{b}Muszę ją wykorzystać{/b}":
                        luszcz "Muszę ją wykorzystać"
                        luszcz "..."
                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                        hide deszcz
                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ money += 3
                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

            "{b}Użyj parasola{/b}":
                $ renpy.music.set_volume(0.25, delay=0.3)
                hide deszcz
                n "{i}Otworzyłeś parasolkę i schroniłeś się pod nią razem z Lilith!{/i}"
                n "{i}Co ty wyprawiasz!? Miałeś ją zabić!{/i}"

                show bg lilith3

                lilith "..? Czemu? Czemu to zrobiłeś?"
                lilith "Nie rozumiem... Przecież chciałam Cię zabić!?"

                luszcz "Bo, bo ja Ciebie kocham Lilith!"
                luszcz "Czy zostaniesz moją dziewczyną?"

                lilith "Ohhh... Oczywiście, że tak!"
                lilith "Oto, oto mi chodziło od początku!"

                n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                play music "audio/music/anakin.mp3"

                n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                luszcz "(Ja nie lękam się Lilith jak ty!)"

                n "{i}...{/i}"

                luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                n "{i}Twojej głowy!?{/i}"

                luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszemu kierunkowskazu!{/i}"

                luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                n "{i}Ja zrobię co muszę!{/i}"

                luszcz "(Możesz spróbować!)"

                luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                n "{i}Łuszczu! Lilith jest zła!{/i}"

                luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                n "{i}Zatem jesteś zgubiony!{/i}"

                luszcz "(To twój koniec mój mistrzu!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                n "{i}Nie doceniasz mojej mocy!{/i}"

                luszcz "(Nie próbuj!)"

                n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                with vpunch

                $ renpy.pause(0.3)
                play sound "audio/sfx/krzyk.mp3" 
                stop music

                luszcz "(Nareszcie! Zwycięstwo jest moje!)"

                lilith "Skończyłeś już z nim!?"

                luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                lilith "No nareszcie!"

                scene bg black with fade

                "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                "{i}I żyli długo i szczęśliwie{/i}"
                "{i}na pewno, na pewno{/i}"
                "{i}pewnie, jasne{/i}"
                "{i}zobaczymy, czas pokaże{/i}"

                $ lilith_social_link = 2
                jump spanko_bed

    label lilith7:
        hide screen global_eq_key
        hide screen clock
        window hide
        $ renpy.pause(1.5)
        scene bg lilith3 with fade
        show screen global_eq_key
        show screen clock
        play music "audio/music/lilith1.mp3"
        n "{i}Jesteś na łóżku w twoim pokoju. Na tobie jest Lilith.{/i}"
        n "{i}Jesteś tu, żeby ją zabić. Jeśli tego nie zrobisz, to będzie koniec świata.{/i}"

        luszcz "(Aaaghhh, co ty nie powiesz!? Ostatnio i ostatnio i ostatnio też tak mówiłeś i co? I co?)"
        luszcz "(Umarłem przez ciebie!!!)"

        rizzler "(Dokładnie, ty ty barbarzyńco! Chciałeś zabić moją ukochaną Lilith!)"

        dentysta "(Ty sukinsynie!!! Tym razem się nie wywiniesz!)"

        stomatolog "(Tak było nie zmyślają.)"

        n "{i}Okej po pierwsze to nie jest żadna \"twoja ukochana\"{/i}"
        n "{i}A po drugie nie przypominam sobię, żeby coś takiego się wydarzyło!{/i}"

        luszcz "(Na początku, źle wyczułem miejsce piguły i umarłem!)"
        luszcz "(A później kiedy miałem wziąść leki na schizofrenię przejełeś kontrolę nad moim ciałem i próbowałeś zabić Lilith)"
        luszcz "(Lecz Ci na to nie pozwoliłem przez co Lilith mnie zabiła!)"

        n "{i}Nie pamiętam, by wydarzyło się coś takiego!{/i}"

        lilith "Ohhh, wróciłeś do mnie..."
        lilith "NIESTETY NADAL Z TYM OCHYDNYM ROBAKIEM!"

        n "{i}Chwila ONA też twierdzi, że to o czym mówiliście już się wydarzyło...!?{/i}"
        n "{i}Hmmmm, może to jednak jest prawda...{/i}"

        lilith "To jak skarbeńku? Pozbędziemy się tego robaka?"

        n "{i}Łuszczu, nie możesz się na to zgodzić!{/i}"
        n "{i}Nie wiem co wydarzyło się w poprzedniej rzeczywistości, ale wybranie Lilith sprawi, że świat się skończy!{/i}"
        n "{i}Musisz ją zabić!{/i}"

        rizzler "(Zabić mą ukochaną Lilith!? Nie, nie zabić to trzeba Ciebie w akcie pełnego, miłosnego oddania naszej najdroższej Lilith!)"

        dentysta "(Nie jestem pewien co do intencji Lilith, ale intencje tego pieprzonego karalucha są dla mnie jasne!!!)"

        stomatolog "(Mi jest troche obojętnie, więc poprę każdą twoją decyzje szefuńciu!)"

        menu:
            "{b}Posłuchaj się Głosu Rizzlera{/b}":
                stop music
                luszcz "Dobrze niech będzie kochanie"
                luszcz "Musimy się pozbyć tego karalucha!"
                
                lilith "Yuppi..."

                rizzler "(O tak, to będzie wspaniałe!)"
                rizzler "(W końcu zostaniemy sam na sam z naszą ukochaną, bez tego podżegacza!)"

                n "{i}NIE! NIE! NIE! Nie zgadzam się!{/i}"

                play music "audio/music/anakin.mp3"

                n "{i}Pozwoliłeś tej Lilith wypaczać umysł aż stałeś się tym co miałeś zniszczyć!{/i}"

                luszcz "(Nie pouczaj mnie Narratorze, widzę dobrze twoje kłamstwa!)"
                luszcz "(Ja nie lękam się Lilith jak ty!)"

                n "{i}...{/i}"

                luszcz "(Sprowadziłem pokój, sprawiedliwość, bezpieczeństwo i wolność do mojej głowy!)"

                n "{i}Twojej głowy!?{/i}"

                luszcz "(Nie zmuszaj mnie, bym Cię zabił!)"

                n "{i}Łuszczu jestem lojalny zdrowemu rozsądkowi! Naszym wartością!{/i}"

                luszcz "(Jeśli nie jesteś ze mną, jesteś moim wrogiem!)"

                n "{i}Tylko spermiarz przemawia w ten sposób!{/i}"
                n "{i}Ja zrobię co muszę!{/i}"

                luszcz "(Możesz spróbować!)"

                luszcz "(ARGHHHHHHHHHHHHHHHHHHH!!!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                n "{i}Zawiodłem Cię Łuszczu, zawiodłem Cię{/i}"

                luszcz "(Powinien był wiedzieć, że spiskujesz, by przejąć włądze nad moim ciałem!)"

                n "{i}Łuszczu! Lilith jest zła!{/i}"

                luszcz "(Z mojego punktu widzenia ty jesteś zły!)"

                n "{i}Zatem jesteś zgubiony!{/i}"

                luszcz "(To twój koniec mój mistrzu!)"

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with hpunch

                $ renpy.pause(0.3)

                with vpunch

                $ renpy.pause(0.3)

                luszcz "(To koniec Narratorze! Mam wyższą pozycję!)"

                n "{i}Nie doceniasz mojej mocy!{/i}"

                luszcz "(Nie próbuj!)"

                n "{i}AAAAGHHHHHHHHHHHHHHHHHHH!{/i}"

                with vpunch

                $ renpy.pause(0.3)
                play sound "audio/sfx/krzyk.mp3" 
                stop music

                rizzler "(Nareszcie! Zwycięstwo jest nasze!)"

                lilith "Skończyłeś już z nim!?"

                luszcz "Tak, już nikt nam nie przeszkodzi, teraz możemy być razem!"

                lilith "No nareszcie!"

                scene bg black with fade

                "{i}I od tego momentu Łuszcz i Lilith zostali oficjalną parą{/i}"
                "{i}I żyli długo i szczęśliwie{/i}"
                "{i}na pewno, na pewno{/i}"
                "{i}pewnie, jasne{/i}"
                "{i}zobaczymy, czas pokaże{/i}"

                $ lilith_social_link = 2
                jump spanko_bed

            "{b}Posłuchaj się Narratora{/b}":
                stop music
                show pristine_blade

                n "{i}Unosisz ostrze, aby wbić je w serce Lilith.{/i}"

                hide pristine_blade

                play sound "audio/sfx/nuz1.mp3"
                queue sound "audio/sfx/nuz2.mp3"

                show bg lilith16

                n "{i}I dokonujesz tego zanim Lilith rozumie co się dzieje.{/i}"

                lilith "Ohhh, a myślałam, że jednak jesteś inny..."
                lilith "Cóż, skoro tak to zanim umrę musisz jeszcze wiedzieć, że..."

                show bg lilith17
                play sound "audio/sfx/rzygi.mp3"
                lilith "Blehhh"

                n "{i}Lilith umarła nim zdążyła dokończyć.{/i}"

                rizzler "(CÓŻ TY UCZYNIŁ! TY, TY POTWORZE! ZABIŁEŚ MOJĄ UKOCHANĄ LILITH!)"
                rizzler "(JAK MOGŁEŚ TO UCZYNIĆ!?)"

                luszcz "(Spoko ziomuś nie pultaj się mamy jeszcze gotkę)"

                rizzler "(ZABIŁEŚ MOJĄ UKOCHA... GOTKĘ?)"

                luszcz "(No w aptece nieopodal pracuje tak spoczko gotka, która mnie zawsze upodla i traktuje jak zwykłego śmiecia!)"

                rizzler "(HMMMM, no dobra przekonałeś mnie, to kiedy do niej idziemy?)"

                luszcz "(Można jutro jeśli tak bardzo chcesz)"

                luszcz "(Ale najpierw musimy coś zrobić z tym ciałem...)"

                menu: 
                    "{b}Jeszcze jest ciepla…{/b}":
                        luszcz "Jeszcze jest ciepła..."
                        luszcz "Muszę ją wykorzystać!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Dokonałeś swojego haniebnego czynnu poczym schowałeś ciało do szafy{/i}"
                        n "{i}Od teraz służyło Ci jako seks zabawka po wsze czasy{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed

                    "{b}Muszę ją wykorzystać{/b}":
                        luszcz "Muszę ją wykorzystać"
                        luszcz "..."
                        luszcz "wiem sprzedam ja rzeźnikowi na mięso!"

                        scene bg black with fade

                        n "{i}I jak powiedziałeś tak zrobiłeś{/i}"
                        n "{i}Poszedłeś do lokalnego rzeźnika i zaproponowałeś sprzedaż ciała{/i}"
                        n "{i}Rzeżnik przez chwilę się opierał, ale ostatecznmie stwierdził, ze mięso to mięso i kupił{/i}"
                        n "{i}Po wszystkim wróciłeś do domu i poszedłeś spać{/i}"

                        window hide
                        play music "audio/music/applause.mp3"
                        call screen full_click_screen("images/good_end.png")
                        stop music
                        window show

                        $ money += 3
                        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

                        $ lilith_social_link = 10
                        $ pills = 20
                        "{i}*Słoik z Pigułkami został dodany do ekwipunku*{/i}"
                        jump spanko_bed
