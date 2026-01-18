
label tarczownik:
    label tarczownik1:
        $ tarczownik_social_link = 1
        play music "audio/music/pole.mp3"
        scene bg wolbromska with fade
        show luszcz neutral zorder 11 at left

        $ renpy.pause(0.5)

        show pies woof at center:
            xalign 1.5
            yalign 1.0
            easeout 0.6 xalign 0.7
        
        $ renpy.pause(0.5)

        pies "woof woof XP rawr"
        luszcz "O kurde furas na wolności"

        show pies woof at center:
            xalign 0.7
            yalign 1.0
            easeout 0.6 xalign -0.5

        $ renpy.pause(1.0)

        show tarczownik neutral at slightright:
            xalign 1.5
            yalign 1.0
            easeout 0.6 xalign 0.7
        
        $ renpy.pause(0.5)

        tarczownik "Ej ty! Widziałeś Raphtalie?"

        luszcz "Tego psa?"

        tarczownik "To bardziej coś typu szopa ale tak"

        luszcz "Pobiegł na lewo, a potem w prawo"

        tarczownik "Okej dzięki"

        show tarczownik neutral at center:
            xalign 0.7
            yalign 1.0
            easeout 0.6 xalign -0.5
        
        $ renpy.pause(0.5)

        luszcz "W sumie morznaby za nim pobiec"

        menu:
            "{b}Pobiegnij za nim (5h){/b}":
                $ timer += 300
                show luszcz neutral at center:
                    xalign 0.0
                    yalign 1.0
                    easeout 0.6 xalign -0.5
            
                $ renpy.pause(1.0)

     
            "{b}Nie chce mi się{/b}":
                luszcz "Niech sobie frajer sam lata za swoim psem"

                $ tarczownik_wybory = 0
                $ tarczownik_social_link = 10
                jump wolbromska

        play music "audio/music/natura.mp3"
        scene bg black with fade
        scene bg las with fade

        show pies woof at right

        $ renpy.pause(0.5)

        show tarczownik neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.4
        
        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.05

        tarczownik "Raptylja! Do nogi!!!"

        pies "Hał hał xd"

        tarczownik "Wracaj tu!!"

        luszcz "ale mentzonce bieganko"

        show pies woof at center:
            xalign 1.0
            yalign 1.0
            easeout 0.6 xalign 1.5

        $ renpy.pause(0.3)

        show tarczownik neutral at center:
            xalign 0.4
            yalign 1.0
            easeout 0.6 xalign 1.5
        
        show luszcz neutral at center:
            xalign 0.05
            yalign 1.0
            easeout 0.6 xalign 1.5
        
        $ renpy.pause(1.0)

        play music "audio/music/portal.mp3"
        scene bg portal

        show pies woof at center:
            xalign -0.5
            yalign 1.0
            easeout 0.8 xalign 1.1

        $ renpy.pause(0.5)

        show tarczownik neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.4
        
        show luszcz neutral at center:
            xalign -0.5
            yalign 1.0
            easeout 0.6 xalign 0.05
        
        $ renpy.pause(0.5)

        pies "hmm… :pp"

        tarczownik "Nie waż się!"

        luszcz "Tu zawsze był jakiś portal?"

        tarczownik "No jakoś od 1984"
        tarczownik "Zobacz sobie na mapach"
        tarczownik "Google"

        luszcz "Okej później"

        pies "dobra wskakuje xD"

        tarczownik "Raphtalia!!!!!!"

        
        show pies woof:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide pies

        $ renpy.pause(0.05)

        tarczownik "Boże…"
        tarczownik "Raaah!!!!! Nie wytrzymam bez niej!! Była moją dog girl!!!! Czemu wszyscy mnie zostawiają!!"

        luszcz "Idź po nią jak ci tak zalerzy"

        tarczownik "Jest mały problem"
        tarczownik "Ten portal prowadzi do nieskończonej ilości uniwersów, szukanie jej będzie jak igły w stogu siana"
        tarczownik "Ale z drugiej strony… nie mam nic do stracenia"

        luszcz "A czemó tak od ciebie uciekła..?"

        tarczownik "Dałem jej spróbować cytryny żeby zobaczyć jej reakcję jak w tych filmikach ze zwierzątkami"
        tarczownik "Mogłem przewidzieć że to gówno to było ai…"
        tarczownik "Weszła w szał i wybiegła z domu"

        luszcz "Głópie w ciól"
        luszcz "Ale przykre"

        tarczownik "Ehh… ide sie zabic…"

        luszcz "Nie no bez przesady"
        luszcz "Czy gdybym poszedł z tobą poszukać to zostaniesz przy żywych?"

        tarczownik "Jeśli tam od czegoś nie zginiemy to tak"

        luszcz "(Czy chcę tam z nim wskakiwać…?)"

        menu:
            "{b}Czy chcę wskoczyć do portalu?{/b}"

            "{b}Tak{/b}":
                luszcz "Dobra to ty pierwszy"
                tarczownik "Okej"

            "{b}Nie{/b}":
                luszcz "W takim razie pora umierać"
                tarczownik "Rel"

                show tarczownik gun
                $ renpy.pause(0.1)
                with vpunch
                play sound "audio/sfx/gun.mp3"
                $ renpy.pause(0.1)
                show tarczownik dead

                luszcz "Ups.."
                luszcz "To był rzarcik…"
                luszcz "Anyway"

                play music "audio/music/pole.mp3"
                $ tarczownik_wybory = 10
                $ tarczownik_social_link = 10
                jump wolbromska

        show tarczownik neutral at center:
            xalign 0.4
            yalign 1.0
            easeout 0.5 xalign 0.7
        
        $ renpy.pause(0.5)

        show tarczownik neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide tarczownik

        $ renpy.pause(0.05)

        luszcz "okej..."

        show luszcz neutral at center:
            xalign 0.05
            yalign 1.0
            easeout 0.5 xalign 0.7
        
        $ renpy.pause(0.5)

        show luszcz neutral:
            yoffset 0
            linear 0.15 yoffset -50
            linear 0.15 yoffset 0

        $ renpy.pause(0.1)
        with hpunch
        hide luszcz

        $ renpy.pause(0.05)

        scene bg inportal with pixellate
        play music "audio/music/inportal.mp3"

        luszcz "Ziuuuuu…"
        luszcz "Ej a jak masz na imie"

        tarczownik "Naofumi"

        luszcz "fajnie a ja Łuszczu"

        pies "rawr!!"

        tarczownik "Słyszałeś TO ONA!!!"

        luszcz "To chyba w tom strone..!"

