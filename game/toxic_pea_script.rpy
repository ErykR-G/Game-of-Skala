default toxic_limit = 0
label toxic_pea:
    label toxic_pea1:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at left
        show toxic_pea neutral at slightright

        toxic "Oh, to ty."
        toxic "A jak masz wgl na imie?"

        luszcz "Maciej"

        toxic "Już mamy jednego takiego"
        toxic "To jak coś to będziemy na ciebie mówić Maciej_Rel, spoko?"

        luszcz "Dobrze.."
        luszcz2 "(czemó akurat tak…?)"

        toxic "Dobra, słuchaj, nie mamy czasu, zombiaki nadchodzą."
        toxic "Od dłuższego czasu zaczęły nocami wychodzić przez jakiś portal schowany niedaleko."
        toxic "Ogród Szalonego Dawida, znaczy naszego szefa jest jedyną rzeczą trzymającą je przed pełną inwazją na Skałę."
        toxic "Raczej sobie radzimy, ale zdarza się, że nas przeliczają, więc każda pomoc się przyda."
        toxic "Jak tu jesteś, to raczej umiesz się bić, cnie?"

        luszcz2 "Oh, i to jeszcze jak!"
        luszcz2 "Jeszcze nie dawno udało mi się pokonać…"

        toxic "Nie, nie ma teraz czasu na rozmowy."
        toxic "Broń w dłoń i do boju!"

        jump after_fight131
        jump fight131
        label after_fight131:
            play music "audio/music/toxic2.mp3"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            luszcz2 "Ufff…"

            toxic "Dobra robota, Maciej_Rel"
            toxic "Nie jesteś taki słaby jak mi się wydawało"

            luszcz2 "Hehe… dzięki.."

            toxic "Wiesz co, nie będę owijał w bawełne."
            toxic "Ruchasz czy trzeba z tobą chodzić?"
            show luszcz blush
            menu:
                "{b}rucham{/b}":
                    show luszcz sigma
                    luszcz2 "Od takiego kociaka nie odrzóciłbym propozycji 😼"

                    toxic "Ta? Zobaczymy kto będzie miauczeć w łóżku."
                
                "{b}chodzić{/b}":
                    luszcz2 "A co jeśli powiem, rze trzeba ze mną chodzić?"

                    toxic "To po dzisiejszej nocy dowiemy się czy się jeszcze zobaczymy."
            
            scene bg black with fade
            nikt "{i}Jeden netflix później{/i}"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            toxic "Dzięki, było całkiem nieźle."
            toxic "Twoje palce nie były idealne, ale można nad tym popracować."

            luszcz2 "Ohhhh Toxic, jedyne co mogę powiedzieć, to że było za mało radia"

            toxic "To jak, kolejna rundka następnej nocy?"
            toxic "Ale pamiętaj, na nagrodę trzeba zapracować. Walczysz z nami albo wypad."

            menu:
                "{b}PLANT ZEGZ 🤤{/b}":
                    show luszcz sigma

                    luszcz2 "Pewnie, widzimy się kochanie."

                    toxic "Nie no nie mów tak do mnie"

                    show luszcz neutral

                    luszcz2 "A jak do ciebie mówić?"

                    toxic "Tatusiu"

                    luszcz2 "Dobże tatusiu"

                    toxic "XD"
                    toxic "Dobra, cześć, widzimy się"

                    luszcz2 "Cześć..!"

                    scene bg black with fade

                    n "{i}Łuszczu nagle wzdrygnął, tak jakby jego ciało próbowało opanować się po tym czego dziś doznał.{/i}"

                    n "{i}Jedna noc spełniła tyle jego pragnień, odpowiedziała na tyle potrzeb.{/i}"

                    n "{i}Potrzeb, bez których spełnienia jego ciało więdło.{/i}"

                    n "{i}Nareszcie, w jego życiu miłosnym zasadziło się nasionko nadziei.{/i}"

                    n "{i}Albo, alternatywnie, nasienie.{/i}"
                
                "{b}NO THANKS{/b}":
                    luszcz2 "Coś we mnie stara się mnie zmusić do odmowy."

                    toxic "Nie wiem o czym nawijasz, ale w razie czego widzimy się jutro."
                    toxic "A jak nie przyjdziesz, to i tak dzięki za noc."
                    toxic "Nara!"

                    luszcz2 "Pa.."

                    scene bg black with fade

                    n "{i}Łuszczu nagle wzdrygnął, tak jakby jego ciało próbowało opanować się po tym czego dziś doznał.{/i}"

                    n "{i}Jedna noc spełniła tyle jego pragnień, odpowiedziała na tyle potrzeb.{/i}"

                    n "{i}Potrzeb, bez których spełnienia jego ciało więdło.{/i}"

                    n "{i}Jednakże, coś wewnątrz każe mu uciekać od szansy, którą dało mu życie.{/i}"

                    n "{i}Czy Łuszczu ulegnie, i pozwoli drugiej duszy trzymać nad nim konewkę?{/i}"

            $ toxic_pea_social_link = 2
            $ toxic_pea_wybory = 1
            $ toxic_limit = 1

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska

    label toxic_pea2:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at left
        show toxic_pea neutral at slightright

        luszcz2 "Hej!"

        toxic "Wreszcie się ukazałeś, Maciek_Rel!"
        toxic "Chodź, dziś są jacyś pojebani!"

        jump after_fight141
        jump fight141
        label after_fight141:
            play music "audio/music/toxic2.mp3"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            luszcz2 "Ah… to było.. Niebezpieczne"
            luszcz2 "Ale jakrze ekscytujące!"

            toxic "Co nie!"
            toxic "Tak w sumie na temat, zapomniałem ci powiedzieć."
            toxic "Staraj się połykać jak najmniej mojego śluzu dziś w nocy. Na zewnątrz nie szkodzi ludziom, ale od środka potrafi namieszać."

            luszcz2 "Dopiero teraz mi to mówisz..?"
            luszcz2 "Znaczy, spoko, ale przecież widziałeś wczoraj, jak połykałem całość…"

            toxic "XD, sory, trochę się wtedy wczułem"
            toxic "Ale wygląda na to że nic ci nie jest"
            toxic "To co, idziemy?"

            luszcz2 "Pewnie heh."

            scene bg black with fade

            nikt "{i}jeden netflix później…{/i}"

            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            toxic "Ej, w ogóle, ćwiczyłeś palce."
            toxic "Było czuć."

            luszcz2 "Zgadza się, specjalnie dla ciebie."

            toxic "Tak mówisz?"
            toxic "A czy pojawiłbyś się tu dla mnie następnej nocy?"

            luszcz2 "Hmm…"
            luszcz2 "Myślę że tak"
            luszcz2 "Jestem teraz ogółem na misji"
            luszcz2 "Słyszałeś że kościół chce włączyć Skałę do Krakowa?"

            toxic "Coś mi się usłyszało,"
            toxic "A to nie dobrze?"
            toxic "W sensie, Kraków raczej stać na uporanie się z tą plagą zombi"
            toxic "A obecny rząd chyba potrafi tylko organizować narady i bale."

            luszcz2 "Jak możesz…"
            luszcz2 "Znaczy się,"
            luszcz2 "A co z naszą autonomią? Naszą korupcję możemy jeszcze kontrolować, to co się dzieje w Krakowie to jakiś inny świat."
            luszcz2 "Zresztą, nigdy nikomu nie oddam skały, a zwłaszcza nie dla dorobku naszego księdza."

            toxic "Wiesz co, szczerze, jedyna polityka która mnie obchodzi to ta tutaj, na polu bitwy."
            toxic "Ale możesz mieć swoją opinię i w sumie nie zależy mi żeby ją zmieniać."
            toxic "Ruchamy sie jutro?"

            menu:
                "{b}Tak{/b}":
                    luszcz2 "Pewnie"

                    toxic "no i cacy, siema"

                    luszcz2 "cześć"
                    luszcz2 "cześć …"
                
                "{b}Nie{/b}":
                    luszcz2 "Moje ciało próbuje powiedzieć nie, ale postaram się być"

                    toxic "eee.. Okej, widzimy się."

                    luszcz2 "Żegnaj.."

            scene bg black with fade

            n "{i}Zmieszany, Łuszczu spojrzał w księżyc.{/i}"
            n "{i}Jego światło pozwalało mu widzieć coś poza nieskończoną pustką.{/i}"
            n "{i}Jego ciepło, pozornie znikome nocą, trzymało go przed marznięciem w nicości.{/i}"
            n "{i}Mimo, że ukazuje się tylko nocą, mimo, że nie zna go w pełni.{/i}"
            n "{i}Księżyc tej nocy wyglądał dla niego jak miłość.{/i}"
            n "{i}Łuszczu pozwolił sobie stać jeszcze 5 minut, aż doszedł do konkluzji że i on, i księżyc, mają swoje zadania do wykonania.{/i}"

            $ toxic_pea_social_link = 3
            $ toxic_pea_wybory = 1
            $ toxic_limit = 1

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska

    label toxic_pea3:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at left

        luszcz2 "Maciek_Rel, meldóję się!"

        show sunflower neutral:
            xalign 0.75
            yalign 1.0

        sunflower "Hm?"

        show grucha neutral:
            xalign 0.65
            yalign 1.0

        show sunflower neutral:
            xalign 0.85
            yalign 1.0

        grucha "Człowiek będzie z nam pomagał?"

        show chomper neutral:
            xalign 0.55
            yalign 1.0

        show grucha neutral:
            xalign 0.75
            yalign 1.0

        show sunflower neutral:
            xalign 0.95
            yalign 1.0
        

        chomper "Hau Hau!"

        show grzyb neutral:
            xalign 0.45
            yalign 1.0

        show chomper neutral:
            xalign 0.65
            yalign 1.0

        show grucha neutral:
            xalign 0.85
            yalign 1.0

        show sunflower:
            xalign 1.05
            yalign 1.0

        grzyb "Nie słyszeliście? To ten kolo który kręci z Toksycznym Grochem!"
        sunflower "Chwila, to z nim Toxic zajmuje sypialnie?"
        luszcz2 "…"
        grzyb "O, idzie, rozchodzimy się!"

        hide grzyb
        hide chomper
        hide grucha
        hide sunflower
        show toxic_pea neutral at slightright

        toxic "Serwus"
        toxic "Podoba mi się twoja dedykacja."
        toxic "To co, do roboty!"

        jump after_fight151
        jump fight151
        label after_fight151:
            play music "audio/music/toxic2.mp3"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            toxic "Dobra robota, kociaku"

            show luszcz neutral right
            show toxic_pea at center

            play sound "audio/sfx/klap.mp3"
            with hpunch

            $ renpy.pause(0.2)

            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright
            
            toxic "Gotów na swoją nagrodę?"

            luszcz2 "Haha, pewnie, heh.."

            toxic "Ale musisz przyznać, nie możemy ciągle robić tego samego"
            toxic "Trzeba podnieść poprzeczkę"

            luszcz2 "Jeśli tak óważasz…"

            toxic "Mam na dziś fajny pomysł który moglibyśmy wypróbować"
            toxic "Ile pianek mieści się w twojej buzi"

            luszcz2 "Nie wiem, 6, 7?"

            toxic "To po dzisiaj będziesz mieścił 67 minimum."

            scene bg black with fade

            nikt "{i}jeden netflix później…{/i}"

            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            luszcz2 "*wdech*"
            luszcz2 "*wydech*"
            luszcz2 "*wdech*"

            toxic "Jak tam, dalej wstrząśnięty?"
            toxic "oże, to było cudowne!"
            toxic "I gdy prawie zemdlałeś z tą pełną mordą? Musiałem cyknąć pare zdjęć."
            toxic "Zawsze chciałem tego spróbować, dzięki dziunia."
            toxic "Ten sam czas, to samo miejsce, żegnam!"

            hide toxic_pea 
            show luszcz neutral at center

            luszcz2 "…*wydech*..."
            luszcz2 "O mój boż…"

            show luszcz blush

            luszcz2 "!!!"

            scene bg black with fade

            luszcz2 "Błlech!"

            scene bg przed_walka_toxic_pea with fade
            show luszcz kula at center

            luszcz2 "….."

            show sunflower neutral:
                xalign 1.05
                yalign 1.0
            
            sunflower "..."

            hide sunflower

            $ renpy.pause(0.5)

            luszcz2 "…"

            scene bg black with fade
            n "{i}Łuszczu po raz kolejny spojrzał na księżyc, tym razem unosząc ku niemu kulę, którą dzierżył w dłoni.{/i}"
            n "{i}Robiąc to dostrzegł, jak obślizgła bryła reaguje na światło księżyca.{/i}"
            n "{i}Nagle ciepło i światło, które zawdzięczał księżycowi.{/i}"
            n "{i}Stało się w jego oczach fałszywe.{/i}"
            n "{i}Nagle księżyc zdawał się bawić ciepłem i światłem tak, aby zyskać jego spojrzenie, jego myśli, jego wdzięczność.{/i}"
            n "{i}Nagle, Łuszczu pomyślał, że nie chce już księżyca,{/i}"
            n "{i}I z myślą tą poczuł jak ciepło i światło, opuszczając jego ciało{/i}"
            n "{i}Pozostawiają tylko pustkę.{/i}"

            $ ile_item_fabularne += 1
            $ zielona_kula = 1

            "{i}*Zielona Kula została dodana do ekwipunku*{/i}" 

            $ toxic_pea_social_link = 4
            $ toxic_pea_wybory = 2
            $ toxic_limit = 1

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska

    label toxic_pea4:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz zmentzony at center

        luszcz2 "*wdech*"
        luszcz2 "…"
        luszcz2 "*wydech*"
        luszcz2 "Przyszedłem."

        toxic "O!"
        toxic "CZEKAJCIE, PRZYSZŁO WSPARCIE!"
        toxic "EJ DAWAJ TU SZYBKO, MAMY KURWA GIGANTY!"

        jump after_fight161
        jump fight161
        label after_fight161:
            play music "audio/music/toxic2.mp3"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            luszcz2 "Ah…. Całe szczęście…"

            toxic "Maciej_Rel, świetna robota z tym ulańcem!"
            toxic "Myślę…"
            toxic "Że należy ci się nagroda."

            menu:
                "{b}Zdozuneg{/b}":
                    luszcz2 "…"
                    luszcz2 "Proszę, tatusiu, nakarm mnie."

                    toxic "Heh"
                    toxic "Tatuś ma dla ciebie duuużo ammo…."
                
                "{b}Bez zdozunku{/b}":
                    luszcz2 "Nie-"
                    luszcz2 "Znaczy, em…"
                    luszcz2 "Nie mogę się… doczekać."

                    toxic "Lubię to co słyszę!"
                    toxic "Długo czekałem na twoje paluszki.."
            
            scene bg black with fade

            nikt "{i}jeden netflix później…{/i}"

            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            toxic "Dzięki kicia, ale następnym razem postaraj się może więcej miauczeć"
            toxic "Tatuś lubi, gdy miauczysz."
            toxic "Może zacząć ci coś nalewać? Tak na wywołanie pasji."

            menu:
                "{b}Tak (+2 jabole){/b}":
                    luszcz2 "Eh… jak chcesz… zobaczymy."

                "{b}Nie{/b}":
                    luszcz2 "Eh… jak chcesz… zobaczymy."

            toxic "Ej nie mówiłeś mi, że masz jakąś depresję albo coś."
            toxic "O takich rzeczach się ostrzega w relacjach, wiesz?"
            toxic "Znaczy, jakby spoko, to też jest trochę hot. Ale lubiłem twoją niezręczność."
            toxic "Spróbuj coś z tym zrobić do jutra, co?"

            hide toxic_pea
            show luszcz neutral at center
            
            if ailbib == 1:
                luszcz2 "Czarna księgo… pomóż mi"

                "{i}Łuszcz otwiera księgę{/i}"

                luszcz2 "“Chuj ci w dupę”"
                luszcz2 "“Albo mu”"
                luszcz2 "“Albo wam wszystkim”"
                luszcz2 "“Moje problemy jakoś nie są wasze.”"

                "{i}Łuszcz chowa ęilbib{/i}"

                luszcz2 "Ah."
            
            else:
                if biblia == 1:
                    luszcz2 "Jezu… pomóż mi"

                    "{i}Łuszcz otwiera biblię{/i}"

                    luszcz2 "“Wy jesteście światłem świata.”"
                    luszcz2 "“Nie może się ukryć miasto położone na górze.”"
                    luszcz2 "“Nie zapala się też światła i nie stawia pod korcem,”"
                    luszcz2 "“Ale na świeczniku, aby świeciło wszystkim, którzy są w domu.”"
                    luszcz2 "“Tak niech świeci wasze światło przed ludźmi, aby widzieli wasze dobre uczynki i chwalili Ojca waszego, które jest w niebie.”"

                    "{i}Łuszcz chowa biblię{/i}"

                    luszcz2 "Hm.."
                
                else:
                    luszcz2 "…"
                    luszcz2 "mam dość…"
            
            scene bg black with fade

            n "{i}Łuszczu, celowo unikając księżyca, spojrzał na swoje buty, a później swój ubiór.{/i}"
            n "{i}Brudne, zniszczone od walki łachmany przypomniały mu co sprawiło, że odwiedza to miejsce.{/i}"
            n "{i}Uczuł, jak całe jego ciało słabnie pod wpływem tej realizacji.{/i}"
            n "{i}Łuszczu jest zwiędłą roślinką, szukającą miłości.{/i}"
            n "{i} …{/i}"
            n "{i}Gdzie jest konewka, która miała go podlewać?{/i}"
            n "{i}Co da światło, co da ciepło, gdy nie ma wody?{/i}"
            n "{i}Nagle, ze szczyptą nienawiści, Łuczu spojrzał na księżyc, szukając w nim odpowiedzi.{/i}"
            n "{i}…{/i}"
            n "{i}Nie znalazł odpowiedzi, ale zwrócił uwagę na coś ciekawego.{/i}"
            n "{i}Księżyc, tak samo jak zielona kula, podeszwy jego butów, a nawet krople wody z konewki.{/i}"
            n "{i}Żadna z tych rzeczy, nieważne jak duża, nie daje ani światła, ani ciepła.{/i}"
            n "{i}To Słońce je dostarcza, wszystkim, wszędzie.{/i}"
            n "{i}Księżyc może tylko odbijać to, co noc ukrywa przed resztą Skały.{/i}"
            n "{i}Księżyc nie jest wyjątkowy.{/i}"
            n "{i}Wyjątkowa jest woda mineralna, której Łuszczu nagle zapragnął.{/i}"
            n "{i}Sponsorowane przez Muszynianka.{/i}"

            $ toxic_pea_social_link = 4
            $ toxic_pea_wybory = 1
            $ toxic_limit = 1

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska

    label toxic_pea5:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at center

        luszcz2 "(Nie czuję się na walkę. Poczekam tutaj)"

        scene bg black with fade

        "{i}Łuszczu zasypia{/i}"

        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at slightleft
        show toxic_pea neutral at slightright 

        toxic "O, Maciek_Rel, nie było cię dzisiaj"
        toxic "Opierdzielasz się?"
        toxic "Myślisz, że możesz tu przyjść na darmowy seks? Bez takich."
        toxic "Chyba, że ślicznie poprosisz tatusia, to może zmieni zdanie..?"

        luszcz2 "To koniec!"
        luszcz2 "Już tu więcej nie przychodzę. Chciałem żebyś wiedział, że jesteś okropną osobą i że twoje imię ci bardzo pasuje."

        toxic "A dziękuję."
        toxic "Ale nie mam pojęcia o co ci chodzi."

        luszcz2 "Byłem przez ciebie traktowany jak robotnik i zabawka! Myślałem że między nami coś było!"

        toxic "Może by było, gdybyś się tak nie zachowywał."
        toxic "Zresztą, robotnik i zabawka? Myślisz że nie widzę, jak przychodzisz tu ze swoją propagandą antychrześcijańską? Politycznymi agendami?"
        toxic "Niektórzy cię tutaj mylą z jechowymi, ciesz się że robię ci za adwokata bo byś dawno stracił głowę!"

        luszcz2 "Tylko raz wspomniałem o tej sprawie. I to prawda że zależy mi na tej sprawie, ale do ciebie podszedłem z kompletnie innymi intencjami."

        toxic "Wiesz co nie chce mi się kłócić. Ruchasz się czy nie?"

        menu:
            "{b}Tak{/b}":
                luszcz2 "T-"
                luszcz "Oczywiście że nie!"
            
            "{b}Nie{/b}":
                luszcz "Oczywiście że nie!"
        
        luszcz "Mam dość, idę stond."

        toxic "Czekaj, twoja wypłata, lewaku."
        
        play sound "audio/sfx/plucie.mp3"

        "{i}Toxic Pea pluje Łuszczowi na twarz obślizgłą kartką{/i}"

        toxic "Zmywaj się stąd."

        hide toxic_pea 
        show luszcz neutral at center

        "{i}Łuszcz zdejmuje kartkę z twarzy i zaczyna ją czytać{/i}"

        luszcz "“Ja, Toxic Pea, oświadczam że podpisuję się pod agendę obywatela Skały Macieja Cwela Łuszcza. Jestem wdzięczny za jego usługi seksualne, w tym palcowanie czy seks analny oraz miauczenie w ich procesie. Ten papier może być użyty jako głos w dowolnym głosowaniu jaki Maciej Cwel Łuszcz sobie wymarzy.”"
        luszcz "…"
        luszcz "Heh, pżynajmniej to wszystko nie poszło na marne."
        luszcz "Niech ja to tylko wyczyszczę"

        "{i}*siioooooooorb*{/i}"

        luszcz "Jest szansa rze będę tęsknić za tym smakiem."

        $ toxic_pea_social_link = 5
        $ toxic_pea_wybory = 2
        $ toxic_limit = 1

        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            play music "audio/music/pole.mp3"
        else:
            play music "audio/music/pole_noc.mp3"
        jump wolbromska


