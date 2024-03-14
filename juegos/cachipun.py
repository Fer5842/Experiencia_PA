import random
def cachipun():
    print("Bienvenido al juego Cachipun")
    print("Elige entre piedra, papel o tijera: ")
    jugador = input(str()).lower()
    computadora = random.choice(["piedra","papel","tijera"])
    print("La computadora eligió:",computadora)
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
