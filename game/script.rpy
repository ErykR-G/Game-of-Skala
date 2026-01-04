init python:
    def get_time(timer):
        day = timer // 1440 + 1
        hour = (timer % 1440) // 60
        minute = timer % 60
        return day, hour, minute

label prolog_decyzje:
    define ofiara = 0

label postacie:
    define all = Character("Wszyscy", color="#6a6a6e")

    define luszcz = Character("Łuszcz", color="#1d0cbb")
    image luszcz siedzi right = Transform("luszcz siedzi", xzoom=-1) 
    image luszcz zmentzony right = Transform("luszcz zmentzony", xzoom=-1) 

    define eminem = Character("Shadow", color="#32313a")
    define urban = Character("Jerzy Urban", color="#ff4040")
    define zyd = Character("Żyd", color="#25ff37")
    define kazuma = Character("Kazuma", color="#dbf01f")
    define tarczownik = Character("Naofumi", color="#0a570a")
    

    define ksiadz = Character("Ksiądz", color="#8607b8")

    define kosc = Character("Kościelny", color="#9db2f8")
    image kosc neutral left = Transform("kosc neutral", xzoom=-1) 
    image kosc zly left = Transform("kosc zly", xzoom=-1)

    define akane = Character("Akane", color="#ffffff")
    define kibol1 = Character("Kibol 1", color="#ffffff")
    define kibol2 = Character("Kibol 2", color="#ffffff")

    

    

image ruch = "fight/ruch.png"



label pozycje:
    transform slightleft:
        xalign 0.25
        yalign 1.0
    
    transform slightright:
        xalign 0.75
        yalign 1.0

    transform time:
        xalign 0.97
        yalign 0.03

    transform sojusznik1:
        xalign 0.20
        yalign 0.10

    transform sojusznik2:
        xalign 0.20
        yalign 0.90

    transform sojusznik3:
        xalign 0.05
        yalign 0.50

    transform wrog1:
        xalign 0.80
        yalign 0.10

    transform wrog2:
        xalign 0.80
        yalign 0.90

    transform wrog3:
        xalign 0.95
        yalign 0.50

label pozycje_center:
    transform center_sojusznik1:
        xalign 0.22
        yalign 0.18

    transform center_sojusznik2:
        xalign 0.22
        yalign 0.75

    transform center_sojusznik3:
        xalign 0.085
        yalign 0.47

    transform center_wrog1:
        xalign 0.78
        yalign 0.18

    transform center_wrog2:
        xalign 0.78
        yalign 0.75

    transform center_wrog3:
        xalign 0.915
        yalign 0.47

label pozycje_prison:
    transform prison_sojusznik1:
        xalign 0.165
        yalign 0.075

    transform prison_sojusznik2:
        xalign 0.165
        yalign 0.925

    transform prison_sojusznik3:
        xalign 0
        yalign 0.50

    transform prison_wrog1:
        xalign 0.835
        yalign 0.075

    transform prison_wrog2:
        xalign 0.835
        yalign 0.925

    transform prison_wrog3:
        xalign 100
        yalign 0.50

label pozycje_head:
    transform head_sojusznik1:
        xalign 0.228
        yalign 0.10

    transform head_sojusznik2:
        xalign 0.228
        yalign 0.66

    transform head_sojusznik3:
        xalign 0.09
        yalign 0.38

    transform head_wrog1:
        xalign 0.772
        yalign 0.075

    transform head_wrog2:
        xalign 0.772
        yalign 0.63

    transform head_wrog3:
        xalign 0.91
        yalign 0.35

label pozycje_bok:
    transform bok_sojusznik1:
        xalign 0.19
        yalign 0.24

    transform bok_sojusznik2:
        xalign 0.19
        yalign 0.80

    transform bok_sojusznik3:
        xalign 0.057
        yalign 0.51

    transform bok_wrog1:
        xalign 0.81
        yalign 0.24

    transform bok_wrog2:
        xalign 0.81
        yalign 0.80

    transform bok_wrog3:
        xalign 0.943
        yalign 0.51
    
label pozycje_weapon:
    transform weapon_sojusznik1:
        xalign 0.265
        yalign 0.18

    transform weapon_sojusznik2:
        xalign 0.265
        yalign 0.73

    transform weapon_sojusznik3:
        xalign 0.13
        yalign 0.45

    transform weapon_wrog1:
        xalign 0.735
        yalign 0.18

    transform weapon_wrog2:
        xalign 0.735
        yalign 0.73

    transform weapon_wrog3:
        xalign 0.87
        yalign 0.45
    
