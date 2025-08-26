import tkinter as tk
import random
from tkinter import messagebox

class AdivinaNumeroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego: Adivina el número")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.victorias = 0
        self.partidas = 0
        self.limite_intentos = 0
        self.intentos_realizados = 0
        self.secreto = 0

        self.crear_widgets_inicio()

    def crear_widgets_inicio(self):
        self.limpiar_ventana()
        label = tk.Label(self.root, text="Elige la dificultad", font=("Arial", 14))
        label.pack(pady=20)

        tk.Button(self.root, text="Fácil (10 intentos)", command=lambda: self.iniciar_partida(10)).pack(pady=5)
        tk.Button(self.root, text="Normal (7 intentos)", command=lambda: self.iniciar_partida(7)).pack(pady=5)
        tk.Button(self.root, text="Difícil (5 intentos)", command=lambda: self.iniciar_partida(5)).pack(pady=5)

    def iniciar_partida(self, intentos):
        self.limite_intentos = intentos
        self.intentos_realizados = 0
        self.secreto = random.randint(1, 100)

        self.limpiar_ventana()

        tk.Label(self.root, text="He pensado un número del 1 al 100", font=("Arial", 12)).pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(pady=5)

        tk.Button(self.root, text="Probar", command=self.probar_numero).pack(pady=5)

        self.feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

        self.intentos_label = tk.Label(self.root, text=f"Intentos restantes: {self.limite_intentos}", font=("Arial", 12))
        self.intentos_label.pack(pady=10)

    def probar_numero(self):
        valor = self.entry.get().strip()
        if not valor.isdigit():
            messagebox.showwarning("Error", "Ingresa un número válido entre 1 y 100")
            return

        guess = int(valor)
        if guess < 1 or guess > 100:
            messagebox.showwarning("Error", "El número debe estar entre 1 y 100")
            return

        self.intentos_realizados += 1
        intentos_restantes = self.limite_intentos - self.intentos_realizados

        if guess == self.secreto:
            self.victorias += 1
            self.partidas += 1
            messagebox.showinfo("Ganaste!", f"🎉 ¡Correcto! El número era {self.secreto} en {self.intentos_realizados} intento(s).")
            self.jugar_de_nuevo()
            return
        else:
            dist = abs(guess - self.secreto)
            consejo = "Demasiado bajo" if guess < self.secreto else "Demasiado alto"
            self.feedback.config(text=f"{consejo} · {self.pista(dist)}")

        if intentos_restantes <= 0:
            self.partidas += 1
            messagebox.showinfo("Perdiste", f"🤖 Me ganaste… El número era {self.secreto}.")
            self.jugar_de_nuevo()
        else:
            self.intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")

    def pista(self, dist):
        if dist == 0:
            return "¡Correcto!"
        if dist <= 2:
            return "🔥 Muy cerca"
        if dist <= 5:
            return "🌶️ Caliente"
        if dist <= 10:
            return "🌤️ Tibio"
        return "🧊 Frío"

    def jugar_de_nuevo(self):
        respuesta = messagebox.askyesno("Jugar otra vez", f"Marcador: {self.victorias} victoria(s) de {self.partidas} partida(s).\n\n¿Quieres jugar otra vez?")
        if respuesta:
            self.crear_widgets_inicio()
        else:
            self.root.quit()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaNumeroGUI(root)
    root.mainloop()
