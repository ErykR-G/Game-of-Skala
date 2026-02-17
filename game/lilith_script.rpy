label lilith:
    label lilith1:
        "{i}{/i}"
        "{i}Tej nocy pojawiła się Lilith{/i}"
        "{i}Leżę na łóżku, zagubiony w czasie-Nie wiem, jak długo próbowałem zasnąć i nawet nie pamiętam, kiedy ostatnio farmiłem na skyblocku{/i}"
        "{i}Jedyne co mi pozostało to umrzeć tutaj... i czekać aż moje ciało się rozłoży{/i}"
        "{i}i wtedy... ona pojawiła się obok mnie{/i}"

        scene bg gnoms with fade
        play music "audio/music/lilith1.mp3"
        scene bg lilith1 with fade

        lilith "..."

        luszcz "..?"

        lilith "..."

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
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

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
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

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
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

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
                lilith "..."
            "{b}Kim jesteś?{/b}":
                jump after_yapping

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
                if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
                    if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
            show lilith neutral1 at left

            luszcz "Kim ty do kurwy jesteś? I jak dostałaś się do mojego domu?"

            lilith "Naprawdę chcesz to wiedzieć? Przecież to jest tylko gra komputerowa…."

            # krzeslo Panie ona się Ciebie nie słucha

            # szafka Na pewno coś ukrywa! 

            menu:
                "{b}Jesteś prostytutką?{/b}":
                    luszcz "Jesteś prostytutką?"

                    lilith "Skoro tak o mnie myślisz to mogę być"
                    lilith "w sumie ej nawet o sobie nie myślałam w ten sposób, a to chyba najlepszy opis mojej pracy"
                    lilith "za pieniądze daję ci miłość"
                    lilith "Dobra w takim razie skoro jestem już ze sobą szczera to chce kasy, albo spadam stąd"

                    menu:
                        "{b}Masz dychę i ma wystarczyć na wszystko (1 💰){/b}" if money >= 1:
                            luszcz "Masz dychę i ma wystarczyć na wszystko"
                            
                            $ money -= 1

                            lilith "żałosne" 

                        "{b}Taaa? To spierdalaj{/b}":
                            luszcz "Taaa? To spierdalaj"

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

                    lilith "Nie do końca, ale mogą dla Ciebie zostać jeśli chcesz"

                    luszcz "Ohhhh prosze, prosze, proszeeeee"

                    lilith "Nie powinieneś się tak jawnie zdradzać ze swoim fantazjami seksualnymi przy kobietach!"
                    lilith "To może je zniechęcić do Ciebie"

                    menu:
                        "{b}Dobrze proszę Pani{/b}":
                            luszcz "Dobrze proszę Pani"
                            luszcz "a usiądzie mi Pani na mordzie?"

                            lilith "iiiii juj jesteś dziwny…"
                            lilith "na pewno mam to zrobić?"

                            luszcz "TAK"

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

                            lilith "dobrze dobrze będę twoją gotką"

                            luszcz "LETS GO!"

                                    
                "{b}Mamo?{/b}":
                    luszcz "Mamo?"

                    lilith "Czyli tak na mnie patrzysz…"
                    lilith "No cóż jeśli tego ode mnie oczekujesz"
                    lilith "W takim razie Macieju posprzątaj pokój w tej chwili! Co to za szmata w kącie pokoju! Masz 5 minut, a jak nie to dostaniesz szlaban na komputra!"

                    luszcz "przepraszam mamusiu już biorę się do sprzątania"
                                    
                "{b}Japierdole znów mam zwidy{/b}":
                    luszcz "Japierdole znów mam zwidy, mogłem nie wdychać tyle kadzidła podczas mszy…"

                    #krzesło Panie, nic panu nie jest … to normalne w tym wieku

                    #szafka dokładnie, dokładnie jest pan całkowicie normalny

                    luszcz "a okej"

                "{i}…{/i}"



