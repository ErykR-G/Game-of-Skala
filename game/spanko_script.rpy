default drukowanko = 0
default tasma_spotkanko = 0
default czasd = 0
default nocka = 1
default ltite = 0
default gdzie_spisz = 0

label spanko:
    if yusuke_social_link == 0:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj8 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj7 with fade
        else:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj4 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj3 with fade
        
        show luszcz neutral at center

        luszcz "Wait wtf kim jest ten ziomek??"

        yusuke "zzz…"

        "{i}łuszczu dotyka go za suty*{/i}"

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                scene bg pokoj12
            else:
                scene bg pokoj11
        else:
            if drukowanko == 1:
                scene bg pokoj10
            else:
                scene bg pokoj9

        show luszcz neutral at left
        show yusuke neutral right at center

        yusuke "aaa!!! Prosze nie obiecałeś że już nie..!"

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            kazuma "Ej nie wydzieraj sie tak próbuję tu spać!"

        yusuke "Oh. Um, proszę wybaczyć."

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            kazuma "honk mimimimi"

        yusuke "Panie Łuszcz, niech pan pozwoli że się przedstawię."

        yusuke "Mam na imię Yusuke."
        yusuke "Jako iż zostałem pozbawiony domu, twoi rodzice zgodzili się przyjąć mnie do końca tygodnia abym mógł rozejrzeć się nad stałym dachem nad głową oraz pracą."
        yusuke "Jednak jako iż nie mają czasu, powierzyli opiekę nade mną tobie."
        yusuke "Możesz zrobić ze mną co zechcesz, mistrzu."

        luszcz "Em… okej? Yusuke."
        luszcz "Czyli zwaliłeś mi się do mojego pokoju?"

        yusuke "Nie będę sprawiał problemów. Zależy mi tylko na ciszy i miejscu na sztalugę."

        luszcz "O, malujesz obrazy?"

        yusuke "Tak, moim planem jest namalować coś na Wielką Wystawę Zwycięstwa w Krakowie. Jeśli mój obraz zostanie zaakceptowany, będę w stanie utrzymać się samemu, w takim razie opuścić twój pokój."
        yusuke "Czasu jest jednak niewiele. Muszę spędzić każdą możliwą chwilę na dopieszczaniu malunku."
        yusuke "Wybacz za moją bezpośredniość, zarówno jak i moje wymagania. Obiecuję że jak tylko mi się uda, odpłacę ci odpowiednią sumę."
        yusuke "Czy mógłbyś pomóc mi znaleźć inspirację do moich obrazów?"

        menu:
            "{b}Nic ci nie pomogę, wynocha z pokojó{/b}":
                $ yusuke_social_link = 10
                luszcz "Hola hola nie bądź taki do przodu bo cię z tyłu zabraknie"
                luszcz "Jestem bardzo zajętym człowiekiem i żaden niebieskowłosy obiekt nie będzie mi się wpieprzał teraz do pokoju"

                yusuke "Ale mistrzu-"

                luszcz "Polecam zacząć rysować furry porno."
                luszcz "Dowidzenia."
                luszcz "Panu."

                yusuke "Ah, więc to tak…"
                yusuke "W takim razie się stąd usuwam."
                yusuke "Dowidzenia."
                yusuke "Panu."
                
                hide yusuke
                show luszcz neutral at center

                luszcz "Co to miało niby być?"

                show luszcz neutral at left
                show tata neutral at center

                tata "No sory synu chcieliśmy sprawdzić jak byś sobie poradził ze zwierzątkiem domowym."
                tata "Planowaliśmy ci kupić kota na dzień dziecka"

                luszcz "Tato ale nie jestem już dzieckiem!!!"
                luszcz "Zresztą mówiłem wam że ja chcę Allozaura!!"

                tata "Allozaur by cię zjadł synu"
                
                show luszcz blush

                luszcz "Nieee… racja… nie chciałbym tego…."

                tata "Tak my z mamą też byśmy tego nie chcieli"
                tata "Dobra wracam do łóżeczka dobranoc."

                luszcz "Dobranoc tato."

                hide tata 
                show luszcz neutral at center
            
            "{b}Jak mogę pomóc?{/b}":
                $ yusuke_social_link = 1
                luszcz "Jaką pomoc masz na myśli?"
                luszcz "Nie rzebym się przechwalał, ale mam w sobie trochę artysty"
                luszcz "Btw najlepsza rzecz jaką narysowałem"
                luszcz "To to:"

                show obraz1 zorder 50 at center
                ""
                hide obraz1

                yusuke "Ah… cóż za piękne dzieło."
                yusuke "W ramach pomocy, chciałbym żebyś zabierał mnie do ciekawych miejsc w okolicy."
                yusuke "Będąc pod opiekądo mojego poprzedniego mistrza miałem zakaz opuszczania domu."
                yusuke "Swoją drogą to przez to że ktoś wyjawił jego nielegalne praktyki jestem teraz bezdomny i bezrobotny."

                luszcz "To bardzo niemiłe ze strony tej osoby"
                luszcz "Jebać ją jebać kapusi"

                yusuke "Widzę że się tu zgadzamy."

                luszcz "Czyli co, mam cię zabierać do rurznych miejsc, a potem ty będziesz sobie malował, a potem się wyprowadzisz?"
                
                yusuke "Jeśli byłbyś taki dobry, i wszystko wyszło zgodnie z planem, to tak."

                luszcz "Dobrze, ale chciałbym ci postawić jeden warónek na to wszystko:"
                luszcz "Czy postawisz się przeciw księdzó w sprawie przyłączenia Skały do Krakowa?"

                yusuke "Ah, słyszałem coś o tym. Ogłaszano to podczas mszy, gdy przechodziłem obok żeby napić się wody święconej."
                yusuke "Oczywiście że stanę po twojej stronie, mistrzu."

                luszcz "No i sigmastycznie."

                yusuke "W takim razie, chciałbyś mnie gdzieś teraz zabrać?"

                luszcz "Nie"
                luszcz "Wrócę do ciebie jak będę miał czas."

                yusuke "Dobrze mistrzu."

                luszcz "Jest puźna:00"
                luszcz "Trzeba spać"

                yusuke "Ah, tak, rzeczywiście."
                yusuke "Dobranoc, mistrzu"

                luszcz "Dobranoc"

                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        scene bg pokoj8
                    else:
                        scene bg pokoj7
                else:
                    if drukowanko == 1:
                        scene bg pokoj4
                    else:
                        scene bg pokoj3

                hide yusuke 
                show luszcz neutral at center

    else:
        if yusuke_social_link >= 1 and yusuke_social_link <= 5:
            if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj8 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj7 with fade
                
                show luszcz neutral at center

            else:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj4 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj3 with fade
                
                show luszcz neutral at center

        else:
            if yusuke_social_link >= 6:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj6 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj5 with fade
                    
                    show luszcz neutral at center
                    
                else:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj2 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj with fade

                    show luszcz neutral at center 

    luszcz "ohhh jestem wyczerpany"
    luszcz "idę spać"

    scene bg black with fade
    stop music
    if nocka == 4 and lilith_social_link == 0:
        $ kostka = renpy.random.randint(1, 3)
        if kostka >= 2:
            $ ltite = 2
            $ timer += 120
            jump lilith1
    
    if nocka >= 5 and lilith_social_link == 0:
        $ ltite = 2
        $ timer += 120
        jump lilith1
    
    if nocka == 6 and lilith_social_link == 1 and ltite == 0:
        $ kostka = renpy.random.randint(1, 3)
        if kostka >= 2:
            $ timer += 120
            jump lilith2
    
    if nocka == 7 and lilith_social_link == 1 and ltite == 0:
        $ timer += 120
        jump lilith2

    $ kostka = renpy.random.randint(1, 2)
    if kostka == 1:
        "{i}Łuszcz położył się spać{/i}"
        "{i}Podczas snu założył kilka haremów w innych światach{/i}"
        "{i}Niestety, po obudzeniu stracił wszystkie, które kochał{/i}"
    
    else:
        if lilith_social_link == 0 and nocka > 1:
            $ ltite = 2
            $ timer += 120
            jump lilith1
        
        else:
            if lilith_social_link == 1 and nocka > 3 and ltite == 0:
                $ timer += 120
                jump lilith2
            
            else:
                "{i}Łuszcz położył się spać{/i}"
                "{i}Podczas snu założył kilka haremów w innych światach{/i}"
                "{i}Niestety, po obudzeniu stracił wszystkie, które kochał{/i}"

    label spanko_bed:
        if yusuke_social_link >= 1 and yusuke_social_link <= 5:
            if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj8 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj7 with fade

            else:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj4 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj3 with fade

        else:
            if yusuke_social_link >= 6:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj6 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj5 with fade
                    
                else:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj2 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj with fade

        if timer > 1200 and timer < 1800:
            $ timer = 1980
        
        else:
            if timer > 2640 and timer < 3240:
                $ timer = 3420
            
            else:
                if timer > 4080 and timer < 4680: 
                    $ timer = 4860
                
                else:
                    if timer > 5520 and timer < 6120: 
                        $ timer = 6300
                    
                    else:
                        if  timer > 6960 and timer < 7560: 
                            $ timer = 7740
                        
                        else:
                            if timer > 8400 and timer < 9000: 
                                $ timer = 9180
                            
                            else:
                                if timer > 9840 and timer < 10440:
                                    $ timer = 10620

        show luszcz neutral at center

        if timer >= 10080 and timer <= 11460:
            luszcz "Ohhh, dzisiaj wielki dzień!"
            luszcz "dziś referendum o 21:37 w kościele!"
            luszcz "dlatego muszę zrobić wszystko co w mojej mocy, by je powstrzymać!"

            $ gdzie_spisz = 0

            $ luszcz_piguly = 0
            $ eminem_piguly = 0
            $ urban_piguly = 0
            $ zyd_piguly = 0
            $ kazuma_piguly = 0
            $ tarczownik_dzien = 0
            $ akcja1 = 0
            $ spanko = 0
            $ krowko_limit = 0
            $ toxic_limit = 0
            $ czasd -= 1
            $ duda_timer -= 1
            $ nocka += 1
            if ltite > 0:
                $ ltite -= 1
            if kazuma_strzal > 0:
                $ kazuma_strzal -= 1
            if tasma_spotkanko == 2:
                $ tasma_spotkanko = 1
            else: 
                if tasma_spotkanko == 1:
                    $ tasma_spotkanko = 0
            
            luszcz "Czas brać się do roboty!"
        
            luszcz "Ooo rodzice zostawili mi kieszonkowe.."

            $ money += 3

            "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

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

        luszcz "Kurwa znowu w tej Polsce"
        luszcz "Nienawidzę tego syfu, tego państwa..."

        $ gdzie_spisz = 0

        $ luszcz_piguly = 0
        $ eminem_piguly = 0
        $ urban_piguly = 0
        $ zyd_piguly = 0
        $ kazuma_piguly = 0
        $ tarczownik_dzien = 0
        $ akcja1 = 0
        $ spanko = 0
        $ krowko_limit = 0
        $ toxic_limit = 0
        $ czasd -= 1
        $ duda_timer -= 1
        $ nocka += 1
        if ltite > 0:
            $ ltite -= 1
        if kazuma_strzal > 0:
            $ kazuma_strzal -= 1
        if tasma_spotkanko == 2:
            $ tasma_spotkanko = 1
        else: 
            if tasma_spotkanko == 1:
                $ tasma_spotkanko = 0


        if timer >= 8640 and timer <= 10020:
            jump bal1
        luszcz "Ehh dobra, czas brać się do roboty"
        
        luszcz "Ooo rodzice zostawili mi kieszonkowe.."

        $ money += 3

        "{i}*3 Portfele zostały dodane do ekwipunku*{/i}"

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


