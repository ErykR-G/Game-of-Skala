
label kazuma:
    label kazuma1:
        scene ss1 with fade
        play music "audio/music/ryby.mp3"
        show luszcz neutral at left
        kazuma "Siema, przyszedłeś połowić?"

        menu:
            "{b}Chcę połowić{/b}":
                luszcz "Chętnie."

                play sound "audio/sfx/start.mp3"

                scene ss2

            "{b}Nie chcę połowić{/b}":
                luszcz "Nie, tak się tylko rozglądam."

                kazuma "Szkoda, wartościowe śmieci można tu wyłowić."

                if timer >= 360 and timer <= 1200 or timer >= 1800 and timer <= 2640 or timer >= 3240 and timer <= 4080 or timer >= 4680 and timer <= 5520 or timer >= 6120 and timer <= 6960 or timer >= 7560 and timer <= 8400 or timer >= 9000 and timer <= 9840 or timer >= 10440 and timer <= 11280:
                    play music "audio/music/pole.mp3"
                else:
                    play music "audio/music/pole_noc.mp3"
                jump granica

        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"

        kazuma "o!"

        play sound "audio/sfx/powrot.mp3"

        scene ss3

        kazuma "Jackpot!"

        kazuma "Skąd to jezioro ma w ogóle takie rzeczy?"

        play sound "audio/sfx/beta.mp3"
        scene ss4
        luszcz "Dobre pytanie"
        luszcz "Długo tu już siedzisz?"

        play sound "audio/sfx/start.mp3"
        scene ss5

        kazuma "Nie no, jakoś z dwie godzinki."

        luszcz "huh."
        luszcz "To musisz mieć dużo szczęścia"

        kazuma "Yup."

        "{i}.{/i}"
        "{i}.{/i}"
        "{i}.{/i}"

        luszcz "o!"

        play sound "audio/sfx/powrot.mp3"
        scene ss6

        luszcz "Patż, Grzegorz!"
        luszcz "Schowam go do kieszeni."

        play sound "audio/sfx/beta.mp3"
        scene ss7

        kazuma "Fajny,"
        kazuma "fajny pies."

        play sound "audio/sfx/start.mp3"
        scene ss5

        luszcz "W ogóle czemu tu tak hurtowo łowisz?"

        kazuma "Nie wiem czy powinienem o tym mówić na głos"
        kazuma "Skąd mam wiedzieć że nie wygadasz?"

        luszcz "Uszy słyszą oczy widzą usta milczą"
        luszcz "Śmierć konfidentom!"

        kazuma "W takim razie dobra"
        kazuma "Ogółem to po mojej ostatniej przygodzie popadłem w ogromny dług"
        kazuma "Zazwyczaj spłacam długi idąc na kolejne przygody i dorabiając się na nich,"
        kazuma "Ale tym razem nigdzie nie widzę żadnego srogo płacącego questa"
        kazuma "Więc muszę znaleźć nowe sposoby na pieniądze."
        kazuma "Akurat tutaj mają darmowe wędki, więc zacząłem od łowienia."
        kazuma "Potem spróbuję sprzedać cały ten grat i potęgować zysk w kasynie"
        kazuma "O, i nie wiem czy wspomniałem ale ściga mnie urząd skarbowy."

        luszcz "Ciekawe masz rzycie."
        luszcz "Ale serio, nie spodziewałbym się nigdy że morzna tu wyłowić tyle rzeczy. Muszę zacząć tu wracać."

        kazuma "Ostrzegam, że raczej nie wyłowisz ćwiartki tego co ja, ale yeah. Sam się nie spodziewałem takich wyników. Nawet nie wiem jak to przenieść."
        kazuma "A w ogóle to czym ty się w życiu zajmujesz?"

        luszcz "Jestem na misji!"
        luszcz "Ksiądz na ostatniej mszy ogłosił że w najblirzszą niedzielę Skała zostanie pochłonienta przez Kraków."
        luszcz "Drań robi to czysto dla zarobku! Nie ma powodu żeby oddawać im naszą niepodległość!"

        kazuma "Kraków? Tutaj?!"
        kazuma "W Krakowie szukają mnie za moje długi! Dopiero co udało mi się uciec!"
        kazuma "Gdybym mógł to bym ci pomógł w twojej sprawie, ale muszę najpierw postawić się na nogi."

        luszcz "Spoko sam, fakt że jesteś po mojej stronie to durzo."
        luszcz "btw mam na imie Łuszcz, a ty?"

        kazuma "Nazywam się Kazuma."

        trump "Tak, brązowowłosy animochłopiec poszedł w tą stronę."
        trump "Teraz poproszę o tego piątaka."

        kazuma "Chwila… co?"

        scene bg jezioro
        show kazuma neutral right at left 
        show luszcz neutral at slightleft
        show policja1 neutral at slightright
        show policja2 neutral at right

        ""

        us "Czy jest tu jakiś Kazuma Sato?"

        show kazuma neutral right at slightleft
        show luszcz neutral at left

        kazuma "Tak, jestem Kazuma."
        kazuma "Znaczy!! Um….!!"

        us "Proszę się nie ruszać! Rączki do góry!"

        kazuma "Nie no bez jaj, jak mnie tak szybko znaleźliście?"

        us "Dostaliśmy donosicielski telefon na pana! Jest pan aresztowany!"

        kazuma "Nie wierzę! To ty!?"

        luszcz "Przecież widziałeś że ciągle byłem koło ciebie!"

        kazuma "To weź bądź kolega i mi tu pomóż!"

        luszcz "Dobra dobra"
        luszcz "Z psami zawsze powalcze"

        jump after_fight161
        jump fight161
        label after_fight161:
