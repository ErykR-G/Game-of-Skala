default yusuke_timer = 0
default kebab_wyruchany = 0
default pos = 0
default bzle = 0
default bdobrze = 0

default gdrzwi = 0
default gobraz = 0
default gtelewizor = 0
default gkuchnia = 0
default glodowka = 0
default gszafka = 0

default obraz_kebab = 0
default obraz_emo_outline = 0
default obraz_hitla = 0
default obraz_glaz = 0
default obraz_allozaur = 0
default obraz_golab = 0
default obraz_dich_autko = 0
default obraz_dwie_wieze = 0
default obraz_plaza = 0
default obraz_prawictwo = 0
default obraz_pieklo = 0
default obraz_jordanow = 0

default ykebab = 0
default ycmentarz = 0
default ycmentarz_zydowski = 0
default yskalka = 0
default yplac = 0
default ykosciol = 0
default yszkola = 0
default yportal = 0

label yusuke:
    label yusuke1:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
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

            
            "{b}🌀 Portal (15min){/b}" if yportal == 1 and obraz_dwie_wieze == 0:
                $ timer += 15
                $ yusuke_timer = timer
                $ yusuke_timer += 300
                play sound "audio/sfx/traveling.mp3"
                scene bg black with fade

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    scene bg portal with fade
                else:
                    scene bg portal_noc with fade

                play music "audio/music/portal.mp3"
                show luszcz neutral at slightleft
                show yusuke neutral right at right

                yusuke "Nie miałem pojęcia, że w Skale jest portal międzywymiarowy"
                
                luszcz "Widać na mapach google"

                yusuke "Czy to jest bezpieczne?"

                luszcz "To nieistotne"
                luszcz "Wskakujemy"

                show yusuke neutral right at center:
                    xalign 1.0
                    yalign 1.0
                    easeout 0.5 xalign 0.75
                
                $ renpy.pause(0.5)

                show yusuke neutral right:
                    yoffset 0
                    linear 0.15 yoffset -50
                    linear 0.15 yoffset 0

                $ renpy.pause(0.1)
                with hpunch
                hide yusuke

                $ renpy.pause(0.1)

                show luszcz neutral at center:
                    xalign 0.25
                    yalign 1.0
                    easeout 0.5 xalign 0.75
                
                $ renpy.pause(0.5)

                show luszcz neutral:
                    yoffset 0
                    linear 0.15 yoffset -50
                    linear 0.15 yoffset 0

                $ renpy.pause(0.1)
                with hpunch
                hide luszcz

                $ renpy.pause(0.1)

                scene bg gumball with pixellate
                play music "audio/music/gumball.mp3"

                show luszcz neutral at slightleft
                show yusuke neutral right at slightright

                luszcz "To jest jakiś random ahh dom"

                yusuke "Cóż za ordynarne uniwersum"
                yusuke "Ale w prostych rzeczach można znaleźć najwięcej piękna"
                yusuke "Rozejrzyjmy się może?"

                label gumball_wybory:
                    if gdrzwi == 1 and gobraz == 1 and gtelewizor == 1 and gkuchnia == 1 and glodowka == 1 and gszafka == 1:
                        $ ado += 1
                    else:
                        menu:
                            "{b}Drzwi{/b}" if gdrzwi == 0:
                                luszcz "Dżwi są zamknięte, co świadczy o tym że właściciele domu są raczej nieobecni. Lepiej nie wychodzić, rzeby potencjalnie nie marftić somsioaduw. Btw wygląda na to, rze jest bardzo wczesny poranek."
                                $ gdrzwi = 1
                                jump gumball_wybory

                            "{b}Obraz{/b}" if gobraz == 0:
                                luszcz "Przedstawia zwykłą amerykańską rodzinę."
                                $ gobraz = 1
                                jump gumball_wybory

                            "{b}Telewizor{/b}" if gtelewizor == 0:
                                luszcz "Telewizor jest taki śmieszny gróby. Nwm gdzie jest pilot."
                                $ gtelewizor = 1
                                jump gumball_wybory

                            "{b}Kuchnia{/b}" if gkuchnia == 0:
                                scene bg gumball2 
                                show luszcz neutral at slightleft
                                show yusuke neutral right at slightright
                                luszcz "Kuchnia jest bardzo czysta i óporządkowana. Może właściciele gdzieś wyjechali? Lub pżyprowadzą tu kogoś ważnego?"
                                label gumball_wybory2:
                                    menu:
                                        "{b}Otwórz lodówkę{/b}" if glodowka == 0:
                                            luszcz "*otwieranko*"
                                            luszcz "Dużo bekonu. Nic więcej."
                                            $ glodowka = 1
                                            jump gumball_wybory2

                                        "{b}Otwórz szafkę{/b}" if gszafka == 0:
                                            luszcz "*otwieranko*"
                                            luszcz "Dużo gier wideo. Nic więcej."
                                            $ gszafka = 1
                                            jump gumball_wybory2

                                        "{b}Powrót{/b}":
                                            if gszafka == 1 and glodowka == 1:
                                                $ gkuchnia = 1
                                            scene bg gumball
                                            show luszcz neutral at slightleft
                                            show yusuke neutral right at slightright
                                            jump gumball_wybory

                luszcz "Morze rozejrzymy się na górze?"

                yusuke "Mistrzu spójrz jakie piękne kiwi znalazłem koło pilota."

                luszcz "O masz pilot? Gdzie go znalazłeś?"

                yusuke "Na tamtej szafce przy kalendarzu."
                
                luszcz "O kurde rzeczywiście kalendarz"
                luszcz "Ciekawe jaki dziś dzień"

                call screen full_click_screen("images/kiwi.png")

                luszcz "Yusuke włącz telewizor"

                yusuke "A po co"

                luszcz "Włącz szybko jakikolwiek kanał"

                yusuke "Okej"

                play sound "audio/sfx/tv2.mp3"

                tvn "ludzie są ewakuowani z budynku.. Mówisz że pojazdy ratunkowe już tam są oczywiście ale oczywiście główną obawą są ofiary śmiertelne, znaczy się, czy wiesz czy było w tym budynku dużo osób?"
                
                play sound "audio/sfx/tv.mp3"

                tvp "O KURDE KOLEJNY WŁAŚNIE UDERZYŁ!"
                tvp "Coś innego właśnie uderzyło- Bardzo duży samolot właśnie wleciał nad moją budowlą i była kolejna kolizja. Widzicie ją?"

                play sound "audio/sfx/tv.mp3"

                polsat "92 letnia babcia z rabki-zdrój zjadła swojego psa, bo uważała, że był za słodki"

                play sound "audio/sfx/tv.mp3"

                tvn "Tak… o mój borze…"

                play sound "audio/sfx/tv.mp3"

                republika "Właśnie zauważyliśmy kolejny samolot uderzający drugą wieżę.."

                yusuke "Ojej.."
                yusuke "Biedne wieże"

                luszcz "Nie słyszałeś o 9/11??"

                yusuke "Niet"
                yusuke "Ale wydaje się ciekawsze niż kiwi"
                yusuke "Zostańmy może obejrzeć całe?"

                "{i}*puk puk puk*{/i}"

                nikt "Widzę was tam!!!"
                nikt "Jeden na podłogę drugi otwiera drzwi albo strzelam!!!"

                luszcz "Pr-"

                play sound "audio/sfx/gun.mp3"

                "{i}*strzał*{/i}"

                yusuke "Ja cie w gacie!"

                luszcz "Dobra zmykamy stąd!"

                play sound "audio/sfx/gun.mp3"

                "{i}*strzał*{/i}"

                play sound "audio/sfx/gun.mp3"

                "{i}*strzał*{/i}"

                play sound "audio/sfx/gun.mp3"

                "{i}*strzał*{/i}"

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    scene bg portal with pixellate
                else:
                    scene bg portal_noc with pixellate

                play music "audio/music/portal.mp3"
                show luszcz neutral at slightleft
                show yusuke neutral right at right

                luszcz "Ah ta ameryczka"
                luszcz "Podobało ci się?"

                yusuke "Tak, podobało"
                yusuke "Będę musiał przelać to doświadczenie na płótno. Chodźmy do domu."

                $ obraz_dwie_wieze = 1
                $ yusuke_social_link += 1

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                
                jump parking

    label yusuke2:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
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

        yusuke "Mistrzu, myślę że mój obraz jest już gotowy!"

        luszcz "Najs"

        yusuke "Trzeba tylko namalować jeszcze tło."

        luszcz "Oh"

        yusuke "I myślałem nad różnymi tłami ale nie mogę się zdecydować."
        yusuke "A jak już mi tyle pomagałeś toooo czy wybrałbyś proszę tło?"

        menu:
            "{b}Plaza{/b}":  
                $ obraz_plaza = 1
                luszcz "Zrób plazę"

                yusuke "Dobry wybór, zastanawiałem się nad nim."

            "{b}Prawictwo{/b}": 
                $ obraz_prawictwo = 1
                luszcz "Zrób prawictwo"

                yusuke "Tak!! Martwiłem się że to nie to, ale jeśli ty tak mówisz to to musi być to."

            "{b}Piekło{/b}": 
                $ obraz_pieklo = 1
                luszcz "Zrób piekło"

                yusuke "Nie byłem co do niego pewien, ale ci ufam."

            "{b}Jordanów{/b}":  
                $ obraz_jordanow = 1      
                luszcz "Zrób jordanów"

                yusuke "Hm.. tak. Jordanów idealnie pasuje do reszty obrazu."

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                scene bg pokoj22
            else:
                scene bg pokoj21

        else:
            if drukowanko == 1:
                scene bg pokoj16
            else:
                scene bg pokoj15 

        hide yusuke
        show luszcz neutral right at center

        "{i}*malu malu malu malu*{/i}"

        yusuke "Włala!"
        yusuke "Dziękuję za pomoc, mistrzu. Jest taki piękny!"

        luszcz "Pokaż"

        yusuke "NIE!"
        yusuke "Zobaczysz na wystawie."

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                scene bg pokoj20
            else:
                scene bg pokoj19

        else:
            if drukowanko == 1:
                scene bg pokoj2 
            else:
                scene bg pokoj 

        show luszcz neutral right at slightright
        show yusuke neutral at slightleft2

        yusuke "A propo, możemy na nią wyruszać."

        luszcz "Tak o?"

        yusuke "Tak, już zadzwoniłem po specjalną podwózkę, zabierze nas do Krakowa w 08 minut i 73 sekund."

        "{i}*puk puk*{/i}"

        yusuke "Proszę wejść!"

        luszcz "To muj pokuj"

        yusuke "O, sory"
        yusuke "Ale to podwózka"

        show luszcz neutral at slightleft2
        show yusuke neutral:
            xalign -0.1
            yalign 1.0
        show blobber at slightright
        show gkp at right

        gkp "Dziendobry"

        blobber "Witam serdecznie my jestesmy podwozka na wystawe"

        yusuke "Dzień dobry"

        luszcz "Dobry dobry"

        gkp "Ja wezme pana alternatywke"

        yusuke "yay"

        blobber "Ja wezme obraz i pana tez bo jestem duzy i silny"

        luszcz "Dobrze"

        gkp "Czy na cos czekamy czy mozemy jechac"

        yusuke "Może się napijemy na drogę?"

        blobber "Ciezko odmowic"

        gkp "Jakas wodeczke"

        luszcz "Nie ma picia żadnego"
        luszcz "Jedziemy"

        gkp "jedziemy"

        blobber "jedziemy z tym koksem"

        play sound "audio/sfx/traveling.mp3" 
        stop music
        scene bg black with fade

        n "{i}Na miejscu yusuke został przyjęty ze swoim obrazem i rozkłada go krótką chwilę przed otwarciem wystawy.{/i}"

        play music "audio/music/krakow.mp3"
        scene bg muzeum with fade
        show zaslona zorder 10 at center
        if obraz_plaza == 1:
            show tlo1 zorder 1 at center
        if obraz_prawictwo == 1:
            show tlo2 zorder 1 at center
        if obraz_pieklo == 1:
            show tlo4 zorder 1 at center
        if obraz_jordanow == 1:
            show tlo3 zorder 1 at center
        
        if obraz_glaz == 1:
            show oy1 zorder 2 at center
        if obraz_hitla == 1:
            show oy2 zorder 3 at center
        if obraz_dwie_wieze == 1:
            show oy3 zorder 4 at center
        if obraz_kebab == 1:
            show oy4 zorder 5 at center
        if obraz_dich_autko == 1:
            show oy5 zorder 6 at center
        if obraz_golab == 1:
            show oy6 zorder 7 at center
        if obraz_allozaur == 1:
            show oy7 zorder 8 at center
        if obraz_emo_outline == 1:
            show oy8 zorder 9 at center

        show luszcz neutral zorder 11 at slightleft
        show yusuke neutral right zorder 11 at slightright

        yusuke "Mistrzu. Nadszedł czas"
        yusuke "Na pokazanie ci. Mojego obrazu."

        luszcz "Pokarz mi"

        yusuke "Dobrze mistrzu…"
        yusuke "Przygotuj się,,, na najpiękniejszy obraz jaki widziałeś"

        label obraz_wybor:
            menu:
                "{b}Przygotuj się{/b}" if pos == 0:
                    $ pos = 1
                    luszcz "Okej daj mi się przygotować…"
                    luszcz "…"
                    luszcz "Hm…"
                    luszcz "*wdech*"
                    luszcz "…"
                    luszcz "*wydech*"

                    yusuke "Jesteś gotów?"

                    luszcz "Czekaj daj mi chwilę pomyśleć"
                    luszcz "…"
                    luszcz "(hm…)"
                    luszcz "(kiedy ostatnio widziałem świetliki..?)"
                    luszcz "…"
                    luszcz "(jak bendę miał samochód, to powieszę mu z tyłu gómowe jajca…)"

                    yusuke "Ej bo zaraz się zacznie wystawa"

                    luszcz "hm…"

                    jump obraz_wybor

                "{b}Jestem gotów{/b}":
                    luszcz "Moje ciało jest gotowe"
                    yusuke "I bardzo dobrze"
                    yusuke "trzy dwa jeden ziu"

                    hide zaslona
                    with hpunch

                    yusuke "!!!"
                    yusuke "Co uwarzasz??"
                    luszcz "Wow"
                    luszcz "Jest to. Obraz."
                    yusuke "Tak! Namalowałem go."
                    luszcz "super"

        glos "Witamy na otwarciu wystawy obrazów dla naszego władcy i lidera Bartucha Przeździucha!!!"

        luszcz "(ej, myślisz że on tu będzie..?)"

        yusuke "Mam nadzieję!"

        luszcz "(kurcze, mogłem włorzyć sobie dynamit w dupe albo cos…)"

        yusuke "Ah, wreszcie moja sztuka jest eksponowana pod moim nazwiskiem!"
        yusuke "Nie mogę się doczekać aż ludzie zauważą moją wartość..!"
        yusuke "Oh, ktoś nadchodzi!"

        show pingwin neutral zorder 11 at slightright
        show luszcz neutral zorder 11 at left
        show yusuke neutral zorder 11 at slightleft

        pingwin "Heh siema"
        pingwin "Który z was to namalował"

        yusuke "Ja!"

        luszcz "on"

        pingwin "Nie musisz mówić jak on już powiedział cnie"

        yusuke "On jest moim mistrzem, dostarczył mi inspirację i dach nad głową! Dzięki niemu to dzieło by nie powstało."

        pingwin "Yeah what ever"
        pingwin "O czym jest ten obraz bo trochę nie łapię"

        if obraz_glaz == 1:
            pingwin "Czemu walnąłeś głaz na pół obrazu? Jakby co w tym ciekawego"

        if obraz_hitla == 1:
            pingwin "Fajny ziomek po prawej seksowny wąsik"

        if obraz_dwie_wieze == 1:
            pingwin "Jezus maria pamiętam jak mi kazali pisać w podstawówce wypracowania o tych dwóch zasranych wieżach."
            pingwin "Napisałem że wszyscy amerykanie sie zerbali i odbudowali dwie wierze ale tak wysoko że sięgały nieba"
            pingwin "I wzięli z nieba ofiary ataku i wszyscy byli szczęśliwi"


        if obraz_kebab == 1:
            pingwin "Mmm ale bym sobie zjadł kebaba…"

            yusuke "Ja w sumie też…"

            luszcz "Ja ruwierz…"

        if obraz_dich_autko == 1:
            pingwin "Ktoś wam dorysował siura na obraz chlopaki"

            yusuke "Jakiego siura…?"

            pingwin "Nieważne sory"

        if obraz_golab == 1:
            pingwin "O wgl czy to ma być jakieś religijne..? Myślałem że Kraków odcina się od kościoła."

            luszcz "(ciekawe co ksiądz o tym myśli..)"

            yusuke "Ten wątek jest do interpretacji własnej."


        if obraz_allozaur == 1:
            pingwin "Epicki dinozaur jaki jest wasz ulubiony"

            luszcz "Allozaur1!!!!! rawr !!!"

            pingwin "Cool"

            yusuke "Archeopteryx."

            pingwin "Ta pewnie to teraz wyszukałeś w internecie"

        if obraz_emo_outline == 1:
            pingwin "Ten outline jest cudowny tho"


        pingwin "Anyway, yeah"
        pingwin "O co w tym chodzi"

        yusuke "Mój mistrz zabrał mnie dookoła pobliskiego miasteczka Skały, dzięki czemu poznałem jego piękno i przelałem je na ten obraz!"

        pingwin "O, Skała?"
        pingwin "Chodzą głosy że będzie zaraz włączana do Krakowa"
        pingwin "To nie wiem czy wiecie ale jak Kraków do czegoś dobierze to piękne są tylko wieżowce"
        pingwin "Póki opozycja w nie nie wleci"

        luszcz "Yeah, my działamy przeciw włączeniu."

        yusuke "Dokładnie.."

        pingwin "Nwm jak zwracanie uwagi na miasto w tym pomaga ale ok"
        pingwin "Czekajcie walne focię"

        "{i}*pstryk*{/i}"

        pingwin "Dzięki guys"

        pingwin "Powodzonka"

        yusuke "Dzięki"

        luszcz "Dzienki"

        hide pingwin
        show luszcz neutral zorder 11 at slightleft
        show yusuke neutral right zorder 11 at slightright

        luszcz "Żeczywiście czy my teraz nie pracujemy na niekorzyść Skały?"

        yusuke "Nie, nie mistrzu… bo widzisz. Jak tylko wygram stanę się naczelnym artystą Krakowa i będę mógł używać swoich wpływów dla ciebie."

        luszcz "Hm… w sumie to fajnie"
        luszcz "(Ze wszystkich osub, nie spodziewałem się rze on będzie miał największy wpływ na sytuację..)"
        luszcz "(W takim razie oby wygrał ten konkurs..!)"

        stop music
        show bg black zorder 50 with fade

        n "{i}Wystawa trwała, randomy chodziły i patrzyły na obrazy, i rzeczywiście widać było, że obraz Yusuke zbiera największe zainteresowanie…{/i}"
        n "{i}Nagle..!!!{/i}"
      
        show bg muzeum zorder 0 with fade
        play music "audio/music/krakow.mp3"

        glos "Uwaga! Prosimy jak najszybciej opuścić galerię! Czas oglądania się skończył."

        luszcz "Chwila… to wszystko?"

        glos "Lada moment na salę wstąpi prezydent Bartuch Przeździuch."

        luszcz "O ojej"
        luszcz "Żeczywiście tu będzie"

        yusuke "Będzie oceniał obrazy osobiście!"

        luszcz "Nwm czy to dobrze"

        yusuke "To znakomite wieści, gdyż dostaniemy czystą, niefiltrowaną ocenę, i nie będę wybierany przez jakichś frajerów tylko mistrza we własnej osobie."
        
        luszcz "A to nie ja byłem mistrzem? 🥺"

        yusuke "Nadal jesteś, mistrzu."

        luszcz "Okay yay"

        bartuch "CZY TO TWÓJ OBRAZ????"

        vergil "Um, tak! Zgadza się!"

        bartuch "NIE PODOBA MI SIE TWÓJ OBRAZ"
        bartuch "CZEMU NARYSOWALES GOTKI W WIĘZIENIU!!! ?"

        vergil "B-bo knuły przeciwko tobie…"

        bartuch "NIGDY NIE WRZUCĘ GOTKI DO WIĘZIENIA"
        bartuch "MAMY DLA NICH SPECJALNE IZOLATKI W KTORYCH GRAJĄ W GRY WIDEO I SURFUJĄ INTERNET DO KONCA ZYCIA"

        luszcz "(wow… based)"

        vergil "Przepraszam! Nikt mi nie powiedział!"

        bartuch "OD DZIŚ PRACUJESZ W KAMIENIOŁOMIE LIBAN BAJ BAJ"

        vergil "aw hell no"

        show bartuch neutral zorder 11 at slightright
        show luszcz neutral zorder 11 at left
        show yusuke neutral zorder 11 at slightleft

        bartuch "A TO CO TO TAKIEGO"
        bartuch "KTO Z WAS TO NAMALOWAŁ?"

        yusuke "Ja prosze pana"

        bartuch "HM.. ZOBACZMY.."

        if obraz_glaz == 1:
            $ bzle += 1
            bartuch "NUDNY JEST TEN KAMIEŃ"
            bartuch "…"

        if obraz_hitla == 1:
            $ bzle += 1
            bartuch "KIM JEST TEN ZIOMEK NIE ZNAM GO"
            bartuch "…"

        if obraz_dwie_wieze == 1:
            $ bzle += 1
            bartuch "O WOW WIEŻOWCE SIGMA"
            bartuch "EJ CZM COŚ LECI W TE WIERZOWCE HALO"
            bartuch "PANOWIE NIE WKURZAJCIE MNIE"
            bartuch "…"

        if obraz_kebab == 1:
            $ bdobrze += 1
            bartuch "MMM KEBABIK PYCHOTKA"
            bartuch "…"

        if obraz_dich_autko == 1:
            $ bdobrze += 1
            bartuch "WIDZĘ DIHOMOBIL"
            bartuch "AKURAT NIEDAWNO ZATRUDNIŁEM MELONA TRZASKA ŻEBY SKONTRUOWAŁ MI TAKI SAMOCHÓD"
            bartuch "DOBRY SZIT"
            bartuch "…"

        if obraz_golab == 1:
            $ bdobrze += 1
            bartuch "FAJNY GOŁOMB"
            bartuch "…"

        if obraz_allozaur == 1:
            $ bzle += 1
            bartuch "CO TU ROBI TEN UGLY AHH DINOZAR GET OUT"
            bartuch "…"

        if obraz_emo_outline == 1:
            $ bdobrze += 1
            bartuch "ALE TUFF OBRAMÓWKA TAKA EMO"
            bartuch "…"

        if obraz_plaza == 1 or obraz_prawictwo == 1:
            $ bdobrze += 1
            bartuch "FAJNE TŁO BTW"
            bartuch "…"

        if obraz_pieklo == 1 or obraz_jordanow == 1:
            $ bzle += 1
            bartuch "GŁUPIE TŁO BTW"
            bartuch "…"

        bartuch "HM…"

        if bzle > bdobrze:
            $ yusuke_social_link = 6
            $ yusuke_wybory = 4
            bartuch "NIE PODOBA MI SIĘ TEN OBRAZ"
            bartuch "ZA KARĘ IDZIESZ PRACOWAĆ DO KAMIENIOŁOMU LIBAN GAHAHAHA"

            yusuke "Nieeeet…!!!"
            yusuke "Moja praca… opluta…"
            yusuke "Czy będę mógł chociaż malować w wolnym czasie?"

            bartuch "NIE"
            bartuch "W KAMIENIOŁOMIE NIE MA WOLNEGO CZASU"

            yusuke "siara.."

            luszcz "Ojć"
            luszcz "Biedny…"

            bartuch "A TY KIM WŁAŚCIWIE JESTEŚ"

            yusuke "On? To jest mój m…"

            luszcz "mtaksówkarz!! Ja tylko go miałem puźniej odwieźć ale rozumiem że już go ze sobą zabierasz?"

            bartuch "TAK"

            yusuke "(mistrzu…)"

            luszcz "(sory to dla Skały)"
            luszcz "(morze kiedyś cię uratuję)"
            luszcz "((raczej nie lol))"

            yusuke "🥺"

            luszcz "Cusz, to ja się morze będę zbierał"

            bartuch "BAJ BAJ"

            luszcz "Baj baj haha"

            stop music
            play sound "audio/sfx/traveling.mp3" 
            scene bg black with fade

            n "{i}Łuszczu znajduje bobra i wraca na nim błyskawicznie do skały opłakując losy swojego pierwszego ever współlokatora.{/i}"

            luszcz "łe łe łe"
            luszcz "Anyway"
            luszcz "Bartuch Przeździuch nie postawi kroku na ziemiach mojego miasta! Dopilnóję tego"
            luszcz "A yusuke niech się trzyma tam jakoś… liban ładna okolica"
            luszcz "Papierz tam pracował"

            blobber "jestesmy na miejscu!"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                scene bg black with fade
                scene bg rynek with fade
            else:
                scene bg black with fade
                scene bg rynek_noc with fade
            
            show luszcz neutral at slightleft
            show blobber at slightright

            luszcz "Kurcze żeczywiście"
            luszcz "Dziękuje za podwózkę"

            blobber "przyjemnosc po mojej stronie dowidzenia"

            hide blobber
            show luszcz neutral at center

            luszcz "no cusz"

            hide luszcz

            jump rynek2

        else:
            $ yusuke_social_link = 6
            $ yusuke_wybory = 3
            bartuch "STOP!! PRZERYWAMY KONKURS!"
            bartuch "WSZYSCY DO DOMÓW!!"
            bartuch "NIEBIESKOWŁOSY CHŁOPCZE"
            bartuch "W NAGRODĘ NATYCHMIASTOWO STAJESZ SIĘ MOIM PRYWATNYM ARTYSTĄ"

            luszcz "(huh?! Co do plo, yusuke?)"

            yusuke "Tak jest mistrzu!"

            luszcz "Co tak jest mistrzu"

            yusuke "Nie mówię do ciebie, tylko do mojego nowego mistrza."

            bartuch "HEL JE"

            luszcz "Oh.. okej"

            luszcz "(ale pomorzesz coś ogarnąć w sprawie Skały, cnie?)"

            yusuke "Hm… spytam mistrza"

            yusuke "Mistrzu, czy możemy coś zrobić, żeby skała pozostała niepodległa?"

            bartuch "WHAT THE SIGMA"
            bartuch "NIEBIESKOWŁOSY CHŁOPCZE NASTĘPNY TWÓJ OBRAZ TO PIĘKNA WIZJA SKAŁY Z WIEŻOWCAMI"
            bartuch "NIGDY WIĘCEJ NIE ZADAWAJ SKIBIDI PYTAŃ"

            yusuke "Dobrze mistrzu!!"

            bartuch "EJ WSM KIM TY W OGÓLE JESTEŚ!! CO TY SZEPTAŁEŚ PRZED CHWILĄ KIM TY JESTEŚ"

            luszcz "Ja?? Ja tylko go tu podwoziłem ale jak go zabierasz ze sobą to ja sobie wrucę do mojej pracy"

            bartuch "PRACUJ PÓKI TWÓJ ZAWÓD JEST LEGALNY"
            bartuch "TO BAJ BAJ, NIEBIESKOWŁOSY CHŁOPCZE POŻEGNAJ SIĘ"

            yusuke "oki mistrzu"
            yusuke "żegnaj um…"
            yusuke "jak miałeś na imię..?"

            luszcz "w sumie lepiej że nie pamiętasz"
            luszcz "to ja zmykam"

            stop music
            play sound "audio/sfx/traveling.mp3" 
            scene bg black with fade

            n "{i}Łuszczu znajduje bobra i wraca na nim błyskawicznie do skały niezadowolony z sytuacji{/i}"

            luszcz "Jak się można tak sprzedać… ale siara"
            luszcz "Bartuch Przeździuch nie postawi kroku na ziemiach mojego miasta! Dopilnóję tego"
            luszcz "I że trzymałem zdrajcę w moim pokoju… oby im za dórzo nie powiedział"

            blobber "jestesmy na miejscu!"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                scene bg black with fade
                scene bg rynek with fade
            else:
                scene bg black with fade
                scene bg rynek_noc with fade
            
            show luszcz neutral at slightleft
            show blobber at slightright

            luszcz "Kurcze żeczywiście"
            luszcz "Dziękuje za podwózkę"

            blobber "przyjemnosc po mojej stronie dowidzenia"

            hide blobber
            show luszcz neutral at center

            luszcz "no cusz"

            hide luszcz

            jump rynek2
