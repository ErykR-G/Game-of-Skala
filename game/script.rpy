init python:
    def get_time(timer):
        day = timer // 1440 + 1
        hour = (timer % 1440) // 60
        minute = timer % 60
        return day, hour, minute

default ado = 0
default kostka = 0
default kostka2 = 0
default timer = 537
default money = 3

label postacie:
    define all = Character("Wszyscy", color="#6a6a6e")
    define nikt = Character("???", color="#6a6a6e")

    define luszcz = Character("Łuszcz", color="#1d0cbb")
    image luszcz siedzi right = Transform("luszcz siedzi", xzoom=-1) 
    image luszcz zmentzony right = Transform("luszcz zmentzony", xzoom=-1) 
    image luszcz neutral right = Transform("luszcz neutral", xzoom=-1) 


    define rand = Character("Ktoś z widowni", color="#8a8a8a")

    define eminem = Character("Shadow", color="#32313a")
    define cid = Character("Cid", color="#32313a")
    image eminem sad right = Transform("eminem sad", xzoom=-1) 
    image eminem neutral reka right = Transform("eminem neutral reka", xzoom=-1) 

    define urban = Character("Jerzy Urban", color="#ff4040")

    define zyd = Character("Żyd", color="#25ff37")
    image zyd neutral right = Transform("zyd neutral", xzoom=-1) 
    image zyd lampa right = Transform("zyd lampa", xzoom=-1) 

    define kazuma = Character("Kazuma", color="#dbf01f")
    define tarczownik = Character("Naofumi", color="#0a570a")

    define emina = Character("Eminem", color="#a2a571")
    
    define burmistrz = Character("Burmistrz", color="#f8bf44")
    image burmistrz neutral right = Transform("burmistrz neutral", xzoom=-1) 

    define tanya = Character("Tanya", color="#215f36")
    image tanya neutral right = Transform("tanya neutral", xzoom=-1) 

    define lb = Character("Łuszcz i Burmistrz", color="#9e9e9e")

    define braun = Character("Braun", color="#412607")
    image braun neutral right = Transform("braun neutral", xzoom=-1) 
    image braun shock right = Transform("braun schock", xzoom=-1) 
    image braun smile right = Transform("braun smile", xzoom=-1) 

    define ksiadz = Character("Ksiądz", color="#8607b8")

    define toxic = Character("Toxic Pea", color="#7ec753")

    define nemeczek = Character("Nemeczek", color="#49290b")

    define kosc = Character("Kościelny", color="#9db2f8")
    image kosc neutral left = Transform("kosc neutral", xzoom=-1) 
    image kosc zly left = Transform("kosc zly", xzoom=-1)

    define czarny = Character("Czarny", color="#3a3a3b")

    define rem = Character("Rem", color="#91C0F9")
    define ram = Character("Ram", color="#FFA7BA")

    define akane = Character("Akane", color="#ffffff")
    define kibol1 = Character("Kibol 1", color="#ffffff")
    define kibol2 = Character("Kibol 2", color="#ffffff")

    define gnom = Character("Noggin Gnomes", color="#180a9b")

    define turek = Character("Turek", color="#910909")


label pozycje:
    transform granatz:
        xalign 0.83
        yalign 0.50


    label vr:
        transform gorasojusznik1:
            xalign 0.32
            yalign 0.09

        transform dolsojusznik1:
            xalign 0.32
            yalign 0.22

        transform gorasojusznik2:
            xalign 0.32
            yalign 0.64

        transform dolsojusznik2:
            xalign 0.32
            yalign 0.78

        transform gorasojusznik3:
            xalign 0.18
            yalign 0.37

        transform dolsojusznik3:
            xalign 0.18
            yalign 0.50

        transform rzygi_sojusznik1:
            xalign 0.27
            yalign 0.16

        transform rzygi_sojusznik2:
            xalign 0.27
            yalign 0.83

        transform rzygi_sojusznik3:
            xalign 0.115
            yalign 0.50
            


    label pozycje_wojownikow:
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

    label pozycje_nadhead:
        transform nadhead_sojusznik1:
            xalign 0.228
            yalign 0.005

        transform nadhead_sojusznik2:
            xalign 0.228
            yalign 0.54

        transform nadhead_sojusznik3:
            xalign 0.09
            yalign 0.28

        transform nadhead_wrog1:
            xalign 0.772
            yalign 0.005

        transform nadhead_wrog2:
            xalign 0.772
            yalign 0.54

        transform nadhead_wrog3:
            xalign 0.91
            yalign 0.28

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


