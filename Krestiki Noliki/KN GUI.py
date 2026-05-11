import tkinter as tk
from tkinter import messagebox
import random

buttons = [[None, None, None] for _ in range(3)]
board = [["","",""],
         ["","",""],
         ["","",""]
         ]
current_player = "X"
game_mode = "PvP"

def start_game(mode, window):
    global game_mode
    game_mode = mode
    window.destroy()
    reset_game()
    if game_mode == "PvP":
        current_player_text.config(text=f"Ход игрока: {current_player}")
    else:
        current_player_text.config(text=f"Ваш ход (X)")

def show_mode_selection():
    mode_window = tk.Toplevel(window)
    mode_window.title("Режимы:")
    mode_window.resizable(False, False)
    mode_window.geometry("300x300")
    center_window(mode_window)
    mode_window.configure(bg="#1a1a2e")
    mode_window.grab_set()
    current_player_text.config(text="Выберите режим игры: ")

    tk.Label(mode_window,text="Крестики нолики", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold")).pack(pady=(10, 0))

    tk.Label(mode_window,text="Выберите Режим игры:", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold")).pack(pady=(10, 0))

    def start_pvp():
        start_game("PvP", mode_window)

    def start_pvc():
        start_game("PvC", mode_window)

    tk.Button(
        mode_window,
        text="P vs P",
        font=("Courier", 12),
        command=start_pvp,
        width=20,
        cursor="hand2",
        fg="white",
        bg="#463075"
    ).pack(pady=5)
    tk.Button(
        mode_window,
        text="P vs Computer",
        font=("Courier", 12),
        command=start_pvc,
        width=20,
        cursor="hand2",
        fg="white",
        bg="#463075"
    ).pack(pady=5)


def center_window(window):
    window.update_idletasks()  # Перезагрузить данные об окне после размещения виджетов
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def check_winner(player):

    """if board[0][0] and board[0][1] and board[0][2] == player:
        return True
    if board[1][0] and board[1][1] and board[1][2] == player:
        return True
    if board[2][0] and board[2][1] and board[2][2] == player:
        return True"""

    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True

    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def reset_game():
    global board, current_player

    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]
             ]
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")

def check_draw():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False
    return True



def make_button(row, colum):
    def click():
        global current_player

        if board[row][colum] != "":
            return
        if game_mode == "PvP":
            board[row][colum] = current_player
            buttons[row][colum].config(text=current_player)
        if game_mode == "PvC":
            board[row][colum] = "X"
            buttons[row][colum].config(text="X")
            a = 0
            b = 0
            while board[a][b] != "":
                a = random.randint(0, 2)
                b = random.randint(0, 2)
            current_player = "O"
            board[a][b] = "O"
            buttons[a][b].config(text="O")
            if check_winner(current_player):
                messagebox.showinfo("Победа", f"Победил игрок {current_player}")
                reset_game()
                return
            current_player = "X"

        if check_winner(current_player):
            messagebox.showinfo("Победа", f"Победил игрок {current_player}")
            reset_game()
            return

        if check_draw():
            messagebox.showinfo("Ничья", "Произошла ничья!")
            reset_game()
            return


        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        current_player_text.config(text=f"Ход игрока: {current_player}")





    button = tk.Button(
        game_frame,
        text="",
        command=click,
        bg="grey",
        fg="white",
        width=4,
        height=2,
        font=("Courier", 36, "bold"),
        cursor="hand2"
    )
    return button


window = tk.Tk()
window.title("Крестики нолики")
window.geometry("600x680")
center_window(window)
window.resizable(width=False, height=False)
window.configure(bg="#1a1a2e")

text1 = tk.Label(text="Крестики нолики", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold"))
text1.pack(pady=(10,0))

current_player_text = tk.Label(text="Выберите Режим игры:", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold"))
current_player_text.pack(pady=(10, 0))

game_frame = tk.Frame(window, bg="#1a1a2e")
game_frame.pack(pady=20)

for r in range(3):
    for c in range(3):
        button = make_button(r, c)
        button.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = button

button_frame = tk.Frame(window, bg="#1a1a2e")
button_frame.pack(pady=20)

new_game_button = tk.Button(
    button_frame,
    text="Новая игра",
    command=reset_game,
    bg="#463075",
    fg="white",
    font=("Courier", 12, "bold"),
    cursor="hand2"
)
new_game_button.pack(pady=5, padx=10, side="left")


new_game_button = tk.Button(
    button_frame,
    text="Сменить режим",
    bg="#463075",
    fg="white",
    font=("Courier", 12, "bold"),
    cursor="hand2",
    command=show_mode_selection
)
new_game_button.pack(pady=5, padx=10, side="right")


window.after(100, show_mode_selection)

window.mainloop()