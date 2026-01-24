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

    default luszcz_nic = 2
    default urban_nic = 3
    default zyd_nic = 4
    default kazuma_nic = 5
    default tarczownik_nic = 6
    default eminem_nic = 7
    default klata_liczba = 0
    default luszcz_klata = 0
    default urban_klata = 0
    default zyd_klata = 0
    default kazuma_klata = 0
    default tarczownik_klata = 0
    default eminem_klata = 0
    default ring = 0
    default vr = 0
    default memy = 0
    default ziemia = 0
    default nogi = 0
    default zloty = 0

    
label items:
    default ile_item = 0

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

    default piknik = 0
    default cake = 0
    default pills = 0
    default woda = 0
    default ostry = 0
    default lagodny = 0
    default drpepper = 0
    default jabole = 0
    default royal = 0
    default warzywo = 0
    default banany = 0
    default skalka = 0
    default granat = 0

label items_fabularne:
    default ile_item_fabularne = 0
    default stronaf1 = 0   
    default stronaf2 = 0
    default stronaf3 = 0   

    default piernik = 0
    default lopatka = 0
    default krowka = 0
    default kremowka = 0
    default biblia = 0
    default ailbib = 0
    default wazon_wezy = 0
    default glowa = 0
    default zielona_kula = 0
    default aparat = 0
    default kartka = 0
    default dinozaur = 0
    default cialo = 0
    default cybertruck = 0
    default okulary = 0
    default klucz = 0
    default folder_memow = 0

    default piernikx = 0
    default lopatkax = 0
    default krowkax = 0
    default kremowkax = 0
    default bibliax = 0
    default ailbibx = 0
    default wazon_wezyx = 0
    default glowax = 0
    default zielona_kulax = 0
    default aparatx = 0
    default kartkax = 0
    default dinozaurx = 0
    default cialox = 0
    default cybertruckx = 0
    default okularyx = 0
    default kluczx = 0
    default folder_memowx = 0

