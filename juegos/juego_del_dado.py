def juego_del_dado():
    import random
    usuario = 0
    computador = 0
    contador = 0
    while usuario < 30 and computador < 30:
        a=input('\nPresiona enter para lanzar el dado.')
        if a== '':
            u = random.randint(1,6)
            usuario += u 
            print(f'\nObtuviste un \033[1m{u}\033[0m en el dado, tu suma total es de \033[1m{usuario}\033[0m puntos')
            if usuario >= 30:
                print(f'\n¡Ganaste! Sumaste {usuario} puntos')
        if usuario < 30:
            c = random.randint(1,6)
            computador += c
            print(f'El computador obtuvo un \033[1m{c}\033[0m en el dado, su suma total es de \033[1m{computador}\033[0m puntos')
            if computador >= 30:
                print(f'\nGanó el computador con una suma de {computador} puntos :()')
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    pass