label spanko2:
    scene bg black with fade
    stop music
    play sound "audio/sfx/spadek.mp3"
    "{i}Oczy Łuszcza zamkneły się bez jego kontroli, a on upadł bezwładnie na ziemię{/i}"
    "{i}Podczas nieobecności jego świadomości został kilkukrotnie brutalnie zgwałcony przez 2 buldożery, które nie były zamknięte w kojcach{/i}"
    "{i}Na miejscu zdarzenia był również Owczarek Niemiecki, lecz on akurat powstrzymał się od jakikolwiek akcji{/i}"
    "{i}Po kilku godzinach snu Łuszczu otworzył oczy{/i}"

    if timer > 1200 and timer < 1800: 
            $ timer = 2100
        
    else:
        if timer > 2640 and timer < 3240: 
            $ timer = 3540
        
        else:
            if timer > 4080 and timer < 4680: 
                $ timer = 4980
            
            else:
                if timer > 5520 and timer < 6120: 
                    $ timer = 6420
                
                else:
                    if  timer > 6960 and timer < 7560: 
                        $ timer = 7860
                    
                    else:
                        if timer > 8400 and timer < 9000: 
                            $ timer = 9300
                        
                        else:
                            if timer > 9840 and timer < 10440:
                                $ timer = 10740

    $ luszcz_piguly = 0
    $ eminem_piguly = 0
    $ urban_piguly = 0
    $ zyd_piguly = 0
    $ kazuma_piguly = 0
    $ tarczownik_dzien = 0
    $ akcja1 = 0
    $ spanko = 0
    $ krowko_limit = 0
    $ toxic_limit = 0
    $ czasd -= 1
    $ nocka += 1
    $ duda_timer -= 1
    if ltite > 0:
        $ ltite -= 1
    if kazuma_strzal > 0:
            $ kazuma_strzal -= 1
    if tasma_spotkanko == 2:
            $ tasma_spotkanko = 1
    else: 
        if tasma_spotkanko == 1:
            $ tasma_spotkanko = 0

    if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
        play music "audio/music/pole.mp3"
    else:
        play music "audio/music/pole_noc.mp3"
    if rynek == 1:
        scene bg rynek with fade
    if sloneczna == 1:
        scene bg sloneczna with fade
    if alejka == 1:
        scene bg alejka with fade
    if parking == 1:
        scene bg parking with fade
    if wolbromska == 1:
        scene bg wolbromska with fade
    if bohaterow_wrzesnia == 1:
        scene bg bohaterow_wrzesnia with fade
    if lipowa == 1:
        scene bg lipowa with fade
    if granica == 1:
        scene bg granica with fade

    show luszcz neutral at center
    
    $ gdzie_spisz = 1
    luszcz "Ała, ale mnie dupa napierdala"
    luszcz "kurwa, ała japierdole wsyztsko boli"

    if timer >= 8640 and timer <= 10020:
        jump bal1

    if timer >= 10080 and timer <= 11460:
        luszcz "japierdole dobra już muszę brać się do roboty"
        luszcz "dziś wielki dzień, dzień referendum o 21:37 w kościele!"
        luszcz "dlatego muszę zrobić wszystko co w mojej mocy, by je powstrzymać!"
        hide luszcz

        if rynek == 1:
            jump rynek2
        if sloneczna == 1:
            jump sloneczna2 
        if alejka == 1:
            jump alejka2 
        if parking == 1:
            jump parking2
        if wolbromska == 1:
            jump wolbromska2
        if bohaterow_wrzesnia == 1:
            jump bohaterow_wrzesnia2 
        if lipowa == 1:
            jump lipowa2 
        if granica == 1:
            jump granica2
    luszcz "japierdole dobra już muszę brać się do roboty..."

    hide luszcz

    if rynek == 1:
        jump rynek2
    if sloneczna == 1:
        jump sloneczna2 
    if alejka == 1:
        jump alejka2 
    if parking == 1:
        jump parking2
    if wolbromska == 1:
        jump wolbromska2
    if bohaterow_wrzesnia == 1:
        jump bohaterow_wrzesnia2 
    if lipowa == 1:
        jump lipowa2 
    if granica == 1:
        jump granica2

