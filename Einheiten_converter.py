import tkinter as tk
import random
import string

class PasswortGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Passwort Generator")
        self.root.geometry("400x350")

        self.sprache = "DE"

        self.texte = {
            "DE": {
                "label": "Passwortlänge eingeben:",
                "btn_gen": "Passwort generieren",
                "btn_lang": "Sprache wechseln (DE)",
                "ausgabe": "Generiertes Passwort:",
                "min_error": "Länge muss mindestens 4 sein.",
                "max_error": "Länge darf maximal 64 sein."
            },
            "EN": {
                "label": "Enter password length:",
                "btn_gen": "Generate Password",
                "btn_lang": "Change Language (EN)",
                "ausgabe": "Generated Password:",
                "min_error": "Length must be at least 4.",
                "max_error": "Length must be max 64."
            },
            "AR": {
                "label": "أدخل طول كلمة المرور:",
                "btn_gen": "توليد كلمة السر",
                "btn_lang": "تغيير اللغة (AR)",
                "ausgabe": "كلمة السر المولدة:",
                "min_error": "يجب أن يكون الطول 4 على الأقل.",
                "max_error": "يجب أن يكون الطول 64 كحد أقصى."
            }
        }

        # Label
        self.label = tk.Label(root, text=self.texte[self.sprache]["label"])
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(root, text=self.texte[self.sprache]["btn_gen"], command=self.anzeigen)
        self.button.pack(pady=10)

        # Language switch button
        self.lang_button = tk.Button(root, text=self.texte[self.sprache]["btn_lang"], command=self.sprache_wechseln)
        self.lang_button.pack(pady=5)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def generiere_passwort(self, length):
        if length < 4:
            return self.texte[self.sprache]["min_error"]
        elif length > 64:
            return self.texte[self.sprache]["max_error"]
        else:
            characters = string.ascii_letters + string.digits #+ string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            return password


    def anzeigen(self):
        try:
            length = int(self.entry.get())
        except ValueError:
            self.output_label.config(text="Bitte eine gültige Zahl eingeben.")
            return
        length = int(self.entry.get())
        passwort=self.generiere_passwort(length)
        übersetzung = self.texte[self.sprache]["ausgabe"]
        self.output_label.config(text=f"{übersetzung} {passwort}")

    def sprache_wechseln(self):
        if self.sprache == "DE":
            self.sprache = "EN"
        elif self.sprache == "EN":
            self.sprache = "AR"
        else:
            self.sprache = "DE"

        self.label.config(text=self.texte[self.sprache]["label"])
        self.button.config(text=self.texte[self.sprache]["btn_gen"])
        self.lang_button.config(text=self.texte[self.sprache]["btn_lang"])

if __name__ == "__main__":
    root = tk.Tk()
    gui = PasswortGenerator(root)
    root.mainloop()

