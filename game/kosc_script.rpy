default lechia = 0
default koscielny_zyje = 0 
default cialo_wybrane = 0
default glowa_wybrane = 0

label kosc:
    label kosc1:
        scene bg kosciol with fade
        play music "audio/music/kosciol.mp3"
        show luszcz neutral at left

        luszcz "Em.. nieh będzie pochwalony."

        show kosc neutral at center 

        kosc "Niech będzie."
        kosc "Czego tu szukasz?"

        luszcz "Pomyślałem że mugłbym dowiedzieć się trochę więcej o Bogó."

        kosc "Na prawdę?"
        kosc "Tak myślałem, młody, że się tak szybko nie poddasz."
        kosc "Nawet się przed sprzątaniem modliłem w twojej intencji."
        kosc "To jak, może poczytamy Biblię?"

        luszcz "Dobże"

        kosc "Hmm.. gdzie by tu zacząć. O, wiem!"
        kosc "Słuchaj tego, to jest takie tuff."
        kosc "Mk 11, 12-14"
        kosc "“Nazajutrz, gdy wyszli oni z Betanii, uczułi głód. A widząc z daleka drzewo figowe, okryte liśćmi, podszedł ku niemu zobaczyć, czy nie znajdzie czegoś na nim…"

        scene bg black with fade
        scene bg kosciol with fade
        show luszcz neutral at left
        show kosc neutral at center 

        kosc "…Przez co, widzisz, wychodzi na to że kinuję Adama. Tak, Adama, pierwszego człowieka."
        kosc "Zgaduję że robi to ze mnie teoretyczne twojego ojca, ale nie martw się o to, jakoś to ogarniemy."
        kosc "Być może mógłbyś nazywać mnie tatą?"
        kosc "To był żart. Nie dzwoń na policję."


        luszcz "Wow, to wszystko takie fascynujące."
        luszcz "Zwłaszcza to że kinujesz Adama."
        luszcz "I opowieść z figami."
        luszcz "I liczne nawiązania do twórczości Zenona Martyniuka"

        kosc "Tak, zenon jest super."
        kosc "Słyszałeś o koncercie w czwartek po 15:00?"

        luszcz "O, no, chyba coś było na ogłoszeniach parafialnych."

        kosc "Zenek przyjdzie do kościoła i będzie śpiewał kolędy, dla dzieci z opóźnionym doświadczaniem ducha świąt."
        kosc "Bardzo miłe z jego strony, niech mu Bóg błogosławi."

        luszcz "Na pewno, pewnie, jasne."
        luszcz "W ogule dzienki że poczytałeś mi biblię"

        kosc "Spoko młody"
        kosc "Jak coś to Biblia z wielkiej litery"

        luszcz "Dobrze będę pamiętał."

        kosc "Wiesz co, mamy dużo egzemplarzy, nawet więcej niż ksiądz samochodów."
        kosc "Myślę że mogę ci jedną podarować."

        $ ile_item_fabularne += 1
        $ biblia = 1

        "{i}*Biblia została dodana do ekwipunku*{/i}"

        luszcz "Dziękuję"

        kosc "A gdybyś chciał się jeszcze pouczyć ze mną o Bogu, to co ty na to aby pójść na moje lekcje religii w podstawówce? Uczę teraz o religii w historii."

        luszcz "Historia jest ogułem fajna"
        luszcz "Jest szansa że nie dowiem się niczego nowego, ale myślę że mogę przyjść."

        kosc "To jak coś to to ta szkoła daleko od cmentarza."

        luszcz "Spoko, dzięki, Szczęść Borze"

        kosc "Szczęść Boże młody."

        play music "audio/music/pole.mp3"

        $ kosc_social_link = 1
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
        
    
    label kosc2:
        scene bg szkola with fade
        play music "audio/music/natura.mp3"
        show luszcz neutral at left
        show kosc neutral at center

        kosc "O przyszedłeś!"
        kosc "Widzę, że naprawdę chcesz zgłębiać wiedzę o Bogu!"

        luszcz "Tak, kocham Boga!"

        kosc "Dobrze w takim razie zapraszam za mną!"

        scene bg klasa
        play music "audio/music/szkola.mp3"
        show luszcz neutral right at slightright
        show kosc neutral left at slightleft

        kosc "To jest moja klasa, tutaj uczę te bachory prawdy"

        luszcz "Chwila kogo!?"

        kosc "Eeee znaczy kochane dzieci no tak kochane dzieci tutaj uczę..."
        kosc "Dobra, dobra za chwilę lekcja się zaczyna"

        show kosc neutral left at left

        kosc "Siądź sobie w jakiejś ławce, a ja przygotuję się do lekcji"

        show luszcz neutral right at right

        "{i}Łuszcz bez chwili zastanowienia rzucił się do ławki przy oknie z samego tyłu{/i}"

        luszcz "I feel so sigma"

        play sound "audio/sfx/dzwonek.mp3"

        "{i}Dzieci wchodzą do klasy{/i}"

        dzieciak "Ej to moje miejsce, ja tu zawsze siedzę!"

        luszcz "Sklej pizde, ja jestem eminencją w cieniu i nie widzisz mnie, bo się nie wyróżniam"

        kosc "Właśnie Stefan sklej pizdę i do dyrektora w tej chwili"

        stefan "Grrr strzelam"

        "{i}Stefan bierze plecak i wychodzi z klasy{/i}"
        hide luszcz 

        show kosc neutral left at center

        kosc "No dobrze drogie dzieci, a teraz przechodzimy do lekcji"
        kosc "Dziś znów wracamy do temtu religii w historii"
        kosc "I zaczniemy od czasów republiki rzymskiej, kiedy to polska jeszcze nie istniała"
        
        menu:
            "{b}...{/b}":
                luszcz "..."

            "{b}akszuli...{/b}":
                $ lechia += 1
                show luszcz sigma right at right
                luszcz "Akszuli to wtedy trwał złoty wiek Wielkiej Lechii"
                luszcz "i Lechici toczyli nawet wojny z rzymianami"
                luszcz "I byliśmy tak potężni, że sam Juliusz Cezar musiał wydać swoja siostrę za władce Lechii Leszka III!"

                kosc "..."
                kosc "wracając"
                hide luszcz

        kosc "Wtedy to właśnie powstała religia katolicka i przejeła należny dla niej tytuł najważniejszej religi świata obalając jakieś plemienie zabobony"

        menu:
            "{b}...{/b}":
                luszcz "..."

            "{b}akszuli...{/b}":
                $ lechia += 1
                show luszcz sigma right at right
                luszcz "Akszuli to nie były zabobony tylko prawda!"
                luszcz "Wszystkie obecne wtedy religie czciły Lechitów jako Bogów tak jak powinno być"
                luszcz "nawet został na to dowód w języku arabskim gdzie buk oznacza Al-lah, lah, lehita czyli my"
                luszcz "Jestem Bogiem uświadomcie to sobie sobie!"
                luszcz "Wy też jesteście Bogami, tylko uświadomcie to sobie sobie"

                kosc "..."
                kosc "wracając"
                hide luszcz
        
        kosc "Powstał wtedy też urząd papieża, co umożliwiło łatwiejsze rozprzestrzenianie się wiary katolickiej na świecie"
        kosc "I późniejsze dotarcie jej do nowo powstałej Polski w X wieku"

        menu:
            "{b}...{/b}":
                luszcz "..."

            "{b}akszuli...{/b}":
                $ lechia += 1
                show luszcz sigma right at right
                luszcz "Akszuli to nie była nowo powstała polska!"
                luszcz "Tylko WATYKAN tak sfałszował naszą historię, żeby nikt nie pamietał o WILKIEJ LECHII"
                luszcz "Ludzie obudźcie się! Nie możemy pozwalać, by ktoś nas kontrolował!"
                luszcz "Myslcie samodzielnie!"

                if lechia == 3:
                    kosc "Dość"
                    kosc "Nie chcę słyszeć, ani jednej bzdury więcej!"
                    kosc "Wynoś się stąd w tej chwili, albo wezwę Hiszpańską Inkwizycje"

                    luszcz "Aaaa dobrze już"
                    luszcz "ale wasze kłamstwo się długo nie utrzyma!"
                    luszcz "zobaczycie kiedyś ludzie przejrzą na oczy!"

                    scene bg szkola
                    show luszcz neutral at center
                    luszcz "Ehhh nie powinienem się bratać z katolami"
                    luszcz "przecież wiedziałem jak to się skończy..."
                    luszcz "no dobra,ale teraz spadam stąd zanim pojawi się inkwizycja"

                    $ kosc_social_link = 10
                    play music "audio/music/pole.mp3"
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
                    kosc "..."
                    hide luszcz
            
        scene bg black with fade
        "{i}reszta lekcji upłyneła w miarę bez zakłóceń{/i}"
        scene bg szkola with fade
        play music "audio/music/natura.mp3"
        show luszcz neutral right at slightright
        show kosc neutral left at slightleft

        kosc "Miło z twojej strony że przyszedłeś "
        kosc "Wiem że wcześniej byłeś jedynym dzieckiem ateistą w Skale"

        luszcz "Nie jestem dzieckiem!!!"

        kosc "A wybacz"
        kosc "W każdym razie chciałem się ciebie spytać czy nie chciałbyś mi potowarzyszyć podczas koncertu w czwartek po 15:00 na rynku?"
        kosc "Z przyjacielem zawsze raźniej."
        kosc "A serio uwierz mi on robi taką dobrą muzykę.."

        $ config.menu_include_disabled = True
        menu:
            "{b}Nienawidzę Zenek Martyniuk{/b}":
                $ config.menu_include_disabled = False
                luszcz "Nienawidzę Zenka!!! Gówno dupa!!!"

                kosc "O czym ty mówisz wymień jednego lepszego muzyka jakiegokolwiek."

                luszcz "Organista lepiej od niego śpiewa."
                luszcz "Gdybym miał czas to bym zorganizował na niego zamach w tym kościele."
                luszcz "Ale nie mam czasu więc haha żarcik"

                kosc "Sama myśl to nie grzech, liczą się czyny, więc spoko"
            
            "{b}Toleruję Zenek Martyniuk{/b}":
                $ config.menu_include_disabled = False
                luszcz "Szanuję twoją opinię ale ogółem to to jest dno polskiej sceny muzycznej"
                luszcz "Tuż obok (slaby artysta) i (slaby artysta)"

                kosc "Toleruję twoją tolerancję wobec mojej opinii."
            
            "{b}Kocham Zenek Martyniuk{/b}" if luszcz_hp == 12000339:
                $ config.menu_include_disabled = False

        luszcz "W każdym razie zastanowię się."

        kosc "Nie, ja chcę żebyś mi już powiedział czy będziesz!"
        kosc "Obiecaj na mały paluszek!"

        menu:
            "{b}Obiecuję{/b}":
                luszcz "Obiecuję"

                kosc "yaaay oki to cześć młody niech będzie pochwalon"

                luszcz "Niech będzie niech będzie"

                $ kosc_social_link = 2
                play music "audio/music/pole.mp3"
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
            
            "{b}Okej to nie{/b}":
                luszcz "Okej to nie idę"

                kosc "Szkoda"
                kosc "Ale spoko"
                kosc "Szanuję"
                kosc "To jest jakby okej"
                kosc "I w ogóle"
                kosc "Widzimy się w niedzielę czy coś.."
                kosc "Pa.."

                $ kosc_social_link = 10
                play music "audio/music/pole.mp3"
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

    label kosc_smierc:
        $ koscielny_zyje = 1
        show luszcz neutral at center
        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "A co to"

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Trzy uderzenia to norma w niedzielę."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Ale nie ma niedzieli lol"

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "W takim razie pewnie porzar…"

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Ciekawe co się pali…"

        "{i}(niet){/i}"

        luszcz "Chwila 6 uderzeń to pożar…"
        luszcz "A 5 uderzeń znaczyło…"
        luszcz "Śmierć kościelnego :0000"
        if kosc_social_link == 2:
            luszcz "Biedny… i to tuż przed koncertem…"
            luszcz "A tak mu zależało… nie spotka swojego idola…"
            luszcz "Może na pójdę na koncert? Tak ku pamięci?"
        else:
            if kosc_social_link == 10:
                luszcz "Nie, żeby mnie to jakoś obchodziło czy coś"

            else:
                luszcz "whatever"
        
        hide luszcz
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

    label kosc3:
        scene bg kosciol with fade
        play music "audio/music/koledy.mp3"
        show luszcz neutral at center
        luszcz "Nienawidzę tego co słyszę"
        if kosc_social_link == 2:
            luszcz "Ciekawe co się stało z Kościelnym…"
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        if kosc_social_link == 2:
            luszcz "Chyba stąd pójdę"

            show kosc duch at right

            kosc "CZEKAJ!"
            kosc "Uff udało mi się przebić"

            luszcz "Jezus Maria"

            kosc "Nie mów tak tak nie wolno"
            kosc "Wiesz ile ona płacze bo tak mówią?"

            luszcz "Co ci się w ogóle stało? Jak umarłeś? Czemu tu jesteś?"

            kosc "Musiałem tu być przecież sobie obiecaliśmy."
            kosc "Ogółem to prawda jest taka… że ja sam cierpię na ducha opóźnionych świąt"
            kosc "I choroba polega na tym, że jak nie będziesz świętować w bardzo ścisłym okresie czasowym, to umierasz i konsekwentnie, giniesz."
            kosc "A tegoroczny okres czasowy skończył się dziś koło 15:00."
            kosc "Koncert miał się odbyć na styk, jednakże Zenek Martyniuk postanowił wysłać się do Skały pocztą polską. Więc zamiast być tu wczoraj jest dopiero dziś"

            luszcz "Ej szczerze to bardzo wcześnie jak na ich standardy"

            kosc "No niby tak ale choroba nie poczeka."
            
            luszcz "Chwila czyli to znaczy że wszycy inni chorzy w Skale też poumierali?"
            luszcz "To dlatego taka tu stypa"

            kosc "Tak ale dostali rabaty do nieba w zamian więc jest okej."

            luszcz "A ty czemu nie w niebie?"

            kosc "Próbowałem się dostać ale Św. Piotr mnie nie wpuścił, bo Bóg ma Adam kinnerów w “DNI”"
            kosc "W sensie, nie chce ze mną wchodzić interakcje."
            kosc "Ale nie ma dla mnie miejsca w piekle, więc tułam się po ziemi."

            luszcz "Jak w dziadach"

            kosc "Nie kojarzę"

            luszcz "Siara"
            luszcz "…"
            luszcz "Przynajmniej możesz słuchać koncertu."

            kosc "Tak, ale o wiele gorzej się słyszy gdy jest się duchem."

            luszcz "Ojć"

            kosc "I w ogóle nic nie czuję"
            kosc "Taki taki"
            kosc "Hollow"
            kosc ";("

            luszcz "Chętnie bym się z tobą zamienił miejscami teraz"

            kosc "Wiesz co szczerze nie wiem czy to ma sens tak w nieskończoność latać po ziemi"
            kosc "Nie mogę głosić ewangelii, czytać biblii, ani zbierać składki. Co to za życie."

            luszcz "Nie przejmuj się bracie"
            luszcz "Zawsze masz mnie"
            luszcz "Znaczy, przez najbliższe powiedzmy 30 lat"

            kosc "Że co że planujesz umrzeć za 30 lat?"

            luszcz "20.56.2056"

            kosc "co"

            luszcz "20.56.2056"

            kosc "okej"
            kosc "Wracając, chyba nie mogę z tobą cały czas rozmawiać"
            kosc "Tylko teraz miłość do zenka i ciebie mnie przebiła"
            kosc "Przykre to ale"
            kosc "Powinienem wiedzieć na co się piszę kinując Adama piewszego człowieka."
            kosc "Rzegnaj"

            hide kosc

            luszcz "Niech będzie pochwalon…"
            luszcz "głópi Bug"
            luszcz "kto to widział takie rzeczy"
            luszcz "I poczcie polskiej terz nigdy tego nie zapomnę."
            luszcz "Gdybym tylko mugł go jakoś wrucić do rzywych……………………………………………..…………………………………………………………………."
            luszcz "…………………………………………………..…………………………………………………………………"
            luszcz "Dobra, spadam stąd."

            $ kosc_social_link = 3
            play music "audio/music/pole.mp3"

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
            luszcz "Dłużej nie wytrzymam, idę stąd"
            play music "audio/music/pole.mp3"
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

    label kosc4:
        scene bg cmentarz_noc with fade
        play music "audio/music/natura.mp3"
        show luszcz neutral at left
        show harambe duch at slightright

        luszcz "Harambe! Potrzebóję twojej pomocy!"

        harambe "Łuszcz. Co."

        luszcz "Kościelny zginął, ale nie dostał się do nieba i tuła się nieskończenie po ziemi!"

        harambe "Jak. W. Dziadach."

        luszcz "Czy da się coś zrobić aby go przywrócić do żywych?"

        harambe "Oczywiście."
        harambe "Jeden:"
        harambe "Znajdź. ailbiB."
        harambe "Jezioro. Noc."
        harambe "Dwa:"
        harambe "Ciało. Bez. Duszy."
        harambe "Trzy:"
        harambe "Przynieś. Harambe. Czary Mary."

        luszcz "Ah, no przecierz"
        luszcz "Dziękuję Harambe"

        harambe "Przyjaciel."

        $ harambe_social_link = 2

        play music "audio/music/pole.mp3"
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

    label kosc5:
        scene bg cmentarz_noc with fade
        play music "audio/music/natura.mp3"
        show luszcz neutral at left
        show harambe duch at slightright

        luszcz "Harambe, mam już wszystko!"
        harambe "Czary. Mary?"

        menu:
            "{b}Czary Mary{/b}":
                if cialo == 1 and glowa == 1:
                    harambe "Wybierz. Ciało."
                    menu:
                        "{b}Eminem{/b}":
                            $ cialo_wybrane = 1
                            harambe "Ciało. Emina."
                            $ cialo = 0
                            $ ile_item_fabularne -= 1
                            harambe "Dobrze."
                        
                        "{b}Nemeczek{/b}":
                            harambe "Ciało. Nemeczek."
                            harambe "Ciało? Głowa."
                            harambe "Głowa?"
                            luszcz "(Czy to na pewno dobry pomysł?)"

                            menu:
                                "{b}Tak{/b}":
                                    $ glowa_wybrane = 1
                                    luszcz "Tak, głowa."
                                    $ glowa = 0
                                    $ ile_item_fabularne -= 1

                                    harambe "Okej…"
                                
                                "{b}Nie{/b}":
                                    $ cialo_wybrane = 1
                                    luszcz "Żeczywiście, może lepiej nie."

                                    harambe "Dobrze."

                                    luszcz "W takim razie niech będzie ciało Eminema"
                                    $ cialo = 0
                                    $ ile_item_fabularne -= 1

                                    harambe "Ciało. Emina."
                                    harambe "Dobrze."

                else:
                    if cialo == 1:
                        $ cialo_wybrane = 1
                        harambe "Ciało. Emina."
                        $ cialo = 0
                        $ ile_item_fabularne -= 1
                        harambe "Dobrze."
                
                    if glowa == 1:
                        harambe "Ciało. Nemeczek."
                        harambe "Ciało? Głowa."
                        harambe "Głowa?"
                        luszcz "(Czy to na pewno dobry pomysł?)"

                        menu:
                            "{b}Tak{/b}":
                                $ glowa = 0
                                luszcz "Tak, głowa."
                                $ glowa = 0
                                $ ile_item_fabularne -= 1

                                harambe "Okej…"
                            
                            "{b}Nie{/b}":
                                luszcz "Żeczywiście, może lepiej nie."

                                harambe "Dobrze."

                                luszcz "(Morze znajdę coś innego?)"

                                play music "audio/music/pole.mp3"
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
                $ ailbib = 0
                $ ile_item_fabularne -= 1
                harambe "Start. Rytuał."
                show harambe ksiazka at right
                if cialo_wybrane == 1:
                    show emina dead at center
                    harambe "U U A A"
                    harambe "UE UE UEHEHEHE"
                    harambe "…"
                    harambe "リᔑ⋮ʖᔑ∷↸⨅╎ᒷ⋮  ꖎ⚍ʖ╎ᒷ  ⨅⚍⨅||ℸ ̣ ᒷ  !¡𝙹  ᓵᔑꖎ||ᒲ  ↸リ╎⚍  ᒲ𝙹ꖌ∷ᒷ  ∷ᔑ⋮ᓭℸ ̣ 𝙹!¡||  ∴ᓵ╎ᔑ⊣ᔑᓵ  ⨅ᔑ!¡ᔑᓵ⍑  ᒲᒲᒲ  !¡||ᓵ⍑𝙹ℸ ̣ ᔑ"
                    harambe "⋮ᒷᓭꖎ╎  ℸ ̣ 𝙹  ᓵ⨅||ℸ ̣ ᔑᓭ⨅  ꖎ⚍ʖ╎ᓭ⨅  ↸⚍⨅ᒷ  ᒲᒷᓭꖌ╎ᒷ  !¡ᒷリ╎ᓭ||  ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ"
                    show harambe duch at right

                    show emina neutral

                    emina "AAAAAAAAAAAA!!!"
                    emina "Fuck!"
                    emina "Kto to powiedział!"

                    harambe "Czar. Zadzialał."

                    luszcz "he he hell je"
                    luszcz "Szczęść Boże!"

                    emina "Szczęść Boże!"
                    emina "Fuck!"
                    emina "Fucking hell!! Czemu ciągle przeklinam!"

                    luszcz "Jesteś w ciele Eminema"
                    luszcz "Użyliśmy go żeby przywrócić cię do żywych"

                    emina "Zabiłeś dla mnie drugiego człowieka? Fuck!"
                    emina "A to nie był grzech?"

                    luszcz "Nie no nie"
                    luszcz "Znaczy teoretycznie zabiłem ale nie dla ciebie"
                    luszcz "Jednakrze jak już lerzy ciało i się marnuje to morzna wykorzystać"

                    emina "Hmm… Fuck!"
                    emina "Dobra nie mam czasu żeby się tym martwić, mam swoje pierdolone życie spowrorem!"
                    emina "Shit! To przeklinanie mnie drażni tho"

                    harambe "Taka. Cena. Życia."

                    luszcz "Dokładnie, to co mistrz powiedział."

                    emina "Fuck on ma racje."
                    emina "Życie ponad wszystko"
                    emina "Kocham kurwa życie"
                    emina "Fuck"
                    emina "Dziękuję ci, młody, za zaaranżowanie tego"
                    emina "Jestem ci nieskończenie wdzięczny"
                    emina "Fuck"
                    emina "Pozwól że pójdę oczyszczać to ciało z grzechu ciężką pracą. Fuck."
                    emina "Przy okazji korzystając z kinowania pierwszego człowieka póki mogę."
                    emina "Bóg z wami dobrzy ludzie! Fuck y’all!"

                    hide emina
                    $ kosc_wybory = 2
                    $ kosc_social_link = 4

                    luszcz "…"
                    luszcz "CZEKAJ!"

                    show emina neutral at center

                    luszcz "Czy potrafisz zrymować pomarańczę z bananem?"
                    emina "…"
                    emina "Bornana"

                    hide emina

                    harambe "Mmmmm…"

                    play music "audio/music/pole.mp3"
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
                    show glowa_nemeczek at center
                    harambe "U U A A"
                    harambe "UE UE UEHEHEHE"
                    harambe "…"
                    harambe "リᔑ⋮ʖᔑ∷↸⨅╎ᒷ⋮  ꖎ⚍ʖ╎ᒷ  ⨅⚍⨅||ℸ ̣ ᒷ  !¡𝙹  ᓵᔑꖎ||ᒲ  ↸リ╎⚍  ᒲ𝙹ꖌ∷ᒷ  ∷ᔑ⋮ᓭℸ ̣ 𝙹!¡||  ∴ᓵ╎ᔑ⊣ᔑᓵ  ⨅ᔑ!¡ᔑᓵ⍑  ᒲᒲᒲ  !¡||ᓵ⍑𝙹ℸ ̣ ᔑ"
                    harambe "⋮ᒷᓭꖎ╎  ℸ ̣ 𝙹  ᓵ⨅||ℸ ̣ ᔑᓭ⨅  ꖎ⚍ʖ╎ᓭ⨅  ↸⚍⨅ᒷ  ᒲᒷᓭꖌ╎ᒷ  !¡ᒷリ╎ᓭ||  ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ⍑ᔑ"
                    show harambe duch at right

                    show glowa_nemeczek 2 

                    nemeczek "AAAAAAAAA"
                    nemeczek "AŁAAAAAAA AAAAAAA"

                    harambe "Czar. Zadziałał."

                    nemeczek "AAAAAAAAA AAAAAAAAAA"

                    luszcz "Ups"

                    nemeczek "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                    nemeczek "eee…. eee……"
                    nemeczek "hhhhhh  h hh hhh…"
                    nemeczek "gfsddw"

                    hide glowa_nemeczek
                    $ kosc_wybory = 0
                    $ kosc_social_link = 4

                    luszcz "To chyba nie był dobry pomysł."

                    harambe "Hm."

                    play music "audio/music/pole.mp3"
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

            "{b}Twoja Stara To Twój Stary{/b}":
                harambe "Ha."
                luszcz "Wrócę jak będę gotów."
                play music "audio/music/pole.mp3"
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

