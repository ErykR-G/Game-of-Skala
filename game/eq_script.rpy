label bronie: 
    default gitara = 2
    default fuck = 3
    default chanuka = 4
    default chunchunmaru = 5
    default legendary_shield = 6
    default stop = 0
    default miecz_swietlny = 0
    default ostrza_chaosu = 0
    default patyk = 0
    default bazooka = 0
    default miecz3d = 0
    default przepychaczka_liczba = 0
    default luszcz_przepychaczka = 0
    default urban_przepychaczka = 0
    default zyd_przepychaczka = 0
    default kazuma_przepychaczka = 0
    default tarczownik_przepychaczka = 0

    
label items:
    default ile_item = 2
    default bandaz = 1
    default granat = 1


label eq:
    window hide
    show eq zorder 100 at center
    $ eq_on = 1
    menu:
        "{b}Broń{/b}":
            label bron:
                menu:
                    "{b}Łuszcz: Gitara (ATK:1-4){/b}" if luszcz_sojusznik == 1 and gitara == 2:
                        window show
                        "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                        window hide

                        if przepychaczka_liczba >= 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Przepychaczka (ATK:2-4){/b}" if luszcz_sojusznik == 1 and luszcz_przepychaczka == 2:
                        window show
                        "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                        window hide

                        if gitara == 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Łuszcz: Znak Drogowy (ATK:1-6){/b}" if luszcz_sojusznik == 1 and stop == 2:
                        window show
                        "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Miecz Świetlny (ATK:3-4){/b}" if luszcz_sojusznik == 1 and miecz_swietlny == 2:
                        window show
                        "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or stop == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 3
                                    $ luszcz_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if luszcz_sojusznik == 1 and ostrza_chaosu == 2:
                        window show
                        "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or stop == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 0
                                    $ luszcz_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Fajny Patyk (ATK:1-5){/b}" if luszcz_sojusznik == 1 and patyk == 2:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or stop == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Łuszcz: Wężowa Bazooka (ATK:1-3){/b}" if luszcz_sojusznik == 1 and bazooka == 2:
                        window show
                        "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or stop == 1 or miecz3d == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz3d = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Wydrukowany Miecz (ATK:2-5){/b}" if luszcz_sojusznik == 1 and miecz3d == 2:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                        window hide

                        if gitara == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or stop == 1:
                            menu:         
                                "{b}Gitara (ATK:1-4){/b}" if gitara == 1:
                                    window show
                                    "{b}(ATK:1-4){/b}\n{i}Gitara siema{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ luszcz_przepychaczka = 2
                                    $ przepychaczka_liczba -= 1
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ miecz_swietlny = 2
                                    $ luszcz_min_attack += 3
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ ostrza_chaosu = 2
                                    $ luszcz_min_attack += 0
                                    $ luszcz_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ patyk = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 3
                                    $ miecz3d = 1
                                    $ bazooka = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 1
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                        


                    "{b}Shadow: Ręka (ATK:2-5){/b}" if eminem_sojusznik == 1:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Jedyna taka ręka człowieka zdolnego zamienić sie w żywą atomówkę {w}\nDruga niestety uległa destrukcji ...{/i}"
                        window hide

                        jump bron
                    


                    "{b}Jerzy Urban: Fuck (ATK:0-4){/b}" if urban_sojusznik == 1 and fuck == 3:
                        window show
                        "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                        window hide

                        if przepychaczka_liczba >= 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Przepychaczka (ATK:2-4){/b}" if urban_sojusznik == 1 and urban_przepychaczka == 3:
                        window show
                        "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                        window hide

                        if fuck == 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Jerzy Urban: Znak Drogowy (ATK:1-6){/b}" if urban_sojusznik == 1 and stop == 3:
                        window show
                        "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Miecz Świetlny (ATK:3-4){/b}" if urban_sojusznik == 1 and miecz_swietlny == 3:
                        window show
                        "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or stop == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 3
                                    $ urban_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if urban_sojusznik == 1 and ostrza_chaosu == 3:
                        window show
                        "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or stop == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4)" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Fajny Patyk (ATK:1-5){/b}" if urban_sojusznik == 1 and patyk == 3:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or stop == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Jerzy Urban: Wężowa Bazooka (ATK:1-3){/b}" if urban_sojusznik == 1 and bazooka == 3:
                        window show
                        "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or stop == 1 or miecz3d == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz3d = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Wydrukowany Miecz (ATK:2-5){/b}" if urban_sojusznik == 1 and miecz3d == 3:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                        window hide

                        if fuck == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or stop == 1:
                            menu:         
                                "{b}Fuck (ATK:0-4){/b}" if fuck == 1:
                                    window show
                                    "{b}(ATK:0-4){/b}\n{i}No kochane dzieci mam tu dla was ho ho ho ho ho ho o{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ urban_przepychaczka = 3
                                    $ przepychaczka_liczba -= 1
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ miecz_swietlny = 3
                                    $ urban_min_attack += 3
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ ostrza_chaosu = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ patyk = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 3
                                    $ miecz3d = 1
                                    $ bazooka = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 1
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    


                    "{b}Żyd: Chanuka (ATK:1-5){/b}" if zyd_sojusznik == 1 and chanuka == 4:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                        window hide

                        if przepychaczka_liczba >= 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ chanuka = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Przepychaczka (ATK:2-4){/b}" if zyd_sojusznik == 1 and zyd_przepychaczka == 4:
                        window show
                        "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                        window hide

                        if chanuka == 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ bazooka = 4
                                    $ zyd_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Żyd: Znak Drogowy (ATK:1-6){/b}" if zyd_sojusznik == 1 and stop == 4:
                        window show
                        "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Miecz Świetlny (ATK:3-4){/b}" if zyd_sojusznik == 1 and miecz_swietlny == 4:
                        window show
                        "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or stop == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 3
                                    $ zyd_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if zyd_sojusznik == 1 and ostrza_chaosu == 4:
                        window show
                        "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or stop == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 0
                                    $ zyd_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Fajny Patyk (ATK:1-5){/b}" if zyd_sojusznik == 1 and patyk == 4:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or stop == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Żyd: Wężowa Bazooka (ATK:1-3){/b}" if zyd_sojusznik == 1 and bazooka == 4:
                        window show
                        "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or stop == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chanuka (ATK:1-5){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz3d = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Wydrukowany Miecz (ATK:2-5){/b}" if zyd_sojusznik == 1 and miecz3d == 4:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or stop == 1:
                            menu:         
                                "{b}chanuka (ATK:1-4){/b}" if chanuka == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Co pan wyprawia{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ zyd_przepychaczka = 4
                                    $ przepychaczka_liczba -= 1
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ miecz_swietlny = 4
                                    $ zyd_min_attack += 3
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ ostrza_chaosu = 4
                                    $ zyd_min_attack += 0
                                    $ zyd_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ patyk = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 3
                                    $ miecz3d = 1
                                    $ bazooka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 1
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    


                    "{b}Kazuma: Chunchunmaru (ATK:0-8){/b}" if kazuma_sojusznik == 1 and chunchunmaru == 5:
                        window show
                        "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                        window hide

                        if przepychaczka_liczba >= 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaru = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaru = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaruunmaru = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaruunmaru = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaru = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaru = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 6
                                    $ chunchunmaru = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Przepychaczka (ATK:2-4){/b}" if kazuma_sojusznik == 1 and kazuma_przepychaczka == 5:
                        window show
                        "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                        window hide

                        if chunchunmaru == 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Kazuma: Znak Drogowy (ATK:1-6){/b}" if kazuma_sojusznik == 1 and stop == 5:
                        window show
                        "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 6
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Miecz Świetlny (ATK:3-4){/b}" if kazuma_sojusznik == 1 and miecz_swietlny == 5:
                        window show
                        "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or stop == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 3
                                    $ kazuma_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if kazuma_sojusznik == 1 and ostrza_chaosu == 5:
                        window show
                        "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or stop == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 0
                                    $ kazuma_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Fajny Patyk (ATK:1-5){/b}" if kazuma_sojusznik == 1 and patyk == 5:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or stop == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Kazuma: Wężowa Bazooka (ATK:1-3){/b}" if kazuma_sojusznik == 1 and bazooka == 5:
                        window show
                        "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or stop == 1 or miecz3d == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz3d = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Wydrukowany Miecz (ATK:2-5){/b}" if kazuma_sojusznik == 1 and miecz3d == 5:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or stop == 1:
                            menu:         
                                "{b}Chunchunmaru (ATK:0-8){/b}" if chunchunmaru == 1:
                                    window show
                                    "{b}(ATK:0-8){/b}\n{i}Siurowaty anime miecz{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 6
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ kazuma_przepychaczka = 5
                                    $ przepychaczka_liczba -= 1
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ miecz_swietlny = 5
                                    $ kazuma_min_attack += 3
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ patyk = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 3
                                    $ miecz3d = 1
                                    $ bazooka = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 1
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    


                    "{b}Naofumi: Legendary Shield (ATK:1-5){/b}" if tarczownik_sojusznik == 1 and legendary_shield == 6:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                        window hide

                        if przepychaczka_liczba >= 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ legendary_shield = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Przepychaczka (ATK:2-4){/b}" if tarczownik_sojusznik == 1 and tarczownik_przepychaczka == 6:
                        window show
                        "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                        window hide

                        if legendary_shield == 1 or stop == 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 1
                                    $ przepychaczka_liczba += 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Naofumi: Znak Drogowy (ATK:1-6){/b}" if tarczownik_sojusznik == 1 and stop == 6:
                        window show
                        "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Miecz Świetlny (ATK:3-4){/b}" if tarczownik_sojusznik == 1 and miecz_swietlny == 6:
                        window show
                        "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or stop == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 3
                                    $ tarczownik_max_attack -= 2
                                    $ miecz_swietlny = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if tarczownik_sojusznik == 1 and ostrza_chaosu == 6:
                        window show
                        "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or stop == 1 or patyk == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 0
                                    $ tarczownik_max_attack -= 1
                                    $ ostrza_chaosu = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumii: Fajny Patyk (ATK:1-5){/b}" if tarczownik_sojusznik == 1 and patyk == 6:
                        window show
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or stop == 1 or bazooka == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 3
                                    $ patyk = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Naofumi: Wężowa Bazooka (ATK:1-3){/b}" if tarczownik_sojusznik == 1 and bazooka == 6:
                        window show
                        "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or stop == 1 or miecz3d == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wydrukowany Miecz (ATK:2-5){/b}" if miecz3d == 1:
                                    window show
                                    "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 1
                                    $ bazooka = 1
                                    $ miecz3d = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Wydrukowany Miecz (ATK:2-5){/b}" if tarczownik_sojusznik == 1 and miecz3d == 6:
                        window show
                        "{b}(ATK:2-5){/b}\n{i}Zrobiony w jedynej kuźni w Skale. Zwiększa dmg do (ATK:3-7), gdy nosiciel ma poniżej 50%% hp{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka_liczba >= 1 or miecz_swietlny == 1 or ostrza_chaosu == 1 or patyk == 1 or bazooka == 1 or stop == 1:
                            menu:         
                                "{b}Legendary Shield (ATK:1-5){/b}" if legendary_shield == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Niekonsekwentna anime tarcza{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Przepychaczka (ATK:2-4){/b}" if przepychaczka_liczba >= 1:
                                    window show
                                    "{b}(ATK:2-4){/b}\n{i}Idealny prezent. Szansa na zestunnowanie wroga na turę{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ tarczownik_przepychaczka = 6
                                    $ przepychaczka_liczba -= 1
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Znak Drogowy (ATK:1-6){/b}" if stop == 1:
                                    window show
                                    "{b}(ATK:1-6){/b}\n{i}Ma na sobie duży napis NIE{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ stop = 6
                                    $ tarczownikwnik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Miecz Świetlny (ATK:3-4){/b}" if miecz_swietlny == 1:
                                    window show
                                    "{b}(ATK:3-4){/b}\n{i}Świeci w kolorze fioletowym{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ miecz_swietlny = 6
                                    $ tarczownik_min_attack += 3
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Ostrza Chaosu (ATK:0-3 FOR ALL){/b}" if ostrza_chaosu == 1:
                                    window show
                                    "{b}(ATK:0-3 FOR ALL){/b}\n{i}O bogowie, wojna xdxd lol. Poza głównym atakiem zadają wszystkim po 0-1dmg. Gdy przeciwnik jest jeden, +1 min dmg.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ ostrza_chaosu = 6
                                    $ tarczownik_min_attack += 0
                                    $ tarczownik_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. Mała szansa na podwojenie obrażeń.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ patyk = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 3
                                    jump bron
                                
                                "{b}Wężowa Bazooka (ATK:1-3){/b}" if bazooka == 1:
                                    window show
                                    "{b}(ATK:1-3){/b}\n{i}Jak się robi więcej dzieci? Zatruwa zaatakowanego wroga na 3 tury.{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 3
                                    $ miecz3d = 1
                                    $ bazooka = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 1
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron



                    "{b}Powrót":
                        jump eq
                    


        "{b}Zbroja{/b}":
            "Kiedyś będą"
            jump eq
            
        "{b}Itemy Fabularne{/b}":
            "Kiedyś będą"
            jump eq

        
        "{b}Itemy do Walki{/b}":
            label itemy_do_walki:
                menu:
                    "{b}Bandaż (+5HP){/b}" if bandaz >= 1:
                        window show
                        "{i}Bandaż jest git{/i}"
                        window hide

                        jump itemy_do_walki

                    "{b}Granat (8 DMG){/b}" if granat >= 1:
                        window show
                        "{i}Granat jest git{/i}"
                        window hide

                        jump itemy_do_walki

                    "{b}Powrót{/b}":
                        jump eq

        "{b}Zamknij{/b}":
            hide eq 
            window show
            $ eq_on = 0
            pass

    return
