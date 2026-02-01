default ruchanie = 0
default nie_ruchanie = 0
default gnat = 0
default tarczownik_dzien = 0

label tarczownik:
    label tarczownik1:
        $ tarczownik_social_link = 1
        if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
            play music "audio/music/pole.mp3"
        else:
            play music "audio/music/pole_noc.mp3"
        scene bg wolbromska with fade
        show luszcz neutral zorder 11 at left

        $ renpy.pause(0.5)

        show pies woof at center:
            xalign 1.5
            yalign 1.0
            easeout 0.6 xalign 0.7
        
        $ renpy.pause(0.5)

        pies "woof woof XP rawr"
        luszcz "O kurde furas na wolności"

        show pies woof at center:
            xalign 0.7
            yalign 1.0
            easeout 0.6 xalign -0.5

        $ renpy.pause(1.0)

        show tarczownik neutral at slightright:
            xalign 1.5
            yalign 1.0
            easeout 0.6 xalign 0.7
        
        $ renpy.pause(0.5)

        tarczownik "Ej ty! Widziałeś Raphtalie?"

        luszcz "Tego psa?"

        tarczownik "To bardziej coś typu szopa ale tak"

        luszcz "Pobiegł na lewo, a potem w prawo"

        tarczownik "Okej dzięki"

        show tarczownik neutral at center:
            xalign 0.7
            yalign 1.0
            easeout 0.6 xalign -0.5
        
        $ renpy.pause(0.5)

        luszcz "W sumie morznaby za nim pobiec"

        menu:
            "{b}Pobiegnij za nim (5h){/b}":
                $ timer += 300
                show luszcz neutral at center:
                    xalign 0.0
                    yalign 1.0
                    easeout 0.6 xalign -0.5
            
                $ renpy.pause(1.0)

     
            "{b}Nie chce mi się{/b}":
                luszcz "Niech sobie frajer sam lata za swoim psem"

                $ tarczownik_wybory = 0
                $ tarczownik_social_link = 10
                hide luszcz
                jump wolbromska2

        play music "audio/music/natura.mp3"
        scene bg black with fade
        scene bg las with fade

        show pies woof at right

        $ renpy.pause(0.5)

        show tarczownik neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.4
        
        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.05

        tarczownik "Raptylja! Do nogi!!!"

        pies "Hał hał xd"

        tarczownik "Wracaj tu!!"

        luszcz "ale mentzonce bieganko"

        show pies woof at center:
            xalign 1.0
            yalign 1.0
            easeout 0.6 xalign 1.5

        $ renpy.pause(0.3)

        show tarczownik neutral at center:
            xalign 0.4
            yalign 1.0
            easeout 0.6 xalign 1.5
        
        show luszcz neutral at center:
            xalign 0.05
            yalign 1.0
            easeout 0.6 xalign 1.5
        
        $ renpy.pause(1.0)

        play music "audio/music/portal.mp3"
        scene bg portal

        show pies woof at center:
            xalign -0.5
            yalign 1.0
            easeout 0.8 xalign 1.1

        $ renpy.pause(0.5)

        show tarczownik neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.4
        
        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.05
        
        $ renpy.pause(0.5)

        pies "hmm… :pp"

        tarczownik "Nie waż się!"

        luszcz "Tu zawsze był jakiś portal?"

        tarczownik "No jakoś od 1984"
        tarczownik "Zobacz sobie na mapach"
        tarczownik "Google"

        luszcz "Okej później"

        pies "dobra wskakuje xD"

        tarczownik "Raphtalia!!!!!!"
        
        show pies woof:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide pies

        $ renpy.pause(0.05)

        tarczownik "Boże…"
        tarczownik "Raaah!!!!! Nie wytrzymam bez niej!! Była moją dog girl!!!! Czemu wszyscy mnie zostawiają!!"

        luszcz "Idź po nią jak ci tak zalerzy"

        tarczownik "Jest mały problem"
        tarczownik "Ten portal prowadzi do nieskończonej ilości uniwersów, szukanie jej będzie jak igły w stogu siana"
        tarczownik "Ale z drugiej strony… nie mam nic do stracenia"

        luszcz "A czemó tak od ciebie uciekła..?"

        tarczownik "Dałem jej spróbować cytryny żeby zobaczyć jej reakcję jak w tych filmikach ze zwierzątkami"
        tarczownik "Mogłem przewidzieć że to gówno to było ai…"
        tarczownik "Weszła w szał i wybiegła z domu"

        luszcz "Głópie w ciól"
        luszcz "Ale przykre"

        tarczownik "Ehh… ide sie zabic…"

        luszcz "Nie no bez przesady"
        luszcz "Czy gdybym poszedł z tobą poszukać to zostaniesz przy żywych?"

        tarczownik "Jeśli tam od czegoś nie zginiemy to tak"

        luszcz "(Czy chcę tam z nim wskakiwać…?)"

        menu:
            "{b}Czy chcę wskoczyć do portalu?{/b}"

            "{b}Tak{/b}":
                luszcz "Dobra to ty pierwszy"
                tarczownik "Okej"

            "{b}Nie{/b}":
                luszcz "W takim razie pora umierać"
                tarczownik "Rel"

                show tarczownik gun
                $ renpy.pause(0.1)
                with vpunch
                play sound "audio/sfx/gun.mp3"
                $ renpy.pause(0.1)
                show tarczownik dead

                luszcz "Ups.."
                luszcz "To był rzarcik…"
                luszcz "Anyway"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                $ tarczownik_wybory = 10
                $ tarczownik_social_link = 10
                jump wolbromska

        show tarczownik neutral at center:
            xalign 0.4
            yalign 1.0
            easeout 0.5 xalign 0.7
        
        $ renpy.pause(0.5)

        show tarczownik neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide tarczownik

        $ renpy.pause(0.05)

        luszcz "okej..."

        show luszcz neutral at center:
            xalign 0.05
            yalign 1.0
            easeout 0.5 xalign 0.7
        
        $ renpy.pause(0.5)

        show luszcz neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide luszcz

        $ renpy.pause(0.05)

        scene bg inportal with pixellate
        play music "audio/music/inportal.mp3"

        luszcz "Ziuuuuu…"
        luszcz "Ej a jak masz na imie"

        tarczownik "Naofumi"

        luszcz "fajnie a ja Łuszczu"

        pies "rawr!!"

        tarczownik "Słyszałeś TO ONA!!!"

        luszcz "To chyba w tom strone..!"

        scene bg cult with pixellate
        play music "audio/music/cult.mp3"
        show luszcz neutral at slightleft
        show tarczownik neutral at slightright

        tarczownik "ałć… gdzie jesteśmy?"

        luszcz "Jakaś wioska..?"

        show owca neutral at right
        show luszcz neutral at left
        show tarczownik neutral right at center

        owca "A co to takiego?"
        owca "Witajcie, przybysze! Skąd i dlaczego tu się pojawiliście?"
        owca "Czy ten portal będzie dało się przestawić? Planowałam tu coś postawić…"

        luszcz "Pochodzimy ze Skały. Szukamy kobiety z szopowatymi ószami zachowującej się jak pies"

        tarczownik "Oddaj nam moją psiapsi!!!!"
        
        owca "Hm…"
        owca "…"
        owca "Jest szansa że mamy stworzenie o którym mówicie"
        owca "Znajduje się w tej nie podejrzanej świątyni rytualnej"

        tarczownik "Nie idziemy tam!! To podstęp!!"

        menu:
            "{b}It's NOT a Trap{/b}":
                luszcz "Nie słuchaj go, ja tobie ufam"

                tarczownik "Nie, to TY jej nie słuchaj, nie ufam jej!"

                show tarczownik tarcza at slightleft
                play sound "audio/sfx/shield.mp3"

                $ wypadek2 = 1

                "{i}*tarczownik bije cię bokiem tarczy w kostkę*{/i}"
    
                show luszcz kuca_smutny
                show tarczownik neutral at center

                luszcz "AŁAAAA"
                if gotka_szpan > 0 or gotka_social_link > 0:
                    luszcz "(hm…. Będę mógł z tym iść do gotki… hehe)"
                luszcz "AŁA CZEMÓ MNIE BIJESZ!?"

                tarczownik "To dla twojego dobra… idę odbić Raphtalię, jeśli tam jest"
                tarczownik "Ty tu poczekaj…"

                hide tarczownik 

                owca "What the sigma"
                owca "Ja sobie pójdę rogueliekować"

                hide owca

                luszcz "Wtf… i tak nie wstanę, idę lulu"

                scene bg black with fade
                "*po jakimś czasie Łuszcz się budzi*"
                scene bg cult with fade

                show luszcz neutral at slightleft
                show tarczownik neutral at slightright

                tarczownik "Hej, wreszcie się obudziłeś"

                luszcz "Ile tu lerzałem…? Co się stało..?"

                tarczownik "Nie za długo… zneutralizowałem cię bo prawie dałeś się wykorzystać"
                tarczownik "Potem poszedłem do świątyni w której miała być Raphtalia, ale zamiast tego były obrzędy dziadów"
                tarczownik "Później pojawił się wielki potwór z mackami i wykorzystał mnie seksualnie"
                tarczownik "Szczerze, czuję się trochę wykorzystany przez ciebie"
                tarczownik "Mogłeś mi pomóc w tym wszstkim a nie takie hop siup bum tarara"

                luszcz "Weź to ty mnie walnąłeś"

                tarczownik "Dobra nie gadaj tam, tylko spadamy"
            
            "{b}It's a Trap{/b}":
                luszcz "Czy mogłabyś ją stamtąd zawołać?"

                owca "…"
                owca "Pewnie, spróbuję"

                show owca neutral at center:
                    xalign 1.0
                    yalign 1.0
                    easeout 0.5 xalign 1.5
                
                $ renpy.pause(1.0)

                show owca neutral at center:
                    xalign 1.5
                    yalign 1.0
                    easeout 0.5 xalign 1.0

                $ renpy.pause(0.5)

                owca "Nie, mówi że nie wyjdzie bo jej głupio że mi nie ufacie"
                owca "Czy coś"

                tarczownik " A gdybyśmy ci zaufali to by wyszła"

                owca "No myślę że tak"

                tarczownik " To ja ci ufam"

                hide tarczownik
                show luszcz neutral at slightleft

                luszcz "Japierdziele…"
                luszcz "Dobra on się tam w najlepszym wypadku tylko obroni"
                luszcz "Muszę mó pomuc"

                scene bg dziady
                play music "audio/music/dziady.mp3"
                show prymon neutral:
                    xalign 1.08
                    yalign 1.0
                
                show kononowicz neutral:
                    xalign 0.93
                    yalign 1.0
                
                show obama neutral:
                    xalign 0.78
                    yalign 1.0

                show tarczownik lezy:
                    xalign 0.93
                    yalign 1.0
                
                show luszcz neutral at left

                kult "Ciemno wszędzie… głucho wszędzie…"

                tarczownik "Ej pomocy!! Rzucili się na mnie i recytują Dziady!!! To zdrada!!!"

                luszcz "WOW Kto by się spodziewał!!!"

                kult "Co to będzie… co to będzie…"

                scene bg dziady2
                show prymon neutral:
                    xalign 1.08
                    yalign 1.0
                
                show kononowicz neutral:
                    xalign 0.93
                    yalign 1.0
                
                show obama neutral:
                    xalign 0.78
                    yalign 1.0

                show tarczownik lezy:
                    xalign 0.93
                    yalign 1.0
                
                show luszcz neutral at left

                "{i}*hentai tentakle potwor delikatnie wychyla się z wyrwy w podłodze*{/i}"

                kult "mno wszędzie… ciemno wsz…"

                luszcz "musze użyć jakiegoś dobrego ruchu żeby zbić ich z tarczownika"

                kult "szędzie… co to będzie… c…"

                tentacle "hmmm, ale bym sobie wyruchał młodych mężczyzn"

                luszcz "Spinjitzu!! *wrżżżż*"

                show tarczownik neutral at slightleft
                play sound "audio/sfx/fighting.mp3"
                with hpunch
                "{i}*łuszczu zbija kultystów z tarczownika*{/i}"
                
                tarczownik "Boże dzięki"

                luszcz "Nie mów do mnie boże"
                luszcz "Chyba że masz na myśli…"
                luszcz "Boże wojny (walki (czas na walke))"

                $ tarczownik_sojusznik = 1
                $ liczba_sojusznikow += 1

                jump fight81
                label after_fight81:
                    $ tarczownik_sojusznik = 0
                    $ liczba_sojusznikow -= 1
                    scene bg dziady2
                    play music "audio/music/dziady.mp3"
                    show luszcz neutral at slightleft
                    show tarczownik neutral:
                        xalign 0.84
                        yalign 1.0

                    tentacle "nieeee nie chce wracać do arkham asylum nieeeee…"

                    diddy "hehe tęskniłem kochany 😜"

                    tentacle "nieeeeeeeeeeet……"

                    scene bg dziady
                    show luszcz neutral at slightleft
                    show tarczownik neutral:
                        xalign 0.84
                        yalign 1.0

                    tarczownik "To było takie traumatyczne nwm czy kiedykolwiek z tego wyjde"
                    tarczownik "byłem tak bardzo dotykany"

                    luszcz " To pszykre ale musimy stąd spadać"

                    scene bg cult
                    play music "audio/music/cult.mp3"
                    show luszcz neutral at slightleft
                    show tarczownik neutral:
                        xalign 0.84
                        yalign 1.0

                    tarczownik "ale szczerze to trochę już nastawiałem dupę szkoda że sie nie daliśmy"

                    luszcz "Lubisz dóże menskie kutasy"

                    show luszcz neutral at left
                    show tarczownik neutral right at center
                    show owca neutral at right

                    owca "Ej wracać!!"
                    owca "Chwilę byłam poroguelikeować i już wszystko obsrali!!"

                    luszcz "zmykamy"

        show tarczownik neutral right:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide tarczownik

        $ renpy.pause(0.1)

        show luszcz neutral at center:
            xalign 0.0
            yalign 1.0
            easeout 0.5 xalign 0.5
        
        $ renpy.pause(0.5)

        show luszcz neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)

        scene bg portal with pixellate
        show luszcz neutral at slightleft
        show tarczownik neutral at slightright
        play music "audio/music/portal.mp3"

        luszcz "hmm… Rzeczywiście zrobiło się niebezpiecznie…"

        tarczownik "No mówiłem"
        tarczownik "I ta Owca… nigdy więcej nie ufam liderom kultu.."
        tarczownik "Ale z ważniejszych spraw"
        tarczownik "Mam taką potężną chcicę"
        tarczownik "…"
        tarczownik "Byłbyś może..?"
        tarczownik "O JEZU MOJA DOG GIRL"
        tarczownik "MUSIMY JĄ ZNALEŹĆ ZAPOMNIAŁEM TAK TĘSKNIĘ"
        tarczownik "AAAAAAAAAAAAAA"

        $ tarczownik_dzien = 1

        label ruchaniez:
            menu:
                "{b}Nie będę się z tobą ruchał{/b}" if nie_ruchanie == 0:
                    luszcz "Nie będę się z tobą ruchał!"

                    tarczownik "TO NIE JEST WAŻNE!!! JUŻ O TYM NIE MYŚLE!!"

                    $ nie_ruchanie = 1
                    jump ruchaniez

                "{b}Jestem otwarty na niezobowiązujący seks{/b}" if ruchanie == 0:
                    luszcz "jestem otwarty na niezobowiązujący seks"

                    tarczownik "POMYŚLIMY O TYM PO SPRAWIE ALE SPK"

                    $ ruchanie = 1
                    jump ruchaniez

                "{b}Możemy jej poszukać jeszcze jutro{/b}":
                    luszcz "Morzemy jej poszókać jeszcze jótro"

                    tarczownik "okej heh"
                    tarczownik "w ogóle wpadłem na pomysł"
                    tarczownik "moglibyśmy się tu spotkać jutro i spróbować znów jej poszukać"

                    luszcz "tak dobry pomysł. Zróbmy to. Widzimy się jutro"

                    tarczownik "Widzimy, Tłuszczu"

                    $ tarczownik_wybory = 1
                    $ tarczownik_social_link = 1
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska

    label tarczownik2:
        scene bg portal with fade
        play music "audio/music/portal.mp3"
        show luszcz neutral at slightleft
        show tarczownik neutral at right

        tarczownik "Witaj przyjacielu, jak się poczuwasz?"

        luszcz "Ile ty tu stałeś?"

        tarczownik "Kto rano wstaje ten dupy daje"

        luszcz "Ok rozumiem"

        tarczownik "Dobra dawaj do portalu, tym razem na pewno się uda"

        luszcz "for sure bratku"

        show tarczownik neutral at center:
            xalign 1.0
            yalign 1.0
            easeout 0.5 xalign 0.75
        
        $ renpy.pause(0.5)

        show tarczownik neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide tarczownik

        $ renpy.pause(0.1)

        show luszcz neutral at center:
            xalign 0.25
            yalign 1.0
            easeout 0.5 xalign 0.75
        
        $ renpy.pause(0.5)

        show luszcz neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide luszcz

        $ renpy.pause(0.1)

        scene bg gow with pixellate
        play music "audio/music/gow.mp3"
        show luszcz neutral at slightleft
        show tarczownik neutral at slightright
        
        nikt "hau hau wrrrrrrrr"

        luszcz "Słyszysz to..? To morze być ona!"

        tarczownik "Warto sprawdzić! Chodźmy do chatki"

        scene bg chatka
        play music "audio/music/chatka.mp3"
        show luszcz neutral at left
        show tarczownik neutral right at slightleft
        show ares neutral at right

        tarczownik "Ej patrz to Bóg wojny!"
        tarczownik "Ares!"

        luszcz "Chłopie o czym ty mówisz!"
        luszcz "To jest Mars"

        ares "Chłopaki obaj pieprzycie głupoty"
        ares "Przecież moje imie to…"
        ares "A nie, sory"
        ares "Ten z tarczą ma rację"
        ares "Witajcie, to ja, Ares"

        tarczownik "Słyszeliśmy dźwięki typu szczekanie, czy znasz może ich źródło..?"

        ares "Znam, znam jak swoje dziecko!"
        ares "Bo to jest moje dziecko :)"
        ares "Arteuszku, przyjdź no proszę!"

        arteuszek "Już idę, tatku!"

        menu:
            "{b}Twój syn jest furasem?{/b}":
                luszcz "Twuj syn jest furasem?"

                ares "Nie,"
                ares "Może, nie wiem"
                ares "Ale umie zrobić taki fajny trik"

                show arteuszek neutral at slightright

                arteuszek "Cześć tatku, co to za panowie?"

                ares "Ci relatywnie uprzejmi goście są ciekawi twoich sztuczek!"

                arteuszek "Tatku…"

                ares "Arteuszku pokaż gościom twoje sztuczki"

                arteuszek "Dobrze tatku…"

                show arteuszek wolf
                with hpunch

                ares "Brawo!!!"

                luszcz "👏👏👏"

                tarczownik "O jaki słodki piesek!"

                arteuszek "Tatku nie mogę oddychać…"
                
                ares "Zaraz cię zmienimy spowrotem"
                ares "Czy mogę wam w czymś jeszcze pomóc..?"
                ares "Może troszke piwka, albo moje ostrza chaosu?"

                menu:
                    "{b}Sześciopak Jaboli{/b}":
                        luszcz "Pilnie potrzebujemy sześciopaka jaboli"

                        tarczownik "Pychotka"

                        ares "Proszę bardzo"

                        if jabole == 0:
                            $ ile_item += 1
                        $ jabole += 6
                        "{i}6 Jaboli zostało dodane do ekwipunku{/i}"
                    
                    "{b}Ostrza Chaosu{/b}":
                        luszcz "Pilnie potrzebójemy twoich ostrzów chaosu!"

                        tarczownik "Oddajesz nam swoją broń od tak..?"
                        tarczownik "Nigdy bym nie oddał swojej tarczy!!"

                        ares "Oh to dla mnie nie problem"
                        ares "Mogę poprosić kowala o nowe na spokojnie"

                        $ ostrza_chaosu = 1
                        "{i}Ostrza Chaosu zostały dodane do ekwipunku{/i}"

                luszcz "Dobrze dziękójemy to bardzo tóff z waszej strony Aresie"

                ares "Do usług!"

                arteuszek "Tatku ja tu umieram…"
                arteuszek "Pomusz mi tatku…"

            "{b}Twój syn lubi wielkie męskie kutasy?{/b}":
                luszcz "Twój syn lubie wielkie męskie kutasy?"

                ares "Em… przepraszam?"

                tarczownik "Nie, czekaj"
                tarczownik "To może do czegoś prowadzić"
                tarczownik "Kolega pyta czy pan lubi duże męskie kutasy"

                ares "Nie twój interes?"

                luszcz "Nie, pytałem o to czy pański SYN lubi duże męskie kutasy"

                ares "Mój syn jest za młody na takie żarty"
                ares "Wypierdalać z mojego domu zanim się wkurwie"
                ares "Nie chcecie znać gniewu Boga wojny Aresa"

                show arteuszek neutral at slightright

                arteuszek "Tatku jestem, o co chodzi? Kim są ci panowie?"

                ares "za kilka sekund będą gore na naszej podłodze synu"

                tarczownik "Bożeee nie ponoszę odpowiedzialności za nic co przed chwilą powiedziałem chodźmy stąd!!!!"
                
                luszcz "Real"
        
        hide luszcz
        hide tarczownik
        $ renpy.pause(0.5)

        scene bg portal with pixellate
        show luszcz neutral at slightleft
        show tarczownik neutral at slightright
        play music "audio/music/portal.mp3"

        tarczownik "Nie wytrzymam zaraz…"
        tarczownik "Gdzie jest mój pies… tatuś potrzebuje swojego pieska…"
        tarczownik "Zastrzele się jak zaraz nie przyjdzie…"

        luszcz "(mam wrażenie że nie znajdziemy jej w tym big ahh wrzechświecie… pewnie już dawno zdechła)"
        luszcz "(Nie mogę tak marnować dni. Los skały ode mnie zależy.)"
        luszcz "(Co powinienem mu powiedzieć..?)"

        tarczownik "Jak coś to nie żartuje!!!! Zastrzele się tu na miejscu!!!"

        label debil:
            menu:
                "{b}jeśli masz pistolet to czemu z niego nie korzystasz?{/b}" if gnat == 0:
                    luszcz "Jeśli zawsze masz ze sobą gnata to czemu z niego nie korzystasz?"

                    tarczownik "NIe korzystaM? Hm?? MOgę skorzystać!!!! Tu i teraz!!!"

                    luszcz "Dobra nieważne cofam"

                    $ gnat = 1
                    jump debil
                
                "{b}Ja będę twoją psiapsi dog girl{/b}":
                    luszcz "Ja będę twoją psiapsi dog girl"
                    
                    tarczownik "Nie wierzę!"

                    luszcz "Serio będę"

                    tarczownik "I będziesz mi lojalny do końca życia?"

                    luszcz "Arz będziesz miał mnie dość"

                    tarczownik "A zmienisz zaimki na żeńskie..?"

                    luszcz "Nie no aż tyle to nie"
                    luszcz "Sorry"

                    tarczownik "A chociaż zawarcz dla mnie"
                    tarczownik "Zawarczysz dla mnie?"

                    show luszcz blush
                    luszcz "wrrrrr"
                    luszcz "wrrrrrr hau! Hau!"
                    luszcz "wrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"

                    tarczownik "Dzięki brachu"
                    tarczownik "Może dam radę z tym żyć"

                    luszcz "Tak… i wiesz co?"

                    show luszcz neutral
                    
                    luszcz "Potrzebuję cię w moim składzi"
                    luszcz "Słyszałeś że ksiądz próbuje włączyć Skałę do Krakowa?"

                    tarczownik "Troche wywalone"

                    $ tarczownik_sojusznik = 1
                    $ liczba_sojusznikow += 1
                    
                    tarczownik "Znaczy pomogę"
                    tarczownik "Ale to jest takie nieistotne"
                    tarczownik "A mógłbyś zrobić UwU"

                    play sound "audio/sfx/uwu.mp3"
                    show luszcz blush

                    luszcz "UwU <robi UwU>"

                    tarczownik "Good boooy"

                    luszcz "Ku chwale Skale"

                    $ tarczownik_wybory = 2
                    $ tarczownik_social_link = 2
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Obawiam się że nie przyjdzie…{/b}":
                    luszcz "Obawiam się, że nie przyjdzie…"
                    luszcz "Może poszła do szkoły dla psich dziewczyn i nauczyła się ludzkiego"
                    luszcz "I już nie szczeka ani nie emotkuje"
                    luszcz "I pracuje w korpo albo coś"
                    luszcz "I zrobiła sobie dzieci"
                    luszcz "I one szczekają a ona się złości i je wysyła na lobotomie"

                    show tarczownik gun
                    $ renpy.pause(0.1)
                    with vpunch
                    play sound "audio/sfx/gun.mp3"
                    $ renpy.pause(0.1)
                    show tarczownik dead

                    luszcz "Ups"
                    luszcz "Cóż…"

                    hide tarczownik
                    "{i}Łuszcz wrzuca ciało do portalu{/i}"

                    luszcz "Życie się toczy dalej……"

                    $ tarczownik_wybory = 10
                    $ tarczownik_social_link = 10
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska
                
                "{b}Nie masz psychy{/b}":
                    luszcz "Nie masz psychy"

                    tarczownik "Hm…"
                    tarczownik "To prawda, nie mam psychy"
                    tarczownik "…"
                    tarczownik "…"
                    tarczownik "…"
                    tarczownik "Ale jakby chwilkę nie myśleć o konsekwencjach-"

                    show tarczownik gun
                    $ renpy.pause(0.1)
                    with vpunch
                    play sound "audio/sfx/gun.mp3"
                    $ renpy.pause(0.1)
                    show tarczownik dead

                    luszcz "Oj…"
                    luszcz "Kurcze byłem pewien że to zadziała"
                    luszcz "Cóż…"

                    hide tarczownik
                    "{i}Łuszcz wrzuca ciało do portalu{/i}"

                    luszcz "Życie się toczy dalej……"

                    $ tarczownik_wybory = 10
                    $ tarczownik_social_link = 10
                    
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump wolbromska

            

