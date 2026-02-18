default yusuke_timer = 0
default kebab_wyruchany = 0

default obraz_kebab = 0
default obraz_emo_outline = 0
default obraz_hitla = 0
default obraz_glaz = 0
default obraz_allozaur = 0
default obraz_golab = 0
default obraz_dich_autko = 0

default ykebab = 0
default ycmentarz = 0
default ycmentarz_zydowski = 0
default yskalka = 0
default yplac = 0
default ykosciol = 0
default yszkola = 0

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

            "{b}🛒 Kebab (2 💰)(15min){/b}" if (money >= 2 and ykebab == 1 and kebab_wyruchany == 0) and ((timer >= 660 and timer <= 1380) or (timer >= 2100 and timer <= 2820) or (timer >= 3540 and timer <= 4260) or (timer >= 4980 and timer <= 5700) or (timer >= 6420 and timer <= 7140) or (timer >= 7860 and timer <= 8580) or (timer >= 9300 and timer <= 10020) or (timer >= 10740 and timer <= 11460)):
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
            
            "{b}🪦 Cmentarz (15min){/b}" if ycmentarz == 1 and obraz_emo_outline == 0:
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    scene bg cmentarz with fade
                else:
                    scene bg cmentarz_noc with fade
                play music "audio/music/natura.mp3"

                show yusuke neutral right at slightright
                show luszcz neutral at left

                yusuke "Ostatnio na cmentarzu byłem gdy byłem małym dzieckiem."
                yusuke "Czemu akurat tutaj mistrzu?"

                luszcz "Myślę że jest tu mocny klimacik o dobrej poże."

                yusuke "Hm…"
                yusuke "O, spójrz mistrzu!"
                yusuke "Tamten nagrobek ma napisany rok 1967!"

                luszcz "…"
                luszcz "Ło kurde żeczywiście"

                yusuke "Jeśli umarł w roku 67."
                yusuke "To znaczy że leży tu już 59 lat."
                yusuke "Wyobraź sobie leżeć 59 lat."

                luszcz "Nie"

                yusuke "Okej mistrzu"
                yusuke "Chodziło mi o to że trochę tu stypa jak tak wszyscy leżą."
                yusuke "Prędzej i my umrzemy i do nich dołączymy."
                yusuke "Ach jakie to smutne."

                luszcz "rzycie"

                yusuke "Mistrzu myślę że jestem emo teraz."
                yusuke "Muszę przelać moje emo smutne myśli na papier. Wróćmy do domu."

                $ obraz_emo_outline = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"

                jump parking
            
            "{b}🕯️ Cmentarz Żydowski (15min){/b}" if ycmentarz_zydowski == 1 and obraz_hitla == 0:
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                scene bg cmentarz_zydowski with fade
                play music "audio/music/natura.mp3"
                show yusuke neutral right zorder 10 at slightright
                show luszcz neutral zorder 10 at left
                show hitla zorder 5:
                    xalign 0.25
                    yalign 0.0

                yusuke "Ostatnio na cmentarzu byłem gdy byłem małym dzieckiem."
                yusuke "Czemu akurat tutaj mistrzu?"

                luszcz "Myślę że jest tu mocny klimacik o dobrej poże."

                yusuke "Hm…"
                yusuke "O, spójrz mistrzu!"
                yusuke "Ten pan zamiast leżeć pod ziemią wisi na drzewie!"

                luszcz "Tak, to Adolf Hitler"
                luszcz "Przywódca nazistowskich niemiec"

                yusuke "Oh… chyba widziałem jego obrazy."
                yusuke "Sposób w jaki wisi, gdy cała reszta leży w grobach."
                yusuke "Jest jak anioł, pilnujący żeby spali spokojnie."

                luszcz "Em… tak"

                yusuke "Widzę w tym coś pięknego. Pozwól że się chwilę przypatrzę."
                yusuke "…"
                yusuke "…"
                yusuke "…"
                yusuke "Dobrze, możemy iść. Muszę przelać ten widok na papier. Wróćmy do domu."

                $ obraz_hitla = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"

                jump parking
            
            "{b}🪨 Skała widokowa (15min){/b}" if (yskalka == 1 and obraz_glaz == 0) and ((timer >= 360 and timer <= 1080) or (timer >= 1800 and timer <= 2520) or (timer >= 3240 and timer <= 3960) or (timer >= 4680 and timer <= 5400) or (timer >= 6120 and timer <= 6840) or (timer >= 7560 and timer <= 8280) or (timer >= 9000 and timer <= 9720) or (timer >= 10440 and timer <= 11160)):
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                scene bg start with fade
                play music "audio/music/wiatr.mp3"
                show luszcz neutral at center
                show yusuke neutral right at right

                luszcz "Tutaj chodzę myśleć i być mondrym."

                yusuke "Ja preferuję myśleć wszędzie gdzie jestem"

                luszcz "Nie podskakuj boo cię zepchnę"

                yusuke "Dobrze mistrzu"
                yusuke "Ależ tu pięknie"
                yusuke "Miasto Skała wygląda stąd zdumiewająco."
                yusuke "Ciekawe czemu ma taką nazwę…"

                luszcz "Pewnie dlatego rze skała to naturalnie powstały zespół minerałów, a minerały to takie śmieszne kamienie, a w łazienkach czasem są takie śmieszne kamienie, i można je pomylić z cukierkami i zjeść, a cukierki są słodkie, a co jest jeszcze słodkie?"
                luszcz "Malutkie autobusy aglomeracyjne, niestety karzdy kierowca autobusu jest walonym palaczem i przed jazdą musi nasrać naokoło dymem, przez co niemiłosiernie śmierdzi, a gdzie jeszcze śmierdzi? Tutaj w skale, przez sąsiadów."
                luszcz "Taki jest muj domysł."

                yusuke "Hm."
                yusuke "Ten widok dał mi do myślenia. Muszę to przelać na papier. Wróćmy do domu."

                $ obraz_glaz = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                
                jump parking

            "{b}🏗️ Plac Budowy (15min){/b}" if (yplac == 1 and obraz_allozaur == 0) and ((timer >= 360 and timer <= 1080) or (timer >= 1800 and timer <= 2520) or (timer >= 3240 and timer <= 3960) or (timer >= 4680 and timer <= 5400) or (timer >= 6120 and timer <= 6840) or (timer >= 7560 and timer <= 8280) or (timer >= 9000 and timer <= 9720) or (timer >= 10440 and timer <= 11160)):
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                scene bg poludnie2 with fade
                play music "audio/music/dinozaur.mp3"

                show luszcz neutral at left
                show yusuke neutral at slightleft

                luszcz "Chciałem ci pokazać mojego psa"

                allozaur "meow"

                yusuke "Ale duża kreatura"

                luszcz "Spokojnie nie gryzie"
                luszcz "Pogłaskaj go"

                yusuke "Dobrze mistrzu"

                "{i}*głasku, głasku*{/i}"

                allozaur "meow meow"

                luszcz "No, fajnie"

                yusuke "Fajnie fajnie"

                luszcz "Podoba ci się?"

                yusuke "Tak, pewnie."
                yusuke "Mogę go namalować"

                luszcz "Możesz jeszcze jak"

                yusuke "Mhm dokładnie"
                yusuke "To wróćmy do domu."

                $ obraz_allozaur = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                
                jump parking

            "{b}⛪ Kościół (15min){/b}" if ykosciol == 1 and obraz_golab == 0:
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                scene bg kosciol with fade
                play music "audio/music/kosciol.mp3"
                show luszcz neutral at left
                show yusuke neutral right at slightright
                show duch zorder 5:
                    xalign 0.25
                    yalign 0.0

                yusuke "Miałem okazję być w kościele, ale nigdy nie miałem okazji przyjrzeć się obrazom."

                luszcz "Widzisz to możesz sobie popatrzeć"

                yusuke "Dobrze"

                duchs "Kurde tego hej"

                yusuke "W Kościele są gołębie?"
                luszcz "Nie to Duch Święty"
                luszcz "Serwus"

                duchs "Serwus"
                duchs "Zrobić wam święcenie?"

                yusuke "Tak poproszę"

                window hide

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)

                window show
                yusuke "aaaaaaaa{nw=0.2}"
                window hide

                hide swiatlo2
                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center

                window show
                luszcz "aaaaaaa{nw=0.2}"
                window hide

                hide swiatlo2
                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                show swiatlo1 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo1

                show swiatlo2 zorder 50 at center
                $ renpy.pause(0.1)
                hide swiatlo2

                window show

                duchs "podobało wam się chłopaki"

                yusuke "tak dziękuję"
                yusuke "To było takie inspirujące. wracajmy do domu. muszę to przelać na papier."

                $ obraz_golab = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                
                jump parking

            
            "{b}🏫 Szkoła (15min){/b}" if (yszkola == 1 and obraz_dich_autko == 0) and ((timer >= 480 and timer <= 900) or (timer >= 1920 and timer <= 2340) or (timer >= 3360 and timer <= 3780) or (timer >= 4800 and timer <= 5220) or (timer >= 6240 and timer <= 6660) or (timer >= 7680 and timer <= 8100) or (timer >= 9120 and timer <= 9540) or (timer >= 10560 and timer <= 10980)):
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                yusuke "Podstawówka? Czego ciekawego można szukać w tym więzieniu?"

                luszcz "Pomyśl o dzieciach Yusuke"
                luszcz "Dzieci zawsze coś ciekawego szponcą"
                luszcz "O ile brainrot nie zdąrzył doszczętnie zerzreć im mózguw"

                yusuke "Hm. Dobrze, rozejrzymy się zatem."
                
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade
                scene bg klasa with fade
                play music "audio/music/szkola.mp3"
                show yusuke neutral right at slightright
                show luszcz neutral at left

                luszcz "O patż"
                luszcz "Dzieci grają w pokera"

                yusuke "Nic w tym nadzwyczajnego"

                dziecko "lalala"

                yusuke "hm.. przepraszam cię młody czlowieku"

                show bachor1 at center

                dziecko "co"

                yusuke "Jaki jest twój ulubiony kolor?"

                dziecko "Damn mam juz dziewczyne dawg"
                dziecko "Gupi creep"

                hide bachor1

                yusuke "huh?"

                luszcz "Ja terz nie wiem."
                luszcz "O ej tam coś rysóją widzisz?"

                yusuke "Chodźmy tam"

                scene bg black with fade

                yusuke "Witaj, czy mógłbym zobaczyć co rysujesz?"

                chlopiec "Autka"

                yusuke "Hm... niech spojrzę…"
                yusuke "…"
                yusuke "Niesamowite! Uosobienie samochodu poprzez dodanie twarzy, ukazujące jego spełnienie podczas jazdy, tak, jakby cieszyło go wykonywanie swojej roli w świecie…"
                yusuke "I to nachylenie, dynamizujące obraz."
                yusuke "Co znaczą te kreski na kołach?"

                chlopiec "Włoski"

                yusuke "ok, scusa"

                chlopiec "Grazie."
                chlopiec "Il mio lavoro si concentra sugli impulsi sessuali incontrollati, parlando di persone, uomini, i cui desideri sono così intensi da pensare costantemente solo al sesso, il che può danneggiare loro e chi li circonda, ad esempio a causa dell'HIV, di gravidanze accidentali, di relazioni complicate o di un frenulo rotto."
                chlopiec "Ho usato l'analogia di un'auto che corre a tutta velocità e si dirige verso un incidente."

                yusuke "Grazie per aver spiegato il tuo splendido lavoro. Posso trarne ispirazione per il mio prossimo dipinto?"

                chlopiec "Ovviamente."

                yusuke "Grazie."

                luszcz "…"

                yusuke "Mistrzu, dziękuję że mnie tu zabrałeś."
                yusuke "Chodźmy do domu. Muszę przelać moją nowo zdobytą wiedzę na płótno."

                $ obraz_dich_autko = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                
                jump parking

            
#            "{b}🌀 Portal (15min{/b}":

