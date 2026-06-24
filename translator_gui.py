import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target = language_var.get()

    if text:
        translated = GoogleTranslator(
            source='auto',
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x400")

tk.Label(root, text="Enter Text").pack(pady=5)

input_text = tk.Text(root, height=5)
input_text.pack(fill="x", padx=10)

language_var = tk.StringVar(value="ta")

languages = ["ta", "hi", "en", "fr", "de", "es"]

ttk.Combobox(
    root,
    textvariable=language_var,
    values=languages
).pack(pady=5)

tk.Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

tk.Label(root, text="Translated Text").pack()

output_text = tk.Text(root, height=5)
output_text.pack(fill="x", padx=10)

root.mainloop()