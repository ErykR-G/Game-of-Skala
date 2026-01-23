
label toxic_pea:
    label toxic_pea1:
        play music "audio/music/toxic1.mp3"
        scene bg przed_walka_toxic_pea with fade
        show luszcz neutral at left
        show toxic_pea neutral at slightright

        toxic "Oh, to ty."
        toxic "A jak masz wgl na imie?"

        luszcz "Maciej"

        toxic "Już mamy jednego takiego"
        toxic "To jak coś to będziemy na ciebie mówić Maciej_Rel, spoko?"

        luszcz "Dobrze.."
        luszcz2 "(czemó akurat tak…?)"

        toxic "Dobra, słuchaj, nie mamy czasu, zombiaki nadchodzą."
        toxic "Od dłuższego czasu zaczęły nocami wychodzić przez jakiś portal schowany niedaleko."
        toxic "Ogród Szalonego Dawida, znaczy naszego szefa jest jedyną rzeczą trzymającą je przed pełną inwazją na Skałę."
        toxic "Raczej sobie radzimy, ale zdarza się, że nas przeliczają, więc każda pomoc się przyda."
        toxic "Jak tu jesteś, to raczej umiesz się bić, cnie?"

        luszcz2 "Oh, i to jeszcze jak!"
        luszcz2 "Jeszcze nie dawno udało mi się pokonać…"

        toxic "Nie, nie ma teraz czasu na rozmowy."
        toxic "Broń w dłoń i do boju!"

        jump after_fight131
        jump fight131
        label after_fight131:
            play music "audio/music/toxic2.mp3"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            luszcz2 "Ufff…"

            toxic "Dobra robota, Maciej_Rel"
            toxic "Nie jesteś taki słaby jak mi się wydawało"

            luszcz2 "Hehe… dzięki.."

            toxic "Wiesz co, nie będę owijał w bawełne."
            toxic "Ruchasz czy trzeba z tobą chodzić?"
            show luszcz blush
            menu:
                "{b}rucham{/b}":
                    show luszcz sigma
                    luszcz2 "Od takiego kociaka nie odrzóciłbym propozycji 😼"

                    toxic "Ta? Zobaczymy kto będzie miauczeć w łóżku."
                
                "{b}chodzić{/b}":
                    luszcz2 "A co jeśli powiem, rze trzeba ze mną chodzić?"

                    toxic "To po dzisiejszej nocy dowiemy się czy się jeszcze zobaczymy."
            
            scene bg black with fade
            "{i}Jeden netflix później{/i}"
            scene bg przed_walka_toxic_pea with fade
            show luszcz neutral at slightleft
            show toxic_pea neutral at slightright

            toxic "Dzięki, było całkiem nieźle."
            toxic "Twoje palce nie były idealne, ale można nad tym popracować."

            luszcz2 "Ohhhh Toxic, jedyne co mogę powiedzieć, to że było za mało radia"

            toxic "To jak, kolejna rundka następnej nocy?"
            toxic "Ale pamiętaj, na nagrodę trzeba zapracować. Walczysz z nami albo wypad."

            menu:
                "{b}PLANT ZEGZ 🤤{/b}":
                    show luszcz sigma

                    luszcz2 "Pewnie, widzimy się kochanie."

                    toxic "Nie no nie mów tak do mnie"

                    show luszcz neutral

                    luszcz2 "A jak do ciebie mówić?"

                    toxic "Tatusiu"

                    luszcz2 "Dobże tatusiu"

                    toxic "XD"
                    toxic "Dobra, cześć, widzimy się"

                    luszcz2 "Cześć..!"

                    scene bg black with fade

                    n "{i}Łuszczu nagle wzdrygnął, tak jakby jego ciało próbowało opanować się po tym czego dziś doznał.{/i}"

                    n "{i}Jedna noc spełniła tyle jego pragnień, odpowiedziała na tyle potrzeb.{/i}"

                    n "{i}Potrzeb, bez których spełnienia jego ciało więdło.{/i}"

                    n "{i}Nareszcie, w jego życiu miłosnym zasadziło się nasionko nadziei.{/i}"

                    n "{i}Albo, alternatywnie, nasienie.{/i}"
                
                "{b}NO THANKS{/b}":
                    luszcz2 "Coś we mnie stara się mnie zmusić do odmowy."

                    toxic "Nie wiem o czym nawijasz, ale w razie czego widzimy się jutro."
                    toxic "A jak nie przyjdziesz, to i tak dzięki za noc."
                    toxic "Nara!"

                    luszcz2 "Pa.."

                    scene bg black with fade

                    n "{i}Łuszczu nagle wzdrygnął, tak jakby jego ciało próbowało opanować się po tym czego dziś doznał.{/i}"

                    n "{i}Jedna noc spełniła tyle jego pragnień, odpowiedziała na tyle potrzeb.{/i}"

                    n "{i}Potrzeb, bez których spełnienia jego ciało więdło.{/i}"

                    n "{i}Jednakże, coś wewnątrz każe mu uciekać od szansy, którą dało mu życie.{/i}"

                    n "{i}Czy Łuszczu ulegnie, i pozwoli drugiej duszy trzymać nad nim konewkę?{/i}"

            $ toxic_pea_social_link = 2
            $ toxic_pea_wybory = 1

            if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                play music "audio/music/pole.mp3"
            else:
                play music "audio/music/pole_noc.mp3"
            jump wolbromska



