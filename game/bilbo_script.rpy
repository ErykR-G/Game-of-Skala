label bilbo:
    label bilbo1:
        scene bg przystanek_noc with fade
        show luszcz neutral at center
        luszcz "Ktoś tutaj śpi nie będę mu przeszkadzał."
        luszcz "Chociarz… ma gołe stopy…"
        menu:
            "{i}pogilgaj stupki{/i}":
                luszcz "giligiligiligili"
                nikt "hihihihi przestań przestań… hrrrrrrr… *honk mimimimi*"
                luszcz "hehe"
                jump sloneczna
            
            "{i}niet{/i}":
                jump sloneczna
    
    label bilbo2:
        scene bg przystanek with fade
        show luszcz neutral at slightleft
        show bilbo neutral at slightright
        luszcz "Serwus wyglądasz jakbyś czegoś szukał"

        bilbo "Dzień dobry. Istotnie czegoś szukam, i jest to transport."
        bilbo "Ja, na imię mam Bilbo, i mój brat Dilbo próbujemy dostać się do Pustelni Błogosławionej Salmonelli na tun tun tun zachód stąd."
        bilbo "Jednakże nie ma szans że będziemy tam iść całą drogę na nogach. Bo nam się nie chce. I nie chciałbym podrażnić moich wrażliwych stópek."
        bilbo "Więc jakbyś miał nas czym podwieźć to byłoby wyśmienicie."

        luszcz "A co was tam sprowadza"

        bilbo "Wybieramy się na ekpikckcą przygodę aby utrzeć noska somogowi o imieniu Smoug"
        bilbo "Gdyż winny jest za odebranie nam naszych drogich braci"
        bilbo "Ailbo i Cilbo"
        bilbo "Mieli jeszcze tyle życia przed sobą…"
        bilbo "Musimy tam dojechać a dużo jest przeszkód po drodze i Dilbo często musi isć siurać więc to nie jest takie hop siup, pewnie spora porcja dnia zejdzie"
        bilbo "Ale wiesz dostaniesz część skarbu smoga na pewno więc jest to raczej uczciwa wymiana."

        luszcz "Okej… mamy tótaj smoka?"

        bilbo "Nie smoka tylko smoga tego jakby wiesz tego z Krakowa"
        bilbo "W sumie nie wiem co tu robi ale wysoki czarodziej ezoteriusz powiedział nam że jest w pustelni."

        luszcz "A jak mielibyście pokonać smog?"
        
        bilbo "Pomyślałem że wymyślimy coś po drodzę"

        luszcz "oo okej"

        bilbo "To jak zabrałbyś się z nami? Swoją drogą nie mamy żadnych predyspozycji do walki będziemy raczej stać obok i patrzeć gdyby coś się działo. Nie chciałbym też podrażnić moich wrażliwych stópek."

        $ config.menu_include_disabled = True
        menu:
            "{i}tak mam czym jechać i możemy to zrobić (5h){/i}" if cybertruck == 1:
                $ config.menu_include_disabled = False
                if timer >= 360 and timer <= 990 or timer >= 1800 and timer <= 2430 or timer >= 3240 and timer <= 3870 or timer >= 4680 and timer <= 5310 or timer >= 6120 and timer <= 6750 or timer >= 7560 and timer <= 8190 or timer >= 9000 and timer <= 9630 or timer >= 10440 and timer <= 10980:
                    $ timer += 300
                    $ bilbo_social_link = 1
                    luszcz "Wiesz co akurat skołowałem sobie takiego grata na kółkach może się tutaj dobrze zmarnować"

                    bilbo "Ojej na poważnie? Ale klasa"
                    bilbo "Jesteśmy ci sromotnie wdzięczni. To ja pójdę wyciągnąć brata z krzaków a ty przygotuj furę"

                else:
                    luszcz "Ojej no chciałbym ale jóż się robi puzyno to tak średnio dziś"

                    bilbo "To jak chcesz to możesz jutro"

                    luszcz "Okej pewnie jasne zobaczymy, czas pokarze"

                    jump sloneczna
            
            "{i}nuh uh{/i}":
                $ config.menu_include_disabled = False
                luszcz "Nie nie biorę was nigdzie sorki"
                bilbo "Dobra to będę tu stał cały czas aż ktoś się będzie chciał i mógł"
                jump sloneczna
        
        scene bg black with fade


