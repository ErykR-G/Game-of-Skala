style dmg_text:
    size 13
    color "#dddddd"
    outlines [(1, "#00000080", 0, 0)]

screen kartaginczyk1_stats():
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

                bar value kartaginczyk1_hp_now range kartaginczyk1_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kartaginczyk1_hp_now/kartaginczyk1_hp > 0.5 else
                                "#ffcc00" if kartaginczyk1_hp_now/kartaginczyk1_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kartaginczyk1_hp_now]/[kartaginczyk1_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kartaginczyk1_min_attack_now]-[kartaginczyk1_max_attack_now]" style "dmg_text" xalign 0.5

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

screen kartaginczyk1_stats():
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

                bar value kartaginczyk1_hp_now range kartaginczyk1_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kartaginczyk1_hp_now/kartaginczyk1_hp > 0.5 else
                                "#ffcc00" if kartaginczyk1_hp_now/kartaginczyk1_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kartaginczyk1_hp_now]/[kartaginczyk1_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kartaginczyk1_min_attack_now]-[kartaginczyk1_max_attack_now]" style "dmg_text" xalign 0.5

screen tanya_stats():
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

                bar value tanya_hp_now range tanya_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if tanya_hp_now/tanya_hp > 0.5 else
                                "#ffcc00" if tanya_hp_now/tanya_hp > 0.2 else
                                "#ff0000"
                            )

                text "[tanya_hp_now]/[tanya_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [tanya_min_attack_now]-[tanya_max_attack_now]" style "dmg_text" xalign 0.5

screen kartaginczyk2_stats():
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

                bar value kartaginczyk2_hp_now range kartaginczyk2_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if kartaginczyk2_hp_now/kartaginczyk2_hp > 0.5 else
                                "#ffcc00" if kartaginczyk2_hp_now/kartaginczyk2_hp > 0.2 else
                                "#ff0000"
                            )

                text "[kartaginczyk2_hp_now]/[kartaginczyk2_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [kartaginczyk2_min_attack_now]-[kartaginczyk2_max_attack_now]" style "dmg_text" xalign 0.5

screen gnom1_stats():
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

                bar value gnom1_hp_now range gnom1_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if gnom1_hp_now/gnom1_hp > 0.5 else
                                "#ffcc00" if gnom1_hp_now/gnom1_hp > 0.2 else
                                "#ff0000"
                            )

                text "[gnom1_hp_now]/[gnom1_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [gnom1_min_attack_now]-[gnom1_max_attack_now]" style "dmg_text" xalign 0.5

screen gnom2_stats():
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

                bar value gnom2_hp_now range gnom2_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if gnom2_hp_now/gnom2_hp > 0.5 else
                                "#ffcc00" if gnom2_hp_now/gnom2_hp > 0.2 else
                                "#ff0000"
                            )

                text "[gnom2_hp_now]/[gnom2_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [gnom2_min_attack_now]-[gnom2_max_attack_now]" style "dmg_text" xalign 0.5

screen gnom3_stats():
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

                bar value gnom3_hp_now range gnom3_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if gnom3_hp_now/gnom3_hp > 0.5 else
                                "#ffcc00" if gnom3_hp_now/gnom3_hp > 0.2 else
                                "#ff0000"
                            )

                text "[gnom3_hp_now]/[gnom3_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [gnom3_min_attack_now]-[gnom3_max_attack_now]" style "dmg_text" xalign 0.5

screen yippee1_stats():
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

                bar value yippee1_hp_now range yippee1_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if yippee1_hp_now/yippee1_hp > 0.5 else
                                "#ffcc00" if yippee1_hp_now/yippee1_hp > 0.2 else
                                "#ff0000"
                            )

                text "[yippee1_hp_now]/[yippee1_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [yippee1_min_attack_now]-[yippee1_max_attack_now]" style "dmg_text" xalign 0.5

screen yippee2_stats():
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

                bar value yippee2_hp_now range yippee2_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if yippee2_hp_now/yippee2_hp > 0.5 else
                                "#ffcc00" if yippee2_hp_now/yippee2_hp > 0.2 else
                                "#ff0000"
                            )

                text "[yippee2_hp_now]/[yippee2_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [yippee2_min_attack_now]-[yippee2_max_attack_now]" style "dmg_text" xalign 0.5

screen ram_stats():
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

                bar value ram_hp_now range ram_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if ram_hp_now/ram_hp > 0.5 else
                                "#ffcc00" if ram_hp_now/ram_hp > 0.2 else
                                "#ff0000"
                            )

                text "[ram_hp_now]/[ram_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [ram_min_attack_now]-[ram_max_attack_now]" style "dmg_text" xalign 0.5

screen rem_stats():
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

                bar value rem_hp_now range rem_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if rem_hp_now/rem_hp > 0.5 else
                                "#ffcc00" if rem_hp_now/rem_hp > 0.2 else
                                "#ff0000"
                            )

                text "[rem_hp_now]/[rem_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [rem_min_attack_now]-[rem_max_attack_now]" style "dmg_text" xalign 0.5

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

screen czarny_stats():
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

                bar value czarny_hp_now range czarny_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if czarny_hp_now/czarny_hp > 0.5 else
                                "#ffcc00" if czarny_hp_now/czarny_hp > 0.2 else
                                "#ff0000"
                            )

                text "[czarny_hp_now]/[czarny_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [czarny_min_attack_now]-[czarny_max_attack_now]" style "dmg_text" xalign 0.5

screen braun_stats():
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

                bar value braun_hp_now range braun_hp xsize 200 ysize 14:
                    left_bar Solid(
                                "#00cc00" if braun_hp_now/braun_hp > 0.5 else
                                "#ffcc00" if braun_hp_now/braun_hp > 0.2 else
                                "#ff0000"
                            )

                text "[braun_hp_now]/[braun_hp]" size 12 color "#ffffff" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

            text "ATK: [braun_min_attack_now]-[braun_max_attack_now]" style "dmg_text" xalign 0.5





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