label drukarka3d1:
    if yusuke_social_link == 0:
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
        
        show yusuke neutral at slightleft2
        show luszcz neutral right at slightright

        yusuke "Ah… więc to ty musisz być właścicielem tego pomieszczenia."

        luszcz "Dafaq? Kim ty jesteś co ty robisz w moim pokojó?"

        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            luszcz "Jeśli dobrze pamiętam zaprosiłem tu tylko jendą osobę…"

            kazuma "Też myślałem że będę tu sam lol"

        yusuke "Gdzie są moje maniery…"
        yusuke "Mam na imię Yusuke."
        yusuke "Jako iż zostałem pozbawiony domu, twoi rodzice zgodzili się przyjąć mnie do końca tygodnia abym mógł rozejrzeć się nad stałym dachem nad głową oraz pracą."
        yusuke "Jednak jako iż nie mają czasu, powierzyli opiekę nade mną tobie."
        yusuke "Możesz zrobić ze mną co zechcesz, mistrzu."

        luszcz "Em… okej? Yusuke."
        luszcz "Czyli zwaliłeś mi się do mojego pokoju?"

        yusuke "Nie będę sprawiał problemów. Zależy mi tylko na ciszy i miejscu na sztalugę."

        luszcz "O, malujesz obrazy?"

        yusuke "Tak, moim planem jest namalować coś na Wielką Wystawę Zwycięstwa w Krakowie. Jeśli mój obraz zostanie zaakceptowany, będę w stanie utrzymać się samemu, w takim razie opuścić twój pokój."
        yusuke "Czasu jest jednak niewiele. Muszę spędzić każdą możliwą chwilę na dopieszczaniu malunku."
        yusuke "Wybacz za moją bezpośredniość, zarówno jak i moje wymagania. Obiecuję że jak tylko mi się uda, odpłacę ci odpowiednią sumę."
        yusuke "Czy mógłbyś pomóc mi znaleźć inspirację do moich obrazów?"

        menu:
            "{b}Nic ci nie pomogę, wynocha z pokojó{/b}":
                $ yusuke_social_link = 10
                luszcz "Hola hola nie bądź taki do przodu bo cię z tyłu zabraknie"
                luszcz "Jestem bardzo zajętym człowiekiem i żaden niebieskowłosy obiekt nie będzie mi się wpieprzał teraz do pokoju"

                yusuke "Ale mistrzu-"

                luszcz "Polecam zacząć rysować furry porno."
                luszcz "Dowidzenia."
                luszcz "Panu."

                yusuke "Ah, więc to tak…"
                yusuke "W takim razie się stąd usuwam."
                yusuke "Dowidzenia."
                yusuke "Panu."

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
                
                hide yusuke
                show luszcz neutral right at center

                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    kazuma "Damn ziomuś. Dobrze że mnie nie wywalasz."

                    luszcz "No bo ciebie tutaj sam zaprosiłem."
                    luszcz "A tamto coś…"

                luszcz "Co to miało niby być?"

                show luszcz neutral at slightleft2
                show tata neutral at slightright

                tata "No sory synu chcieliśmy sprawdzić jak byś sobie poradził ze zwierzątkiem domowym."
                tata "Planowaliśmy ci kupić kota na dzień dziecka"

                luszcz "Tato ale nie jestem już dzieckiem!!!"
                luszcz "Zresztą mówiłem wam że ja chcę Allozaura!!"

                tata "Allozaur by cię zjadł synu"
                
                show luszcz blush

                luszcz "Nieee… racja… nie chciałbym tego…."

                tata "Tak my z mamą też byśmy tego nie chcieli"
                tata "Muszę wracać do swoich zajęć papatki."

                show luszcz neutral

                luszcz "Serwus"

                hide tata
                show luszcz neutral at center

                luszcz "(Em.. po co ja tu przyszedłem..?)"
                luszcz "Ah tak"
                luszcz "Drukarka 3D"
            
            "{b}Jak mogę pomóc?{/b}":
                $ yusuke_social_link = 1
                luszcz "Jaką pomoc masz na myśli?"
                luszcz "Nie rzebym się przechwalał, ale mam w sobie trochę artysty"
                luszcz "Btw najlepsza rzecz jaką narysowałem"
                luszcz "To to:"

                show obraz1 zorder 50 at center
                ""
                hide obraz1

                yusuke "Ah… cóż za piękne dzieło."
                yusuke "W ramach pomocy, chciałbym żebyś zabierał mnie do ciekawych miejsc w okolicy."
                yusuke "Będąc pod opiekądo mojego poprzedniego mistrza miałem zakaz opuszczania domu."
                yusuke "Swoją drogą to przez to że ktoś wyjawił jego nielegalne praktyki jestem teraz bezdomny i bezrobotny."

                luszcz "To bardzo niemiłe ze strony tej osoby"
                luszcz "Jebać ją jebać kapusi"

                yusuke "Widzę że się tu zgadzamy."

                luszcz "Czyli co, mam cię zabierać do rurznych miejsc, a potem ty będziesz sobie malował, a potem się wyprowadzisz?"
                
                yusuke "Jeśli byłbyś taki dobry, i wszystko wyszło zgodnie z planem, to tak."

                luszcz "Dobrze, ale chciałbym ci postawić jeden warónek na to wszystko:"
                luszcz "Czy postawisz się przeciw księdzó w sprawie przyłączenia Skały do Krakowa?"

                yusuke "Ah, słyszałem coś o tym. Ogłaszano to podczas mszy, gdy przechodziłem obok żeby napić się wody święconej."
                yusuke "Oczywiście że stanę po twojej stronie, mistrzu."

                luszcz "No i sigmastycznie."

                yusuke "W takim razie, chciałbyś mnie gdzieś teraz zabrać?"

                luszcz "Nie"
                luszcz "Wrócę do ciebie jak będę miał czas."

                yusuke "Dobrze mistrzu."

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
                show luszcz neutral at center

                luszcz "(Em.. po co ja tu przyszedłem..?)"
                luszcz "Ah tak"
                luszcz "Drukarka 3D"

    else:
        if yusuke_social_link >= 1 and yusuke_social_link <= 5:
            if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj22 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj21 with fade
                
                show luszcz neutral right at center
                luszcz "Dzień dobry panowie"

                yusuke "Dzień dobry"

                kazuma "Dzień dobry"

            else:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj16 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj15 with fade
                
                show luszcz neutral right at center
                luszcz "Dzień dobry"

                yusuke "Dzień dobry"
        else:
            if yusuke_social_link >= 6:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj20 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj19 with fade
                    
                    show luszcz neutral right at center
                    luszcz "Dzień dobry"

                    kazuma "Dzień dobry"
                    
                else:
                    if drukowanko == 1:
                        play music "audio/music/drukowanie.mp3"
                        scene bg pokoj2 with fade
                    else:
                        play music "audio/music/pokoj.mp3"
                        scene bg pokoj with fade

    show luszcz neutral at center

    luszcz "Its drukin’ time…"

    scene bg black with fade
    $ drukowanko = 1
    $ drukarka3d_social_link = 1
    $ czasd = 5

    if yusuke_social_link == 0:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                scene bg pokoj24 with fade
                play music "audio/music/drukowanie.mp3"
            else:
                scene bg pokoj23 with fade
        else:
            if drukowanko == 1:
                scene bg pokoj18 with fade
                play music "audio/music/drukowanie.mp3"
            else:
                scene bg pokoj17 with fade

    else:
        if yusuke_social_link >= 1 and yusuke_social_link <= 5:
            if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                if drukowanko == 1:
                    scene bg pokoj22 with fade
                    play music "audio/music/drukowanie.mp3"
                else:
                    scene bg pokoj21 with fade

            else:
                if drukowanko == 1:
                    scene bg pokoj16 with fade
                    play music "audio/music/drukowanie.mp3"
                else:
                    scene bg pokoj15 with fade
                
        else:
            if yusuke_social_link >= 6:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                    if drukowanko == 1:
                        scene bg pokoj20 with fade
                        play music "audio/music/drukowanie.mp3"
                    else:
                        scene bg pokoj19 with fade
                    
                else:
                    if drukowanko == 1:
                        scene bg pokoj2 with fade
                        play music "audio/music/drukowanie.mp3"
                    else:
                        scene bg pokoj with fade
    
    show luszcz neutral at center
  
    luszcz "Dobra, to pewnie chwilę potrwa…"
    luszcz "Za kilka dni powinno być gotowe."
    
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

