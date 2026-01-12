style dmg_text:
    size 13
    color "#dddddd"
    outlines [(1, "#00000080", 0, 0)]

screen kibol1_stats():
    fixed:
        xpos 0.76
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value kibol1_hp_now range kibol1_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kibol1_hp_now/kibol1_hp > 0.5 else
                                "#ffcc00" if kibol1_hp_now/kibol1_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kibol1_hp_now]/[kibol1_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kibol1_min_attack_now]-[kibol1_max_attack_now]" style "dmg_text" xalign 0.5

screen akane_stats():
    fixed:
        xpos 0.89
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value akane_hp_now range akane_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if akane_hp_now/akane_hp > 0.5 else
                                "#ffcc00" if akane_hp_now/akane_hp > 0.2 else
                                "#ff0000"
                            )

                text "[akane_hp_now]/[akane_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [akane_min_attack_now]-[akane_max_attack_now]" style "dmg_text" xalign 0.5

screen kibol2_stats():
    fixed:
        xpos 0.76
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value kibol2_hp_now range kibol2_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kibol2_hp_now/kibol2_hp > 0.5 else
                                "#ffcc00" if kibol2_hp_now/kibol2_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kibol2_hp_now]/[kibol2_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kibol2_min_attack_now]-[kibol2_max_attack_now]" style "dmg_text" xalign 0.5


screen emina_stats():
    fixed:
        xpos 0.89
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value emina_hp_now range emina_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if emina_hp_now/emina_hp > 0.5 else
                                "#ffcc00" if emina_hp_now/emina_hp > 0.2 else
                                "#ff0000"
                            )

                text "[emina_hp_now]/[emina_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [emina_min_attack_now]-[emina_max_attack_now]" style "dmg_text" xalign 0.5








screen luszcz1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value luszcz_hp_now range luszcz_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if luszcz_hp_now/luszcz_hp > 0.5 else
                                "#ffcc00" if luszcz_hp_now/luszcz_hp > 0.2 else
                                "#ff0000"
                            )

                text "[luszcz_hp_now]/[luszcz_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [luszcz_min_attack_now]-[luszcz_max_attack_now]" style "dmg_text" xalign 0.5

screen eminem1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value eminem_hp_now range eminem_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if eminem_hp_now/eminem_hp > 0.5 else
                                "#ffcc00" if eminem_hp_now/eminem_hp > 0.2 else
                                "#ff0000"
                            )

                text "[eminem_hp_now]/[eminem_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [eminem_min_attack_now]-[eminem_max_attack_now]" style "dmg_text" xalign 0.5

screen urban1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value urban_hp_now range urban_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if urban_hp_now/urban_hp > 0.5 else
                                "#ffcc00" if urban_hp_now/urban_hp > 0.2 else
                                "#ff0000"
                            )

                text "[urban_hp_now]/[urban_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [urban_min_attack_now]-[urban_max_attack_now]" style "dmg_text" xalign 0.5

screen zyd1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value zyd_hp_now range zyd_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if zyd_hp_now/zyd_hp > 0.5 else
                                "#ffcc00" if zyd_hp_now/zyd_hp > 0.2 else
                                "#ff0000"
                            )

                text "[zyd_hp_now]/[zyd_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [zyd_min_attack_now]-[zyd_max_attack_now]" style "dmg_text" xalign 0.5

screen kazuma1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value kazuma_hp_now range kazuma_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kazuma_hp_now/kazuma_hp > 0.5 else
                                "#ffcc00" if kazuma_hp_now/kazuma_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kazuma_hp_now]/[kazuma_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kazuma_min_attack_now]-[kazuma_max_attack_now]" style "dmg_text" xalign 0.5   

screen tarczownik1_stats():
    fixed:
        xpos 0.24
        ypos 0.44  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value tarczownik_hp_now range tarczownik_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if tarczownik_hp_now/tarczownik_hp > 0.5 else
                                "#ffcc00" if tarczownik_hp_now/tarczownik_hp > 0.2 else
                                "#ff0000"
                            )

                text "[tarczownik_hp_now]/[tarczownik_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [tarczownik_min_attack_now]-[tarczownik_max_attack_now]" style "dmg_text" xalign 0.5

screen luszcz2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value luszcz_hp_now range luszcz_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if luszcz_hp_now/luszcz_hp > 0.5 else
                                "#ffcc00" if luszcz_hp_now/luszcz_hp > 0.2 else
                                "#ff0000"
                            )

                text "[luszcz_hp_now]/[luszcz_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [luszcz_min_attack_now]-[luszcz_max_attack_now]" style "dmg_text" xalign 0.5

