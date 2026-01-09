label fight1_stats:
    default kibol1_sex = 0
    default kibol2_sex = 0
    default akane_sex = 1

    default kibol1_hp = 15
    default kibol2_hp = 15
    default akane_hp = 30

    default kibol1_uszy = 0
    default akane_uszy = 0
    default kibol2_uszy = 0

    default kibol1_pager = 0
    default kibol2_pager = 0
    default akane_pager = 0

    default kibol1_slime = 0
    default kibol2_slime = 0
    default akane_slime = 0

    default kibol1_weapon = 1
    default kibol2_weapon = 1
    default akane_weapon = 1

    default kibol1_hp_now = kibol1_hp
    default kibol2_hp_now = kibol2_hp
    default akane_hp_now = akane_hp

    default kibol1_min_attack = 1
    default kibol2_min_attack = 1
    default akane_min_attack = 3

    default kibol1_max_attack = 4
    default kibol2_max_attack = 4
    default akane_max_attack = 8

    default kibol1_max_attack_now = kibol1_max_attack
    default kibol2_max_attack_now = kibol2_max_attack
    default akane_max_attack_now = akane_max_attack

    default kibol1_min_attack_now = kibol1_min_attack
    default kibol2_min_attack_now = kibol2_min_attack
    default akane_min_attack_now = akane_min_attack

    default kibol1_max_attack_now_true = kibol1_max_attack
    default kibol2_max_attack_now_true = kibol2_max_attack
    default akane_max_attack_now_true = akane_max_attack

    default kibol1_min_attack_now_true = kibol1_min_attack
    default kibol2_min_attack_now_true = kibol2_min_attack
    default akane_min_attack_now_true = akane_min_attack

    default kibol1_attack = 0
    default kibol2_attack = 0
    default akane_attack = 0

    default kibol1_obrona = 0
    default kibol2_obrona = 0
    default akane_obrona = 0

    default kibol1_umarty = 0
    default kibol2_umarty = 0
    default akane_umarty = 0

    default kibol1_poison = 0
    default kibol2_poison = 0
    default akane_poison = 0

    default kibol1_stun = 0
    default kibol2_stun = 0
    default akane_stun = 0

