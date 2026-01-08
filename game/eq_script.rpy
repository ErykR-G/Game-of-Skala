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
    default ile_item = 13

    default strona1 = 0   
    default strona2 = 0
    default piknikx = 0
    default cakex = 0
    default pillsx = 0
    default wodax = 0
    default ostryx = 0
    default lagodnyx = 0
    default drpepperx = 0
    default jabolex = 0
    default royalx = 0
    default warzywox = 0
    default bananyx = 0
    default skalkax = 0
    default granatx = 0

    default piknik = 1
    default cake = 1
    default pills = 20
    default woda = 2
    default ostry = 2
    default lagodny = 3
    default drpepper = 5
    default jabole = 5
    default royal = 4
    default warzywo = 3
    default banany = 4
    default skalka = 2
    default granat = 3

    


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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    $ chunchunmaru = 1
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
                                    $ chunchunmaru = 1
                                    $ ostrza_chaosu = 5
                                    $ kazuma_min_attack += 0
                                    $ kazuma_max_attack += 1
                                    jump bron

                                "{b}Fajny Patyk (ATK:1-5){/b}" if patyk == 1:
                                    window show
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                        "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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
                                    "{b}(ATK:1-5){/b}\n{i}Przeepicki badyl. 33%% na podwojenie obrażeń.{/i}"
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

        
        "{b}Itemy do Walki{/b}" if ile_item > 0: 
            $ strona1 = 0   
            $ strona2 = 0
            $ piknikx = 0
            $ cakex = 0
            $ pillsx = 0
            $ wodax = 0
            $ ostryx = 0
            $ lagodnyx = 0
            $ drpepperx = 0
            $ jabolex = 0
            $ royalx = 0
            $ warzywox = 0
            $ bananyx = 0
            $ skalkax = 0
            $ granatx = 0

            if piknik >= 1:
                $ strona1 += 1
                $ piknikx += 1
                
            if cake >= 1:
                $ strona1 += 1
                $ cakex += 1
                
            if pills >= 1:
                $ strona1 += 1
                $ pillsx += 1

            if woda >= 1:
                $ strona1 += 1
                $ wodax += 1

            if ostry >= 1:
                $ strona1 += 1
                $ ostryx += 1
                
            if lagodny >= 1:
                $ strona1 += 1
                $ lagodnyx += 1
                
            if drpepper >= 1 and strona1 < 6:
                $ strona1 += 1
                $ drpepperx += 1

            else:
                if drpepper >= 1:
                    $ drpepperx += 2
                    $ strona2 += 1
                
            if jabole >= 1 and strona1 < 6:
                $ strona1 += 1
                $ jabolex += 1

            else:
                if jabole >= 1:
                    $ jabolex += 2
                    $ strona2 += 1
                
            if royal >= 1 and strona1 < 6:
                $ strona1 += 1
                $ royalx += 1

            else:
                if royal >= 1:
                    $ royalx += 2
                    $ strona2 += 1
                
            if warzywo >= 1 and strona1 < 6:
                $ strona1 += 1
                $ warzywox += 1

            else:
                if warzywo >= 1:
                    $ warzywox += 2
                    $ strona2 += 1
                
            if banany >= 1 and strona1 < 6:
                $ strona1 += 1
                $ bananyx += 1

            else:
                if banany >= 1:
                    $ bananyx += 2
                    $ strona2 += 1
                
            if skalka >= 1 and strona1 < 6:
                $ strona1 += 1
                $ skalkax += 1

            else: 
                if skalka >= 1:
                    $ skalkax += 2
                    $ strona2 += 1
                
            if granat >= 1 and strona1 < 6:
                $ strona1 += 1
                $ granatx += 1

            else:
                if granat >= 1:
                    $ granatx += 2
                    $ strona2 += 1

            label itemy_do_walki:
                menu:
                    "{b}Piknik (+FULL HP FOR ALL) x [piknik]{/b}" if piknikx == 1:
                        window show
                        "{i}Nie pamiętam kiedy ostatnio miałem piknik. Leczy całą drużynę do pełni życia{/i}"
                        window hide

                        jump itemy_do_walki

                    "{b}Strawberry Cake (+15HP LUB +5HP FOR ALL) x [cake]{/b}" if cakex == 1:
                        window show
                        "{i}Ciasto truskawkowe, które upiekłeś z Lilith. Leczy +15HP jedenej osbie lub wszystkich po +5HP{/i}"
                        window hide

                        jump itemy_do_walki

                    "{b}Słoik z Pigułkami (+3HP){/b} x [pills]" if pillsx >= 1:
                        window show
                        "{i}Słoik z Pigułkami, którym Lilith prawie Ciebie zabiła. Leczy +3HP od pigułki{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Tutorialowa Woda Święcona (+6HP) x [woda]{/b}" if wodax == 1:
                        window show
                        "{i}leczy. +6HP{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Kebab Ostry (+3HP i +1 MAX DMG) x [ostry]{/b}" if ostryx == 1:
                        window show
                        "{i}Na cienkim, bardzo ostry. +3HP oraz +1 MAX DMG do konca walki{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Kebab Łagodny (+4HP i + 1HP FOR 3 TURNS) x [lagodny]{/b}" if lagodnyx == 1:
                        window show
                        "{i}Pod grubym, trochę łagodny. +4HP oraz +1HP przez 3 tury{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Dr Pepper (+2HP i MAX DMG NEXT ATTACK) x [drpepper]{/b}" if drpepperx == 1:
                        window show
                        "{i}Ulubiony napój Eryka R-G. +2HP oraz następny atak zadaje możliwie najwięcej obrażeń{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Jabole (+6HP) x [jabole]{/b}" if jabolex == 1:
                        window show
                        "{i}Tylko anioły nie płaczą na dniu cebuli (TheMontaże). +6hp oraz następny atak zadaje możliwie najmniej obrażeń{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Royal Cola (+9HP) x [royal]{/b}" if royalx == 1:
                        window show
                        "{i}Ulubiony napój Macieja Ł. +9HP{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Warzywo skalne (+(4-7)HP) x [warzywo]{/b}" if warzywox == 1:
                        window show
                        "{i}warzywko rosnące tylko w Skale. +4-7HP{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Kiść bananów (+3HP FOR ALL) x [banany]{/b}" if bananyx == 1:
                        window show
                        "{i}Uuuu uuu aaaaaa aa aaaaaaa uu u u aaaa. +3HP dla całej drużyny{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Ostra Skałka (5-8 DMG) x [skalka]{/b}" if skalkax == 1:
                        window show
                        "{i}Prosto ze skały ze skały. Zadaje 5-8 DMG{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{b}Granat (4 DMG FOR ALL) x [granat]{/b}" if granatx == 1:
                        window show
                        "{i}Owoc. Zadaje wszystkim przeciwnikom po 4 DMG{/i}"
                        window hide

                        jump itemy_do_walki
                    
                    "{i}Strona 1/2 --->{/i}" if strona2 > 0:
                        jump itemy_do_walki2


                    "{b}Powrót{/b}":
                        jump eq

        "{b}Zamknij{/b}":
            hide eq 
            window show
            $ eq_on = 0
            pass

    return

