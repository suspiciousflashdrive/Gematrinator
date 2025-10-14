from tkinter import *
import tkinter as tk

ordinal = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16","Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24","Y":"25","Z":"26",
"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26",
"Α":"1","Β":"2","Γ":"3","Δ":"4","Ε":"5","Ζ":"6","Η":"7","Θ":"8","Ι":"9","Κ":"10","Λ":"11","Μ":"12","Ν":"13","Ξ":"14","Ο":"15","Π":"16","Ρ":"17","Σ":"18","Τ":"19","Υ":"20","Φ":"21","Χ":"22","Ψ":"23","Ω":"24",
"α":"1","β":"2","γ":"3","δ":"4","ε":"5","ζ":"6","η":"7","θ":"8","ι":"9","κ":"10","λ":"11","μ":"12","ν":"13","ξ":"14","ο":"15","π":"16","ρ":"17","σ":"18","ς":"18","τ":"19","υ":"20","φ":"21","χ":"22","ψ":"23","ω":"24"}

revOrdinal = {"A":"26","B":"25","C":"24","D":"23","E":"22","F":"21","G":"20","H":"19","I":"18","J":"17","K":"16","L":"15","M":"14","N":"13","O":"12","P":"11","Q":"10","R":"9","S":"8","T":"7","U":"6","V":"5","W":"4","X":"3","Y":"2","Z":"1",
"a":"26","b":"25","c":"24","d":"23","e":"22","f":"21","g":"20","h":"19","i":"18","j":"17","k":"16","l":"15","m":"14","n":"13","o":"12","p":"11","q":"10","r":"9","s":"8","t":"7","u":"6","v":"5","w":"4","x":"3","y":"2","z":"1",
"Α":"24","Β":"23","Γ":"22","Δ":"21","Ε":"20","Ζ":"19","Η":"18","Θ":"17","Ι":"16","Κ":"15","Λ":"14","Μ":"13","Ν":"12","Ξ":"11","Ο":"10","Π":"9","Ρ":"8","Σ":"7","Τ":"6","Υ":"5","Φ":"4","Χ":"3","Ψ":"2","Ω":"1",
"α":"24","β":"23","γ":"22","δ":"21","ε":"20","ζ":"19","η":"18","θ":"17","ι":"16","κ":"15","λ":"14","μ":"13","ν":"12","ξ":"11","ο":"10","π":"9","ρ":"8","σ":"7","ς":"7","τ":"6","υ":"5","φ":"4","χ":"3","ψ":"2","ω":"1"}

reduction = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"1","K":"2","L":"3","M":"4","N":"5","O":"6","P":"7","Q":"8","R":"9","S":"1","T":"2","U":"3","V":"4","W":"5","X":"6","Y":"7","Z":"8",
"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"1","k":"2","l":"3","m":"4","n":"5","o":"6","p":"7","q":"8","r":"9","s":"1","t":"2","u":"3","v":"4","w":"5","x":"6","y":"7","z":"8",
"Α":"1","Β":"2","Γ":"3","Δ":"4","Ε":"5","Ζ":"6","Η":"7","Θ":"8","Ι":"9","Κ":"1","Λ":"2","Μ":"3","Ν":"4","Ξ":"5","Ο":"6","Π":"7","Ρ":"8","Σ":"9","Τ":"1","Υ":"2","Φ":"3","Χ":"4","Ψ":"5","Ω":"6",
"α":"1","β":"2","γ":"3","δ":"4","ε":"5","ζ":"6","η":"7","θ":"8","ι":"9","κ":"1","λ":"2","μ":"3","ν":"4","ξ":"5","ο":"6","π":"7","ρ":"8","σ":"9","ς":"9","τ":"1","υ":"2","φ":"3","χ":"4","ψ":"5","ω":"6"}

revReduction = {"A":"8","B":"7","C":"6","D":"5","E":"4","F":"3","G":"2","H":"1","I":"9","J":"8","K":"7","L":"6","M":"5","N":"4","O":"3","P":"2","Q":"1","R":"9","S":"8","T":"7","U":"6","V":"5","W":"4","X":"3","Y":"2","Z":"1",
"a":"8","b":"7","c":"6","d":"5","e":"4","f":"3","g":"2","h":"1","i":"9","j":"8","k":"7","l":"6","m":"5","n":"4","o":"3","p":"2","q":"1","r":"9","s":"8","t":"7","u":"6","v":"5","w":"4","x":"3","y":"2","z":"1",
"Α":"6","Β":"5","Γ":"4","Δ":"3","Ε":"2","Ζ":"1","Η":"9","Θ":"8","Ι":"7","Κ":"6","Λ":"5","Μ":"4","Ν":"3","Ξ":"2","Ο":"1","Π":"9","Ρ":"8","Σ":"7","Τ":"6","Υ":"5","Φ":"4","Χ":"3","Ψ":"2","Ω":"1",
"α":"6","β":"5","γ":"4","δ":"3","ε":"2","ζ":"1","η":"9","θ":"8","ι":"7","κ":"6","λ":"5","μ":"4","ν":"3","ξ":"2","ο":"1","π":"9","ρ":"8","σ":"7","ς":"7","τ":"6","υ":"5","φ":"4","χ":"3","ψ":"2","ω":"1"}