label eq:
    $ config.menu_include_disabled = False
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
                                    $ tarczownik_min_attack += 1
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
            label zbroja:
                menu:
                    "{b}Łuszcz (HP:[luszcz_hp]){/b}" if luszcz_sojusznik == 1 and luszcz_nic == 2:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ ring = 2
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ vr = 2
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ memy = 2
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ ziemia = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ luszcz_nic = 1
                                    $ zloty = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Diamentowa Klata{/b}" if luszcz_sojusznik == 1 and luszcz_klata == 2:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if luszcz_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ ring = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ vr = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ memy = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ ziemia = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ nogi = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ luszcz_klata = 1
                                    $ zloty = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ luszcz_klata = 1
                                    $ luszcz_nic = 2
                                    $ klata_liczba += 1
                                    $ luszcz_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Pierścień z Władców Pierścieni{/b}" if luszcz_sojusznik == 1 and ring == 2:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or luszcz_nic == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 2
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 2
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 2
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ ring = 1
                                    $ luszcz_nic = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): VR Headset{/b}" if luszcz_sojusznik == 1 and vr == 2:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or luszcz_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 2
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 2
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 2
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ vr = 1
                                    $ luszcz_nic = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Szalik z Memów{/b}" if luszcz_sojusznik == 1 and memy == 2:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or luszcz_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 2
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 2
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 2
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ memy = 1
                                    $ luszcz_nic = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if luszcz_sojusznik == 1 and ziemia == 2:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or luszcz_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 2
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 2
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 2
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ ziemia = 1
                                    $ luszcz_nic = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Długie Nogi{/b}" if luszcz_sojusznik == 1 and nogi == 2:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or luszcz_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp -= 10
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ nogi = 1
                                    $ luszcz_nic = 2
                                    $ luszcz_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Łuszcz (HP:[luszcz_hp]): Złoty Człowiek{/b}" if luszcz_sojusznik == 1 and zloty == 2:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or luszcz_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ luszcz_klata = 2
                                    $ klata_liczba -= 1
                                    $ luszcz_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 2
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 2
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 2
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 2
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 2
                                    $ luszcz_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if luszcz_nic == 1:
                                    $ zloty = 1
                                    $ luszcz_nic = 2
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja

                    





                    "{b}Shadow (HP:[eminem_hp]){/b}" if eminem_sojusznik == 1 and eminem_nic == 7:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ ring = 7
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ vr = 7
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ memy = 7
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ ziemia = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ eminem_nic = 1
                                    $ zloty = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Diamentowa Klata{/b}" if eminem_sojusznik == 1 and eminem_klata == 7:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if eminem_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ ring = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ vr = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ memy = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ ziemia = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ nogi = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ eminem_klata = 1
                                    $ zloty = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ eminem_klata = 1
                                    $ eminem_nic = 7
                                    $ klata_liczba += 1
                                    $ eminem_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Pierścień z Władców Pierścieni{/b}" if eminem_sojusznik == 1 and ring == 7:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or eminem_nic == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 7
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 7
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 7
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ ring = 1
                                    $ eminem_nic = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): VR Headset{/b}" if eminem_sojusznik == 1 and vr == 7:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or eminem_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 7
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 7
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 7
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ vr = 1
                                    $ eminem_nic = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Szalik z Memów{/b}" if eminem_sojusznik == 1 and memy == 7:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or eminem_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 7
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 7
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 7
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ memy = 1
                                    $ eminem_nic = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if eminem_sojusznik == 1 and ziemia == 7:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or eminem_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 7
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 7
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 7
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ ziemia = 1
                                    $ eminem_nic = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Długie Nogi{/b}" if eminem_sojusznik == 1 and nogi == 7:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or eminem_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp -= 10
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 7
                                    $ eminem_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 7
                                    $ eminem_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 7
                                    $ eminem_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 7
                                    $ eminem_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 7
                                    $ eminem_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ nogi = 1
                                    $ eminem_nic = 7
                                    $ eminem_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Shadow (HP:[eminem_hp]): Złoty Człowiek{/b}" if eminem_sojusznik == 1 and zloty == 7:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or eminem_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ eminem_klata = 7
                                    $ klata_liczba -= 1
                                    $ eminem_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 7
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 7
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 7
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 7
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 7
                                    $ eminem_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if eminem_nic == 1:
                                    $ zloty = 1
                                    $ eminem_nic = 7
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja







                    "{b}Jerzy Urban (HP:[urban_hp]){/b}" if urban_sojusznik == 1 and urban_nic == 3:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ ring = 3
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ vr = 3
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ memy = 3
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ ziemia = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ urban_nic = 1
                                    $ zloty = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Diamentowa Klata{/b}" if urban_sojusznik == 1 and urban_klata == 3:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if urban_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ ring = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ vr = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ memy = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ ziemia = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ nogi = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ urban_klata = 1
                                    $ zloty = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ urban_klata = 1
                                    $ urban_nic = 3
                                    $ klata_liczba += 1
                                    $ urban_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Pierścień z Władców Pierścieni{/b}" if urban_sojusznik == 1 and ring == 3:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or urban_nic == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 3
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 3
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 3
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ ring = 1
                                    $ urban_nic = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): VR Headset{/b}" if urban_sojusznik == 1 and vr == 3:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or urban_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 3
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 3
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 3
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ vr = 1
                                    $ urban_nic = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Szalik z Memów{/b}" if urban_sojusznik == 1 and memy == 3:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or urban_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 3
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 3
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 3
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ memy = 1
                                    $ urban_nic = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if urban_sojusznik == 1 and ziemia == 3:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or urban_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 3
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 3
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 3
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ ziemia = 1
                                    $ urban_nic = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Długie Nogi{/b}" if urban_sojusznik == 1 and nogi == 3:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or urban_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp -= 10
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 3
                                    $ urban_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 3
                                    $ urban_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 3
                                    $ urban_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 3
                                    $ urban_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 3
                                    $ urban_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ nogi = 1
                                    $ urban_nic = 3
                                    $ urban_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Jerzy Urban (HP:[urban_hp]): Złoty Człowiek{/b}" if urban_sojusznik == 1 and zloty == 3:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or urban_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ urban_klata = 3
                                    $ klata_liczba -= 1
                                    $ urban_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 3
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 3
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 3
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 3
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 3
                                    $ urban_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if urban_nic == 1:
                                    $ zloty = 1
                                    $ urban_nic = 3
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja








                    "{b}Żyd (HP:[zyd_hp]){/b}" if zyd_sojusznik == 1 and zyd_nic == 4:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ ring = 4
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ vr = 4
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ memy = 4
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ ziemia = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ zyd_nic = 1
                                    $ zloty = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Diamentowa Klata{/b}" if zyd_sojusznik == 1 and zyd_klata == 4:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if zyd_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ ring = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ vr = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ memy = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ ziemia = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ nogi = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ zyd_klata = 1
                                    $ zloty = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ zyd_klata = 1
                                    $ zyd_nic = 4
                                    $ klata_liczba += 1
                                    $ zyd_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Pierścień z Władców Pierścieni{/b}" if zyd_sojusznik == 1 and ring == 4:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or zyd == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 4
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 4
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 4
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ ring = 1
                                    $ zyd_nic = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): VR Headset{/b}" if zyd_sojusznik == 1 and vr == 4:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or zyd_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 4
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 4
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 4
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ vr = 1
                                    $ zyd_nic = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Szalik z Memów{/b}" if zyd_sojusznik == 1 and memy == 4:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or zyd_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 4
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 4
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 4
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ memy = 1
                                    $ zyd_nic = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if zyd_sojusznik == 1 and ziemia == 4:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or zyd_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 4
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 4
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 4
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ ziemia = 1
                                    $ zyd_nic = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Długie Nogi{/b}" if zyd_sojusznik == 1 and nogi == 4:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or zyd_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp -= 10
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 4
                                    $ zyd_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 4
                                    $ zyd_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 4
                                    $ zyd_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 4
                                    $ zyd_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 4
                                    $ zyd_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ nogi = 1
                                    $ zyd_nic = 4
                                    $ zyd_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Żyd (HP:[zyd_hp]): Złoty Człowiek{/b}" if zyd_sojusznik == 1 and zloty == 4:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zyd_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ zyd_klata = 4
                                    $ klata_liczba -= 1
                                    $ zyd_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 4
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 4
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 4
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 4
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 4
                                    $ zyd_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if zyd_nic == 1:
                                    $ zloty = 1
                                    $ zyd_nic = 4
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    




                    "{b}Kazuma (HP:[kazuma_hp]){/b}" if kazuma_sojusznik == 1 and kazuma_nic == 5:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ ring = 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ vr = 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ memy = 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ ziemia = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ kazuma_nic = 1
                                    $ zloty = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Diamentowa Klata{/b}" if kazuma_sojusznik == 1 and kazuma_klata == 5:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if kazuma_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ ring = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ vr = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ memy = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ ziemia = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ nogi = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ kazuma_klata = 1
                                    $ zloty = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ kazuma_klata = 1
                                    $ kazuma_nic = 5
                                    $ klata_liczba += 1
                                    $ kazuma_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Pierścień z Władców Pierścieni{/b}" if kazuma_sojusznik == 1 and ring == 5:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or kazuma_nic == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 5
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ ring = 1
                                    $ kazuma_nic = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): VR Headset{/b}" if kazuma_sojusznik == 1 and vr == 5:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or kazuma_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 5
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ vr = 1
                                    $ kazuma_nic = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Szalik z Memów{/b}" if kazuma_sojusznik == 1 and memy == 5:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or kazuma_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 5
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ memy = 1
                                    $ kazuma_nic = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if kazuma_sojusznik == 1 and ziemia == 5:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or kazuma_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 5
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ ziemia = 1
                                    $ kazuma_nic = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Długie Nogi{/b}" if kazuma_sojusznik == 1 and nogi == 5:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or kazuma_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp -= 10
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ nogi = 1
                                    $ kazuma_nic = 5
                                    $ kazuma_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Kazuma (HP:[kazuma_hp]): Złoty Człowiek{/b}" if kazuma_sojusznik == 1 and zloty == 5:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or kazuma_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ kazuma_klata = 5
                                    $ klata_liczba -= 1
                                    $ kazuma_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 5
                                    $ kazuma_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if kazuma_nic == 1:
                                    $ zloty = 1
                                    $ kazuma_nic = 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    






                    "{b}Naofumi (HP:[tarczownik_hp]){/b}" if tarczownik_sojusznik == 1 and tarczownik_nic == 6:
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ ring = 6
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ vr = 6
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ memy = 6
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ ziemia = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ tarczownik_nic = 1
                                    $ zloty = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Diamentowa Klata{/b}" if tarczownik_sojusznik == 1 and tarczownik_klata == 6:
                        window show
                        "{i}Moje klejnoty. +5HP{/i}"
                        window hide
                        if tarczownik_nic == 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ ring = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ vr = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ memy = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ ziemia = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ nogi = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ tarczownik_klata = 1
                                    $ zloty = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja

                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ tarczownik_klata = 1
                                    $ tarczownik_nic = 6
                                    $ klata_liczba += 1
                                    $ tarczownik_hp -= 5
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Pierścień z Władców Pierścieni{/b}" if tarczownik_sojusznik == 1 and ring == 6:
                        window show
                        "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                        window hide
                        if klata_liczba >= 1 or tarczownik_nic == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ring = 1
                                    $ vr = 6
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ring = 1
                                    $ memy = 6
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ ziemia = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ring = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ring = 1
                                    $ zloty = 6
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ ring = 1
                                    $ tarczownik_nic = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): VR Headset{/b}" if tarczownik_sojusznik == 1 and vr == 6:
                        window show
                        "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or tarczownik_nic == 1 or memy == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza"
                                    window hide
                                    $ vr = 1
                                    $ ring = 6
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ vr = 1
                                    $ memy = 6
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ ziemia = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ vr = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ vr = 1
                                    $ zloty = 6
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ vr = 1
                                    $ tarczownik_nic = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Szalik z Memów{/b}" if tarczownik_sojusznik == 1 and memy == 6:
                        window show
                        "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or tarczownik_nic == 1 or ziemia == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ring = 6
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ memy = 1
                                    $ vr = 6
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ ziemia = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ memy = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ memy = 1
                                    $ zloty = 6
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ memy = 1
                                    $ tarczownik_nic = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Kawałek ziemi, po której stąpał Jan Paweł 2{/b}" if tarczownik_sojusznik == 1 and ziemia == 6:
                        window show
                        "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or tarczownik_nic == 1 or nogi == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ ring = 6
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ vr = 6
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ memy = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ ziemia = 1
                                    $ zloty = 6
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ ziemia = 1
                                    $ tarczownik_nic = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Długie Nogi{/b}" if tarczownik_sojusznik == 1 and nogi == 6:
                        window show
                        "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or tarczownik_nic == 1 or zloty == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp -= 10
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ring = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ vr = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ memy = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ ziemia = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja
                                
                                "{b}Złoty Człowiek{/b}" if zloty == 1:
                                    window show
                                    "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                                    window hide
                                    $ nogi = 1
                                    $ zloty = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ nogi = 1
                                    $ tarczownik_nic = 6
                                    $ tarczownik_hp -= 10
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja
                    
                    "{b}Naofumi (HP:[tarczownik_hp]): Złoty Człowiek{/b}" if tarczownik_sojusznik == 1 and zloty == 6:
                        window show
                        "{i}Pozdrawiamy Dominikę. Gdy umrzesz odżywasz. Działa tylko raz na walkę{/i}"
                        window hide
                        if klata_liczba >= 1 or ring == 1 or vr == 1 or memy == 1 or ziemia == 1 or nogi == 1 or tarczownik_nic == 1:
                            menu:         
                                "{b}Diamentowa Klata{/b}" if klata_liczba >= 1:
                                    window show
                                    "{i}Moje klejnoty. +5HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ tarczownik_klata = 6
                                    $ klata_liczba -= 1
                                    $ tarczownik_hp += 5
                                    jump zbroja
                                
                                "{b}Pierścień z Władców Pierścieni{/b}" if ring == 1:
                                    window show
                                    "{i}Pierścień z Władców Pierścieni. 33%% w każdej turze na utworzenie potężnej obrony dla posiadacza{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ring = 6
                                    jump zbroja
                                
                                "{b}VR Headset{/b}" if vr == 1:
                                    window show
                                    "{i}Dla pół-żywych lol. W każdej turze rzyga na losowego przeciwnika zadając 1-2 DMG{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ vr = 6
                                    jump zbroja

                                "{b}Szalik z Memów{/b}" if memy == 1:
                                    window show
                                    "{i}Zaspamowany z miłością. 15%% szans na odbicie obrażeń do atakującego{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ memy = 6
                                    jump zbroja
                                
                                "{b}Kawałek ziemi, po której stąpał Jan Paweł 2" if ziemia == 1:
                                    window show
                                    "{i}Jak Pan Jezus powiedział. Gdy nosiciel atakuje, leczy się o 1-2 HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ ziemia = 6
                                    jump zbroja
                                
                                "{b}Długie Nogi{/b}" if nogi == 1:
                                    window show
                                    "{i}Wysoki chłopak. Szybki. +10HP{/i}"
                                    window hide
                                    $ zloty = 1
                                    $ nogi = 6
                                    $ tarczownik_hp += 10
                                    jump zbroja
                                
                                "{b}Zdejmij Zbroję{/b}" if tarczownik_nic == 1:
                                    $ zloty = 1
                                    $ tarczownik_nic = 6
                                    jump zbroja
                                
                                "{b}Powrót":
                                    jump zbroja

                        else:
                            jump zbroja



                    "{b}Powrót":
                        jump eq
            jump eq
            
        "{b}Itemy Fabularne{/b}" if ile_item_fabularne > 0: 
            $ stronaf1 = 0   
            $ stronaf2 = 0
            $ stronaf3 = 0  
            $ piernikx = 0
            $ lopatkax = 0
            $ krowkax = 0
            $ kremowkax = 0
            $ bibliax = 0
            $ ailbibx = 0
            $ wazon_wezyx = 0
            $ glowax = 0
            $ zielona_kulax = 0
            $ aparatx = 0
            $ kartkax = 0
            $ dinozaurx = 0
            $ cialox = 0
            $ cybertruckx = 0
            $ okularyx = 0
            $ kluczx = 0
            $ folder_memowx = 0

            if piernik >= 1:
                $ stronaf1 += 1
                $ piernikx += 1
                
            if lopatka >= 1:
                $ stronaf1 += 1
                $ lopatkax += 1
                
            if krowka >= 1:
                $ stronaf1 += 1
                $ krowkax += 1

            if kremowka >= 1:
                $ stronaf1 += 1
                $ kremowkax += 1

            if biblia >= 1:
                $ stronaf1 += 1
                $ bibliax += 1
                
            if ailbib >= 1:
                $ stronaf1 += 1
                $ ailbibx += 1
                
            if wazon_wezy >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ wazon_wezyx += 1

            else:
                if wazon_wezy >= 1:
                    $ wazon_wezyx += 2
                    $ stronaf2 += 1
                
            if glowa >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ glowax += 1

            else:
                if glowa >= 1:
                    $ glowax += 2
                    $ stronaf2 += 1
                
            if zielona_kula >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ zielona_kulax += 1

            else:
                if zielona_kula >= 1:
                    $ zielona_kulax += 2
                    $ stronaf2 += 1
                
            if aparat >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ aparatx += 1

            else:
                if aparat >= 1:
                    $ aparatx += 2
                    $ stronaf2 += 1
                
            if kartka >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ kartkax += 1

            else:
                if kartka >= 1:
                    $ kartkax += 2
                    $ stronaf2 += 1
                
            if dinozaur >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ dinozaurx += 1

            else: 
                if dinozaur >= 1 and stronaf2 < 5:
                    $ dinozaurx += 2
                    $ stronaf2 += 1
                
                else: 
                    if dinozaur >= 1:
                        $ dinozaurx += 3
                        $ stronaf3 += 1
            
            if cialo >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ cialox += 1

            else: 
                if cialo >= 1 and stronaf2 < 5:
                    $ cialox += 2
                    $ stronaf2 += 1
                
                else: 
                    if cialo >= 1:
                        $ cialox += 3
                        $ stronaf3 += 1
            
            if cybertruck >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ cybertruckx += 1

            else: 
                if cybertruck >= 1 and stronaf2 < 5:
                    $ cybertruckx += 2
                    $ stronaf2 += 1
                
                else: 
                    if cybertruck >= 1:
                        $ cybertruckx += 3
                        $ stronaf3 += 1
            
            if okulary >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ okularyx += 1

            else: 
                if okulary >= 1 and stronaf2 < 5:
                    $ okularyx += 2
                    $ stronaf2 += 1
                
                else: 
                    if okulary >= 1:
                        $ okularyx += 3
                        $ stronaf3 += 1
            
            if klucz >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ kluczx += 1

            else: 
                if klucz >= 1 and stronaf2 < 5:
                    $ kluczx += 2
                    $ stronaf2 += 1
                
                else: 
                    if klucz >= 1:
                        $ kluczx += 3
                        $ stronaf3 += 1
            
            if folder_memow >= 1 and stronaf1 < 6:
                $ stronaf1 += 1
                $ folder_memowx += 1

            else: 
                if folder_memow >= 1 and stronaf2 < 5:
                    $ folder_memowx += 2
                    $ stronaf2 += 1
                
                else: 
                    if folder_memow >= 1:
                        $ folder_memowx += 3
                        $ stronaf3 += 1

            label itemy_fabularne:
                menu:
                    "{b}Piernik{/b}" if piernikx == 1:
                        window show
                        "{i}Piernik jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Łopatka{/b}" if lopatkax == 1:
                        window show
                        "{i}Łopatka jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Krówka{/b}" if krowkax == 1:
                        window show
                        "{i}Krówka jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Kremówka{/b}" if kremowkax == 1:
                        window show
                        "{i}Kremówka jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Biblia{/b}" if bibliax == 1:
                        window show
                        "{i}Biblia jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Ailbib{/b}" if ailbibx == 1:
                        window show
                        "{i}Ailbib jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Wazon Węży{/b}" if wazon_wezyx == 1:
                        window show
                        "{i}Wazon Węży jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Głowa Nemeczka{/b}" if glowax == 1:
                        window show
                        "{i}Głowa Nemeczka jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Kula Toxic Pea{/b}" if zielona_kulax == 1:
                        window show
                        "{i}Kula Toxic Pea jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Aparat{/b}" if aparatx == 1:
                        window show
                        "{i}Aparat jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Kartka z Życzeniami{/b}" if kartkax == 1:
                        window show
                        "{i}Kartka z Życzeniami jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Dinozaur{/b}" if dinozaurx == 1:
                        window show
                        "{i}Dinozaur jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Ciało Eminema{/b}" if cialox == 1:
                        window show
                        "{i}Ciało Eminema jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Tesla Cybertruck{/b}" if cybertruckx == 1:
                        window show
                        "{i}Tesla Cybertruck jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Okulary z Wąsem{/b}" if okularyx == 1:
                        window show
                        "{i}Okulary z Wąsem jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Klucz{/b}" if kluczx == 1:
                        window show
                        "{i}Klucz jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{b}Folder z Memami{/b}" if folder_memowx == 1:
                        window show
                        "{i}Folder z Memami jest fajny{/i}"
                        window hide

                        jump itemy_fabularne
                    
                    "{i}Strona 1/2 --->{/i}" if stronaf2 > 0 and stronaf3 == 0:
                        jump itemy_fabularne2
                    
                    "{i}Strona 1/3 --->{/i}" if stronaf2 > 0 and stronaf3 > 0:
                        jump itemy_fabularne2


                    "{b}Powrót{/b}":
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

