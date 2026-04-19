import tkinter as tk

buttons = [[None, None, None] for _ in range(3)]

def snow_mode_selection():
    mode_window = tk.Toplevel(window)
    mode_window.title("Режимы:")
    mode_window.resizable(False, False)
    mode_window.geometry("300x300")
    center_window(mode_window)
    mode_window.configure(bg="#1a1a2e")
    mode_window.grab_set()

    tk.Label(mode_window,text="Крестики нолики", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold")).pack(pady=(10, 0))

    tk.Label(mode_window,text="Выберите Режим игры:", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold")).pack(pady=(10, 0))

    tk.Button(
        mode_window,
        text="P vs P",
        font=("Courier", 12),
        ##command=,
        width=20,
        cursor="hand2",
        fg="white",
        bg="#463075"
    ).pack(pady=5)
    tk.Button(
        mode_window,
        text="P vs Computer",
        font=("Courier", 12),
        ##command=,
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

def make_button(row, colum):
    def click():
        pass
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

text2 = tk.Label(text="Выберите Режим игры:", bg="#1a1a2e", fg="white", font=("Courier", 12, "bold"))
text2.pack(pady=(10,0))

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
    ##command=,
    bg="#463075",
    fg="white",
    font=("Courier", 12, "bold"),
    cursor="hand2"
)
new_game_button.pack(pady=5, padx=10, side="left")


new_game_button = tk.Button(
    button_frame,
    text="Сменить режим",
    ##command=,
    bg="#463075",
    fg="white",
    font=("Courier", 12, "bold"),
    cursor="hand2"
)
new_game_button.pack(pady=5, padx=10, side="right")


window.after(100,snow_mode_selection)

window.mainloop()