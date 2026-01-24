
label kazuma:
    label kazuma1:
        scene bg jezioro with fade
        play music "audio/music/ryby.mp3"
        show luszcz neutral right at slightright
        show kazuma neutral right at left

        kazuma "Siema, przyszedłeś połowić?"

        menu:
            "{b}Chcę połowić{/b}":
                luszcz "Chętnie."

                show luszcz siedzi right at center

            "{b}Nie chcę połowić{/b}":
                luszcz "Nie, tak się tylko rozglądam."

                kazuma "Szkoda, wartościowe śmieci można tu wyłowić."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump wolbromska

        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"

        kazuma "o!"