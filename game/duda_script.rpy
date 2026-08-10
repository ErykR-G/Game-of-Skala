default duda_miecz = 0
default duda_timer = 1000

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

        duda "muszę napisać wzór na gaz bojowy jaki ma używać wojsko polskie"
        duda "miałem to w szkole w '85 ale już zapomniałem, a ty wygladasz na młodszego, więc może to wiesz"

        luszcz "co? nie ja cały czas ściągałem z chemii"
        luszcz "nie ma drogi, że coś będę wiedział"

        duda "ajjj no cóż, rozumiem ja też czasem ściągam"
        luszcz "no szkoła jest ciężka"
        duda "ja nie mówie o szkole"
        duda "ja sciągałem na podpisie na księdze kondolencyjnej królowej anglii"
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

        duda "ze niby pan Władek i Zdzichu?"
        duda "jak nie są pijani to graja w kasynie online z malty"
        duda "nie ma co na nich liczyć"

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

        $ spiknik = piknik
        $ scake = cake
        $ spills = pills
        $ swoda = woda
        $ sostry = ostry
        $ slagodny = lagodny
        $ sdrpepper = drpepper
        $ sjabole = jabole
        $ sroyal = royal
        $ swarzywo = warzywo
        $ sbanany = banany
        $ sskalka = skalka
        $ sgranat = granat
        $ sluszcz_piguly = luszcz_piguly
        $ seminem_piguly = eminem_piguly
        $ surban_piguly = urban_piguly
        $ szyd_piguly = zyd_piguly
        $ skazuma_piguly = kazuma_piguly
        $ sile_item = ile_item

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
                    if timer >= 10080:
                        duda "wiesz co? za pomoc jestem ci w stanie wręczyć drogocenny miecz, który miałem przekazać tutejszemu księdzu za to, aby nadal nas chwlił mówiąc, że to bóg tak mówi"

                        luszcz "Yuppi!"

                        duda "proszę oto on"

                        $ miecz_swietlny = 1

                        "{i}*Miecz Świetlny został dodany do ekwipunku*{/i}"

                        luszcz "jooo dziękuję bardzo panie Duda"
                        luszcz "ale wracając do księdza..."
                        luszcz "to czy pomogl by pan w walce z nim?"
                    else:
                        if timer >= 2880 and timer <= 4260 or timer >= 5760 and timer <= 7140 or timer >= 8640 and timer <= 10020:
                            $ duda_timer = 1
                        else:
                            $ duda_timer = 2

                        duda "wiesz co? za pomoc jestem ci w stanie wręczyć drogocenny miecz, który miałem przekazać tutejszemu księdzu za to, aby nadal nas chwlił mówiąc, że to bóg tak mówi"

                        luszcz "Yuppi!"

                        duda "a ale jakby co to go nie mam teraz przy sobie więc eeee kiedyś tam przyjdę i ci go dam"

                        luszcz "mhhhh no okej"
                        luszcz "ale wracając do księdza..."
                        luszcz "to czy pomogl by pan w walce z nim?"

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
                    $ duda_miecz = 0

                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump parking
    
    label duda_ceremonia:
        $ duda_miecz = 1
        show luszcz neutral at slightleft
        show duda neutral at slightright

        duda "O Łuszczu, dobrze że jesteś!"
        duda "Wszędzie Cię szukałem, ale nie mogłem znaleźć"

        luszcz "..?"

        duda "No wiesz, miałem Ci przekazać ten miecz pamiętasz?"

        luszcz "Aaaaa jezu tak dobra pamiętam pamiętam"

        duda "Dobra to możemy zaczynać"

        show luszcz neutral at left
        show duda neutral at center

        duda "dziękuje wszystkim za przybycie"
        duda "powstańmy wszyscy na baczność!"

        label duda2:
            menu:
                "{b}nie stawaj{/b}":
                    duda ".................................?"
                    duda ".......................?"
                    duda "................................................?"
                    duda "............................?"
                    duda "......................................?"
                    duda "..........................................................?"
                    duda "............................?"
                    duda "................................................?"
                    duda ".......................?"
                    duda "...........................................?"
                    duda "..................?"
                    duda "......................................?"
                    duda ".....................................................?"
                    duda "debil"
                    duda ".......................?"
                    duda ".................................?"
                    duda "............................?"
                    duda "....................................................................?"
                    duda ".................................?"
                    duda "......................?"
                    duda "............................?"
                    duda "..................?"
                    duda "no debil"
                    duda "..........................................................?"
                    duda "...........................................?"
                    duda "..................?"
                    duda "no dobra to jeszcze raz"
                    duda "na baczność!"
                    jump duda2
                
                "{b}stań{/b}":
                    show luszcz bacznosc
                    duda "zebraliśmy się tu wszyscy, tu gdzie rozgrywają się wydarzenia, które przejdą do historii"
                    duda "Przypomina mi to kiedy w 1980 roku miejsce mia....."

                    show luszcz neutral

                    luszcz "Duda skończ pierdolić!"
                    luszcz "ja tu przyszedłem po miecz a nie jakieś wspominki"

                    duda "ja nawet jeszcze nie zacząłem, chociaż dobra czas to cenna waluta"
                    duda "naczelny wodzu proszę zaczynać"

                    show rydz_ryzyk neutral at center
                    show duda neutral at right

                    rydz_ryzyk "Dobrze, awięc"
                    rydz_ryzyk "Macieju Łuszczu"
                    rydz_ryzyk "ten oto miecz"
                    rydz_ryzyk "wykuty na zamówienie samego Andrzeja Leppera"
                    rydz_ryzyk "popełniliśmy nim jego samobójstwo"
                    rydz_ryzyk "był naszą najlepszą bronią"
                    rydz_ryzyk "niechaj od tego okresu czasu dnia dzisiejszego służy on tobie tak jak służył nam"

                    $ miecz_swietlny = 1

                    "{i}*Miecz Świetlny został dodany do ekwipunku*{/i}"

                    luszcz "no nareszcie, gorsze czekanie niż na NFZecie"
                    luszcz "dobra dzięki czy coś, ja lęcę"
            
            hide luszcz
            hide rydz_ryzyk
            hide duda
            if rynek == 1:
                jump rynek2
            if sloneczna == 1:
                jump sloneczna2 
            if alejka == 1:
                jump alejka2 
            if parking == 1:
                jump parking2
            if wolbromska == 1:
                jump wolbromska2
            if bohaterow_wrzesnia == 1:
                jump bohaterow_wrzesnia2 
            if lipowa == 1:
                jump lipowa2 
            if granica == 1:
                jump granica2