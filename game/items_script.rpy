label eff:
    label dsdssd:   
        label items11:
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
                    
            menu:
                "{b}Co użyć?{/b}"

                "{b}Piknik (+FULL HP FOR ALL) x [piknik]{/b}" if piknikx == 1:
                    hide chest
                    play sound "audio/sfx/heal.mp3" 
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1:
                            show piknik zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2:
                            show piknik zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3:
                            show piknik zorder 15 at weapon_sojusznik3
                    
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1:
                            show piknik zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2:
                            show piknik zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3:
                            show piknik zorder 15 at weapon_sojusznik3
                    
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1:
                            show piknik zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2:
                            show piknik zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3:
                            show piknik zorder 15 at weapon_sojusznik3
                    
                    if urban_fighter == 1:
                        if urban_wybrany == 1:
                            show piknik zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2:
                            show piknik zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3:
                            show piknik zorder 15 at weapon_sojusznik3
                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1:
                            show piknik zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2:
                            show piknik zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3:
                            show piknik zorder 15 at weapon_sojusznik3

                    if luszcz_hp_now > 0 and luszcz_wybrany > 0:
                        $ luszcz_hp_now = luszcz_hp
                    if eminem_hp_now > 0 and eminem_wybrany > 0:
                        $ eminem_hp_now = eminem_hp
                    if urban_hp_now > 0 and urban_wybrany > 0:
                        $ urban_hp_now = urban_hp
                    if zyd_hp_now > 0 and zyd_wybrany > 0:
                        $ zyd_hp_now = zyd_hp
                    if kazuma_hp_now > 0 and kazuma_wybrany > 0:
                        $ kazuma_hp_now = kazuma_hp
                    if tarczownik_hp_now > 0 and tarczownik_wybrany > 0:
                        $ tarczownik_hp_now = tarczownik_hp
                    "{i}Życie każdej z postaci zostało w pełni przywrócone{/i}"
                    hide piknik
                    $ piknik -= 1
                    if piknik == 0:
                        $ ile_item -= 1
                    jump faza12

                "{b}Strawberry Cake (+15HP LUB +5HP FOR ALL) x [cake]{/b}" if cakex == 1:
                    hide chest

                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik3
                            
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik3
                            
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik3
                            
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik3
                                
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show cake_full zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Zjeść sam? (+15HP){/b}":
                            play sound "audio/sfx/heal.mp3" 
                            if luszcz_fighter == 1:
                                if luszcz_hp_now + 15 >= luszcz_hp:
                                    $ luszcz_hp_now = luszcz_hp
                                    "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                else:
                                    $ luszcz_hp_now += 5
                                    "{i}Łuszcz odzyskał 15 punktów życia{/i}"
                            
                            if eminem_fighter == 1:
                                if eminem_hp_now + 15 >= eminem_hp:
                                    $ eminem_hp_now = eminem_hp
                                    "{i}Shadow odzyskał cały pasek życia{/i}"
                                else:
                                    $ eminem_hp_now += 5
                                    "{i}Shadow odzyskał 15 punktów życia{/i}"
                            
                            if urban_fighter == 1:
                                if urban_hp_now + 15 >= urban_hp:
                                    $ urban_hp_now = urban_hp
                                    "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                else:
                                    $ urban_hp_now += 5
                                    "{i}Jerzy Urban odzyskał 15 punktów życia{/i}"
                            
                            if zyd_fighter == 1:
                                if zyd_hp_now + 15 >= zyd_hp:
                                    $ zyd_hp_now = zyd_hp
                                    "{i}Żyd odzyskał cały pasek życia{/i}"
                                else:
                                    $ zyd_hp_now += 5
                                    "{i}Żyd odzyskał 15 punktów życia{/i}"
                            
                            if kazuma_fighter == 1:
                                if kazuma_hp_now + 15 >= kazuma_hp:
                                    $ kazuma_hp_now = kazuma_hp
                                    "{i}Kazuma odzyskał cały pasek życia{/i}"
                                else:
                                    $ kazuma_hp_now += 5
                                    "{i}Kazuma odzyskał 15 punktów życia{/i}"
                            
                            hide cake_full
                            $ cake -= 1
                            if cake == 0:
                                $ ile_item -= 1
                            jump faza12

                        "{b}Pokroić? (+5HP FOR ALL){/b}":
                            hide cake_full
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show cake1 zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show cake1 zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show cake1 zorder 15 at weapon_sojusznik3
                            
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show cake2 zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show cake2 zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show cake2 zorder 15 at weapon_sojusznik3
                            
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show cake3 zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show cake3 zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show cake3 zorder 15 at weapon_sojusznik3
                            
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show cake4 zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show cake4 zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show cake4 zorder 15 at weapon_sojusznik3
                            
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show cake5 zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show cake5 zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show cake5 zorder 15 at weapon_sojusznik3
                            
                            if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                                show cake6 zorder 15 at weapon_sojusznik1
                            if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                                show cake6 zorder 15 at weapon_sojusznik2
                            if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                                show cake6 zorder 15 at weapon_sojusznik3
                                    
                            if luszcz_hp_now > 0 and luszcz_wybrany > 0:
                                if luszcz_hp_now + 5 >= luszcz_hp:
                                    $ luszcz_hp_now = luszcz_hp
                                else:
                                    $ luszcz_hp_now += 5

                            if eminem_hp_now > 0 and eminem_wybrany > 0:
                                if eminem_hp_now + 5 >= eminem_hp:
                                    $ eminem_hp_now = eminem_hp
                                else:
                                    $ eminem_hp_now += 5
                                
                            if urban_hp_now > 0 and urban_wybrany > 0:
                                if urban_hp_now + 5 >= urban_hp:
                                    $ urban_hp_now = urban_hp
                                else:
                                    $ urban_hp_now += 5

                            if zyd_hp_now > 0 and zyd_wybrany > 0:
                                if zyd_hp_now + 5 >= zyd_hp:
                                    $ zyd_hp_now = zyd_hp
                                else:
                                    $ zyd_hp_now += 5

                            if kazuma_hp_now > 0 and kazuma_wybrany > 0:
                                if kazuma_hp_now + 5 >= kazuma_hp:
                                    $ kazuma_hp_now = kazuma_hp
                                else:
                                    $ kazuma_hp_now += 5

                            if tarczownik_hp_now > 0 and tarczownik_wybrany > 0:
                                if tarczownik__hp_now + 5 >= tarczownik__hp:
                                    $ tarczownik__hp_now = tarczownik__hp
                                else:
                                    $ tarczownik_hp_now += 5
                            
                            play sound "audio/sfx/heal.mp3" 
                            "{i}Wszystkie postacie odzyskały po 5 punktów życia{/i}"
                            hide cake1
                            hide cake2
                            hide cake3
                            hide cake4
                            hide cake5
                            hide cake6

                            $ cake -= 1
                            if cake == 0:
                                $ ile_item -= 1
                            jump faza12

                "{b}Słoik z Pigułkami (+3HP) x [pills] {/b}" if pillsx >= 1:
                    label pigulki11:
                        hide chest
                        if pills == 0:
                            $ ile_item -= 1
                            jump faza12

                        if luszcz_fighter == 1:
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik3
                                
                        if eminem_fighter == 1:
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik3
                                
                        if urban_fighter == 1:
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik3
                                
                        if zyd_fighter == 1:
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik3
                                    
                        if kazuma_fighter == 1:
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show pills zorder 15 at weapon_sojusznik3

                        
                        if luszcz_fighter == 1:
                            menu:
                                "{b}Weź pigułke{/b}":
                                    if luszcz_piguly <= 3:
                                        if luszcz_hp_now + 3 >= luszcz_hp:
                                            $ pills -= 1
                                            $ luszcz_piguly += 1
                                            $ luszcz_hp_now = luszcz_hp
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                            jump pigulki11
                                        else:
                                            $ pills -= 1
                                            $ luszcz_piguly += 1
                                            $ luszcz_hp_now += 3
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Łuszcz odzyskał 3 punkty życia{/i}"
                                            jump pigulki11
                                    
                                    else:
                                        if luszcz_piguly == 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka == 1:
                                                $ luszcz_hp_now = 0
                                                $ pills -= 1
                                                play sound "audio/sfx/lyk.mp3"
                                                queue sound "audio/sfx/spadek.mp3"
                                                "{i}Łuszcz umiera z przedawkowania{/i}"
                                                hide pills
                                                jump faza12

                                            else:
                                                if luszcz_hp_now + 3 >= luszcz_hp:
                                                    $ luszcz_piguly += 1
                                                    $ pills -= 1
                                                    $ luszcz_hp_now = luszcz_hp
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                                    jump pigulki11
                                                else:
                                                    $ pills -= 1
                                                    $ luszcz_piguly += 1
                                                    $ luszcz_hp_now += 3
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Łuszcz odzyskał 3 punkty życia{/i}"
                                                    jump pigulki11
                                        
                                        else:
                                            if luszcz_piguly == 4:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka <= 3:
                                                    $ luszcz_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Łuszcz umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                                else:
                                                    if luszcz_hp_now + 3 >= luszcz_hp:
                                                        $ luszcz_piguly += 1
                                                        $ pills -= 1
                                                        $ luszcz_hp_now = luszcz_hp
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                                        jump pigulki11
                                                    else:
                                                        $ pills -= 1
                                                        $ luszcz_piguly += 1
                                                        $ luszcz_hp_now += 3
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Łuszcz odzyskał 3 punkty życia{/i}"
                                                        jump pigulki11
                                            
                                            else:
                                                if luszcz_piguly >= 5:
                                                    $ luszcz_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Łuszcz umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                "{b}Może lepiej już nie{/b}":
                                    hide pills
                                    jump faza12

                        if eminem_fighter == 1:
                            menu:
                                "{b}Weź pigułke{/b}":
                                    if eminem_piguly <= 3:
                                        if eminem_hp_now + 3 >= eminem_hp:
                                            $ pills -= 1
                                            $ eminem_piguly += 1
                                            $ eminem_hp_now = eminem_hp
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Shadow odzyskał cały pasek życia{/i}"
                                            jump pigulki11
                                        else:
                                            $ pills -= 1
                                            $ eminem_piguly += 1
                                            $ eminem_hp_now += 3
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Shadow odzyskał 3 punkty życia{/i}"
                                            jump pigulki11
                                    
                                    else:
                                        if eminem_piguly == 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka == 1:
                                                $ eminem_hp_now = 0
                                                $ pills -= 1
                                                play sound "audio/sfx/lyk.mp3"
                                                queue sound "audio/sfx/spadek.mp3"
                                                "{i}Shadow umiera z przedawkowania{/i}"
                                                hide pills
                                                jump faza12

                                            else:
                                                if eminem_hp_now + 3 >= eminem_hp:
                                                    $ eminem_piguly += 1
                                                    $ pills -= 1
                                                    $ eminem_hp_now = eminem_hp
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Shadow odzyskał cały pasek życia{/i}"
                                                    jump pigulki11
                                                else:
                                                    $ pills -= 1
                                                    $ eminem_piguly += 1
                                                    $ eminem_hp_now += 3
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Shadow odzyskał 3 punkty życia{/i}"
                                                    jump pigulki11
                                        
                                        else:
                                            if eminem_piguly == 4:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka <= 3:
                                                    $ eminem_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Shadow umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                                else:
                                                    if eminem_hp_now + 3 >= eminem_hp:
                                                        $ eminem_piguly += 1
                                                        $ pills -= 1
                                                        $ eminem_hp_now = eminem_hp
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Shadow odzyskał cały pasek życia{/i}"
                                                        jump pigulki11
                                                    else:
                                                        $ pills -= 1
                                                        $ eminem_piguly += 1
                                                        $ eminem_hp_now += 3
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Shadow odzyskał 3 punkty życia{/i}"
                                                        jump pigulki11
                                            
                                            else:
                                                if eminem_piguly >= 5:
                                                    $ eminem_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Shadow umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                "{b}Może lepiej już nie{/b}":
                                    hide pills
                                    jump faza12

                        if urban_fighter == 1:
                            menu:
                                "{b}Weź pigułke{/b}":            
                                    if urban_piguly <= 3:
                                        if urban_hp_now + 3 >= urban_hp:
                                            $ pills -= 1
                                            $ urban_piguly += 1
                                            $ urban_hp_now = urban_hp
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                            jump pigulki11
                                        else:
                                            $ pills -= 1
                                            $ urban_piguly += 1
                                            $ urban_hp_now += 3
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Jerzy Urban odzyskał 3 punkty życia{/i}"
                                            jump pigulki11
                                    
                                    else:
                                        if urban_piguly == 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka == 1:
                                                $ urban_hp_now = 0
                                                $ pills -= 1
                                                play sound "audio/sfx/lyk.mp3"
                                                queue sound "audio/sfx/spadek.mp3"
                                                "{i}Jerzy Urban umiera z przedawkowania{/i}"
                                                hide pills
                                                jump faza12

                                            else:
                                                if urban_hp_now + 3 >= urban_hp:
                                                    $ urban_piguly += 1
                                                    $ pills -= 1
                                                    $ urban_hp_now = urban_hp
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                                    jump pigulki11
                                                else:
                                                    $ pills -= 1
                                                    $ urban_piguly += 1
                                                    $ urban_hp_now += 3
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Jerzy Urban odzyskał 3 punkty życia{/i}"
                                                    jump pigulki11
                                        
                                        else:
                                            if urban_piguly == 4:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka <= 3:
                                                    $ urban_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Jerzy Urban umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                                else:
                                                    if urban_hp_now + 3 >= urban_hp:
                                                        $ urban_piguly += 1
                                                        $ pills -= 1
                                                        $ urban_hp_now = urban_hp
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                                        jump pigulki11
                                                    else:
                                                        $ pills -= 1
                                                        $ urban_piguly += 1
                                                        $ urban_hp_now += 3
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Jerzy Urban odzyskał 3 punkty życia{/i}"
                                                        jump pigulki11
                                            
                                            else:
                                                if urban_piguly >= 5:
                                                    $ urban_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Jerzy Urban umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                "{b}Może lepiej już nie{/b}":
                                    hide pills
                                    jump faza12

                        if zyd_fighter == 1:
                            menu:
                                "{b}Weź pigułke{/b}":            
                                    if zyd_piguly <= 3:
                                        if zyd_hp_now + 3 >= zyd_hp:
                                            $ pills -= 1
                                            $ zyd_piguly += 1
                                            $ zyd_hp_now = zyd_hp
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Żyd odzyskał cały pasek życia{/i}"
                                            jump pigulki11
                                        else:
                                            $ pills -= 1
                                            $ zyd_piguly += 1
                                            $ zyd_hp_now += 3
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Żyd odzyskał 3 punkty życia{/i}"
                                            jump pigulki11
                                    
                                    else:
                                        if zyd_piguly == 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka == 1:
                                                $ zyd_hp_now = 0
                                                $ pills -= 1
                                                play sound "audio/sfx/lyk.mp3"
                                                queue sound "audio/sfx/spadek.mp3"
                                                "{i}Żyd umiera z przedawkowania{/i}"
                                                hide pills
                                                jump faza12

                                            else:
                                                if zyd_hp_now + 3 >= zyd_hp:
                                                    $ zyd_piguly += 1
                                                    $ pills -= 1
                                                    $ zyd_hp_now = zyd_hp
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Żyd odzyskał cały pasek życia{/i}"
                                                    jump pigulki11
                                                else:
                                                    $ pills -= 1
                                                    $ zyd_piguly += 1
                                                    $ zyd_hp_now += 3
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Żyd odzyskał 3 punkty życia{/i}"
                                                    jump pigulki11
                                        
                                        else:
                                            if zyd_piguly == 4:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka <= 3:
                                                    $ zyd_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Żyd umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                                else:
                                                    if zyd_hp_now + 3 >= zyd_hp:
                                                        $ zyd_piguly += 1
                                                        $ pills -= 1
                                                        $ zyd_hp_now = zyd_hp
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Żyd odzyskał cały pasek życia{/i}"
                                                        jump pigulki11
                                                    else:
                                                        $ pills -= 1
                                                        $ zyd_piguly += 1
                                                        $ zyd_hp_now += 3
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Żyd odzyskał 3 punkty życia{/i}"
                                                        jump pigulki11
                                            
                                            else:
                                                if zyd_piguly >= 5:
                                                    $ zyd_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Żyd umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                "{b}Może lepiej już nie{/b}":
                                    hide pills
                                    jump faza12

                        if kazuma_fighter == 1:
                            menu:
                                "{b}Weź pigułke{/b}":            
                                    if kazuma_piguly <= 3:
                                        if kazuma_hp_now + 3 >= kazuma_hp:
                                            $ pills -= 1
                                            $ kazuma_piguly += 1
                                            $ kazuma_hp_now = kazuma_hp
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Kazuma odzyskał cały pasek życia{/i}"
                                            jump pigulki11
                                        else:
                                            $ pills -= 1
                                            $ kazuma_piguly += 1
                                            $ kazuma_hp_now += 3
                                            play sound "audio/sfx/lyk.mp3"
                                            "{i}Kazuma odzyskał 3 punkty życia{/i}"
                                            jump pigulki11
                                    
                                    else:
                                        if kazuma_piguly == 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka == 1:
                                                $ kazuma_hp_now = 0
                                                $ pills -= 1
                                                play sound "audio/sfx/lyk.mp3"
                                                queue sound "audio/sfx/spadek.mp3"
                                                "{i}Kazuma umiera z przedawkowania{/i}"
                                                hide pills
                                                jump faza12

                                            else:
                                                if kazuma_hp_now + 3 >= kazuma_hp:
                                                    $ kazuma_piguly += 1
                                                    $ pills -= 1
                                                    $ kazuma_hp_now = kazuma_hp
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Kazuma odzyskał cały pasek życia{/i}"
                                                    jump pigulki11
                                                else:
                                                    $ pills -= 1
                                                    $ kazuma_piguly += 1
                                                    $ kazuma_hp_now += 3
                                                    play sound "audio/sfx/lyk.mp3"
                                                    "{i}Kazuma odzyskał 3 punkty życia{/i}"
                                                    jump pigulki11
                                        
                                        else:
                                            if kazuma_piguly == 4:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka <= 3:
                                                    $ kazuma_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Kazuma umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                                else:
                                                    if kazuma_hp_now + 3 >= kazuma_hp:
                                                        $ kazuma_piguly += 1
                                                        $ pills -= 1
                                                        $ kazuma_hp_now = kazuma_hp
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Kazuma odzyskał cały pasek życia{/i}"
                                                        jump pigulki11
                                                    else:
                                                        $ pills -= 1
                                                        $ kazuma_piguly += 1
                                                        $ kazuma_hp_now += 3
                                                        play sound "audio/sfx/lyk.mp3"
                                                        "{i}Kazuma odzyskał 3 punkty życia{/i}"
                                                        jump pigulki11
                                            
                                            else:
                                                if kazuma_piguly >= 5:
                                                    $ kazuma_hp_now = 0
                                                    $ pills -= 1
                                                    play sound "audio/sfx/lyk.mp3"
                                                    queue sound "audio/sfx/spadek.mp3"
                                                    "{i}Kazuma umiera z przedawkowania{/i}"
                                                    hide pills
                                                    jump faza12

                                "{b}Może lepiej już nie{/b}":
                                    hide pills
                                    jump faza12
                    
                "{b}Tutorialowa Woda Święcona (+6HP) x [woda]{/b}" if wodax == 1:
                    hide chest
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show woda zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3

                            if luszcz_hp_now + 6 >= luszcz_hp:
                                $ luszcz_hp_now = luszcz_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał cały pasek życia{/i}"
                            else:
                                $ luszcz_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12
                        
                        "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3

                            if eminem_hp_now + 6 >= eminem_hp:
                                $ eminem_hp_now = eminem_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał cały pasek życia{/i}"
                            else:
                                $ eminem_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12

                        "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3

                            if urban_hp_now + 6 >= urban_hp:
                                $ urban_hp_now = urban_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                            else:
                                $ urban_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12

                        "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3

                            if zyd_hp_now + 6 >= zyd_hp:
                                $ zyd_hp_now = zyd_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał cały pasek życia{/i}"
                            else:
                                $ zyd_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12

                        "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3

                            if kazuma_hp_now + 6 >= kazuma_hp:
                                $ kazuma_hp_now = kazuma_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał cały pasek życia{/i}"
                            else:
                                $ kazuma_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12
                        
                        "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                            if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik1
                            if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik2
                            if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                                show woda zorder 15 at weapon_sojusznik3
                                
                            if tarczownik_hp_now + 6 >= tarczownik_hp:
                                $ tarczownik_hp_now = tarczownik_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał cały pasek życia{/i}"
                            else:
                                $ tarczownik_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał 6 punktów życia{/i}"

                            $ woda -= 1
                            if woda == 0:
                                $ ile_item -= 1
                            hide woda
                            jump faza12
                    
                "{b}Kebab Ostry (+3HP i +1 MAX DMG) x [ostry]{/b}" if ostryx == 1:
                    ""
                    
                "{b}Kebab Łagodny (+4HP i + 1HP FOR 3 TURNS) x [lagodny]{/b}" if lagodnyx == 1:
                    ""
                    
                "{b}Dr Pepper (+2HP i MAX DMG NEXT ATTACK) x [drpepper]{/b}" if drpepperx == 1:
                    ""
                    
                "{b}Jabole (+6HP){/b} x [jabole]" if jabolex == 1:
                    hide chest
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show jabole zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3

                            if luszcz_hp_now + 6 >= luszcz_hp:
                                $ luszcz_hp_now = luszcz_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał cały pasek życia{/i}"
                            else:
                                $ luszcz_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12
                        
                        "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3

                            if eminem_hp_now + 6 >= eminem_hp:
                                $ eminem_hp_now = eminem_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał cały pasek życia{/i}"
                            else:
                                $ eminem_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12

                        "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3

                            if urban_hp_now + 6 >= urban_hp:
                                $ urban_hp_now = urban_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                            else:
                                $ urban_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12

                        "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3

                            if zyd_hp_now + 6 >= zyd_hp:
                                $ zyd_hp_now = zyd_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał cały pasek życia{/i}"
                            else:
                                $ zyd_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12

                        "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3

                            if kazuma_hp_now + 6 >= kazuma_hp:
                                $ kazuma_hp_now = kazuma_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał cały pasek życia{/i}"
                            else:
                                $ kazuma_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12
                        
                        "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                            if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik1
                            if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik2
                            if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                                show jabole zorder 15 at weapon_sojusznik3
                                
                            if tarczownik_hp_now + 6 >= tarczownik_hp:
                                $ tarczownik_hp_now = tarczownik_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał cały pasek życia{/i}"
                            else:
                                $ tarczownik_hp_now += 6
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał 6 punktów życia{/i}"

                            $ jabole -= 1
                            if jabole == 0:
                                $ ile_item -= 1
                            hide jabole
                            jump faza12
                    
                "{b}Royal Cola (+9HP) x [royal]{/b}" if royalx == 1:
                    hide chest
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show royal zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3

                            if luszcz_hp_now + 9 >= luszcz_hp:
                                $ luszcz_hp_now = luszcz_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał cały pasek życia{/i}"
                            else:
                                $ luszcz_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12
                        
                        "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3

                            if eminem_hp_now + 9 >= eminem_hp:
                                $ eminem_hp_now = eminem_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał cały pasek życia{/i}"
                            else:
                                $ eminem_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12

                        "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3

                            if urban_hp_now + 9 >= urban_hp:
                                $ urban_hp_now = urban_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                            else:
                                $ urban_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12

                        "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3

                            if zyd_hp_now + 9 >= zyd_hp:
                                $ zyd_hp_now = zyd_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał cały pasek życia{/i}"
                            else:
                                $ zyd_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12

                        "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3

                            if kazuma_hp_now + 9 >= kazuma_hp:
                                $ kazuma_hp_now = kazuma_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał cały pasek życia{/i}"
                            else:
                                $ kazuma_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12
                        
                        "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                            if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik1
                            if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik2
                            if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                                show royal zorder 15 at weapon_sojusznik3
                                
                            if tarczownik_hp_now + 9 >= tarczownik_hp:
                                $ tarczownik_hp_now = tarczownik_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał cały pasek życia{/i}"
                            else:
                                $ tarczownik_hp_now += 9
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał 9 punktów życia{/i}"

                            $ royal -= 1
                            if royal == 0:
                                $ ile_item -= 1
                            hide royal
                            jump faza12
                    
                "{b}Warzywo skalne (+(4-7)HP) x [warzywo]{/b}" if warzywox == 1:
                    $ kostka = renpy.random.randint(4, 7)
                    hide chest
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show warzywo zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                            if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3

                            if luszcz_hp_now + kostka >= luszcz_hp:
                                $ luszcz_hp_now = luszcz_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał cały pasek życia{/i}"
                            else:
                                $ luszcz_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Łuszcz odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12
                        
                        "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                            if eminem_wybrany == 1 and eminem_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if eminem_wybrany == 2 and eminem_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if eminem_wybrany == 3 and eminem_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3

                            if eminem_hp_now + kostka >= eminem_hp:
                                $ eminem_hp_now = eminem_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał cały pasek życia{/i}"
                            else:
                                $ eminem_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Shadow odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12

                        "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                            if urban_wybrany == 1 and urban_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if urban_wybrany == 2 and urban_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if urban_wybrany == 3 and urban_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3

                            if urban_hp_now + kostka >= urban_hp:
                                $ urban_hp_now = urban_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                            else:
                                $ urban_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Jerzy Urban odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12

                        "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_wybrany == 1 and zyd_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if zyd_wybrany == 2 and zyd_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if zyd_wybrany == 3 and zyd_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3

                            if zyd_hp_now + kostka >= zyd_hp:
                                $ zyd_hp_now = zyd_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał cały pasek życia{/i}"
                            else:
                                $ zyd_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Żyd odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12

                        "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                            if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3

                            if kazuma_hp_now + kostka >= kazuma_hp:
                                $ kazuma_hp_now = kazuma_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał cały pasek życia{/i}"
                            else:
                                $ kazuma_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Kazuma odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12
                        
                        "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                            if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik1
                            if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik2
                            if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                                show warzywo zorder 15 at weapon_sojusznik3
                                
                            if tarczownik_hp_now + kostka >= tarczownik_hp:
                                $ tarczownik_hp_now = tarczownik_hp
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał cały pasek życia{/i}"
                            else:
                                $ tarczownik_hp_now += kostka
                                play sound "audio/sfx/heal.mp3"
                                "{i}Naofumi odzyskał [kostka] punktów życia{/i}"

                            $ warzywo -= 1
                            if warzywo == 0:
                                $ ile_item -= 1
                            hide warzywo
                            jump faza12
                    
                "{b}Kiść bananów (+3HP FOR ALL) x [banany]{/b}" if bananyx == 1:
                    hide chest

                    if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                        show banany1 zorder 15 at weapon_sojusznik1
                    if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                        show banany1 zorder 15 at weapon_sojusznik2
                    if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                        show banany1 zorder 15 at weapon_sojusznik3
                            
                    if eminem_wybrany == 1 and eminem_hp_now > 0:
                        show banany2 zorder 15 at weapon_sojusznik1
                    if eminem_wybrany == 2 and eminem_hp_now > 0:
                        show banany2 zorder 15 at weapon_sojusznik2
                    if eminem_wybrany == 3 and eminem_hp_now > 0:
                        show banany2 zorder 15 at weapon_sojusznik3
                            
                    if urban_wybrany == 1 and urban_hp_now > 0:
                        show banany3 zorder 15 at weapon_sojusznik1
                    if urban_wybrany == 2 and urban_hp_now > 0:
                        show banany3 zorder 15 at weapon_sojusznik2
                    if urban_wybrany == 3 and urban_hp_now > 0:
                        show banany3 zorder 15 at weapon_sojusznik3
                            
                    if zyd_wybrany == 1 and zyd_hp_now > 0:
                        show banany4 zorder 15 at weapon_sojusznik1
                    if zyd_wybrany == 2 and zyd_hp_now > 0:
                        show banany4 zorder 15 at weapon_sojusznik2
                    if zyd_wybrany == 3 and zyd_hp_now > 0:
                        show banany4 zorder 15 at weapon_sojusznik3
                            
                    if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                        show banany5 zorder 15 at weapon_sojusznik1
                    if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                        show banany5 zorder 15 at weapon_sojusznik2
                    if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                        show banany5 zorder 15 at weapon_sojusznik3
                            
                    if tarczownik_wybrany == 1 and tarczownik_hp_now > 0:
                        show banany6 zorder 15 at weapon_sojusznik1
                    if tarczownik_wybrany == 2 and tarczownik_hp_now > 0:
                        show banany6 zorder 15 at weapon_sojusznik2
                    if tarczownik_wybrany == 3 and tarczownik_hp_now > 0:
                        show banany6 zorder 15 at weapon_sojusznik3
                    
                    if luszcz_wybrany > 0:
                        if luszcz_hp_now + 3 >= luszcz_hp:
                            $ luszcz_hp_now = luszcz_hp
                        else:
                            $ luszcz_hp_now += 3
                            
                    if eminem_wybrany > 0:
                        if eminem_hp_now + 3 >= eminem_hp:
                            $ eminem_hp_now = eminem_hp
                        else:
                            $ eminem_hp_now += 3
                            
                    if urban_wybrany > 0:
                        if urban_hp_now + 3 >= urban_hp:
                            $ urban_hp_now = urban_hp
                        else:
                            $ urban_hp_now += 3
                            
                    if zyd_wybrany > 0:
                        if zyd_hp_now + 3 >= zyd_hp:
                            $ zyd_hp_now = zyd_hp
                        else:
                            $ zyd_hp_now += 3
                            
                    if kazuma_wybrany > 0:
                        if kazuma_hp_now + 3 >= kazuma_hp:
                            $ kazuma_hp_now = kazuma_hp
                        else:
                            $ kazuma_hp_now += 3
                    
                    if tarczownik_wybrany > 0:
                        if tarczownik_hp_now + 3 >= tarczownik_hp:
                            $ tarczownik_hp_now = tarczownik_hp
                        else:
                            $ tarczownik_hp_now += 3
                    
                    play sound "audio/sfx/heal.mp3" 
                    "{i}Wszystkie postacie odzyskały po 3 punkty życia{/i}"
                    hide banany1
                    hide banany2
                    hide banany3
                    hide banany4
                    hide banany5
                    hide banany6

                    $ banany -= 1
                    if banany == 0:
                        $ ile_item -= 1
                    jump faza12
                    
                "{b}Ostra Skałka (5-8 DMG){/b} x [skalka]" if skalkax == 1:
                    hide chest
                    $ kostka = renpy.random.randint(5, 8)
                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show skalka zorder 15 at weapon_sojusznik3

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Ostra Skałka została zablokowana{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                show skalka zorder 15 at center_wrog1
                                play sound "audio/sfx/atak.mp3"
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)

                                    "{i}Kibol 1 traci [int(kostka / 2)] punkty życia{/i}"
                                else:
                                    $ kibol1_hp_now -= kostka

                                    "{i}Kibol 1 traci [kostka] punktów życia{/i}"
                            
                            $ skalka -= 1
                            if skalka == 0:
                                $ ile_item -= 1
                            hide skalka
                            jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Ostra Skałka została zablokowana{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                show skalka zorder 15 at center_wrog3
                                play sound "audio/sfx/atak.mp3"
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)

                                    "{i}Akane traci [int(kostka / 2)] punkty życia{/i}"
                                else:
                                    $ akane_hp_now -= kostka

                                    "{i}Akane traci [kostka] punktów życia{/i}"

                            $ skalka -= 1
                            if skalka == 0:
                                $ ile_item -= 1
                            hide skalka
                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Ostra Skałka została zablokowana{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                show skalka zorder 15 at center_wrog2
                                play sound "audio/sfx/atak.mp3"
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)

                                    "{i}Kibol 2 traci [int(kostka / 2)] punkty życia{/i}"
                                else:
                                    $ kibol2_hp_now -= kostka

                                    "{i}Kibol 2 traci [kostka] punktów życia{/i}"

                            $ skalka -= 1
                            if skalka == 0:
                                $ ile_item -= 1
                            hide skalka
                            jump faza12
                    
                "{b}Granat (4 DMG FOR ALL){/b} x [granat]" if granatx == 1:
                    hide chest
                    $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                    if luszcz_fighter == 1:
                        if luszcz_wybrany == 1 and luszcz_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik1
                        if luszcz_wybrany == 2 and luszcz_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik2
                        if luszcz_wybrany == 3 and luszcz_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik3
                                
                    if eminem_fighter == 1:
                        if eminem_wybrany == 1 and eminem_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik1
                        if eminem_wybrany == 2 and eminem_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik2
                        if eminem_wybrany == 3 and eminem_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik3
                                
                    if urban_fighter == 1:
                        if urban_wybrany == 1 and urban_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik1
                        if urban_wybrany == 2 and urban_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik2
                        if urban_wybrany == 3 and urban_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik3
                                
                    if zyd_fighter == 1:
                        if zyd_wybrany == 1 and zyd_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik1
                        if zyd_wybrany == 2 and zyd_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik2
                        if zyd_wybrany == 3 and zyd_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik3
                                    
                    if kazuma_fighter == 1:
                        if kazuma_wybrany == 1 and kazuma_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik1
                        if kazuma_wybrany == 2 and kazuma_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik2
                        if kazuma_wybrany == 3 and kazuma_hp_now > 0:
                            show granat zorder 15 at weapon_sojusznik3

                    if kibol1_hp_now >= 1:
                        if kibol1_obrona >= 2:
                            if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                hide granat
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Granat został zablokowany{/i}"
                            $ kibol1_obrona = 1
                                                                
                        else:     
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= 2
                            else:
                                $ kibol1_hp_now -= 4
                        
                    if akane_hp_now >= 1:
                        if akane_obrona >= 2:
                            if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                hide granat
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Granat został zablokowany{/i}"
                            $ akane_obrona = 1
                                                                
                        else:     
                            if akane_obrona == 1:
                                $ akane_hp_now -= 2
                            else:
                                $ akane_hp_now -= 4

                    if kibol2_hp_now >= 1:
                        if kibol2_obrona >= 2:
                            if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                hide granat
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Granat został zablokowany{/i}"
                            $ kibol2_obrona = 1
                                                                
                        else:     
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= 2
                            else:
                                $ kibol2_hp_now -= 4
                        
                    if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                        show granat zorder 15 at granatz
                        with hpunch
                        show eksplozja1 zorder 15 at granatz
                        play sound "audio/sfx/atak.mp3"
                        "{i}Atak zadał 4 obrażenia wszystkim przeciwniką{/i}"
                        hide eksplozja1
                        
                    else:
                        hide granat
                        play sound "audio/sfx/obrona.mp3"
                        "{i}Granat został zablokowany{/i}"
                        
                    $ granat -= 1
                    if granat == 0:
                        $ ile_item -= 1
                    hide granat
                    jump faza12
                    
                "{i}Strona 1/2 --->{/i}" if strona2 > 0:
                    jump items112