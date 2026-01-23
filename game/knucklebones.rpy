
# knucklebones.rpy
init python:
    import random

    # --- KONFIGURACJA ---
    BOARD_SIZE = 3  # maksymalna liczba kości w kolumnie

    # --- STAN GRY ---
    player_board = [[] for _ in range(BOARD_SIZE)]
    ai_board = [[] for _ in range(BOARD_SIZE)]
    player_turn = True
    current_die = 1
    player_score = 0
    ai_score = 0

    # --- FUNKCJE POMOCNICZE ---
    def board_full(board):
        return all(len(col) >= BOARD_SIZE for col in board)

    def column_score(col):
        """Zwraca sumę kolumny z mnożnikami za powtarzające się kości"""
        if not col:
            return 0
        score = 0
        counts = {}
        for val in col:
            counts[val] = counts.get(val, 0) + 1
        for val, count in counts.items():
            score += val * count
        return score

    def board_score(board):
        return sum(column_score(col) for col in board)

    def remove_from_column(board, col_index, value):
        """AI usuwa przeciwnika z kolumny jeśli potrzebne (opcjonalnie)"""
        if board[col_index]:
            # przykładowa prosta logika AI, można zmienić na trudniejszą
            pass

    def player_place(col):
        global player_turn, current_die, player_score, ai_score

        # dodaj kość gracza
        if len(player_board[col]) < BOARD_SIZE:
            player_board[col].append(current_die)

        # odśwież punktację
        player_score = board_score(player_board)
        ai_score = board_score(ai_board)

        # Zakończ grę jeśli pełna plansza
        if board_full(player_board) or board_full(ai_board):
            renpy.jump("knucklebones_end")
            return

        player_turn = False

        # AI ruszy się po chwili
        renpy.call_in_new_context("ai_turn_delayed")


    def ai_turn():
        global player_turn, current_die, player_score, ai_score
        # prosta AI: losowa kolumna
        options = [i for i in range(BOARD_SIZE) if len(ai_board[i]) < BOARD_SIZE]
        if options:
            col = random.choice(options)
            ai_board[col].append(random.randint(1, 6))
        # odśwież punkty
        player_score = board_score(player_board)
        ai_score = board_score(ai_board)
        player_turn = True
        # wylosuj nowy rzut dla gracza
        global current_die
        current_die = random.randint(1, 6)


# --- OPÓŹNIONY RUCH AI ---
label ai_turn_delayed:
    $ renpy.pause(0.6)
    $ ai_turn()
    return


# --- EKRAN KNUCKLEBONES ---
screen knucklebones():
    tag knucklebones
    zorder 5

    # Tło planszy
    add Solid("#120808")

    # Wyświetl rzut kości
    text "Rzut kości: [current_die]" size 28 xalign 0.5 yalign 0.02 color "#ffffff"

    vbox:
        spacing 50
        xalign 0.5
        yalign 0.5

        # ========================
        # AI U GÓRY
        # ========================
        vbox:
            spacing 10
            xalign 0.5

            $ ai_label = "PRZECIWNIK: {}".format(ai_score)
            text ai_label size 34 color "#ff6666" xalign 0.5

            hbox:
                spacing 30
                for col in range(BOARD_SIZE):
                    vbox:
                        spacing 6

                        # pola AI
                        for row in range(BOARD_SIZE):
                            $ value = ai_board[col][row] if row < len(ai_board[col]) else None
                            frame:
                                xsize 80
                                ysize 80
                                background "#3a1010"
                                text (str(value) if value else "") size 34 xalign 0.5 yalign 0.5

                        # suma kolumny AI (pod planszą)
                        text str(column_score(ai_board[col])) size 24 color "#ff9999" xalign 0.5

        # ========================
        # GRACZ U DOŁU
        # ========================
        vbox:
            spacing 10
            xalign 0.5

            hbox:
                spacing 30
                for col in range(BOARD_SIZE):
                    vbox:
                        spacing 6

                        # suma kolumny gracza (nad planszą)
                        text str(column_score(player_board[col])) size 24 xalign 0.5

                        button:
                            action If(
                                player_turn and len(player_board[col]) < BOARD_SIZE,
                                Function(player_place, col),
                                NullAction()
                            )
                            xpadding 0
                            ypadding 0

                            vbox:
                                spacing 6
                                for row in range(BOARD_SIZE):
                                    $ value = player_board[col][row] if row < len(player_board[col]) else None
                                    frame:
                                        xsize 80
                                        ysize 80
                                        background "#2b1a1a"
                                        text (str(value) if value else "") size 34 xalign 0.5 yalign 0.5

            $ player_label = "GRACZ: {}".format(player_score)
            text player_label size 34 color "#ffffff" xalign 0.5


# --- KONIEC GRY ---
label knucklebones_end:
    $ winner = "GRACZ" if player_score >= ai_score else "PRZECIWNIK"
    "Koniec gry! Wygrywa [winner]!"
    return


# --- START GRY ---
label start_knucklebones:
    # Wylosuj pierwszy rzut kości dla gracza
    $ current_die = random.randint(1, 6)
    show screen knucklebones
    # Teraz plansza działa cały czas, bez dialogui
    return
