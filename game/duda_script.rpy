
label duda:
    label duda1:
        scene bg stomatolog2 with fade
        play music "audio/music/stomatolog.mp3"
        show luszcz neutral at left
        show duda neutral at slightright

        luszcz "wow pan prezydent"
        luszcz "dzień dobry"

        duda "dzień dobry"

        luszcz "co pan prezydent tu robi?"

        duda "mam horom curke"
        duda "potrzebuje pomocy"

        luszcz "co się stało?"

        duda "muszę napisać wzór na gaz bojowy jaki ma używać wosjko polskie"
        duda "miałem to w szkole w '85 ale już zapomniałem, a ty wygladasz na młodszego, więc może to wiesz"

        luszcz "co? nie ja cały czas ściągałem z chemii"
        luszcz "nie ma drogi, że coś będę wiedział"

        duda "ajjj no cóż, rozumiem ja też czasem ściągam"
        luszcz "no szkoła jest ciężka"
        duda "ja nie mówie o szkole"
        duda "ja sciągałem na podpisie na księdze konndolencyjnej królowej anglii"
        duda "pisałem jakies dys ys eee dys ys de wery..."
        duda "no nie pamiętam, dlatego miałem sciage"
        duda "niestety reporterzy zauważyli, ale no trudno wyszedłem z wprawy"
        duda "podpisywanie ustaw jest łatwiejsze"
        duda "słuchasz tylko pana szanownego prezesa i robisz co ci każe"

        luszcz "wow to chyba fajnie jest być prezydentem"

        duda "to nie ma tak, że fajnie albo nie fajnie"
        duda "gdybym miał powiedzieć co w życiu cenie najbardziej powiedziałbym, że łzy"
        duda "łzy lewaków, którzy spłakują się po każdej mojej decyzji"
        duda "chodzi tylko o to żeby nie oglądać tvnu, bo on cie tylko gnoi 24/7"
        duda "przynajmniej ta lepsza stacja robi ci cały czas laurki jak w korei północnej"

        luszcz "wooo ale pan jest odwazny"
        luszcz "chociaż dla lez lewaków to chyba warto?"

        duda "warto"
        duda "....." 
        duda "oj warto"
        duda "ale jest jeszcze jeden szczegół"
        duda "musisz być na bieżąco ze światem"
        duda "siedzę nad newsami i tylko"
        duda "ja się uczę w domu"
        duda "ja się uczę w samolocie"
        duda "ja się uczę w gabinecie stomatologicznym"
        duda "ja się cały czas czegoś ucze"

        luszcz "fajnie fajnie"
        luszcz "a pomoglby pan nam w walce z ksiedzem"

        duda "z checia bym pomogl ale aktualnie nie mogę się wychylać, ukrywam się przed moim wrogiem"

        luszcz "jak to? a ochrona prezydencka?"
        luszcz "co to za wróg"

        duda "ze niby pan wladek i Zdzichu?"
        duda "jak nie są pijani to graja w kasynie online z malty"
        duda "nie ma co na nich liczyc"

        nikt "koniec ukrywania herr Präsident"

        show duda neutral right at left
        show luszcz neutral at slightleft
        show cien neutral at slightright

        duda "to on"

        luszcz "woo kurwa"
        luszcz "czy to...?"

        duda "to ostry cień mgły"
        duda "jeden z najlepszych agentów abwehry"
        duda "obecnie na usługach tfuska"

        cien "czekałem na ten moment od bardzo, bardzo dawna, ale doczekałem się"
        cien "w imieniu Niemieckiej Republiki Polski skazuje cię na karę śmierci"

        show duda czolg at slightleft
        show cien neutral at right
        show luszcz neutral at left

        duda "nigdy nie zabijesz mnie żywcem!"

        cien "to dopiero się okaże"

        luszcz "o bogowie! walka!"

        show duda neutral at slightleft
        show cien neutral at slightright

        duda "drogi obywatelu, mógłbyś mi pomóc?"

        menu:
            "{b}nie mój problem{/b}":
                luszcz "to nie mój problem, mam ważniejsze żeczy do roboty"
                luszcz "adios żartownisiu"

                $ duda_social_link = 10
                $ duda_wybory = 0

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump parking

            "{b}no dobra{/b}":
                luszcz "toż to zamach stanu"
                luszcz "liberum veto!!!"

                cien "a więc zginiesz razem z nim"

        jump after_fight201
        jump fight201
        label after_fight201:
            scene bg stomatolog2
            play music "audio/music/stomatolog2.mp3"
            show luszcz neutral at left
            show duda neutral at slightright
            luszcz "no to nam się udało"

            duda "tylko na jakiś czas, chuj się odradza"
            duda "ale jestem wdzięczny za pomoc"

            luszcz "cieszę się ze mogłem pomóc"

            duda "jednakże mam jeszcze do ciebie jedno pytanie"
            duda "na kogo głosowałeś?"

            luszcz "ja nawet nie mogłem wtedy głosować"

            duda "no i co mnie to obchodzi"
            duda "na kogo głosowałeś się pytam"

            menu:
                "{b}na trzaska{/b}":
                    luszcz "trzask prask i serce oszalało"

                    duda "coo?!"
                    duda "czym prędzej znikaj krypto tęczuchu"
                    duda "myślałem, że mogę ci ufać"
                    duda "akysz akysz"

                    luszcz "a weź pal gume chłopie"
                    luszcz "do nie widzenia"

                    $ duda_social_link = 10
                    $ duda_wybory = 1

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump parking

                "{b}na dude{/b}":
                    luszcz "oczywiście, że kocham prezydenta dude i morawieckiego!"

                    duda "no i to się nazywa prawdziwy polak patriota"
                    duda "za pomoc jestem ci w stanie dać trochę itemków od ochrony"

                    #[dostajesz jakieś itemy]

                    luszcz "bardzo dziekuje ale miałem nadzieje na cos innego"
                    luszcz "czy pomogl by pan walczyc z ksiedzem"

                    duda "nie"
                    duda "walcze z ostatnim pokoleniem"

                    luszcz "oj rozumiem, ciężka sprawa"
                    luszcz "powiedziałbym, że są odklejeni, ale oni się w sumie przyklejają to nie mogę tak powiedzieć"

                    duda "mają problem do wungla"
                    duda "mówią że zanieczyszcza środowisko"
                    duda "ale to nie prawda"
                    duda "to na pewno niemiecka agentura"
                    duda "a poza tym ten wungiel był nam obiecany 3 tysiące lat temu"

                    luszcz "no szkoda, ale ktoś musi nas od nich uratować"
                    luszcz "w takim razie wybaczam" 

                    duda "nie mogę ci pomoc bardziej ale mogę dac ci rade "
                    duda "pamiętaj "
                    duda "MUSISZ"
                    duda "BYĆ"
                    duda "TWARDY"
                    duda "Jak masz być obrońcą skały, to Nie możesz sobie pozwolić na to, że cię coś rozbije, jakaś sytuacja, zwłaszcza taka, która cię dotyczy osobiście."
                    duda "No nie, tu są naprawdę poważne sprawy, tu nie ma żartów. Tu może przyjdzie dzień, że trzeba będzie podjąć takie decyzje, że człowiek sobie nie wyobraża, że musiałby takie decyzje podjąć. Dotyczące chociażby bezpieczeństwa skały"
                    
                    $ duda_social_link = 1
                    $ duda_wybory = 2

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump parking