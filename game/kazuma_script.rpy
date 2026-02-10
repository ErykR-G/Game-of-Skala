default gacie_ukradniete = 0

label kazuma:
    label kazuma1:
        scene ss1 with fade
        play music "audio/music/ryby.mp3"
        show luszcz neutral at left
        kazuma "Siema, przyszedłeś połowić?"

        menu:
            "{b}Chcę połowić{/b}":
                luszcz "Chętnie."

                play sound "audio/sfx/start.mp3"

                scene ss2

            "{b}Nie chcę połowić{/b}":
                luszcz "Nie, tak się tylko rozglądam."

                kazuma "Szkoda, wartościowe śmieci można tu wyłowić."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump granica

        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"

        kazuma "o!"

        play sound "audio/sfx/powrot.mp3"

        scene ss3

        kazuma "Jackpot!"

        kazuma "Skąd to jezioro ma w ogóle takie rzeczy?"

        play sound "audio/sfx/beta.mp3"
        scene ss4
        luszcz "Dobre pytanie"
        luszcz "Długo tu już siedzisz?"

        play sound "audio/sfx/start.mp3"
        scene ss5

        kazuma "Nie no, jakoś z dwie godzinki."

        luszcz "huh."
        luszcz "To musisz mieć dużo szczęścia"

        kazuma "Yup."

        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"

        luszcz "o!"

        play sound "audio/sfx/powrot.mp3"
        scene ss6

        luszcz "Patż, Grzegorz!"
        luszcz "Schowam go do kieszeni."

        play sound "audio/sfx/beta.mp3"
        scene ss7

        kazuma "Fajny,"
        kazuma "fajny pies."

        play sound "audio/sfx/start.mp3"
        scene ss5

        luszcz "W ogóle czemu tu tak hurtowo łowisz?"

        kazuma "Nie wiem czy powinienem o tym mówić na głos"
        kazuma "Skąd mam wiedzieć że nie wygadasz?"

        luszcz "Uszy słyszą oczy widzą usta milczą"
        luszcz "Śmierć konfidentom!"

        kazuma "W takim razie dobra"
        kazuma "Ogółem to po mojej ostatniej przygodzie popadłem w ogromny dług"
        kazuma "Zazwyczaj spłacam długi idąc na kolejne przygody i dorabiając się na nich,"
        kazuma "Ale tym razem nigdzie nie widzę żadnego srogo płacącego questa"
        kazuma "Więc muszę znaleźć nowe sposoby na pieniądze."
        kazuma "Akurat tutaj mają darmowe wędki, więc zacząłem od łowienia."
        kazuma "Potem spróbuję sprzedać cały ten grat i potęgować zysk w kasynie"
        kazuma "O, i nie wiem czy wspomniałem ale ściga mnie urząd skarbowy."

        luszcz "Ciekawe masz rzycie."
        luszcz "Ale serio, nie spodziewałbym się nigdy że morzna tu wyłowić tyle rzeczy. Muszę zacząć tu wracać."

        kazuma "Ostrzegam, że raczej nie wyłowisz ćwiartki tego co ja, ale yeah. Sam się nie spodziewałem takich wyników. Nawet nie wiem jak to przenieść."
        kazuma "A w ogóle to czym ty się w życiu zajmujesz?"

        luszcz "Jestem na misji!"
        luszcz "Ksiądz na ostatniej mszy ogłosił że w najblirzszą niedzielę Skała zostanie pochłonienta przez Kraków."
        luszcz "Drań robi to czysto dla zarobku! Nie ma powodu żeby oddawać im naszą niepodległość!"

        kazuma "Kraków? Tutaj?!"
        kazuma "W Krakowie szukają mnie za moje długi! Dopiero co udało mi się uciec!"
        kazuma "Gdybym mógł to bym ci pomógł w twojej sprawie, ale muszę najpierw postawić się na nogi."

        luszcz "Spoko sam, fakt że jesteś po mojej stronie to durzo."
        luszcz "btw mam na imie Łuszcz, a ty?"

        kazuma "Nazywam się Kazuma."

        trump "Tak, brązowowłosy animochłopiec poszedł w tą stronę."
        trump "Teraz poproszę o tego piątaka."

        kazuma "Chwila… co?"

        scene bg jezioro10
        show kazuma neutral right at left 
        show luszcz neutral at slightleft
        show policja1 neutral at slightright
        show policja2 neutral at right

        ""

        us "Czy jest tu jakiś Kazuma Sato?"

        show kazuma neutral right at slightleft
        show luszcz neutral at left

        kazuma "Tak, jestem Kazuma."
        kazuma "Znaczy!! Um….!!"

        us "Proszę się nie ruszać! Rączki do góry!"

        kazuma "Nie no bez jaj, jak mnie tak szybko znaleźliście?"

        us "Dostaliśmy donosicielski telefon na pana! Jest pan aresztowany!"

        kazuma "Nie wierzę! To ty!?"

        luszcz "Przecież widziałeś że ciągle byłem koło ciebie!"

        kazuma "To weź bądź kolega i mi tu pomóż!"

        luszcz "Dobra dobra"
        luszcz "Z psami zawsze powalcze"

        $ kazuma_sojusznik = 1
        $ liczba_sojusznikow += 1

        jump fight161

    label after_fight161:
        $ kazuma_sojusznik = 0
        $ liczba_sojusznikow -= 1
        scene bg jezioro
        play music "audio/music/ryby.mp3"
        show kazuma neutral at slightright
        show luszcz neutral at slightleft

        if gacie_ukradniete > 0:
            luszcz "Czemu kradniesz ludziom ich gacie??"

            kazuma "Działa? Działa."
            kazuma "Po co zbędne pytania."
            kazuma "Zresztą, nie ludziom. Tylko kobietom."
            kazuma "…"
            kazuma "Sory źle zabrzmiało"

            luszcz "To jeszcze dziwniejsze…"

            kazuma "Anyway, czas przetransportować mój…"
            kazuma "Gdzie jest mój towar????"
            kazuma "Te dranie!!! Wszystko ukradli!!!"
            kazuma "Wszystko od nowa!!!"
            kazuma "Pewnie jeszcze kogoś po mnie teraz wysłali…"
            kazuma "Pomóż mi kurwa…"

        menu:
            "{b}Inwestuj w kolegę{/b}":
                luszcz "Wiesz co, może schowaj się na razie u mnie w domó."
                luszcz "Wymyślimy tam co robić dalej. Ale jeśli cię tak ścigają to lepiej cię gdzieś chować."
                luszcz "Tu masz klucze."

                kazuma "Wow bratku dzięki."
                kazuma "To ja nie tracę czasu, tylko się zwijam."

                $ kazuma_social_link = 1
                $ kazuma_wybory = 1
                hide kazuma
                show luszcz neutral at center
                luszcz "Ja też powinienem pójść z tego miejsca..."
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump granica
                            
            "{b}Powodzenia!!!{/b}":
                luszcz "Hej, przykro że jesteś w takiej sytuacji, ale nie mam teraz czasu na pieprzenie się z policją."
                luszcz "Powodzenia!! Idę ratować skałę!"

                kazuma "A daj spokój, dzięki."
                kazuma "Tobie też powodzenia."

                $ kazuma_social_link = 10
                $ kazuma_wybory = 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump granica

