import tkinter as tk
from datetime import datetime
import requests

BASE_URL = "https://v6.exchangerate-api.com/v6"
API_KEY = "8b5c05efb0dfeb155570ff44"

root = tk.Tk()
root.geometry("350x200")
root.title("Currency Converter")

# --- Top Bar ---
top_bar = tk.Frame(root, bg="#0090c3", height=33)
top_bar.pack(side="top", fill="x")
tk.Label(top_bar, text="Currency Converter", bg="#0090c3", fg="black").pack(pady=5)

# --- Main Frame ---
mainFrame = tk.Frame(root)
mainFrame.pack(pady=10)

# Currencies
currencies = [
    "USD","EUR","GBP","JPY","AUD","CAD","CHF","CNY","NZD","SEK",
    "NOK","DKK","SGD","HKD","INR","ZAR","BRL","MXN","PLN","TRY",
    "AED","RUB","KRW","THB","CZK","HUF","ILS","SAR","MYR","IDR",
    "PHP","PKR","EGP","CLP","COP","ARS","VND","NGN","BDT","KES",
    "QAR","BHD","KWD","OMR","MAD","TWD","UAH","RON","HRK","BGN"
]

# Variables for selected currencies
a_currency_var = tk.StringVar(value="EUR")
b_currency_var = tk.StringVar(value="USD")

# Dropdowns
a_dropdown = tk.OptionMenu(mainFrame, a_currency_var, *currencies)
a_dropdown.pack(side="left", padx=5)

textAmount = tk.Entry(mainFrame, width=8)
textAmount.insert(0, "1")  # default value
textAmount.pack(side="left", padx=5)

b_dropdown = tk.OptionMenu(mainFrame, b_currency_var, *currencies)
b_dropdown.pack(side="left", padx=5)

# Result label
result_var = tk.StringVar(value=f"Date: {datetime.today().strftime('%Y-%m-%d')}")
result_label = tk.Label(root, textvariable=result_var, justify="left", anchor="w")
result_label.pack(fill="x", padx=10, pady=5)

# Conversion function
def convert(event=None):
    a_currency = a_currency_var.get().strip()
    b_currency = b_currency_var.get().strip()
    raw = textAmount.get().strip()
    if raw == "":
        raw = "1"
    raw = raw.replace(",", ".")
    
    try:
        amount_val = float(raw)
    except ValueError:
        result_var.set("Invalid amount. Use numbers like 1 or 1.5")
        return

    # Format amount for API URL
    if amount_val.is_integer():
        amount_str = str(int(amount_val))
    else:
        amount_str = f"{amount_val:.6f}".rstrip("0").rstrip(".")

    # API request
    try:
        r = requests.get(f'{BASE_URL}/{API_KEY}/pair/{a_currency}/{b_currency}/{amount_str}/')
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        result_var.set("Error connecting to API")
        print(e)
        return

    if data.get("result") == "success":
        conv_rate = data.get("conversion_rate")
        conv_result = data.get("conversion_result") or (conv_rate * amount_val)
        result_var.set(f"{amount_str} {a_currency} = {conv_result} {b_currency}\nRate: {conv_rate}\nDate: {datetime.today().strftime('%Y-%m-%d')}")
    else:
        result_var.set(f"API Error: {data.get('error-type', 'Unknown')}")

# Convert button
convertButton = tk.Button(mainFrame, text="Convert", command=convert)
convertButton.pack(side="left", padx=5)

# Bind Enter key
root.bind("<Return>", convert)

root.mainloop()
