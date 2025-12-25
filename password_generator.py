from zxcvbn import zxcvbn
import tkinter as tk
from tkinter import ttk

BG = "#1e1e1e"
ENTRY_BG = "#2a2a2a"
ENTRY_FG = "#ffffff"

root = tk.Tk()
root.geometry("1280x720")
root.title("Password Generator")
root.configure(bg=BG)

root.grid_columnconfigure(0, weight=1)

row_frame = tk.Frame(root, bg=BG)
row_frame.grid(row=3, column=0, pady=40)

def generate():
    import secrets
    import string

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(14))
    var.set(password)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Blue.Horizontal.TProgressbar",
    troughcolor="#333333",
    background="#2d7dff",
    thickness=12
)

def on_change(*args):
    results = zxcvbn(var.get())
    score_map = {0: 10, 1: 30, 2: 50, 3: 70, 4: 100}
    progressbar["value"] = score_map.get(results["score"], 0)

var = tk.StringVar()

entry = tk.Entry(
    row_frame,
    textvariable=var,
    justify="center",
    width=50,
    bg=ENTRY_BG,
    fg=ENTRY_FG,
    insertbackground=ENTRY_FG
)
entry.grid(row=0, column=0, padx=(0, 4))

dice = tk.PhotoImage(file="dice.png")
dice_small = dice.subsample(5, 5)

dice1 = tk.Button(
    row_frame,
    image=dice_small,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2",
    command=generate
)
dice1.grid(row=0, column=1)

progressbar = ttk.Progressbar(
    root,
    orient="horizontal",
    mode="determinate",
    length=300,
    maximum=100,
    style="Blue.Horizontal.TProgressbar"
)
progressbar.grid(row=4, column=0, pady=(0, 20))

var.trace_add("write", on_change)
entry.focus_set()
root.mainloop()
