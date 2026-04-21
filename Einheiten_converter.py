import tkinter as tk
import random
import string

class PasswortGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine Tkinter GUI")

        # Label
        self.label = tk.Label(root, text="Passwortlänge eingeben:")
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(root, text="Passwort generieren", command=self.anzeigen)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def generiere_passwort(self, length):
        characters = string.ascii_letters + string.digits #+ string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password


    def anzeigen(self):
        length = int(self.entry.get())
        passwort=self.generiere_passwort(length)
        self.output_label.config(text=f"Generiertes Passwort: {passwort}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = PasswortGenerator(root)
    root.mainloop()

