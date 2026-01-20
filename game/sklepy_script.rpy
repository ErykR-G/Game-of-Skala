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
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 1441 and timer <= 2880 and monopolowy_den == 1:  
                $ monopolowy_den += 1
                $ monopolowy_jabole = 2
                $ monopolowy_drpepper = 2
                $ monopolowy_royal = 1
                $ monopolowy_granat = 4
            if timer >= 2881 and timer <= 4320 and monopolowy_den == 2: 
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 4321 and timer <= 5760 and monopolowy_den == 3: 
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 5761 and timer <= 7200 and monopolowy_den == 4: 
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 7201 and timer <= 8640 and monopolowy_den == 5: 
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 8641 and timer <= 10080 and monopolowy_den == 6:
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            if timer >= 10081 and timer <= 11520 and monopolowy_den == 7:
                $ monopolowy_den += 1
                $ monopolowy_jabole = 4
                $ monopolowy_drpepper = 3
                $ monopolowy_royal = 3
                $ monopolowy_granat = 2
            menu:
                "{b}Co kupić?{/b}"

                "{b}Jabole x 2 (1 💰){/b}" if monopolowy_jabole > 0 and money >= 1:
                    if jabole == 0:
                        $ ile_item += 1
                    $ jabole += 2
                    $ monopolowy_jabole -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Jabole x 2 zostały dodane do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}DrPepper (1 💰){/b}" if monopolowy_drpepper > 0 and money >= 1:
                    if drpepper == 0:
                        $ ile_item += 1
                    $ drpepper += 1
                    $ monopolowy_drpepper -= 1
                    $ money -= 1
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*DrPepper został dodany do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Royal Cola (2 💰){/b}" if monopolowy_royal > 0 and money >= 2:
                    if royal == 0:
                        $ ile_item += 1
                    $ royal += 1
                    $ monopolowy_royal -= 1
                    $ money -= 2
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Royal Cola została dodana do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Granat (2 💰){/b}" if monopolowy_granat > 0 and money >= 2:
                    if granat == 0:
                        $ ile_item += 1
                    $ granat += 1
                    $ monopolowy_granat -= 1
                    $ money -= 2
                    play sound "audio/sfx/kupno.mp3"
                    "{i}*Granat został dodany do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{i}Powrót{/i}":
                    $ config.menu_include_disabled = False
                    braun "Bóg zapłać"
                    hide braun 
                    hide luszcz
                    play music "audio/music/pole.mp3"
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

            "{b}Tak (2 💰){/b}" if money >= 2:
                play sound "audio/sfx/kupno.mp3"
                $ config.menu_include_disabled = False
                $ money -= 2
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

                play music "audio/music/pole.mp3"
                jump bohaterow_wrzesnia


                
            "{b}Nie{/b}":
                $ config.menu_include_disabled = False
                luszcz "dowidzenia"
                play music "audio/music/pole.mp3"
                jump bohaterow_wrzesnia