label fight_stats:
    default dialog_fight1 = 0
    default dialog_fight2 = 0

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

    default luszcz_hp = 25
    default eminem_hp = 20
    default urban_hp = 25
    default zyd_hp = 15
    default kazuma_hp = 15
    default tarczownik_hp = 20

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

    default luszcz_piguly = 0
    default eminem_piguly = 0
    default urban_piguly = 0
    default zyd_piguly = 0
    default kazuma_piguly = 0

    default luszcz_lagodny = 0
    default eminem_lagodny = 0
    default urban_lagodny = 0
    default zyd_lagodny = 0
    default kazuma_lagodny = 0
    default tarczownik_lagodny = 0

    default luszcz_drpepper = 0
    default eminem_drpepper = 0
    default urban_drpepper = 0
    default zyd_drpepper = 0
    default kazuma_drpepper = 0
    default tarczownik_drpepper = 0

    default luszcz_zloty_czlowiek = 0
    default eminem_zloty_czlowiek = 0
    default urban_zloty_czlowiek = 0
    default zyd_zloty_czlowiek = 0
    default kazuma_zloty_czlowiek = 0
    default tarczownik_zloty_czlowiek = 0

    default luszcz_stun = 0
    default eminem_stun = 0
    default urban_stun = 0
    default zyd_stun = 0
    default kazuma_stun = 0
    default tarczownik_stun = 0


label prolog_decyzje:
    default ofiara = 0

label wybory:
    default eminem_wybory = 0
    default zyd_wybory = 0
    default braun_wybory = 0
    default burmistrz_wybory = 0
    default nemeczek_wybory = 0
    default toxic_pea_wybory = 0

label social_links:
    default zyd_social_link = 0
    default burmistrz_social_link = 0
    default toxic_pea_social_link = 0



