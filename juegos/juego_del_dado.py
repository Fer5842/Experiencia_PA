def juego_del_dado():
    import random
    usuario = 0
    computador = 0
    contador = 0
    while usuario < 30 and computador < 30:
        a=input('Presiona enter para lanzar el dado.')
        if a== '':
            contador += 1
            if contador%2 != 0:
                u = random.randint(1,6)
                usuario += u 
                print(f'Obtuviste un {u} en el dado, tu suma total es de {usuario} puntos')
            if usuario >= 30:
                contador += 1
                if contador%2 ==0:
                    c = random.randint(1,6)
                    computador += c
                    print(f'El computador obtuvo un {c} en el dado, su suma total es de {computador} puntos')
    if contador%2 != 0:
        return f'¡Ganaste! Sumaste {usuario} puntos'
    else:
        return f'Ganó el computador con una suma de {computador} puntos :()'
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    pass