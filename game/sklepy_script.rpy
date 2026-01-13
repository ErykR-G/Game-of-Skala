label sklepy:
    label sklep_monopolowy:
        play music "audio/music/monopolowy.mp3"
        show bg monopolowy
        show luszcz neutral at left
        show braun neutral at right

        braun "Szczęsć boże"

        label sklep_monopolowy2:
            menu:
                "{b}Co kupić?{/b}"

                "{b}Masło{/b}":
                    "{i}*Masło zostało dodane do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Margaryna{/b}":
                    "{i}*Margaryna została dodana do twojego ekwipunku*{/i}"
                    jump sklep_monopolowy2
                
                "{b}Powrót{/b}":
                    braun "Bóg zapłać"
                    hide braun 
                    hide luszcz
                    jump alejka