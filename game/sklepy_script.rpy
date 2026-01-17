label sklepy_define:
    define monopolowy_den = 0
    define monopolowy_jabole = 0
    define monopolowy_drpepper = 0
    define monopolowy_royal = 0
    define monopolowy_granat = 0

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
        play music "audio/music/kebab.mp3"
        scene bg kebab with fade
        show luszcz neutral at left
        show toxic_pea neutral at right

        luszcz "Dzień dobry"