root = tk.Tk()
root.geometry("1280x720")
root.title("Gematrinator")

var = tk.StringVar()

# Entry
entry = tk.Entry(root, textvariable=var, font=("Courier", 20), justify='center', width=50)
root.grid_columnconfigure(0, weight=1)
entry.grid(pady="44",row=3, column=0, sticky='n')

# Frame to display letters and numbers
display_frame = tk.Frame(root)
display_frame.grid(sticky='N')

# Totals label
totals_label = tk.Label(root, text="", font=("Courier", 16))
totals_label.grid(sticky='S')

def on_change(*args):
    # Clear previous labels
    for widget in display_frame.winfo_children():
        widget.destroy()

    total_ordinal = total_reduction = total_revOrdinal = total_revReduction = 0

    col_index = 0

    text = var.get()
    for char in text:
        if char.isalpha() or char.isdigit():
            if char.isdigit():
                val_ord = val_red = val_revOrd = val_revRed = int(char)
            elif char in ordinal:
                val_ord = int(ordinal[char])
                val_red = int(reduction[char])
                val_revOrd = int(revOrdinal[char])
                val_revRed = int(revReduction[char])
            else:
                continue  # skip unknown characters

            total_ordinal += val_ord
            total_reduction += val_red
            total_revOrdinal += val_revOrd
            total_revReduction += val_revRed

            # Letter on top
            tk.Label(display_frame, text=char, font=("Courier", 20)).grid(row=0, column=col_index, padx=5)
            # Ordinal below
            tk.Label(display_frame, text=str(val_ord), font=("Courier", 20)).grid(row=1, column=col_index, padx=5)

            col_index += 1

    totals_label.config(
        text=f"Ordinal: {total_ordinal}    Reduction: {total_reduction}    "
             f"Reverse Ordinal: {total_revOrdinal}    Reverse Reduction: {total_revReduction}",fg="blue", font=("Courier", 16, "bold")
    )

display = tk.Frame(root)
display.grid()

rows_frame = tk.Frame(root)
rows_frame.grid()

def create_header():
    tk.Label(rows_frame, text="| Word |", font=("Courier", 16, "bold")).grid(row=0, column=0, padx=8, pady=40)
    tk.Label(rows_frame, text=" Ordinal |", font=("Courier", 16, "bold")).grid(row=0, column=1, padx=8, pady=40)
    tk.Label(rows_frame, text=" Reduction |", font=("Courier", 16, "bold")).grid(row=0, column=2, padx=8, pady=40)
    tk.Label(rows_frame, text=" Rev Ordinal |", font=("Courier", 16, "bold")).grid(row=0, column=3, padx=8, pady=40)
    tk.Label(rows_frame, text=" Rev Reduction |", font=("Courier", 16, "bold")).grid(row=0, column=4, padx=8, pady=40)

header_created = False
next_row = 1

text = var.get()
for char in text:
    if char.isalpha() or char.isdigit():
        if char.isdigit():
            val_ord = val_red = val_revOrd = val_revRed = int(char)
        elif char in ordinal:
            val_ord = int(ordinal[char])
            val_red = int(reduction[char])
            val_revOrd = int(revOrdinal[char])
            val_revRed = int(revReduction[char])
        else:
            continue  # skip unknown characters

def on_enter(event):
    global header_created, next_row

    word = var.get().strip()
    if not word:  # do nothing if empty
        return

    # Create header if it hasn't been created yet
    if not header_created:
        create_header()
        header_created = True

    # Compute cipher totals for the word
    ord_total = sum(int(ordinal[ch]) for ch in word if ch in ordinal)
    rev_ord_total = sum(int(revOrdinal[ch]) for ch in word if ch in revOrdinal)
    red_total = sum(int(reduction[ch]) for ch in word if ch in reduction)
    rev_red_total = sum(int(revReduction[ch]) for ch in word if ch in revReduction)

    # Insert a new row for this word
    tk.Label(rows_frame, text=word, font=("Courier", 14)).grid(row=next_row, column=0, padx=8, pady=2)
    tk.Label(rows_frame, text=str(ord_total), font=("Courier", 14)).grid(row=next_row, column=1, padx=8, pady=2)
    tk.Label(rows_frame, text=str(red_total), font=("Courier", 14)).grid(row=next_row, column=2, padx=8, pady=2)
    tk.Label(rows_frame, text=str(rev_ord_total), font=("Courier", 14)).grid(row=next_row, column=3, padx=8, pady=2)
    tk.Label(rows_frame, text=str(rev_red_total), font=("Courier", 14)).grid(row=next_row, column=4, padx=8, pady=2)

    # Increment the row counter for the next Enter
    next_row += 1

    # Clear the entry
    var.set("")
    entry.focus_set()
    
root.bind('<Return>', on_enter)

var.trace_add('write', on_change)

root.mainloop()
