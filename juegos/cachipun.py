import random

def cachipun(jugador):
    computadora = random.choice(["piedra","papel","tijera"])
    print("La computadora eligió:",computadora)
    while jugador == computadora:
        print("Empate, puedes hacerlo mejor. Intenta de nuevo.")
        return cachipun(input("Elige entre piedra, papel o tijera: ").lower())
    
    if jugador == "piedra":
        if computadora == "papel":
            return "Perdiste. Una computadora te gano :("
        else:
            return "¡Felicitaciones! La computadora te dejó ganar :)"
    if jugador == "papel":
        if computadora == "tijera":
            return "Perdiste. Una computadora te gano :("
        else:
            return "¡Felicitaciones! La computadora te dejó ganar :)"
    if jugador == "tijera":
        if computadora == "piedra":
            return "Perdiste. Una computadora te gano :("
        else:
            return "¡Felicitaciones! La computadora te dejó ganar :)"

print("Bienvenido al juego Cachipun")
jugador = input("Elige entre piedra, papel o tijera: ").lower()
resultado = cachipun(jugador)
print(resultado)