label drukarka3d2:
    if yusuke_social_link >= 1 and yusuke_social_link <= 5:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj22 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj21 with fade
            
            show luszcz neutral right at center
            luszcz "Dzień dobry panowie"

            yusuke "Dzień dobry"

            kazuma "Dzień dobry"

        else:
            if drukowanko == 1:
                play music "audio/music/drukowanie.mp3"
                scene bg pokoj16 with fade
            else:
                play music "audio/music/pokoj.mp3"
                scene bg pokoj15 with fade
            
            show luszcz neutral right at center
            luszcz "Dzień dobry"

            yusuke "Dzień dobry"
    else:
        if yusuke_social_link >= 6:
            if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj20 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj19 with fade
                
                show luszcz neutral right at center
                luszcz "Dzień dobry"

                kazuma "Dzień dobry"
                
            else:
                if drukowanko == 1:
                    play music "audio/music/drukowanie.mp3"
                    scene bg pokoj2 with fade
                else:
                    play music "audio/music/pokoj.mp3"
                    scene bg pokoj with fade

    show luszcz neutral at center

    luszcz "Wreszcie… czas drukowania dobiegł końca."
    luszcz "Chodź tu mój drogi…"

    $ drukowanko = 0
    $ drukarka3d_social_link = 2

    if yusuke_social_link == 0:
        if kazuma_social_link >= 1 and kazuma_social_link <= 2 or kazuma_social_link == 12:
            if drukowanko == 1:
                scene bg pokoj24 
            else:
                scene bg pokoj23
        else:
            if drukowanko == 1:
                scene bg pokoj18
            else:
                scene bg pokoj17 

    else:
        if yusuke_social_link >= 1 and yusuke_social_link <= 5:
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
                
        else:
            if yusuke_social_link >= 6:
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
    
    show luszcz neutral at center
  
    $ miecz3d = 1
    "{i}*Wydrukowany Miecz został dodany do ekwipunku*{/i}"
    luszcz "Hel je"
    
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