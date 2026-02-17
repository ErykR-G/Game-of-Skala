default yusuke_timer = 0
default obraz_kebab = 0
default kebab_wyruchany = 0

default ykebab = 0

label yusuke:
    label yusuke1:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj24 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj23 with fade

        else:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj18 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj17 with fade

        show luszcz neutral right at slightright
        show yusuke neutral at slightleft2
        
        yusuke "Witaj mistrzu. Jeśli chcesz, możemy iść szukać inspiracji."
        yusuke "Czy masz jakieś miejsce na oku?"

        menu:
            "{b}Nie teraz{/b}":
                luszcz "Nie teraz nie idziemy"
                luszcz "Tylko sobie przyszedłem na ciebie popatrzeć"

                yusuke "To zaszczyt mistrzu."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"

                if rynek == 1:
                    jump rynek
                if sloneczna == 1:
                    jump sloneczna 
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

            "{b}🛒 Kebab (2 💰)(15min){/b}" if (money >= 2 and ykebab >= 1 and kebab_wyruchany == 0) and ((timer >= 660 and timer <= 1380) or (timer >= 2100 and timer <= 2820) or (timer >= 3540 and timer <= 4260) or (timer >= 4980 and timer <= 5700) or (timer >= 6420 and timer <= 7140) or (timer >= 7860 and timer <= 8580) or (timer >= 9300 and timer <= 10020) or (timer >= 10740 and timer <= 11460)):
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                $ kebab_wyruchany = 1

                yusuke "Nie wiem czy słyszałem kiedykolwiek takie słowo."
                yusuke "“Kebab”"

                luszcz "Takie jedzenie"
                luszcz "Chodź zobaczysz"

                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade
                $ mieso = 0
                $ os = 0
                $ lag = 0
                $ samosamo = 0
                play music "audio/music/kebab.mp3"
                scene bg kebab with fade
                show luszcz neutral at left
                show yusuke neutral right at center
                if toxic_pea_social_link == 0:
                    show toxic_pea neutral at right

                luszcz "Poproszę dwa kebaby.."

                $ money -= 2
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
                
                turek "Dobrze a drugi?"

                luszcz "Yusuke jakiego chcesz kebaba?"

                yusuke "Hm… wezmę to co ty."

                luszcz "Dwa takie same"

                turek "Robi się szefie 😊"
                turek "turturtur tur"
                turek "tur tur tur tur tur"

                luszcz "Uwierz mi to będzie najlepsza rzecz jaką kiedykolwiek jadłeś"

                yusuke "Wierzę ci mistrzu"

                turek "tur turtur"

                "{i}…{/i}"

                turek "Proszę gotowe smacznego!"

                luszcz "Dziękuję"

                yusuke "Dziękuję również"

                "{i}*łuszczu zjada szybko*{/i}"

                yusuke "Hm… ale potwór"
                yusuke "Dobrze czas na degustację"

                "{i}*am*{/i}"

                if mieso == 1 and samosamo == 1:
                    yusuke "…wybacz mi, ale czy to nie jest samo mięso w cieście?"

                    luszcz "No pychota"

                    yusuke "Dobre mięso nie jest złe."
                    yusuke "Ale nie widzę w tym niczego wyjątkowego. Może spróbujmy następnym razem iść gdzie indziej?"

                if mieso == 0 and samosamo == 0:
                    yusuke "…wybacz mi, ale czy to nie jest sałatka w cieście?"

                    luszcz "Zgadza się…"

                    yusuke "Znaczy, jest dobra."
                    yusuke "Ale nie widzę w tym niczego wyjątkowego. Może spróbujmy następnym razem iść gdzie indziej?"


                if mieso == 1 and samosamo == 0:
                    $ obraz_kebab = 1
                    $ yusuke_social_link += 1

                    yusuke "…!"
                    yusuke "Mistrzu, to jest zajebiste!"

                    "{i}*am*{/i}"
                    "{i}*am*{/i}"

                    "{i}*zjadł*{/i}"

                    yusuke "Moje kubki smakowe są w ekstazie, a mój brzuch usatysfakcjonowany"
                    yusuke "Całe moje życie mógłbym spożywać “Kebab”."
                    yusuke "Dziękuję ci za zabranie mnie tutaj."

                    luszcz "No mówiłem że smakuwa"

                    yusuke "Moja miłość do kebabów musi zostać przelana na papier. Wróćmy do domu."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"

                jump parking



            
#            "{b}🪦 Cmentarz (15min){/b}":
            
#            "{b}🕯️ Cmentarz Żydowski (15min){/b}":
            
#            "{b}🪨 Skała widokowa (15min){/b}":
            
#            "{b}🏗️ Plac Budowy (15min){/b}":
            
#            "{b}⛪ Kościół (15min){/b}":
            
#            "{b}🏫 Szkoła (15min){/b}":
            
#            "{b}🌀 Portal (15min{/b}":

