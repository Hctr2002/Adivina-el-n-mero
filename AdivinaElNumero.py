import random
import sys

BANNER = r"""
  __ _           _ _                 _             _              
 / _(_)         | (_)               | |           | |             
| |_ _ _ __   __| |_ _ __   ___  ___| |_ _ __ __ _| |_ ___  _ __  
|  _| | '_ \ / _` | | '_ \ / _ \/ __| __| '__/ _` | __/ _ \| '__| 
| | | | | | | (_| | | | | |  __/\__ \ |_| | | (_| | || (_) | |    
|_| |_|_| |_|\__,_|_|_| |_|\___||___/\__|_|  \__,_|\__\___/|_|    
                                                                  
"""


def elegir_dificultad():
    print("\nElige la dificultad:")
    print("1) Fácil    (10 intentos)")
    print("2) Normal   (7 intentos)")
    print("3) Difícil  (5 intentos)")
    while True:
        opcion = input("> ").strip()
        if opcion in {"1", "2", "3"}:
            return {"1": 10, "2": 7, "3": 5}[opcion]
        print("Opción inválida. Escribe 1, 2 o 3.")


def leer_int(mensaje, minimo, maximo):
    while True:
        valor = input(mensaje).strip()
        if valor.lower() in {"salir", "exit", "q"}:
            print("¡Hasta luego!")
            sys.exit(0)
        try:
            n = int(valor)
            if minimo <= n <= maximo:
                return n
            else:
                print(f"Escribe un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Eso no parece un número válido.")


def pista(dist):
    if dist == 0:
        return "¡Correcto!"
    if dist <= 2:
        return "🔥 Muy cerca"
    if dist <= 5:
        return "🌶️ Caliente"
    if dist <= 10:
        return "🌤️ Tibio"
    return "🧊 Frío"


def jugar_una_partida():
    limite_intentos = elegir_dificultad()
    secreto = random.randint(1, 100)
    print("\nHe pensado un número del 1 al 100. ¡Adivínalo!")
    print("(Escribe 'salir' para terminar en cualquier momento)\n")

    for intento in range(1, limite_intentos + 1):
        guess = leer_int(f"Intento {intento}/{limite_intentos} -> Tu número: ", 1, 100)
        if guess == secreto:
            print(f"\n🎉 ¡Ganaste! El número era {secreto}.")
            print(f"Lo lograste en {intento} intento(s).")
            return True
        else:
            dist = abs(guess - secreto)
            consejo = "📉 Demasiado bajo" if guess < secreto else "📈 Demasiado alto"
            print(f"{consejo} · {pista(dist)}\n")

    print(f"\n🤖 Me ganaste… El número era {secreto}.")
    return False


def jugar():
    print(BANNER)
    victorias = 0
    partidas = 0
    while True:
        gano = jugar_una_partida()
        partidas += 1
        victorias += int(gano)
        print(f"\nMarcador: {victorias} victoria(s) de {partidas} partida(s).")
        otra = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra not in {"s", "si", "sí", "y", "yes"}:
            print("\nGracias por jugar. ¡Hasta la próxima!")
            break


if __name__ == "__main__":
    jugar()
