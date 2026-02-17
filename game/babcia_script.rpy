
label babcia:
    label babcia1:
        scene bg dom_kultury with fade
        play music "audio/music/dom_kultury.mp3"
        show luszcz neutral at slightleft
        show babcia neutral at slightright

        babcia "Oh… Witaj kochaniutki"

        luszcz "Dzień dobry, gdzie cała reszta?"

        babcia "Wszyscy odpuścili sobie dom kultury po całym incydencie z czarodziejem"
        babcia "Zostałam tylko ja, i szyję sobie szaliki."
        babcia "A potrzebujesz czegoś?"

        luszcz "Nie do końca, po prostu fajnie by było przekonać lódzi do walki o Skałę."

        babcia "Moje poparcie masz."

        luszcz "Dziękuję pani."

        babcia "Uszyć ci może szalik?"
        
        luszcz "Skąd się bieże pani uprzejmość?"

        babcia "Cóż, przede wszystkim, uprzejmość nie musi się skądś brać."
        babcia "Jestem tobie jednak bardzo wdzięczna za pokonanie tego czarodzieja."
        babcia "Bardzo go nielubiłam."
        babcia "Nigdy nie mogliśmy się dogadać."
        babcia "Nie dlatego że ma touretta, tylko dlatego że jest czarny."

        luszcz "Ah."
        luszcz "Anyway jeśli pani hce to chętnie przyjmę od pani szalik."

        babcia "Dobrze, tylko przynieś mi proszę jakiś materiał"
        babcia "Kończy mi się włóczka więc będziemy musieli szpącić dookoła."

        luszcz "Hm… materiał…"
        luszcz "Mam 5 terabajtuw memów na konkuterze, czy to zadziała?"

        babcia "Nie jestem pewna co to znaczy, ale chyba tak.."
        babcia "Zobaczymy, gdy je przyniesiesz."

        luszcz "W takim razie pójdę po nie."

        babcia "Dobrze mój drogi."

        $ babcia_wybory == 2
        $ babcia_social_link = 1
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
    
    label babcia2:
        if yusuke_social_link == 0:
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
            
            show yusuke neutral at slightleft2
            show luszcz neutral right at slightright

            yusuke "Ah… więc to ty musisz być właścicielem tego pomieszczenia."

            luszcz "Dafaq? Kim ty jesteś co ty robisz w moim pokojó?"

            if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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

                    if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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

                    if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
                    luszcz "Memy"
                
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

                    if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
                    luszcz "Memy"

        else:
            if yusuke_social_link >= 1 and yusuke_social_link <= 5:
                if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
                    if kazuma_social_link >= 1 and kazuma_social_link <= 2:
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
        luszcz "Okej, gdzie ja miałem folder z memami…"
        luszcz "O, jest!"
        luszcz "O, jest!"
        luszcz "O nie…"
        luszcz "Są dwa…"
        luszcz "Oj…………….."
        luszcz "Który folder wybrać…?"

        menu:
            "{b}memy{/b}":
                show mem zorder 50 at center

            "{b}Memy{/b}":
                show mem zorder 50 at center

        nikt "Fan fakt:"
        nikt "Czy wiecie że PopCap, studio które stworzyło pvz"
        nikt "Było oryginalnie stworzone pod nazwą “Sexy Action Cool”?"
        nikt "Ich pierwszą grą wideo był strip poker, który miał zarabiać pieniądze na ich późniejsze tytuły."

        hide mem

        luszcz "Okej, w takim razie to ten drugi folder."

        $ babcia_social_link = 2
        $ ile_item_fabularne += 1
        $ folder_memow = 1

        "{i}*Folder Memów został dodany do ekwipunku*{/i}" 

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

    label babcia3:
        scene bg dom_kultury with fade
        play music "audio/music/dom_kultury.mp3"
        show luszcz neutral at left
        show babcia neutral at center

        babcia "Czy masz materiał, o który prosiłam?"

        luszcz "Mam!"


        luszcz "Proszę, oto wszystkie memy kture posiadam."

        babcia "Dziękuję. Zamknij na chwilkę oczy."

        luszcz "Oki"
        
        scene bg black with fade
        scene bg dom_kultury with fade
        show luszcz neutral at left
        show babcia neutral at center

        babcia "Proszę, oto twój szalik"

        luszcz "Wow ale fajny"

        $ memy = 1
        "{i}*Szalik z Memów został dodany do ekwipunku*{/i}" 

        luszcz "Dziękuję, rasistowska babciu"

        babcia "Nie ma za co, bogaty seksisto"
        babcia "Skop księdzu dupsko"

        luszcz "Spk."

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