label itemy_do_walki2:
    menu:
        "{b}Dr Pepper (+2HP i MAX DMG NEXT ATTACK) x [drpepper]{/b}" if drpepperx == 2:
            window show
            "{i}Ulubiony napój Eryka R-G. +2HP oraz następny atak zadaje możliwie najwięcej obrażeń{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Jabole (+6HP) x [jabole]{/b}" if jabolex == 2:
            window show
            "{i}Tylko anioły nie płaczą na dniu cebuli (TheMontaże). +6HP oraz następny atak zadaje możliwie najmniej obrażeń{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Royal Cola (+9HP) x [royal]{/b}" if royalx == 2:
            window show
            "{i}Ulubiony napój Macieja Ł. +9HP{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Warzywo skalne (+(4-7)HP) x [warzywo]{/b}" if warzywox == 2:
            window show
            "{i}warzywko rosnące tylko w Skale. +4-7HP{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Kiść bananów (+3HP FOR ALL) x [banany]{/b}" if bananyx == 2:
            window show
            "{i}Uuuu uuu aaaaaa aa aaaaaaa uu u u aaaa. +3HP dla całej drużyny{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Ostra Skałka (5-8 DMG) x [skalka]{/b}" if skalkax == 2:
            window show
            "{i}Prosto ze skały ze skały. Zadaje 5-8 DMG{/i}"
            window hide

            jump itemy_do_walki2
                    
        "{b}Granat (4 DMG FOR ALL) x [granat]{/b}" if granatx == 2:
            window show
            "{i}Owoc. Zadaje wszystkim przeciwnikom po 4 DMG{/i}"
            window hide

            jump itemy_do_walki2
        
        "{i}<--- Strona 2/2{/i}":
            jump itemy_do_walki