label fight1:
    label fight_wybor1:
        play music "audio/music/fight.mp3"
        scene bg korytarz
        $ ile_wrogow += 3
        show kibol1 fight zorder 10 at wrog1
        show screen kibol1_stats
        show akane fight zorder 10 at wrog3
        show screen akane_stats
        show kibol2 fight zorder 10 at wrog2
        show screen kibol2_stats
        $ kibol1_hp_now = kibol1_hp
        $ kibol1_min_attack_now = kibol1_min_attack
        $ kibol1_max_attack_now = kibol1_max_attack
        $ kibol1_min_attack_now_true = kibol1_min_attack
        $ kibol1_max_attack_now_true = kibol1_max_attack
        $ kibol2_hp_now = kibol2_hp
        $ kibol2_min_attack_now = kibol2_min_attack
        $ kibol2_max_attack_now = kibol2_max_attack
        $ kibol2_min_attack_now_true = kibol2_min_attack
        $ kibol2_max_attack_now_true = kibol2_max_attack
        $ akane_hp_now = akane_hp
        $ akane_min_attack_now = akane_min_attack
        $ akane_max_attack_now = akane_max_attack
        $ akane_min_attack_now_true = akane_min_attack
        $ akane_max_attack_now_true = akane_max_attack

        label team1:
            $ fight_on = 1
            if liczba_sojusznikow >= 3:
                $ ile_sojusznikow += 3
                menu:
                    "{b}Kogo wystawić do walki?{/b}"

                    "{b}Maciej Łuszcz (HP:[luszcz_hp], ATK:[luszcz_min_attack]-[luszcz_max_attack]){/b}" if luszcz_sojusznik >= 1 and luszcz_wybrany == 0:
                        $ luszcz_wybrany += 1
                        $ luszcz_fighter += 1
                        $ luszcz_hp_now = luszcz_hp
                        $ luszcz_min_attack_now = luszcz_min_attack
                        $ luszcz_max_attack_now = luszcz_max_attack
                        $ luszcz_min_attack_now_true = luszcz_min_attack
                        $ luszcz_max_attack_now_true = luszcz_max_attack

                        if luszcz_klata == 2:
                            show luszcz_klata zorder 11 at sojusznik1
                        if ring == 2:
                            show luszcz_ring zorder 11 at sojusznik1
                        if zloty == 2:
                            show luszcz_zloty zorder 11 at sojusznik1
                            $ luszcz_zloty_czlowiek = 1
                        if memy == 2:
                            show luszcz_memy zorder 11 at sojusznik1
                        if vr == 2:
                            show luszcz_vr zorder 11 at sojusznik1
                        if ziemia == 2:
                            show luszcz_ziemia zorder 11 at sojusznik1
                        if nogi == 2:
                            show luszcz_nogi zorder 11 at sojusznik1

                        show luszcz fight zorder 10 at sojusznik1
                        show screen luszcz1_stats
                        luszcz "Gotowy do boju"
                    
                    "{b}Shadow (HP:[eminem_hp], ATK:[eminem_min_attack]-[eminem_max_attack]){/b}" if eminem_sojusznik >= 1 and eminem_wybrany == 0:
                        $ eminem_wybrany += 1
                        $ eminem_fighter += 1
                        $ eminem_hp_now = eminem_hp
                        $ eminem_min_attack_now = eminem_min_attack
                        $ eminem_max_attack_now = eminem_max_attack
                        $ eminem_min_attack_now_true = eminem_min_attack
                        $ eminem_max_attack_now_true = eminem_max_attack

                        if eminem_klata == 7:
                            show eminem_klata zorder 11 at sojusznik1
                        if ring == 7:
                            show eminem_ring zorder 11 at sojusznik1
                        if zloty == 7:
                            show eminem_zloty zorder 11 at sojusznik1
                            $ eminem_zloty_czlowiek = 1
                        if memy == 7:
                            show eminem_memy zorder 11 at sojusznik1
                        if vr == 7:
                            show eminem_vr zorder 11 at sojusznik1
                        if ziemia == 7:
                            show eminem_ziemia zorder 11 at sojusznik1
                        if nogi == 7:
                            show eminem_nogi zorder 11 at sojusznik1

                        show eminem fight zorder 10 at sojusznik1
                        show screen eminem1_stats
                        eminem "Gotowy do boju"

                    "{b}Jerzy Urban (HP:[urban_hp], ATK:[urban_min_attack]-[urban_max_attack]){/b}" if urban_sojusznik >= 1 and urban_wybrany == 0:
                        $ urban_wybrany += 1
                        $ urban_fighter += 1
                        $ urban_hp_now = urban_hp
                        $ urban_min_attack_now = urban_min_attack
                        $ urban_max_attack_now = urban_max_attack
                        $ urban_min_attack_now_true = urban_min_attack
                        $ urban_max_attack_now_true = urban_max_attack

                        if urban_klata == 3:
                            show urban_klata zorder 11 at sojusznik1
                        if ring == 3:
                            show urban_ring zorder 11 at sojusznik1
                        if zloty == 3:
                            show urban_zloty zorder 11 at sojusznik1
                            $ urban_zloty_czlowiek = 1
                        if memy == 3:
                            show urban_memy zorder 11 at sojusznik1
                        if vr == 3:
                            show urban_vr zorder 11 at sojusznik1
                        if ziemia == 3:
                            show urban_ziemia zorder 11 at sojusznik1
                        if nogi == 3:
                            show urban_nogi zorder 11 at sojusznik1

                        show urban fight zorder 10 at sojusznik1
                        show screen urban1_stats
                        urban "Gotowy do boju"

                    "{b}Żyd (HP:[zyd_hp], ATK:[zyd_min_attack]-[zyd_max_attack]){/b}" if zyd_sojusznik >= 1 and zyd_wybrany == 0:
                        $ zyd_wybrany += 1
                        $ zyd_fighter += 1
                        $ zyd_hp_now = zyd_hp
                        $ zyd_min_attack_now = zyd_min_attack
                        $ zyd_max_attack_now = zyd_max_attack
                        $ zyd_min_attack_now_true = zyd_min_attack
                        $ zyd_max_attack_now_true = zyd_max_attack

                        if zyd_klata == 4:
                            show zyd_klata zorder 11 at sojusznik1
                        if ring == 4:
                            show zyd_ring zorder 11 at sojusznik1
                        if zloty == 4:
                            show zyd_zloty zorder 11 at sojusznik1
                            $ zyd_zloty_czlowiek = 1
                        if memy == 4:
                            show zyd_memy zorder 11 at sojusznik1
                        if vr == 4:
                            show zyd_vr zorder 11 at sojusznik1
                        if ziemia == 4:
                            show zyd_ziemia zorder 11 at sojusznik1
                        if nogi == 4:
                            show zyd_nogi zorder 11 at sojusznik1

                        show zyd fight zorder 10 at sojusznik1
                        show screen zyd1_stats
                        zyd "Gotowy do boju"

                    "{b}Kazuma (HP:[kazuma_hp], ATK:[kazuma_min_attack]-[kazuma_max_attack]){/b}" if kazuma_sojusznik >= 1 and kazuma_wybrany == 0:
                        $ kazuma_wybrany += 1
                        $ kazuma_fighter += 1
                        $ kazuma_hp_now = kazuma_hp
                        $ kazuma_min_attack_now = kazuma_min_attack
                        $ kazuma_max_attack_now = kazuma_max_attack
                        $ kazuma_min_attack_now_true = kazuma_min_attack
                        $ kazuma_max_attack_now_true = kazuma_max_attack

                        if kazuma_klata == 5:
                            show kazuma_klata zorder 11 at sojusznik1
                        if ring == 5:
                            show kazuma_ring zorder 11 at sojusznik1
                        if zloty == 5:
                            show kazuma_zloty zorder 11 at sojusznik1
                            $ kazuma_zloty_czlowiek = 1
                        if memy == 5:
                            show kazuma_memy zorder 11 at sojusznik1
                        if vr == 5:
                            show kazuma_vr zorder 11 at sojusznik1
                        if ziemia == 5:
                            show kazuma_ziemia zorder 11 at sojusznik1
                        if nogi == 5:
                            show kazuma_nogi zorder 11 at sojusznik1

                        show kazuma fight zorder 10 at sojusznik1
                        show screen kazuma1_stats
                        kazuma "Gotowy do boju"
                    
                    "{b}Naofumi (HP:[tarczownik_hp], ATK:[tarczownik_min_attack]-[tarczownik_max_attack]){/b}" if tarczownik_sojusznik >= 1 and tarczownik_wybrany == 0:
                        $ tarczownik_wybrany += 1
                        $ tarczownik_fighter += 1
                        $ tarczownik_hp_now = tarczownik_hp
                        $ tarczownik_min_attack_now = tarczownik_min_attack
                        $ tarczownik_max_attack_now = tarczownik_max_attack
                        $ tarczownik_min_attack_now_true = tarczownik_min_attack
                        $ tarczownik_max_attack_now_true = tarczownik_max_attack

                        if tarczownik_klata == 6:
                            show tarczownik_klata zorder 11 at sojusznik1
                        if ring == 6:
                            show tarczownik_ring zorder 11 at sojusznik1
                        if zloty == 6:
                            show tarczownik_zloty zorder 11 at sojusznik1
                            $ tarczownik_zloty_czlowiek = 1
                        if memy == 6:
                            show tarczownik_memy zorder 11 at sojusznik1
                        if vr == 6:
                            show tarczownik_vr zorder 11 at sojusznik1
                        if ziemia == 6:
                            show tarczownik_ziemia zorder 11 at sojusznik1
                        if nogi == 6:
                            show tarczownik_nogi zorder 11 at sojusznik1

                        show tarczownik fight zorder 10 at sojusznik1
                        show screen tarczownik1_stats
                        tarczownik "Gotowy do boju"

                menu:
                    "{b}Kogo wystawić do walki?{/b}"

                    "{b}Maciej Łuszcz (HP:[luszcz_hp], ATK:[luszcz_min_attack]-[luszcz_max_attack]){/b}" if luszcz_sojusznik >= 1 and luszcz_wybrany == 0:
                        $ luszcz_wybrany += 3
                        $ luszcz_fighter += 2
                        $ luszcz_hp_now = luszcz_hp
                        $ luszcz_min_attack_now = luszcz_min_attack
                        $ luszcz_max_attack_now = luszcz_max_attack
                        $ luszcz_min_attack_now_true = luszcz_min_attack
                        $ luszcz_max_attack_now_true = luszcz_max_attack

                        if luszcz_klata == 2:
                            show luszcz_klata zorder 11 at sojusznik3
                        if ring == 2:
                            show luszcz_ring zorder 11 at sojusznik3
                        if zloty == 2:
                            show luszcz_zloty zorder 11 at sojusznik3
                            $ luszcz_zloty_czlowiek = 1
                        if memy == 2:
                            show luszcz_memy zorder 11 at sojusznik3
                        if vr == 2:
                            show luszcz_vr zorder 11 at sojusznik3
                        if ziemia == 2:
                            show luszcz_ziemia zorder 11 at sojusznik3
                        if nogi == 2:
                            show luszcz_nogi zorder 11 at sojusznik3

                        show luszcz fight zorder 10 at sojusznik3
                        show screen luszcz3_stats
                        luszcz "Gotowy do boju"
                    
                    "{b}Shadow (HP:[eminem_hp], ATK:[eminem_min_attack]-[eminem_max_attack]){/b}" if eminem_sojusznik >= 1 and eminem_wybrany == 0:
                        $ eminem_wybrany += 3
                        $ eminem_fighter += 2
                        $ eminem_hp_now = eminem_hp
                        $ eminem_min_attack_now = eminem_min_attack
                        $ eminem_max_attack_now = eminem_max_attack
                        $ eminem_min_attack_now_true = eminem_min_attack
                        $ eminem_max_attack_now_true = eminem_max_attack

                        if eminem_klata == 7:
                            show eminem_klata zorder 11 at sojusznik3
                        if ring == 7:
                            show eminem_ring zorder 11 at sojusznik3
                        if zloty == 7:
                            show eminem_zloty zorder 11 at sojusznik3
                            $ eminem_zloty_czlowiek = 1
                        if memy == 7:
                            show eminem_memy zorder 11 at sojusznik3
                        if vr == 7:
                            show eminem_vr zorder 11 at sojusznik3
                        if ziemia == 7:
                            show eminem_ziemia zorder 11 at sojusznik3
                        if nogi == 7:
                            show eminem_nogi zorder 11 at sojusznik3

                        show eminem fight zorder 10 at sojusznik3
                        show screen eminem3_stats
                        eminem "Gotowy do boju"

                    "{b}Jerzy Urban (HP:[urban_hp], ATK:[urban_min_attack]-[urban_max_attack]){/b}" if urban_sojusznik >= 1 and urban_wybrany == 0:
                        $ urban_wybrany += 3
                        $ urban_fighter += 2
                        $ urban_hp_now = urban_hp
                        $ urban_min_attack_now = urban_min_attack
                        $ urban_max_attack_now = urban_max_attack
                        $ urban_min_attack_now_true = urban_min_attack
                        $ urban_max_attack_now_true = urban_max_attack

                        if urban_klata == 3:
                            show urban_klata zorder 11 at sojusznik3
                        if ring == 3:
                            show urban_ring zorder 11 at sojusznik3
                        if zloty == 3:
                            show urban_zloty zorder 11 at sojusznik3
                            $ urban_zloty_czlowiek = 1
                        if memy == 3:
                            show urban_memy zorder 11 at sojusznik3
                        if vr == 3:
                            show urban_vr zorder 11 at sojusznik3
                        if ziemia == 3:
                            show urban_ziemia zorder 11 at sojusznik3
                        if nogi == 3:
                            show urban_nogi zorder 11 at sojusznik3

                        show urban fight zorder 10 at sojusznik3
                        show screen urban3_stats
                        urban "Gotowy do boju"

                    "{b}Żyd (HP:[zyd_hp], ATK:[zyd_min_attack]-[zyd_max_attack]){/b}" if zyd_sojusznik >= 1 and zyd_wybrany == 0:
                        $ zyd_wybrany += 3
                        $ zyd_fighter += 2
                        $ zyd_hp_now = zyd_hp
                        $ zyd_min_attack_now = zyd_min_attack
                        $ zyd_max_attack_now = zyd_max_attack
                        $ zyd_min_attack_now_true = zyd_min_attack
                        $ zyd_max_attack_now_true = zyd_max_attack

                        if zyd_klata == 4:
                            show zyd_klata zorder 11 at sojusznik3
                        if ring == 4:
                            show zyd_ring zorder 11 at sojusznik3
                        if zloty == 4:
                            show zyd_zloty zorder 11 at sojusznik3
                            $ zyd_zloty_czlowiek = 1
                        if memy == 4:
                            show zyd_memy zorder 11 at sojusznik3
                        if vr == 4:
                            show zyd_vr zorder 11 at sojusznik3
                        if ziemia == 4:
                            show zyd_ziemia zorder 11 at sojusznik3
                        if nogi == 4:
                            show zyd_nogi zorder 11 at sojusznik3

                        show zyd fight zorder 10 at sojusznik3
                        show screen zyd3_stats
                        zyd "Gotowy do boju"

                    "{b}Kazuma (HP:[kazuma_hp], ATK:[kazuma_min_attack]-[kazuma_max_attack]){/b}" if kazuma_sojusznik >= 1 and kazuma_wybrany == 0:
                        $ kazuma_wybrany += 3
                        $ kazuma_fighter += 2
                        $ kazuma_hp_now = kazuma_hp
                        $ kazuma_min_attack_now = kazuma_min_attack
                        $ kazuma_max_attack_now = kazuma_max_attack
                        $ kazuma_min_attack_now_true = kazuma_min_attack
                        $ kazuma_max_attack_now_true = kazuma_max_attack

                        if kazuma_klata == 5:
                            show kazuma_klata zorder 11 at sojusznik3
                        if ring == 5:
                            show kazuma_ring zorder 11 at sojusznik3
                        if zloty == 5:
                            show kazuma_zloty zorder 11 at sojusznik3
                            $ kazuma_zloty_czlowiek = 1
                        if memy == 5:
                            show kazuma_memy zorder 11 at sojusznik3
                        if vr == 5:
                            show kazuma_vr zorder 11 at sojusznik3
                        if ziemia == 5:
                            show kazuma_ziemia zorder 11 at sojusznik3
                        if nogi == 5:
                            show kazuma_nogi zorder 11 at sojusznik3

                        show kazuma fight zorder 10 at sojusznik3
                        show screen kazuma3_stats
                        kazuma "Gotowy do boju"
                    
                    "{b}Naofumi (HP:[tarczownik_hp], ATK:[tarczownik_min_attack]-[tarczownik_max_attack]){/b}" if tarczownik_sojusznik >= 1 and tarczownik_wybrany == 0:
                        $ tarczownik_wybrany += 3
                        $ tarczownik_fighter += 1
    
                        if luszcz_fighter == 1:
                            $ luszcz_fighter += 1

                        if eminem_fighter == 1:
                            $ eminem_fighter += 1

                        if urban_fighter == 1:
                            $ urban_fighter += 1

                        if zyd_fighter == 1:
                            $ zyd_fighter += 1

                        if kazuma_fighter == 1:
                            $ kazuma_fighter += 1

                        $ tarczownik_hp_now = tarczownik_hp
                        $ tarczownik_min_attack_now = tarczownik_min_attack
                        $ tarczownik_max_attack_now = tarczownik_max_attack
                        $ tarczownik_min_attack_now_true = tarczownik_min_attack
                        $ tarczownik_max_attack_now_true = tarczownik_max_attack

                        if tarczownik_klata == 6:
                            show tarczownik_klata zorder 11 at sojusznik3
                        if ring == 6:
                            show tarczownik_ring zorder 11 at sojusznik3
                        if zloty == 6:
                            show tarczownik_zloty zorder 11 at sojusznik3
                            $ tarczownik_zloty_czlowiek = 1
                        if memy == 6:
                            show tarczownik_memy zorder 11 at sojusznik3
                        if vr == 6:
                            show tarczownik_vr zorder 11 at sojusznik3
                        if ziemia == 6:
                            show tarczownik_ziemia zorder 11 at sojusznik3
                        if nogi == 6:
                            show tarczownik_nogi zorder 11 at sojusznik3

                        show tarczownik fight zorder 10 at sojusznik3
                        show screen tarczownik3_stats
                        tarczownik "Gotowy do boju"

                menu:
                    "{b}Kogo wystawić do walki?{/b}"

                    "{b}Maciej Łuszcz (HP:[luszcz_hp], ATK:[luszcz_min_attack]-[luszcz_max_attack]){/b}" if luszcz_sojusznik >= 1 and luszcz_wybrany == 0:
                        $ luszcz_wybrany += 2
                        $ luszcz_fighter += 3
                        $ luszcz_hp_now = luszcz_hp
                        $ luszcz_min_attack_now = luszcz_min_attack
                        $ luszcz_max_attack_now = luszcz_max_attack
                        $ luszcz_min_attack_now_true = luszcz_min_attack
                        $ luszcz_max_attack_now_true = luszcz_max_attack
                        if luszcz_klata == 2:
                            show luszcz_klata zorder 11 at sojusznik2
                        if ring == 2:
                            show luszcz_ring zorder 11 at sojusznik2
                        if zloty == 2:
                            show luszcz_zloty zorder 11 at sojusznik2
                            $ luszcz_zloty_czlowiek = 1
                        if memy == 2:
                            show luszcz_memy zorder 11 at sojusznik2
                        if vr == 2:
                            show luszcz_vr zorder 11 at sojusznik2
                        if ziemia == 2:
                            show luszcz_ziemia zorder 11 at sojusznik2
                        if nogi == 2:
                            show luszcz_nogi zorder 11 at sojusznik2

                        show luszcz fight zorder 10 at sojusznik2
                        show screen luszcz2_stats
                        luszcz "Gotowy do boju"

                    "{b}Shadow (HP:[eminem_hp], ATK:[eminem_min_attack]-[eminem_max_attack]){/b}" if eminem_sojusznik >= 1 and eminem_wybrany == 0:
                        $ eminem_wybrany += 2
                        $ eminem_fighter += 3
                        $ eminem_hp_now = eminem_hp
                        $ eminem_min_attack_now = eminem_min_attack
                        $ eminem_max_attack_now = eminem_max_attack
                        $ eminem_min_attack_now_true = eminem_min_attack
                        $ eminem_max_attack_now_true = eminem_max_attack

                        if eminem_klata == 7:
                            show eminem_klata zorder 11 at sojusznik2
                        if ring == 7:
                            show eminem_ring zorder 11 at sojusznik2
                        if zloty == 7:
                            show eminem_zloty zorder 11 at sojusznik2
                            $ eminem_zloty_czlowiek = 1
                        if memy == 7:
                            show eminem_memy zorder 11 at sojusznik2
                        if vr == 7:
                            show eminem_vr zorder 11 at sojusznik2
                        if ziemia == 7:
                            show eminem_ziemia zorder 11 at sojusznik2
                        if nogi == 7:
                            show eminem_nogi zorder 11 at sojusznik2

                        show eminem fight zorder 10 at sojusznik2
                        show screen eminem2_stats
                        eminem "Gotowy do boju"

                    "{b}Jerzy Urban (HP:[urban_hp], ATK:[urban_min_attack]-[urban_max_attack]){/b}" if urban_sojusznik >= 1 and urban_wybrany == 0:
                        $ urban_wybrany += 2
                        $ urban_fighter += 3
                        $ urban_hp_now = urban_hp
                        $ urban_min_attack_now = urban_min_attack
                        $ urban_max_attack_now = urban_max_attack
                        $ urban_min_attack_now_true = urban_min_attack
                        $ urban_max_attack_now_true = urban_max_attack

                        if urban_klata == 3:
                            show urban_klata zorder 11 at sojusznik2
                        if ring == 3:
                            show urban_ring zorder 11 at sojusznik2
                        if zloty == 3:
                            show urban_zloty zorder 11 at sojusznik2
                            $ urban_zloty_czlowiek = 1
                        if memy == 3:
                            show urban_memy zorder 11 at sojusznik2
                        if vr == 3:
                            show urban_vr zorder 11 at sojusznik2
                        if ziemia == 3:
                            show urban_ziemia zorder 11 at sojusznik2
                        if nogi == 3:
                            show urban_nogi zorder 11 at sojusznik2

                        show urban fight zorder 10 at sojusznik2
                        show screen urban2_stats
                        urban "Gotowy do boju"

                    "{b}Żyd (HP:[zyd_hp], ATK:[zyd_min_attack]-[zyd_max_attack]){/b}" if zyd_sojusznik >= 1 and zyd_wybrany == 0:
                        $ zyd_wybrany += 2
                        $ zyd_fighter += 3
                        $ zyd_hp_now = zyd_hp
                        $ zyd_min_attack_now = zyd_min_attack
                        $ zyd_max_attack_now = zyd_max_attack
                        $ zyd_min_attack_now_true = zyd_min_attack
                        $ zyd_max_attack_now_true = zyd_max_attack

                        if zyd_klata == 4:
                            show zyd_klata zorder 11 at sojusznik2
                        if ring == 4:
                            show zyd_ring zorder 11 at sojusznik2
                        if zloty == 4:
                            show zyd_zloty zorder 11 at sojusznik2
                            $ zyd_zloty_czlowiek = 1
                        if memy == 4:
                            show zyd_memy zorder 11 at sojusznik2
                        if vr == 4:
                            show zyd_vr zorder 11 at sojusznik2
                        if ziemia == 4:
                            show zyd_ziemia zorder 11 at sojusznik2
                        if nogi == 4:
                            show zyd_nogi zorder 11 at sojusznik2

                        show zyd fight zorder 10 at sojusznik2
                        show screen zyd2_stats
                        zyd "Gotowy do boju"

                    "{b}Kazuma (HP:[kazuma_hp], ATK:[kazuma_min_attack]-[kazuma_max_attack]){/b}" if kazuma_sojusznik >= 1 and kazuma_wybrany == 0:
                        $ kazuma_wybrany += 2
                        $ kazuma_fighter += 3
                        $ kazuma_hp_now = kazuma_hp
                        $ kazuma_min_attack_now = kazuma_min_attack
                        $ kazuma_max_attack_now = kazuma_max_attack
                        $ kazuma_min_attack_now_true = kazuma_min_attack
                        $ kazuma_max_attack_now_true = kazuma_max_attack

                        if kazuma_klata == 5:
                            show kazuma_klata zorder 11 at sojusznik2
                        if ring == 5:
                            show kazuma_ring zorder 11 at sojusznik2
                        if zloty == 5:
                            show kazuma_zloty zorder 11 at sojusznik2
                            $ kazuma_zloty_czlowiek = 1
                        if memy == 5:
                            show kazuma_memy zorder 11 at sojusznik2
                        if vr == 5:
                            show kazuma_vr zorder 11 at sojusznik2
                        if ziemia == 5:
                            show kazuma_ziemia zorder 11 at sojusznik2
                        if nogi == 5:
                            show kazuma_nogi zorder 11 at sojusznik2

                        show kazuma fight zorder 10 at sojusznik2
                        show screen kazuma2_stats
                        kazuma "Gotowy do boju"
                    
                    "{b}Naofumi (HP:[tarczownik_hp], ATK:[tarczownik_min_attack]-[tarczownik_max_attack]){/b}" if tarczownik_sojusznik >= 1 and tarczownik_wybrany == 0:
                        $ tarczownik_wybrany += 2
                        $ tarczownik_fighter += 1
    
                        if luszcz_fighter == 1:
                            $ luszcz_fighter += 1
                        else:
                            if luszcz_fighter == 2:
                                $ luszcz_fighter += 1

                        if eminem_fighter == 1:
                            $ eminem_fighter += 1
                        else:
                            if eminem_fighter == 2:
                                $ eminem_fighter += 1

                        if urban_fighter == 1:
                            $ urban_fighter += 1
                        else:
                            if urban_fighter == 2:
                                $ urban_fighter += 1

                        if zyd_fighter == 1:
                            $ zyd_fighter += 1
                        else:
                            if zyd_fighter == 2:
                                $ zyd_fighter += 1

                        if kazuma_fighter == 1:
                            $ kazuma_fighter += 1
                        else:
                            if kazuma_fighter == 2:
                                $ kazuma_fighter += 1

                        $ tarczownik_hp_now = tarczownik_hp
                        $ tarczownik_min_attack_now = tarczownik_min_attack
                        $ tarczownik_max_attack_now = tarczownik_max_attack
                        $ tarczownik_min_attack_now_true = tarczownik_min_attack
                        $ tarczownik_max_attack_now_true = tarczownik_max_attack

                        if tarczownik_klata == 6:
                            show tarczownik_klata zorder 11 at sojusznik2
                        if ring == 6:
                            show tarczownik_ring zorder 11 at sojusznik2
                        if zloty == 6:
                            show tarczownik_zloty zorder 11 at sojusznik2
                            $ tarczownik_zloty_czlowiek = 1
                        if memy == 6:
                            show tarczownik_memy zorder 11 at sojusznik2
                        if vr == 6:
                            show tarczownik_vr zorder 11 at sojusznik2
                        if ziemia == 6:
                            show tarczownik_ziemia zorder 11 at sojusznik2
                        if nogi == 6:
                            show tarczownik_nogi zorder 11 at sojusznik2

                        show tarczownik fight zorder 10 at sojusznik2
                        show screen tarczownik2_stats
                        tarczownik "Gotowy do boju"

                jump start_fight1
                
            else:
                if liczba_sojusznikow == 2:
                    $ ile_sojusznikow += 2
                    menu:
                        "{b}Kogo wystawić do walki?{/b}"

                        "{b}Maciej Łuszcz (HP:[luszcz_hp], ATK:[luszcz_min_attack]-[luszcz_max_attack]){/b}" if luszcz_sojusznik >= 1 and luszcz_wybrany == 0:
                            $ luszcz_wybrany += 1
                            $ luszcz_fighter += 1
                            $ luszcz_hp_now = luszcz_hp
                            $ luszcz_min_attack_now = luszcz_min_attack
                            $ luszcz_max_attack_now = luszcz_max_attack
                            $ luszcz_min_attack_now_true = luszcz_min_attack
                            $ luszcz_max_attack_now_true = luszcz_max_attack
                            show screen luszcz1_stats

                            if luszcz_klata == 2:
                                show luszcz_klata zorder 11 at sojusznik1
                            if ring == 2:
                                show luszcz_ring zorder 11 at sojusznik1
                            if zloty == 2:
                                show luszcz_zloty zorder 11 at sojusznik1
                                $ luszcz_zloty_czlowiek = 1
                            if memy == 2:
                                show luszcz_memy zorder 11 at sojusznik1
                            if vr == 2:
                                show luszcz_vr zorder 11 at sojusznik1
                            if ziemia == 2:
                                show luszcz_ziemia zorder 11 at sojusznik1
                            if nogi == 2:
                                show luszcz_nogi zorder 11 at sojusznik1
                                
                            show luszcz fight zorder 10 at sojusznik1
                            luszcz "Gotowy do boju"

                        "{b}Shadow (HP:[eminem_hp], ATK:[eminem_min_attack]-[eminem_max_attack]){/b}" if eminem_sojusznik >= 1 and eminem_wybrany == 0:
                            $ eminem_wybrany += 1
                            $ eminem_fighter += 1
                            $ eminem_hp_now = eminem_hp
                            $ eminem_min_attack_now = eminem_min_attack
                            $ eminem_max_attack_now = eminem_max_attack
                            $ eminem_min_attack_now_true = eminem_min_attack
                            $ eminem_max_attack_now_true = eminem_max_attack

                            if eminem_klata == 7:
                                show eminem_klata zorder 11 at sojusznik1
                            if ring == 7:
                                show eminem_ring zorder 11 at sojusznik1
                            if zloty == 7:
                                show eminem_zloty zorder 11 at sojusznik1
                                $ eminem_zloty_czlowiek = 1
                            if memy == 7:
                                show eminem_memy zorder 11 at sojusznik1
                            if vr == 7:
                                show eminem_vr zorder 11 at sojusznik1
                            if ziemia == 7:
                                show eminem_ziemia zorder 11 at sojusznik1
                            if nogi == 7:
                                show eminem_nogi zorder 11 at sojusznik1

                            show eminem fight zorder 10 at sojusznik1
                            show screen eminem1_stats
                            eminem "Gotowy do boju"

                        "{b}Jerzy Urban (HP:[urban_hp], ATK:[urban_min_attack]-[urban_max_attack]){/b}" if urban_sojusznik >= 1 and urban_wybrany == 0:
                            $ urban_wybrany += 1
                            $ urban_fighter += 1
                            $ urban_hp_now = urban_hp
                            $ urban_min_attack_now = urban_min_attack
                            $ urban_max_attack_now = urban_max_attack
                            $ urban_min_attack_now_true = urban_min_attack
                            $ urban_max_attack_now_true = urban_max_attack
                            show screen urban1_stats

                            if urban_klata == 3:
                                show urban_klata zorder 11 at sojusznik1
                            if ring == 3:
                                show urban_ring zorder 11 at sojusznik1
                            if zloty == 3:
                                show urban_zloty zorder 11 at sojusznik1
                                $ urban_zloty_czlowiek = 1
                            if memy == 3:
                                show urban_memy zorder 11 at sojusznik1
                            if vr == 3:
                                show urban_vr zorder 11 at sojusznik1
                            if ziemia == 3:
                                show urban_ziemia zorder 11 at sojusznik1
                            if nogi == 3:
                                show urban_nogi zorder 11 at sojusznik1

                            show urban fight zorder 10 at sojusznik1
                            urban "Gotowy do boju"

                        "{b}Żyd (HP:[zyd_hp], ATK:[zyd_min_attack]-[zyd_max_attack]){/b}" if zyd_sojusznik >= 1 and zyd_wybrany == 0:
                            $ zyd_wybrany += 1
                            $ zyd_fighter += 1
                            $ zyd_hp_now = zyd_hp
                            $ zyd_min_attack_now = zyd_min_attack
                            $ zyd_max_attack_now = zyd_max_attack
                            $ zyd_min_attack_now_true = zyd_min_attack
                            $ zyd_max_attack_now_true = zyd_max_attack

                            if zyd_klata == 4:
                                show zyd_klata zorder 11 at sojusznik1
                            if ring == 4:
                                show zyd_ring zorder 11 at sojusznik1
                            if zloty == 4:
                                show zyd_zloty zorder 11 at sojusznik1
                                $ zyd_zloty_czlowiek = 1
                            if memy == 4:
                                show zyd_memy zorder 11 at sojusznik1
                            if vr == 4:
                                show zyd_vr zorder 11 at sojusznik1
                            if ziemia == 4:
                                show zyd_ziemia zorder 11 at sojusznik1
                            if nogi == 4:
                                show zyd_nogi zorder 11 at sojusznik1

                            show screen zyd1_stats
                            show zyd fight zorder 10 at sojusznik1
                            zyd "Gotowy do boju"

                        "{b}Kazuma (HP:[kazuma_hp], ATK:[kazuma_min_attack]-[kazuma_max_attack]){/b}" if kazuma_sojusznik >= 1 and kazuma_wybrany == 0:
                            $ kazuma_wybrany += 1
                            $ kazuma_fighter += 1
                            $ kazuma_hp_now = kazuma_hp
                            $ kazuma_min_attack_now = kazuma_min_attack
                            $ kazuma_max_attack_now = kazuma_max_attack
                            $ kazuma_min_attack_now_true = kazuma_min_attack
                            $ kazuma_max_attack_now_true = kazuma_max_attack

                            if kazuma_klata == 5:
                                show kazuma_klata zorder 11 at sojusznik1
                            if ring == 5:
                                show kazuma_ring zorder 11 at sojusznik1
                            if zloty == 5:
                                show kazuma_zloty zorder 11 at sojusznik1
                                $ kazuma_zloty_czlowiek = 1
                            if memy == 5:
                                show kazuma_memy zorder 11 at sojusznik1
                            if vr == 5:
                                show kazuma_vr zorder 11 at sojusznik1
                            if ziemia == 5:
                                show kazuma_ziemia zorder 11 at sojusznik1
                            if nogi == 5:
                                show kazuma_nogi zorder 11 at sojusznik1
                                
                            show screen kazuma1_stats
                            show kazuma fight zorder 10 at sojusznik1
                            kazuma "Gotowy do boju"
                        
                        "{b}Naofumi (HP:[tarczownik_hp], ATK:[tarczownik_min_attack]-[tarczownik_max_attack]){/b}" if tarczownik_sojusznik >= 1 and tarczownik_wybrany == 0:
                            $ tarczownik_wybrany += 1
                            $ tarczownik_fighter += 1
                            $ tarczownik_hp_now = tarczownik_hp
                            $ tarczownik_min_attack_now = tarczownik_min_attack
                            $ tarczownik_max_attack_now = tarczownik_max_attack 
                            $ tarczownik_min_attack_now_true = tarczownik_min_attack
                            $ tarczownik_max_attack_now_true = tarczownik_max_attack 

                            if tarczownik_klata == 6:
                                show tarczownik_klata zorder 11 at sojusznik1
                            if ring == 6:
                                show tarczownik_ring zorder 11 at sojusznik1
                            if zloty == 6:
                                show tarczownik_zloty zorder 11 at sojusznik1
                                $ tarczownik_zloty_czlowiek = 1
                            if memy == 6:
                                show tarczownik_memy zorder 11 at sojusznik1
                            if vr == 6:
                                show tarczownik_vr zorder 11 at sojusznik1
                            if ziemia == 6:
                                show tarczownik_ziemia zorder 11 at sojusznik1
                            if nogi == 6:
                                show tarczownik_nogi zorder 11 at sojusznik1
                                
                            show tarczownik fight zorder 10 at sojusznik1
                            show screen tarczownik1_stats
                            tarczownik "Gotowy do boju"

                    menu:
                        "{b}Kogo wystawić do walki?{/b}"

                        "{b}Maciej Łuszcz (HP:[luszcz_hp], ATK:[luszcz_min_attack]-[luszcz_max_attack]){/b}" if luszcz_sojusznik >= 1 and luszcz_wybrany == 0:
                            $ luszcz_wybrany += 2
                            $ luszcz_fighter += 2
                            $ luszcz_hp_now = luszcz_hp
                            $ luszcz_min_attack_now = luszcz_min_attack
                            $ luszcz_max_attack_now = luszcz_max_attack
                            $ luszcz_min_attack_now_true = luszcz_min_attack
                            $ luszcz_max_attack_now_true = luszcz_max_attack
                            show screen luszcz2_stats

                            if luszcz_klata == 2:
                                show luszcz_klata zorder 11 at sojusznik2
                            if ring == 2:
                                show luszcz_ring zorder 11 at sojusznik2
                            if zloty == 2:
                                show luszcz_zloty zorder 11 at sojusznik2
                                $ luszcz_zloty_czlowiek = 1
                            if memy == 2:
                                show luszcz_memy zorder 11 at sojusznik2
                            if vr == 2:
                                show luszcz_vr zorder 11 at sojusznik2
                            if ziemia == 2:
                                show luszcz_ziemia zorder 11 at sojusznik2
                            if nogi == 2:
                                show luszcz_nogi zorder 11 at sojusznik2
                                
                            show luszcz fight zorder 10 at sojusznik2
                            luszcz "Gotowy do boju"
                        
                        "{b}Shadow (HP:[eminem_hp], ATK:[eminem_min_attack]-[eminem_max_attack]){/b}" if eminem_sojusznik >= 1 and eminem_wybrany == 0:
                            $ eminem_wybrany += 2
                            $ eminem_fighter += 2
                            $ eminem_hp_now = eminem_hp
                            $ eminem_min_attack_now = eminem_min_attack
                            $ eminem_max_attack_now = eminem_max_attack
                            $ eminem_min_attack_now_true = eminem_min_attack
                            $ eminem_max_attack_now_true = eminem_max_attack

                            if eminem_klata == 7:
                                show eminem_klata zorder 11 at sojusznik2
                            if ring == 7:
                                show eminem_ring zorder 11 at sojusznik2
                            if zloty == 7:
                                show eminem_zloty zorder 11 at sojusznik2
                                $ eminem_zloty_czlowiek = 1
                            if memy == 7:
                                show eminem_memy zorder 11 at sojusznik2
                            if vr == 7:
                                show eminem_vr zorder 11 at sojusznik2
                            if ziemia == 7:
                                show eminem_ziemia zorder 11 at sojusznik2
                            if nogi == 7:
                                show eminem_nogi zorder 11 at sojusznik2

                            show eminem fight zorder 10 at sojusznik2
                            show screen eminem2_stats
                            eminem "Gotowy do boju"

                        "{b}Jerzy Urban (HP:[urban_hp], ATK:[urban_min_attack]-[urban_max_attack]){/b}" if urban_sojusznik >= 1 and urban_wybrany == 0:
                            $ urban_wybrany += 2
                            $ urban_fighter += 2
                            $ urban_hp_now = urban_hp
                            $ urban_min_attack_now = urban_min_attack
                            $ urban_max_attack_now = urban_max_attack
                            $ urban_min_attack_now_true = urban_min_attack
                            $ urban_max_attack_now_true = urban_max_attack

                            if urban_klata == 3:
                                show urban_klata zorder 11 at sojusznik2
                            if ring == 3:
                                show urban_ring zorder 11 at sojusznik2
                            if zloty == 3:
                                show urban_zloty zorder 11 at sojusznik2
                                $ urban_zloty_czlowiek = 1
                            if memy == 3:
                                show urban_memy zorder 11 at sojusznik2
                            if vr == 3:
                                show urban_vr zorder 11 at sojusznik2
                            if ziemia == 3:
                                show urban_ziemia zorder 11 at sojusznik2
                            if nogi == 3:
                                show urban_nogi zorder 11 at sojusznik2

                            show urban fight zorder 10 at sojusznik2
                            show screen urban2_stats
                            urban "Gotowy do boju"

                        "{b}Żyd (HP:[zyd_hp], ATK:[zyd_min_attack]-[zyd_max_attack]){/b}" if zyd_sojusznik >= 1 and zyd_wybrany == 0:
                            $ zyd_wybrany += 2
                            $ zyd_fighter += 2
                            $ zyd_hp_now = zyd_hp
                            $ zyd_min_attack_now = zyd_min_attack
                            $ zyd_max_attack_now = zyd_max_attack
                            $ zyd_min_attack_now_true = zyd_min_attack
                            $ zyd_max_attack_now_true = zyd_max_attack

                            if zyd_klata == 4:
                                show zyd_klata zorder 11 at sojusznik2
                            if ring == 4:
                                show zyd_ring zorder 11 at sojusznik2
                            if zloty == 4:
                                show zyd_zloty zorder 11 at sojusznik2
                                $ zyd_zloty_czlowiek = 1
                            if memy == 4:
                                show zyd_memy zorder 11 at sojusznik2
                            if vr == 4:
                                show zyd_vr zorder 11 at sojusznik2
                            if ziemia == 4:
                                show zyd_ziemia zorder 11 at sojusznik2
                            if nogi == 4:
                                show zyd_nogi zorder 11 at sojusznik2

                            show zyd fight zorder 10 at sojusznik2
                            show screen zyd2_stats
                            zyd "Gotowy do boju"

                        "{b}Kazuma (HP:[kazuma_hp], ATK:[kazuma_min_attack]-[kazuma_max_attack]){/b}" if kazuma_sojusznik >= 1 and kazuma_wybrany == 0:
                            $ kazuma_wybrany += 2
                            $ kazuma_fighter += 2
                            $ kazuma_hp_now = kazuma_hp
                            $ kazuma_min_attack_now = kazuma_min_attack
                            $ kazuma_max_attack_now = kazuma_max_attack
                            $ kazuma_min_attack_now_true = kazuma_min_attack
                            $ kazuma_max_attack_now_true = kazuma_max_attack

                            if kazuma_klata == 5:
                                show kazuma_klata zorder 11 at sojusznik2
                            if ring == 5:
                                show kazuma_ring zorder 11 at sojusznik2
                            if zloty == 5:
                                show kazuma_zloty zorder 11 at sojusznik2
                                $ kazuma_zloty_czlowiek = 1
                            if memy == 5:
                                show kazuma_memy zorder 11 at sojusznik2
                            if vr == 5:
                                show kazuma_vr zorder 11 at sojusznik2
                            if ziemia == 5:
                                show kazuma_ziemia zorder 11 at sojusznik2
                            if nogi == 5:
                                show kazuma_nogi zorder 11 at sojusznik2
                                
                            show kazuma fight zorder 10 at sojusznik2
                            show screen kazuma2_stats
                            kazuma "Gotowy do boju"
                        
                        "{b}Naofumi (HP:[tarczownik_hp], ATK:[tarczownik_min_attack]-[tarczownik_max_attack]){/b}" if tarczownik_sojusznik >= 1 and tarczownik_wybrany == 0:
                            $ tarczownik_wybrany += 2
                            $ tarczownik_fighter += 1
        
                            if luszcz_fighter == 1:
                                $ luszcz_fighter += 1

                            if eminem_fighter == 1:
                                $ eminem_fighter += 1

                            if urban_fighter == 1:
                                $ urban_fighter += 1

                            if zyd_fighter == 1:
                                $ zyd_fighter += 1

                            if kazuma_fighter == 1:
                                $ kazuma_fighter += 1

                            $ tarczownik_hp_now = tarczownik_hp
                            $ tarczownik_min_attack_now = tarczownik_min_attack
                            $ tarczownik_max_attack_now = tarczownik_max_attack
                            $ tarczownik_min_attack_now_true = tarczownik_min_attack
                            $ tarczownik_max_attack_now_true = tarczownik_max_attack

                            if tarczownik_klata == 6:
                                show tarczownik_klata zorder 11 at sojusznik2
                            if ring == 6:
                                show tarczownik_ring zorder 11 at sojusznik2
                            if zloty == 6:
                                show tarczownik_zloty zorder 11 at sojusznik2
                                $ tarczownik_zloty_czlowiek = 1
                            if memy == 6:
                                show tarczownik_memy zorder 11 at sojusznik2
                            if vr == 6:
                                show tarczownik_vr zorder 11 at sojusznik2
                            if ziemia == 6:
                                show tarczownik_ziemia zorder 11 at sojusznik2
                            if nogi == 6:
                                show tarczownik_nogi zorder 11 at sojusznik2
                                
                            show tarczownik fight zorder 10 at sojusznik2
                            show screen tarczownik2_stats
                            tarczownik "Gotowy do boju"
                        
                    jump start_fight1

                else:
                    $ ile_sojusznikow += 1
                    $ luszcz_wybrany += 3
                    $ luszcz_fighter += 1
                    $ luszcz_hp_now = luszcz_hp
                    $ luszcz_min_attack_now = luszcz_min_attack
                    $ luszcz_max_attack_now = luszcz_max_attack
                    $ luszcz_min_attack_now_true = luszcz_min_attack
                    $ luszcz_max_attack_now_true = luszcz_max_attack

                    if luszcz_klata == 2:
                        show luszcz_klata zorder 11 at sojusznik3
                    if ring == 2:
                        show luszcz_ring zorder 11 at sojusznik3
                    if zloty == 2:
                        show luszcz_zloty zorder 11 at sojusznik3
                        $ luszcz_zloty_czlowiek = 1
                    if memy == 2:
                        show luszcz_memy zorder 11 at sojusznik3
                    if vr == 2:
                        show luszcz_vr zorder 11 at sojusznik3
                    if ziemia == 2:
                        show luszcz_ziemia zorder 11 at sojusznik3
                    if nogi == 2:
                        show luszcz_nogi zorder 11 at sojusznik3

                    show luszcz fight zorder 10 at sojusznik3
                    show screen luszcz3_stats
                    luszcz "Gotowy do boju"

                    jump start_fight1
    
    label start_fight1:
        hide air_strike_shield1
        hide air_strike_shield2
        hide air_strike_shield3
        hide shield_prison
        hide uszy1
        hide uszy2
        hide uszy3
        hide slime
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide ruch
        hide tarcza1
        hide tarcza2
        hide tarcza3
        hide tarcza4
        hide tarcza5
        hide stun1
        hide stun2
        hide stun3

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide ekdplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0

        if ile_sojusznikow <= 0:
            jump przegranko_fight1

        if kibol1_poison >= 3 and kibol1_hp_now >= 1:
            $ kibol1_hp_now -= 1
        
        else:
            if kibol1_poison == 2:
                $ kibol1_hp_now -= 1
            
            else:
                if kibol1_poison == 1:
                    $ kibol1_hp_now -= 1
        
        if akane_poison >= 3 and akane_hp_now >= 1:
            $ akane_hp_now -= 1
        
        else:
            if akane_poison == 2:
                $ akane_hp_now -= 1
            
            else:
                if akane_poison == 1:
                    $ akane_hp_now -= 1
        
        if kibol2_poison >= 3 and kibol2_hp_now >= 1:
            $ kibol2_hp_now -= 1
        
        else:
            if kibol2_poison == 2:
                $ kibol2_hp_now -= 1
            
            else:
                if kibol2_poison == 1:
                    $ kibol2_hp_now -= 1
                
        if kibol1_poison >= 1 and akane_poison >= 1 and kibol2_poison >= 1 and kibol1_hp_now >= 0 and akane_hp_now >= 0 and kibol2_hp_now >= 0:
            play sound "audio/sfx/snake.mp3"
            "{i}Kibol 1, Akane i Kibol 2 stracili po 1HP z powodu ukąszenia przez węża{/i}"
                    
        else:
            if kibol1_poison >= 1 and akane_poison >= 1 and kibol1_hp_now >= 0 and akane_hp_now >= 0:
                play sound "audio/sfx/snake.mp3"
                "{i}Kibol 1 i Akane stracili po 1HP z powodu ukąszenia przez węża{/i}"
                        
            else:
                if akane_poison >= 1 and kibol2_poison >= 1 and akane_hp_now >= 0 and kibol2_hp_now >= 0:
                    play sound "audio/sfx/snake.mp3"
                    "{i}Akane i Kibol 2 stracili po 1HP z powodu ukąszenia przez węża{/i}"
                                
                            
                else:
                    if kibol1_poison >= 1 and kibol2_poison >= 1 and kibol1_hp_now >= 0 and kibol2_hp_now >= 0:
                        play sound "audio/sfx/snake.mp3"
                        "{i}Kibol 1 i Kibol 2 stracili po 1HP z powodu ukąszenia przez węża{/i}"
                                
                    else:
                        if kibol1_poison >= 1 and kibol1_hp_now >= 0:
                            play sound "audio/sfx/snake.mp3"
                            "{i}Kibol 1 stracił 1HP z powodu ukąszenia przez węża{/i}"
                                    
                        else:
                            if akane_poison >= 1 and akane_hp_now >= 0:
                                play sound "audio/sfx/snake.mp3"
                                "{i}Akane stracił 1HP z powodu ukąszenia przez węża{/i}"

                            else:
                                if kibol2_poison >= 1 and kibol2_hp_now >= 0:
                                    play sound "audio/sfx/snake.mp3"
                                    "{i}Kibol 2 stracił 1HP z powodu ukąszenia przez węża{/i}"
        
        if kibol1_poison == 1 and kibol1_hp_now >= 1:
            $ kibol1_poison -= 1
            hide snake11
        
        if kibol1_poison == 2 and kibol1_hp_now >= 1:
            $ kibol1_poison -= 1
            hide snake21
            show snake11 zorder 15 at center_wrog1

        if kibol1_poison == 3 and kibol1_hp_now >= 1:
            $ kibol1_poison -= 1
            hide snake31
            show snake21 zorder 15 at center_wrog1
        
        if akane_poison == 1 and akane_hp_now >= 1:
            $ akane_poison -= 1
            hide snake12
        
        if akane_poison == 2 and akane_hp_now >= 1:
            $ akane_poison -= 1
            hide snake22
            show snake12 zorder 15 at center_wrog3
        
        if akane_poison == 3 and akane_hp_now >= 1:
            $ akane_poison -= 1
            hide snake32
            show snake22 zorder 15 at center_wrog3

        if kibol2_poison == 1 and kibol2_hp_now >= 1:
            $ kibol2_poison -= 1
            hide snake13    

        if kibol2_poison == 2 and kibol2_hp_now >= 1:
            $ kibol2_poison -= 1
            hide snake23
            show snake13 zorder 15 at center_wrog2 
        
        if kibol2_poison == 3 and kibol2_hp_now >= 1:
            $ kibol2_poison -= 1
            hide snake33
            show snake23 zorder 15 at center_wrog2

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide ekdplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0

        if ile_sojusznikow <= 0:
            jump przegranko_fight1

        if luszcz_lagodny == 1:
            if luszcz_hp_now + 1 < luszcz_hp:
                $ luszcz_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Łuszcz odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ luszcz_lagodny -= 1
            hide plamka1

        if luszcz_lagodny == 2:
            if luszcz_hp_now + 1 < luszcz_hp:
                $ luszcz_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Łuszcz odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ luszcz_lagodny -= 1

        if luszcz_lagodny == 3:
            if luszcz_hp_now + 1 < luszcz_hp:
                $ luszcz_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Łuszcz odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ luszcz_lagodny -= 1

        if eminem_lagodny == 1:
            if eminem_hp_now + 1 < eminem_hp:
                $ eminem_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Shadow odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ eminem_lagodny -= 1
            hide plamka2

        if eminem_lagodny == 2:
            if eminem_hp_now + 1 < eminem_hp:
                $ eminem_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Shadow odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ eminem_lagodny -= 1

        if eminem_lagodny == 3:
            if eminem_hp_now + 1 < eminem_hp:
                $ eminem_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Shadow odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ eminem_lagodny -= 1
        
        if urban_lagodny == 1:
            if urban_hp_now + 1 < urban_hp:
                $ urban_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Jerzy Urban odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ urban_lagodny -= 1
            hide plamka3

        if urban_lagodny == 2:
            if urban_hp_now + 1 < urban_hp:
                $ urban_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Jerzy Urban odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ urban_lagodny -= 1

        if urban_lagodny == 3:
            if urban_hp_now + 1 < urban_hp:
                $ urban_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Jerzy Urban odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ urban_lagodny -= 1
        
        if zyd_lagodny == 1:
            if zyd_hp_now + 1 < zyd_hp:
                $ zyd_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Żyd odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ zyd_lagodny -= 1
            hide plamka4

        if zyd_lagodny == 2:
            if zyd_hp_now + 1 < zyd_hp:
                $ zyd_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Żyd odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ zyd_lagodny -= 1

        if zyd_lagodny == 3:
            if zyd_hp_now + 1 < zyd_hp:
                $ zyd_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Żyd odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ zyd_lagodny -= 1
    
        if kazuma_lagodny == 1:
            if kazuma_hp_now + 1 < kazuma_hp:
                $ kazuma_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Kazuma odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ kazuma_lagodny -= 1
            hide plamka5

        if kazuma_lagodny == 2:
            if kazuma_hp_now + 1 < kazuma_hp:
                $ kazuma_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Kazuma odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ kazuma_lagodny -= 1

        if kazuma_lagodny == 3:
            if kazuma_hp_now + 1 < kazuma_hp:
                $ kazuma_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Kazuma odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ kazuma_lagodny -= 1
        
        if tarczownik_lagodny == 1:
            if tarczownik_hp_now + 1 >= tarczownik_hp:
                $ tarczownik_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Naofumi odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ tarczownik_lagodny -= 1
            hide plamka6

        if tarczownik_lagodny == 2:
            if tarczownik_hp_now + 1 < tarczownik_hp:
                $ tarczownik_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Naofumi odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ tarczownik_lagodny -= 1

        if tarczownik_lagodny == 3:
            if tarczownik_hp_now + 1 < tarczownik_hp:
                $ tarczownik_hp_now += 1
                play sound "audio/sfx/heal.mp3"
                "{i}Naofumi odzyskuje 1 punkt życia dzięki zjedzeniu łagodnego kebaba{/i}"

            $ tarczownik_lagodny -= 1
        
        $ kibol1_uszy = 0
        $ akane_uszy = 0
        $ kibol2_uszy = 0

        $ akane_stun = 0
        $ kibol1_stun = 0
        $ kibol2_stun = 0

        $ luszcz_obrona = 0
        $ eminem_obrona = 0
        $ urban_obrona = 0
        $ zyd_obrona = 0
        $ kazuma_obrona = 0
        $ tarczownik_obrona = 0

        $ tarczownik_air_strike_shield = 0

        $ kibol1_min_attack_now = kibol1_min_attack_now_true
        $ kibol1_max_attack_now = kibol1_max_attack_now_true
        $ kibol2_min_attack_now = kibol2_min_attack_now_true
        $ kibol2_max_attack_now = kibol2_max_attack_now_true
        $ akane_min_attack_now = akane_min_attack_now_true
        $ akane_max_attack_now = akane_max_attack_now_true

        if miecz3d == 2 and luszcz_hp_now <= luszcz_hp / 2 and luszcz_fighter == 1:
            $ luszcz_min_attack_now += 1
            $ luszcz_max_attack_now += 2
        
        if miecz3d == 3 and urban_hp_now <= urban_hp / 2 and urban_fighter == 1:
            $ urban_min_attack_now += 1
            $ urban_max_attack_now += 2
        
        if miecz3d == 4 and zyd_hp_now <= zyd_hp / 2 and zyd_fighter == 1:
            $ zyd_min_attack_now += 1
            $ zyd_max_attack_now += 2
        
        if miecz3d == 5 and kazuma_hp_now <= kazuma_hp / 2 and kazuma_fighter == 1:
            $ kazuma_min_attack_now += 1
            $ kazuma_max_attack_now += 2
        
        if miecz3d == 6 and tarczownik_hp_now <= tarczownik_hp / 2 and tarczownik_fighter == 1:
            $ tarczownik_min_attack_now += 1
            $ tarczownik_max_attack_now += 2
        
        if luszcz_drpepper == 0:
            hide okabe1
        
        if luszcz_drpepper == 1:
            $ luszcz_drpepper -= 1
            $ luszcz_min_attack_now = luszcz_max_attack_now
    
        if eminem_drpepper == 0:
            hide okabe2
        
        if eminem_drpepper == 1:
            $ eminem_drpepper -= 1
            $ eminem_min_attack_now = eminem_max_attack_now
        
        if urban_drpepper == 0:
            hide okabe3
        
        if urban_drpepper == 1:
            $ urban_drpepper -= 1
            $ urban_min_attack_now = urban_max_attack_now
        
        if zyd_drpepper == 0:
            hide okabe4
        
        if zyd_drpepper == 1:
            $ zyd_drpepper -= 1
            $ zyd_min_attack_now = zyd_max_attack_now
        
        if kazuma_drpepper == 0:
            hide okabe5
        
        if kazuma_drpepper == 1:
            $ kazuma_drpepper -= 1
            $ kazuma_min_attack_now = kazuma_max_attack_now
        
        if tarczownik_drpepper == 0:
            hide okabe6
        
        if tarczownik_drpepper == 1:
            $ tarczownik_drpepper -= 1
            $ tarczownik_min_attack_now = tarczownik_max_attack_now


        if luszcz_fighter == 1:
            if luszcz_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if luszcz_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if luszcz_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 2 and luszcz_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ luszcz_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([luszcz_min_attack_now]-[luszcz_max_attack_now] DMG){/b}":
                    if luszcz_weapon >= 1:
                        if luszcz_wybrany == 1:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik1  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if luszcz_wybrany == 2:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik2  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if luszcz_wybrany == 3:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik3 

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik3   

                    else:
                        if luszcz_wybrany == 1:
                            show reka1 zorder 15 at weapon_sojusznik1 

                        if luszcz_wybrany == 2:
                            show reka1 zorder 15 at weapon_sojusznik2  

                        if luszcz_wybrany == 3:
                            show reka1 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 2 and luszcz_weapon >= 1:                     
                        luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                    
                        $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol1_hp_now -= luszcz_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ akane_hp_now -= luszcz_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol2_hp_now -= luszcz_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [luszcz_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Łuszcza został zablokowany{/i}"

                        jump faza12

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:  
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12

                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"

                                jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:     
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3"  

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12

                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza12
                    
                "{b}Obrona{/b}" if luszcz_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if luszcz_wybrany == 1:
                        show tarcza1 zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show tarcza1 zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show tarcza1 zorder 15 at weapon_sojusznik3 

                    $ luszcz_obrona += 1
                    luszcz "I want sex"
                    jump faza12
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if luszcz_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    luszcz "Umiem wyobrażać sobie ludzi w stroju ziemniaka"
                    jump items11

                "{b}Zaparz Herbatę{/b}":
                    play sound "audio/sfx/herbaty.mp3"
                    if luszcz_wybrany == 1:
                        show herbaty zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show herbaty zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show herbaty zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Ale jaką?{/b}"

                        "{b}Wiśnia z Rumem (+5HP){/b}":
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                            menu:
                                "{b}Dla Kogo?{/b}"

                                "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    if luszcz_hp_now + 5 > luszcz_hp:
                                        $ luszcz_hp_now = luszcz_hp
                                        "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                    else:
                                        $ luszcz_hp_now += 5
                                        "{i}Łuszcz odzyskał 5 punktów życia{/i}"
                                
                                "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if eminem_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if eminem_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if eminem_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if eminem_hp_now + 5 > eminem_hp:
                                        $ eminem_hp_now = eminem_hp
                                        "{i}Shadow odzyskał cały pasek życia{/i}"
                                    else:
                                        $ eminem_hp_now += 5
                                        "{i}Shadow odzyskał 5 punktów życia{/i}"

                                "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if urban_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if urban_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if urban_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if urban_hp_now + 5 > urban_hp:
                                        $ urban_hp_now = urban_hp
                                        "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                    else:
                                        $ urban_hp_now += 5
                                        "{i}Jerzy Urban odzyskał 5 punktów życia{/i}"

                                "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if zyd_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if zyd_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if zyd_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if zyd_hp_now + 5 > zyd_hp:
                                        $ zyd_hp_now = zyd_hp
                                        "{i}Żyd odzyskał cały pasek życia{/i}"
                                    else:
                                        $ zyd_hp_now += 5
                                        "{i}Żyd odzyskał 5 punktów życia{/i}"

                                "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if kazuma_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if kazuma_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if kazuma_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if kazuma_hp_now + 5 > kazuma_hp:
                                        $ kazuma_hp_now = kazuma_hp
                                        "{i}Kazuma odzyskał cały pasek życia{/i}"
                                    else:
                                        $ kazuma_hp_now += 5
                                        "{i}Kazuma odzyskał 5 punktów życia{/i}"
                                
                                "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if tarczownik_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if tarczownik_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if tarczownik_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if tarczownik_hp_now + 5 > tarczownik_hp:
                                        $ tarczownik_hp_now = tarczownik_hp
                                        "{i}Naofumi odzyskał cały pasek życia{/i}"
                                    else:
                                        $ tarczownik_hp_now += 5
                                        "{i}Naofumi odzyskał 5 punktów życia{/i}"
                            
                            hide wisnia_w_rumie
                            jump faza12
                            
                        "{b}Hiszpańska Mandarynka (+2HP FOR ALL){/b}":
                            luszcz "Tak. Moja mama tylko czasami zagląda mi do buzi"
                            play sound "audio/sfx/herbata.mp3"
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                            if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                if luszcz_hp_now + 2 > luszcz_hp:
                                    $ luszcz_hp_now = luszcz_hp
                                else:
                                    $ luszcz_hp_now += 2
                            
                            if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                if eminem_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if eminem_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if eminem_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if eminem_hp_now + 2 > eminem_hp:
                                    $ eminem_hp_now = eminem_hp
                                else:
                                    $ eminem_hp_now += 2

                            if urban_hp_now >= 1 and urban_wybrany >= 1:
                                if urban_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if urban_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if urban_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if urban_hp_now + 2 > urban_hp:
                                    $ urban_hp_now = urban_hp
                                else:
                                    $ urban_hp_now += 2

                            if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                if zyd_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if zyd_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if zyd_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if zyd_hp_now + 2 > zyd_hp:
                                    $ zyd_hp_now = zyd_hp
                                else:
                                    $ zyd_hp_now += 2

                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if kazuma_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if kazuma_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if kazuma_hp_now + 2 > kazuma_hp:
                                    $ kazuma_hp_now = kazuma_hp
                                else:
                                    $ kazuma_hp_now += 2
                            
                            if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                if tarczownik_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if tarczownik_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if tarczownik_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if tarczownik_hp_now + 2 > tarczownik_hp:
                                    $ tarczownik_hp_now = tarczownik_hp
                                else:
                                    $ tarczownik_hp_now += 2

                            "{i}Wszyscy sojusznicy odzyskali po 2 punkty życia{/i}"
                            hide hiszpanska_mandarynka1
                            hide hiszpanska_mandarynka2
                            hide hiszpanska_mandarynka3
                            jump faza12
        
        if eminem_fighter == 1:
            if eminem_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if eminem_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if eminem_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([eminem_min_attack_now]-[eminem_max_attack_now] DMG){/b}":
                    if eminem_weapon >= 1:
                        if eminem_wybrany == 1:
                            show eminem_weapon zorder 15 at weapon_sojusznik1  

                        if eminem_wybrany == 2:
                            show eminem_weapon zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show eminem_weapon zorder 15 at weapon_sojusznik3 

                    else:
                        if eminem_wybrany == 1:
                            show reka2 zorder 15 at weapon_sojusznik1 

                        if eminem_wybrany == 2:
                            show reka2 zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show reka2 zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:  
                                play sound "audio/sfx/reka.mp3"             
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol1_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else: 
                                play sound "audio/sfx/reka.mp3"                          
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ akane_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                play sound "audio/sfx/reka.mp3"
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol2_hp_now -= eminem_attack

                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza12
                    
                "{b}Obrona{/b}" if eminem_obrona == 0:
                    eminem "I am ..."
                    play sound "audio/sfx/shield.mp3"
                    if eminem_wybrany == 1:
                        show tarcza2 zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show tarcza2 zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show tarcza2 zorder 15 at weapon_sojusznik3 

                    $ eminem_obrona += 1
                    eminem "... rzymskim legionistą"
                    jump faza12
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if eminem_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    eminem "Czas zabawy się skończył"
                    jump items11

                "{b}Rzut Szlamem{/b}":
                    if eminem_wybrany == 1:
                        show slime zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show slime zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show slime zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 1 obronił się przed szlamem{/i}"
                                jump faza12
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol1_min_attack_now >= 2:
                                    $ kibol1_min_attack_now -= 2
                                    if kibol1_max_attack_now >= 6:
                                        $ kibol1_max_attack_now -= 3
                                    else:
                                        $ kibol1_max_attack_now -= 2
                                    
                                else:
                                    $ kibol1_min_attack_now = 0

                                    if kibol1_max_attack_now >= 2:
                                        if kibol1_max_attack_now >= 6:
                                            $ kibol1_max_attack_now -= 3
                                        else:
                                            $ kibol1_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol1_max_attack_now = 0
                                
                                $ kibol1_slime += 1
                                show slime zorder 15 at center_wrog1 
                                "{i}Statystyki Kibol 1 zostały osłabione{/i}"
                                jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Akane obronił się przed szlamem{/i}"
                                jump faza12
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if akane_min_attack_now >= 2:
                                    $ akane_min_attack_now -= 2
                                    if akane_max_attack_now >= 6:
                                        $ akane_max_attack_now -= 3
                                    else:
                                        $ akane_max_attack_now -= 2
                        
                                else:
                                    $ akane_min_attack_now = 0

                                    if akane_max_attack_now >= 2:
                                        if akane_max_attack_now >= 6:
                                            $ akane_max_attack_now -= 3
                                        else:
                                            $ akane_max_attack_now -= 2
                                    
                                    else:
                                        $ akane_max_attack_now = 0
                                
                                $ akane_slime += 1
                                show slime zorder 15 at center_wrog3
                                "{i}Statystyki Akane zostały osłabione{/i}"
                                jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 2 obronił się przed szlamem{/i}"
                                jump faza12
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol2_min_attack_now >= 2:
                                    $ kibol2_min_attack_now -= 2
                                    if kibol2_max_attack_now >= 6:
                                        $ kibol2_max_attack_now -= 3
                                    else:
                                        $ kibol2_max_attack_now -= 2
                        
                                else:
                                    $ kibol2_min_attack_now = 0

                                    if kibol2_max_attack_now >= 2:
                                        if kibol2_max_attack_now >= 6:
                                            $ kibol2_max_attack_now -= 3
                                        else:
                                            $ kibol2_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol2_max_attack_now = 0
                                
                                $ kibol2_slime += 1
                                show slime zorder 15 at center_wrog2
                                "{i}Statystyki Kibol 2 zostały osłabione{/i}"
                                jump faza12

        if urban_fighter == 1:
            if urban_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if urban_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if urban_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 

            if ostrza_chaosu == 3 and urban_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ urban_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([urban_min_attack_now]-[urban_max_attack_now] DMG){/b}":
                    if urban_weapon >= 1:
                        if urban_wybrany == 1:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik1  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if urban_wybrany == 2:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik2  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if urban_wybrany == 3:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik3 

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if urban_wybrany == 1:
                            show reka3 zorder 15 at weapon_sojusznik1 

                        if urban_wybrany == 2:
                            show reka3 zorder 15 at weapon_sojusznik2  

                        if urban_wybrany == 3:
                            show reka3 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 3 and urban_weapon >= 1:
                        urban "i Ci kutasa obetnie"
                    
                        $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol1_hp_now -= urban_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ akane_hp_now -= urban_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol2_hp_now -= urban_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [urban_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Jerzego Urbana został zablokowany{/i}"

                        jump faza12

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban1:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol1_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol1_obrona = 1
                                                                
                                else:  
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol1_obrona == 1 and stop == 3 or urban_attack == 2 and kibol1_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban1
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol1_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza12

                                            $ kibol1_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol1_poison = 3
                                                show snake31 zorder 15 at center_wrog1
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza12

                                            $ kibol1_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol1_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun1 zorder 15 at head_wrog1
                                                    $ kibol1_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza12
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban2:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if akane_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ akane_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and akane_obrona == 1 and stop == 3 or urban_attack == 2 and akane_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban2
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if akane_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza12

                                            $ akane_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ akane_poison = 3
                                                show snake32 zorder 15 at center_wrog3
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza12

                                            $ akane_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and akane_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun2 zorder 15 at head_wrog3
                                                    $ akane_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza12
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban3:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol2_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol2_obrona = 1
                                                                
                                else: 
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol2_obrona == 1 and stop == 3 or urban_attack == 2 and kibol2_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban3
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol2_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza12

                                            $ kibol2_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol2_poison = 3
                                                show snake33 zorder 15 at center_wrog2
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza12

                                            $ kibol2_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol2_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun3 zorder 15 at head_wrog2
                                                    $ kibol2_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza12

                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza12
                    
                "{b}Obrona{/b}" if urban_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if urban_wybrany == 1:
                        show tarcza3 zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show tarcza3 zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show tarcza3 zorder 15 at weapon_sojusznik3 

                    $ urban_obrona += 1
                    urban "A ja mam to w dupie"
                    jump faza12
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if urban_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    urban "No tak było, nie zmyślam"
                    jump items11

                "{b}Zatrzepocz Uszami{/b}":
                    if urban_wybrany == 1:
                        show uszy zorder 15 at head_sojusznik1  

                    if urban_wybrany == 2:
                        show uszy zorder 15 at head_sojusznik2  

                    if urban_wybrany == 3:
                        show uszy zorder 15 at head_sojusznik3 
                    
                    urban "Hhyyy pfff hhyyy pffff hhyyy"
                    play sound "audio/sfx/uszy.mp3" 

                    if kibol1_obrona <= 0:
                        $ kibol1_uszy += 1
                    
                    if akane_obrona <= 0:
                        $ akane_uszy += 1
                    
                    if kibol2_obrona <= 0:
                        $ kibol2_uszy += 1

                    if kibol1_uszy == 1 and akane_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                        show uszy2 zorder 15 at head_wrog3
                        show uszy3 zorder 15 at head_wrog2
                        show uszy1 zorder 15 at head_wrog1
                        "{i}Kibol 1, Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                    
                    else:
                        if kibol1_uszy == 1 and akane_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            show uszy2 zorder 15 at head_wrog3
                            show uszy1 zorder 15 at head_wrog1
                            "{i}Kibol 1 i Akane skupili się na uszach Urbana{/i}"
                        
                        else:
                            if akane_uszy == 1 and kibol2_uszy == 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                                show uszy2 zorder 15 at head_wrog3
                                show uszy3 zorder 15 at head_wrog2
                                "{i}Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                                
                            
                            else:
                                if kibol1_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                                    show uszy3 zorder 15 at head_wrog2
                                    show uszy1 zorder 15 at head_wrog1
                                    "{i}Kibol 1 i Kibol 2 skupili się na uszach Urbana{/i}"
                                
                                else:
                                    if kibol1_uszy == 1 and kibol1_hp_now >= 1:
                                        show uszy1 zorder 15 at head_wrog1
                                        "{i}Kibol 1 skupił się na uszach Urbana{/i}"
                                    
                                    else:
                                        if akane_uszy == 1 and akane_hp_now >= 1:
                                            show uszy2 zorder 15 at head_wrog3
                                            "{i}Akane skupił się na uszach Urbana{/i}"

                                        else:
                                            if kibol2_uszy == 1 and kibol2_hp_now >= 1:
                                                show uszy3 zorder 15 at head_wrog2
                                                "{i}Kibol 2 skupił się na uszach Urbana{/i}"

                                            else:
                                                "{i}Niestety, ale uszy Urbana nie uwiodły nikogo{/i}"

                    hide uszy
                    jump faza12   
        if zyd_fighter == 1:
            if zyd_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if zyd_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if zyd_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 4 and zyd_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ zyd_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([zyd_min_attack_now]-[zyd_max_attack_now] DMG){/b}":
                    if zyd_weapon >= 1:
                        if zyd_wybrany == 1:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik1  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if zyd_wybrany == 2:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik2  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if zyd_wybrany == 3:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik3 

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik3

                    else:
                        if zyd_wybrany == 1:
                            show reka4 zorder 15 at weapon_sojusznik1 

                        if zyd_wybrany == 2:
                            show reka4 zorder 15 at weapon_sojusznik2  

                        if zyd_wybrany == 3:
                            show reka4 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 4 and zyd_weapon >= 1:    
                        zyd "Proszę pana, oni są zakałą tej ziemi!"
                    
                        $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol1_hp_now -= zyd_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ akane_hp_now -= zyd_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol2_hp_now -= zyd_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [zyd_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Żyda został zablokowany{/i}"

                        jump faza12

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1

                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"

                            jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else: 
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:  
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12

                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza12
                    
                "{b}Obrona{/b}" if zyd_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if zyd_wybrany == 1:
                        show tarcza4 zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show tarcza4 zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show tarcza4 zorder 15 at weapon_sojusznik3 

                    $ zyd_obrona += 1
                    zyd "Nie interesuje mnie polska polityka"
                    jump faza12
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if zyd_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    zyd "Chcą, abyś to my żydzi się asymilowali i przechodzili na ich religie!"
                    jump items11

                "{b}Sprzedaj Pager{/b}" if pager_boom == 0 and kibol1_pager == 0 and kibol1_hp_now >= 1 or pager_boom == 0 and akane_pager == 0 and akane_hp_now >= 1 or pager_boom == 0 and kibol2_pager == 0 and kibol2_hp_now >= 1:
                    if zyd_wybrany == 1:
                        show pager zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show pager zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show pager zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Komu?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol1_pager += 1
                            show pager1 zorder 15 at bok_wrog1  
                            
                            "{i}Kibol 1 kupił pager od Żyda{/i}"

                            jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ akane_pager += 1
                            
                            show pager2 zorder 15 at bok_wrog3
                            "{i}Akane kupił pager od Żyda{/i}"

                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol2_pager += 1
                            
                            show pager3 zorder 15 at bok_wrog2
                            "{i}Kibol 2 kupił pager od Żyda{/i}"

                            jump faza12
                
                "{b}Wysadź Pagery{/b}" if kibol1_pager >= 1 and pager_boom == 0 or akane_pager >= 1 and pager_boom == 0 or kibol2_pager >= 1 and pager_boom == 0:
                    $ pager_boom += 1
                    if zyd_wybrany == 1:
                        show red_button zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show red_button zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show red_button zorder 15 at weapon_sojusznik3 

                    zyd "Posmakujcie gniewu WIELKIEGO IZRAELA!!!"
                    play sound "audio/sfx/boom.mp3" 

                    if kibol1_pager == 1 and akane_pager == 1 and kibol2_pager == 1:
                        $ kibol1_hp_now -= 8
                        $ kibol2_hp_now -= 8
                        $ akane_hp_now -= 8
                        show eksplozja1 zorder 16 at bok_wrog1
                        show eksplozja3 zorder 16 at bok_wrog2
                        show eksplozja2 zorder 16 at bok_wrog3
                        "{i}Kibol 1, Akane i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                            
                    else:
                        if kibol1_pager == 1 and akane_pager == 1:
                            $ kibol1_hp_now -= 8
                            $ akane_hp_now -= 8
                            show eksplozja1 zorder 16 at bok_wrog1
                            show eksplozja2 zorder 16 at bok_wrog3
                            "{i}Kibol 1 i Akane w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                
                        else:
                            if akane_pager == 1 and kibol2_pager == 1:
                                $ kibol2_hp_now -= 8
                                $ akane_hp_now -= 8
                                show eksplozja3 zorder 16 at bok_wrog2
                                show eksplozja2 zorder 16 at bok_wrog3
                                "{i}Akane i Kibol 1 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                    
                            else:
                                if kibol1_pager == 1 and kibol2_pager == 1:
                                    $ kibol1_hp_now -= 8
                                    $ kibol2_hp_now -= 8
                                    show eksplozja1 zorder 16 at bok_wrog1
                                    show eksplozja3 zorder 16 at bok_wrog2
                                    "{i}Kibol 1 i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                        
                                else:
                                    if kibol1_pager == 1:
                                        $ kibol1_hp_now -= 8
                                        show eksplozja1 zorder 16 at bok_wrog1
                                        "{i}Kibol 1 w wyniku ekspolzji Pageru stracił 8HP{/i}"
                                            
                                    else:
                                        if akane_pager == 1:
                                            $ akane_hp_now -= 8
                                            show eksplozja2 zorder 16 at bok_wrog3
                                            "{i}Akane w wyniku ekspolzji Pageru stracił 8HP{/i}"

                                        else:
                                            if kibol2_pager == 1:
                                                $ kibol2_hp_now -= 8
                                                show eksplozja3 zorder 16 at bok_wrog2
                                                "{i}Kibol 2 w wyniku ekspolzji Pageru stracił 8HP{/i}"

                    hide red_button
                    hide pager1
                    hide pager2
                    hide pager3
                    hide pager
                    hide eksplozja1
                    hide eksplozja2
                    hide eksplozja3
                    if dialog_fight1 == 0:
                        luszcz "O ja pierdole, może Braun jednak miał trochę racji!"
                        $ dialog_fight1 += 1

                    jump faza12

        if kazuma_fighter == 1:
            if kazuma_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if kazuma_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if kazuma_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 5 and kazuma_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ kazuma_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([kazuma_min_attack_now]-[kazuma_max_attack_now] DMG){/b}":
                    if kazuma_weapon >= 1:
                        if kazuma_wybrany == 1:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik1  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if kazuma_wybrany == 2:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik2  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if kazuma_wybrany == 3:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik3 

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if kazuma_wybrany == 1:
                            show reka5 zorder 15 at weapon_sojusznik1 

                        if kazuma_wybrany == 2:
                            show reka5 zorder 15 at weapon_sojusznik2  

                        if kazuma_wybrany == 3:
                            show reka5 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 5 and kazuma_weapon >= 1:   
                        kazuma "Tak, jestem Kazuma"
                    
                        $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol1_hp_now -= kazuma_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ akane_hp_now -= kazuma_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(v_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol2_hp_now -= kazuma_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [kazuma_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Kazumy został zablokowany{/i}"

                        jump faza12

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol1_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ akane_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza12

                                    $ kibol2_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza12
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza12
    
                    
                "{b}Obrona{/b}" if kazuma_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if kazuma_wybrany == 1:
                        show tarcza5 zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show tarcza5 zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show tarcza5 zorder 15 at weapon_sojusznik3 

                    $ kazuma_obrona += 1
                    kazuma "Nic na to nie można poradzić!"
                    jump faza12
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if kazuma_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    kazuma "Jestem zwolennikiem prawdziwej równości płci"
                    jump items11

                "{b}Steal{/b}" if kibol1_weapon >= 1 or akane_weapon >= 1 or kibol2_weapon >= 1:
                    if kazuma_wybrany == 1:
                        show chwyta zorder 16 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chwyta zorder 16 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chwyta zorder 16 at weapon_sojusznik3 

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_weapon > 0:
                            kazuma "Steal!"

                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 1 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza12
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol1_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol1_max_attack_now < kibol1_max_attack:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true
                                            $ kibol1_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true
                                        
                                        $ kibol1_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 1.  \nStatystyki Kibol 1 zostały stale drastycznie osłabione.{/i}"
                                        hide kibol1_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol1 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 1.  \nKibol 1 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol1_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                                        
                                jump faza12

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_weapon > 0:
                            kazuma "Steal!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Akane obronił się przed umiejętnością “Steal“{/i}"
                                jump faza12
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if akane_sex == 0:
                                    
                                    if kostka >= 9:
                                        if akane_max_attack_now < akane_max_attack:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                            $ akane_max_attack_now -= 2
                                        
                                        else:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                        
                                        $ akane_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show akane_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show akane_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show akane_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Akane.  \nStatystyki Akane zostały stale drastycznie osłabione.{/i}"
                                        hide kibol2_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        akane "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Akane.  \nAkane poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ akane_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                                        
                                jump faza12

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_weapon > 0:
                            kazuma "Steal!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 2 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza12
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol2_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol2_max_attack_now < kibol2_max_attack:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                            $ kibol2_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                        
                                        $ kibol2_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 2.  \nStatystyki Kibol 2 zostały stale drastycznie osłabione.{/i}"
                                        hide akane_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol2 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 2.  \nKibol 2 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol2_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                                        
                                jump faza12

        if tarczownik_fighter == 1 and tarczownik_weapon >= 1:
            if tarczownik_hp_now >= 1:
                if tarczownik_wybrany == 1:
                    show ruch zorder 0 at tlo_sojusznik1  

                if tarczownik_wybrany == 2:
                    show ruch zorder 0 at tlo_sojusznik2  

                if tarczownik_wybrany == 3:
                    show ruch zorder 0 at tlo_sojusznik3 

                if luszcz_hp_now <= 4 and luszcz_wybrany >= 1 or eminem_hp_now <= 4 and eminem_wybrany >= 1 or urban_hp_now <= 4 and urban_wybrany >= 1 or zyd_hp_now <= 4 and zyd_wybrany >= 1 or kazuma_hp_now <= 4 and kazuma_wybrany >= 1:
                    $ kostka = renpy.random.randint(1, 10)

                    if kostka >= 4:
                        $ luszcz_obrona += 1
                        $ eminem_obrona += 1
                        $ urban_obrona += 1
                        $ zyd_obrona += 1
                        $ kazuma_obrona += 1
                        $ tarczownik_obrona += 1
                        play sound "audio/sfx/air_strike_shield.mp3"

                        if luszcz_wybrany == 1 and luszcz_hp_now >= 1 or eminem_wybrany == 1 and eminem_hp_now >= 1 or urban_wybrany == 1 and urban_hp_now >= 1 or zyd_wybrany == 1 and zyd_hp_now >= 1 or kazuma_wybrany == 1 and kazuma_hp_now >= 1 or tarczownik_wybrany == 1 and tarczownik_hp_now >= 1:
                            show air_strike_shield1 zorder 18 at tarcza_sojusznik1 

                        if luszcz_wybrany == 2 and luszcz_hp_now >= 1 or eminem_wybrany == 2 and eminem_hp_now >= 1 or urban_wybrany == 2 and urban_hp_now >= 1 or zyd_wybrany == 2 and zyd_hp_now >= 1 or kazuma_wybrany == 2 and kazuma_hp_now >= 1 or tarczownik_wybrany == 2 and tarczownik_hp_now >= 1:
                            show air_strike_shield2 zorder 18 at tarcza_sojusznik2 
                        
                        if luszcz_wybrany == 3 and luszcz_hp_now >= 1 or eminem_wybrany == 3 and eminem_hp_now >= 1 or urban_wybrany == 3 and urban_hp_now >= 1 or zyd_wybrany == 3 and zyd_hp_now >= 1 or kazuma_wybrany == 3 and kazuma_hp_now >= 1 or tarczownik_wybrany == 3 and tarczownik_hp_now >= 1:
                            show air_strike_shield3 zorder 18 at tarcza_sojusznik3 

                        tarczownik "Air Strike Shield!l"

                        if dialog_fight2 == 0:
                            $ dialog_fight2 += 1

                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                            luszcz "..."
                        
                        else:
                            if dialog_fight2 == 1:
                                $ dialog_fight2 += 1
                                luszcz "Ja jebie co za debil"
                            
                            else:
                                if dialog_fight2 == 2:
                                    $ dialog_fight2 += 1
                                    luszcz "Zajębię tego huja zaraz"
                            
                                else:
                                    if dialog_fight2 >= 3:
                                        $ dialog_fight2 += 1
                                        luszcz "..."



                        jump faza12
                
                if tarczownik_hp_now <= 5 and tarczownik_weapon >= 1:
                    $ kostka = renpy.random.randint(1, 2)

                    if kostka == 1:
                        $ tarczownik_obrona += 2
                        play sound "audio/sfx/shield_prison.mp3"
                        if tarczownik_wybrany == 1:
                            show shield_prison zorder 18 at prison_sojusznik1

                        if tarczownik_wybrany == 2:
                            show shield_prison zorder 18 at prison_sojusznik2  

                        if tarczownik_wybrany == 3:
                            show shield_prison zorder 18 at prison_sojusznik3 

                        tarczownik "Shield Prison!"

                        if dialog_fight2 == 0:
                            $ dialog_fight2 += 1

                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                            luszcz "..."
                        
                        else:
                            if dialog_fight2 == 1:
                                $ dialog_fight2 += 1
                                luszcz "Ja jebie co za debil"
                            
                            else:
                                if dialog_fight2 == 2:
                                    $ dialog_fight2 += 1
                                    luszcz "Zajębię tego huja zaraz"
                            
                                else:
                                    if dialog_fight2 >= 3:
                                        $ dialog_fight2 += 1
                                        luszcz "..."



                        jump faza12
                
                $ kostka = renpy.random.randint(1, 10)

                if kostka == 10 and tarczownik_weapon >= 1:
                    $ luszcz_obrona += 1
                    $ eminem_obrona += 1
                    $ urban_obrona += 1
                    $ zyd_obrona += 1
                    $ kazuma_obrona += 1
                    $ tarczownik_obrona += 1
                    play sound "audio/sfx/air_strike_shield.mp3"

                    if luszcz_wybrany == 1 and luszcz_hp_now >= 1 or eminem_wybrany == 1 and eminem_hp_now >= 1 or urban_wybrany == 1 and urban_hp_now >= 1 or zyd_wybrany == 1 and zyd_hp_now >= 1 or kazuma_wybrany == 1 and kazuma_hp_now >= 1 or tarczownik_wybrany == 1 and tarczownik_hp_now >= 1:
                        show air_strike_shield1 zorder 18 at tarcza_sojusznik1 

                    if luszcz_wybrany == 2 and luszcz_hp_now >= 1 or eminem_wybrany == 2 and eminem_hp_now >= 1 or urban_wybrany == 2 and urban_hp_now >= 1 or zyd_wybrany == 2 and zyd_hp_now >= 1 or kazuma_wybrany == 2 and kazuma_hp_now >= 1 or tarczownik_wybrany == 2 and tarczownik_hp_now >= 1:
                        show air_strike_shield2 zorder 18 at tarcza_sojusznik2 
                        
                    if luszcz_wybrany == 3 and luszcz_hp_now >= 1 or eminem_wybrany == 3 and eminem_hp_now >= 1 or urban_wybrany == 3 and urban_hp_now >= 1 or zyd_wybrany == 3 and zyd_hp_now >= 1 or kazuma_wybrany == 3 and kazuma_hp_now >= 1 or tarczownik_wybrany == 3 and tarczownik_hp_now >= 1:
                        show air_strike_shield3 zorder 18 at tarcza_sojusznik3 

                    tarczownik "Air Strike Shield!"

                    if dialog_fight2 == 0:
                            $ dialog_fight2 += 1

                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                            luszcz "..."
                    
                    else:
                        if dialog_fight2 == 1:
                            $ dialog_fight2 += 1
                            luszcz "Ja jebie co za debil"
                            
                        else:
                            if dialog_fight2 == 2:
                                $ dialog_fight2 += 1
                                luszcz "Zajębię tego huja zaraz"
                            
                            else:
                                if dialog_fight2 >= 3:
                                    $ dialog_fight2 += 1
                                    luszcz "..."


                    jump faza12
                
                if tarczownik_weapon >= 1:
                    if tarczownik_wybrany == 1:
                        if legendary_shield == 6:
                            show tarczownik_weapon zorder 15 at weapon_sojusznik1  

                        if tarczownik_przepychaczka == 6:
                            show tarczownik_przepychaczka zorder 15 at weapon_sojusznik1  

                        if stop == 6:
                            show stop zorder 15 at weapon_sojusznik1  
                            
                        if miecz_swietlny == 6:
                            show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                        if ostrza_chaosu == 6:
                            show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                        if patyk == 6:
                            show patyk zorder 15 at weapon_sojusznik1  

                        if bazooka == 6:
                            show bazooka zorder 15 at weapon_sojusznik1  
                            
                        if miecz3d == 6:
                            show miecz3d zorder 15 at weapon_sojusznik1  

                    if tarczownik_wybrany == 2:
                        if legendary_shield == 6:
                            show tarczownik_weapon zorder 15 at weapon_sojusznik2  

                        if tarczownik_przepychaczka == 6:
                            show tarczownik_przepychaczka zorder 15 at weapon_sojusznik2  

                        if stop == 6:
                            show stop zorder 15 at weapon_sojusznik2 
                            
                        if miecz_swietlny == 6:
                            show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                        if ostrza_chaosu == 6:
                            show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                        if patyk == 6:
                            show patyk zorder 15 at weapon_sojusznik2  

                        if bazooka == 6:
                            show bazooka zorder 15 at weapon_sojusznik2  
                            
                        if miecz3d == 6:
                            show miecz3d zorder 15 at weapon_sojusznik2   

                    if tarczownik_wybrany == 3:
                        if legendary_shield == 6:
                            show tarczownik_weapon zorder 15 at weapon_sojusznik3 

                        if tarczownik_przepychaczka == 6:
                            show tarczownik_przepychaczka zorder 15 at weapon_sojusznik3  

                        if stop == 6:
                            show stop zorder 15 at weapon_sojusznik3  
                            
                        if miecz_swietlny == 6:
                            show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                        if ostrza_chaosu == 6:
                            show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                        if patyk == 6:
                            show patyk zorder 15 at weapon_sojusznik3  

                        if bazooka == 6:
                            show bazooka zorder 15 at weapon_sojusznik3  
                            
                        if miecz3d == 6:
                            show miecz3d zorder 15 at weapon_sojusznik3  

                else:
                    if tarczownik_wybrany == 1:
                        show reka9 zorder 15 at weapon_sojusznik1 

                    if tarczownik_wybrany == 2:
                        show reka9 zorder 15 at weapon_sojusznik2  

                    if tarczownik_wybrany == 3:
                        show reka9 zorder 15 at weapon_sojusznik3 

                if ostrza_chaosu == 6 and tarczownik_weapon >= 1:
                    if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                        $ tarczownik_min_attack_now += 1
                        
                    tarczownik "Aaaaaaaaagh!"
                    
                    $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                    if kibol1_hp_now >= 1:
                        if kibol1_obrona >= 2:
                            if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Naofumiego został zablokowany{/i}"
                            $ kibol1_obrona = 1
                                                                
                        else:     
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(tarczownik_attack / 2)

                                $ dmg = int(tarczownik_attack / 2)
                            else:
                                $ kibol1_hp_now -= tarczownik_attack
                        
                    if akane_hp_now >= 1:
                        if akane_obrona >= 2:
                            if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Naofumiego został zablokowany{/i}"
                            $ akane_obrona = 1
                                                                
                        else:     
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(tarczownik_attack / 2)

                                $ dmg = int(tarczownik_attack / 2)
                            else:
                                $ akane_hp_now -= tarczownik_attack

                    if kibol2_hp_now >= 1:
                        if kibol2_obrona >= 2:
                            if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Naofumiego został zablokowany{/i}"
                            $ kibol2_obrona = 1
                                                                
                        else:     
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(tarczownik_attack / 2)

                                $ dmg = int(tarczownik_attack / 2)
                            else:
                                $ kibol2_hp_now -= tarczownik_attack
                        
                    if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                        play sound "audio/sfx/ostrza_chaosu.mp3"
                        "{i}Atak zadał [tarczownik_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                    else:
                        play sound "audio/sfx/obrona.mp3"
                        "{i}Atak Naofumiego został zablokowany{/i}"

                    jump faza12
                
                tarczownik "Aaaaaaaaagh!"

                label losowanko_tarczownik1:
                    $ kostka = renpy.random.randint(1, 3)
                    if kostka == 1:
                        if kibol1_hp_now >= 1:
                            if kibol1_hp_now <= 3:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 2:
                                    $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                    if kibol1_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Naofumiego został zablokowany{/i}"
                                        $ kibol1_obrona = 1
                                                            
                                    else:
                                        if tarczownik_weapon >= 1:
                                            if legendary_shield == 6:
                                                play sound "audio/sfx/legendary_shield.mp3" 

                                            if tarczownik_przepychaczka == 6: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 6:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 6:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 6:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 6:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 6:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol1_obrona == 1:
                                            if patyk == 6:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= tarczownik_attack
                                                    "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                
                                                else:
                                                    $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                    $ dmg = int(tarczownik_attack / 2)
                                                    "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"
                                            else:
                                                $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                $ dmg = int(tarczownik_attack / 2)
                                                "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"

                                        else:
                                            if bazooka == 6:
                                                $ kibol1_poison = 3
                                                show snake31 zorder 15 at center_wrog1
                                            
                                            if patyk == 6:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= tarczownik_attack * 2
                                                    "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                
                                                else:
                                                    $ kibol1_hp_now -= tarczownik_attack
                                                    "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                            else:
                                                $ kibol1_hp_now -= tarczownik_attack
                                                if tarczownik_przepychaczka == 6 and kibol1_stun == 0:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        show stun1 zorder 15 at head_wrog1
                                                        $ kibol1_stun = 1
                                                        "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    
                                                    else:
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                                
                                                else:
                                                    "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"

                                    
                                    if dialog_fight2 == 0:
                                        $ dialog_fight2 += 1

                                        luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                        tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                        tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                        luszcz "..."
                                    
                                    else:
                                        if dialog_fight2 == 1:
                                            $ dialog_fight2 += 1
                                            luszcz "Ja jebie co za debil"
                                        
                                        else:
                                            if dialog_fight2 == 2:
                                                $ dialog_fight2 += 1
                                                luszcz "Zajębię tego huja zaraz"
                                        
                                            else:
                                                if dialog_fight2 >= 3:
                                                    $ dialog_fight2 += 1
                                                    luszcz "..."

                                    jump faza12
                                else:
                                    jump losowanko_tarczownik1

                            else:
                                if kibol1_hp_now <= 10:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 3:
                                        $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                        if kibol1_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Naofumiego został zablokowany{/i}"
                                            $ kibol1_obrona = 1
                                                                
                                        else:
                                            if tarczownik_weapon >= 1:
                                                if legendary_shield == 6:
                                                    play sound "audio/sfx/legendary_shield.mp3" 

                                                if tarczownik_przepychaczka == 6: 
                                                    play sound "audio/sfx/przepychaczka.mp3" 

                                                if stop == 6:
                                                    play sound "audio/sfx/stop.mp3" 

                                                if miecz_swietlny == 6:
                                                    play sound "audio/sfx/miecz_swietlny.mp3" 
                                                
                                                if patyk == 6:
                                                    play sound "audio/sfx/patyk.mp3" 
                                                
                                                if bazooka == 6:
                                                    play sound "audio/sfx/bazooka.mp3" 
                                                
                                                if miecz3d == 6:
                                                    play sound "audio/sfx/miecz3d.mp3" 

                                            else:
                                                play sound "audio/sfx/reka.mp3" 
                                            if kibol1_obrona == 1:
                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ kibol1_hp_now -= tarczownik_attack
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                    
                                                    else:
                                                        $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"
                                                else:
                                                    $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                    $ dmg = int(tarczownik_attack / 2)
                                                    "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"
                                            else:
                                                if bazooka == 6:
                                                    $ kibol1_poison = 3
                                                    show snake31 zorder 15 at center_wrog1
                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ kibol1_hp_now -= tarczownik_attack * 2
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                    
                                                    else:
                                                        $ kibol1_hp_now -= tarczownik_attack
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                                else:
                                                    $ kibol1_hp_now -= tarczownik_attack
                                                    if tarczownik_przepychaczka == 6 and kibol1_stun == 0:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            show stun1 zorder 15 at head_wrog1
                                                            $ kibol1_stun = 1
                                                            "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                                    
                                                    else:
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                        
                                        if dialog_fight2 == 0:
                                            $ dialog_fight2 += 1

                                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                            luszcz "..."
                                        
                                        else:
                                            if dialog_fight2 == 1:
                                                $ dialog_fight2 += 1
                                                luszcz "Ja jebie co za debil"
                                            
                                            else:
                                                if dialog_fight2 == 2:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Zajębię tego huja zaraz"
                                            
                                                else:
                                                    if dialog_fight2 >= 3:
                                                        $ dialog_fight2 += 1
                                                        luszcz "..."

                                        jump faza12
                                    else:
                                        jump losowanko_tarczownik1
                                
                                else:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 5:
                                        $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                        if kibol1_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Naofumiego został zablokowany{/i}"
                                            $ kibol1_obrona = 1
                                                                
                                        else:
                                            if tarczownik_weapon >= 1:
                                                if legendary_shield == 6:
                                                    play sound "audio/sfx/legendary_shield.mp3" 

                                                if tarczownik_przepychaczka == 6: 
                                                    play sound "audio/sfx/przepychaczka.mp3" 

                                                if stop == 6:
                                                    play sound "audio/sfx/stop.mp3" 

                                                if miecz_swietlny == 6:
                                                    play sound "audio/sfx/miecz_swietlny.mp3" 
                                                
                                                if patyk == 6:
                                                    play sound "audio/sfx/patyk.mp3" 
                                                
                                                if bazooka == 6:
                                                    play sound "audio/sfx/bazooka.mp3" 
                                                
                                                if miecz3d == 6:
                                                    play sound "audio/sfx/miecz3d.mp3" 

                                            else:
                                                play sound "audio/sfx/reka.mp3" 
                                            if kibol1_obrona == 1:
                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ kibol1_hp_now -= tarczownik_attack
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                    
                                                    else:
                                                        $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"
                                                else:
                                                    $ kibol1_hp_now -= int(tarczownik_attack / 2)
                                                    $ dmg = int(tarczownik_attack / 2)
                                                    "{i}Naofumi zadaje [dmg] obrażeń Kibol 1{/i}"
                                            else:
                                                if bazooka == 6:
                                                    $ kibol1_poison = 3
                                                    show snake31 zorder 15 at center_wrog1

                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ kibol1_hp_now -= tarczownik_attack * 2
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                    
                                                    else:
                                                        $ kibol1_hp_now -= tarczownik_attack
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                                else:
                                                    $ kibol1_hp_now -= tarczownik_attack
                                                    if tarczownik_przepychaczka == 6 and kibol1_stun == 0:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            show stun1 zorder 15 at head_wrog1
                                                            $ kibol1_stun = 1
                                                            "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                                    
                                                    else:
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 1{/i}"
                                        
                                        if dialog_fight2 == 0:
                                            $ dialog_fight2 += 1

                                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                            luszcz "..."
                                        
                                        else:
                                            if dialog_fight2 == 1:
                                                $ dialog_fight2 += 1
                                                luszcz "Ja jebie co za debil"
                                            
                                            else:
                                                if dialog_fight2 == 2:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Zajębię tego huja zaraz"
                                            
                                                else:
                                                    if dialog_fight2 >= 3:
                                                        $ dialog_fight2 += 1
                                                        luszcz "..."

                                        jump faza12
                                    else:
                                        jump losowanko_tarczownik1

                        else:
                            jump losowanko_tarczownik1
                    else:
                        if kostka == 2:
                            if akane_hp_now >= 1:
                                if akane_hp_now <= 3:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 2:
                                        $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                        if akane_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Naofumiego został zablokowany{/i}"
                                            $ akane_obrona = 1
                                                                    
                                        else:
                                            if tarczownik_weapon >= 1:
                                                if legendary_shield == 6:
                                                    play sound "audio/sfx/legendary_shield.mp3" 

                                                if tarczownik_przepychaczka == 6: 
                                                    play sound "audio/sfx/przepychaczka.mp3" 

                                                if stop == 6:
                                                    play sound "audio/sfx/stop.mp3" 

                                                if miecz_swietlny == 6:
                                                    play sound "audio/sfx/miecz_swietlny.mp3" 
                                                
                                                if patyk == 6:
                                                    play sound "audio/sfx/patyk.mp3" 
                                                
                                                if bazooka == 6:
                                                    play sound "audio/sfx/bazooka.mp3" 
                                                
                                                if miecz3d == 6:
                                                    play sound "audio/sfx/miecz3d.mp3" 

                                            else:
                                                play sound "audio/sfx/reka.mp3" 
                                            if akane_obrona == 1:
                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ akane_hp_now -= tarczownik_attack
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                        
                                                    else:
                                                        $ akane_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                                else:
                                                    $ akane_hp_now -= int(tarczownik_attack / 2)
                                                    $ dmg = int(tarczownik_attack / 2)
                                                    "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                            else:
                                                if bazooka == 6:
                                                    $ akane_poison = 3
                                                    show snake32 zorder 15 at center_wrog3

                                                if patyk == 6:
                                                    $ kostka = renpy.random.randint(1, 3)
                                                    if kostka == 3:
                                                        $ akane_hp_now -= tarczownik_attack * 2
                                                        "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                    
                                                    else:
                                                        $ akane_hp_now -= tarczownik_attack
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                else:
                                                    $ akane_hp_now -= tarczownik_attack
                                                    if tarczownik_przepychaczka == 6 and akane_stun == 0:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            show stun2 zorder 15 at head_wrog3
                                                            $ akane_stun = 1
                                                            "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                    
                                                    else:
                                                        "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                            
                                        if dialog_fight2 == 0:
                                            $ dialog_fight2 += 1

                                            luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                            tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                            tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                            luszcz "..."
                                        
                                        else:
                                            if dialog_fight2 == 1:
                                                $ dialog_fight2 += 1
                                                luszcz "Ja jebie co za debil"
                                            
                                            else:
                                                if dialog_fight2 == 2:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Zajębię tego huja zaraz"
                                            
                                                else:
                                                    if dialog_fight2 >= 3:
                                                        $ dialog_fight2 += 1
                                                        luszcz "..."

                                        jump faza12
                                    else:
                                        jump losowanko_tarczownik1

                                else:
                                    if akane_hp_now <= 10:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 3:
                                            $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                            if akane_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Naofumiego został zablokowany{/i}"
                                                $ akane_obrona = 1
                                                                        
                                            else:
                                                if tarczownik_weapon >= 1:
                                                    if legendary_shield == 6:
                                                        play sound "audio/sfx/legendary_shield.mp3" 

                                                    if tarczownik_przepychaczka == 6: 
                                                        play sound "audio/sfx/przepychaczka.mp3" 

                                                    if stop == 6:
                                                        play sound "audio/sfx/stop.mp3" 

                                                    if miecz_swietlny == 6:
                                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                                    
                                                    if patyk == 6:
                                                        play sound "audio/sfx/patyk.mp3" 
                                                    
                                                    if bazooka == 6:
                                                        play sound "audio/sfx/bazooka.mp3" 
                                                    
                                                    if miecz3d == 6:
                                                        play sound "audio/sfx/miecz3d.mp3" 

                                                else:
                                                    play sound "audio/sfx/reka.mp3" 

                                                if akane_obrona == 1:
                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ akane_hp_now -= tarczownik_attack
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ akane_hp_now -= int(tarczownik_attack / 2)
                                                            $ dmg = int(tarczownik_attack / 2)
                                                            "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                                    else:
                                                        $ akane_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                                else:
                                                    if bazooka == 6:
                                                        $ akane_poison = 3
                                                        show snake32 zorder 15 at center_wrog3

                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ akane_hp_now -= tarczownik_attack * 2
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ akane_hp_now -= tarczownik_attack
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                    else:
                                                        $ akane_hp_now -= tarczownik_attack
                                                        if tarczownik_przepychaczka == 6 and akane_stun == 0:
                                                            $ kostka = renpy.random.randint(1, 20)
                                                            if kostka <= 3:
                                                                show stun2 zorder 15 at head_wrog3
                                                                $ akane_stun = 1
                                                                "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                            
                                                            else:
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                            
                                            if dialog_fight2 == 0:
                                                $ dialog_fight2 += 1

                                                luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                                tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                                tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                                luszcz "..."
                                            
                                            else:
                                                if dialog_fight2 == 1:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Ja jebie co za debil"
                                                
                                                else:
                                                    if dialog_fight2 == 2:
                                                        $ dialog_fight2 += 1
                                                        luszcz "Zajębię tego huja zaraz"
                                                
                                                    else:
                                                        if dialog_fight2 >= 3:
                                                            $ dialog_fight2 += 1
                                                            luszcz "..."

                                            jump faza12
                                        else:
                                            jump losowanko_tarczownik1
                                    
                                    else:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 5:
                                            $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                            if akane_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Naofumiego został zablokowany{/i}"
                                                $ akane_obrona = 1
                                                                        
                                            else:
                                                if tarczownik_weapon >= 1:
                                                    if legendary_shield == 6:
                                                        play sound "audio/sfx/legendary_shield.mp3" 

                                                    if tarczownik_przepychaczka == 6: 
                                                        play sound "audio/sfx/przepychaczka.mp3" 

                                                    if stop == 6:
                                                        play sound "audio/sfx/stop.mp3" 

                                                    if miecz_swietlny == 6:
                                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                                    
                                                    if patyk == 6:
                                                        play sound "audio/sfx/patyk.mp3" 
                                                    
                                                    if bazooka == 6:
                                                        play sound "audio/sfx/bazooka.mp3" 
                                                    
                                                    if miecz3d == 6:
                                                        play sound "audio/sfx/miecz3d.mp3" 

                                                else:
                                                    play sound "audio/sfx/reka.mp3" 

                                                if akane_obrona == 1:
                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ akane_hp_now -= tarczownik_attack
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ akane_hp_now -= int(tarczownik_attack / 2)
                                                            $ dmg = int(tarczownik_attack / 2)
                                                            "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                                    else:
                                                        $ akane_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Akane{/i}"
                                                else:
                                                    if bazooka == 6:
                                                        $ akane_poison = 3
                                                        show snake32 zorder 15 at center_wrog3

                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ akane_hp_now -= tarczownik_attack * 2
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ akane_hp_now -= tarczownik_attack
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                    else:
                                                        $ akane_hp_now -= tarczownik_attack
                                                        if tarczownik_przepychaczka == 6 and akane_stun == 0:
                                                            $ kostka = renpy.random.randint(1, 20)
                                                            if kostka <= 3:
                                                                show stun2 zorder 15 at head_wrog3
                                                                $ akane_stun = 1
                                                                "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                            
                                                            else:
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Akane{/i}"
                                                

                                            if dialog_fight2 == 0:
                                                $ dialog_fight2 += 1

                                                luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                                tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                                tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                                luszcz "..."
                                            
                                            else:
                                                if dialog_fight2 == 1:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Ja jebie co za debil"
                                                
                                                else:
                                                    if dialog_fight2 == 2:
                                                        $ dialog_fight2 += 1
                                                        luszcz "Zajębię tego huja zaraz"
                                                
                                                    else:
                                                        if dialog_fight2 >= 3:
                                                            $ dialog_fight2 += 1
                                                            luszcz "..."

                                            jump faza12
                                        else:
                                            jump losowanko_tarczownik1

                            else:
                                jump losowanko_tarczownik1
                        else:
                            if kostka == 3:
                                if kibol2_hp_now >= 1:
                                    if kibol2_hp_now <= 3:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 2:
                                            $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                            if kibol2_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Naofumiego został zablokowany{/i}"
                                                $ kibol2_obrona = 1
                                                                    
                                            else:
                                                if tarczownik_weapon >= 1:
                                                    if legendary_shield == 6:
                                                        play sound "audio/sfx/legendary_shield.mp3" 

                                                    if tarczownik_przepychaczka == 6: 
                                                        play sound "audio/sfx/przepychaczka.mp3" 

                                                    if stop == 6:
                                                        play sound "audio/sfx/stop.mp3" 

                                                    if miecz_swietlny == 6:
                                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                                    
                                                    if patyk == 6:
                                                        play sound "audio/sfx/patyk.mp3" 
                                                    
                                                    if bazooka == 6:
                                                        play sound "audio/sfx/bazooka.mp3" 
                                                    
                                                    if miecz3d == 6:
                                                        play sound "audio/sfx/miecz3d.mp3" 

                                                else:
                                                    play sound "audio/sfx/reka.mp3" 

                                                if kibol2_obrona == 1:
                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ kibol2_hp_now -= tarczownik_attack
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                            $ dmg = int(tarczownik_attack / 2)
                                                            "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                    else:
                                                        $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                        $ dmg = int(tarczownik_attack / 2)
                                                        "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                else:
                                                    if bazooka == 6:
                                                        $ kibol2_poison = 3
                                                        show snake33 zorder 15 at center_wrog2

                                                    if patyk == 6:
                                                        $ kostka = renpy.random.randint(1, 3)
                                                        if kostka == 3:
                                                            $ kibol2_hp_now -= tarczownik_attack * 2
                                                            "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                        
                                                        else:
                                                            $ kibol2_hp_now -= tarczownik_attack
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                    else:
                                                        $ kibol2_hp_now -= tarczownik_attack
                                                        if tarczownik_przepychaczka == 6 and kibol2_stun == 0:
                                                            $ kostka = renpy.random.randint(1, 20)
                                                            if kostka <= 3:
                                                                show stun3 zorder 15 at head_wrog2
                                                                $ kibol2_stun = 1
                                                                "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                            
                                                            else:
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                        
                                                        else:
                                                            "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                            
                                            if dialog_fight2 == 0:
                                                $ dialog_fight2 += 1

                                                luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                                tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                                tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                                luszcz "..."
                                            
                                            else:
                                                if dialog_fight2 == 1:
                                                    $ dialog_fight2 += 1
                                                    luszcz "Ja jebie co za debil"
                                                
                                                else:
                                                    if dialog_fight2 == 2:
                                                        $ dialog_fight2 += 1
                                                        luszcz "Zajębię tego huja zaraz"
                                                
                                                    else:
                                                        if dialog_fight2 >= 3:
                                                            $ dialog_fight2 += 1
                                                            luszcz "..."

                                            jump faza12
                                        else:
                                            jump losowanko_tarczownik1

                                    else:
                                        if kibol2_hp_now <= 10:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 3:
                                                $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                                if kibol2_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Naofumiego został zablokowany{/i}"
                                                    $ kibol2_obrona = 1
                                                                        
                                                else:
                                                    if tarczownik_weapon >= 1:
                                                        if legendary_shield == 6:
                                                            play sound "audio/sfx/legendary_shield.mp3" 

                                                        if tarczownik_przepychaczka == 6: 
                                                            play sound "audio/sfx/przepychaczka.mp3" 

                                                        if stop == 6:
                                                            play sound "audio/sfx/stop.mp3" 

                                                        if miecz_swietlny == 6:
                                                            play sound "audio/sfx/miecz_swietlny.mp3" 
                                                        
                                                        if patyk == 6:
                                                            play sound "audio/sfx/patyk.mp3" 
                                                        
                                                        if bazooka == 6:
                                                            play sound "audio/sfx/bazooka.mp3" 
                                                        
                                                        if miecz3d == 6:
                                                            play sound "audio/sfx/miecz3d.mp3" 

                                                    else:
                                                        play sound "audio/sfx/reka.mp3" 

                                                    if kibol2_obrona == 1:
                                                        if patyk == 6:
                                                            $ kostka = renpy.random.randint(1, 3)
                                                            if kostka == 3:
                                                                $ kibol2_hp_now -= tarczownik_attack
                                                                "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                            
                                                            else:
                                                                $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                                $ dmg = int(tarczownik_attack / 2)
                                                                "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                        else:
                                                            $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                            $ dmg = int(tarczownik_attack / 2)
                                                            "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                    else:
                                                        if bazooka == 6:
                                                            $ kibol2_poison = 3
                                                            show snake33 zorder 15 at center_wrog2

                                                        if patyk == 6:
                                                            $ kostka = renpy.random.randint(1, 3)
                                                            if kostka == 3:
                                                                $ kibol2_hp_now -= tarczownik_attack * 2
                                                                "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                            
                                                            else:
                                                                $ kibol2_hp_now -= tarczownik_attack
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                        else:
                                                            $ kibol2_hp_now -= tarczownik_attack
                                                            if tarczownik_przepychaczka == 6 and kibol2_stun == 0:
                                                                $ kostka = renpy.random.randint(1, 20)
                                                                if kostka <= 3:
                                                                    show stun3 zorder 15 at head_wrog2
                                                                    $ kibol2_stun = 1
                                                                    "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                                
                                                                else:
                                                                    "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                            
                                                            else:
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                
                                                if dialog_fight2 == 0:
                                                    $ dialog_fight2 += 1

                                                    luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                                    tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                                    tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                                    luszcz "..."
                                                
                                                else:
                                                    if dialog_fight2 == 1:
                                                        $ dialog_fight2 += 1
                                                        luszcz "Ja jebie co za debil"
                                                    
                                                    else:
                                                        if dialog_fight2 == 2:
                                                            $ dialog_fight2 += 1
                                                            luszcz "Zajębię tego huja zaraz"
                                                    
                                                        else:
                                                            if dialog_fight2 >= 3:
                                                                $ dialog_fight2 += 1
                                                                luszcz "..."

                                                jump faza12
                                            else:
                                                jump losowanko_tarczownik1
                                        
                                        else:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 5:
                                                $ tarczownik_attack = renpy.random.randint(tarczownik_min_attack_now, tarczownik_max_attack_now)

                                                if kibol2_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Naofumiego został zablokowany{/i}"
                                                    $ kibol2_obrona = 1
                                                                        
                                                else:
                                                    if tarczownik_weapon >= 1:
                                                        if legendary_shield == 6:
                                                            play sound "audio/sfx/legendary_shield.mp3" 

                                                        if tarczownik_przepychaczka == 6: 
                                                            play sound "audio/sfx/przepychaczka.mp3" 

                                                        if stop == 6:
                                                            play sound "audio/sfx/stop.mp3" 

                                                        if miecz_swietlny == 6:
                                                            play sound "audio/sfx/miecz_swietlny.mp3" 
                                                        
                                                        if patyk == 6:
                                                            play sound "audio/sfx/patyk.mp3" 
                                                        
                                                        if bazooka == 6:
                                                            play sound "audio/sfx/bazooka.mp3" 
                                                        
                                                        if miecz3d == 6:
                                                            play sound "audio/sfx/miecz3d.mp3" 

                                                    else:
                                                        play sound "audio/sfx/reka.mp3" 

                                                    if kibol2_obrona == 1:
                                                        if patyk == 6:
                                                            $ kostka = renpy.random.randint(1, 3)
                                                            if kostka == 3:
                                                                $ kibol2_hp_now -= tarczownik_attack
                                                                "{i}Atak został podwojony i zadał [tarczownik_attack] obrażeń{/i}"
                                                            
                                                            else:
                                                                $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                                $ dmg = int(tarczownik_attack / 2)
                                                                "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                        else:
                                                            $ kibol2_hp_now -= int(tarczownik_attack / 2)
                                                            $ dmg = int(tarczownik_attack / 2)
                                                            "{i}Naofumi zadaje [dmg] obrażeń Kibol 2{/i}"
                                                    else:
                                                        if bazooka == 6:
                                                            $ kibol2_poison = 3
                                                            show snake33 zorder 15 at center_wrog2

                                                        if patyk == 6:
                                                            $ kostka = renpy.random.randint(1, 3)
                                                            if kostka == 3:
                                                                $ kibol2_hp_now -= tarczownik_attack * 2
                                                                "{i}Atak został podwojony i zadał [tarczownik_attack * 2] obrażeń{/i}"
                                                            
                                                            else:
                                                                $ kibol2_hp_now -= tarczownik_attack
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                        else:
                                                            $ kibol2_hp_now -= tarczownik_attack
                                                            if tarczownik_przepychaczka == 6 and kibol2_stun == 0:
                                                                $ kostka = renpy.random.randint(1, 20)
                                                                if kostka <= 3:
                                                                    show stun3 zorder 15 at head_wrog2
                                                                    $ kibol2_stun = 1
                                                                    "{i}Atak zadał [tarczownik_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                                
                                                                else:
                                                                    "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                            
                                                            else:
                                                                "{i}Naofumi zadaje [tarczownik_attack] obrażeń Kibol 2{/i}"
                                                

                                                if dialog_fight2 == 0:
                                                    $ dialog_fight2 += 1

                                                    luszcz "Ej co ty odpierdalasz? To ja tutaj dowodzę i masz się mnie słuchać"

                                                    tarczownik "Wal się na ryj, ty to co najwyżej możesz mi buty wylizać"
                                                    tarczownik "Pewnie też mnie zdradzisz CO?. Całe pierdolone życie w kłamstwie!"
                                                    luszcz "..."
                                                
                                                else:
                                                    if dialog_fight2 == 1:
                                                        $ dialog_fight2 += 1
                                                        luszcz "Ja jebie co za debil"
                                                    
                                                    else:
                                                        if dialog_fight2 == 2:
                                                            $ dialog_fight2 += 1
                                                            luszcz "Zajębię tego huja zaraz"
                                                    
                                                        else:
                                                            if dialog_fight2 >= 3:
                                                                $ dialog_fight2 += 1
                                                                luszcz "..."

                                                jump faza12
                                            else:
                                                jump losowanko_tarczownik1

                                else:
                                    jump losowanko_tarczownik1
                            else:
                                jump losowanko_tarczownik1

    label faza12:
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide ruch

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0
        
        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        
        if miecz3d == 2 and luszcz_hp_now <= luszcz_hp / 2 and luszcz_fighter == 2:
            $ luszcz_min_attack_now += 1
            $ luszcz_max_attack_now += 2
        
        if miecz3d == 3 and urban_hp_now <= urban_hp / 2 and urban_fighter == 2:
            $ urban_min_attack_now += 1
            $ urban_max_attack_now += 2
        
        if miecz3d == 4 and zyd_hp_now <= zyd_hp / 2 and zyd_fighter == 2:
            $ zyd_min_attack_now += 1
            $ zyd_max_attack_now += 2
        
        if miecz3d == 5 and kazuma_hp_now <= kazuma_hp / 2 and kazuma_fighter == 2:
            $ kazuma_min_attack_now += 1
            $ kazuma_max_attack_now += 2
        
        if miecz3d == 6 and tarczownik_hp_now <= tarczownik_hp / 2 and tarczownik_fighter == 2:
            $ tarczownik_min_attack_now += 1
            $ tarczownik_max_attack_now += 2

        if luszcz_fighter == 2:
            if luszcz_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if luszcz_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if luszcz_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 2 and luszcz_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ luszcz_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([luszcz_min_attack_now]-[luszcz_max_attack_now] DMG){/b}":
                    if luszcz_weapon >= 1:
                        if luszcz_wybrany == 1:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik1  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if luszcz_wybrany == 2:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik2  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if luszcz_wybrany == 3:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik3 

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik3  

                    else:
                        if luszcz_wybrany == 1:
                            show reka1 zorder 15 at weapon_sojusznik1 

                        if luszcz_wybrany == 2:
                            show reka1 zorder 15 at weapon_sojusznik2  

                        if luszcz_wybrany == 3:
                            show reka1 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 2 and luszcz_weapon >= 1:
                        luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                    
                        $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol1_hp_now -= luszcz_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ akane_hp_now -= luszcz_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol2_hp_now -= luszcz_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [luszcz_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Łuszcza został zablokowany{/i}"

                        jump faza13

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:  
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:  
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13

                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza13
                    
                "{b}Obrona{/b}" if luszcz_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if luszcz_wybrany == 1:
                        show tarcza1 zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show tarcza1 zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show tarcza1 zorder 15 at weapon_sojusznik3 

                    $ luszcz_obrona += 1
                    luszcz "I want sex"
                    jump faza13
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if luszcz_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    luszcz "Umiem wyobrażać sobie ludzi w stroju ziemniaka"
                    jump items12

                "{b}Zaparz Herbatę{/b}":
                    play sound "audio/sfx/herbaty.mp3"
                    if luszcz_wybrany == 1:
                        show herbaty zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show herbaty zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show herbaty zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Ale jaką?{/b}"

                        "{b}Wiśnia z Rumem (+5HP){/b}":
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                            menu:
                                "{b}Dla Kogo?{/b}"

                                "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    if luszcz_hp_now + 5 > luszcz_hp:
                                        $ luszcz_hp_now = luszcz_hp
                                        "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                    else:
                                        $ luszcz_hp_now += 5
                                        "{i}Łuszcz odzyskał 5 punktów życia{/i}"
                                
                                "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if eminem_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if eminem_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if eminem_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if eminem_hp_now + 5 > eminem_hp:
                                        $ eminem_hp_now = eminem_hp
                                        "{i}Shadow odzyskał cały pasek życia{/i}"
                                    else:
                                        $ eminem_hp_now += 5
                                        "{i}Shadow odzyskał 5 punktów życia{/i}"

                                "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if urban_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if urban_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if urban_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if urban_hp_now + 5 > urban_hp:
                                        $ urban_hp_now = urban_hp
                                        "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                    else:
                                        $ urban_hp_now += 5
                                        "{i}Jerzy Urban odzyskał 5 punktów życia{/i}"

                                "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if zyd_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if zyd_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if zyd_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if zyd_hp_now + 5 > zyd_hp:
                                        $ zyd_hp_now = zyd_hp
                                        "{i}Żyd odzyskał cały pasek życia{/i}"
                                    else:
                                        $ zyd_hp_now += 5
                                        "{i}Żyd odzyskał 5 punktów życia{/i}"

                                "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if kazuma_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if kazuma_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if kazuma_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if kazuma_hp_now + 5 > kazuma_hp:
                                        $ kazuma_hp_now = kazuma_hp
                                        "{i}Kazuma odzyskał cały pasek życia{/i}"
                                    else:
                                        $ kazuma_hp_now += 5
                                        "{i}Kazuma odzyskał 5 punktów życia{/i}"
                                
                                "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if tarczownik_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if tarczownik_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if tarczownik_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if tarczownik_hp_now + 5 > tarczownik_hp:
                                        $ tarczownik_hp_now = tarczownik_hp
                                        "{i}Naofumi odzyskał cały pasek życia{/i}"
                                    else:
                                        $ tarczownik_hp_now += 5
                                        "{i}Naofumi odzyskał 5 punktów życia{/i}"
                            
                            hide wisnia_w_rumie
                            jump faza13
                            
                        "{b}Hiszpańska Mandarynka (+2HP FOR ALL){/b}":
                            luszcz "Tak. Moja mama tylko czasami zagląda mi do buzi"
                            play sound "audio/sfx/herbata.mp3"
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                            if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                if luszcz_hp_now + 2 > luszcz_hp:
                                    $ luszcz_hp_now = luszcz_hp
                                else:
                                    $ luszcz_hp_now += 2
                            
                            if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                if eminem_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if eminem_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if eminem_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if eminem_hp_now + 2 > eminem_hp:
                                    $ eminem_hp_now = eminem_hp
                                else:
                                    $ eminem_hp_now += 2

                            if urban_hp_now >= 1 and urban_wybrany >= 1:
                                if urban_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if urban_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if urban_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if urban_hp_now + 2 > urban_hp:
                                    $ urban_hp_now = urban_hp
                                else:
                                    $ urban_hp_now += 2

                            if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                if zyd_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if zyd_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if zyd_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if zyd_hp_now + 2 > zyd_hp:
                                    $ zyd_hp_now = zyd_hp
                                else:
                                    $ zyd_hp_now += 2

                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if kazuma_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if kazuma_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if kazuma_hp_now + 2 > kazuma_hp:
                                    $ kazuma_hp_now = kazuma_hp
                                else:
                                    $ kazuma_hp_now += 2
                            
                            if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                if tarczownik_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if tarczownik_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if tarczownik_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if tarczownik_hp_now + 2 > tarczownik_hp:
                                    $ tarczownik_hp_now = tarczownik_hp
                                else:
                                    $ tarczownik_hp_now += 2

                            "{i}Wszyscy sojusznicy odzyskali po 2 punkty życia{/i}"
                            hide hiszpanska_mandarynka1
                            hide hiszpanska_mandarynka2
                            hide hiszpanska_mandarynka3
                            jump faza13
        
        if eminem_fighter == 2:
            if eminem_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if eminem_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if eminem_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([eminem_min_attack_now]-[eminem_max_attack_now] DMG){/b}":
                    if eminem_weapon >= 1:
                        if eminem_wybrany == 1:
                            show eminem_weapon zorder 15 at weapon_sojusznik1  

                        if eminem_wybrany == 2:
                            show eminem_weapon zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show eminem_weapon zorder 15 at weapon_sojusznik3 

                    else:
                        if eminem_wybrany == 1:
                            show reka2 zorder 15 at weapon_sojusznik1 

                        if eminem_wybrany == 2:
                            show reka2 zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show reka2 zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else: 
                                play sound "audio/sfx/reka.mp3"                             
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol1_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:  
                                play sound "audio/sfx/reka.mp3"                          
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ akane_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                play sound "audio/sfx/reka.mp3"
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol2_hp_now -= eminem_attack

                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza13
                    
                "{b}Obrona{/b}" if eminem_obrona == 0:
                    eminem "I am ..."
                    play sound "audio/sfx/shield.mp3"
                    if eminem_wybrany == 1:
                        show tarcza2 zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show tarcza2 zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show tarcza2 zorder 15 at weapon_sojusznik3 

                    $ eminem_obrona += 1
                    eminem "... rzymskim legionistą"
                    jump faza13
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if eminem_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    eminem "Czas zabawy się skończył"
                    jump items12

                "{b}Rzut Szlamem{/b}":
                    if eminem_wybrany == 1:
                        show slime zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show slime zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show slime zorder 15 at weapon_sojusznik3 
                    
                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 1 obronił się przed szlamem{/i}"
                                jump faza13
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol1_min_attack_now >= 2:
                                    $ kibol1_min_attack_now -= 2
                                    if kibol1_max_attack_now >= 6:
                                        $ kibol1_max_attack_now -= 3
                                    else:
                                        $ kibol1_max_attack_now -= 2
                        
                                else:
                                    $ kibol1_min_attack_now = 0

                                    if kibol1_max_attack_now >= 2:
                                        if kibol1_max_attack_now >= 6:
                                            $ kibol1_max_attack_now -= 3
                                        else:
                                            $ kibol1_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol1_max_attack_now = 0
                                
                                $ kibol1_slime += 1
                                show slime zorder 15 at center_wrog1 
                                "{i}Statystyki Kibol 1 zostały osłabione{/i}"
                                jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Akane obronił się przed szlamem{/i}"
                                jump faza13
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if akane_min_attack_now >= 2:
                                    $ akane_min_attack_now -= 2
                                    if akane_max_attack_now >= 6:
                                        $ akane_max_attack_now -= 3
                                    else:
                                        $ akane_max_attack_now -= 2
                        
                                else:
                                    $ akane_min_attack_now = 0

                                    if akane_max_attack_now >= 2:
                                        if akane_max_attack_now >= 6:
                                            $ akane_max_attack_now -= 3
                                        else:
                                            $ akane_max_attack_now -= 2
                                    
                                    else:
                                        $ akane_max_attack_now = 0

                                $ akane_slime += 1
                                show slime zorder 15 at center_wrog3 
                                "{i}Statystyki Akane zostały osłabione{/i}"
                                jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 2 obronił się przed szlamem{/i}"
                                jump faza13
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol2_min_attack_now >= 2:
                                    $ kibol2_min_attack_now -= 2
                                    if kibol2_max_attack_now >= 6:
                                        $ kibol2_max_attack_now -= 3
                                    else:
                                        $ kibol2_max_attack_now -= 2
                        
                                else:
                                    $ kibol2_min_attack_now = 0

                                    if kibol2_max_attack_now >= 2:
                                        if kibol2_max_attack_now >= 6:
                                            $ kibol2_max_attack_now -= 3
                                        else:
                                            $ kibol2_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol2_max_attack_now = 0
                                
                                $ kibol2_slime += 1
                                show slime zorder 15 at center_wrog2
                                "{i}Statystyki Kibol 2 zostały osłabione{/i}"
                                jump faza13

        if urban_fighter == 2:
            if urban_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if urban_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if urban_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 3 and urban_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ urban_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([urban_min_attack_now]-[urban_max_attack_now] DMG){/b}":
                    if urban_weapon >= 1:
                        if urban_wybrany == 1:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik1  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if urban_wybrany == 2:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik2  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if urban_wybrany == 3:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik3 

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if urban_wybrany == 1:
                            show reka3 zorder 15 at weapon_sojusznik1 

                        if urban_wybrany == 2:
                            show reka3 zorder 15 at weapon_sojusznik2  

                        if urban_wybrany == 3:
                            show reka3 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 3 and urban_weapon >= 1:                  
                        urban "i Ci kutasa obetnie"
                    
                        $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol1_hp_now -= urban_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ akane_hp_now -= urban_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol2_hp_now -= urban_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [urban_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Jerzego Urbana został zablokowany{/i}"

                        jump faza13

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban4:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol1_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol1_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol1_obrona == 1 and stop == 3 or urban_attack == 2 and kibol1_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban4
                                    
                                    else:  
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol1_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza13

                                            $ kibol1_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol1_poison = 3
                                                show snake31 zorder 15 at center_wrog1
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza13

                                            $ kibol1_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol1_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun1 zorder 15 at head_wrog1
                                                    $ kibol1_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza13
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban5:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if akane_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ akane_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and akane_obrona == 1 and stop == 3 or urban_attack == 2 and akane_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban5
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if akane_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza13

                                            $ akane_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ akane_poison = 3
                                                show snake32 zorder 15 at center_wrog3
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza13

                                            $ akane_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and akane_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun2 zorder 15 at head_wrog3
                                                    $ akane_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza13
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban6:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol2_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol2_obrona = 1
                                                                
                                else:  
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol2_obrona == 1 and stop == 3 or urban_attack == 2 and kibol2_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban6
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol2_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza13

                                            $ kibol2_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol2_poison = 3
                                                show snake33 zorder 15 at center_wrog2
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza13

                                            $ kibol2_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol2_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun3 zorder 15 at head_wrog2
                                                    $ kibol2_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza13

                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza13
                    
                "{b}Obrona{/b}" if urban_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if urban_wybrany == 1:
                        show tarcza3 zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show tarcza3 zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show tarcza3 zorder 15 at weapon_sojusznik3 

                    $ urban_obrona += 1
                    urban "A ja mam to w dupie"
                    jump faza13
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if urban_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    urban "No tak było, nie zmyślam"
                    jump items12

                "{b}Zatrzepocz Uszami{/b}":
                    if urban_wybrany == 1:
                        show uszy zorder 15 at head_sojusznik1  

                    if urban_wybrany == 2:
                        show uszy zorder 15 at head_sojusznik2  

                    if urban_wybrany == 3:
                        show uszy zorder 15 at head_sojusznik3 
                    
                    urban "Hhyyy pfff hhyyy pffff hhyyy"
                    play sound "audio/sfx/uszy.mp3" 

                    if kibol1_obrona <= 0:
                        $ kibol1_uszy += 1
                    
                    if akane_obrona <= 0:
                        $ akane_uszy += 1
                    
                    if kibol2_obrona <= 0:
                        $ kibol2_uszy += 1

                    if kibol1_uszy == 1 and akane_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                        show uszy2 zorder 15 at head_wrog3
                        show uszy1 zorder 15 at head_wrog1
                        show uszy3 zorder 15 at head_wrog2
                        "{i}Kibol 1, Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                    
                    else:
                        if kibol1_uszy == 1 and akane_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            show uszy2 zorder 15 at head_wrog3
                            show uszy1 zorder 15 at head_wrog1
                            "{i}Kibol 1 i Akane skupili się na uszach Urbana{/i}"
                        
                        else:
                            if akane_uszy == 1 and kibol2_uszy == 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                                show uszy2 zorder 15 at head_wrog3
                                show uszy3 zorder 15 at head_wrog2
                                "{i}Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                            
                            else:
                                if kibol1_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                                    show uszy3 zorder 15 at head_wrog2
                                    show uszy1 zorder 15 at head_wrog1
                                    "{i}Kibol 1 i Kibol 2 skupili się na uszach Urbana{/i}"
                                
                                else:
                                    if kibol1_uszy == 1 and kibol1_hp_now >= 1:
                                        show uszy1 zorder 15 at head_wrog1
                                        "{i}Kibol 1 skupił się na uszach Urbana{/i}"
                                    
                                    else:
                                        if akane_uszy == 1 and akane_hp_now >= 1:
                                            show uszy2 zorder 15 at head_wrog3
                                            "{i}Akane skupił się na uszach Urbana{/i}"

                                        else:
                                            if kibol2_uszy == 1 and kibol2_hp_now >= 1:
                                                show uszy3 zorder 15 at head_wrog2
                                                "{i}Kibol 2 skupił się na uszach Urbana{/i}"

                                            else:
                                                "{i}Niestety, ale uszy Urbana nie uwiodły nikogo{/i}"

                    hide uszy
                    jump faza13  

        if zyd_fighter == 2:
            if zyd_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if zyd_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if zyd_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 

            if ostrza_chaosu == 4 and zyd_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ zyd_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([zyd_min_attack_now]-[zyd_max_attack_now] DMG){/b}":
                    if zyd_weapon >= 1:
                        if zyd_wybrany == 1:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik1  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if zyd_wybrany == 2:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik2  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if zyd_wybrany == 3:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik3 

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if zyd_wybrany == 1:
                            show reka4 zorder 15 at weapon_sojusznik1 

                        if zyd_wybrany == 2:
                            show reka4 zorder 15 at weapon_sojusznik2  

                        if zyd_wybrany == 3:
                            show reka4 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 4 and zyd_weapon >= 1:
                        zyd "Proszę pana, oni są zakałą tej ziemi!"
                    
                        $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol1_hp_now -= zyd_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ akane_hp_now -= zyd_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol2_hp_now -= zyd_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [zyd_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Żyda został zablokowany{/i}"

                        jump faza13

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else: 
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:  
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13

                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza13
                    
                "{b}Obrona{/b}" if zyd_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if zyd_wybrany == 1:
                        show tarcza4 zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show tarcza4 zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show tarcza4 zorder 15 at weapon_sojusznik3 

                    $ zyd_obrona += 1
                    zyd "Nie interesuje mnie polska polityka"
                    jump faza13
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if zyd_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    zyd "Chcą, abyś to my żydzi się asymilowali i przechodzili na ich religie!"
                    jump items12

                "{b}Sprzedaj Pager{/b}" if pager_boom == 0 and kibol1_pager == 0 and kibol1_hp_now >= 1 or pager_boom == 0 and akane_pager == 0 and akane_hp_now >= 1 or pager_boom == 0 and kibol2_pager == 0 and kibol2_hp_now >= 1:
                    if zyd_wybrany == 1:
                        show pager zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show pager zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show pager zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Komu?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol1_pager += 1
                            
                            show pager1 zorder 15 at bok_wrog1
                            "{i}Kibol 1 kupił pager od Żyda{/i}"

                            jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ akane_pager += 1
                            
                            show pager2 zorder 15 at bok_wrog3
                            "{i}Akane kupił pager od Żyda{/i}"

                            jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol2_pager += 1
                            
                            show pager3 zorder 15 at bok_wrog2
                            "{i}Kibol 2 kupił pager od Żyda{/i}"

                            jump faza13
                
                "{b}Wysadź Pagery{/b}" if kibol1_pager >= 1 and pager_boom == 0 or akane_pager >= 1 and pager_boom == 0 or kibol2_pager >= 1 and pager_boom == 0:
                    $ pager_boom += 1
                    if zyd_wybrany == 1:
                        show red_button zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show red_button zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show red_button zorder 15 at weapon_sojusznik3 

                    zyd "Posmakujcie gniewu WIELKIEGO IZRAELA!!!"
                    play sound "audio/sfx/boom.mp3" 

                    if kibol1_pager == 1 and akane_pager == 1 and kibol2_pager == 1:
                        $ kibol1_hp_now -= 8
                        $ kibol2_hp_now -= 8
                        $ akane_hp_now -= 8
                        show eksplozja1 zorder 16 at bok_wrog1
                        show eksplozja3 zorder 16 at bok_wrog2
                        show eksplozja2 zorder 16 at bok_wrog3
                        "{i}Kibol 1, Akane i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                            
                    else:
                        if kibol1_pager == 1 and akane_pager == 1:
                            $ kibol1_hp_now -= 8
                            $ akane_hp_now -= 8
                            show eksplozja1 zorder 16 at bok_wrog1
                            show eksplozja2 zorder 16 at bok_wrog3
                            "{i}Kibol 1 i Akane w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                
                        else:
                            if akane_pager == 1 and kibol2_pager == 1:
                                $ kibol2_hp_now -= 8
                                $ akane_hp_now -= 8
                                show eksplozja3 zorder 16 at bok_wrog2
                                show eksplozja2 zorder 16 at bok_wrog3
                                "{i}Akane i Kibol 1 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                    
                            else:
                                if kibol1_pager == 1 and kibol2_pager == 1:
                                    $ kibol1_hp_now -= 8
                                    $ kibol2_hp_now -= 8
                                    show eksplozja1 zorder 16 at bok_wrog1
                                    show eksplozja3 zorder 16 at bok_wrog2
                                    "{i}Kibol 1 i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                        
                                else:
                                    if kibol1_pager == 1:
                                        $ kibol1_hp_now -= 8
                                        show eksplozja1 zorder 16 at bok_wrog1
                                        "{i}Kibol 1 w wyniku ekspolzji Pageru stracił 8HP{/i}"
                                            
                                    else:
                                        if akane_pager == 1:
                                            $ akane_hp_now -= 8
                                            show eksplozja2 zorder 16 at bok_wrog3
                                            "{i}Akane w wyniku ekspolzji Pageru stracił 8HP{/i}"

                                        else:
                                            if kibol2_pager == 1:
                                                $ kibol2_hp_now -= 8
                                                show eksplozja3 zorder 16 at bok_wrog2
                                                "{i}Kibol 2 w wyniku ekspolzji Pageru stracił 8HP{/i}"

                    hide red_button
                    hide pager1
                    hide pager2
                    hide pager3
                    hide pager
                    hide eksplozja1
                    hide eksplozja2
                    hide eksplozja3
                    if dialog_fight1 == 0:
                        luszcz "O ja pierdole, może Braun jednak miał trochę racji!"
                        $ dialog_fight1 += 1
                    jump faza13

        if kazuma_fighter == 2:
            if kazuma_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if kazuma_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if kazuma_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 5 and kazuma_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ kazuma_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([kazuma_min_attack_now]-[kazuma_max_attack_now] DMG){/b}":
                    if kazuma_weapon >= 1:
                        if kazuma_wybrany == 1:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik1  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if kazuma_wybrany == 2:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik2  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if kazuma_wybrany == 3:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik3 

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if kazuma_wybrany == 1:
                            show reka5 zorder 15 at weapon_sojusznik1 

                        if kazuma_wybrany == 2:
                            show reka5 zorder 15 at weapon_sojusznik2  

                        if kazuma_wybrany == 3:
                            show reka5 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 5 and kazuma_weapon >= 1:
                        kazuma "Tak, jestem Kazuma"
                    
                        $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol1_hp_now -= kazuma_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ akane_hp_now -= kazuma_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(v_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol2_hp_now -= kazuma_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [kazuma_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Kazumy został zablokowany{/i}"

                        jump faza13

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol1_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ akane_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza13

                                    $ kibol2_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza13
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza13
                    
                "{b}Obrona{/b}" if kazuma_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if kazuma_wybrany == 1:
                        show tarcza5 zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show tarcza5 zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show tarcza5 zorder 15 at weapon_sojusznik3 

                    $ kazuma_obrona += 1
                    kazuma "Nic na to nie można poradzić!"
                    jump faza13
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if kazuma_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    kazuma "Jestem zwolennikiem prawdziwej równości płci"
                    jump items12

                "{b}Steal{/b}" if kibol1_weapon >= 1 or akane_weapon >= 1 or kibol2_weapon >= 1:
                    if kazuma_wybrany == 1:
                        show chwyta zorder 16 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chwyta zorder 16 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chwyta zorder 16 at weapon_sojusznik3 

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_weapon > 0:
                            kazuma "Steal!"
                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 1 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza13
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol1_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol1_max_attack_now < kibol1_max_attack:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true
                                            $ kibol1_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true

                                        $ kibol1_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 1.  \nStatystyki Kibol 1 zostały stale drastycznie osłabione.{/i}"
                                        hide kibol1_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol1 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 1.  \nKibol 1 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol1_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                                        
                                jump faza13

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_weapon > 0:
                            kazuma "Steal!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Akane obronił się przed umiejętnością “Steal“{/i}"
                                jump faza13
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if akane_sex == 0:
                                    
                                    if kostka >= 9:
                                        if akane_max_attack_now < akane_max_attack:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                            $ akane_max_attack_now -= 2
                                        
                                        else:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                        
                                        $ akane_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show akane_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show akane_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show akane_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Akane.  \nStatystyki Akane zostały stale drastycznie osłabione.{/i}"
                                        hide akane_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        akane "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Akane.  \nAkane poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ akane_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                                        
                                jump faza13

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_weapon > 0:
                            kazuma "Steal!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 2 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza13
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol2_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol2_max_attack_now < kibol2_max_attack:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                            $ kibol2_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                        
                                        $ kibol2_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 2.  \nStatystyki Kibol 2 zostały stale drastycznie osłabione.{/i}"
                                        hide kibol2_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol2 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 2.  \nKibol 2 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol2_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                                        
                                jump faza13

    label faza13:
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide ruch

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0

        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        
        if miecz3d == 2 and luszcz_hp_now <= luszcz_hp / 2 and luszcz_fighter == 3:
            $ luszcz_min_attack_now += 1
            $ luszcz_max_attack_now += 2
        
        if miecz3d == 3 and urban_hp_now <= urban_hp / 2 and urban_fighter == 3:
            $ urban_min_attack_now += 1
            $ urban_max_attack_now += 2
        
        if miecz3d == 4 and zyd_hp_now <= zyd_hp / 2 and zyd_fighter == 3:
            $ zyd_min_attack_now += 1
            $ zyd_max_attack_now += 2
        
        if miecz3d == 5 and kazuma_hp_now <= kazuma_hp / 2 and kazuma_fighter == 3:
            $ kazuma_min_attack_now += 1
            $ kazuma_max_attack_now += 2
        
        if miecz3d == 6 and tarczownik_hp_now <= tarczownik_hp / 2 and tarczownik_fighter == 3:
            $ tarczownik_min_attack_now += 1
            $ tarczownik_max_attack_now += 2

        if luszcz_fighter == 3:
            if luszcz_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if luszcz_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if luszcz_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 2 and luszcz_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ luszcz_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([luszcz_min_attack_now]-[luszcz_max_attack_now] DMG){/b}":
                    if luszcz_weapon >= 1:
                        if luszcz_wybrany == 1:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik1  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if luszcz_wybrany == 2:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik2  

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if luszcz_wybrany == 3:
                            if gitara == 2:
                                show luszcz_weapon zorder 15 at weapon_sojusznik3 

                            if luszcz_przepychaczka == 2:
                                show luszcz_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 2:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 2:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 2:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 2:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 2:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 2:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if luszcz_wybrany == 1:
                            show reka1 zorder 15 at weapon_sojusznik1 

                        if luszcz_wybrany == 2:
                            show reka1 zorder 15 at weapon_sojusznik2  

                        if luszcz_wybrany == 3:
                            show reka1 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 2 and luszcz_weapon >= 1:                     
                        luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                    
                        $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol1_hp_now -= luszcz_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ akane_hp_now -= luszcz_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                else:
                                    $ kibol2_hp_now -= luszcz_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [luszcz_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Łuszcza został zablokowany{/i}"

                        jump faza14

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:  
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            luszcz "Jesli mialbym kogos zabic to bym uzyl mojego 30 cm potwora"
                            $ luszcz_attack = renpy.random.randint(luszcz_min_attack_now, luszcz_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Łuszcza został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:  
                                if luszcz_weapon >= 1:
                                    if gitara == 2:
                                        play sound "audio/sfx/gitara.mp3" 

                                    if luszcz_przepychaczka == 2: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 2:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 2:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 2:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 2:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 2:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= luszcz_attack
                                            "{i}Atak został podwojony i zadał [luszcz_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= int(luszcz_attack / 2)

                                    $ dmg = int(luszcz_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 2:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 2:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= luszcz_attack * 2
                                            "{i}Atak został podwojony i zadał [luszcz_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= luszcz_attack

                                    if luszcz_przepychaczka == 2 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [luszcz_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14

                                    "{i}Atak zadał [luszcz_attack] obrażeń{/i}"
                            jump faza14
                    
                "{b}Obrona{/b}" if luszcz_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if luszcz_wybrany == 1:
                        show tarcza1 zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show tarcza1 zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show tarcza1 zorder 15 at weapon_sojusznik3 

                    $ luszcz_obrona += 1
                    luszcz "I want sex"
                    jump faza14
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if luszcz_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    luszcz "Umiem wyobrażać sobie ludzi w stroju ziemniaka"
                    jump items13

                "{b}Zaparz Herbatę{/b}":
                    play sound "audio/sfx/herbaty.mp3"
                    if luszcz_wybrany == 1:
                        show herbaty zorder 15 at weapon_sojusznik1  

                    if luszcz_wybrany == 2:
                        show herbaty zorder 15 at weapon_sojusznik2  

                    if luszcz_wybrany == 3:
                        show herbaty zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Ale jaką?{/b}"

                        "{b}Wiśnia z Rumem (+5HP){/b}":
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                            menu:
                                "{b}Dla Kogo?{/b}"

                                "{b}Łuszcz{/b}" if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    if luszcz_hp_now + 5 > luszcz_hp:
                                        $ luszcz_hp_now = luszcz_hp
                                        "{i}Łuszcz odzyskał cały pasek życia{/i}"
                                    else:
                                        $ luszcz_hp_now += 5
                                        "{i}Łuszcz odzyskał 5 punktów życia{/i}"
                                
                                "{b}Shadow{/b}" if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if eminem_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if eminem_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if eminem_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if eminem_hp_now + 5 > eminem_hp:
                                        $ eminem_hp_now = eminem_hp
                                        "{i}Shadow odzyskał cały pasek życia{/i}"
                                    else:
                                        $ eminem_hp_now += 5
                                        "{i}Shadow odzyskał 5 punktów życia{/i}"

                                "{b}Jerzy Urban{/b}" if urban_hp_now >= 1 and urban_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if urban_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if urban_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if urban_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if urban_hp_now + 5 > urban_hp:
                                        $ urban_hp_now = urban_hp
                                        "{i}Jerzy Urban odzyskał cały pasek życia{/i}"
                                    else:
                                        $ urban_hp_now += 5
                                        "{i}Jerzy Urban odzyskał 5 punktów życia{/i}"

                                "{b}Żyd{/b}" if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if zyd_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if zyd_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if zyd_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if zyd_hp_now + 5 > zyd_hp:
                                        $ zyd_hp_now = zyd_hp
                                        "{i}Żyd odzyskał cały pasek życia{/i}"
                                    else:
                                        $ zyd_hp_now += 5
                                        "{i}Żyd odzyskał 5 punktów życia{/i}"

                                "{b}Kazuma{/b}" if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if kazuma_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if kazuma_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if kazuma_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if kazuma_hp_now + 5 > kazuma_hp:
                                        $ kazuma_hp_now = kazuma_hp
                                        "{i}Kazuma odzyskał cały pasek życia{/i}"
                                    else:
                                        $ kazuma_hp_now += 5
                                        "{i}Kazuma odzyskał 5 punktów życia{/i}"
                                
                                "{b}Naofumi{/b}" if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                    luszcz "Kiedyś używałem małej ale wolę duże"
                                    play sound "audio/sfx/herbata.mp3"
                                    hide wisnia_w_rumie
                                    if tarczownik_wybrany == 1:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik1  

                                    if tarczownik_wybrany == 2:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik2  

                                    if tarczownik_wybrany == 3:
                                        show wisnia_w_rumie zorder 15 at weapon_sojusznik3 

                                    if tarczownik_hp_now + 5 > tarczownik_hp:
                                        $ tarczownik_hp_now = tarczownik_hp
                                        "{i}Naofumi odzyskał cały pasek życia{/i}"
                                    else:
                                        $ tarczownik_hp_now += 5
                                        "{i}Naofumi odzyskał 5 punktów życia{/i}"
                            
                            hide wisnia_w_rumie
                            jump faza14
                            
                        "{b}Hiszpańska Mandarynka (+2HP FOR ALL){/b}":
                            luszcz "Tak. Moja mama tylko czasami zagląda mi do buzi"
                            play sound "audio/sfx/herbata.mp3"
                            hide herbaty
                            if luszcz_wybrany == 1:
                                show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                            if luszcz_wybrany == 2:
                                show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                            if luszcz_wybrany == 3:
                                show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                            if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                                if luszcz_hp_now + 2 > luszcz_hp:
                                    $ luszcz_hp_now = luszcz_hp
                                else:
                                    $ luszcz_hp_now += 2
                            
                            if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                if eminem_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if eminem_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if eminem_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if eminem_hp_now + 2 > eminem_hp:
                                    $ eminem_hp_now = eminem_hp
                                else:
                                    $ eminem_hp_now += 2

                            if urban_hp_now >= 1 and urban_wybrany >= 1:
                                if urban_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if urban_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if urban_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if urban_hp_now + 2 > urban_hp:
                                    $ urban_hp_now = urban_hp
                                else:
                                    $ urban_hp_now += 2

                            if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                                if zyd_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if zyd_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if zyd_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if zyd_hp_now + 2 > zyd_hp:
                                    $ zyd_hp_now = zyd_hp
                                else:
                                    $ zyd_hp_now += 2

                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if kazuma_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if kazuma_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if kazuma_hp_now + 2 > kazuma_hp:
                                    $ kazuma_hp_now = kazuma_hp
                                else:
                                    $ kazuma_hp_now += 2
                            
                            if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                if tarczownik_wybrany == 1:
                                    show hiszpanska_mandarynka1 zorder 15 at weapon_sojusznik1  

                                if tarczownik_wybrany == 2:
                                    show hiszpanska_mandarynka2 zorder 15 at weapon_sojusznik2  

                                if tarczownik_wybrany == 3:
                                    show hiszpanska_mandarynka3 zorder 15 at weapon_sojusznik3 

                                if tarczownik_hp_now + 2 > tarczownik_hp:
                                    $ tarczownik_hp_now = tarczownik_hp
                                else:
                                    $ tarczownik_hp_now += 2

                            "{i}Wszyscy sojusznicy odzyskali po 2 punkty życia{/i}"
                            hide hiszpanska_mandarynka1
                            hide hiszpanska_mandarynka2
                            hide hiszpanska_mandarynka3
                            jump faza14
        
        if eminem_fighter == 3:
            if eminem_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if eminem_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if eminem_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([eminem_min_attack_now]-[eminem_max_attack_now] DMG){/b}":
                    if eminem_weapon >= 1:
                        if eminem_wybrany == 1:
                            show eminem_weapon zorder 15 at weapon_sojusznik1  

                        if eminem_wybrany == 2:
                            show eminem_weapon zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show eminem_weapon zorder 15 at weapon_sojusznik3 

                    else:
                        if eminem_wybrany == 1:
                            show reka2 zorder 15 at weapon_sojusznik1 

                        if eminem_wybrany == 2:
                            show reka2 zorder 15 at weapon_sojusznik2  

                        if eminem_wybrany == 3:
                            show reka2 zorder 15 at weapon_sojusznik3 
                    
                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:  
                                play sound "audio/sfx/reka.mp3"     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol1_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:   
                                play sound "audio/sfx/reka.mp3"                        
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ akane_hp_now -= eminem_attack
                                
                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Moje imię to Cień. \nTen, kto czai się w cieniu, aby upolować cień"
                            $ eminem_attack = renpy.random.randint(eminem_min_attack_now, eminem_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Shadowa został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                play sound "audio/sfx/reka.mp3"
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(eminem_attack / 2)

                                    $ dmg = int(eminem_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    $ kibol2_hp_now -= eminem_attack

                                    "{i}Atak zadał [eminem_attack] obrażeń{/i}"
                            jump faza14
                    
                "{b}Obrona{/b}" if eminem_obrona == 0:
                    eminem "I am ..."
                    play sound "audio/sfx/shield.mp3"
                    if eminem_wybrany == 1:
                        show tarcza2 zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show tarcza2 zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show tarcza2 zorder 15 at weapon_sojusznik3 

                    $ eminem_obrona += 1
                    eminem "... rzymskim legionistą"
                    jump faza14
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if eminem_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    eminem "Czas zabawy się skończył"
                    jump items13

                "{b}Rzut Szlamem{/b}":

                    if eminem_wybrany == 1:
                        show slime zorder 15 at weapon_sojusznik1  

                    if eminem_wybrany == 2:
                        show slime zorder 15 at weapon_sojusznik2  

                    if eminem_wybrany == 3:
                        show slime zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 1 obronił się przed szlamem{/i}"
                                jump faza14
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol1_min_attack_now >= 2:
                                    $ kibol1_min_attack_now -= 2
                                    if kibol1_max_attack_now >= 6:
                                        $ kibol1_max_attack_now -= 3
                                    else:
                                        $ kibol1_max_attack_now -= 2
                        
                                else:
                                    $ kibol1_min_attack_now = 0

                                    if kibol1_max_attack_now >= 2:
                                        if kibol1_max_attack_now >= 6:
                                            $ kibol1_max_attack_now -= 3
                                        else:
                                            $ kibol1_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol1_max_attack_now = 0
                                
                                $ kibol1_slime += 1
                                show slime zorder 15 at center_wrog1 
                                "{i}Statystyki Kibol 1 zostały osłabione{/i}"
                                jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Akane obronił się przed szlamem{/i}"
                                jump faza14
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if akane_min_attack_now >= 2:
                                    $ akane_min_attack_now -= 2
                                    if akane_max_attack_now >= 6:
                                        $ akane_max_attack_now -= 3
                                    else:
                                        $ akane_max_attack_now -= 2
                        
                                else:
                                    $ akane_min_attack_now = 0

                                    if akane_max_attack_now >= 2:
                                        if akane_max_attack_now >= 6:
                                            $ akane_max_attack_now -= 3
                                        else:
                                            $ akane_max_attack_now -= 2
                                    
                                    else:
                                        $ akane_max_attack_now = 0
                                
                                $ akane_slime += 1
                                show slime zorder 15 at center_wrog3
                                "{i}Statystyki Akane zostały osłabione{/i}"
                                jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            eminem "Godzina przebudzenia nadeszła!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/sluz.mp3"
                                hide slime
                                "{i}Kibol 2 obronił się przed szlamem{/i}"
                                jump faza14
                            else:
                                play sound "audio/sfx/slime.mp3"
                                if kibol2_min_attack_now >= 2:
                                    $ kibol2_min_attack_now -= 2
                                    if kibol2_max_attack_now >= 6:
                                        $ kibol2_max_attack_now -= 3
                                    else:
                                        $ kibol2_max_attack_now -= 2
                        
                                else:
                                    $ kibol2_min_attack_now = 0

                                    if kibol2_max_attack_now >= 2:
                                        if kibol2_max_attack_now >= 6:
                                            $ kibol2_max_attack_now -= 3
                                        else:
                                            $ kibol2_max_attack_now -= 2
                                    
                                    else:
                                        $ kibol2_max_attack_now = 0
                                
                                $ kibol2_slime += 1
                                show slime zorder 15 at center_wrog2
                                "{i}Statystyki Kibol 2 zostały osłabione{/i}"
                                jump faza14

        if urban_fighter == 3:
            if urban_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if urban_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if urban_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 3 and urban_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ urban_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([urban_min_attack_now]-[urban_max_attack_now] DMG){/b}":
                    if urban_weapon >= 1:
                        if urban_wybrany == 1:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik1  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if urban_wybrany == 2:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik2  

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if urban_wybrany == 3:
                            if fuck == 3:
                                show urban_weapon zorder 15 at weapon_sojusznik3 

                            if urban_przepychaczka == 3:
                                show urban_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 3:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 3:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 3:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 3:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 3:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 3:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if urban_wybrany == 1:
                            show reka3 zorder 15 at weapon_sojusznik1 

                        if urban_wybrany == 2:
                            show reka3 zorder 15 at weapon_sojusznik2  

                        if urban_wybrany == 3:
                            show reka3 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 3 and urban_weapon >= 1:                    
                        urban "i Ci kutasa obetnie"
                    
                        $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol1_hp_now -= urban_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ akane_hp_now -= urban_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(urban_attack / 2)

                                    $ dmg = int(urban_attack / 2)
                                else:
                                    $ kibol2_hp_now -= urban_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [urban_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Jerzego Urbana został zablokowany{/i}"

                        jump faza14

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban7:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol1_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol1_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol1_obrona == 1 and stop == 3 or urban_attack == 2 and kibol1_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban7
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3"  

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol1_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza14

                                            $ kibol1_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol1_poison = 3
                                                show snake31 zorder 15 at center_wrog1
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol1_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza14

                                            $ kibol1_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol1_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun1 zorder 15 at head_wrog1
                                                    $ kibol1_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza14
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban8:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if akane_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ akane_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and akane_obrona == 1 and stop == 3 or urban_attack == 2 and akane_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban8
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if akane_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza14

                                            $ akane_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ akane_poison = 3
                                                show snake32 zorder 15 at center_wrog3
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ akane_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza14

                                            $ akane_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and akane_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun2 zorder 15 at head_wrog3
                                                    $ akane_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza14
                                        
                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            urban "i Ci kutasa obetnie"
                            label urban9:
                                $ urban_attack = renpy.random.randint(urban_min_attack_now, urban_max_attack_now)

                                if kibol2_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Jerzego Urbana został zablokowany{/i}"
                                    $ kibol2_obrona = 1
                                                                
                                else:
                                    if urban_attack == 1 and stop == 3 or urban_attack == 3 and kibol2_obrona == 1 and stop == 3 or urban_attack == 2 and kibol2_obrona == 1 and stop == 3:
                                        play sound "audio/sfx/nie.mp3"
                                        "{i}Urban NIE pozwala sobie zadać tylko 1dmg i stara się mocniej{/i}"
                                        jump urban9
                                    
                                    else:
                                        if urban_weapon >= 1:
                                            if fuck == 3:
                                                play sound "audio/sfx/fuck.mp3" 

                                            if urban_przepychaczka == 3: 
                                                play sound "audio/sfx/przepychaczka.mp3" 

                                            if stop == 3:
                                                play sound "audio/sfx/stop.mp3" 

                                            if miecz_swietlny == 3:
                                                play sound "audio/sfx/miecz_swietlny.mp3" 
                                            
                                            if patyk == 3:
                                                play sound "audio/sfx/patyk.mp3" 
                                            
                                            if bazooka == 3:
                                                play sound "audio/sfx/bazooka.mp3" 
                                            
                                            if miecz3d == 3:
                                                play sound "audio/sfx/miecz3d.mp3" 

                                        else:
                                            play sound "audio/sfx/reka.mp3" 

                                        if kibol2_obrona == 1:
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack
                                                    "{i}Atak został podwojony i zadał [urban_attack] obrażeń{/i}"
                                                    jump faza14

                                            $ kibol2_hp_now -= int(urban_attack / 2)

                                            $ dmg = int(urban_attack / 2)
                                            "{i}Atak zadał [dmg] obrażeń{/i}"
                                        else:
                                            if bazooka == 3:
                                                $ kibol2_poison = 3
                                                show snake33 zorder 15 at center_wrog2
                                            
                                            if patyk == 3:
                                                $ kostka = renpy.random.randint(1, 3)
                                                if kostka == 3:
                                                    $ kibol2_hp_now -= urban_attack * 2
                                                    "{i}Atak został podwojony i zadał [urban_attack * 2] obrażeń{/i}"
                                                    jump faza14

                                            $ kibol2_hp_now -= urban_attack

                                            if urban_przepychaczka == 3 and kibol2_stun == 0:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    show stun3 zorder 15 at head_wrog2
                                                    $ kibol2_stun = 1
                                                    "{i}Atak zadał [urban_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                                    jump faza14

                                            "{i}Atak zadał [urban_attack] obrażeń{/i}"
                                jump faza14
                    
                "{b}Obrona{/b}" if urban_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if urban_wybrany == 1:
                        show tarcza3 zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show tarcza3 zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show tarcza3 zorder 15 at weapon_sojusznik3 

                    $ urban_obrona += 1
                    urban "A ja mam to w dupie"
                    jump faza14
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if urban_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if urban_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if urban_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    urban "No tak było, nie zmyślam"
                    jump items13

                "{b}Zatrzepocz Uszami{/b}":
                    if urban_wybrany == 1:
                        show uszy zorder 15 at head_sojusznik1  

                    if urban_wybrany == 2:
                        show uszy zorder 15 at head_sojusznik2  

                    if urban_wybrany == 3:
                        show uszy zorder 15 at head_sojusznik3 
                    
                    urban "Hhyyy pfff hhyyy pffff hhyyy"
                    play sound "audio/sfx/uszy.mp3" 

                    if kibol1_obrona <= 0:
                        $ kibol1_uszy += 1
                    
                    if akane_obrona <= 0:
                        $ akane_uszy += 1
                    
                    if kibol2_obrona <= 0:
                        $ kibol2_uszy += 1

                    if kibol1_uszy == 1 and akane_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                        show uszy2 zorder 15 at head_wrog3
                        show uszy1 zorder 15 at head_wrog1
                        show uszy3 zorder 15 at head_wrog2
                        "{i}Kibol 1, Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                    
                    else:
                        if kibol1_uszy == 1 and akane_uszy == 1 and kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                            show uszy2 zorder 15 at head_wrog3
                            show uszy1 zorder 15 at head_wrog1
                            "{i}Kibol 1 i Akane skupili się na uszach Urbana{/i}"
                        
                        else:
                            if akane_uszy == 1 and kibol2_uszy == 1 and akane_hp_now >= 1 and kibol2_hp_now >= 1:
                                show uszy2 zorder 15 at head_wrog3
                                show uszy3 zorder 15 at head_wrog2
                                "{i}Akane i Kibol 2 skupili się na uszach Urbana{/i}"
                            
                            else:
                                if kibol1_uszy == 1 and kibol2_uszy == 1 and kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                                    show uszy1 zorder 15 at head_wrog1
                                    show uszy3 zorder 15 at head_wrog2
                                    "{i}Kibol 1 i Kibol 2 skupili się na uszach Urbana{/i}"
                                
                                else:
                                    if kibol1_uszy == 1 and kibol1_hp_now >= 1:
                                        show uszy1 zorder 15 at head_wrog1
                                        "{i}Kibol 1 skupił się na uszach Urbana{/i}"
                                    
                                    else:
                                        if akane_uszy == 1 and akane_hp_now >= 1:
                                            show uszy2 zorder 15 at head_wrog3
                                            "{i}Akane skupił się na uszach Urbana{/i}"

                                        else:
                                            if kibol2_uszy == 1 and kibol2_hp_now >= 1:
                                                show uszy3 zorder 15 at head_wrog2
                                                "{i}Kibol 2 skupił się na uszach Urbana{/i}"

                                            else:
                                                "{i}Niestety, ale uszy Urbana nie uwiodły nikogo{/i}"
                    
                    hide uszy
                    jump faza14

        if zyd_fighter == 3:
            if zyd_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if zyd_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if zyd_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 4 and zyd_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ zyd_min_attack_now += 1

            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([zyd_min_attack_now]-[zyd_max_attack_now] DMG){/b}":
                    if zyd_weapon >= 1:
                        if zyd_wybrany == 1:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik1  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if zyd_wybrany == 2:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik2  

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if zyd_wybrany == 3:
                            if chanuka == 4:
                                show zyd_weapon zorder 15 at weapon_sojusznik3 

                            if zyd_przepychaczka == 4:
                                show zyd_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 4:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 4:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 4:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 4:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 4:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 4:
                                show miecz3d zorder 15 at weapon_sojusznik3 

                    else:
                        if zyd_wybrany == 1:
                            show reka4 zorder 15 at weapon_sojusznik1 

                        if zyd_wybrany == 2:
                            show reka4 zorder 15 at weapon_sojusznik2  

                        if zyd_wybrany == 3:
                            show reka4 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 4 and zyd_weapon >= 1:
                        zyd "Proszę pana, oni są zakałą tej ziemi!"
                    
                        $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol1_hp_now -= zyd_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ akane_hp_now -= zyd_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                else:
                                    $ kibol2_hp_now -= zyd_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [zyd_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Żyda został zablokowany{/i}"

                        jump faza14

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:   
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            zyd "Proszę pana, oni są zakałą tej ziemi!"
                            $ zyd_attack = renpy.random.randint(zyd_min_attack_now, zyd_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Żyda został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:   
                                if zyd_weapon >= 1:
                                    if chanuka == 4:
                                        play sound "audio/sfx/chanuka.mp3" 

                                    if zyd_przepychaczka == 4: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 4:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 4:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 4:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 4:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 4:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack
                                            "{i}Atak został podwojony i zadał [zyd_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= int(zyd_attack / 2)

                                    $ dmg = int(zyd_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 4:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 4:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= zyd_attack * 2
                                            "{i}Atak został podwojony i zadał [zyd_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= zyd_attack

                                    if zyd_przepychaczka == 4 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [zyd_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14

                                    "{i}Atak zadał [zyd_attack] obrażeń{/i}"
                            jump faza14
                    
                "{b}Obrona{/b}" if zyd_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if zyd_wybrany == 1:
                        show tarcza4 zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show tarcza4 zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show tarcza4 zorder 15 at weapon_sojusznik3 

                    $ zyd_obrona += 1
                    zyd "Nie interesuje mnie polska polityka"
                    jump faza14
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if zyd_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    zyd "Chcą, abyś to my żydzi się asymilowali i przechodzili na ich religie!"
                    jump items13

                "{b}Sprzedaj Pager{/b}" if pager_boom == 0 and kibol1_pager == 0 and kibol1_hp_now >= 1 or pager_boom == 0 and akane_pager == 0 and akane_hp_now >= 1 or pager_boom == 0 and kibol2_pager == 0 and kibol2_hp_now >= 1:
                    if zyd_wybrany == 1:
                        show pager zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show pager zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show pager zorder 15 at weapon_sojusznik3 

                    menu:
                        "{b}Komu?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol1_pager += 1
                            
                            show pager1 zorder 15 at bok_wrog1
                            "{i}Kibol 1 kupił pager od Żyda{/i}"

                            jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ akane_pager += 1
                            
                            show pager2 zorder 15 at bok_wrog3
                            "{i}Akane kupił pager od Żyda{/i}"

                            jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_pager == 0:
                            zyd "Szalom alejchem, tanio pagery sprzedaję!"
                            play sound "audio/sfx/kupno.mp3" 
                            hide pager
                            $ kibol2_pager += 1
                            
                            show pager3 zorder 15 at bok_wrog2
                            "{i}Kibol 2 kupił pager od Żyda{/i}"

                            jump faza14
                
                "{b}Wysadź Pagery{/b}" if kibol1_pager >= 1 and pager_boom == 0 or akane_pager >= 1 and pager_boom == 0 or kibol2_pager >= 1 and pager_boom == 0:
                    $ pager_boom += 1
                    if zyd_wybrany == 1:
                        show red_button zorder 15 at weapon_sojusznik1  

                    if zyd_wybrany == 2:
                        show red_button zorder 15 at weapon_sojusznik2  

                    if zyd_wybrany == 3:
                        show red_button zorder 15 at weapon_sojusznik3 

                    zyd "Posmakujcie gniewu WIELKIEGO IZRAELA!!!"
                    play sound "audio/sfx/boom.mp3" 

                    if kibol1_pager == 1 and akane_pager == 1 and kibol2_pager == 1:
                        $ kibol1_hp_now -= 8
                        $ kibol2_hp_now -= 8
                        $ akane_hp_now -= 8
                        show eksplozja1 zorder 16 at bok_wrog1
                        show eksplozja3 zorder 16 at bok_wrog2
                        show eksplozja2 zorder 16 at bok_wrog3
                        "{i}Kibol 1, Akane i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                            
                    else:
                        if kibol1_pager == 1 and akane_pager == 1:
                            $ kibol1_hp_now -= 8
                            $ akane_hp_now -= 8
                            show eksplozja1 zorder 16 at bok_wrog1
                            show eksplozja2 zorder 16 at bok_wrog3
                            "{i}Kibol 1 i Akane w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                
                        else:
                            if akane_pager == 1 and kibol2_pager == 1:
                                $ kibol2_hp_now -= 8
                                $ akane_hp_now -= 8
                                show eksplozja3 zorder 16 at bok_wrog2
                                show eksplozja2 zorder 16 at bok_wrog3
                                "{i}Akane i Kibol 1 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                    
                            else:
                                if kibol1_pager == 1 and kibol2_pager == 1:
                                    $ kibol1_hp_now -= 8
                                    $ kibol2_hp_now -= 8
                                    show eksplozja1 zorder 16 at bok_wrog1
                                    show eksplozja3 zorder 16 at bok_wrog2
                                    "{i}Kibol 1 i Kibol 2 w wyniku ekspolzji Pagerów stracili po 8HP{/i}"
                                        
                                else:
                                    if kibol1_pager == 1:
                                        $ kibol1_hp_now -= 8
                                        show eksplozja1 zorder 16 at bok_wrog1
                                        "{i}Kibol 1 w wyniku ekspolzji Pageru stracił 8HP{/i}"
                                            
                                    else:
                                        if akane_pager == 1:
                                            $ akane_hp_now -= 8
                                            show eksplozja2 zorder 16 at bok_wrog3
                                            "{i}Akane w wyniku ekspolzji Pageru stracił 8HP{/i}"

                                        else:
                                            if kibol2_pager == 1:
                                                $ kibol2_hp_now -= 8
                                                show eksplozja3 zorder 16 at bok_wrog2
                                                "{i}Kibol 2 w wyniku ekspolzji Pageru stracił 8HP{/i}"
                    
                    hide red_button
                    hide pager1
                    hide pager2
                    hide pager3
                    hide pager
                    hide eksplozja1
                    hide eksplozja2
                    hide eksplozja3
                    if dialog_fight1 == 0:
                        luszcz "O ja pierdole, może Braun jednak miał trochę racji!"
                        $ dialog_fight1 += 1
                    jump faza14

        if kazuma_fighter == 3:
            if kazuma_wybrany == 1:
                show ruch zorder 0 at tlo_sojusznik1  

            if kazuma_wybrany == 2:
                show ruch zorder 0 at tlo_sojusznik2  

            if kazuma_wybrany == 3:
                show ruch zorder 0 at tlo_sojusznik3 
            
            if ostrza_chaosu == 5 and kazuma_weapon >= 1:
                if kibol1_hp_now >= 1 and akane_hp_now <= 0 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now >= 1 and kibol2_hp_now <= 0 or kibol1_hp_now <= 0 and akane_hp_now <= 0 and kibol2_hp_now >= 1:
                    $ kazuma_min_attack_now += 1
                
            menu:
                "{b}Co zrobić{/b}"

                "{b}Atak ([kazuma_min_attack_now]-[kazuma_max_attack_now] DMG){/b}":
                    if kazuma_weapon >= 1:
                        if kazuma_wybrany == 1:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik1  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik1  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik1  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik1  
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik1  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik1  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik1  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik1  

                        if kazuma_wybrany == 2:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik2  

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik2  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik2 
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik2 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik2 

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik2  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik2  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik2   

                        if kazuma_wybrany == 3:
                            if chunchunmaru == 5:
                                show kazuma_weapon zorder 15 at weapon_sojusznik3 

                            if kazuma_przepychaczka == 5:
                                show kazuma_przepychaczka zorder 15 at weapon_sojusznik3  

                            if stop == 5:
                                show stop zorder 15 at weapon_sojusznik3  
                            
                            if miecz_swietlny == 5:
                                show miecz_swietlny zorder 15 at weapon_sojusznik3 
                            
                            if ostrza_chaosu == 5:
                                show ostrza_chaosu zorder 15 at weapon_sojusznik3  

                            if patyk == 5:
                                show patyk zorder 15 at weapon_sojusznik3  

                            if bazooka == 5:
                                show bazooka zorder 15 at weapon_sojusznik3  
                            
                            if miecz3d == 5:
                                show miecz3d zorder 15 at weapon_sojusznik3  

                    else:
                        if kazuma_wybrany == 1:
                            show reka5 zorder 15 at weapon_sojusznik1 

                        if kazuma_wybrany == 2:
                            show reka5 zorder 15 at weapon_sojusznik2  

                        if kazuma_wybrany == 3:
                            show reka5 zorder 15 at weapon_sojusznik3 
                    
                    if ostrza_chaosu == 5 and kazuma_weapon >= 1:
                        kazuma "Tak, jestem Kazuma"
                    
                        $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                        if kibol1_hp_now >= 1:
                            if kibol1_obrona >= 2:
                                if akane_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                                
                            else:     
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol1_hp_now -= kazuma_attack
                        
                        if akane_hp_now >= 1:
                            if akane_obrona >= 2:
                                if kibol1_hp_now <= 0 and kibol2_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                                
                            else:     
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ akane_hp_now -= kazuma_attack

                        if kibol2_hp_now >= 1:
                            if kibol2_obrona >= 2:
                                if akane_hp_now <= 0 and kibol1_hp_now <= 0:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                                
                            else:     
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(v_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                else:
                                    $ kibol2_hp_now -= kazuma_attack
                        
                        if kibol1_hp_now >= 1 and kibol1_obrona <= 1 or akane_hp_now >= 1 and akane_obrona <= 1 or kibol2_hp_now >= 1 and kibol2_obrona <= 1:
                            play sound "audio/sfx/ostrza_chaosu.mp3"
                            "{i}Atak zadał [kazuma_attack] obrażeń wszystkim przeciwniką{/i}"
                        
                        else:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Atak Kazumy został zablokowany{/i}"

                        jump faza14

                    menu:
                        "{b}Kogo zaatakować?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol1_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol1_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol1_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol1_poison = 3
                                        show snake31 zorder 15 at center_wrog1
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol1_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol1_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol1_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun1 zorder 15 at head_wrog1
                                            $ kibol1_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if akane_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ akane_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3" 

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if akane_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ akane_poison = 3
                                        show snake32 zorder 15 at center_wrog3
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ akane_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ akane_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and akane_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun2 zorder 15 at head_wrog3
                                            $ akane_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1:
                            kazuma "Tak, jestem Kazuma"
                            $ kazuma_attack = renpy.random.randint(kazuma_min_attack_now, kazuma_max_attack_now)

                            if kibol2_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kazumy został zablokowany{/i}"
                                $ kibol2_obrona = 1
                                                               
                            else:
                                if kazuma_weapon >= 1:
                                    if chunchunmaru == 5:
                                        play sound "audio/sfx/chunchunmaru.mp3" 

                                    if kazuma_przepychaczka == 5: 
                                        play sound "audio/sfx/przepychaczka.mp3" 

                                    if stop == 5:
                                        play sound "audio/sfx/stop.mp3" 

                                    if miecz_swietlny == 5:
                                        play sound "audio/sfx/miecz_swietlny.mp3" 
                                    
                                    if patyk == 5:
                                        play sound "audio/sfx/patyk.mp3" 
                                    
                                    if bazooka == 5:
                                        play sound "audio/sfx/bazooka.mp3" 
                                    
                                    if miecz3d == 5:
                                        play sound "audio/sfx/miecz3d.mp3"  

                                else:
                                    play sound "audio/sfx/reka.mp3" 

                                if kibol2_obrona == 1:
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack
                                            "{i}Atak został podwojony i zadał [kazuma_attack] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= int(kazuma_attack / 2)

                                    $ dmg = int(kazuma_attack / 2)
                                    "{i}Atak zadał [dmg] obrażeń{/i}"
                                else:
                                    if bazooka == 5:
                                        $ kibol2_poison = 3
                                        show snake33 zorder 15 at center_wrog2
                                    
                                    if patyk == 5:
                                        $ kostka = renpy.random.randint(1, 3)
                                        if kostka == 3:
                                            $ kibol2_hp_now -= kazuma_attack * 2
                                            "{i}Atak został podwojony i zadał [kazuma_attack * 2] obrażeń{/i}"
                                            jump faza14

                                    $ kibol2_hp_now -= kazuma_attack

                                    if kazuma_przepychaczka == 5 and kibol2_stun == 0:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            show stun3 zorder 15 at head_wrog2
                                            $ kibol2_stun = 1
                                            "{i}Atak zadał [kazuma_attack] obrażeń \nPrzeciwnik został również zestunnowany{/i}"
                                            jump faza14
                                
                                    "{i}Atak zadał [kazuma_attack] obrażeń{/i}"
                            jump faza14
                    
                "{b}Obrona{/b}" if kazuma_obrona == 0:
                    play sound "audio/sfx/shield.mp3"
                    if kazuma_wybrany == 1:
                        show tarcza5 zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show tarcza5 zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show tarcza5 zorder 15 at weapon_sojusznik3 

                    $ kazuma_obrona += 1
                    kazuma "Nic na to nie można poradzić!"
                    jump faza14
                
                "{b}Item{/b}" if ile_item >= 1:
                    play sound "audio/sfx/chest.mp3"
                    if kazuma_wybrany == 1:
                        show chest zorder 15 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chest zorder 15 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chest zorder 15 at weapon_sojusznik3 

                    kazuma "Jestem zwolennikiem prawdziwej równości płci"
                    jump items13

                "{b}Steal{/b}" if kibol1_weapon >= 1 or akane_weapon >= 1 or kibol2_weapon >= 1:
                    if kazuma_wybrany == 1:
                        show chwyta zorder 16 at weapon_sojusznik1  

                    if kazuma_wybrany == 2:
                        show chwyta zorder 16 at weapon_sojusznik2  

                    if kazuma_wybrany == 3:
                        show chwyta zorder 16 at weapon_sojusznik3 

                    menu:
                        "{b}Na kim użyć?{/b}"

                        "{b}Kibol 1{/b}" if kibol1_hp_now >= 1 and kibol1_weapon > 0:
                            kazuma "Steal!"
                            if kibol1_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 1 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza14
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol1_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol1_max_attack_now < kibol1_max_attack:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true
                                            $ kibol1_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol1_max_attack_now_true = 2
                                            $ kibol1_min_attack_now_true = 0
                                            $ kibol1_min_attack_now = kibol1_min_attack_now_true
                                            $ kibol1_max_attack_now = kibol1_max_attack_now_true
                                        
                                        $ kibol1_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol1_weapon zorder 15 at weapon_sojusznik3 

                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 1.  \nStatystyki Kibol 1 zostały stale drastycznie osłabione.{/i}"
                                        hide kibol1_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol1 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 1.  \nKibol 1 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol1_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 1{/i}"
                                        hide chwyta
                                        
                                jump faza14

                        "{b}Akane{/b}" if akane_hp_now >= 1 and akane_weapon > 0:
                            kazuma "Steal!"
                            if akane_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Akane obronił się przed umiejętnością “Steal“{/i}"
                                jump faza14
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if akane_sex == 0:
                                    
                                    if kostka >= 9:
                                        if akane_max_attack_now < akane_max_attack:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                            $ akane_max_attack_now -= 2
                                        
                                        else:
                                            $ akane_max_attack_now_true = 2
                                            $ akane_min_attack_now_true = 0
                                            $ akane_min_attack_now = akane_min_attack_now_true
                                            $ akane_max_attack_now = akane_max_attack_now_true
                                        
                                        $ akane_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show akane_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show akane_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show akane_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Akane.  \nStatystyki Akane zostały stale drastycznie osłabione.{/i}"
                                        hide akane_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        akane "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Akane.  \nAkane poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ akane_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Akane{/i}"
                                        hide chwyta
                                        
                                jump faza14

                        "{b}Kibol 2{/b}" if kibol2_hp_now >= 1 and kibol2_weapon > 0:
                            kazuma "Steal!"
                            if kibol2_obrona >= 1:
                                play sound "audio/sfx/stel.mp3"
                                "{i}Kibol 2 obronił się przed umiejętnością “Steal“{/i}"
                                jump faza14
                            else:
                                $ kostka = renpy.random.randint(1, 11)
                                if kibol2_sex == 0:
                                    
                                    if kostka >= 9:
                                        if kibol2_max_attack_now < kibol2_max_attack:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                            $ kibol2_max_attack_now -= 2
                                        
                                        else:
                                            $ kibol2_max_attack_now_true = 2
                                            $ kibol2_min_attack_now_true = 0
                                            $ kibol2_min_attack_now = kibol2_min_attack_now_true
                                            $ kibol2_max_attack_now = kibol2_max_attack_now_true
                                        
                                        $ kibol2_weapon -= 1

                                        if kazuma_wybrany == 1:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show kibol2_weapon zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        "{i}Udało sie ukraść broń Kibol 2.  \nStatystyki Kibol 2 zostały stale drastycznie osłabione.{/i}"
                                        hide kibol2_weapon
                                        hide chwyta
                                    
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                        
                                else:
                                    if kostka >= 6:
                                        if kazuma_wybrany == 1:
                                            show majtki zorder 15 at weapon_sojusznik1  

                                        if kazuma_wybrany == 2:
                                            show majtki zorder 15 at weapon_sojusznik2  

                                        if kazuma_wybrany == 3:
                                            show majtki zorder 15 at weapon_sojusznik3 
                                        
                                        play sound "audio/sfx/steal.mp3"

                                        kazuma "Trafiłem jackpota!"
                                        kibol2 "Nie! Oddaj mi moje majtki!"
                                        kazuma "Uuuoohohoho!"
                                        "{i}Udało sie ukraść bieliznę Kibol 2.  \nKibol 2 poddaje sie wzamian za jej zwrócenie.{/i}"
                                        $ kibol2_hp_now = 0
                                        hide majtki
                                        hide chwyta
                                        
                                    else:
                                        play sound "audio/sfx/stel.mp3"
                                        "{i}Nie udało sie ukraść broni Kibol 2{/i}"
                                        hide chwyta
                                        
                                jump faza14

    label faza14:
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide tarcza6
        hide tarcza7
        hide tarcza8
        hide ruch

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0
    
        if vr == 2 and miecz_swietlny == 2 and luszcz_weapon >= 1 and luszcz_obrona == 0 and luszcz_hp_now > 0 and luszcz_wybrany > 0:
            if luszcz_wybrany == 1:
                show kostka1 zorder 15 at gorasojusznik1
                show kostka2 zorder 15 at dolsojusznik1
                show miecz_swietlny zorder 15 at weapon_sojusznik1
            
            if luszcz_wybrany == 2:
                show kostka1 zorder 15 at gorasojusznik2
                show kostka2 zorder 15 at dolsojusznik2
                show miecz_swietlny zorder 15 at weapon_sojusznik2
            
            if luszcz_wybrany == 3:
                show kostka1 zorder 15 at gorasojusznik3
                show kostka2 zorder 15 at dolsojusznik3
                show miecz_swietlny zorder 15 at weapon_sojusznik3

            play sound "audio/sfx/megalovania.mp3"
            "{i}Łuszcz odpala Beat Sabera{/i}"

            label losowanko_luszcz_vr1:
                $ kostka2 = renpy.random.randint(1, 3)
                if kibol1_hp_now >= 1 and kibol2_hp_now >= 1 or akane_hp_now >= 1 and kibol2_hp_now >= 1 or kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if kibol2_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1
                    
                    if kostka2 == 2:
                        if kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if akane_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog3
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Akane{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1

                    if kostka2 == 3:
                        if akane_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if akane_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 2:
                                    hide kostka1

                                if kibol2_obrona == 2:
                                    hide kostka2

                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Akane i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1

                else:
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol1_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog1
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                    
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog1 
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1
                    
                    if kostka2 == 2:
                        if akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1

                    if kostka2 == 3:
                        if kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:   
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog2
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog2  
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_luszcz_vr1

        else:
            if vr == 2 and luszcz_obrona == 0 and luszcz_hp_now > 0 and luszcz_wybrany > 0:
                label losowanko_luszcz_rzygi1:
                if luszcz_wybrany == 1:
                    show rzyg zorder 15 at rzygi_sojusznik1
                
                if luszcz_wybrany == 2:
                    show rzyg zorder 15 at rzygi_sojusznik2
                
                if luszcz_wybrany == 3:
                    show rzyg zorder 15 at rzygi_sojusznik3

                $ kostka2 = renpy.random.randint(1, 3)
                if kostka2 == 1:
                    if kibol1_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol1_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol1_obrona == 0:
                                $ kibol1_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_luszcz_rzygi1
                
                if kostka2 == 2:
                    if akane_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if akane_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if akane_obrona == 0:
                                $ akane_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_luszcz_rzygi1

                if kostka2 == 3:
                    if kibol2_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol2_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:   
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol2_obrona == 0:
                                $ kibol2_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Łuszcz zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_luszcz_rzygi1

        if vr == 7 and eminem_obrona == 0 and eminem_hp_now > 0 and eminem_wybrany > 0:
            label losowanko_eminem_rzygi1:
            if eminem_wybrany == 1:
                show rzyg zorder 15 at rzygi_sojusznik1
            
            if eminem_wybrany == 2:
                show rzyg zorder 15 at rzygi_sojusznik2
            
            if eminem_wybrany == 3:
                show rzyg zorder 15 at rzygi_sojusznik3

            $ kostka2 = renpy.random.randint(1, 3)
            if kostka2 == 1:
                if kibol1_hp_now >= 1:
                    $ kostka = renpy.random.randint(1, 2)
                    if kibol1_obrona == 2:
                        play sound "audio/sfx/obrona.mp3"
                        "{i}Rzygi zostały zablokowane{/i}"
                        hide rzyg
                    else:
                        if kibol1_obrona == 1:
                            $ kibol1_hp_now -= int(kostka / 2)
                            show rzygowina zorder 15 at center_wrog1
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                            hide rzygowina
                            hide rzyg
                        
                        if kibol1_obrona == 0:
                            $ kibol1_hp_now -= kostka
                            show rzygowina zorder 15 at center_wrog1
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                            hide rzygowina
                            hide rzyg
                else:
                    jump losowanko_eminem_rzygi1
            
            if kostka2 == 2:
                if akane_hp_now >= 1:
                    $ kostka = renpy.random.randint(1, 2)
                    if akane_obrona == 2:
                        play sound "audio/sfx/obrona.mp3"
                        "{i}Rzygi zostały zablokowane{/i}"
                        hide rzyg
                    else:
                        if akane_obrona == 1:
                            $ akane_hp_now -= int(kostka / 2)
                            show rzygowina zorder 15 at center_wrog3
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                            hide rzygowina
                            hide rzyg
                        
                        if akane_obrona == 0:
                            $ akane_hp_now -= kostka
                            show rzygowina zorder 15 at center_wrog3
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                            hide rzygowina
                            hide rzyg
                else:
                    jump losowanko_eminem_rzygi1

            if kostka2 == 3:
                if kibol2_hp_now >= 1:
                    $ kostka = renpy.random.randint(1, 2)
                    if kibol2_obrona == 2:
                        play sound "audio/sfx/obrona.mp3"
                        "{i}Rzygi zostały zablokowane{/i}"
                        hide rzyg
                    else:   
                        if kibol2_obrona == 1:
                            $ kibol2_hp_now -= int(kostka / 2)
                            show rzygowina zorder 15 at center_wrog2
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                            hide rzygowina
                            hide rzyg
                        
                        if kibol2_obrona == 0:
                            $ kibol2_hp_now -= kostka
                            show rzygowina zorder 15 at center_wrog2
                            play sound "audio/sfx/rzygi.mp3"
                            "{i}Shadow zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                            hide rzygowina
                            hide rzyg
                else:
                    jump losowanko_eminem_rzygi1


        
        if vr == 3 and miecz_swietlny == 3 and urban_weapon >= 1 and urban_obrona == 0 and urban_hp_now > 0 and urban_wybrany > 0:
            if urban_wybrany == 1:
                show kostka1 zorder 15 at gorasojusznik1
                show kostka2 zorder 15 at dolsojusznik1
                show miecz_swietlny zorder 15 at weapon_sojusznik1
            
            if urban_wybrany == 2:
                show kostka1 zorder 15 at gorasojusznik2
                show kostka2 zorder 15 at dolsojusznik2
                show miecz_swietlny zorder 15 at weapon_sojusznik2
            
            if urban_wybrany == 3:
                show kostka1 zorder 15 at gorasojusznik3
                show kostka2 zorder 15 at dolsojusznik3
                show miecz_swietlny zorder 15 at weapon_sojusznik3

            play sound "audio/sfx/megalovania.mp3"
            "{i}Jerzy Urban odpala Beat Sabera{/i}"

            label losowanko_urban_vr1:
                $ kostka2 = renpy.random.randint(1, 3)
                if kibol1_hp_now >= 1 and kibol2_hp_now >= 1 or akane_hp_now >= 1 and kibol2_hp_now >= 1 or kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if kibol2_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1
                    
                    if kostka2 == 2:
                        if kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if akane_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog3
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Akane{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1

                    if kostka2 == 3:
                        if akane_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if akane_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 2:
                                    hide kostka1

                                if kibol2_obrona == 2:
                                    hide kostka2

                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Akane i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1

                else:
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol1_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog1
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                    
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog1 
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1
                    
                    if kostka2 == 2:
                        if akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1

                    if kostka2 == 3:
                        if kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:   
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog2
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog2  
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_urban_vr1

        else:
            if vr == 3 and urban_obrona == 0 and urban_hp_now > 0 and urban_wybrany > 0:
                label losowanko_urban_rzygi1:
                if urban_wybrany == 1:
                    show rzyg zorder 15 at rzygi_sojusznik1
                
                if urban_wybrany == 2:
                    show rzyg zorder 15 at rzygi_sojusznik2
                
                if urban_wybrany == 3:
                    show rzyg zorder 15 at rzygi_sojusznik3

                $ kostka2 = renpy.random.randint(1, 3)
                if kostka2 == 1:
                    if kibol1_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol1_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol1_obrona == 0:
                                $ kibol1_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_urban_rzygi1
                
                if kostka2 == 2:
                    if akane_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if akane_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if akane_obrona == 0:
                                $ akane_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_urban_rzygi1

                if kostka2 == 3:
                    if kibol2_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol2_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:   
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol2_obrona == 0:
                                $ kibol2_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Jerzy Urban zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_urban_rzygi1
        


        if vr == 4 and miecz_swietlny == 4 and zyd_weapon >= 1 and zyd_obrona == 0 and zyd_hp_now > 0 and zyd_wybrany > 0:
            if zyd_wybrany == 1:
                show kostka1 zorder 15 at gorasojusznik1
                show kostka2 zorder 15 at dolsojusznik1
                show miecz_swietlny zorder 15 at weapon_sojusznik1
            
            if zyd_wybrany == 2:
                show kostka1 zorder 15 at gorasojusznik2
                show kostka2 zorder 15 at dolsojusznik2
                show miecz_swietlny zorder 15 at weapon_sojusznik2
            
            if zyd_wybrany == 3:
                show kostka1 zorder 15 at gorasojusznik3
                show kostka2 zorder 15 at dolsojusznik3
                show miecz_swietlny zorder 15 at weapon_sojusznik3

            play sound "audio/sfx/megalovania.mp3"
            "{i}Żyd odpala Beat Sabera{/i}"

            label losowanko_zyd_vr1:
                $ kostka2 = renpy.random.randint(1, 3)
                if kibol1_hp_now >= 1 and kibol2_hp_now >= 1 or akane_hp_now >= 1 and kibol2_hp_now >= 1 or kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if kibol2_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1
                    
                    if kostka2 == 2:
                        if kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if akane_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog3
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Akane{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1

                    if kostka2 == 3:
                        if akane_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if akane_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 2:
                                    hide kostka1

                                if kibol2_obrona == 2:
                                    hide kostka2

                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Akane i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1

                else:
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol1_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog1
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                    
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog1 
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1
                    
                    if kostka2 == 2:
                        if akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1

                    if kostka2 == 3:
                        if kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:   
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog2
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog2  
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_zyd_vr1

        else:
            if vr == 4 and zyd_obrona == 0 and zyd_hp_now > 0 and zyd_wybrany > 0:
                label losowanko_zyd_rzygi1:
                if zyd_wybrany == 1:
                    show rzyg zorder 15 at rzygi_sojusznik1
                
                if zyd_wybrany == 2:
                    show rzyg zorder 15 at rzygi_sojusznik2
                
                if zyd_wybrany == 3:
                    show rzyg zorder 15 at rzygi_sojusznik3

                $ kostka2 = renpy.random.randint(1, 3)
                if kostka2 == 1:
                    if kibol1_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol1_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol1_obrona == 0:
                                $ kibol1_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_zyd_rzygi1
                
                if kostka2 == 2:
                    if akane_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if akane_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if akane_obrona == 0:
                                $ akane_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_zyd_rzygi1

                if kostka2 == 3:
                    if kibol2_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol2_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:   
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol2_obrona == 0:
                                $ kibol2_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Żyd zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_zyd_rzygi1


        
        if vr == 5 and miecz_swietlny == 5 and kazuma_weapon >= 1 and kazuma_obrona == 0 and kazuma_hp_now > 0 and kazuma_wybrany > 0:
            if kazuma_wybrany == 1:
                show kostka1 zorder 15 at gorasojusznik1
                show kostka2 zorder 15 at dolsojusznik1
                show miecz_swietlny zorder 15 at weapon_sojusznik1
            
            if kazuma_wybrany == 2:
                show kostka1 zorder 15 at gorasojusznik2
                show kostka2 zorder 15 at dolsojusznik2
                show miecz_swietlny zorder 15 at weapon_sojusznik2
            
            if kazuma_wybrany == 3:
                show kostka1 zorder 15 at gorasojusznik3
                show kostka2 zorder 15 at dolsojusznik3
                show miecz_swietlny zorder 15 at weapon_sojusznik3

            play sound "audio/sfx/megalovania.mp3"
            "{i}Kazuma odpala Beat Sabera{/i}"

            label losowanko_kazuma_vr1:
                $ kostka2 = renpy.random.randint(1, 3)
                if kibol1_hp_now >= 1 and kibol2_hp_now >= 1 or akane_hp_now >= 1 and kibol2_hp_now >= 1 or kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if kibol2_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1
                    
                    if kostka2 == 2:
                        if kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if akane_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog3
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Akane{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1

                    if kostka2 == 3:
                        if akane_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if akane_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 2:
                                    hide kostka1

                                if kibol2_obrona == 2:
                                    hide kostka2

                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Akane i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1

                else:
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol1_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog1
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                    
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog1 
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1
                    
                    if kostka2 == 2:
                        if akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1

                    if kostka2 == 3:
                        if kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:   
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog2
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog2  
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_kazuma_vr1

        else:
            if vr == 5 and kazuma_obrona == 0 and kazuma_hp_now > 0 and kazuma_wybrany > 0:
                label losowanko_kazuma_rzygi1:
                if kazuma_wybrany == 1:
                    show rzyg zorder 15 at rzygi_sojusznik1
                
                if kazuma_wybrany == 2:
                    show rzyg zorder 15 at rzygi_sojusznik2
                
                if kazuma_wybrany == 3:
                    show rzyg zorder 15 at rzygi_sojusznik3

                $ kostka2 = renpy.random.randint(1, 3)
                if kostka2 == 1:
                    if kibol1_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol1_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol1_obrona == 0:
                                $ kibol1_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_kazuma_rzygi1
                
                if kostka2 == 2:
                    if akane_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if akane_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if akane_obrona == 0:
                                $ akane_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_kazuma_rzygi1

                if kostka2 == 3:
                    if kibol2_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol2_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:   
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol2_obrona == 0:
                                $ kibol2_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Kazuma zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_kazuma_rzygi1


        
        if vr == 6 and miecz_swietlny == 6 and tarczownik_weapon >= 1 and tarczownik_obrona == 0 and tarczownik_hp_now > 0 and tarczownik_wybrany > 0:
            if tarczownik_wybrany == 1:
                show kostka1 zorder 15 at gorasojusznik1
                show kostka2 zorder 15 at dolsojusznik1
                show miecz_swietlny zorder 15 at weapon_sojusznik1
            
            if tarczownik_wybrany == 2:
                show kostka1 zorder 15 at gorasojusznik2
                show kostka2 zorder 15 at dolsojusznik2
                show miecz_swietlny zorder 15 at weapon_sojusznik2
            
            if tarczownik_wybrany == 3:
                show kostka1 zorder 15 at gorasojusznik3
                show kostka2 zorder 15 at dolsojusznik3
                show miecz_swietlny zorder 15 at weapon_sojusznik3

            play sound "audio/sfx/megalovania.mp3"
            "{i}Naofumi odpala Beat Sabera{/i}"

            label losowanko_tarczownik_vr1:
                $ kostka2 = renpy.random.randint(1, 3)
                if kibol1_hp_now >= 1 and kibol2_hp_now >= 1 or akane_hp_now >= 1 and kibol2_hp_now >= 1 or kibol1_hp_now >= 1 and akane_hp_now >= 1: 
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if kibol2_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1
                    
                    if kostka2 == 2:
                        if kibol1_hp_now >= 1 and akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if kibol1_obrona == 2 and akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 2:
                                    hide kostka1
                                
                                if akane_obrona == 2:
                                    hide kostka2

                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog1
                                
                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog3
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Kibol 1 i Akane{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1

                    if kostka2 == 3:
                        if akane_hp_now >= 1 and kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 2)
                            if akane_obrona == 2 and kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 2:
                                    hide kostka1

                                if kibol2_obrona == 2:
                                    hide kostka2

                                if akane_obrona == 1:
                                    $ akane_hp_now -= kostka / 2
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    show kostka1 zorder 15 at center_wrog3
                                
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= kostka / 2
                                    show kostka2 zorder 15 at center_wrog2
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    show kostka2 zorder 15 at center_wrog2
                                
                                play sound "audio/sfx/atak.mp3"
                                "{i}Atak zadał [kostka] obrażeń Akane i Kibol 2{/i}"
                                hide kostka1
                                hide kostka2
                                hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1

                else:
                    if kostka2 == 1:
                        if kibol1_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol1_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if kibol1_obrona == 1:
                                    $ kibol1_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog1
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                    
                                if kibol1_obrona == 0:
                                    $ kibol1_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog1 
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 1{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1
                    
                    if kostka2 == 2:
                        if akane_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if akane_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:
                                if akane_obrona == 1:
                                    $ akane_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if akane_obrona == 0:
                                    $ akane_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog3
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Akane{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1

                    if kostka2 == 3:
                        if kibol2_hp_now >= 1:
                            $ kostka = renpy.random.randint(1, 3)
                            if kibol2_obrona == 2:
                                play sound "audio/sfx/obrona.mp3"
                                hide kostka1
                                hide kostka2
                                "{i}Atak został zablokowany{/i}"
                                hide miecz_swietlny
                            else:   
                                if kibol2_obrona == 1:
                                    $ kibol2_hp_now -= int(kostka / 2)
                                    hide kostka2
                                    show kostka1 zorder 15 at center_wrog2
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [int(kostka / 2)] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                                
                                if kibol2_obrona == 0:
                                    $ kibol2_hp_now -= kostka
                                    hide kostka1
                                    show kostka2 zorder 15 at center_wrog2  
                                    play sound "audio/sfx/atak.mp3"
                                    "{i}Atak zadał [kostka] obrażeń Kibol 2{/i}"
                                    hide kostka1
                                    hide kostka2
                                    hide miecz_swietlny
                        else:
                            jump losowanko_tarczownik_vr1

        else:
            if vr == 2 and tarczownik_obrona == 0 and tarczownik_hp_now > 0 and tarczownik_wybrany > 0:
                label losowanko_tarczownik_rzygi1:
                if tarczownik_wybrany == 1:
                    show rzyg zorder 15 at rzygi_sojusznik1
                
                if tarczownik_wybrany == 2:
                    show rzyg zorder 15 at rzygi_sojusznik2
                
                if tarczownik_wybrany == 3:
                    show rzyg zorder 15 at rzygi_sojusznik3

                $ kostka2 = renpy.random.randint(1, 3)
                if kostka2 == 1:
                    if kibol1_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol1_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if kibol1_obrona == 1:
                                $ kibol1_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Kibol 1 zadając [int(kostka / 2)] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol1_obrona == 0:
                                $ kibol1_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog1
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Kibol 1 zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_tarczownik_rzygi1
                
                if kostka2 == 2:
                    if akane_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if akane_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:
                            if akane_obrona == 1:
                                $ akane_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Akane zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if akane_obrona == 0:
                                $ akane_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog3
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Akane zadając [kostka] obrażeń{/i}"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_tarczownik_rzygi1

                if kostka2 == 3:
                    if kibol2_hp_now >= 1:
                        $ kostka = renpy.random.randint(1, 2)
                        if kibol2_obrona == 2:
                            play sound "audio/sfx/obrona.mp3"
                            "{i}Rzygi zostały zablokowane{/i}"
                            hide rzyg
                        else:   
                            if kibol2_obrona == 1:
                                $ kibol2_hp_now -= int(kostka / 2)
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Kibol 2 zadając [int(kostka / 2)] obrażeń"
                                hide rzygowina
                                hide rzyg
                            
                            if kibol2_obrona == 0:
                                $ kibol2_hp_now -= kostka
                                show rzygowina zorder 15 at center_wrog2
                                play sound "audio/sfx/rzygi.mp3"
                                "{i}Naofumi zrzygał się na Kibol 2 zadając [kostka] obrażeń"
                                hide rzygowina
                                hide rzyg
                    else:
                        jump losowanko_tarczownik_rzygi1

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0

        $ kibol1_obrona = 0
        $ akane_obrona = 0
        $ kibol2_obrona = 0
        $ luszcz_min_attack_now = luszcz_min_attack_now_true
        $ luszcz_max_attack_now = luszcz_max_attack_now_true
        $ eminem_min_attack_now = eminem_min_attack_now_true
        $ eminem_max_attack_now = eminem_max_attack_now_true
        $ urban_min_attack_now = urban_min_attack_now_true
        $ urban_max_attack_now = urban_max_attack_now_true
        $ zyd_min_attack_now = zyd_min_attack_now_true
        $ zyd_max_attack_now = zyd_max_attack_now_true
        $ kazuma_min_attack_now = kazuma_min_attack_now_true
        $ kazuma_max_attack_now = kazuma_max_attack_now_true
        $ tarczownik_min_attack_now = tarczownik_min_attack_now_true
        $ tarczownik_max_attack_now = tarczownik_max_attack_now_true  

        if kibol1_hp_now <= 0:
            jump faza15    

        show ruch zorder 0 at tlo_wrog1  
    
        if kibol1_stun == 1:
            "{i}Kibol 1 jest zestunnowany{/i}"
            jump faza15  

        if kibol1_uszy >= 1 and urban_hp_now >= 1:
            if kibol1_weapon >= 1:
                show kibol1_weapon zorder 15 at weapon_wrog1  
            else:
                show reka6 zorder 15 at weapon_wrog1
            
            $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

            if memy == 3:
                $ kostka = renpy.random.randint(1, 20)
                if kostka <= 3:
                    $ kibol1_hp_now -= kibol1_attack
                    play sound "audio/sfx/obrona.mp3"
                    "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                    jump faza15

            if urban_obrona >= 2:
                play sound "audio/sfx/obrona.mp3"
                "{i}Atak Kibol 1 został zablokowany{/i}"
                $ urban_obrona = 1
                                                
            else:
                play sound "audio/sfx/kibol1_weapon.mp3"
                if urban_obrona == 1:
                    $ urban_hp_now -= int(kibol1_attack / 2)

                    $ dmg = int(kibol1_attack / 2)
                    "{i}Kibol 1 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"

                    jump faza15
                else:
                    $ urban_hp_now -= kibol1_attack

                    "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Jerzemu Urbanowi{/i}"

                    jump faza15
        
        if kibol1_max_attack_now <= 0 and kibol1_obrona == 0:
            show tarcza6 zorder 15 at weapon_wrog1  
            play sound "audio/sfx/shield.mp3"
            "{i}Kibol 1 broni się{/i}"
            $ kibol1_obrona += 1
            jump faza15

        if kibol1_hp_now >= 1 and kibol1_obrona == 0:
            if kibol1_hp_now <= 3:
                $ kostka = renpy.random.randint(1, 4)

                if kostka >= 2:
                    show tarcza6 zorder 15 at weapon_wrog1  
                    play sound "audio/sfx/shield.mp3"
                    "{i}Kibol 1 broni się{/i}"
                    $ kibol1_obrona += 1
                    jump faza15
                
                else:
                    jump losowanko14
            
            else:
                jump losowanko14
                    
        label losowanko14:   
            if kibol1_weapon >= 1:
                show kibol1_weapon zorder 15 at weapon_wrog1  
            else:
                show reka6 zorder 15 at weapon_wrog1    
            $ kostka = renpy.random.randint(1, 6)
            if kostka == 1:
                if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                    if luszcz_hp_now <= 3:
                        $ kostka = renpy.random.randint(1, 5)
                        if kostka >= 2:
                            $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                            if memy == 2:
                                $ kostka = renpy.random.randint(1, 20)
                                if kostka <= 3:
                                    $ kibol1_hp_now -= kibol1_attack
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                    jump faza15

                            if luszcz_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kibol 1 został zablokowany{/i}"
                                $ luszcz_obrona = 1
                                                
                            else:
                                if kibol1_weapon >= 1:
                                    play sound "audio/sfx/kibol1_weapon.mp3"
                                
                                else:
                                    play sound "audio/sfx/reka.mp3"

                                if luszcz_obrona == 1:
                                    $ luszcz_hp_now -= int(kibol1_attack / 2)

                                    $ dmg = int(kibol1_attack / 2)
                                    "{i}Kibol 1 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                else:
                                    $ luszcz_hp_now -= kibol1_attack

                                    "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Łuszczowi{/i}"

                            jump faza15
                        else:
                            jump losowanko14

                    else:
                        if luszcz_hp_now <= 10:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 3:
                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol1_hp_now -= kibol1_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                        jump faza15

                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                    
                                else:
                                    if kibol1_weapon >= 1:
                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(kibol1_attack / 2)

                                        $ dmg = int(kibol1_attack / 2)
                                        "{i}Kibol 1 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= kibol1_attack

                                        "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Łuszczowi{/i}"

                                jump faza15
                            else:
                                jump losowanko14
                        
                        else:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 5:
                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol1_hp_now -= kibol1_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                        jump faza15
                            
                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                    
                                else:
                                    if kibol1_weapon >= 1:
                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(kibol1_attack / 2)

                                        $ dmg = int(kibol1_attack / 2)
                                        "{i}Kibol 1 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= kibol1_attack

                                        "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Łuszczowi{/i}"

                                jump faza15
                            else:
                                jump losowanko14

                else:
                    jump losowanko14
            else:
                if kostka == 2:
                    if urban_hp_now >= 1 and urban_wybrany >= 1:
                        if urban_hp_now <= 3:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 2:
                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                if memy == 3:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol1_hp_now -= kibol1_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                        jump faza15

                                if urban_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                    $ urban_obrona = 1

                                else:
                                    if kibol1_weapon >= 1:
                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if urban_obrona == 1:
                                        $ urban_hp_now -= int(kibol1_attack / 2)

                                        $ dmg = int(kibol1_attack / 2)
                                        "{i}Kibol 1 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                    else:
                                        $ urban_hp_now -= kibol1_attack

                                        "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Jerzemu Urbanowi{/i}"

                                jump faza15
                            else:
                                jump losowanko14

                        else:
                            if urban_hp_now <= 10:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 3:
                                    $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol1_hp_now -= kibol1_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                            jump faza15

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 został zablokowany{/i}"
                                        $ urban_obrona = 1

                                    else:
                                        if kibol1_weapon >= 1:
                                            play sound "audio/sfx/kibol1_weapon.mp3"
                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(kibol1_attack / 2)

                                            $ dmg = int(kibol1_attack / 2)
                                            "{i}Kibol 1 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= kibol1_attack

                                            "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump faza15
                                else:
                                    jump losowanko14
                            
                            else:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 5:
                                    $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol1_hp_now -= kibol1_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                            jump faza15

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 został zablokowany{/i}"
                                        $ urban_obrona = 1

                                    else:
                                        if kibol1_weapon >= 1:
                                            play sound "audio/sfx/kibol1_weapon.mp3"
                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"
                                    
                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(kibol1_attack / 2)

                                            $ dmg = int(kibol1_attack / 2)
                                            "{i}Kibol 1 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= kibol1_attack

                                            "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump faza15
                                else:
                                    jump losowanko14

                    else:
                        jump losowanko14
                else:
                    if kostka == 3:
                        if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_hp_now <= 3:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 2:
                                    $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                    if memy == 4:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol1_hp_now -= kibol1_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                            jump faza15

                                    if zyd_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 1 został zablokowany{/i}"
                                        $ zyd_obrona = 1
                                        
                                    else:
                                        if kibol1_weapon >= 1:
                                            play sound "audio/sfx/kibol1_weapon.mp3"
                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if zyd_obrona == 1:
                                            $ zyd_hp_now -= int(kibol1_attack / 2)

                                            $ dmg = int(kibol1_attack / 2)
                                            "{i}Kibol 1 zadaje [dmg] obrażeń Żydowi{/i}"
                                        else:
                                            $ zyd_hp_now -= kibol1_attack

                                            "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Żydowi{/i}"

                                    jump faza15
                                else:
                                    jump losowanko14

                            else:
                                if zyd_hp_now <= 10:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 3:
                                        $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol1_hp_now -= kibol1_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                jump faza15

                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 został zablokowany{/i}"
                                            $ zyd_obrona = 1

                                        else:
                                            if kibol1_weapon >= 1:
                                                play sound "audio/sfx/kibol1_weapon.mp3"
                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(kibol1_attack / 2)

                                                $ dmg = int(kibol1_attack / 2)
                                                "{i}Kibol 1 zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= kibol1_attack

                                                "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Żydowi{/i}"

                                        jump faza15
                                    else:
                                        jump losowanko14
                                
                                else:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 5:
                                        $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol1_hp_now -= kibol1_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                jump faza15
                                        
                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 został zablokowany{/i}"
                                            $ zyd_obrona = 1

                                        else:
                                            if kibol1_weapon >= 1:
                                                play sound "audio/sfx/kibol1_weapon.mp3"
                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(kibol1_attack / 2)

                                                $ dmg = int(kibol1_attack / 2)
                                                "{i}Kibol 1 zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= kibol1_attack

                                                "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Żydowi{/i}"

                                        jump faza15
                                    else:
                                        jump losowanko14

                        else:
                            jump losowanko14
                    else:
                        if kostka == 4:
                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_hp_now <= 3:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 2:
                                        $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                        if memy == 5:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol1_hp_now -= kibol1_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                jump faza15

                                        if kazuma_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 1 został zablokowany{/i}"
                                            $ kazuma_obrona = 1
                                        
                                        else:
                                            if kibol1_weapon >= 1:
                                                play sound "audio/sfx/kibol1_weapon.mp3"
                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if kazuma_obrona == 1:
                                                $ kazuma_hp_now -= int(kibol1_attack / 2)

                                                $ dmg = int(kibol1_attack / 2)
                                                "{i}Kibol 1 zadaje [dmg] obrażeń Kazumie{/i}"
                                            else:
                                                $ kazuma_hp_now -= kibol1_attack

                                                "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Kazumie{/i}"

                                        jump faza15
                                    else:
                                        jump losowanko14

                                else:
                                    if kazuma_hp_now <= 10:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 3:
                                            $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol1_hp_now -= kibol1_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                    jump faza15

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if kibol1_weapon >= 1:
                                                    play sound "audio/sfx/kibol1_weapon.mp3"
                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(kibol1_attack / 2)

                                                    $ dmg = int(kibol1_attack / 2)
                                                    "{i}Kibol 1 zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= kibol1_attack

                                                    "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Kazumie{/i}"

                                            jump faza15
                                        else:
                                            jump losowanko14
                                    
                                    else:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 5:
                                            $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol1_hp_now -= kibol1_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                    jump faza15

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if kibol1_weapon >= 1:
                                                    play sound "audio/sfx/kibol1_weapon.mp3"
                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(kibol1_attack / 2)

                                                    $ dmg = int(kibol1_attack / 2)
                                                    "{i}Kibol 1 zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= kibol1_attack

                                                    "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Kazumie{/i}"

                                            jump faza15
                                        else:
                                            jump losowanko14

                            else:
                                jump losowanko14
                        else:
                            if kostka == 5:
                                if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    if eminem_hp_now <= 3:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 2:
                                            $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                            if memy == 7:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol1_hp_now -= kibol1_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                    jump faza15

                                            if eminem_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 1 został zablokowany{/i}"
                                                $ eminem_obrona = 1
                                            
                                            else:
                                                if kibol1_weapon >= 1:
                                                    play sound "audio/sfx/kibol1_weapon.mp3"
                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if eminem_obrona == 1:
                                                    $ eminem_hp_now -= int(kibol1_attack / 2)

                                                    $ dmg = int(kibol1_attack / 2)
                                                    "{i}Kibol 1 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                else:
                                                    $ eminem_hp_now -= kibol1_attack

                                                    "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Shadowowi{/i}"

                                            jump faza15
                                        else:
                                            jump losowanko14

                                    else:
                                        if eminem_hp_now <= 10:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 3:
                                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol1_hp_now -= kibol1_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                        jump faza15

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if kibol1_weapon >= 1:
                                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(kibol1_attack / 2)

                                                        $ dmg = int(kibol1_attack / 2)
                                                        "{i}Kibol 1 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= kibol1_attack

                                                        "{i} [kibol1_attack] obrażeń Shadowowi{/i}"

                                                jump faza15
                                            else:
                                                jump losowanko14
                                        
                                        else:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 5:
                                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol1_hp_now -= kibol1_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                        jump faza15

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if kibol1_weapon >= 1:
                                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(kibol1_attack / 2)

                                                        $ dmg = int(kibol1_attack / 2)
                                                        "{i}Kibol 1 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= kibol1_attack

                                                        "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Shadowowi{/i}"

                                                jump faza15
                                            else:
                                                jump losowanko14

                                else:
                                    jump losowanko14
                            else:
                                if kostka == 6:
                                    if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                        if tarczownik_hp_now <= 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 2:
                                                $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                                if memy == 6:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol1_hp_now -= kibol1_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                        jump faza15

                                                if tarczownik_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 1 został zablokowany{/i}"
                                                    $ tarczownik_obrona = 1
                                                
                                                else:
                                                    if kibol1_weapon >= 1:
                                                        play sound "audio/sfx/kibol1_weapon.mp3"
                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if tarczownik_obrona == 1:
                                                        $ tarczownik_hp_now -= int(kibol1_attack / 2)

                                                        $ dmg = int(kibol1_attack / 2)
                                                        "{i}Kibol 1 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                    else:
                                                        $ tarczownik_hp_now -= kibol1_attack

                                                        "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Naofumiemu{/i}"

                                                jump faza15
                                            else:
                                                jump losowanko14

                                        else:
                                            if tarczownik_hp_now <= 10:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 3:
                                                    $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ kibol1_hp_now -= kibol1_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                            jump faza15

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 1 został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if kibol1_weapon >= 1:
                                                            play sound "audio/sfx/kibol1_weapon.mp3"
                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(kibol1_attack / 2)

                                                            $ dmg = int(kibol1_attack / 2)
                                                            "{i}Kibol 1 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= kibol1_attack

                                                            "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Naofumiemu{/i}"

                                                    jump faza15
                                                else:
                                                    jump losowanko14
                                            
                                            else:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 5:
                                                    $ kibol1_attack = renpy.random.randint(kibol1_min_attack_now, kibol1_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ kibol1_hp_now -= kibol1_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Kibol 1 odbił się od Szalika z Memów i zadał [kibol1_attack] obrażeń nadawcy{/i}"
                                                            jump faza15

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 1 został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if kibol1_weapon >= 1:
                                                            play sound "audio/sfx/kibol1_weapon.mp3"
                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(kibol1_attack / 2)

                                                            $ dmg = int(kibol1_attack / 2)
                                                            "{i}Kibol 1 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= kibol1_attack

                                                            "{i}Kibol 1 zadaje [kibol1_attack] obrażeń Naofumiemu{/i}"

                                                    jump faza15
                                                else:
                                                    jump losowanko14

                                    else:
                                        jump losowanko14
                                else:
                                    jump losowanko14
                
                
    label faza15:
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide ruch

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0
        
        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        else:
            $ ado += 1  

        if akane_hp_now <= 0:
            jump faza16      

        show ruch zorder 0 at tlo_wrog3 

        if akane_stun == 1:
            "{i}Akane jest zestunnowany{/i}"
            jump faza16 

        if akane_uszy >= 1 and urban_hp_now >= 1:
            if akane_weapon >= 1:
                show akane_weapon zorder 15 at weapon_wrog3 
            else:
                show reka7 zorder 15 at weapon_wrog3
            $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

            if memy == 3:
                $ kostka = renpy.random.randint(1, 20)
                if kostka <= 3:
                    $ akane_hp_now -= akane_attack
                    play sound "audio/sfx/obrona.mp3"
                    "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                    jump faza16

            if urban_obrona >= 2:
                play sound "audio/sfx/obrona.mp3"
                "{i}Atak Akane został zablokowany{/i}"
                $ urban_obrona = 1
                                                
            else:
                if akane_weapon >= 1:
                    play sound "audio/sfx/akane_weapon.mp3"
                                
                else:
                    play sound "audio/sfx/reka.mp3"

                if akane_obrona == 1:
                    $ akane_hp_now -= int(akane_attack / 2)

                    $ dmg = int(akane_attack / 2)
                    "{i}Akane zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"

                    jump faza16
                else:
                    $ urban_hp_now -= akane_attack

                    "{i}Akane zadaje [akane_attack] obrażeń Jerzemu Urbanowi{/i}"

                jump faza16

        if akane_max_attack_now <= 0 and akane_obrona == 0:
            show tarcza7 zorder 15 at weapon_wrog3  
            play sound "audio/sfx/shield.mp3"
            "{i}Akane broni się{/i}"
            $ akane_obrona += 1
            jump faza16

        if akane_hp_now >= 1 and akane_obrona == 0:
            if akane_hp_now <= 3:
                $ kostka = renpy.random.randint(1, 4)

                if kostka >= 2:
                    show tarcza7 zorder 15 at weapon_wrog3  
                    play sound "audio/sfx/shield.mp3"
                    "{i}Akane broni się{/i}"
                    $ akane_obrona += 1
                    jump faza16
                
                else:
                    jump losowanko15
            
            else:
                jump losowanko15
                    
        label losowanko15:
            if akane_weapon >= 1:
                show akane_weapon zorder 15 at weapon_wrog3 
            else:
                show reka7 zorder 15 at weapon_wrog3

            $ kostka = renpy.random.randint(1, 6)
            if kostka == 1:
                if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                    if luszcz_hp_now <= 3:
                        $ kostka = renpy.random.randint(1, 5)
                        if kostka >= 2:
                            $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                            if memy == 2:
                                $ kostka = renpy.random.randint(1, 20)
                                if kostka <= 3:
                                    $ akane_hp_now -= akane_attack
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                    jump faza16

                            if luszcz_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Akane został zablokowany{/i}"
                                $ luszcz_obrona = 1
                                                    
                            else:
                                if akane_weapon >= 1:
                                    play sound "audio/sfx/akane_weapon.mp3"
                                                
                                else:
                                    play sound "audio/sfx/reka.mp3"

                                if luszcz_obrona == 1:
                                    $ luszcz_hp_now -= int(akane_attack / 2)

                                    $ dmg = int(akane_attack / 2)
                                    "{i}Akane zadaje [dmg] obrażeń Łuszczowi{/i}"
                                else:
                                    $ luszcz_hp_now -= akane_attack

                                    "{i}Akane zadaje [akane_attack] obrażeń Łuszczowi{/i}"

                            jump faza16
                        else:
                            jump losowanko15

                    else:
                        if luszcz_hp_now <= 10:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 3:
                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ akane_hp_now -= akane_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                        jump faza16

                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Akane został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                        
                                else:
                                    if akane_weapon >= 1:
                                        play sound "audio/sfx/akane_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(akane_attack / 2)

                                        $ dmg = int(akane_attack / 2)
                                        "{i}Akane zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= akane_attack

                                        "{i}Akane zadaje [akane_attack] obrażeń Łuszczowi{/i}"

                                jump faza16
                            else:
                                jump losowanko15
                        
                        else:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 5:
                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ akane_hp_now -= akane_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                        jump faza16

                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Akane został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                        
                                else:
                                    if akane_weapon >= 1:
                                        play sound "audio/sfx/akane_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(akane_attack / 2)

                                        $ dmg = int(akane_attack / 2)
                                        "{i}Akane zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= akane_attack

                                        "{i}Akane zadaje [akane_attack] obrażeń Łuszczowi{/i}"

                                jump faza16
                            else:
                                jump losowanko15

                else:
                    jump losowanko15
            else:
                if kostka == 2:
                    if urban_hp_now >= 1 and urban_wybrany >= 1:
                        if urban_hp_now <= 3:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 2:
                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                if memy == 3:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ akane_hp_now -= akane_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                        jump faza16

                                if urban_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Akane został zablokowany{/i}"
                                    $ urban_obrona = 1

                                else:
                                    if akane_weapon >= 1:
                                        play sound "audio/sfx/akane_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if urban_obrona == 1:
                                        $ urban_hp_now -= int(akane_attack / 2)

                                        $ dmg = int(akane_attack / 2)
                                        "{i}Akane zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                    else:
                                        $ urban_hp_now -= akane_attack

                                        "{i}Akane zadaje [akane_attack] obrażeń Jerzemu Urbanowi{/i}"

                                jump faza16
                            else:
                                jump losowanko15

                        else:
                            if urban_hp_now <= 10:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 3:
                                    $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ akane_hp_now -= akane_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                            jump faza16

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane został zablokowany{/i}"
                                        $ urban_obrona = 1

                                    else:
                                        if akane_weapon >= 1:
                                            play sound "audio/sfx/akane_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(akane_attack / 2)

                                            $ dmg = int(akane_attack / 2)
                                            "{i}Akane zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= akane_attack

                                            "{i}Akane zadaje [akane_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump faza16
                                else:
                                    jump losowanko15
                            
                            else:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 5:
                                    $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ akane_hp_now -= akane_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                            jump faza16

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane został zablokowany{/i}"
                                        $ urban_obrona = 1

                                    else:
                                        if akane_weapon >= 1:
                                            play sound "audio/sfx/akane_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(akane_attack / 2)

                                            $ dmg = int(akane_attack / 2)
                                            "{i}Akane zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= akane_attack

                                            "{i}Akane zadaje [akane_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump faza16
                                else:
                                    jump losowanko15

                    else:
                        jump losowanko15
                else:
                    if kostka == 3:
                        if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_hp_now <= 3:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 2:
                                    $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                    if memy == 4:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ akane_hp_now -= akane_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                            jump faza16

                                    if zyd_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Akane został zablokowany{/i}"
                                        $ zyd_obrona = 1

                                    else:
                                        if akane_weapon >= 1:
                                            play sound "audio/sfx/akane_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if zyd_obrona == 1:
                                            $ zyd_hp_now -= int(akane_attack / 2)

                                            $ dmg = int(akane_attack / 2)
                                            "{i}Akane zadaje [dmg] obrażeń Żydowi{/i}"
                                        else:
                                            $ zyd_hp_now -= akane_attack

                                            "{i}Akane zadaje [akane_attack] obrażeń Żydowi{/i}"

                                    jump faza16
                                else:
                                    jump losowanko15

                            else:
                                if zyd_hp_now <= 10:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 3:
                                        $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ akane_hp_now -= akane_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                jump faza16

                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane został zablokowany{/i}"
                                            $ zyd_obrona = 1

                                        else:
                                            if akane_weapon >= 1:
                                                play sound "audio/sfx/akane_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(akane_attack / 2)

                                                $ dmg = int(akane_attack / 2)
                                                "{i}Akane zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= akane_attack

                                                "{i}Akane zadaje [akane_attack] obrażeń Żydowi{/i}"

                                        jump faza16
                                    else:
                                        jump losowanko15
                                
                                else:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 5:
                                        $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ akane_hp_now -= akane_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                jump faza16

                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane został zablokowany{/i}"
                                            $ zyd_obrona = 1

                                        else:
                                            if akane_weapon >= 1:
                                                play sound "audio/sfx/akane_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(akane_attack / 2)

                                                $ dmg = int(akane_attack / 2)
                                                "{i}Akane zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= akane_attack

                                                "{i}Akane zadaje [akane_attack] obrażeń Żydowi{/i}"

                                        jump faza16
                                    else:
                                        jump losowanko15

                        else:
                            jump losowanko15
                    else:
                        if kostka == 4:
                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_hp_now <= 3:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 2:
                                        $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                        if memy == 5:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ akane_hp_now -= akane_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                jump faza16

                                        if kazuma_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Akane został zablokowany{/i}"
                                            $ kazuma_obrona = 1
                                        
                                        else:
                                            if akane_weapon >= 1:
                                                play sound "audio/sfx/akane_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if kazuma_obrona == 1:
                                                $ kazuma_hp_now -= int(akane_attack / 2)

                                                $ dmg = int(akane_attack / 2)
                                                "{i}Akane zadaje [dmg] obrażeń Kazumie{/i}"
                                            else:
                                                $ kazuma_hp_now -= akane_attack

                                                "{i}Akane zadaje [akane_attack] obrażeń Kazumie{/i}"

                                        jump faza16
                                    else:
                                        jump losowanko15

                                else:
                                    if kazuma_hp_now <= 10:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 3:
                                            $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ akane_hp_now -= akane_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                    jump faza16

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if akane_weapon >= 1:
                                                    play sound "audio/sfx/akane_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(akane_attack / 2)

                                                    $ dmg = int(akane_attack / 2)
                                                    "{i}Akane zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= akane_attack

                                                    "{i}Akane zadaje [akane_attack] obrażeń Kazumie{/i}"

                                            jump faza16
                                        else:
                                            jump losowanko15
                                    
                                    else:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 5:
                                            $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ akane_hp_now -= akane_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                    jump faza16

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if akane_weapon >= 1:
                                                    play sound "audio/sfx/akane_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(akane_attack / 2)

                                                    $ dmg = int(akane_attack / 2)
                                                    "{i}Akane zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= akane_attack

                                                    "{i}Akane zadaje [akane_attack] obrażeń Kazumie{/i}"

                                            jump faza16
                                        else:
                                            jump losowanko15

                            else:
                                jump losowanko15
                        else:
                            if kostka == 5:
                                if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    if eminem_hp_now <= 3:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 2:
                                            $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                            if memy == 7:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ akane_hp_now -= akane_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                    jump faza16

                                            if eminem_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Akane został zablokowany{/i}"
                                                $ eminem_obrona = 1
                                                
                                            else:
                                                if akane_weapon >= 1:
                                                    play sound "audio/sfx/akane_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if eminem_obrona == 1:
                                                    $ eminem_hp_now -= int(akane_attack / 2)

                                                    $ dmg = int(akane_attack / 2)
                                                    "{i}Akane zadaje [dmg] obrażeń Shadowowi{/i}"
                                                else:
                                                    $ eminem_hp_now -= akane_attack

                                                    "{i}Akane zadaje [akane_attack] obrażeń Shadowowi{/i}"

                                            jump faza16
                                        else:
                                            jump losowanko15

                                    else:
                                        if eminem_hp_now <= 10:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 3:
                                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ akane_hp_now -= akane_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                        jump faza16

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if akane_weapon >= 1:
                                                        play sound "audio/sfx/akane_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(akane_attack / 2)

                                                        $ dmg = int(akane_attack / 2)
                                                        "{i}Akane zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= akane_attack

                                                        "{i}Akane zadaje [akane_attack] obrażeń Shadowowi{/i}"

                                                jump faza16
                                            else:
                                                jump losowanko15
                                        
                                        else:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 5:
                                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ akane_hp_now -= akane_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                        jump faza16

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if akane_weapon >= 1:
                                                        play sound "audio/sfx/akane_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(akane_attack / 2)

                                                        $ dmg = int(akane_attack / 2)
                                                        "{i}Akane zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= akane_attack

                                                        "{i}Akane zadaje [akane_attack] obrażeń Shadowowi{/i}"

                                                jump faza16
                                            else:
                                                jump losowanko15

                                else:
                                    jump losowanko15
                            else:
                                if kostka == 6:
                                    if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                        if tarczownik_hp_now <= 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 2:
                                                $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                                if memy == 6:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ akane_hp_now -= akane_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                        jump faza16

                                                if tarczownik_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Akane został zablokowany{/i}"
                                                    $ tarczownik_obrona = 1
                                                
                                                else:
                                                    if akane_weapon >= 1:
                                                        play sound "audio/sfx/akane_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if tarczownik_obrona == 1:
                                                        $ tarczownik_hp_now -= int(akane_attack / 2)

                                                        $ dmg = int(akane_attack / 2)
                                                        "{i}Akane zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                    else:
                                                        $ tarczownik_hp_now -= akane_attack

                                                        "{i}Akane zadaje [akane_attack] obrażeń Naofumiemu{/i}"

                                                jump faza16
                                            else:
                                                jump losowanko15

                                        else:
                                            if tarczownik_hp_now <= 10:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 3:
                                                    $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ akane_hp_now -= akane_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                            jump faza16

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Akane został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if akane_weapon >= 1:
                                                            play sound "audio/sfx/akane_weapon.mp3"
                                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(akane_attack / 2)

                                                            $ dmg = int(akane_attack / 2)
                                                            "{i}Akane zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= akane_attack

                                                            "{i}Akane zadaje [akane_attack] obrażeń Naofumiemu{/i}"

                                                    jump faza16
                                                else:
                                                    jump losowanko15
                                            
                                            else:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 5:
                                                    $ akane_attack = renpy.random.randint(akane_min_attack_now, akane_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ akane_hp_now -= akane_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Akane odbił się od Szalika z Memów i zadał [akane_attack] obrażeń nadawcy{/i}"
                                                            jump faza16

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Akane został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if akane_weapon >= 1:
                                                            play sound "audio/sfx/akane_weapon.mp3"
                                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(akane_attack / 2)

                                                            $ dmg = int(akane_attack / 2)
                                                            "{i}Akane zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= akane_attack

                                                            "{i}Akane zadaje [akane_attack] obrażeń Naofumiemu{/i}"

                                                    jump faza16
                                                else:
                                                    jump losowanko15

                                    else:
                                        jump losowanko15
                                else:
                                    jump losowanko15


    label faza16:
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide ruch

        if kibol1_hp_now <= 0 and kibol1_umarty == 0:
            hide snake31
            hide snake21
            hide snake11
            hide pager1
            hide uszy1
            hide kibol1
            hide tarcza6
            hide screen kibol1_stats
            $ kibol1_umarty = 1
            $ ile_wrogow -= 1
            $ kibol1_obrona = 0
            $ kibol1_weapon = 0
            $ kibol1_pager = 0
            $ kibol1_poison = 0
            $ kibol1_stun = 0

            if kibol1_slime >= 1:
                hide slime

        if akane_hp_now <= 0 and akane_umarty == 0:
            hide snake32
            hide snake22
            hide snake12
            hide pager2
            hide uszy2
            hide akane
            hide tarcza7
            hide screen akane_stats
            $ akane_umarty = 1
            $ ile_wrogow -= 1
            $ akane_obrona = 0
            $ akane_weapon = 0
            $ akane_pager = 0
            $ akane_poison = 0
            $ akane_stun = 0

            if akane_slime >= 1:
                hide slime
        
        if kibol2_hp_now <= 0 and kibol2_umarty == 0:
            hide snake33
            hide snake23
            hide snake13
            hide pager3
            hide uszy3
            hide kibol2
            hide tarcza8
            hide screen kibol2_stats
            $ kibol2_umarty = 1
            $ ile_wrogow -= 1
            $ kibol2_obrona = 0
            $ kibol2_weapon = 0
            $ kibol2_pager = 0
            $ kibol2_poison = 0
            $ kibol2_stun = 0

            if kibol2_slime >= 1:
                hide slime
        
        if ile_wrogow <= 0:
            jump wygranko_fight1
        
        if luszcz_zloty_czlowiek == 1 and luszcz_hp_now <= 0:
            hide luszcz_zloty
            $ luszcz_zloty_czlowiek = 0
            $ luszcz_hp_now = luszcz_hp
            "{i}Łuszcz uniknął śmierci, dzięki mocy złotego człowieka{/i}"

        if luszcz_hp_now <= 0 and luszcz_fighter >= 1:
            hide luszcz_vr
            hide luszcz_klata
            hide luszcz_memy
            hide luszcz_ring
            hide luszcz_ziemia
            hide luszcz_nogi
            hide luszcz_zloty
            hide plamka1
            hide luszcz
            hide tarcza1
            hide screen luszcz1_stats
            hide screen luszcz2_stats
            hide screen luszcz3_stats
            $ ile_sojusznikow -= 1
            $ luszcz_fighter = 0
            $ luszcz_obrona = 0
            $ luszcz_wybrany = 0
            $ luszcz_weapon = 0
        
        if eminem_hp_now <= 0 and eminem_fighter >= 1:
            hide plamka2
            hide eminem
            hide tarcza2
            hide eminem_vr
            hide eminem_klata
            hide eminem_memy
            hide eminem_ring
            hide eminem_ziemia
            hide eminem_nogi
            hide eminem_zloty
            hide screen eminem1_stats
            hide screen eminem2_stats
            hide screen eminem3_stats
            $ ile_sojusznikow -= 1
            $ eminem_fighter = 0
            $ eminem_obrona = 0
            $ eminem_wybrany = 0
            $ eminem_weapon = 0

        if urban_hp_now <= 0 and urban_fighter >= 1:
            hide plamka3
            hide uszy1
            hide uszy2
            hide uszy3
            hide urban
            hide tarcza3
            hide urban_vr
            hide urban_klata
            hide urban_memy
            hide urban_ring
            hide urban_ziemia
            hide urban_nogi
            hide urban_zloty
            hide screen urban1_stats
            hide screen urban2_stats
            hide screen urban3_stats
            $ ile_sojusznikow -= 1
            $ urban_fighter = 0
            $ urban_obrona = 0
            $ urban_wybrany = 0
            $ urban_weapon = 0

        if zyd_hp_now <= 0 and zyd_fighter >= 1:
            hide plamka4
            hide red_button
            hide pager1
            hide pager2
            hide pager3
            hide pager
            hide eksplozja1
            hide eksplozja2
            hide eksplozja3
            hide zyd
            hide tarcza4
            hide zyd_vr
            hide zyd_klata
            hide zyd_memy
            hide zyd_ring
            hide zyd_ziemia
            hide zyd_nogi
            hide zyd_zloty
            hide screen zyd1_stats
            hide screen zyd2_stats
            hide screen zyd3_stats
            $ ile_sojusznikow -= 1
            $ zyd_fighter = 0
            $ zyd_obrona = 0
            $ zyd_wybrany = 0
            $ zyd_weapon = 0

        if kazuma_hp_now <= 0 and kazuma_fighter >= 1:
            hide plamka5
            hide kazuma
            hide tarcza5
            hide kazuma_vr
            hide kazuma_klata
            hide kazuma_memy
            hide kazuma_ring
            hide kazuma_ziemia
            hide kazuma_nogi
            hide kazuma_zloty
            hide screen kazuma1_stats
            hide screen kazuma2_stats
            hide screen kazuma3_stats
            $ ile_sojusznikow -= 1
            $ kazuma_fighter = 0
            $ kazuma_obrona = 0
            $ kazuma_wybrany = 0
            $ kazuma_weapon = 0
        
        if tarczownik_hp_now <= 0 and tarczownik_fighter >= 1:
            hide plamka6
            hide air_strike_shield1
            hide air_strike_shield2
            hide air_strike_shield3
            hide shield_prison
            hide tarczownik_vr
            hide tarczownik_klata
            hide tarczownik_memy
            hide tarczownik_ring
            hide tarczownik_ziemia
            hide tarczownik_nogi
            hide tarczownik_zloty

            if tarczownik_air_strike_shield >= 1:
                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

            hide tarczownik
            hide screen tarczownik1_stats
            hide screen tarczownik2_stats
            hide screen tarczownik3_stats
            $ ile_sojusznikow -= 1
            $ tarczownik_fighter = 0
            $ tarczownik_obrona = 0
            $ tarczownik_wybrany = 0
            $ tarczownik_weapon = 0
        
        if ile_sojusznikow <= 0:
            jump przegranko_fight1
        else:
            $ ado += 1    

        if kibol2_hp_now <= 0:
            jump start_fight1  

        show ruch zorder 0 at tlo_wrog2

        if kibol2_stun == 1:
            "{i}Kibol 2 jest zestunnowany{/i}"
            jump start_fight1  

        if kibol2_uszy >= 1 and urban_hp_now >= 1:
            if kibol2_weapon >= 1:
                show kibol2_weapon zorder 15 at weapon_wrog2 
            else:
                show reka8 zorder 15 at weapon_wrog2
            $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

            if memy == 3:
                $ kostka = renpy.random.randint(1, 20)
                if kostka <= 3:
                    $ kibol2_hp_now -= kibol2_attack
                    play sound "audio/sfx/obrona.mp3"
                    "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                    jump start_fight1

            if urban_obrona >= 2:
                play sound "audio/sfx/obrona.mp3"
                "{i}Atak Kibol 2 został zablokowany{/i}"
                $ urban_obrona = 1
                                                
            else:
                if kibol2_weapon >= 1:
                    play sound "audio/sfx/kibol2_weapon.mp3"
                                
                else:
                    play sound "audio/sfx/reka.mp3"

                if urban_obrona >= 1:
                    $ urban_hp_now -= int(kibol2_attack / 2)

                    $ dmg = int(kibol2_attack / 2)
                    "{i}Kibol 2 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"

                    jump start_fight1
                else:
                    $ urban_hp_now -= kibol2_attack

                    "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Jerzemu Urbanowi{/i}"

                jump start_fight1

        if kibol2_max_attack_now <= 0 and kibol2_obrona == 0:
            show tarcza8 zorder 15 at weapon_wrog2  
            play sound "audio/sfx/shield.mp3"
            "{i}Kibol 2 broni się{/i}"
            $ kibol2_obrona += 1
            jump start_fight1

        if kibol2_hp_now >= 1 and kibol2_obrona == 0:
            if kibol2_hp_now <= 3:
                $ kostka = renpy.random.randint(1, 4)

                if kostka >= 2:
                    show tarcza8 zorder 15 at weapon_wrog2  
                    play sound "audio/sfx/shield.mp3"
                    "{i}Kibol 2 broni się{/i}"
                    $ kibol2_obrona += 1
                    jump start_fight1
                
                else:
                    jump losowanko16
            
            else:
                jump losowanko16
                    
        label losowanko16:    
            if kibol2_weapon >= 1:
                show kibol2_weapon zorder 15 at weapon_wrog2 
            else:
                show reka8 zorder 15 at weapon_wrog2     
            $ kostka = renpy.random.randint(1, 6)
            if kostka == 1:
                if luszcz_hp_now >= 1 and luszcz_wybrany >= 1:
                    if luszcz_hp_now <= 3:
                        $ kostka = renpy.random.randint(1, 5)
                        if kostka >= 2:
                            $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                            if memy == 2:
                                $ kostka = renpy.random.randint(1, 20)
                                if kostka <= 3:
                                    $ kibol2_hp_now -= kibol2_attack
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                    jump start_fight1

                            if luszcz_obrona >= 2:
                                play sound "audio/sfx/obrona.mp3"
                                "{i}Atak Kibol 2 został zablokowany{/i}"
                                $ luszcz_obrona = 1
                                                    
                            else:
                                if kibol2_weapon >= 1:
                                    play sound "audio/sfx/kibol2_weapon.mp3"
                                                
                                else:
                                    play sound "audio/sfx/reka.mp3"

                                if luszcz_obrona == 1:
                                    $ luszcz_hp_now -= int(kibol2_attack / 2)

                                    $ dmg = int(kibol2_attack / 2)
                                    "{i}Kibol 2 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                else:
                                    $ luszcz_hp_now -= kibol2_attack

                                    "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Łuszczowi{/i}"

                            jump start_fight1
                        else:
                            jump losowanko16

                    else:
                        if luszcz_hp_now <= 10:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 3:
                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol2_hp_now -= kibol2_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                        jump start_fight1

                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                    
                                else:
                                    if kibol2_weapon >= 1:
                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(kibol2_attack / 2)

                                        $ dmg = int(kibol2_attack / 2)
                                        "{i}Kibol 2 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= kibol2_attack

                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Łuszczowi{/i}"

                                jump start_fight1
                            else:
                                jump losowanko16
                        
                        else:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 5:
                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                if memy == 2:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol2_hp_now -= kibol2_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                        jump start_fight1

                                if luszcz_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                    $ luszcz_obrona = 1
                                                    
                                else:
                                    if kibol2_weapon >= 1:
                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if luszcz_obrona == 1:
                                        $ luszcz_hp_now -= int(kibol2_attack / 2)

                                        $ dmg = int(kibol2_attack / 2)
                                        "{i}Kibol 2 zadaje [dmg] obrażeń Łuszczowi{/i}"
                                    else:
                                        $ luszcz_hp_now -= kibol2_attack

                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Łuszczowi{/i}"

                                jump start_fight1
                            else:
                                jump losowanko16

                else:
                    jump losowanko16
            else:
                if kostka == 2:
                    if urban_hp_now >= 1 and urban_wybrany >= 1:
                        if urban_hp_now <= 3:
                            $ kostka = renpy.random.randint(1, 5)
                            if kostka >= 2:
                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                if memy == 3:
                                    $ kostka = renpy.random.randint(1, 20)
                                    if kostka <= 3:
                                        $ kibol2_hp_now -= kibol2_attack
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                        jump start_fight1

                                if urban_obrona >= 2:
                                    play sound "audio/sfx/obrona.mp3"
                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                    $ urban_obrona = 1

                                else:
                                    if kibol2_weapon >= 1:
                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                    
                                    else:
                                        play sound "audio/sfx/reka.mp3"

                                    if urban_obrona == 1:
                                        $ urban_hp_now -= int(kibol2_attack / 2)

                                        $ dmg = int(kibol2_attack / 2)
                                        "{i}Kibol 2 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                    else:
                                        $ urban_hp_now -= kibol2_attack

                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Jerzemu Urbanowi{/i}"

                                jump start_fight1
                            else:
                                jump losowanko16

                        else:
                            if urban_hp_now <= 10:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 3:
                                    $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol2_hp_now -= kibol2_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                            jump start_fight1

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 został zablokowany{/i}"
                                        $ urban_obrona = 1

                                    else:
                                        if kibol2_weapon >= 1:
                                            play sound "audio/sfx/kibol2_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(kibol2_attack / 2)

                                            $ dmg = int(kibol2_attack / 2)
                                            "{i}Kibol 2 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= kibol2_attack

                                            "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump start_fight1
                                else:
                                    jump losowanko16
                            
                            else:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 5:
                                    $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                    if memy == 3:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol2_hp_now -= kibol2_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                            jump start_fight1

                                    if urban_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 został zablokowany{/i}"
                                        $ urban_obrona = 1
                                    
                                    else:
                                        if kibol2_weapon >= 1:
                                            play sound "audio/sfx/kibol2_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if urban_obrona == 1:
                                            $ urban_hp_now -= int(kibol2_attack / 2)

                                            $ dmg = int(kibol2_attack / 2)
                                            "{i}Kibol 2 zadaje [dmg] obrażeń Jerzemu Urbanowi{/i}"
                                        else:
                                            $ urban_hp_now -= kibol2_attack

                                            "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Jerzemu Urbanowi{/i}"

                                    jump start_fight1
                                else:
                                    jump losowanko16

                    else:
                        jump losowanko16
                else:
                    if kostka == 3:
                        if zyd_hp_now >= 1 and zyd_wybrany >= 1:
                            if zyd_hp_now <= 3:
                                $ kostka = renpy.random.randint(1, 5)
                                if kostka >= 2:
                                    $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                    if memy == 4:
                                        $ kostka = renpy.random.randint(1, 20)
                                        if kostka <= 3:
                                            $ kibol2_hp_now -= kibol2_attack
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                            jump start_fight1

                                    if zyd_obrona >= 2:
                                        play sound "audio/sfx/obrona.mp3"
                                        "{i}Atak Kibol 2 został zablokowany{/i}"
                                        $ zyd_obrona = 1
                                    
                                    else:
                                        if kibol2_weapon >= 1:
                                            play sound "audio/sfx/kibol2_weapon.mp3"
                                                        
                                        else:
                                            play sound "audio/sfx/reka.mp3"

                                        if zyd_obrona == 1:
                                            $ zyd_hp_now -= int(kibol2_attack / 2)

                                            $ dmg = int(kibol2_attack / 2)
                                            "{i}Kibol 2 zadaje [dmg] obrażeń Żydowi{/i}"
                                        else:
                                            $ zyd_hp_now -= kibol2_attack

                                            "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Żydowi{/i}"

                                    jump start_fight1
                                else:
                                    jump losowanko16

                            else:
                                if zyd_hp_now <= 10:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 3:
                                        $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol2_hp_now -= kibol2_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                jump start_fight1

                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 został zablokowany{/i}"
                                            $ zyd_obrona = 1
                                        
                                        else:
                                            if kibol2_weapon >= 1:
                                                play sound "audio/sfx/kibol2_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(kibol2_attack / 2)

                                                $ dmg = int(kibol2_attack / 2)
                                                "{i}Kibol 2 zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= kibol2_attack

                                                "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Żydowi{/i}"

                                        jump start_fight1
                                    else:
                                        jump losowanko16
                                
                                else:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 5:
                                        $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                        if memy == 4:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol2_hp_now -= kibol2_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                jump start_fight1

                                        if zyd_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 został zablokowany{/i}"
                                            $ zyd_obrona = 1
                                        
                                        else:
                                            if kibol2_weapon >= 1:
                                                play sound "audio/sfx/kibol2_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if zyd_obrona == 1:
                                                $ zyd_hp_now -= int(kibol2_attack / 2)

                                                $ dmg = int(kibol2_attack / 2)
                                                "{i}Kibol 2 zadaje [dmg] obrażeń Żydowi{/i}"
                                            else:
                                                $ zyd_hp_now -= kibol2_attack

                                                "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Żydowi{/i}"

                                        jump start_fight1
                                    else:
                                        jump losowanko16

                        else:
                            jump losowanko16
                    else:
                        if kostka == 4:
                            if kazuma_hp_now >= 1 and kazuma_wybrany >= 1:
                                if kazuma_hp_now <= 3:
                                    $ kostka = renpy.random.randint(1, 5)
                                    if kostka >= 2:
                                        $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                        if memy == 5:
                                            $ kostka = renpy.random.randint(1, 20)
                                            if kostka <= 3:
                                                $ kibol2_hp_now -= kibol2_attack
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                jump start_fight1

                                        if kazuma_obrona >= 2:
                                            play sound "audio/sfx/obrona.mp3"
                                            "{i}Atak Kibol 2 został zablokowany{/i}"
                                            $ kazuma_obrona = 1
                                        
                                        else:
                                            if kibol2_weapon >= 1:
                                                play sound "audio/sfx/kibol2_weapon.mp3"
                                                            
                                            else:
                                                play sound "audio/sfx/reka.mp3"

                                            if kazuma_obrona == 1:
                                                $ kazuma_hp_now -= int(kibol2_attack / 2)

                                                $ dmg = int(kibol2_attack / 2)
                                                "{i}Kibol 2 zadaje [dmg] obrażeń Kazumie{/i}"
                                            else:
                                                $ kazuma_hp_now -= kibol2_attack

                                                "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Kazumie{/i}"

                                        jump start_fight1
                                    else:
                                        jump losowanko16

                                else:
                                    if kazuma_hp_now <= 10:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 3:
                                            $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol2_hp_now -= kibol2_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                    jump start_fight1

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if kibol2_weapon >= 1:
                                                    play sound "audio/sfx/kibol2_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(kibol2_attack / 2)

                                                    $ dmg = int(kibol2_attack / 2)
                                                    "{i}Kibol 2 zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= kibol2_attack

                                                    "{i}Kibol 1 zadaje [kibol2_attack] obrażeń Kazumie{/i}"

                                            jump start_fight1
                                        else:
                                            jump losowanko16
                                    
                                    else:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 5:
                                            $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                            if memy == 5:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol2_hp_now -= kibol2_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                    jump start_fight1

                                            if kazuma_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 został zablokowany{/i}"
                                                $ kazuma_obrona = 1
                                            
                                            else:
                                                if kibol2_weapon >= 1:
                                                    play sound "audio/sfx/kibol2_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if kazuma_obrona == 1:
                                                    $ kazuma_hp_now -= int(kibol2_attack / 2)

                                                    $ dmg = int(kibol2_attack / 2)
                                                    "{i}Kibol 2 zadaje [dmg] obrażeń Kazumie{/i}"
                                                else:
                                                    $ kazuma_hp_now -= kibol2_attack

                                                    "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Kazumie{/i}"

                                            jump start_fight1
                                        else:
                                            jump losowanko16

                            else:
                                jump losowanko16
                        else:
                            if kostka == 5:
                                if eminem_hp_now >= 1 and eminem_wybrany >= 1:
                                    if eminem_hp_now <= 3:
                                        $ kostka = renpy.random.randint(1, 5)
                                        if kostka >= 2:
                                            $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                            if memy == 7:
                                                $ kostka = renpy.random.randint(1, 20)
                                                if kostka <= 3:
                                                    $ kibol2_hp_now -= kibol2_attack
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                    jump start_fight1

                                            if eminem_obrona >= 2:
                                                play sound "audio/sfx/obrona.mp3"
                                                "{i}Atak Kibol 2 został zablokowany{/i}"
                                                $ eminem_obrona = 1  
                                            
                                            else:
                                                if kibol2_weapon >= 1:
                                                    play sound "audio/sfx/kibol2_weapon.mp3"
                                                                
                                                else:
                                                    play sound "audio/sfx/reka.mp3"

                                                if eminem_obrona == 1:
                                                    $ eminem_hp_now -= int(kibol2_attack / 2)

                                                    $ dmg = int(kibol2_attack / 2)
                                                    "{i}Kibol 2 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                else:
                                                    $ eminem_hp_now -= kibol2_attack

                                                    "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Shadowowi{/i}"

                                            jump start_fight1
                                        else:
                                            jump losowanko16

                                    else:
                                        if eminem_hp_now <= 10:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 3:
                                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol2_hp_now -= kibol2_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                        jump start_fight1

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if kibol2_weapon >= 1:
                                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(kibol2_attack / 2)

                                                        $ dmg = int(kibol2_attack / 2)
                                                        "{i}Kibol 2 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= kibol2_attack

                                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Shadowowi{/i}"

                                                jump start_fight1
                                            else:
                                                jump losowanko16
                                        
                                        else:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 5:
                                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                                if memy == 7:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol2_hp_now -= kibol2_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                        jump start_fight1

                                                if eminem_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                                    $ eminem_obrona = 1
                                                
                                                else:
                                                    if kibol2_weapon >= 1:
                                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if eminem_obrona == 1:
                                                        $ eminem_hp_now -= int(kibol2_attack / 2)

                                                        $ dmg = int(kibol2_attack / 2)
                                                        "{i}Kibol 2 zadaje [dmg] obrażeń Shadowowi{/i}"
                                                    else:
                                                        $ eminem_hp_now -= kibol2_attack

                                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Shadowowi{/i}"

                                                jump start_fight1
                                            else:
                                                jump losowanko16

                                else:
                                    jump losowanko16
                            else:
                                if kostka == 6:
                                    if tarczownik_hp_now >= 1 and tarczownik_wybrany >= 1:
                                        if tarczownik_hp_now <= 3:
                                            $ kostka = renpy.random.randint(1, 5)
                                            if kostka >= 2:
                                                $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                                if memy == 6:
                                                    $ kostka = renpy.random.randint(1, 20)
                                                    if kostka <= 3:
                                                        $ kibol2_hp_now -= kibol2_attack
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                        jump start_fight1

                                                if tarczownik_obrona >= 2:
                                                    play sound "audio/sfx/obrona.mp3"
                                                    "{i}Atak Kibol 2 został zablokowany{/i}"
                                                    $ tarczownik_obrona = 1
                                                
                                                else:
                                                    if kibol2_weapon >= 1:
                                                        play sound "audio/sfx/kibol2_weapon.mp3"
                                                                    
                                                    else:
                                                        play sound "audio/sfx/reka.mp3"

                                                    if tarczownik_obrona == 1:
                                                        $ tarczownik_hp_now -= int(kibol2_attack / 2)

                                                        $ dmg = int(kibol2_attack / 2)
                                                        "{i}Kibol 2 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                    else:
                                                        $ tarczownik_hp_now -= kibol2_attack

                                                        "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Naofumiemu{/i}"

                                                jump start_fight1
                                            else:
                                                jump losowanko16

                                        else:
                                            if tarczownik_hp_now <= 10:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 3:
                                                    $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ kibol2_hp_now -= kibol2_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                            jump start_fight1

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 2 został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if kibol2_weapon >= 1:
                                                            play sound "audio/sfx/kibol2_weapon.mp3"
                                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(kibol2_attack / 2)

                                                            $ dmg = int(kibol2_attack / 2)
                                                            "{i}Kibol 2 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= kibol2_attack

                                                            "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Naofumiemu{/i}"

                                                    jump start_fight1
                                                else:
                                                    jump losowanko16
                                            
                                            else:
                                                $ kostka = renpy.random.randint(1, 5)
                                                if kostka >= 5:
                                                    $ kibol2_attack = renpy.random.randint(kibol2_min_attack_now, kibol2_max_attack_now)

                                                    if memy == 6:
                                                        $ kostka = renpy.random.randint(1, 20)
                                                        if kostka <= 3:
                                                            $ kibol2_hp_now -= kibol2_attack
                                                            play sound "audio/sfx/obrona.mp3"
                                                            "{i}Atak Kibol 2 odbił się od Szalika z Memów i zadał [kibol2_attack] obrażeń nadawcy{/i}"
                                                            jump start_fight1

                                                    if tarczownik_obrona >= 2:
                                                        play sound "audio/sfx/obrona.mp3"
                                                        "{i}Atak Kibol 2 został zablokowany{/i}"
                                                        $ tarczownik_obrona = 1
                                                
                                                    else:
                                                        if kibol2_weapon >= 1:
                                                            play sound "audio/sfx/kibol2_weapon.mp3"
                                                                        
                                                        else:
                                                            play sound "audio/sfx/reka.mp3"

                                                        if tarczownik_obrona == 1:
                                                            $ tarczownik_hp_now -= int(kibol2_attack / 2)

                                                            $ dmg = int(kibol2_attack / 2)
                                                            "{i}Kibol 2 zadaje [dmg] obrażeń Naofumiemu{/i}"
                                                        else:
                                                            $ tarczownik_hp_now -= kibol2_attack

                                                            "{i}Kibol 2 zadaje [kibol2_attack] obrażeń Naofumiemu{/i}"

                                                    jump start_fight1
                                                else:
                                                    jump losowanko16

                                    else:
                                        jump losowanko16
                                else: 
                                    jump losowanko16                

    label przegranko_fight1:
        scene bg dead
        play music "audio/music/losing.mp3" 
        queue music "audio/music/dead.mp3" 
        hide plamka1
        hide plamka2
        hide plamka3
        hide plamka4
        hide plamka5
        hide plamka6
        hide snake33
        hide snake23
        hide snake13
        hide snake32
        hide snake22
        hide snake12
        hide snake31
        hide snake21
        hide snake11
        hide air_strike_shield1
        hide air_strike_shield2
        hide air_strike_shield3
        hide shield_prison
        hide red_button
        hide pager1
        hide pager2
        hide pager3
        hide pager
        hide eksplozja1
        hide eksplozja2
        hide eksplozja3
        hide uszy1
        hide uszy2
        hide uszy3
        hide slime
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide luszcz_vr
        hide luszcz_klata
        hide luszcz_memy
        hide luszcz_ring
        hide luszcz_ziemia
        hide luszcz_nogi
        hide luszcz_zloty
        hide eminem_vr
        hide eminem_klata
        hide eminem_memy
        hide eminem_ring
        hide eminem_ziemia
        hide eminem_nogi
        hide eminem_zloty
        hide urban_vr
        hide urban_klata
        hide urban_memy
        hide urban_ring
        hide urban_ziemia
        hide urban_nogi
        hide urban_zloty
        hide zyd_vr
        hide zyd_klata
        hide zyd_memy
        hide zyd_ring
        hide zyd_ziemia
        hide zyd_nogi
        hide zyd_zloty
        hide kazuma_vr
        hide kazuma_klata
        hide kazuma_memy
        hide kazuma_ring
        hide kazuma_ziemia
        hide kazuma_nogi
        hide kazuma_zloty
        hide tarczownik_vr
        hide tarczownik_klata
        hide tarczownik_memy
        hide tarczownik_ring
        hide tarczownik_ziemia
        hide tarczownik_nogi
        hide tarczownik_zloty
        hide screen kibol1_stats
        hide screen akane_stats
        hide screen kibol2_stats
        window hide
        menu:
            "{b}Powtórz Walkę{/b}":
                window show
                $ fight_on = 0
                $ timer += 5

                $ ile_sojusznikow = 0
                $ ile_wrogow = 0

                $ luszcz_fighter = 0
                $ eminem_fighter = 0
                $ urban_fighter = 0
                $ zyd_fighter = 0
                $ kazuma_fighter = 0
                $ tarczownik_fighter = 0

                $ luszcz_wybrany = 0
                $ eminem_wybrany = 0
                $ urban_wybrany = 0
                $ zyd_wybrany = 0
                $ kazuma_wybrany = 0
                $ tarczownik_wybrany = 0

                $ luszcz_weapon = 1
                $ eminem_weapon = 1
                $ urban_weapon = 1
                $ zyd_weapon = 1
                $ kazuma_weapon = 1
                $ tarczownik_weapon = 1

                $ luszcz_lagodny = 0
                $ eminem_lagodny = 0
                $ urban_lagodny = 0
                $ zyd_lagodny = 0
                $ kazuma_lagodny = 0
                $ tarczownik_lagodny = 0

                $ luszcz_drpepper = 0
                $ eminem_drpepper = 0
                $ urban_drpepper = 0
                $ zyd_drpepper = 0
                $ kazuma_drpepper = 0
                $ tarczownik_drpepper = 0

                $ luszcz_obrona = 0
                $ eminem_obrona = 0
                $ urban_obrona = 0
                $ zyd_obrona = 0
                $ kazuma_obrona = 0
                $ tarczownik_obrona = 0

                $ luszcz_zloty_czlowiek = 0
                $ eminem_zloty_czlowiek = 0
                $ urban_zloty_czlowiek = 0
                $ zyd_zloty_czlowiek = 0
                $ kazuma_zloty_czlowiek = 0
                $ tarczownik_zloty_czlowiek = 0

                $ luszcz_hp_now = luszcz_hp
                $ luszcz_min_attack_now = luszcz_min_attack
                $ luszcz_max_attack_now = luszcz_max_attack
                $ luszcz_min_attack_now_true = luszcz_min_attack
                $ luszcz_max_attack_now_true = luszcz_max_attack
                $ eminem_hp_now = eminem_hp
                $ eminem_min_attack_now = eminem_min_attack
                $ eminem_max_attack_now = eminem_max_attack
                $ eminem_min_attack_now_true = eminem_min_attack
                $ eminem_max_attack_now_true = eminem_max_attack
                $ urban_hp_now = urban_hp
                $ urban_min_attack_now = urban_min_attack
                $ urban_max_attack_now = urban_max_attack
                $ urban_min_attack_now_true = urban_min_attack
                $ urban_max_attack_now_true = urban_max_attack
                $ zyd_hp_now = zyd_hp
                $ zyd_min_attack_now = zyd_min_attack
                $ zyd_max_attack_now = zyd_max_attack
                $ zyd_min_attack_now_true = zyd_min_attack
                $ zyd_max_attack_now_true = zyd_max_attack
                $ kazuma_hp_now = kazuma_hp
                $ kazuma_min_attack_now = kazuma_min_attack
                $ kazuma_max_attack_now = kazuma_max_attack
                $ kazuma_min_attack_now_true = kazuma_min_attack
                $ kazuma_max_attack_now_true = kazuma_max_attack
                $ tarczownik_hp_now = tarczownik_hp
                $ tarczownik_min_attack_now = tarczownik_min_attack
                $ tarczownik_max_attack_now = tarczownik_max_attack
                $ tarczownik_min_attack_now_true = tarczownik_min_attack
                $ tarczownik_max_attack_now_true = tarczownik_max_attack

                $ kibol1_hp_now = kibol1_hp
                $ kibol1_min_attack_now = kibol1_min_attack
                $ kibol1_max_attack_now = kibol1_max_attack
                $ kibol1_min_attack_now_true = kibol1_min_attack
                $ kibol1_max_attack_now_true = kibol1_max_attack
                $ kibol2_hp_now = kibol2_hp
                $ kibol2_min_attack_now = kibol2_min_attack
                $ kibol2_max_attack_now = kibol2_max_attack
                $ kibol2_min_attack_now_true = kibol2_min_attack
                $ kibol2_max_attack_now_true = kibol2_max_attack
                $ akane_hp_now = akane_hp
                $ akane_min_attack_now = akane_min_attack
                $ akane_max_attack_now = akane_max_attack
                $ akane_min_attack_now_true = akane_min_attack
                $ akane_max_attack_now_true = akane_max_attack

                $ kibol1_pager = 0
                $ kibol2_pager = 0
                $ akane_pager = 0
                $ pager_boom = 0
                
                $ kibol1_uszy = 0
                $ kibol2_uszy = 0
                $ akane_uszy = 0

                $ kibol1_slime = 0
                $ kibol2_slime = 0
                $ akane_slime = 0

                $ kibol1_weapon = 1
                $ akane_weapon = 1
                $ kibol2_weapon = 1

                $ kibol1_obrona = 0
                $ kibol2_obrona = 0
                $ akane_obrona = 0

                $ kibol1_umarty = 0
                $ kibol2_umarty = 0
                $ akane_umarty = 0

                $ kibol1_poison = 0
                $ kibol1_stun = 0
                $ kibol2_poison = 0
                $ kibol2_stun = 0
                $ akane_poison = 0
                $ akane_stun = 0
                jump fight1


    label wygranko_fight1:
        hide plamka1
        hide plamka2
        hide plamka3
        hide plamka4
        hide plamka5
        hide plamka6
        hide snake33
        hide snake23
        hide snake13
        hide snake32
        hide snake22
        hide snake12
        hide snake31
        hide snake21
        hide snake11
        hide air_strike_shield1
        hide air_strike_shield2
        hide air_strike_shield3
        hide shield_prison
        hide red_button
        hide pager1
        hide pager2
        hide pager3
        hide pager
        hide eksplozja1
        hide eksplozja2
        hide eksplozja3
        hide uszy1
        hide uszy2
        hide uszy3
        hide slime
        hide reka1
        hide reka2
        hide reka3
        hide reka4
        hide reka5
        hide reka6
        hide reka7
        hide reka8
        hide reka9
        hide ostrza_chaosu
        hide miecz_swietlny
        hide bazooka
        hide miecz3d
        hide patyk
        hide stop
        hide luszcz_przepychaczka
        hide urban_przepychaczka
        hide zyd_przepychaczka
        hide kazuma_przepychaczka
        hide tarczownik_przepychaczka
        hide luszcz_weapon
        hide eminem_weapon
        hide urban_weapon
        hide zyd_weapon
        hide kazuma_weapon
        hide tarczownik_weapon
        hide kibol1_weapon
        hide akane_weapon
        hide kibol2_weapon
        hide luszcz_vr
        hide luszcz_klata
        hide luszcz_memy
        hide luszcz_ring
        hide luszcz_ziemia
        hide luszcz_nogi
        hide luszcz_zloty
        hide eminem_vr
        hide eminem_klata
        hide eminem_memy
        hide eminem_ring
        hide eminem_ziemia
        hide eminem_nogi
        hide eminem_zloty
        hide urban_vr
        hide urban_klata
        hide urban_memy
        hide urban_ring
        hide urban_ziemia
        hide urban_nogi
        hide urban_zloty
        hide zyd_vr
        hide zyd_klata
        hide zyd_memy
        hide zyd_ring
        hide zyd_ziemia
        hide zyd_nogi
        hide zyd_zloty
        hide kazuma_vr
        hide kazuma_klata
        hide kazuma_memy
        hide kazuma_ring
        hide kazuma_ziemia
        hide kazuma_nogi
        hide kazuma_zloty
        hide tarczownik_vr
        hide tarczownik_klata
        hide tarczownik_memy
        hide tarczownik_ring
        hide tarczownik_ziemia
        hide tarczownik_nogi
        hide tarczownik_zloty

        hide screen luszcz1_stats
        hide screen luszcz2_stats
        hide screen luszcz3_stats

        hide screen eminem1_stats
        hide screen eminem2_stats
        hide screen eminem3_stats

        hide screen urban1_stats
        hide screen urban2_stats
        hide screen urban3_stats

        hide screen zyd1_stats
        hide screen zyd2_stats
        hide screen zyd3_stats

        hide screen kazuma1_stats
        hide screen kazuma2_stats
        hide screen kazuma3_stats

        hide screen tarczownik1_stats
        hide screen tarczownik2_stats
        hide screen tarczownik3_stats

        $ fight_on = 0

        $ ile_sojusznikow = 0
        $ ile_wrogow = 0

        $ luszcz_fighter = 0
        $ eminem_fighter = 0
        $ urban_fighter = 0
        $ zyd_fighter = 0
        $ kazuma_fighter = 0
        $ tarczownik_fighter = 0

        $ luszcz_zloty_czlowiek = 0
        $ eminem_zloty_czlowiek = 0
        $ urban_zloty_czlowiek = 0
        $ zyd_zloty_czlowiek = 0
        $ kazuma_zloty_czlowiek = 0
        $ tarczownik_zloty_czlowiek = 0

        $ luszcz_wybrany = 0
        $ eminem_wybrany = 0
        $ urban_wybrany = 0
        $ zyd_wybrany = 0
        $ kazuma_wybrany = 0
        $ tarczownik_wybrany = 0

        $ luszcz_weapon = 1
        $ eminem_weapon = 1
        $ urban_weapon = 1
        $ zyd_weapon = 1
        $ kazuma_weapon = 1
        $ tarczownik_weapon = 1

        $ luszcz_obrona = 0
        $ eminem_obrona = 0
        $ urban_obrona = 0
        $ zyd_obrona = 0
        $ kazuma_obrona = 0
        $ tarczownik_obrona = 0

        $ luszcz_lagodny = 0
        $ eminem_lagodny = 0
        $ urban_lagodny = 0
        $ zyd_lagodny = 0
        $ kazuma_lagodny = 0
        $ tarczownik_lagodny = 0

        $ luszcz_drpepper = 0
        $ eminem_drpepper = 0
        $ urban_drpepper = 0
        $ zyd_drpepper = 0
        $ kazuma_drpepper = 0
        $ tarczownik_drpepper = 0

        $ luszcz_hp_now = luszcz_hp
        $ luszcz_min_attack_now = luszcz_min_attack
        $ luszcz_max_attack_now = luszcz_max_attack
        $ luszcz_min_attack_now_true = luszcz_min_attack
        $ luszcz_max_attack_now_true = luszcz_max_attack
        $ eminem_hp_now = eminem_hp
        $ eminem_min_attack_now = eminem_min_attack
        $ eminem_max_attack_now = eminem_max_attack
        $ eminem_min_attack_now_true = eminem_min_attack
        $ eminem_max_attack_now_true = eminem_max_attack
        $ urban_hp_now = urban_hp
        $ urban_min_attack_now = urban_min_attack
        $ urban_max_attack_now = urban_max_attack
        $ urban_min_attack_now_true = urban_min_attack
        $ urban_max_attack_now_true = urban_max_attack
        $ zyd_hp_now = zyd_hp
        $ zyd_min_attack_now = zyd_min_attack
        $ zyd_max_attack_now = zyd_max_attack
        $ zyd_min_attack_now_true = zyd_min_attack
        $ zyd_max_attack_now_true = zyd_max_attack
        $ kazuma_hp_now = kazuma_hp
        $ kazuma_min_attack_now = kazuma_min_attack
        $ kazuma_max_attack_now = kazuma_max_attack
        $ kazuma_min_attack_now_true = kazuma_min_attack
        $ kazuma_max_attack_now_true = kazuma_max_attack
        $ tarczownik_hp_now = tarczownik_hp
        $ tarczownik_min_attack_now = tarczownik_min_attack
        $ tarczownik_max_attack_now = tarczownik_max_attack
        $ tarczownik_min_attack_now_true = tarczownik_min_attack
        $ tarczownik_max_attack_now_true = tarczownik_max_attack

        $ kibol1_hp_now = kibol1_hp
        $ kibol1_min_attack_now = kibol1_min_attack
        $ kibol1_max_attack_now = kibol1_max_attack
        $ kibol1_min_attack_now_true = kibol1_min_attack
        $ kibol1_max_attack_now_true = kibol1_max_attack
        $ kibol2_hp_now = kibol2_hp
        $ kibol2_min_attack_now = kibol2_min_attack
        $ kibol2_max_attack_now = kibol2_max_attack
        $ kibol2_min_attack_now_true = kibol2_min_attack
        $ kibol2_max_attack_now_true = kibol2_max_attack
        $ akane_hp_now = akane_hp
        $ akane_min_attack_now = akane_min_attack
        $ akane_max_attack_now = akane_max_attack
        $ akane_min_attack_now_true = akane_min_attack
        $ akane_max_attack_now_true = akane_max_attack

        $ kibol1_pager = 0
        $ kibol2_pager = 0
        $ akane_pager = 0
        $ pager_boom = 0

        $ kibol1_uszy = 0
        $ kibol2_uszy = 0
        $ akane_uszy = 0

        $ kibol1_slime = 0
        $ kibol2_slime = 0
        $ akane_slime = 0

        $ kibol1_weapon = 1
        $ akane_weapon = 1
        $ kibol2_weapon = 1

        $ kibol1_obrona = 0
        $ kibol2_obrona = 0
        $ akane_obrona = 0

        $ kibol1_umarty = 0
        $ kibol2_umarty = 0
        $ akane_umarty = 0

        $ kibol1_poison = 0
        $ kibol1_stun = 0
        $ kibol2_poison = 0
        $ kibol2_stun = 0
        $ akane_poison = 0
        $ akane_stun = 0

        jump after_fight1
