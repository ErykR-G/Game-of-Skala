label bronie: 
    default luszcz_gitara = 1
    default urban_fuck = 1
    default zyd_chanuka = 1
    default kazuma_chunchunmaru = 1
    default tarczownik_legendary_shield = 1

    default luszcz_przepychaczka = 0
    default urban_przepychaczka = 0
    default zyd_przepychaczka = 0
    default kazuma_przepychaczka = 0
    default tarczownik_przepychaczka = 0

    default luszcz_stop = 0
    default urban_stop = 0
    default zyd_stop = 0
    default kazuma_stop = 0
    default tarczownik_stop = 0

label eq:
    window hide
    show eq zorder 100 at center
    $ eq_on = 1
    menu:
        "{b}Broń{/b}":
            label bron:
                menu:
                    "{b}Łuszcz: Gitara (ATK:1-2){/b}" if luszcz_sojusznik == 1 and luszcz_gitara == 1:
                        window show
                        "{i}Gitara jest git{/i}"
                        window hide

                        if luszcz_przepychaczka == 2 or luszcz_stop == 2:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if luszcz_gitara == 2:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_gitara = 2
                                    $ luszcz_gitara = 1
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if luszcz_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_gitara = 2
                                    $ luszcz_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if luszcz_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_gitara = 2
                                    $ luszcz_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Łuszcz: Przepychaczka (ATK:2-2){/b}" if luszcz_sojusznik == 1 and luszcz_przepychaczka == 1:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if luszcz_gitara == 2 or luszcz_stop == 2:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if luszcz_gitara == 2:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ luszcz_gitara = 1
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if luszcz_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ luszcz_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if luszcz_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 2
                                    $ luszcz_max_attack -= 2
                                    $ luszcz_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ luszcz_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Łuszcz: Stop (ATK:1-4){/b}" if luszcz_sojusznik == 1 and luszcz_stop == 1:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if luszcz_gitara == 2 or luszcz_przepychaczka == 2:
                            menu:
                                "{b}Gitara (ATK:1-2){/b}" if luszcz_gitara == 2:
                                    window show
                                    "{i}Gitara jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ luszcz_stop = 2
                                    $ luszcz_gitara = 1
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if luszcz_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ luszcz_stop = 2
                                    $ luszcz_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ luszcz_min_attack += 2
                                    $ luszcz_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if luszcz_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ luszcz_min_attack -= 1
                                    $ luszcz_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ luszcz_stop = 2
                                    $ luszcz_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ luszcz_min_attack += 1
                                    $ luszcz_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    

                    "{b}Shadow: Ręka (ATK:2-3){/b}" if eminem_sojusznik == 1:
                        jump bron


                    "{b}Jerzy Urban: Fuck (ATK:0-2){/b}" if urban_sojusznik == 1 and urban_fuck == 1:
                        window show
                        "{i}Fuck jest git{/i}"
                        window hide

                        if urban_przepychaczka == 2 or urban_stop == 2:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if urban_fuck == 2:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ urban_fuck = 2
                                    $ urban_fuck = 1
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if urban_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ urban_fuck = 2
                                    $ urban_przepychaczka = 1
                                    $ luszcz_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if urban_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 0
                                    $ urban_max_attack -= 2
                                    $ urban_fuck = 2
                                    $ urban_stop = 1
                                    $ luszcz_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Jerzy Urban: Przepychaczka (ATK:2-2){/b}" if urban_sojusznik == 1 and urban_przepychaczka == 1:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if urban_fuck == 2 or urban_stop == 2:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if urban_fuck == 2:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_fuck = 1
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if urban_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_przepychaczka = 1
                                    $ luszcz_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if urban_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 2
                                    $ urban_max_attack -= 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_stop = 1
                                    $ luszcz_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Jerzy Urban: Stop (ATK:1-4){/b}" if urban_sojusznik == 1 and urban_stop == 1:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if urban_fuck == 2 or urban_przepychaczka == 2:
                            menu:
                                "{b}Fuck (ATK:0-2){/b}" if urban_fuck == 2:
                                    window show
                                    "{i}Fuck jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ luszcz_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ urban_stop = 2
                                    $ urban_fuck = 1
                                    $ urban_min_attack += 0
                                    $ urban_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if urban_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ luszcz_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ urban_stop = 2
                                    $ urban_przepychaczka = 1
                                    $ luszcz_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ urban_min_attack += 2
                                    $ urban_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if urban_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ urban_min_attack -= 1
                                    $ urban_max_attack -= 4
                                    $ luszcz_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ urban_stop = 2
                                    $ urban_stop = 1
                                    $ luszcz_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ urban_min_attack += 1
                                    $ urban_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron

                    


                    "{b}Żyd: Chanuka (ATK:1-3){/b}" if zyd_sojusznik == 1 and zyd_chanuka == 1:
                        window show
                        "{i}Chanuka jest git{/i}"
                        window hide

                        if zyd_przepychaczka == 2 or zyd_stop == 2:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if zyd_chanuka == 2:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ zyd_chanuka = 2
                                    $ zyd_chanuka = 1
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if zyd_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ zyd_chanuka = 2
                                    $ zyd_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if zyd_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 2
                                    $ zyd_chanuka = 2
                                    $ zyd_stop = 1
                                    $ urban_stop = 3
                                    $ luszcz_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Żyd: Przepychaczka (ATK:2-2){/b}" if zyd_sojusznik == 1 and zyd_przepychaczka == 1:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if zyd_chanuka == 2 or zyd_stop == 2:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if zyd_chanuka == 2:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ zyd_chanuka = 1
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if zyd_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ zyd_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if zyd_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 2
                                    $ zyd_max_attack -= 2
                                    $ zyd_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ zyd_stop = 1
                                    $ urban_stop = 3
                                    $ luszcz_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Żyd: Stop (ATK:1-4){/b}" if zyd_sojusznik == 1 and zyd_stop == 1:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if zyd_chanuka == 2 or zyd_przepychaczka == 2:
                            menu:
                                "{b}Chanuka (ATK:1-3){/b}" if zyd_chanuka == 2:
                                    window show
                                    "{i}Chanuka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ urban_stop = 2
                                    $ luszcz_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ zyd_stop = 2
                                    $ zyd_chanuka = 1
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if zyd_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ urban_stop = 2
                                    $ luszcz_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ zyd_stop = 2
                                    $ zyd_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ zyd_min_attack += 2
                                    $ zyd_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if zyd_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ zyd_min_attack -= 1
                                    $ zyd_max_attack -= 4
                                    $ urban_stop = 2
                                    $ luszcz_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ zyd_stop = 2
                                    $ zyd_stop = 1
                                    $ urban_stop = 3
                                    $ luszcz_stop = 3
                                    $ kazuma_stop = 3
                                    $ tarczownik_stop = 3
                                    $ zyd_min_attack += 1
                                    $ zyd_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    



                    "{b}Kazuma: Chunchunmaru (ATK:0-6){/b}" if kazuma_sojusznik == 1 and kazuma_chunchunmaru == 1:
                        window show
                        "{i}Chunchunmaru jest git{/i}"
                        window hide

                        if kazuma_przepychaczka == 2 or kazuma_stop == 2:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if kazuma_chunchunmaru == 2:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_chunchunmaru = 2
                                    $ kazuma_chunchunmaru = 1
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if kazuma_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_chunchunmaru = 2
                                    $ kazuma_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if kazuma_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_chunchunmaru = 2
                                    $ kazuma_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ luszcz_stop = 3
                                    $ tarczownik_stop = 3
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Kazuma: Przepychaczka (ATK:2-2){/b}" if kazuma_sojusznik == 1 and kazuma_przepychaczka == 1:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if kazuma_chunchunmaru == 2 or kazuma_stop == 2:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if kazuma_chunchunmaru == 2:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ kazuma_chunchunmaru = 1
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if kazuma_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ kazuma_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if kazuma_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 2
                                    $ kazuma_max_attack -= 2
                                    $ kazuma_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 2
                                    $ kazuma_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ luszcz_stop = 3
                                    $ tarczownik_stop = 3
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Kazuma: Stop (ATK:1-4){/b}" if kazuma_sojusznik == 1 and kazuma_stop == 1:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if kazuma_chunchunmaru == 2 or kazuma_przepychaczka == 2:
                            menu:
                                "{b}Chunchunmaru (ATK:0-6){/b}" if kazuma_chunchunmaru == 2:
                                    window show
                                    "{i}Chunchunmaru jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ luszcz_stop = 2
                                    $ tarczownik_stop = 2
                                    $ kazuma_stop = 2
                                    $ kazuma_chunchunmaru = 1
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if kazuma_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ luszcz_stop = 2
                                    $ kazuma_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_przepychaczka = 3
                                    $ kazuma_min_attack += 2
                                    $ kazuma_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if kazuma_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ kazuma_min_attack -= 1
                                    $ kazuma_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ luszcz_stop = 2
                                    $ tarczownik_stop = 2
                                    $ kazuma_stop = 2
                                    $ kazuma_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ luszcz_stop = 3
                                    $ tarczownik_stop = 3
                                    $ kazuma_min_attack += 1
                                    $ kazuma_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    



                    "{b}Naofumi: Legendary Shield (ATK:1-3){/b}" if tarczownik_sojusznik == 1 and tarczownik_legendary_shield == 1:
                        window show
                        "{i}Legendary Shield jest git{/i}"
                        window hide

                        if tarczownik_przepychaczka == 2 or tarczownik_stop == 2:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if tarczownik_legendary_shield == 2:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_legendary_shield = 2
                                    $ tarczownik_legendary_shield = 1
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if tarczownik_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_legendary_shield = 2
                                    $ tarczownik_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if tarczownik_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_legendary_shield = 2
                                    $ tarczownik_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ luszcz_stop = 3
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót":
                                    jump bron

                        else:
                            jump bron

                    "{b}Naofumi: Przepychaczka (ATK:2-2){/b}" if tarczownik_sojusznik == 1 and tarczownik_przepychaczka == 1:
                        window show
                        "{i}Przepychaczka jest git{/i}"
                        window hide

                        if tarczownik_legendary_shield == 2 or tarczownik_stop == 2:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if tarczownik_legendary_shield == 2:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ tarczownik_legendary_shield = 1
                                    $ tarczownik_min_attack += 1
                                    $ tarczownikwnikwnik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if tarczownik_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ tarczownik_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if tarczownik_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 2
                                    $ tarczownik_max_attack -= 2
                                    $ tarczownik_przepychaczka = 2
                                    $ urban_przepychaczka = 2
                                    $ zyd_przepychaczka = 2
                                    $ kazuma_przepychaczka = 2
                                    $ luszcz_przepychaczka = 2
                                    $ tarczownik_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ luszcz_stop = 3
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 4
                                    jump bron
                                
                                "{b}Powrót{/b}":
                                    jump bron

                        else:
                            jump bron
                    
                    "{b}Naofumi: Stop (ATK:1-4){/b}" if tarczownik_sojusznik == 1 and tarczownik_stop == 1:
                        window show
                        "{i}Stop jest git{/i}"
                        window hide

                        if tarczownik_legendary_shield == 2 or tarczownik_przepychaczka == 2:
                            menu:
                                "{b}Legendary Shield (ATK:1-3){/b}" if tarczownik_legendary_shield == 2:
                                    window show
                                    "{i}Legendary Shield jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ luszcz_stop = 2
                                    $ tarczownik_stop = 2
                                    $ tarczownik_legendary_shield = 1
                                    $ tarczownik_min_attack += 1
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                    
                                "{b}Przepychaczka (ATK:2-2){/b}" if tarczownik_przepychaczka == 2:
                                    window show
                                    "{i}Przpychaczka jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ luszcz_stop = 2
                                    $ tarczownik_stop = 2
                                    $ tarczownik_przepychaczka = 1
                                    $ urban_przepychaczka = 3
                                    $ zyd_przepychaczka = 3
                                    $ kazuma_przepychaczka = 3
                                    $ luszcz_przepychaczka = 3
                                    $ tarczownik_min_attack += 2
                                    $ tarczownik_max_attack += 2
                                    jump bron
                                
                                "{b}Stop (ATK:1-4){/b}" if tarczownik_stop == 2:
                                    window show
                                    "{i}Stop jest git{/i}"
                                    window hide
                                    $ tarczownik_min_attack -= 1
                                    $ tarczownik_max_attack -= 4
                                    $ urban_stop = 2
                                    $ zyd_stop = 2
                                    $ kazuma_stop = 2
                                    $ tarczownik_stop = 2
                                    $ luszcz_stop = 2
                                    $ tarczownik_stop = 1
                                    $ urban_stop = 3
                                    $ zyd_stop = 3
                                    $ kazuma_stop = 3
                                    $ luszcz_stop = 3
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