label itemy_fabularne2:
    menu:
        "{b}Wazon Węży{/b}" if wazon_wezyx == 2:
            window show
            "{i}Wazon Węży jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Głowa Nemeczka{/b}" if glowax == 2:
            window show
            "{i}Głowa Nemeczka jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Kula Toxic Pea{/b}" if zielona_kulax == 2:
            window show
            "{i}Kula Toxic Pea jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Aparat{/b}" if aparatx == 2:
            window show
            "{i}Aparat jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Kartka z Życzeniami{/b}" if kartkax == 2:
            window show
            "{i}Kartka z Życzeniami jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Dinozaur{/b}" if dinozaurx == 2:
            window show
            "{i}Dinozaur jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Ciało Eminema{/b}" if cialox == 2:
            window show
            "{i}Ciało Eminema jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Tesla Cybertruck{/b}" if cybertruckx == 2:
            window show
            "{i}Tesla Cybertruck jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Okulary z Wąsem{/b}" if okularyx == 2:
            window show
            "{i}Okulary z Wąsem jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Klucz{/b}" if kluczx == 2:
            window show
            "{i}Klucz jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Folder z Memami{/b}" if folder_memowx == 2:
            window show
            "{i}Folder z Memami jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{i}<--- Strona 1/3{/i}" if stronaf3 > 0:
            jump itemy_fabularne
        
        "{i}<--- Strona 1/2{/i}" if stronaf3 == 0:
            jump itemy_fabularne
        
        "{i}Strona 2/3 --->{/i}" if stronaf3 > 0:
            jump itemy_fabularne3

label itemy_fabularne3:
    menu:
        "{b}Dinozaur{/b}" if dinozaurx == 3:
            window show
            "{i}Dinozaur jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Ciało Eminema{/b}" if cialox == 3:
            window show
            "{i}Ciało Eminema jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Tesla Cybertruck{/b}" if cybertruckx == 3:
            window show
            "{i}Tesla Cybertruck jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Okulary z Wąsem{/b}" if okularyx == 3:
            window show
            "{i}Okulary z Wąsem jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Klucz{/b}" if kluczx == 3:
            window show
            "{i}Klucz jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{b}Folder z Memami{/b}" if folder_memowx == 3:
            window show
            "{i}Folder z Memami jest fajny{/i}"
            window hide

            jump itemy_fabularne
        
        "{i}<--- Strona 2/3{/i}":
            jump itemy_fabularne2
        