label pozycje_tarcza:
    transform tarcza_sojusznik1:
        xalign 0.365
        yalign 0.18

    transform tarcza_sojusznik2:
        xalign 0.365
        yalign 0.82

    transform tarcza_sojusznik3:
        xalign 0.365
        yalign 0.50

    transform tarcza_wrog1:
        xalign 0.635
        yalign 0.18

    transform tarcza_wrog2:
        xalign 0.635
        yalign 0.82

    transform tarcza_wrog3:
        xalign 0.635
        yalign 0.50

label pozycje_tla:
    transform tlo_sojusznik1:
        xalign 0.193
        yalign 0.075

    transform tlo_sojusznik2:
        xalign 0.193
        yalign 0.925

    transform tlo_sojusznik3:
        xalign 0.04
        yalign 0.50

    transform tlo_wrog1:
        xalign 0.807
        yalign 0.075

    transform tlo_wrog2:
        xalign 0.807
        yalign 0.925

    transform tlo_wrog3:
        xalign 0.96
        yalign 0.50

default dialog_fight1 = 0

default ado = 0
default kostka = 0
default timer = 537
default money = 3

label items:
    default ile_item = 2
    default bandaz = 1
    default granat = 1

label fight_stats:
    default liczba_sojusznikow = 1
    default ile_sojusznikow = 0
    default ile_wrogow = 0

    default luszcz_sex = 0
    default eminem_sex = 0
    default urban_sex = 0
    default zyd_sex = 0
    default kazuma_sex = 0
    default tarczownik_sex = 0

    default luszcz_weapon = 1
    default eminem_weapon = 0
    default urban_weapon = 1
    default zyd_weapon = 1
    default kazuma_weapon = 1
    default tarczownik_weapon = 1

    default luszcz_fighter = 0
    default eminem_fighter = 0
    default urban_fighter = 0
    default zyd_fighter = 0
    default kazuma_fighter = 0
    default tarczownik_fighter = 0

    default luszcz_sojusznik = 1
    default eminem_sojusznik = 0
    default urban_sojusznik = 0
    default zyd_sojusznik = 0
    default kazuma_sojusznik = 0
    default tarczownik_sojusznik = 0

    default luszcz_wybrany = 0
    default eminem_wybrany = 0
    default urban_wybrany = 0
    default zyd_wybrany = 0
    default kazuma_wybrany = 0
    default tarczownik_wybrany = 0

    default luszcz_obrona = 0
    default eminem_obrona = 0
    default urban_obrona = 0
    default zyd_obrona = 0
    default kazuma_obrona = 0
    default tarczownik_obrona = 0

    default luszcz_hp = 20
    default eminem_hp = 15
    default urban_hp = 20
    default zyd_hp = 10
    default kazuma_hp = 10
    default tarczownik_hp = 15

    default luszcz_hp_now = luszcz_hp
    default eminem_hp_now = eminem_hp
    default urban_hp_now = urban_hp
    default zyd_hp_now = zyd_hp
    default kazuma_hp_now = kazuma_hp
    default tarczownik_hp_now = tarczownik_hp

    default luszcz_min_attack = 1
    default eminem_min_attack = 2
    default urban_min_attack = 0
    default zyd_min_attack = 1
    default kazuma_min_attack = 0
    default tarczownik_min_attack = 1

    default luszcz_max_attack = 4
    default eminem_max_attack = 5
    default urban_max_attack = 4
    default zyd_max_attack = 5
    default kazuma_max_attack = 8
    default tarczownik_max_attack = 5

    default luszcz_max_attack_now = luszcz_max_attack
    default eminem_max_attack_now = eminem_max_attack
    default urban_max_attack_now = urban_max_attack
    default zyd_max_attack_now = zyd_max_attack
    default kazuma_max_attack_now = kazuma_max_attack
    default tarczownik_max_attack_now = tarczownik_max_attack

    default luszcz_min_attack_now = luszcz_min_attack
    default eminem_min_attack_now = eminem_min_attack
    default urban_min_attack_now = urban_min_attack
    default zyd_min_attack_now = zyd_min_attack
    default kazuma_min_attack_now = kazuma_min_attack
    default tarczownik_min_attack_now = tarczownik_min_attack

    default luszcz_max_attack_now_true = luszcz_max_attack
    default eminem_max_attack_now_true = eminem_max_attack
    default urban_max_attack_now_true = urban_max_attack
    default zyd_max_attack_now_true = zyd_max_attack
    default kazuma_max_attack_now_true = kazuma_max_attack
    default tarczownik_max_attack_now_true = tarczownik_max_attack

    default luszcz_min_attack_now_true = luszcz_min_attack
    default eminem_min_attack_now_true = eminem_min_attack
    default urban_min_attack_now_true = urban_min_attack
    default zyd_min_attack_now_true = zyd_min_attack
    default kazuma_min_attack_now_true = kazuma_min_attack
    default tarczownik_min_attack_now_true = tarczownik_min_attack

    default luszcz_attack = 0
    default eminem_attack = 0
    default urban_attack = 0
    default zyd_attack = 0
    default kazuma_attack = 0
    default tarczownik_attack = 0

    default pager_boom = 0

