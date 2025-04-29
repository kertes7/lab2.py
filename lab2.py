import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Конвертація температури")
window.geometry("300x150")

label = tk.Label(window, text="Температура (°C):")
label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

def on_click():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9 / 5 + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть число")

button = tk.Button(window, text="Конвертувати", command=on_click)
button.pack(pady=5)

window.mainloop()
