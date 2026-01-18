define burmistrza1 = 0
define burmistrzkill = 0
define burmistrzzbroja = 0

label burmistrz:
    label burmistrz1:
        $ burmistrz_social_link = 1
        play music "audio/music/senat.mp3"
        scene bg urzad_gminy with fade
        show burmistrz neutral at slightright
        show luszcz neutral at left

        burmistrz "...i ja mu wtedy mówię Grzegorz, to twoja wielka szansa, “Potop” nie kreci się co roku"
        burmistrz "I dzięki mnie zagrał"

        all "Ha ha ha ha, brawo panie burmistrzu"

        burmistrz " A po za tym, uważam że Kartagina musi zostać zniszczona"

        play sound "audio/sfx/cisza.mp3"

        "{i}*cisza na sali*{/i}"

        play sound "audio/sfx/klaskanie.mp3"

        luszcz "Brawo i to jest bórmistż, na kturego głosowałem"

        rand "Ale ty masz 18 lat od 6 dni dopiero…"
        rand "Nie mogłeś głosować w poprzenich wyborach"

        luszcz "Cisza!!!" with vpunch
        luszcz "Ludzie przed chwilą burmistrz wygłosił płomienną przemowę, a wy Ludzkie śmieci byś krztyny rozsądku, ani pomyślunku postanowiliście ją olać"

        "{i}*Gniewne okrzyki na sali*{/i}"

        all "Ukrzyżować go!"

        luszcz "Wy, wy podłe kreatury bez przyszłości. Zniszczenie Kartaginy to jedyna szansa na rozwój skały!"

        luszcz "Będziecie państwo wisieć!"

        hide luszcz

        "{i}*straż marszałkowska wyprowadza Łuszcza na zewnątrz{/i}"

        luszcz "Wspomnicie jeszcze słowa burmistrza, gdy wróg stanie u naszych bram!"

        scene bg urzad_gminy2

        play sound "audio/sfx/rzut.mp3"
        play music "audio/music/pole.mp3"
        with hpunch

        $ renpy.pause(0.5)

        show luszcz neutral at center

        luszcz "Ehhhh, politycy nigdy się nie zmienią"

        show burmistrz neutral at slightright
        show luszcz neutral at slightleft

        burmistrz "Nic ci nie jest młody?"
        burmistrz "Nieźle, Ciebie poturbowali"

        luszcz "Nic mi nie jest panie burmistrzu"
        luszcz "Taka jest cena walki o wolność"

        burmistrz "Oh, gdyby tylko wszyscy obywatele Skali, byli tak mądrzy i oddani sprawie jak ty…"
        burmistrz "Ale wracając, mam dla Ciebie ofertę…"
        burmistrz "Czy chciałbyś może w imieniu miasta zająć rozmieszczeniem ochotniczej straży pożarnej?"

        luszcz "Nie raczej nie…"

        burmistrz "Świetnie, to przyjdź na plac budowy przy ulicy Słonecznej to ci pokaże, gdzie powstanie centrum szkolenia nowych strażaków!"
        burmistrz "Do zobaczenia na placu"

        hide burmistrz
        show luszcz neutral at center

        luszcz "Ehhh, znów się w coś wplątałem"

        $ burmistrz_social_link = 1
        if rynek == 1:
            jump rynek
        if sloneczna == 1:
            jump slonneczna 
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

    label burmistrz2:
        $ burmistrz_social_link = 2        
        scene bg plac with fade
        show burmistrz neutral at slightright
        show luszcz neutral at slightleft

        burmistrz "O przyszedłeś w takim razie bez przedłużania opowiem Ci o moich planach"

        scene bg black with fade
        "{i}2 godziny bajdużenia później{/i}"
        scene bg plac with fade
        show burmistrz neutral at slightright
        show luszcz neutral at slightleft

        burmistrz "I dokładnie w tym oto miejscu powstanie całkowicie nowe, zautomatyzowane centrum szkoleniowe dla strażaków"

        luszcz "Ludzie, ale tu przecież niczego nie ma"

        show nemeczek neutral at center
        show burmistrz neutral at right
        show luszcz neutral at left

        nemeczek "Jak śmiesz tak mówić, to jest nasza ojczyzna, nasz plac broni"
        nemeczek "i my będziemy o nią walczyć"
        nemeczek "nawet jeśli trzeba będzie walczyć na dwa fronty"

        luszcz "Chwila, chwila jakie dwa fronty?!?"

        nemeczek "ahh, bo wy nie wiecie"
        nemeczek "naszą piękną republikę zaatakowała zdradziecko Kartagina"
        nemeczek "i teraz nasi żołnierze giną na froncie powstrzymując napór kartagińczyków"
        nemeczek "Oooo, a, a, a gdybyście nam pomogli"
        nemeczek "to mogłoby odmienić losy wojny…"
        nemeczek "proszę pomóżcie nam, dam wam wszystko o co poprosicie"

        menu:
            "{b}Pomożemy za darmo{/b}":
                luszcz "Nie musisz nas przekonywać do walki z Kartaginą"
                luszcz "My już od dawna ostrzegaliśmy przed nią wszystkich"

                burmistrz "Dokładnie tak, walka z Kartaginą to nasz obowiązek"
                burmistrz "Możesz na nas liczyć generale"

            "{b}Pomożemy za małą zachętą{/b}":
                luszcz "Chętnie wam pomogę, ale nie za darmo"
                luszcz "Za moją pomoc oczekuję, iż dostanę najlepsze uzbrojenie jakie posiadacie"

                nemeczek "Najlepsze?!?"

                burmistrz "Nie przesadzasz trochę młodzieńcze?"
                burmistrz "Oni nie mają za dużo uzbrojenia"
                burmistrz "Na pewno chcesz zażądać ich najlepszej zbroji"

                menu:
                    "{b}Tak{/b}":
                        luszcz "Podjełem swojom decyzje"

                        nemeczek "Dobrze dostaniesz swoje uzbrojenie"

                        $ klata_liczba += 1
                        $ burmistrzzbroja = 1
                        if luszcz_klata == 0 and urban_klata == 0 and zyd_klata == 0 and kazuma_klata == 0 and tarczownik_klata == 0 and eminem_klata == 0:
                            $ luszcz_klata = 1
                            $ urban_klata = 1
                            $ zyd_klata = 1
                            $ kazuma_klata = 1
                            $ tarczownik_klata = 1
                            $ eminem_klata = 1

                        "{i}*Diamentowa Klata została dodana do ekwipunku*{/i}"

                        nemeczek "No, a teraz ruszajmy skopać parę Kartagińskich pośladów"
                
                    "{b}Nie{/b}":
                        luszcz "Dobra, dobra pomogę wam za darmo"

                        nemeczek "I taką postawę to ja rozumiem żołnierzu"
                        nemeczek "No, ale teraz koniec z pogaduchami, mamy parę Kartagińskich pośladów do skopania"

            "{b}Sorki, ale nie…{/b}":
                luszcz "Sorki ale nie jestem, aż tak delulu, by bawić się na jakimś rozjebanym placu w wojnę z jakimiś bachorami"

                burmistrz "jak śmiesz tak mówić!"
                burmistrz ",przecież Kartagina to nasz największy wróg"
                burmistrz "Nie to mówiłeś podczas swojej bohaterskie wypowiedzi w ratuszu?"

                luszcz "Może i tak mówiłem, ale to nie oznacza, że to JA muszę walczyć z Kartaginą"
                luszcz "Jak chcesz to idź walczyć, nie powstrzymuję Cię"
                luszcz "Nawet będę ci kibicował"
                luszcz "Ale ja ruszać dupy nie zamierzam"

                burmistrz "Wiesz co?, wiesz co? Tak zrobię"
                burmistrz "zobaczysz poprowadzę tych dzielnych wojowników do zwycięstwa"

                nemeczek "Za mną żołnierzu"

                hide nemeczek
                hide burmistrz 
                show luszcz neutral at center

                luszcz "..."
                luszcz "wariaty"

                $ burmistrz_wybory = 0
                $ nemeczek_wybory = 0
                $ burmistrz_social_link = 10

                play music "audio/music/pole.mp3"
                jump sloneczna 
                
        scene bg black with fade
        "{i}*po przedarciu się przez linię frontu udało nam się dotrzeć do głównej kwatery dowodzenia sił republiki*{/i}"
        play sound "audio/sfx/traveling.mp3" 
        play music "audio/music/plac.mp3"
        scene bg kwatera with fade

        show nemeczek neutral at right
        show burmistrz neutral right at left
        show luszcz neutral at slightleft
        show dzieci:
            xalign 0.55
            yalign -0.5

        nemeczek "Towarzysze bracia i siostry, w dniu dzisiejszym zdradzieckie oddziały Kartagińczyków wkroczyły na naszą ziemię"
        nemeczek "Gwałcą nasze kobiety i rabują nasze domy nie przejmując się prawem międzynarodowym"
        nemeczek "Nie możemy na to pozwolić!"
        nemeczek "Musimy odeprzeć napór najeźdźcy!"
        nemeczek "Musimy zapobiec temu okrucieństwo!"
        nemeczek "To nasz życiowa misja"
        nemeczek "Misja by chronić słabszych przed silniejszymi"
        nemeczek "By ratować tych, którzy sami się nie uratują"
        nemeczek "Dlatego teraz wykażcie się swoim męstwem i ruszajcie na front"
        nemeczek "Jesteście ostatnią nadzieją republiki!"

        all "Tak jest panie generale!"

        hide dzieci
        "{i}*żołnierze opuścili kwaterę i wyruszyli na front*{/i}"

        nemeczek "Ale jebłem przemówienie"
        nemeczek "Ciekawe czy ktoś ogarnął, że wygenerował mi je chat gpt"

        luszcz "eeee nemeczku…"

        nemeczek "Panie generale"

        luszcz "Panie generale…"
        luszcz "co MY właściwie mamy robić?"

        nemeczek "A tak właśnie zapomniałem"
        nemeczek "otóż potrzebuję was abyście załatali dziurę we froncie na południu"
        nemeczek "z racji korzystnego położenia naszej ojczyzny jest to jedyny kierunek, z którego Kartagińczycy mogą nas zaatakować"

        burmistrz "Jak to jest niby możliwe?"
        burmistrz "Przecież nie ma szans, że uwarunkowania geograficzne chronią was z aż 3 stron!?"

        nemeczek "Jak nie jak tak?"
        nemeczek "z wschodu i zachodu ciągną się rury hydrauliczne nad którymi mamy pełną kontrolę"
        nemeczek "A na północy rozciągają się nieprzekraczalne dla słoni góry kartonów"
        nemeczek "A to na nich wojują nasi przeciwnicy"

        burmistrz "hmmm, no dobra brzmi legit"
        burmistrz "to w takim razie ruszamy na południe"

        nemeczek "Do boju żołnierze"

        play sound "audio/sfx/traveling.mp3"
        scene bg black with fade
        scene bg poludnie with fade
        show burmistrz neutral at slightright
        show luszcz neutral at slightleft

        luszcz "To jest ta cała linia frontu?"
        luszcz "Nie wygląda na zbyt ruchliwą"
        luszcz "Coś mi tu śmierdzi"

        burmistrz "To nie ja, myłem się wczoraj (haha żart z niemycia się mega zabawne)"
        burmistrz "A tak na serio to też mi coś tu nie pasuje"

        luszcz "Ej ej myślisz o tym samym co ja!?"
        lb "Hannibal zamierza przedrzeć się przez góry na słoniach!"

        burmistrz "Musimy natychmiast poinformować Nemeczka!"

        play sound "audio/sfx/traveling.mp3"
        scene bg black with fade
        scene bg kwatera with fade

        show nemeczek neutral at right
        show burmistrz neutral right at left
        show luszcz neutral at slightleft

        luszcz "Panie generale! panie generale!"
        luszcz "Hannibal zamierza przedrzeć się przez góry!"

        nemeczek "Przez góry!? Nie róbcie sobie ze mnie jaj!"
        nemeczek "Nie da się przebyć na słoniach gór z kartonów!"

        burmistrz "Panie generale, ale mu się udało!"
        burmistrz "Na południu nie ma żadnych Kartagińczyków!"

        nemeczek "Dość tych bredni!"

        luszcz "To nie są brednie! To sama prawda, a prawda boli"

        nemeczek "Ani słowa więcej!"

        label burmistrz1a:
            menu:
                "{b}Ulegnij{/b}":
                    luszcz "Ehhh jeżeli pan generał jest tego pewien"

                    nemeczek "Jestem, a teraz wracać mi na południe"

                    "{i}Bez słowa daleszego sprzeciwu wyruszyliście z burmistrzem w drogę powrotną na południe{/i}"

                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    scene bg poludnie with fade
                    show burmistrz neutral at slightright
                    show luszcz neutral at slightleft

                    burmistrz "Mam co do przyszłości naszego kraju bardzo złe przeczucia"

                    luszcz "Może nie będzie, może Kartagińczycy zgubili po prosty drogę?"

                    burmistrz "Miejmy taką nadzieje"

                    scene bg black with fade
                    "{i}*upływają 2 godziny*{/i}"
                    scene bg poludnie with fade
                    show burmistrz neutral at slightright
                    show luszcz neutral at slightleft

                    burmistrz "Chyba Kartagińczycy nie przybędą…"

                    luszcz "Chyba nie…"

                    burmistrz "Wracamy do kwatery dowodzenia?"

                    luszcz "Wracajmy"

                    stop music

                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    scene bg kwatera with fade
                    show burmistrz neutral right at left
                    show luszcz neutral at slightleft

                    luszcz "Panie generale, nadal nikt nieprzybyl"

                    show nemeczek dead at right
                    play sound "audio/sfx/jumpscare.mp3"
                    

                    luszcz "O ja pierdole"  
                    luszcz "On się zajebał"
                    luszcz "Co za pojeb"

                    show luszcz telefon at center
                    luszcz "Zrobię zdjęcię, będzie dla potomnych"

                    show luszcz neutral at center

                    luszcz "Dobra nic tu po nas wracajmy do domu"

                    burmistrz "Wracajmy, nie chcę dłużej na to patrzeć"

                    play sound "audio/sfx/traveling.mp3"
                    scene bg black with fade
                    scene bg plac with fade
                    show burmistrz neutral at slightright
                    show luszcz neutral at slightleft

                    burmistrz "…"

                    luszcz "…"

                    burmistrz "To eeee zajmiesz się tą strażą pożarną?"

                    luszcz "Zajme… zajme…"

                    burmistrz "…"

                    luszcz "…"

                    burmistrz "To do zobaczenia czy coś"

                    luszcz "no bywaj"

                    hide burmistrz
                    show luszcz neutral at center

                    luszcz "…"

                    $ burmistrz_wybory = 1
                    $ nemeczek_wybory = 10
                    $ burmistrz_social_link = 2
                    
                    play music "audio/music/pole.mp3"
                    jump sloneczna

                "{b}Postaw się{/b}":
                    $ burmistrzkill = 0
                    luszcz "Nie, nie mogę na to pozwolić panie generale"
                    luszcz "Ruszam na północ nieważne co pan powie"
                    luszcz "Nie pozwolę, by jeden błąd upartego człowieka doprowadził do upadku naszej republiki"

                    burmistrz "Wyruszam z tobą!"

                    luszcz "Nie, musisz tu zostać i przekonać Nemeczka do wysłania sił na północ"
                    luszcz "Sami i tak, nie powstrzymamy Hanibala"

                    burmistrz "Dobrze zostanę, uważaj na siebie"

                    nemeczek "Jak śmiecie nie słuchać moich rozkazów!"
                    nemeczek "Będziecie państwo wisieć!"
                
                "{b}Spójrz burmistrzowi w oczy{/b}" if burmistrza1 == 0:
                    $ burmistrza1 = 1
                    stop music
                    "{i}W oczach burmistrza zobaczyłeś pełne zrozumienie{/i}"

                    menu:
                        "{b}Czy chcecie to uczynić?{/b}"

                        "{b}Tak{/b}":
                            $ burmistrzzbroja = 0
                            $ burmistrzkill = 1
                            "{i}W pełnej zgodzie i synchronizacji z burmistrzem, wyciągnęliście noże i rozpoczęliście zbrodnię{/i}"

                            show nemeczek dead at right
                            with hpunch
                            play sound "audio/sfx/krzyk.mp3"

                            nemeczek "Aaaaaaaaagh i ty Łuszczu przeciwko mnie!?"

                            "{i}Lecz nie poprzestaliście na jednym dźgnięciu nożem{/i}"
                            "{i}Zaczeliście dźgać, dżgać, dźgać bez opamiętania{/i}"
                            "{i}Nie zważając na nic dokonywaliście tej okrutnej zbrodni, aby uratować republikę przed szaleńcem{/i}"
                            "{i}I dopiero po 23 dźgnięciach stwierdziliścię, że to wystarczy{/i}"

                            burmistrz "Nie chciałem tego uczynić, ale zostałem zmuszony"
                            burmistrz "Dla Republiki zrobię wszystko nawet się skurwię"

                            luszcz "Dobra, dobra dość tych żalów"
                            luszcz "Teraz mamy ważniejsze zmartwienia, a mianowicie gdzie powinniśmy ukryć ciało?"

                            label burmistrz2a:
                                menu:
                                    "{b}Zakopmy{/b}":
                                        luszcz "Bez sensu"
                                        jump burmistrz2a

                                    "{b}Przyczepmy do ściany{/b}":
                                        luszcz "Ej przyczepmy go do ściany, w miejscu tego ziutka co wisi"

                                        burmistrz "Jakiego ziutka!?"

                                        luszcz "No tego tam co tak z tyłu przy wejściu jest"

                                        burmistrz "gdzie... o jezus maria"
                                        burmistrz "i on tak przez cały czas tu był?"
                                        burmistrz "Ej ty dobra podoba mi się ta kryjówka, robimy to"
                                        
                                        scene bg black with fade
                                        scene bg kwatera2 with fade
                                        show burmistrz neutral at slightright
                                        show luszcz neutral at slightleft

                                        luszcz "No i nie widać tak jak mówiłem"

                                        burmistrz "ahh Łuszczu ty to masz łeb"
                                    
                                    "{b}Zjedzmy{/b}":
                                        luszcz "Zjedzmy go"
                                        luszcz "kiedyś jadłem zupę z elfa i była smakówa"
                                        luszcz "Więc zupa z człowieka musi być lepsza z racji na naszą wyższość rasową"

                                        burmistrz "Oh, no dobra"
                                        burmistrz "W końcu trzeba otwierać sie na nowe smaki"

                                        scene bg black with fade

                                        "{i}Przygotowaliścię wszystkie rzeczy do ogniska, rozpaliliście ogień, wrzuciliście przyprawy do garka i zaczeliścię kroić Nemeczka{/i}"

                                        scene bg kwatera with fade
                                        show burmistrz neutral at slightright
                                        show luszcz neutral at slightleft

                                        burmistrz "A co robimy z głową?"
                                        burmistrz "z niej zupa nie wyjdzie..."

                                        luszcz "Ja ją wezmę, już od dawna potrzebowałem piłki do siatkówki, bo wszystkie poprzednie rozwaliłem"

                                        burmistrz "No dobra skoro ją chcesz"

                                        $ glowa = 1

                                        "{i}*głowa nemeczka została dodana do ekwipunku*{/i}"

                            burmistrz "no a teraz sprawa ważniejsza, co robimy, żeby powstrzymać Hannibala"

                            luszcz "Musimy przejąć, kontrolę nad łańcuchem dowodzenia wojskami republiki"
                            luszcz "I to ty burmistrzu musisz tego dokonać!"
                            luszcz "Ja w tym czasię wyruszę na północ i spróbuję opóźnić Hannibala jak mogę"

                            burmistrz "Dobrze, w takim razię powodzenia i niech republika zwycięży!"

                            luszcz "All Hail Republic!"

                        "{b}Nie{/b}":
                            play music "audio/music/plac.mp3"
                            jump burmistrz1a

        scene bg black with fade

        "{i}Podczas drogi na północ nie było widać, ani jednej żywej duszy{/i}"

        "{i}Nawet na samej granicy nie było żadnych republikańskich żołnierzy{/i}"

        scene bg polnoc with fade
        show luszcz neutral at left
        play music "audio/music/plac.mp3"
        
        if burmistrzkill == 1:
            luszcz "(Naprawdę Nemeczek był pewien, że nie przejdą przez góry kartonów…)"
        
        else:
            luszcz "(Naprawdę Nemeczek jest pewien, że nie przejdą przez góry kartonów…)"

        luszcz "(Muszę zbudować mór)"

        "{i}Lecz zanim stanęła na ziemi pierwsza cegła, przybyły wojska nieprzyjaciela{/i}"

        show luszcz neutral at left
        show tanya neutral right at center
        show kartaginczyk1 neutral at right
        show kartaginczyk2 neutral at slightright

        tanya "żołnierze! Przygotować się do blitzkriegu! Musimy dotrzeć ich stolicy zanim ktokol…."

        show tanya neutral at center

        tanya "…wiek się pojawi"

        tanya "Kim ty do cholery jesteś? I skąd wiedziałeś, że tu będziemy?"

        luszcz "Jam jestem Maciejus Luscus i zwom mnie pierwszym strażnikiem republiki!"

        luszcz "i jestem tutaj, aby Ciebie powstrzymać Hannibalu!"

        tanya "Hannibal nie żyje"

        luszcz "Jak to nie żyje!?"

        tanya "Tak to"
        tanya "Ten debil stwierdził, że zamiast jeździć NA słoniach, możemy jeździć W słoniach i mieć w ten sposób zwierzęce czołgi"
        tanya "I ten idiota władował się do dupska słonia"
        tanya "a ten słoń miał sraczkę…"
        tanya "No i teraz ja, Tanya von Degurechaff tu dowodzę"

        luszcz "aha smutne"

        tanya "smutne, ale prawdziwe"
        tanya "no, a wracając do rzeczy ważnych"
        tanya "to stoisz nam na drodzę, więc będziemy musieli ciebie zabić"

        luszcz "spróbujcie jeśli potraficie"

        jump fight71

        label after_fight71:
            play music "audio/music/plac.mp3"
            if burmistrzzbroja == 1:
                scene bg polnoc
                show luszcz zmentzony at center
                luszcz "Ich jest za dużo! Nie powstrzymam ich samemu!"
                luszcz "Nie mam już sił, poddaję się!"

                scene bg black with fade
                "{i}Łuszcz padł bez sił na ziemi i po chwili został pojmany i zgwałcony, a potem zasilił szeregi haremu władcy kartaginy i dopiero po latach udało mu się zwiać…{/i}"
                play music "audio/music/pole.mp3"
                scene bg plac with fade
                show luszcz neutral at center

                luszcz "whooh udało mi się zwiać"
                luszcz "jebany nemeczek nie przysłał posiłków"
                luszcz "ale burmistrz nie lepszy, nawet nie przyszedł mi pomóc, gdy nie przekonał Nemeczka"
                luszcz "Ehhh, teraz to ja chcę tylko o tym zapomnieć jak najszybciej"
                luszcz "Oby zły dotyk jednak nie bolał całe życie,,,"

                $ burmistrz_wybory = 0
                $ nemeczek_wybory = 0
                $ burmistrz_social_link = 10
                
                jump sloneczna
            
            else:
                scene bg polnoc
                show luszcz zmentzony at center

                luszcz "Ich jest za dużo! Nie powstrzymam ich samemu!"

                burmistrz "I nie musisz!"

                show luszcz neutral at left
                show burmistrz neutral at center
                show dzieci at right

                luszcz "Burmistrzu przybyłeś!"

                burmistrz "Nie mógłbym Ciebie porzucić!"
                burmistrz "A teraz odpocznij sobie, a moi chłopcy zajmą się resztą"

                burmistrz "Towarzysze, do boju. Zajebcie każdego kartagińczyka jakiego spotkacie!"

                if burmistrzkill == 1:
                    all "Tak jest panie generale"
                else:
                    all "Tak jest panie pułkowniku"

                play sound "audio/sfx/fighting.mp3"
                play music "audio/music/pole.mp3"

                scene bg black with fade
                scene bg plac with fade
                show luszcz neutral at slightleft
                show burmistrz neutral at slightright

                burmistrz "whooh, ale to był dzień"
                burmistrz "już dawno tak dobrze sie nie czulem"
                burmistrz "trzeba będzie to kiedyś powtórzyć"

                luszcz "no kiedyś będzie trzeba…"

                burmistrz "to co do zobaczenia i pamiętaj o straży pożarnej"

                hide burmistrz
                show luszcz neutral at center

                luszcz "Ale ja nie chcę tego ro…"
                luszcz "Ehhh… strzelam"

                $ burmistrz_wybory = 2
                if burmistrzkill == 1:
                    $ nemeczek_wybory = 10
                else:
                    $ nemeczek_wybory = 1
                $ burmistrz_social_link = 2
                
                jump sloneczna




