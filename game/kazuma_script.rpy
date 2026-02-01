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
            scene bg kasyno3
            show kazuma czapka at center
            ""


