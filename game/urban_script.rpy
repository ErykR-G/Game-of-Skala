
label urban:
    label urban1:
        scene bg przed_dom_kultury
        show luszcz neutral at center

        luszcz "czyli to ten dom kóltury"
        luszcz "dobra tszeba iść, żeby przekonać skaliczan do walki z księdzem natankiem "
        luszcz "mam nadzieje ze bedzie ok"

        scene bg dom_kultury
        play music "audio/music/dom_kultury.mp3"

        show luszcz neutral at left
        show mclowicz neutral at center
        show staruchy at right

        luszcz "dzień dobry, panie robercie"

        mclowicz "a więc to ty jesteś tym eeeeeee buntownikiem"

        luszcz "tak, chciałbym bardzo panu podziękować za udostępnienie sali"

        mclowicz "iiii w gruncie rzeczy to eeee jestem po twojej stronie, eeeee ale jakby co to się nie znamy"
        mclowicz "mam obok restauracje iiiiii eee nie chce się narażać władzy"
        mclowicz "więc ten eeeeee, ja ide zbierać koperek i jakby co to cie nie widziałem dobra?"

        luszcz "zrozumiałem"

        mclowicz "a i masz eeeee około 20 minut zanim powinna się zjawić inkwizycja eeeeee kościelna, także dobrze by było jakbyś zniknął zanim przyjdą"

        luszcz "dziekuje za ostrzeżenie"

        hide mclowicz
        show luszcz at center

        "{i}Łuszcz wchodzi na scene{/i}"

        luszcz "kochani!!!"
        luszcz "nastały ciężkie czasy"
        luszcz "skała została zaatakowana"
        luszcz "niejaki ksionc Natanek zuzurbował skalny tron"
        luszcz "kler zajoł nasze ukochane miasto"
        luszcz "a to jeszcze nie najgorsza informacja"
        luszcz "ten katol chce przyłonczyć skałe do krakowa!!!"
        luszcz "nie możemy na to pozwolić"
        luszcz "jak żyję, przysięgam bronić suwerenności naszego domu"
        luszcz "ale nie dam sobie rady sam"
        luszcz "stworze fundacje suwerenna skala na którą będziecie mogli wpłacać swoje ciężko zarobione pienionszki"
        luszcz "tylko wasze wpłaty mogą uratować skale"
        luszcz "obiecuje że przynajmniej część nie zostanie zdefrałdowana"
        luszcz "dlatego proszę zebyscie z sercem wsłuchali w nastempójonce słowa"
        luszcz "wyklenty powstań, lódó ziemi"
        luszcz "Powstańcie, których drenczy głut."
        luszcz "pamientajcie, morzemy ich powstrzymać, ale musimy się zjednoczyć"
        luszcz ".........."
        luszcz "to jak pomożecie?"

        all "......."
        all "zzzzzz"
        all "......."

        luszcz "chyba dobrze mi poszło"

        "{i}Łuszcz schodzi ze sceny{/i}"

        show luszcz at left

        show czarodziej neutral right at slightright

        czarodziej  "dupa a nie pomożemy"

        luszcz "co?"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "gówno hahahahaha pieprzyć"

        luszcz "a ten co to za guwniak"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "jesteś gupi jeśli myślisz, że coś zdziałasz dupa dupa"

        luszcz "a ty co turreta masz?"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "dupa pieprzyć cie dupa"

        luszcz "to mogę ci pomoc"
        luszcz "tata mówił, że wystarczy pas na dópe, żeby wyleczyć wszystkie horoby"
        luszcz "i faktycznie na mnie działało"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "odsun się pieprzyć"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "jestem potenznym czarodziejem dupa dupa"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "zanim cie zabije chciałbym ci zadac jedno pytanie"  

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "czy chciałbyś może porozmaiać o tym co stało się z magami ognia?"

        luszcz "nie?" 

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "no właśnie a powinieneś dupa pieprzyć"

        luszcz "wiesz jeszcze chyba przyjmują w oknie życia"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "AAAAA DUPA PIEPRZYĆ"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        "{i}Czarodziej zaczyna castować jakiś spell{/i}"

        nikt "nie tak szybko"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "co do dupy"

        show urban neutral right at left
        show luszcz neutral:
            xalign 0.3
            yalign 1.0

        czarodziej "myślałem, że już nie żyjesz"

        urban "prima aprilis skurwysynie"

        urban "sam sobie z nim nie dasz rady"
        urban "może nie wygląda na silnego ale z wielkim autyzmem wiąże się wielka siła"
        urban "jednak w dwójke możemy sobie poradzić"
        urban "wystarzy spuscic mu wpierdol, a pas już mam"
        urban "więc jeśli pozwolisz"

        luszcz "w takim razie zaczynajmy"

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        $ renpy.pause(0.1)

        show czarodziej neutral2 right at slightright
        $ renpy.pause(0.1)
        show czarodziej neutral right at slightright

        czarodziej "dupa dupa"

        $ urban_sojusznik = 1
        $ liczba_sojusznikow += 1

        jump fight91

        label after_fight91:
            scene bg dom_kultury
            $ urban_sojusznik = 0
            $ liczba_sojusznikow -= 1
            show luszcz neutral at slightleft
            show urban neutral at slightright
            luszcz "o jacie jacie, ale ma pan wielkie usz.... eeee znaczy dziekuje za pomoc"

            urban "jeszcze mi nie dziękuj, bardzo mnie ruszyła twoja przemowa"
            urban "a poza tym tez nie nawidze tych szalonych katoli"
            urban "nazywam się jerzy i mogę ci pomoc walczyc z natankiem"

            luszcz "witam ja jeste---"

            urban "nie obchodzi mnie kim jesteś"
            urban "ale jestem w stanie zebrać kolegów i cie wspomóc"
            urban "ale nie tutaj o tym, za chwile przybędzie tu inkwizycja"
            urban "przyjdź do bunkra przy skalnej granicy"

            luszcz "rodzice mowili żeby nie spotykać się z jakimiś starymi dziadami w podejrzanych miejscach"
            luszcz "takze chyba musze powiedzieć" 
            luszcz "jasne bende" 

            urban "w takim razie widzimy się na miejscu"

            $ urban_wybory = 1
            $ urban_social_link = 1

            play music "audio/music/pole.mp3"
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
    
    label urban2:
        play music "audio/music/natura.mp3"
        scene bg bunkier3 with fade
        show luszcz neutral at center
        luszcz "To chyba tutaj"

        scene bg bunkier
        show luszcz neutral at left
        show urban neutral at center
        show jaruzel neutral at slightright
        show girek neutral at right
        play music "audio/music/redsun.mp3"
        urban "o witaj młodzieńcze"
        urban "wiedziałem, że przyjdziesz"
        urban "pozwól, że przedstawie ci moich towarzyszy"
        urban "to jest wojtek"

        jaruzel "czołem"

        urban "a to edward"

        girek "Здравствуйте (zdrastwujtie) eeee znaczy witam"

        luszcz "dzien dobry" 

        urban "to są moi koledzy z PZPR"

        luszcz "w sensie z polskiego związku piłki ręcznej?"

        urban "eee no coś takiego" 
        urban "towarzysze, w skale władze przejął jakiś ksiądz"
        urban "władza centralna obiecała nam autonomie, ale on raczej tego nie uszanuje"

        girek "to wyśle się jakiegoś moherowego agenta z trucizną i po problemie"

        urban "obawiam się, że tym razem to nie zadziała"

        jaruzel "zanim jeszcze zeszliśmy do podziemia to byłaby to opcja"
        jaruzel "ale ostatnio już ledwo nam wyszło nie możemy robie pozwolić"
        jaruzel "a dodatkowo wygląda jakby ten sekciarz miał dobrą ochronę"

        girek "gdyby tylko nie papieżak to byśmy nie musieli siedzieć w tym gównie"

        luszcz "ej ale od papaja to ty się odwal"
        luszcz "ojciec swienty to był przecież największy polak na świecie"
        luszcz "a nawet...."
        luszcz "w polsce"

        jaruzel "a ten to skąd się urwał, że papieża wyznaje?"

        girek "te jerzy skąd ty kto przywlokłeś"
        girek "on mi wygląda na kuca"
        girek "i jeszcze zaraz nam zacznie o sprzedaży paróweczek gadać"

        luszcz "co? o czym on mówi"

        urban "hmmm"
        urban "hmmhmhmmm"
        urban "chyba jesteś gotowy by pozwać prawdę"
        urban "być może słyszałeś, że 3 dekady temu"
        urban "na podstawie obrad kulistego stołu dokonano przemiany ustrojowej"
        urban "to powszechny fakt"
        urban "jednak tylko nieliczny wiedzą o tajnym protokole Urban-Wałęsa"

        luszcz "czyli dlatego jeszcze nie siedzicie, ani w więzieniu, ani Choroszczy?"

        urban "dokładnie, a nawet lepiej" 
        urban "prowadzimy gabinet cienia, który kontroluje obecny rząd"

        luszcz "czyli to wszystko jednak wasza wina, a nie tuska!?"

        urban "nie no wina tuska są bardzo smaczne, mamy spory zapas"
        urban "chcesz trochę?"

        luszcz "bardzo chent---"

        jaruzel "DOŚĆ"
        jaruzel "jak nie załatwimy natanka to ogarną, że podbieramy wina z pobliskich parafii"
        jaruzel "i nie można pić przed pracą"

        girek "nie no, można tylko trzeba wstawać rano, na tym polega odpowiedzialność"
        girek "poza tym w Polsce to nie da się na trzeźwo"

        urban "co prawda to prawda ale nie o tym teraz"
        urban "faktycznie trzeba teraz popracować"
        urban "awięc tak jak mówiłem"
        urban "PRL nigdy nie umarł zmienił tylko forme"

        luszcz "i wałesa się na to po prostu zgodził?"

        urban "nie było łatwo, musiałem zaspokoić jego ego a jak wiadomo jest one po prostu kuuuurwa gigantyczne"
        urban "straciłem tam większość mojej godności, ale było warto"
        urban "dzięki mojemu poswieceniu komuna w Polsce przetrwala"
        urban "i zaczela się nawet przelewac do brukseli"

        luszcz "czyli braun miał racje o eurokołhozie!?"

        urban "nie potwierdzam, nie zaprzeczam"
        urban "ale jakby okazało się ze skończy tak jak Lepper, to na pewno będzie to przypadek"

        luszcz "to są te całe kremlowskie metody?"

        urban "najlepsze techniki FSB, sam putin nam je przekazywał"

        urban "wróćmy do sedna naszej dyskusji"
        urban "powiem ci jaki mamy plan na pokonanie księdza natanka"       
        urban "jednak chciałbym ci przedstawić pewną ofertę"
        urban "przejdźmy do ustronnego pokoju"

        luszcz "chyba nie chcesz mnie teraz zgwałcić?"

        urban "obrzydliwy jesteś, zamknij się bo jeszcze zmienie zdanie"

        scene bg bunkier2
        show urban neutral right at slightleft
        show luszcz neutral right at slightright

        luszcz "dobra to co to za oferta"

        urban "ksiądz natanek to tylko czubek góry lodowej"
        urban "następnie będzie trzeba pokonać masonów, burżuji i inne kapitalistyczne szuje"
        urban "będziemy walczyć dopóki nie osiągniemy rewolucji światowej i obalimy cały zachód"
        urban "jednakże, żeby tego dokonać trzeba pozmieniać stare i zepsute części"
        urban "wyświadcze ci przysługe i ci pomoge, ale najpierw musisz zrobić coś dla mnie"

        luszcz "zamieniam się w słuch"

        urban "jak to stalin mówił, chwilę przed wojną trzeba zrobić czystkę we własnej partii"
        urban "bez urazy ale od chlania przez 30 lat stracili większość sprawności umysłowych"
        urban "a poza tym już mnie świerzbi reka tak dawno nie popelnialem rzadnych zbrodni wojennych"    

        luszcz "co racja to racja, tez tesknie za strzelaniem do bosniakow"
        luszcz "ale skoro poprzebujemy ludzi do walki z natankiem to nie warto zrobić tego, nie wiem innym razem"

        urban "nie no z nimi to było by za latwo wiec trzeba trochę podnieść poziom trudnosci"
        urban "jeszcze skonczylibyscie gre z 10 minut, a tak nie można"

        luszcz "co? jaka gra? jacy wy?"

        urban "....."
        urban "oj wymskło mi się"
        urban "w każdym razie zaraz po czystce trzeba by było obczaić tą [[następna lokacja]"

        luszcz "no ja nie wiem czy się zgadzam na coś takiego"

        urban "no chłopie nie wydziwiaj, zrób to dla fabuły"

        luszcz "eeeeem"

        urban "to jak dołączysz do mnie?"

        menu:
            "{b}nigdy komóhy{/b}":
                luszcz "nigdy komóhy, znacie takie przysłowie? ONRowcy wymyślili [[COŚ], a na drzewie zamiast liści bendom wisieć komónisći"  
                urban "ale czemu?"
                urban "przecież cytowałeś międzynarodówkę na wiecu"

                luszcz "naprawdę? a to missclick"

                urban "myślałem że jesteś mądrzejszy, ale najwyraźniej się myliłem"
                urban "w każdym razie wybrałeś śmierć"

                luszcz "cichaj stary dziadzie, dzwonie na psy i was zamknom w 3 sekundy"

                urban "chłopie przecież połowa policji to jeszcze w zomo służyła, nic ci to nie da"

                luszcz "no cusz, chciałem po dobroci"
                luszcz "teraz bende mósiał was zabić"

                urban "Edward, wojtek!!! chodzcie tu"
                urban "trzeba tu naklepać jednemu libkowi"

                luszcz "simierć wrogom ojczyzny!!!"

                jump fight111

                label after_fight111:
                    play music "audio/music/redsun.mp3"
                    scene bg bunkier2
                    show luszcz neutral at center
                    luszcz "no szkoda, myślałem, że się dogadamy"
                    luszcz "ale babcia jednak miała dobre powiedzenie"
                    luszcz "”dobry komóh to martwy komóh”"


                    scene bg bunkier3
                    play music "audio/music/natura.mp3"
                    show luszcz neutral at center

                    luszcz "no cusz, nie wiem czego się spodziewałem, ale na pewno nie tego"
                    luszcz "mam wrażenie jakby to była strata czasu, oby nie był to decydujący czynnik"

                    $ urban_wybory = 10
                    $ urban_social_link = 10

                    play music "audio/music/pole.mp3"
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

            "{b}no dobra{/b}":
                luszcz "no dobra, w sumie wujek to jednak miał rację, pomogę ci"

                urban "zuch chłopak"
                urban "jak nam się uda to nawet dam ci order przodownika pracy"
                urban "dobra to chodz ich nakl-----"

                show jaruzel neutral at slightright
                show girek neutral at right
                show urban neutral right at left
                show luszcz neutral at slightleft

                jaruzel "i ty urbanie przeciwko nam?"
                jaruzel "a stalin mówił, żeby nie ufać żydom"

                urban "chłopaki, to nie tak"

                girek "zamknij się, jesteś elementem wywrotowym"
                girek "moskwa się o tym dowie"

                urban "a wsadz se w dupe ta twoją moskwe"

                jaruzel "a skoncz pierdolić i walcz jak czlowiek" 

                urban "z przyjemnoscią"
                urban "na nich"

                $ urban_sojusznik = 1
                $ liczba_sojusznikow += 1

                jump fight101

                label after_fight101:
                    play music "audio/music/redsun.mp3"
                    scene bg bunkier2
                    show luszcz neutral at slightleft
                    show urban neutral at slightright

                    $ urban_sojusznik = 0
                    $ liczba_sojusznikow -= 1

                    urban "dziekuje ci, dzięki tobie światowa rewolucja będzie mogla rokwitnac na całym swiecie"

                    $ urban_sojusznik = 1
                    $ liczba_sojusznikow += 1

                    urban "wywiązałeś się ze swojej części umowy, jestem teraz to twojej dystozycji"

                    luszcz "w takim razie, za mną"

                    scene bg bunkier3
                    play music "audio/music/natura.mp3"
                    show luszcz neutral at slightleft
                    show urban neutral at slightright

                    luszcz "nie wiem czego się spodziewałem po tym bunkrze, ale na pewno nie tego"
                    luszcz "w każdym razie czuje, że jestem coraz bliżej obalenia ksieńca natanka "

                    $ urban_wybory = 2
                    $ urban_social_link = 2

                    play music "audio/music/pole.mp3"
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





