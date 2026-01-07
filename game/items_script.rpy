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
                                        if luszcz_piguly == 4:
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
                                            if luszcz_piguly == 5:
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
                                                if luszcz_piguly >= 6:
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
                                        if eminem_piguly == 4:
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
                                            if eminem_piguly == 5:
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
                                                if eminem_piguly >= 6:
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
                                        if urban_piguly == 4:
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
                                            if urban_piguly == 5:
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
                                                if urban_piguly >= 6:
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
                                        if zyd_piguly == 4:
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
                                            if zyd_piguly == 5:
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
                                                if zyd_piguly >= 6:
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
                                        if kazuma_piguly == 4:
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
                                            if kazuma_piguly == 5:
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
                                                if kazuma_piguly >= 6:
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
                    ""
                    
                "{b}Kebab Ostry (+3HP i +1 MAX DMG) x [ostry]{/b}" if ostryx == 1:
                    ""
                    
                "{b}Kebab Łagodny (+4HP i + 1HP FOR 3 TURNS){/b}" if lagodnyx == 1:
                    ""
                    
                "{b}Dr Pepper (+2HP i MAX DMG NEXT ATTACK){/b}" if drpepperx == 1:
                    ""
                    
                "{b}Jabole (+6HP){/b}" if jabolex == 1:
                    ""
                    
                "{b}Royal Cola (+9HP){/b}" if royalx == 1:
                    ""
                    
                "{b}Warzywo skalne (+(4-7)HP){/b}" if warzywox == 1:
                    ""
                    
                "{b}Kiść bananów (+3HP FOR ALL){/b}" if bananyx == 1:
                    ""
                    
                "{b}Ostra Skałka (5-8 DMG){/b}" if skalkax == 1:
                    ""
                    
                "{b}Granat (4 DMG FOR ALL){/b}" if granatx == 1:
                    ""
                    
                "{i}Strona 1/2 --->{/i}" if strona2 > 0:
                    jump items112