label kazuma2:
    if drukowanko == 1:
        scene bg pokoj2 with fade
        play music "audio/music/drukowanie.mp3"
    else:
        scene bg pokoj with fade
        play music "audio/music/pokoj.mp3"

    show kazuma neutral at slightright
    show luszcz neutral at slightleft
    show grzesiu makowiec:
        xalign 0.19
        yalign 0.575
    
    luszcz "Hej"

    kazuma "Wait patrz jaki śmieszny obrazek znalazłem"

    show labubu 

    $ renpy.pause(1.5)

    hide labubu

    kazuma "Albo patrz na to"

    show lion 

    $ renpy.pause(1.5)

    hide lion

    kazuma "Literalnie ja"

    luszcz "Masz jakieś pomysły na zarobek?"

    kazuma "Może rzeczywiście pójdę do kasyna."
    kazuma "Klub Seniora ma całą sekcję do gamblingu."
    kazuma "Z moim szczęściem nie ma szans, żeby coś przewalić."
    kazuma "Potrzebowałbym jednak pieniędzy na start."
    kazuma "Podzieliłbyś się? Obiecuję, nie pożałujesz."

    $ config.menu_include_disabled = True
    menu:
        "{b}Kocham gambling!!!!! Daj 2${/b}" if money >= 2:
            $ config.menu_include_disabled = False
            $ money -= 2
            luszcz "Bierz i korzystaj."

            kazuma "Dzięki! To widzimy się w Klubie Seniora!"

            luszcz "Oki"

            $ kazuma_social_link = 2
            $ kazuma_wybory = 1

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
        
        "{b}Nic nie dam{/b}" if money >= 2:
            $ config.menu_include_disabled = False
            luszcz "Nie dam ci nic"
            luszcz "Moje pieniążki"

            kazuma "A w domu mogę zostać?"
            
            luszcz "Możesz"

            kazuma "To będę siedział aż zmienisz zdanie"
            kazuma "I patrzył na obrazki"

            luszcz "Spk"

            $ kazuma_social_link = 1
            $ kazuma_wybory = 1

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

