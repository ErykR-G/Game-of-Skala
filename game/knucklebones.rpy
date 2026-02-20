init python:
    import random

    # --- KONFIGURACJA ---
    ROWS = 3
    COLS = 3

    knuckle_turn = "player"
    current_die = 1
    knucklebones_finished = False

    player_board = [[] for _ in range(COLS)]
    enemy_board = [[] for _ in range(COLS)]

    # --- FUNKCJE GRY ---
    def roll_die():
        return random.randint(1, 6)

    def total_score(board):
        return sum(column_score(col) for col in board)


    # Oblicza sumę kolumny z mnożnikami za powtarzające się wartości
    def column_score(col):
        total = 0
        for val in col:
            count = col.count(val)  # ile razy dana liczba występuje w kolumnie
            total += val * count
        return total



    def board_full(board):
        # Plansza pełna, jeśli każda kolumna ma ROWS elementów
        for col in board:
            if len(col) < ROWS:
                return False
        return True

    def remove_matches(board, col_idx, die):
        if col_idx < 0 or col_idx >= COLS:
            return
        board[col_idx] = [x for x in board[col_idx] if x != die]

    def ai_choose_column(die, enemy_board, player_board):
        valid = [i for i in range(COLS) if len(enemy_board[i]) < ROWS]
        if not valid:
            return None

        # spróbuj zbić kości gracza
        for i in valid:
            if die in player_board[i]:
                return i
        # spróbuj combo u siebie
        for i in valid:
            if die in enemy_board[i]:
                return i
        # najmniej zapełniona kolumna
        valid.sort(key=lambda i: len(enemy_board[i]))
        return valid[0]

    def finish_knucklebones():
        global knucklebones_finished
        knucklebones_finished = True
        renpy.hide_screen("knucklebones")
        # zamiast renpy.end_interaction(None) po prostu:
        renpy.restart_interaction()


    def player_move(col):
        global knuckle_turn, current_die
        if knuckle_turn != "player" or len(player_board[col]) >= ROWS:
            return
        player_board[col].append(current_die)
        remove_matches(enemy_board, col, current_die)

        # sprawdź koniec gry
        if board_full(player_board) or board_full(enemy_board):
            finish_knucklebones()
            return

        current_die = roll_die()
        knuckle_turn = "enemy"
        renpy.restart_interaction()  # odśwież ekran po ruchu gracza

    def enemy_turn():
        global knuckle_turn, current_die
        if board_full(enemy_board) or board_full(player_board):
            finish_knucklebones()
            return

        current_die = roll_die()
        col = ai_choose_column(current_die, enemy_board, player_board)

        if col is None:
            finish_knucklebones()
            return

        enemy_board[col].insert(0, current_die)
        remove_matches(player_board, col, current_die)

        if board_full(enemy_board) or board_full(player_board):
            finish_knucklebones()
            return

        current_die = roll_die()
        knuckle_turn = "player"
        renpy.restart_interaction()

# --- SCREEN POJEDYNCZEGO POLA ---
screen knuckle_cell(value=None):
    frame:
        xsize 64
        ysize 64
        padding (0,0)
        background Frame(
            Solid("#444" if value is not None else "#222"),
            2, 2
        )
        if value is not None:
            text str(value) size 28 xalign 0.5 yalign 0.5

# --- GŁÓWNY SCREEN MINIGRY ---
screen knucklebones():
    modal True
    tag knucklebones
    zorder 100

    add Solid("#111")  # tło całego ekranu

    frame:
        xfill True
        yfill True
        padding (60, 40)
        background None

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            # --- PLANSZA PRZECIWNIKA ---
            hbox:
                spacing 10
                xalign 0.5
                text "PRZECIWNIK" size 22
                text "[total_score(enemy_board)]" size 22


            hbox:
                spacing 40
                xalign 0.5
                for i in range(COLS):
                    vbox:
                        spacing 6
                        xsize 70

                        # pola przeciwnika od dołu do góry
                        for r in range(ROWS):
                            $ idx = ROWS - 1 - r
                            if idx < len(enemy_board[i]):
                                use knuckle_cell(enemy_board[i][idx])
                            else:
                                use knuckle_cell()

                        # suma kolumny przeciwnika
                        fixed:
                            xsize 70
                            ysize 30
                            text "[column_score(enemy_board[i])]" xalign 0.5 yalign 0.5

            # --- RZUT KOŚCI ---
            frame:
                xsize 220
                ysize 60
                xalign 0.5
                background Frame(Solid("#222"),4,4)
                text "RZUT: [current_die]" size 28 xalign 0.5 yalign 0.5

            # --- PLANSZA GRACZA ---
            hbox:
                spacing 40
                xalign 0.5
                for i in range(COLS):
                    vbox:
                        spacing 6
                        xsize 70

                        # pola gracza od góry do dołu
                        for r in range(ROWS):
                            if r < len(player_board[i]):
                                use knuckle_cell(player_board[i][r])
                            else:
                                button:
                                    background None
                                    xsize 64
                                    ysize 64
                                    action Function(player_move, i)
                                    add Solid("#222")

                        # suma kolumny gracza
                        fixed:
                            xsize 70
                            ysize 30
                            text "[column_score(player_board[i])]" xalign 0.5 yalign 0.5

            # napis GRACZ + punkty pod planszą
            hbox:
                spacing 10
                xalign 0.5
                text "GRACZ" size 22
                text "- [total_score(player_board)]" size 22


    # --- TIMER DO RUCHU AI ---
    if knuckle_turn == "enemy":
        timer 0.5 action Function(enemy_turn)


screen knucklebones_summary(player_points, enemy_points):
    modal True
    tag knucklebones_summary
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 50)
        background Frame(Solid("#111"), 6, 6)

        vbox:
            spacing 30
            xalign 0.5

            text "KONIEC GRY!" size 36

            hbox:
                spacing 50
                xalign 0.5
                text "GRACZ: [player_points]" size 28
                text "PRZECIWNIK: [enemy_points]" size 28

            if player_points > enemy_points:
                text "WYGRYWA GRACZ!" size 32 color "#0f0"
            elif enemy_points > player_points:
                text "WYGRYWA PRZECIWNIK!" size 32 color "#f00"
            else:
                text "REMIS!" size 32 color "#ff0"

            textbutton "Dalej" action Jump("wyniczki")

                        
label play_knucklebones:
    $ player_board = [[] for _ in range(COLS)]
    $ enemy_board = [[] for _ in range(COLS)]
    $ knuckle_turn = "player"
    $ current_die = roll_die()
    $ knucklebones_finished = False

    show screen knucklebones

    # pętla minigry
    while not knucklebones_finished:
        if knuckle_turn == "enemy":
            $ enemy_turn()
        $ renpy.pause(0.1, hard=True)

    hide screen knucklebones

    # --- POKAŻ PODSUMOWANIE ---
    show screen knucklebones_summary(total_score(player_board), total_score(enemy_board))

    $ renpy.pause(2)  # opcjonalnie, żeby chwilę pokazało
    hide screen knucklebones_summary

label wyniczki:
    hide screen knucklebones_summary
    if total_score(player_board) >= total_score(enemy_board):
        jump wygranko_kasyno
    else:
        jump przegranko_kasyno

