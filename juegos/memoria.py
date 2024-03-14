def memoria():
    import random
    secuencia=random.randint(10000000000000000000,99999999999999999999)
    print(secuencia)
    print('ingresa la secuencia')
    ingresado=int(input())
    if ingresado==secuencia:
        print('Felicidades, tienes muy buena memoria :)')
    else:
        print('Perdiste :(')
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    pass