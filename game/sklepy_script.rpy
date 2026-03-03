label sklepy_define:
    default monopolowy_den = 0
    default monopolowy_jabole = 0
    default monopolowy_drpepper = 0
    default monopolowy_royal = 0
    default monopolowy_granat = 0
    default lag = 0
    default os = 0
    default mieso = 0
    default samosamo = 0
    default chinczyk_den = 0
    default chinczyk_banany = 0
    default chinczyk_przepychaczka = 6
    default chinczyk_klata = 6
    default chinczyk_slownik = 1


label sklepy:
    label sklep_monopolowy:
        play music "audio/music/monopolowy.mp3"
        scene bg monopolowy with fade
        show luszcz neutral at left
        show braun neutral at right

        braun "Szczęsć boże"

        label sklep_monopolowy2:
            $ config.menu_include_disabled = True
            if timer >= 0 and timer <= 1440 and monopolowy_den == 0: 
                $ monopolowy_den = 1
                $ monopolowy_jabole = 3
                $ monopolowy_drpepper = 4
                $ monopolowy_royal = 3
                $ monopolowy_granat = 3
            if timer >= 1441 and timer <= 2880 and monopolowy_den <= 1:  
                $ monopolowy_den = 2
                $ monopolowy_jabole = 3
                $ monopolowy_drpepper = 4
                $ monopolowy_royal = 5
                $ monopolowy_granat = 2
            if timer >= 2881 and timer <= 4320 and monopolowy_den <= 2: 
                $ monopolowy_den = 3
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 4
                $ monopolowy_royal = 2
                $ monopolowy_granat = 3
            if timer >= 4321 and timer <= 5760 and monopolowy_den <= 3: 
                $ monopolowy_den = 4
                $ monopolowy_jabole = 3
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 4
                $ monopolowy_granat = 1
            if timer >= 5761 and timer <= 7200 and monopolowy_den <= 4: 
                $ monopolowy_den = 5
                $ monopolowy_jabole = 5
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 4
                $ monopolowy_granat = 2
            if timer >= 7201 and timer <= 8640 and monopolowy_den <= 5: 
                $ monopolowy_den = 6
                $ monopolowy_jabole = 6
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 2
                $ monopolowy_granat = 4
            if timer >= 8641 and timer <= 10080 and monopolowy_den <= 6:
                $ monopolowy_den = 7
                $ monopolowy_jabole = 5
                $ monopolowy_drpepper = 2
                $ monopolowy_royal = 3
                $ monopolowy_granat = 3
            if timer >= 10081 and timer <= 11520 and monopolowy_den <= 7:
                $ monopolowy_den = 8
                $ monopolowy_jabole = 6
                $ monopolowy_drpepper = 2
                $ monopolowy_royal = 2
                $ monopolowy_granat = 4
            menu:
                "{b}Co kupić?{/b}"

                "{b}Jabole x 4 (1 💰){/b}" if monopolowy_jabole > 0 and money >= 1:
                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 4
                    $ monopolowy_jabole -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Jabole x 4 zostały dodane do ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}DrPepper x 2 (1 💰){/b}" if monopolowy_drpepper > 0 and money >= 1:
                    if drpepper == 0:
                        $ ile_item += 1
                    $ drpepper += 2
                    $ monopolowy_drpepper -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*DrPepper x 2 został dodany do ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Royal Cola x 2 (1 💰){/b}" if monopolowy_royal > 0 and money >= 1:
                    if royal == 0:
                        $ ile_item += 1
                    $ royal += 2
                    $ monopolowy_royal -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Royal Cola x 2 została dodana do ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Granat x 2 (2 💰){/b}" if monopolowy_granat > 0 and money >= 2:
                    if granat == 0:
                        $ ile_item += 1
                    $ granat += 2
                    $ monopolowy_granat -= 1
                    $ money -= 2
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Granat x 2 został dodany do ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{i}Powrót{/i}":
                    $ config.menu_include_disabled = False
                    braun "Bóg zapłać"
                    hide braun 
                    hide luszcz
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump alejka
        
    label kebab:
        $ mieso = 0
        $ os = 0
        $ lag = 0
        $ samosamo = 0
        play music "audio/music/kebab.mp3"
        scene bg kebab with fade
        show luszcz neutral at left
        if toxic_pea_social_link == 0:
            show toxic_pea neutral at right

        luszcz "Dzień dobry"

        $ config.menu_include_disabled = True
        menu:
            "{b}Czy na pewno chcę kebaba?{/b}"

            "{b}Tak (1 💰){/b}" if money >= 2:
                $ ykebab = 1
                play sound "audio/sfx/kupno.mp3"
                $ config.menu_include_disabled = False
                $ money -= 1
                luszcz "Chciałbym zamówić kebaba…"
                menu:
                    "{b}Jakiego kebaba chcę..?{/b}"

                    "{b}Zwykły{/b}":
                        $ mieso = 1

                    "{b}Samo mięso{/b}":
                        $ mieso = 1
                        $ samosamo = 1
                        luszcz "Z samym mięsem..."

                    "{b}Bez mięsa{/b}":
                        luszcz "Bez mięsa..."

                if mieso == 1:
                    menu:
                        "{b}Jakie mięso chcę..?{/b}"

                        "{b}Baranina{/b}":
                            luszcz "Baranina"

                        "{b}Wołowina{/b}":
                            luszcz "Wołowina"

                        "{b}Kurczak{/b}":
                            luszcz "Kurczak"
                        
                        "{b}Miszany{/b}":
                            luszcz "Mięso miszane"
                
                menu:
                    "{b}Jaki sos chcę..?{/b}"

                    "{b}Sos ostry{/b}":
                        $ os = 1
                        luszcz "Sos ostry"

                    "{b}Sos łagodny{/b}":
                        $ lag = 1
                        luszcz "Sos łagodny"


                turek "Robi się szefie 😊"

                turek "turturtur tur"
                turek "tur tur tur tur tur"
                turek "tur turtur"

                if mieso == 0 and toxic_pea_social_link == 0:
                    toxic "Obrzydliwe…"
                    toxic "Ej ty, nie jadasz mięsa czy coś?"
                    luszcz "Nie no, jem, ale teraz dla odmiany sobie odpóściłem… Chciałem zobaczyć jak posmakuje~~"
                    toxic "To może ci dla odmiany wybombie i zobaczę jak się błagasz o litość"

                    show luszcz blush at left

                    toxic "Wy byście tylko próbowali i próbowali"
                    toxic "Aż wszystko zwiędnie"
                    toxic "Szkoda strzępić…"

                    $ toxic_pea_social_link = 10
                    $ toxic_pea_wybory = 0
                    hide toxic_pea
                    show luszcz neutral at left

                else:
                    "{i}…{/i}"

                turek "Proszę gotowe smacznego!"

                if lag == 1:
                    if lagodny == 0:
                        $ ile_item += 1
                    $ lagodny += 1
                    "{i}Kebab Łagodny został dodany do ekwipunku{/i}"

                if os == 1:
                    if ostry == 0:
                        $ ile_item += 1
                    $ ostry += 1
                    "{i}Kebab Ostry został dodany do ekwipunku{/i}"

                luszcz "Dziękuję panie turek!"
                luszcz "Serwus!"

                if samosamo == 1 and toxic_pea_social_link == 0:
                    toxic "Ej ty"
                    toxic "Dobry wybór"
                    toxic "Nikt tutaj poza naszą dwójką nie jada z samym mięsem"

                    show luszcz blush at left

                    luszcz "Ah… tak?"

                    turek "Zgadza się!"

                    luszcz "No widzisz, co za niespodzianka"

                    show luszcz neutral at left

                    luszcz "Ci inni ludzie… głupi… co ciągle tylko by.. Jedli warzywa i deptali po trawie"

                    toxic "No dosłownie"

                    luszcz "A wiesz że nawet nie lubie niektórych warzyw? Tak kompletnie?"

                    toxic "Erm.. yeah, ja czasem też"
                    toxic "Uroczy jesteś, chciałbyś może pozbijać trochę zombiaków z mojego trawnika w nocy?"

                    luszcz "Oh..! Um…. pewnie!"

                    toxic "Masz mój adres, mieszkam koło Wołbrymskiej"

                    luszcz "Okej… dzięki! Widzimy się! W nocy!"

                    toxic "Pewnie, narka"

                    $ toxic_pea_social_link = 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump bohaterow_wrzesnia


                
            "{b}Nie{/b}":
                $ config.menu_include_disabled = False
                luszcz "do widzenia"
                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump bohaterow_wrzesnia

    label chinczyk:
        play music "audio/music/chinczyk.mp3"
        scene bg chinczyk with fade
        show luszcz neutral right at slightright

        daj "Witam serdecznie!"

        luszcz "Pokaż mi swoje towary."

        label chinczyk2:
            $ config.menu_include_disabled = True
            if timer >= 0 and timer <= 1440 and chinczyk_den == 0: 
                $ chinczyk_den = 1
                $ chinczyk_banany = 2
            if timer >= 1441 and timer <= 2880 and chinczyk_den <= 1:  
                $ chinczyk_den = 2
                $ chinczyk_banany = 3
            if timer >= 2881 and timer <= 4320 and chinczyk_den <= 2: 
                $ chinczyk_den = 3
                $ chinczyk_banany = 2
            if timer >= 4321 and timer <= 5760 and chinczyk_den <= 3: 
                $ chinczyk_den = 4
                $ chinczyk_banany = 1
            if timer >= 5761 and timer <= 7200 and chinczyk_den <= 4: 
                $ chinczyk_den = 5
                $ chinczyk_banany = 4
            if timer >= 7201 and timer <= 8640 and chinczyk_den <= 5: 
                $ chinczyk_den = 6
                $ chinczyk_banany = 3
            if timer >= 8641 and timer <= 10080 and chinczyk_den <= 6:
                $ chinczyk_den = 7
                $ chinczyk_banany = 2
            if timer >= 10081 and timer <= 11520 and chinczyk_den <= 7:
                $ chinczyk_den = 8
                $ chinczyk_banany = 2
            menu:
                "{b}Co kupić?{/b}"

                "{b}Kiść Bananów x 3 (2 💰){/b}" if chinczyk_banany > 0 and money >= 2:
                    if banany == 0:
                        $ ile_item += 1
                    $ banany += 3
                    $ chinczyk_banany -= 1
                    $ money -= 2
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Kiść Bananów x 3 została dodana do ekwipunku*{/i}"
                    jump chinczyk2
                
                "{b}Przepychaczka x 1 (4 💰){/b}" if chinczyk_przepychaczka > 0 and money >= 4:
                    $ przepychaczka_liczba += 1
                    if luszcz_przepychaczka == 0 and urban_przepychaczka == 0 and zyd_przepychaczka == 0 and kazuma_przepychaczka == 0 and tarczownik_przepychaczka == 0:
                        $ luszcz_przepychaczka = 1
                        $ urban_przepychaczka = 1
                        $ zyd_przepychaczka = 1
                        $ kazuma_przepychaczka = 1
                        $ tarczownik_przepychaczka = 1
                        $ eminem_przepychaczka = 1
                    $ chinczyk_przepychaczka -= 1
                    $ money -= 4
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Przepychaczka x 1 została dodana do ekwipunku*{/i}"
                    jump chinczyk2
                
                "{b}Diamentowa Klata x 1 (4 💰){/b}" if chinczyk_klata > 0 and money >= 4:
                    $ klata_liczba += 1
                    if luszcz_klata == 0 and urban_klata == 0 and zyd_klata == 0 and kazuma_klata == 0 and tarczownik_klata == 0 and eminem_klata == 0:
                        $ luszcz_klata = 1
                        $ urban_klata = 1
                        $ zyd_klata = 1
                        $ kazuma_klata = 1
                        $ tarczownik_klata = 1
                        $ eminem_klata = 1
                    $ chinczyk_klata -= 1
                    $ money -= 4
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Diamentowa Klata x 1 została dodana do ekwipunku*{/i}"
                    jump chinczyk2

                "{b}Rozmówki polsko-chińskie (1 💰){/b}" if chinczyk_slownik > 0 and money >= 1:
                    $ ile_item_fabularne += 1
                    $ slownik = 1
                    $ chinczyk_slownik -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Rozmówki polsko-chińskie zostały dodane do ekwipunku*{/i}"
                    jump chinczyk2
                
                "{i}Powrót{/i}":
                    $ config.menu_include_disabled = False
                    daj "Do widzenia" 
                    hide luszcz
                    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                        play music "audio/music/pole.mp3"
                    else:
                        play music "audio/music/pole_noc.mp3"
                    jump granica