label start:
    label prolog:
        hide screen global_eq_key
        scene bg start
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
        $ renpy.pause(0.5)

        luszcz "O kurde rzeczywiście. Dziś niedziela."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Dzwon zawsze dzwoni trzy razy przed mszą rzeby przypomnieć ludziom że istnieje."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Fajnie by było jakby wymyślili jakiś system który nie rozwala moich ószu."

        play sound "audio/sfx/bell.mp3"
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Ojej… jak bije więcej razy to coś znaczyło…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Pięć uderzeń to śmierć kościelnego…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Sześć to porzar…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Siedem ogłasza Sezon na misia…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

        luszcz "Osiem to utoniencie człowieka w Wiśle…"

        play sound "audio/sfx/bell.mp3" 
        "{i}Bim Bom{/i}"
        $ renpy.pause(0.5)

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
        kosc "A uwierz mi, pamiętam każdą twarz, co do jednej!"

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
        ksiadz "Burmistrz był w stanie wprowadzić tę zmianę natychmiastowo"

        burmistrz "to prawda.."

        ksiadz "Przechodząc do ustawy po którą nas tu zwołałem, pomijając Mszę Świętą."
        ksiadz "Jak już wszyscy wiecie, Kraków od wielu lat prowadzi owocną dla wspólnoty chrześcijańskiej ekspansję."
        ksiadz "Jeszcze przed chwilą wydawał się tak odległy, a dziś stoi u naszej granicy i ubiega się o włączenie Skały w swój obszar."
        ksiadz "Jako, iż Kraków zawsze nam dobrze służył, nie widzę w tym żadnego problemu, a nawet uważam, że przyniesie to nam same zyski."
        ksiadz "Dużo zysków."
        ksiadz "Już dziś wyjeżdżam do Krakowa na tydzień aby spotkać się z wodzem sektora rozwojowego Krakowa Bartuchem Przeździuchem i obgadać sprawę w detalach."
        ksiadz "Po moim powrocie w następną niedzielę msza odbędzie się tylko o 21:37. Będziemy na niej przeprowadzać głosowanie w którym jednoznacznie przyjmiemy ofertę krakowską i włączymy się do nowej potęgi."
        ksiadz "Życzę wszystkim miłego dnia. Bóg z wami."

        $ timer += 10

        scene bg przed_kosciol
        show luszcz neutral at center

        luszcz "Myślę, że ksiądz sobie przeskrobał."
        luszcz "Już widzę jak Bartóch wjeżdrza tu w swoim czołgu i wytyka palcem co zbórzyć i gdzie postawić wierzowce."
        luszcz "Zresztą to oczywiste że ksiądz został przekupiony. Pewnie przez ten tydzień będzie kąpał się w chajsiwie i polewał swoje ciało olejem dziecięcym."
        luszcz "Okej. Mam tydzień aby przekonać mieszkańców Skały do przeciwstawienia się księdzu."
        luszcz "To trochę jak w Personie."
        luszcz "Gdzie by się najpierw wybrać?"

        show eminem cien at slightright 

        "{i}*szturch*{/i}"

        hide eminem

        show luszcz zly at center

        luszcz "Co to ma być"
        luszcz "Nie będzie mnie random sztórchał bez przeprosin"
        luszcz "Oczekuję satysfakcji"
        luszcz "Mószę go dopaść!"

        show luszcz zly:
            linear 0.5 xalign 1.5

        $ renpy.pause(0.5)

        scene bg rynek
        play music "audio/music/pole.mp3"
        $ timer += 5

        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.5
        
        $ renpy.pause(0.5)

        label bieg1:
            menu:
                "{b}Gdzie teraz?{/b}"

                '{b}Idź w lewo{/b}':
                    luszcz "{i}Muszę dopaść drania!{/i}"
                    jump bieg1
                    
                '{b}Idź naprzód{/b}':
                    luszcz "{i}Ziomo pobiegł prosto!{/i}"

                '{b}Idź w prawo{/b}':
                    luszcz "{i}Muszę dopaść drania!{/i}"
                    jump bieg1


        show luszcz neutral:
            linear 0.5 xalign 1.5

        $ renpy.pause(0.5)

        scene bg rynek2
        $ timer += 5

        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.5

        $ renpy.pause(0.5)

        label bieg2:
            menu:
                "{b}Gdzie teraz?{/b}"

                '{b}Idź w lewo{/b}':
                    luszcz "{i}Ziomo pobiegł w lewo!{/i}"
                    
                '{b}Idź naprzód{/b}':
                    luszcz "{i}Potrzebuję swojej satysfakcji!{/i}"
                    jump bieg2

                '{b}Idź w prawo{/b}':
                    luszcz "{i}Potrzebuję swojej satysfakcji!{/i}"
                    jump bieg2
        
        show luszcz neutral:
            linear 0.5 xalign -0.5

        $ renpy.pause(0.5)

        scene bg alejka2
        $ timer += 5

        show luszcz neutral at center:
            xalign 1.5
            yalign 1.0
            easeout 0.6 xalign 0.5

        $ renpy.pause(0.5)

        label bieg3:
            menu:
                "{b}Co zrobić?{/b}"

                "{b}Zejdż do piwnicy{/b}":
                    scene bg black with fade
                    scene bg alejka3 with fade
                    play music "audio/music/alejka3.mp3"

                    
                "{b}Może lepiej nie{/b}":
                    luszcz "{i}Nie ma tak że nie{/i}"
                    jump bieg3

        show eminem cien at slightright

        show luszcz neutral at left

        nikt "Zostaw mnie w spokoju!! Czego ode mnie chcesz.."

        luszcz "Sztórchnąłeś mnie. Ta znieawaga krwi wymaga. Oczekuję satysfakcji."

        nikt "Uwierz mi… nie chciałbyś się ze mną teraz pojedynkować."

        luszcz "A czm?"

        scene bg black with fade
        scene bg alejka3v2 with fade

        show eminem sad at slightright

        show luszcz neutral at left

        cid "Nie jestem teraz w najlepszym miejscu mentalnie."

        luszcz "(O boże to cid z mojej ulubionej chińskiej bajki, całe szczęście że nie chce się bić)"
        luszcz "co się stało?"

        cid "Jest taki jeden raper… i jestem jego największym fanem."
        cid "Jego bary są takie badass"
        cid "I udało mi się go kiedyś spotkać"
        cid "I się zaprzyjaźniliśmy"
        cid "I zaoferował mi żebym pisał słowa do jego piosenek w zamian za to że nikomu nie powiem… I tu sobie siedzę i piszę."

        luszcz "To jak miałeś nie mówić to czemu mi to mówisz"

        cid "Trudno mi w to uwierzyć… ale chyba nie jestem tu najlepiej traktowany."
        cid "Znaczy, kocham swojego idola i zrobiłbym dla niego wszystko, ale…"
        cid "Nie dostaję w ogóle jedzenia. Czasem zjadam myszy jak jakieś się wstawią."
        cid "Jedyna woda jaką mam pozwolenie pić to święcona sprzed kościoła…"
        cid "I w sumie to nigdy nie mogę opuszczać pracowni poza z wyjątkiem mszy niedzielnych."
        cid "I mam zakaz rozmawiania z ludźmi.. musiałem się też odciąć od rodziny.. i.."

        luszcz "Czemu pozwalasz się tak kontrolować"
        luszcz "Nie jesteś przypadkiem chodzącą atomuwkom?"

        cid "Nie mogę zawieść swojego idola..!"
        cid "Tyle mu zawdzięczam i jest taki tuff… widzę że nie jestem traktowany najlepiej ale nie ma mnie na tyle żeby mu się przeciwstawiać.."

        luszcz "imo"
        luszcz "weź się w garść"
        luszcz "nie przydupasój komuś bo wydaje się fajniejszy niż ty"

        cid "hmm… noo…. moze masz racje…"

        luszcz "chodź idziemy z tej ciemnicy literalnie nic cię nie trzyma"

        cid "ig…"

        show eminem neutral reka at slightleft

        nikt "STOP!!!" with vpunch

        show eminem neutral right at slightleft

        nikt "Fuck you!"

        show emina neutral at right

        emina "You can’t let him out!! There can only be one Eminem in Shadows!! And thats Me!! Motherfucker!!"

        luszcz "O kurcze emina"
        luszcz "Kiedy on tu pszyszedł"

        emina "Fuck you! I was here the whole time!"
        emina "Im just very slim… and very shady"

        cid "Jak tu byłeś cały czas to nie mamy nic do omówienia."
        cid "Nareszcie wybiła godzina wyzwolenia!"

        emina "Fuck you!! You wont get outta here alive!!"

        scene bg black with fade
        scene bg alejka3v3 with fade
        
        show luszcz fight at sojusznik1
        show eminem reka fight at sojusznik2
        show emina fight at wrog3

        ""

        show eminem reka fight:
            xalign 0.35
            yalign 0.50

        eminem "Cofnij się chłopcze, ja się nim zajmę"

        luszcz "Panie Shadow, ale ja panu pomogę"
        luszcz "Ja w domu wydrukowałem sobie taki sam miecz jak pan ma i dużo trenowałem"
        luszcz "I biegałem nago po lesie jak pan"
        luszcz "Ja mogę pomóc zobaczy pan"
        luszcz "Pokażę panu jak mogę być użyteczny!"

        menu:
            "{b}Zaatakuj Eminema":
                "Łuszcz wyciągnął swoją gitarę wziął zamach i zaczął biec w kierunku Eminema"
                "Niestety po kilku krokach jego prawa noga napotkała kamień iiii…"
        
        scene bg black with fade
        scene bg alejka3v2 with fade

        show luszcz wtf at left
        show eminem bezreki at center 
        show emina neutral at right
        
        play sound "audio/sfx/krzyk.mp3"
        cid "Ała kurwa moje ręka"
        cid "Japierdole, ale to kurwa boli"

        luszcz "Jezus maria krew jest wszędzie"

        cid "Jebane lata treningu dzień w dzień by stać się niepokonany po to tylko by jakiś debil przewrócił się na kamieniu i mi odjebał rękę!"

        luszcz "Nie, panie Cidzie ja nie chciałem to był wypadek"

        cid "Wypadek? Odrąbałeś mi rękę idioto!"
        cid "Jak z tego wyjdziemy, żywi to będę Ci to codziennie wypominał"
        cid "No, ale teraz mamy ważniejsze zmartwienie i skoro nie mam ręki to musisz mi pomóc"

        eminem "Księżyc zrobił się krwawy"

        $ eminem_sojusznik = 1
        $ liczba_sojusznikow += 1
                
        jump fight01

        label after_fight01:
            $ eminem_sojusznik = 0
            $ liczba_sojusznikow -= 1
            scene bg alejka3v2 with fade
            show luszcz spi at left
            show eminem spi at slightleft
            show emina spi at right
        
        play music "audio/music/alejka3.mp3"
        ""
        
        cid "..."

        luszcz "..."

        play sound "audio/sfx/stand_up.mp3"
        "{i}*głośnik* can the real slim shady please stand up *głośnik*{/i}"
        show eminem neutral at slightleft

        $ renpy.pause(0.5)

        emina "nie denerwuj mnie"

        scene bg black with fade
        scene bg rynek with fade

        play music "audio/music/pole.mp3"

        show luszcz neutral at slightleft
        show eminem neutral at slightright

        cid "Wielkie dzięki za pozbieranie mnie do kupy. Czy mogę się jakoś odpłacić?"

        menu:
            "{b}akszuli...{b}":
                jump akszuli

            '{b}Idź lepiej do szpitala zanim się wykrwawisz{/b}':
                cid "Ale tu nie ma żadnego szpitala… tylko jakiś skibidi lekarz pracujący w aptece."
                luszcz "(Rzeczywiście, gdzieś w Skale był lekaż pracujący w aptece… mugłbym go do niego zabrać)"
                menu:
                    "{b}Dobra chodź ze mną{b}":
                        jump akszuli

                    "{b}Jakoś sobie poradzisz{/b}":
                        luszcz "Jakoś sobie poradzisz"

                        cid "To przynajmniej w podziękowaniu weź tą Tutorialową Wodę Święconą którą udało mi się ukraść z kościoła"

                        $ ile_item += 1
                        $ woda += 1
                        hide screen global_eq_key
                        show screen global_eq_key

                        cid "Włożyłem ją do twojego ekwipunku"
                        cid "Wiedziałeś że wciskając E możesz otworzyć ekwipunek?"

                        jump wodaswiecona
        label akszuli:
            luszcz "Akszuli…"
            luszcz "Jestem na misji żeby przekonać mieszańców Skały do przeciwstawienia się księdzu który dla własnego dobra sprzedaje nas i naszą Ojczyznę."
            luszcz "Każda pomoc by się przydała."
            luszcz "Nawet jeśli jesteś niepełnosprawny"

            cid "To byłby mój zaszczyt"
            cid "Już nigdy nie będę lizał stópek autorytetom!"

            $ eminem_sojusznik = 1
            $ liczba_sojusznikow += 1

            luszcz "cacy"

            cid "O właśnie"
            cid "W ramach podziękowania mam dla ciebie Tutorialową Wodę Święconą którą udało mi się ukraść z kościoła"

            $ ile_item += 1
            $ woda += 1
            hide screen global_eq_key
            show screen global_eq_key

            cid "Włożyłem ją do twojego ekwipunku"
            cid "Wiedziałeś że wciskając E możesz otworzyć ekwipunek?"

            menu:
                "{b}Tak{/b}":
                    luszcz "oczywiście że tak"
                    luszcz "dzięki za leczonko"

                    cid "Nie ma sprawy"
                    $ eminem_wybory = 2

                    luszcz "Dobra, to tym razem serio"
                    luszcz "Gdzie by się najpierw wybrać?"

                    hide luszcz
                    hide eminem
                    play music "audio/music/pole.mp3"
                    jump rynek
                
                "{b}Nie{/b}":
                    luszcz "oczywiście że nie"
                    luszcz "dzięki za leczonko"

                    cid "Nie ma sprawy"
                    $ eminem_wybory = 2

                    luszcz "Dobra, to tym razem serio"
                    luszcz "Gdzie by się najpierw wybrać?"

                    hide luszcz
                    hide eminem
                    play music "audio/music/pole.mp3"
                    jump rynek
        
        label wodaswiecona:
            menu:
                "{b}Tak{/b}":
                    luszcz "oczywiście że tak"
                    luszcz "dzięki za leczonko"

                    cid "Nie ma sprawy, miłego życia"

                    luszcz "Miłego"
                    $ eminem_wybory = 1

                    hide eminem
                    show luszcz neutral at center

                    "{i}*Cid odchodzi z grymasem bólu na twarzy*{/i}"

                    luszcz "Dobra, to tym razem serio"
                    luszcz "Gdzie by się najpierw wybrać?"

                    hide luszcz
                    hide eminem
                    play music "audio/music/pole.mp3"
                    jump rynek

                "{b}Nie{/b}":
                    luszcz "oczywiście że nie"
                    luszcz "dzięki za leczonko"

                    cid "Nie ma sprawy, miłego życia"

                    luszcz "Miłego"
                    $ eminem_wybory = 1

                    hide eminem
                    show luszcz neutral at center

                    "{i}*Cid odchodzi z grymasem bólu na twarzy*{/i}"

                    luszcz "Dobra, to tym razem serio"
                    luszcz "Gdzie by się najpierw wybrać?"

                    hide luszcz
                    hide eminem
                    play music "audio/music/pole.mp3"
                    jump rynek




                
            



