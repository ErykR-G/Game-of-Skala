label bronie: 
    default gitara = 2
    default fuck = 3
    default chanuka = 4
    default chunchunmaru = 5
    default legendary_shield = 6
    default przepychaczka = 0
    default stop = 0


label eq:
    window hide
    show eq zorder 100 at center
    $ eq_on = 1
    menu:
        "{b}Broń{/b}":
            label bron:
                menu:
                    "{b}Łuszcz: Gitara (ATK:1-2){/b}" if luszcz_sojusznik == 1 and gitara == 2:
                        window show
                        "{i}Gitara jest git{/i}"
                        window hide

                        if przepychaczka == 1 or stop == 1:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if gitara == 1:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ przepychaczka = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ gitara = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Łuszcz: Przepychaczka (ATK:2-2){/b}" if luszcz_sojusznik == 1 and przepychaczka == 2:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if gitara == 1 or stop == 1:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if gitara == 1:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ przepychaczka = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Stop (ATK:1-4){/b}" if luszcz_sojusznik == 1 and stop == 2:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if gitara == 1 or przepychaczka == 1:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if gitara == 1:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ gitara = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ przepychaczka = 2
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ stop = 1
                                    $ stop = 2
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    

                    "{b}Shadow: Ręka (ATK:2-3){/b}" if eminem_sojusznik == 1:
                        jump bron


                    "{b}Jerzy Urban: Fuck (ATK:0-2){/b}" if urban_sojusznik == 1 and fuck == 3:
                        window show
                        "{i}Fuck jest git{/i}"
                        window hide

                        if przepychaczka == 1 or stop == 1:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if fuck == 1:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ fuck = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Jerzy Urban: Przepychaczka (ATK:2-2){/b}" if urban_sojusznik == 1 and przepychaczka == 3:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if fuck == 1 or stop == 1:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if fuck == 1:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Stop (ATK:1-4){/b}" if urban_sojusznik == 1 and stop == 3:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if fuck == 1 or przepychaczka == 1:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if fuck == 1:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ fuck = 3
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ stop = 1
                                    $ stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron

                    


                    "{b}Żyd: Chanuka (ATK:1-3){/b}" if zyd_sojusznik == 1 and chanuka == 4:
                        window show
                        "{i}Chanuka jest git{/i}"
                        window hide

                        if przepychaczka == 1 or stop == 1:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if chanuka == 1:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ chanuka = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ chanuka = 1
                                    $ przepychaczka = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ chanuka = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Żyd: Przepychaczka (ATK:2-2){/b}" if zyd_sojusznik == 1 and przepychaczka == 4:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if chanuka == 1 or stop == 1:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if chanuka == 1:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ przepychaczka = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Stop (ATK:1-4){/b}" if zyd_sojusznik == 1 and stop == 4:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if chanuka == 1 or przepychaczka == 1:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if chanuka == 1:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ chanuka = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ przepychaczka = 4
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ stop = 1
                                    $ stop = 4
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    



                    "{b}Kazuma: Chunchunmaru (ATK:0-6){/b}" if kazuma_sojusznik == 1 and chunchunmaru == 5:
                        window show
                        "{i}Chunchunmaru jest git{/i}"
                        window hide

                        if przepychaczka == 1 or stop == 1:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if chunchunmaru == 1:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ chunchunmaru = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ chunchunmaru = 1
                                    $ przepychaczka = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ chunchunmaru = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Kazuma: Przepychaczka (ATK:2-2){/b}" if kazuma_sojusznik == 1 and przepychaczka == 5:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if chunchunmaru == 1 or stop == 1:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if chunchunmaru == 1:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ przepychaczka = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Stop (ATK:1-4){/b}" if kazuma_sojusznik == 1 and stop == 5:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if chunchunmaru == 1 or przepychaczka == 1:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if chunchunmaru == 1:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ chunchunmaru = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ przepychaczka = 5
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ stop = 1
                                    $ stop = 5
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    



                    "{b}Naofumi: Legendary Shield (ATK:1-3){/b}" if tarczownik_sojusznik == 1 and legendary_shield == 6:
                        window show
                        "{i}Legendary Shield jest git{/i}"
                        window hide

                        if przepychaczka == 1 or stop == 1:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if legendary_shield == 1:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ legendary_shield = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ legendary_shield = 1
                                    $ przepychaczka = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ legendary_shield = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Naofumi: Przepychaczka (ATK:2-2){/b}" if tarczownik_sojusznik == 1 and przepychaczka == 6:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if legendary_shield == 1 or stop == 1:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if legendary_shield == 1:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownikwnikwnik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ przepychaczka = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ przepychaczka = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Stop (ATK:1-4){/b}" if tarczownik_sojusznik == 1 and stop == 6:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if legendary_shield == 1 or przepychaczka == 1:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if legendary_shield == 1:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ legendary_shield = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if przepychaczka == 1:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ przepychaczka = 6
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if stop == 1:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ stop = 1
                                    $ stop = 6
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
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