label kazuma3:
        scene bg kasyno with fade
        play music "audio/music/kasyno.mp3"
        show luszcz neutral at slightleft
        show kazuma neutral at slightright

        kazuma "Łuszczu! Cześć!"

        luszcz "Cze, jak ci idzie?"

        kazuma "W kasynie zawsze mi idzie dobrze"
        kazuma "Ale gram powoli, żeby nie przyciągać wzroku"

        kazuma "W zasadzie, to już się na mnie trochę gapią…"
        kazuma "Jak boga kocham jeśli ktoś zadzwoni na policję to wykradam wszystkim tutaj gacie"
        kazuma "W tym mężczyznom i tobie"

        luszcz "Dobra chill chill"
        luszcz "Wpadłem na git pomysł"
        luszcz "Co gdybym grał przez chwilę za ciebie? Tak żeby coś poprzegrywać."

        kazuma "Niegłupie"
        kazuma "Tylko skąd wytrzaśniemy teraz ukryte słuchawki i kamerki i wszystko?"

        luszcz "Oj, nie potrzebujemy niczego takiego."
        luszcz "Chodź na chwilę do kibla"

        kazuma "Dobra"

        scene bg black with fade
        scene bg kasyno with fade
        show kazuma czapka at center

        kazuma "…"
        kazuma "Jestem pod wrażeniem że udało ci się tam zmieścić."

        luszcz "Ja też"

        kazuma "Ej a co jak ktoś oglądał ten film i nas rozgryzie?"

        luszcz "Bez przesady. Nikt w kasynie nie spędza ze swoimi dziećmi na tyle czasu żeby oglądać Pixara"

        kazuma "I guess."

        luszcz "Czekaj zrubmy test mówienia."
        luszcz "Nie pżestrasz się."

        kazuma "Okej jestem gotów"

        menu:
            "{b}Powiedz, że masz bombę{/b}":
                kazuma "MAM BOMBE!!!!!"
                kazuma "Sorki mam touretta!!! Hehe!! Chuj!"
                kazuma "…"
                kazuma "(weź się pierdol, co ty sobie myślisz??)"
                kazuma "(żeby mi to było ostatni raz.)"

                luszcz "(Nigdy więcej szpontu, obiecuję.)"
                            
            "{b}Powiedz coś głupiego{/b}":
                kazuma "coś głupiego"

                luszcz "(okej działa)"
                luszcz "(idziemy)"
            
            "{b}Powiedz prawdę{/b}":
                kazuma "KOCHAM DUŻE MĘSKIE KUTASY!!!"
                kazuma "(Co ty robisz??!!!)"

                luszcz "(mówię prawdę..)"

                kazuma "(To mów ją sobie w swoim imienu!!)"

                show saul neutral at left
                show kazuma czapka at slightright

                saul "Dzień dobry"
                saul "Może usiądzie pan ze mną na drineczka?"

                kazuma "Tak, chętn-"
                kazuma "NIE, nie jestem zainteresowany."

                saul "To po kiego się tak wydzierasz"
                saul "męskie dziwki…"

                hide saul
                show kazuma czapka at center

                kazuma "Dobra weźmy się za bizes a nie kurde tego ten."
            
            "{b}Zacytuj Biblię{/b}" if biblia == 1:
                kazuma "“Jeśli się bić będą mężczyźni, mężczyzna i jego brat, i zbliży się żona jednego z nich i - chcąc wyrwać męża z rąk bijącego - wyciągnie rękę i chwyci go za części wstydliwe, odetniesz jej rękę, nie będzie twe oko miało litości.”"
                kazuma "Jana 20: 8-9"
                kazuma "Czy mogę dostać amen?"
                
                show saul neutral at left
                show kazuma czapka at slightright

                saul "Amen!"

                hide saul
                show kazuma czapka at center

                kazuma "(amen!)"
                kazuma "(dobra, chodźmy)"
        
        scene bg kasyno2
        show poker at left
        show kazuma czapka at slightright

        kazuma "(o, ta gierka jest całkiem prosta, myślę że sobie poradzisz)"

        luszcz "(ej grałem w to gdzieś!)"

        kasyn "Dzień dobry, pan chce zagrać w Knucklebones?"

        kazuma "Chciałbym."
        kazuma "Dobrze, tłumaczyć panu zasady?"
        kazuma "Nie, znam je"

        "{i}jak nie znasz to sobie wyguglaj lol{/i}"

        kasyn "Jak pan wygra to podwajamy kwotę, gdy przegra to zabieramy co pan dał."
        kasyn "Z jaką kwotą gramy?"

        $ money -= 1
        kazuma "Jeden portfel."

        kasyn "Dobrze. Powodzenia."

        play music "audio/music/knuclebones.mp3"
        jump play_knucklebones


        label wygranko_kasyno:
            play music "audio/music/kasyno.mp3"
            kasyn "Gratuluję, oto pański portfel oraz drugi za wygraną."

            $ money += 2
            "{i}*2 Portfele zostały dodane do ekwipunku*{/i}"

            kazuma "A dziękuję."

            scene bg kasyno
            show kazuma czapka at center

            kazuma "(co ty robisz??? Miałeś przegrać?????)"

            luszcz "(o borze zapomniałem)"

            kazuma "(dobra… i tak mam już wystarczająco dużo chajsu…)"
            kazuma "(chodźmy wymienić moje żetony)"

            jump kasyneczek


        label przegranko_kasyno:
            play music "audio/music/kasyno.mp3"
            kasyn "Przykro mi, pański potfel teraz należy do mnie."
            kasyn "(haha przegryw)"

            scene bg kasyno
            show kazuma czapka at center
            
            kazuma "(dobra dzięki, myślę że będę teraz dla nich czysty.)"
            kazuma "(chodźmy wymienić moje żetony)"

            jump kasyneczek
        
        label kasyneczek:
            scene bg kasyno4
            show kazuma czapka right at slightleft

            kazuma "Witam chciałem wymienić moje żetony na pienionżki"
            
            scene bg kasyno6
            show kazuma czapka right at slightleft
            with hpunch

            nu "……"
            nu "(Chryste panie…)"
            nu "(Chyba muszę to zgłosić szefowej…)"
            nu "Już proszę pana, tylko do toalety pójdę"

            kazuma "Oczywiście, nie ma problemu"

            scene bg kasyno7
            show kazuma czapka right at slightleft
            if eminem_sojusznik == 1:
                show eminem neutral at right
                cid "Ej bo ja ją chyba skąś kojarzę"
                cid "Tylko nie wiem skąd..."
                cid "ewentualnie coś mi się powaliło"
                cid "Za dużo kręci się wokół mnie kobiet"

                luszcz "(No kobiety mega fujka)"
                luszcz "(Jakby chociaż miały duże kutasy)"
                luszcz "(ehhh no nic, oby tylko nie poszła nas zgłosić)"
            
            else:
                luszcz "(przygłupie a co jak poszła to zgłosić?)"

                kazuma "(dobra racja, ale przecież jej nie zatrzymam)"

            scene bg kasyno5 with fade
            show gamma neutral at center 
            show nu neutral at right

            gamma "…wiesz że ja jestem tu zajęta!"
            gamma "Następnym razem musisz pukać!!"

            nu "Dobrze, przepraszam…"
            nu "Ale, sprawa jest poważna!"
            nu "Jeden z klientów, Kazuma, właśnie chce wymienić żetony na kwotę dwustu stu trzech tysięcy siedemset portfeli!"

            gamma "Co?! Czym ja będę teraz inwestować w sztuczną inteligencję?"
            gamma "Zresztą, jakim cudem go jeszcze nie czmychnęliście?"

            nu "Nie było podstaw, wszystko wygrał uczciwie"

            gamma "Dobra dość, biorę sprawy w swoje ręce"

            scene bg kasyno7 with fade
            show kazuma czapka right at slightleft

            luszcz "(Myślisz że sra czy siura)"

            kazuma "(Jakbyś spytał minutę temu to bym powiedział że siura, ale już przekroczyła granicę czasową.)"

            luszcz "(Nie no słuchaj)"
            luszcz "(Nie masz tak czasem, że mega dużo wypijesz, i mega długo trzymasz, a potem jak siadasz na kiblu to nie przestaje lać?)"

            scene bg kasyno6
            show kazuma czapka right at slightleft

            nu "Przepraszam, mogło chwilę zająć."

            kazuma "Siórała pani czy srała?"

            nu "Proszę pana proszę się zachowywać!"

            luszcz "(na pewno siurała!)"

            kazuma "Jejku, przepraszam, to moje tiki."
            kazuma "(wykastruję cię jak to się skończy)"

            nu "Em, w takim razie nie ma problemu."
            nu "Znaczy w sumie jest…"
            nu "Nie możemy panu dziś wydać portfeli…"
            nu "Może spróbuje pan jutro?"

            kazuma "O czym pani gada? Żadne kasyno tak nie operuje…"

            nu "Em… dobra, walić"
            nu "Pewnie i tak już mi za nic nie zapłaci"
            nu "Szefowa uciekła ze wszystkimi portfelami."
            nu "Chce pan żebym zadzwoniła dla pana na policję?"

            kazuma "Nie! Proszę nie dzwonić!"

            nu "…?"
            nu "Dobrze, w takim razie miłego dnia, ja się w to nie mieszam."

            kazuma "Miłego."

            luszcz "(chodźmy szybko na zewnątrz, morze jeszcze nie odjechała!)"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                scene bg grota
            else:
                scene bg grota_noc
            show kazuma czapka at center
            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"

            kazuma "NIENAWIDZĘ CZARNYCH!!!"
            kazuma "(Dobra, wyłaź już z tej czapy)"

            luszcz "(Tak myślałem, rze to ostatnia szansa)"

            show kazuma neutral at slightright
            show luszcz neutral at slightleft
            with hpunch

            luszcz "Kurde… pewnie już odjechała…"

            show luszcz neutral at center
            show kazuma neutral right at left
            show grzesiu pistolet at right
            with vpunch

            grzes "Panowie!"
            grzes "Ani kroku dalej!"
            grzes "Jeśli wam życie miłe"
            
            luszcz "Grzegoż co ty robisz?!"

            kazuma "To ten robak z jeziora??"

            grzes "Spokojnie… nikomu nic się nie stanie"
            grzes "Tylko oddajcie wszystko co tam wygraliście."

            luszcz "Ty?! Przeciwko mnie?!"
            luszcz "Ufałem ci Grzegorz…"

            kazuma "To ty zadzwoniłeś na gliny nad jeziorem??"
            kazuma "Zasrany kapuś…"

            grzes "Biznes to biznes."
            grzes "Chajs albo śmierć."

            kazuma "(łuszczu, przecież my nie mamy chajsu…)"
            kazuma "(co robimy?)"

            menu:
                "{b}Zabij karalucha{/b}":
                    luszcz "Uwaga!"

                    "{i}Łuszczu szybkim ruchem próbuje zaatakować Grzesia{/i}"

                    grzes "Piu piu!!!!!"

                    play sound "audio/sfx/gun.mp3"
                    with vpunch

                    show kazuma strzal right

                    kazuma "Ała kurwa!!!!"

                    hide grzesiu
                    show luszcz neutral right at slightright
                    show kazuma strzal right at slightleft

                    kazuma "aaaaaa krew jest wszędzie aaaa!!!"

                    luszcz "Kamzuma!!!!"
                    luszcz "Mósimy cię zabrać do lekaża!!"

                    kazuma "No… kurcze rzeczywiście…"

                    jump gotka7
                
                "{b}Okradziono nas!{/b}":
                    luszcz "Grzesio, ziomek, dałbym wszystko ale mam póste kieszenie!"
                    luszcz "Szefowa jak odkryła ile wygraliśmy uciekła ze wszystkim!!"

                    if urban_sojusznik == 1:
                        show luszcz neutral at slightleft
                        show urban neutral at center
                        urban "Tak było!"
                        urban "Nie zmyślam."
                        hide urban 
                        show luszcz neutral at center

                    grzes "Hm…"
                    grzes "No w sumie widziałem jakąś babkę odjeżdżającą z pełnymi worami."
                    grzes "…"
                    grzes "Pojechała w stronę granicy. Chce opuścić Skałę."
                    grzes "Macie ostatnią szansę. Jak jej nie złapiecie to powiadamiam psy o twoim koledze."

                    kazuma "Pierdol sie!!!"
                    
                    luszcz "Dobra to Kazuma dawaj szybko"

                    kazuma "Ja jestem Kazuma."

                    play sound "audio/sfx/traveling.mp3" 
                    $ rynek = 0
                    $ sloneczna = 0
                    $ alejka = 0
                    $ parking = 0
                    $ wolbromska = 0
                    $ bohaterow_wrzesnia = 0
                    $ lipowa = 0
                    $ granica = 1
                    if timer >= 360 and timer <= 1200:       
                        scene bg black with fade
                        scene bg granica with fade

                    if timer >= 1800 and timer <= 2640:
                        scene bg black with fade
                        scene bg granica2 with fade

                    if timer >= 3240 and timer <= 4080:
                        scene bg black with fade
                        scene bg granica3 with fade

                    if timer >= 4680 and timer <= 5520:
                        scene bg black with fade
                        scene bg granica4 with fade

                    if timer >= 6120 and timer <= 6960:
                        scene bg black with fade
                        scene bg granica5 with fade

                    if timer >= 7560 and timer <= 8400:
                        scene bg black with fade
                        scene bg granica6 with fade

                    if timer >= 9000 and timer <= 9840:
                        scene bg black with fade
                        scene bg granica7 with fade

                    if timer >= 10440 and timer <= 11280:
                        scene bg black with fade
                        scene bg granica8 with fade

                    if timer > 1200 and timer < 1800:       
                        scene bg black with fade
                        scene bg granica_noc with fade

                    if  timer > 2640 and timer < 3240:
                        scene bg black with fade
                        scene bg granica2_noc with fade

                    if  timer > 4080 and timer < 4680:
                        scene bg black with fade
                        scene bg granica3_noc with fade

                    if  timer > 5520 and timer < 6120:
                        scene bg black with fade
                        scene bg granica4_noc with fade

                    if  timer > 6960 and timer < 7560:
                        scene bg black with fade
                        scene bg granica5_noc with fade

                    if  timer > 8400 and timer < 9000:
                        scene bg black with fade
                        scene bg granica6_noc with fade

                    if  timer > 9840 and timer < 10440:
                        scene bg black with fade
                        scene bg granica7_noc with fade

                    if  timer > 11280:
                        scene bg black with fade
                        scene bg granica8_noc with fade
                    
                    show auto zorder 9
                    
                    show gamma neutral zorder 10 at center
                    show trump neutral zorder 10:
                        xalign 1.1
                        yalign 1.0

                    gamma "Ktoś idzie… Czy to mechanik??"

                    trump "Oby, bo to auto mi działa na nerwy"
                    trump "Jeszcze chwila i sam się nim zajmę."

                    gamma "Nie ruszaj SUBARU!!!" with vpunch
                    gamma "On tak bardzo cierpi!"

                    show gamma neutral right zorder 10 

                    gamma "No już Subaru już, spokojnie jesteś już bezpieczny"
                    gamma "Tym razem nie umrzesz obiecuję Ci"

                    if eminem_sojusznik == 0:
                        show kazuma neutral right zorder 10 at slightleft
                        show luszcz neutral zorder 10 at left
                        show gamma neutral right zorder 10 at slightright

                        kazuma "Kobieto oddawaj nasz chajs!!!"

                        gamma "Niczego nie oddam wszystko moje!!!"
                        
                        trump "Ah.. dobra rozumiem"
                        trump "Nie chce mi się. Idę jeść koty z kolegami i gwałcić małe dzieci na wyspie"

                        hide trump

                        gamma "Myślicie że można sobie od tak wejść do kasyna i zarobić!! Kasyno jest do zabawy a nie do zarabiania!"

                        luszcz "Nieprawda!!! Do zabawy i do zarabiania!"

                        kazuma "Dawaj chajs!"

                        gamma "Po moim trupie!"
                        gamma "Jeśli chcecie je dostać, najpierw musicie się przedrzeć przeze mnie!"

                        jump after_fight171
                        jump fight171
                    
                    else:
                        show kazuma neutral right zorder 10:
                            xalign 0.18
                            yalign 1.0
                        show luszcz neutral zorder 10:
                            xalign -0.1
                            yalign 1.0
                        show gamma neutral right zorder 10 at slightright

                        kazuma "Kobieto oddawaj nasz chajs!!!"

                        show eminem neutral right zorder 10:
                            xalign 0.4
                            yalign 1.0

                        cid "Chwila czy ty przypadkiem nie jesteś eeeee..."
                        cid "A jak Alfa..."
                        cid "B jak Beta..."
                        cid "C jak Ciota..."
                        cid "D jak Delta..."
                        cid "E jak Epsilon..."
                        cid "Chwila, chwila, bo Eta też jest na E..!"
                        cid "Coś zjebałem chyba trudno idźmy dalej"
                        cid "F jak Duży Męski Fiut"
                        
                        luszcz "Ahhh jak ja kocham duże męskie fiuty"

                        cid "Cichaj! Ja tu liczę!"
                        cid "..."
                        cid "No i zapomniałem wielkie dzięki!!!"
                        cid "Teraz muszę od początku liczyć"
                        cid "Okej dobra więc, A jak Alfa..."
                        cid "B jak Be... chwila stop przecież są jeszcze te polskie znaczki!"
                        cid "dobra to teraz Ą"
                        cid "Ą jak eeee yyyy eeee..."
                        cid "Ą jak ąaha!"
                        cid "Ahh ta głupia plaża"
                        cid "zawsze zapominam ją obstawić"
                        cid "ale no wracając"
                        cid "B jak Beta..."
                        cid "C jak Ciota..."
                        cid "Ć jak Ćeská republika..."
                        cid "albo po prostu pepiczki"
                        cid "D jak Delta..."
                        cid "E jak Epsilon lub Eta"
                        cid "ewentualnie Epstein"
                        cid "Ę jak Ękaliptus"
                        cid "F jak Duży Męski Fiut"

                        luszcz "koch..."

                        cid "G jak Gamma!"
                        cid "Tak! Już pamiętam ty jesteś Gamma co nie!?"

                        gamma "..."
                        gamma "A ty kurwa skąd to wiesz!?"
                        gamma "Pewnie jesteś z kultu Diablosa!"

                        cid "Nie, nie gamma spójrz to ja Cid twój, twój wybawca"

                        gamma "Mój wybawca nie żyje!"

                        cid "Jak nie żyje, przecież tu jestem spójrz no stoję tu przed tobą!"

                        gamma "Kłamiesz!"
                        gamma "Mój pan, mój wybawca miał dwie ręce i mega aure!"

                        luszcz "..."

                        gamma "I i i do tego nigdy przenigdy nie zapomniałby mojego imienia!"

                        cid "Ej no weź no czasami się to zdarza..."
                        cid "Nie masz czasami tak, że podchodzisz do kogoś zagadać, ale akurat wyleciał ci jego numer z głowy więc krzyczysz “erschießen!” i odchodzisz?"

                        gamma "..."
                        gamma "Nie? Ktoś tak ma na seriO!?"

                        cid "..."
                        cid "Dobra, ale no musisz mi uwierzyć!"

                        gamma "Nie!"
                        gamma "Nigdy Ci nie uwierzę!"
                        gamma "Pewnie to ty zabiłeś mojego wybawce i dlatego, aż tyle wiesz!"
                        gamma "Pomszczę cię mój Panie!"

                        trump "Ah.. dobra rozumiem"
                        trump "Nie chce mi się. Idę jeść koty z kolegami i gwałcić małe dzieci na wyspie"
                        hide trump
                        show gamma neutral right zorder 10 at right 

                        cid "..."
                        cid "Ehhh chyba czas na walkę"

                        $ kazuma_sojusznik = 1
                        $ liczba_sojusznikow += 1

                        jump after_fight171
                        jump fight171
                    
                    label after_fight171:
                        $ kazuma_sojusznik = 0
                        $ liczba_sojusznikow -= 1
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 0
                        $ granica = 1
                        if timer >= 360 and timer <= 1200:       
                            scene bg black with fade
                            scene bg granica with fade

                        if timer >= 1800 and timer <= 2640:
                            scene bg black with fade
                            scene bg granica2 with fade

                        if timer >= 3240 and timer <= 4080:
                            scene bg black with fade
                            scene bg granica3 with fade

                        if timer >= 4680 and timer <= 5520:
                            scene bg black with fade
                            scene bg granica4 with fade

                        if timer >= 6120 and timer <= 6960:
                            scene bg black with fade
                            scene bg granica5 with fade

                        if timer >= 7560 and timer <= 8400:
                            scene bg black with fade
                            scene bg granica6 with fade

                        if timer >= 9000 and timer <= 9840:
                            scene bg black with fade
                            scene bg granica7 with fade

                        if timer >= 10440 and timer <= 11280:
                            scene bg black with fade
                            scene bg granica8 with fade

                        if timer > 1200 and timer < 1800:       
                            scene bg black with fade
                            scene bg granica_noc with fade

                        if  timer > 2640 and timer < 3240:
                            scene bg black with fade
                            scene bg granica2_noc with fade

                        if  timer > 4080 and timer < 4680:
                            scene bg black with fade
                            scene bg granica3_noc with fade

                        if  timer > 5520 and timer < 6120:
                            scene bg black with fade
                            scene bg granica4_noc with fade

                        if  timer > 6960 and timer < 7560:
                            scene bg black with fade
                            scene bg granica5_noc with fade

                        if  timer > 8400 and timer < 9000:
                            scene bg black with fade
                            scene bg granica6_noc with fade

                        if  timer > 9840 and timer < 10440:
                            scene bg black with fade
                            scene bg granica7_noc with fade

                        if  timer > 11280:
                            scene bg black with fade
                            scene bg granica8_noc with fade
                        
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            play music "audio/music/pole.mp3"
                        else:
                            play music "audio/music/pole_noc.mp3"
                        
                        show auto zorder 9
                        show gamma dead zorder 11
                        
                        if eminem_sojusznik == 0:
                            show kazuma neutral zorder 11 at slightright
                            show luszcz neutral zorder 11 at left
                            
                            luszcz "Łatwo z tobą!!"

                            gamma "Chuj wam w dupe!!"

                            play sound "audio/sfx/chanuka.mp3" 
                            show fir zorder 10
                            show kazuma neutral zorder 11 at right
                            show luszcz neutral right zorder 11 at slightright

                            $ renpy.pause(1.0)
                            hide fir

                            play sound "audio/sfx/boom.mp3" 
                            show bu zorder 10

                            $ renpy.pause(0.1)
                            hide bu
                            hide auto

                            show auto2 zorder 9

                            luszcz "Ej wtf po co to było???"

                            kazuma "Uczciwie cię zabiliśmy!"

                            gamma "Nie ma tak że ja przegrywam a inni zyskują!"
                            gamma "Gnijcie sobie frajerzy!"

                            show gamma dead2
                        
                        else:  
                            show kazuma neutral zorder 11 at slightright
                            show luszcz neutral zorder 11 at left
                            
                            luszcz "Łatwo z tobą!!"

                            gamma "Chuj wam w dupe!! Nie będzie kult diablosa pluł nam w twarz!"

                            play sound "audio/sfx/chanuka.mp3" 
                            show fir zorder 10
                            show kazuma neutral zorder 11 at right
                            show luszcz neutral right zorder 11 at slightright

                            $ renpy.pause(1.0)
                            hide fir

                            play sound "audio/sfx/boom.mp3" 
                            show bu zorder 10

                            $ renpy.pause(0.1)
                            hide bu
                            hide auto

                            show auto2 zorder 9

                            luszcz "Ej wtf no i po co to było???"

                            kazuma "Uczciwie cię zabiliśmy!"

                            gamma "Nieprawda! Wy z Kultu Diablosa nie jesteście uczciwi!"

                            luszcz "Ale my nie jesteśmy z kultu diablosa..."

                            gamma "Nie kłam, ja wiem i będe walczyła z wami do końca życ..."
                        
                            show gamma dead2

                            luszcz "No i nie żyje"
                        
                        kazuma "Gupia dziwka…"

                        luszcz "Gszegorz nas zamordóje…"
                        luszcz "… "

                        show grzesiu neutral zorder 11 at left

                        grzes "Ej panowie sory że tak późno"
                        grzes "Odbierałem makowce"
                        grzes "Jak tam pieniądze?"

                        kazuma "Kurrrrwaaaa…."

                        luszcz "Grzegorz, stłukliśmy ją na kwaśne jabłko, ale zamiast przyjąć Gamma postanowiła spalić auto z całym chajsem…"
                        luszcz "Zrobiliśmy co mogliśmy!"

                        grzes "Hm…"
                        grzes "Tak bardzo jak uwielbiam udupiać innych dla własnego zysku…"
                        grzes "Nigdy nie rozumiałem krzywdzenia ludzi bez powodu."
                        grzes "Przecież i tak już nie żyje… na co jej to było…"
                        grzes "…"
                        grzes "… … …"
                        grzes "Ej panowie."
                        grzes "Może… wykorzystajmy jej ciało"

                        menu:
                            "{b}nie?????{/b}":
                                luszcz "Co ty pierdolisz??? Fuj???"

                                kazuma "Nooo…. Dosłownie…"
                            
                            "{b}oki{/b}":
                                luszcz "W sumie czemó nie hehe"

                                kazuma "Ahh zawsze chciałem czegoś takiego spróbować"

                                grzes "Nie, boże, debile"

                        grzes "Nie o to mi chodziło idioci"
                        grzes "Mam kontakty"
                        grzes "Możemy sprzedać jej ciało na części"
                        grzes "Nikt się nie dowie."
                        grzes "A część zysku oddam ci, Kazuma, na spłacenie tamtego długu za który cię ścigają."

                        kazuma "Mam na imie Kazuma."

                        grzes "Wiem."
                        grzes "Wszyscy wygrywają. Podoba wam się taki plan?"

                        kazuma "No dla mnie cacy"

                        luszcz "Ja tó jestem dla kolegi więc oczywiście że tak."

                        grzes "To w takim razie panowie. Zmywamy się."
                        grzes "Zajmę się samochodem zanim Pomarańcza wróci."
                        grzes "Oczy widzą uszy słyszą usta milczą."

                        luszcz "Jesteś ostatnią osobą do muwienia takich rzeczy, ale spoko."

                        kazuma "To siema."

                        play sound "audio/sfx/traveling.mp3" 
                        $ rynek = 0
                        $ sloneczna = 0
                        $ alejka = 0
                        $ parking = 0
                        $ wolbromska = 0
                        $ bohaterow_wrzesnia = 0
                        $ lipowa = 1
                        $ granica = 0
                        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                            scene bg black with fade
                            scene bg lipowa with fade
                        else:
                            scene bg black with fade
                            scene bg lipowa_noc with fade
                            play music "audio/music/pole_noc.mp3"
                        
                        show luszcz neutral at slightleft
                        show kazuma neutral at slightright

                        kazuma "Uff… zasrany cwel z tego karalucha ale przynajmniej rozwiązał sprawę…"

                        luszcz "Będę mósiał go naprostować jak to wszystko się skończy"
                        luszcz "Nie wiedziałem że się zrobił takim rozwydrzonym kapósiem"

                        kazuma "Ej to, póki dalej jestem na oczach policji, mogę ci dalej towarzyszyć?"
                        kazuma "Potrzebuję kogoś kto mnie będzie krył, plus, chętnie ci pomogę w ratowaniu Skały."

                        menu:
                            "{b}Chodź ze mną{/b}":
                                luszcz "Dobra, nie będę kłamał, twóje UMIEJĘTN0ŚCI są dość przydatne."

                                kazuma "cnie"

                                luszcz "To możesz do mnie dołączyć."

                                kazuma "sigmastycznie."

                                $ kazuma_sojusznik = 1
                                $ liczba_sojusznikow += 1
                                $ kazuma_wybory = 2
                                $ kazuma_social_link = 3
                                                            
                            "{b}Dasz sobie radę{/b}":
                                luszcz "Oj tam dasz sobie radę"
                                luszcz "Do końca tygodnia psy tu jeszcze nie będą grasowały, a do wtedy Grzesio na pewno coś ogarnie"

                                kazuma "No w sumie rel"
                                kazuma "Niech będzie"
                                kazuma "To do zobaczenia kolego ziomek fam kicia bratku towarzyszu kamracie."

                                luszcz "Baj baj"

                                $ kazuma_wybory = 2
                                $ kazuma_social_link = 3
                        
                        hide kazuma 
                        hide luszcz
                        
                        jump lipowa2
                                                























