
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

        burmistrz "To świetnie, choć zabiorę Cię na plac, gdzie powstanie centrum szkolenia nowych strażaków!"

        luszcz "Ehhh, znów się w coś wplątałem"

        play sound "audio/sfx/traveling.mp3" 
        scene bg black with fade
        scene bg plac with fade
        show burmistrz neutral at slightright
        show luszcz neutral at slightleft

        burmistrz "I dokładnie w tym oto miejscu powstanie całkowicie nowe, centrum szkoleniowe dla strażaków"

        luszcz "Ludzie, ale tu przecież niczego nie ma"

        show nemeczek neutral at center
        show burmistrz neutral at right
        show luszcz neutral at left

        nemeczek "Jak śmiesz tak mówić, to jest nasza ojczyzna"
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
                luszcz "Dobra nic tu po nas wracajmy do domu"
                show luszcz neutral at center

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
                
                play music "audio/music/pole.mp3"
                jump sloneczna



