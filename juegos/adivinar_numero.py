def adivinar_numero():
    import random
    numero=random.randint(1,10)
    print('Ingresa un numero')
    guess=int(input())
    if guess==numero:
        print('Felicidades, ganaste :)')
    else:
        print('Perdiste :( , el numero era', numero)
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    pass