label start:
    label prolog:
        show screen global_eq_key
        show bg start
        show luszcz siedzi right at slightright
        show screen clock
        play music "audio/music/wiatr.mp3"
        luszcz "Ahhh… ówielbiam siedzieć na moim klifie mondrości i obserwować z niej Skałę"
        luszcz "Ohhh… jak ja kocham mojom ojczyznę Skałę."
        luszcz "Jest taka betonowa…"
        luszcz "I jej ograniczona ilość miejsc rozrywkowo rekreacyjnych jest taka urocza…"
        luszcz "Nigdy nie zostawiłbym jej dla mieszkania w Krakowie."
        luszcz "A społeczność…"
        luszcz "Społeczność jest taka kochana…"
        $ timer += 1
        luszcz "Karzdy jest taki inny, jak gdyby w gdzieś w mieście znajdował się portal wpószczający istoty z innyh uniwersów."
        luszcz "Wszyscy mają też dziwne kryptonimy kturych nie potrafię się naóczyć"
        luszcz "Ale to jest jakby okej."
        luszcz "Dzięki temu czuję się jakbym karzdego dnia poznawał ich na nowo."
        luszcz "Co pozwala mi terz uczyć się od nich kolejnych mondrości które sprawiają, że mogę nazywać się Mędrcem ze Skały."
        luszcz "Jest jednak jeden mieszkaniec którego szczerze nienawidzę."
        $ timer += 1
        luszcz "Ksiądz…"
        luszcz "Sama myśl o nim wyprowadza mnie z ruwnowagi. A niechciałbym spaść z klifu."
        luszcz "Całe szczęście że nie chodzę do kościoła."
        luszcz "…"  
        $ timer += 1    

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "O kurde rzeczywiście. Dziś niedziela."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Dzwon zawsze dzwoni trzy razy przed mszą rzeby przypomnieć ludziom że istnieje."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Fajnie by było jakby wymyślili jakiś system który nie rozwala moich ószu."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"

        luszcz "Ojej… jak bije więcej razy to coś znaczyło…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"

        luszcz "Pięć uderzeń to śmierć kościelnego…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"

        luszcz "Sześć to porzar…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"

        luszcz "Siedem ogłasza Sezon na misia…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"

        luszcz "Osiem to utoniencie człowieka w Wiśle…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"

        luszcz "Dziewięć to ogłoszenia polityczne…"

        "{i}...{/i}"

        luszcz "A dziesięć to…?"

        "{i}...{/i}"

        luszcz "Kurcze akórat tak dawno nie było dziesięciu."
        luszcz "A już poczułem żądzę krwi w moim sercu…"
        luszcz "Cóż… może następnym razem"

        luszcz "Chwila czyli w kościele bendzie o polityce"
        luszcz "Co mu znowu wpadlo do głowy"
        luszcz "Może lepiej pujdę sprawdzić."

        scene bg przed_kosciol
        play music "audio/music/kosciol.mp3"
        show luszcz zmentzony right at center
        $ timer += 5

        luszcz "Ale żem się nabiegał"
        luszcz "Mam nadzieję że zdąrzyłem przed ogłoszeniami."

        scene bg kosciol
        show luszcz zmentzony right at right

        luszcz "Myślę że tutaj ksiądz mnie nie zauwarzy."
        luszcz "Dobra, teraz tylko przesiedzieć do ogłoszeń."

        ksiadz "…to czyńcie na moją pamiątkę…"

        luszcz "Hel noł nie jestem pewien czy pamiętam wszystkie regułki"
        luszcz "Dobra będę kopiował innych"

        show luszcz modlitwa at right
        $ timer += 30

        ksiadz "lalalala"

        show kosc neutral left at center

        kosc "A niech cię, nigdy wcześniej nie widziałem cię w kościele."
        kosc "A uwież mi, pamiętam każdą twarz, co do jednej!"

        luszcz "Erm… to dlatego że jestem tu pierwrzy raz"

        kosc "Tak też myślałem. Wiedz, że idziesz dobrą ścieżką młody."

        luszcz "(mam nadzieję że ten człowiek zaraz sobie pujdzie nie daję mu grosza.)"
        luszcz "(zwłaszcza że nie mam rzadnych drobnych. Tylko pare portfeli które zostały mi z kieszonkowego)"
        luszcz "(niestety są tak pełne że wyjęcie z nich banknota sprawi że wszystkie inne wylecą i zapełnią cały kościół dusząc wszystkich w środku.)"
        luszcz "(a tego nikt by nie chciał.)"

        kosc "…"
        kosc "Nie martw się, z daleka widziałem że kompletnie nie wiesz jak wyglądają obrzędy mszy."
        kosc "Jestem kościelnym. Jednym z moich zadań jest zbieranie pieniędzy od wiernych na utrzymanie kościoła."
        kosc "Pomyśl o tym jak o małej zapłacie za udział we mszy."

        luszcz "(Okej on serio oczekóje ode mnie pieniędzy)"



        $ config.menu_include_disabled = True
        menu:
            
            "{b}Daj (3 💰){/b}" if money >= 3:
                $ money -= 3
                $ ofiara += 3

                kosc "Jak możesz zauważyć w koszyku… ludzie wrzucają zazwyczaj banknoty dziesięciozłotowe"
                kosc "Nawet 5zł jest dobrze u nas postrzegane…"
                kosc "Jesteś pewien że jesteś w stanie tyle nam poświęcić?"

                luszcz "Podjąłem swoją decyzję."

                kosc "W takim razie niech Pan cię strzeże w szczęściu i nieszczęściu. Bóg zapłać!"
            
            "{b}Daj (2 💰){/b}" if money >= 2:
                $ money -= 2
                $ ofiara += 2

                kosc "... oh.."
                kosc "Musi ci bardzo zależeć na Bogu. Oby wszystkie twoje prośby zostały spełnione. Bóg zapłać!"
            
            "{b}Daj (1 💰){/b}" if money >= 1:
                $ money -= 1
                $ ofiara += 1

                kosc "... oh.."
                kosc "łał"
                kosc "Wspólnota jest Ci wdzięczna. Bóg zapłać"

            "{b}Nie daj nic{/b}":
                kosc "Widzę, że nie brakuje ci pieniędzy. Jednak nie planujesz się nimi podzielić?"

                luszcz "Podjąłem swoją decyzję."

                kosc "Pierwszy raz jestem w stanie uszanować. Pamiętaj jednak, że my też musimy na czymś żyć"

                luszcz "(Jebie mnie twój kościół, jak zdechniecie z głodu to nawet lepiej)"

        $ config.menu_include_disabled = False

        ksiadz "…Podajmy sobie znak pokoju."

        if ofiara >= 1:
            show kosc neutral left at slightright

            kosc "Pokój z tobą"

            luszcz "e… pokój z tobą."

            hide kosc
        
        else:
            show kosc zly left at slightleft

            kosc "..."

            hide kosc
        
        luszcz "Okej poszedł sobie"
        "{i}Teraz tylko opłatki i ogłoszenia.{/i}"

        all "Pan… kiedyś stanął na brzegu…"

        scene bg black with fade
        scene bg kosciol with fade
        show luszcz modlitwa at right
        $ timer += 5

        luszcz "Tooobą… nowy zacznę dziś łuuuuw…"
        luszcz "ah potrzebowałem tego"

        ksiadz "Dobrze zatem przejdźmy do ogłoszeń."

        hide luszcz
        show ksiadz kazanie at center

        ksiadz "Chcielibyśmy podziękować kilku osobom z tej ulicy co wtedy była poproszona o posprzątanie kościoła i przekazanie 300 złotych ofiary."
        ksiadz "Ogłaszamy że w parafii odbędzie się charytatywny koncert kolęd Zenona Martyniuka dla dzieci które chorują na doświadczanie ducha świąt miesiąc po zdarzeniu."
        ksiadz "Wstęp jest darmowy, ale zachęcamy coś podarować, gdyż 67%%  wszystkich pieniędzy idzie na leczenie dzieci z opóźnionym duchem świąt."
        ksiadz "Występ Zenona został prywatnie załatwiony przez naszego kościelnego. Pozostałe 33%% idą na rozwój kościoła."
        ksiadz "Z dzisiejszej składki policzyliśmy pięć tysięcy i trzy złote. Na tę kwotę złożyło się:"
        ksiadz "dziesięciu ofiarodawców którzy dali po dwadzieścia złotych, stu dwudziestu sześciu ofiarodawców którzy złożyli po dziesięć złotych, trzystu trzydziestu którzy złożyli po pięć złotych,"
        ksiadz "sześćset dziewięćdziesiąt czterech wiernych którzy złożyli po dwa złote, czterystu siedemdziesięciu dziewięciu wiernych którzy złożyli po złotówce."
        ksiadz "Złożono czterdzieści dziewięć pięćdziesięciogroszówek, ponadto dwadzieścia ofiar prawdopodobnie od dzieci po dwadzieścia, dziesięć, pięć, dwa i jeden grosz."
        ksiadz "Złożono także na tacę jeden euro."
        ksiadz "Za wszystkie ofiary składam serdecznie Bóg zapłać."
        ksiadz "Wszystkie te ofiary w oczach Bożych są miłe i wiele znaczą."

        $ timer += 10

        if ofiara == 3:
            ksiadz "Jednakże najwięcej znaczy ofiara jednej osoby, która włożyła do koszyka trzy całe portfele."
            ksiadz "Ich zawartość była tak obszerna, że zapełniła całą zakrystię, prawie dusząc ministrantów liczących pieniądze."
        
        if ofiara == 2:
            ksiadz "Jednakże najwięcej znaczy ofiara jednej osoby, która włożyła do koszyka dwa całe portfele."
            ksiadz "Ich zawartość była tak obszerna, że zapełniła całą zakrystię, prawie dusząc ministrantów liczących pieniądze."
        
        if ofiara == 1:
            ksiadz "Jednakże najwięcej znaczy ofiara jednej osoby, która włożyła do koszyka cały potfel."
            ksiadz "Jego zawartość była tak obszerna, że zapełniła całą zakrystię, prawie dusząc ministrantów liczących pieniądze."
        
        if ofiara == 0:
            ksiadz "Jednakże mały poranny ptaszek wyśpiewał mi że jeden z parafian postanowił wstrzymać się od dania ofiary mimo posiadania portfeli pełnych pieniędzy."

        ksiadz "Z tego właśnie powodu przechodząc do ogłoszeń związanych z polityką chciałbym zacząć od nowej ustawy która mianuje płacenie portfelami jako jedyną legalną fizyczną formę płatności."

        $ timer += 10
        stop music

        




    label faubla:
        scene bg korytarz
        menu:
            "{b}Ilu masz przyjaciół?{/b}"

            "{b}DUŻO{/b}":
                $ liczba_sojusznikow += 3
                $ eminem_sojusznik += 1
                $ urban_sojusznik += 1
                $ zyd_sojusznik += 1
                $ kazuma_sojusznik += 1
                $ tarczownik_sojusznik += 1
                $ przepychaczka = 1
                $ stop = 1

            "{b}TROCHE{/b}":
                $ liczba_sojusznikow += 2
                $ urban_sojusznik += 1
                $ zyd_sojusznik += 1
                $ stop = 1
                $ przepychaczka = 1
                
            "{b}MAM{/b}":
                $ liczba_sojusznikow += 1
                $ urban_sojusznik += 1
                $ stop = 1
                $ przepychaczka = 1

                
            "{b}CO TO?{/b}":
                $ ado += 1
        
        jump fight1
    label after_fight1:
        "{i}Gratulacje wygrałeś{/i}"
