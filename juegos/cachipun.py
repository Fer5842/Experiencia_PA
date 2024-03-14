def cachipun():
    import random
    print("Bienvenido al juego Cachipun")
    print("Elige entre piedra, papel o tijera:")
    jugador = str(input()).lower()
    computadora = random.choice(["piedra","papel","tijera"])
    print("La computadora eligió:",computadora)
    while jugador == computadora:
        print("Empate, puedes hacerlo mejor. Intenta de nuevo.")
        return cachipun()
    if jugador == "piedra":
        if computadora == "papel":
            print("Perdiste. Una computadora te gano :(")
        else:
            print("¡Felicitaciones! La computadora te dejó ganar :)")
    if jugador == "papel":
        if computadora == "tijera":
            print("Perdiste. Una computadora te gano :(")
        else:
            print("¡Felicitaciones! La computadora te dejó ganar :)")
    if jugador == "tijera":
        if computadora == "piedra":
            print("Perdiste. Una computadora te gano :(")
        else:
            print("¡Felicitaciones! La computadora te dejó ganar :)")
    pass