screen eminem2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value eminem_hp_now range eminem_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if eminem_hp_now/eminem_hp > 0.5 else
                                "#ffcc00" if eminem_hp_now/eminem_hp > 0.2 else
                                "#ff0000"
                            )

                text "[eminem_hp_now]/[eminem_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [eminem_min_attack_now]-[eminem_max_attack_now]" style "dmg_text" xalign 0.5

screen urban2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value urban_hp_now range urban_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if urban_hp_now/urban_hp > 0.5 else
                                "#ffcc00" if urban_hp_now/urban_hp > 0.2 else
                                "#ff0000"
                            )

                text "[urban_hp_now]/[urban_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [urban_min_attack_now]-[urban_max_attack_now]" style "dmg_text" xalign 0.5

screen zyd2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value zyd_hp_now range zyd_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if zyd_hp_now/zyd_hp > 0.5 else
                                "#ffcc00" if zyd_hp_now/zyd_hp > 0.2 else
                                "#ff0000"
                            )

                text "[zyd_hp_now]/[zyd_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [zyd_min_attack_now]-[zyd_max_attack_now]" style "dmg_text" xalign 0.5

screen kazuma2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value kazuma_hp_now range kazuma_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kazuma_hp_now/kazuma_hp > 0.5 else
                                "#ffcc00" if kazuma_hp_now/kazuma_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kazuma_hp_now]/[kazuma_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kazuma_min_attack_now]-[kazuma_max_attack_now]" style "dmg_text" xalign 0.5

screen tarczownik2_stats():
    fixed:
        xpos 0.24
        ypos 0.945  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value tarczownik_hp_now range tarczownik_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if tarczownik_hp_now/tarczownik_hp > 0.5 else
                                "#ffcc00" if tarczownik_hp_now/tarczownik_hp > 0.2 else
                                "#ff0000"
                            )

                text "[tarczownik_hp_now]/[tarczownik_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [tarczownik_min_attack_now]-[tarczownik_max_attack_now]" style "dmg_text" xalign 0.5

screen luszcz3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value luszcz_hp_now range luszcz_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if luszcz_hp_now/luszcz_hp > 0.5 else
                                "#ffcc00" if luszcz_hp_now/luszcz_hp > 0.2 else
                                "#ff0000"
                            )

                text "[luszcz_hp_now]/[luszcz_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [luszcz_min_attack_now]-[luszcz_max_attack_now]" style "dmg_text" xalign 0.5

screen eminem3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value eminem_hp_now range eminem_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if eminem_hp_now/eminem_hp > 0.5 else
                                "#ffcc00" if eminem_hp_now/eminem_hp > 0.2 else
                                "#ff0000"
                            )

                text "[eminem_hp_now]/[eminem_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [eminem_min_attack_now]-[eminem_max_attack_now]" style "dmg_text" xalign 0.5

screen urban3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value urban_hp_now range urban_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if urban_hp_now/urban_hp > 0.5 else
                                "#ffcc00" if urban_hp_now/urban_hp > 0.2 else
                                "#ff0000"
                            )

                text "[urban_hp_now]/[urban_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [urban_min_attack_now]-[urban_max_attack_now]" style "dmg_text" xalign 0.5

screen zyd3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value zyd_hp_now range zyd_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if zyd_hp_now/zyd_hp > 0.5 else
                                "#ffcc00" if zyd_hp_now/zyd_hp > 0.2 else
                                "#ff0000"
                            )

                text "[zyd_hp_now]/[zyd_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [zyd_min_attack_now]-[zyd_max_attack_now]" style "dmg_text" xalign 0.5

screen kazuma3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value kazuma_hp_now range kazuma_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kazuma_hp_now/kazuma_hp > 0.5 else
                                "#ffcc00" if kazuma_hp_now/kazuma_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kazuma_hp_now]/[kazuma_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kazuma_min_attack_now]-[kazuma_max_attack_now]" style "dmg_text" xalign 0.5

screen tarczownik3_stats():
    fixed:
        xpos 0.11
        ypos 0.695  
        xanchor 0.5

        vbox:
            spacing 4
            xalign 0.5

            fixed:
                xalign 0.5
                xsize 200 
                ysize 14

                bar value tarczownik_hp_now range tarczownik_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if tarczownik_hp_now/tarczownik_hp > 0.5 else
                                "#ffcc00" if tarczownik_hp_now/tarczownik_hp > 0.2 else
                                "#ff0000"
                            )

                text "[tarczownik_hp_now]/[tarczownik_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [tarczownik_min_attack_now]-[tarczownik_max_attack_now]" style "dmg_text" xalign 0.5