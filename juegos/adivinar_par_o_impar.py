def adivinar_par_o_impar():
    import random
    numero=random.randint(1,10)
    if numero%2==0:
        par=True
    else:
        par=False
    print('par o impar?')
    guess=input()
    if guess=='par' and par==True or guess=='impar' and par==False:
        print('Felicidades, ganaste :)')
    else:
        print('perdiste :(')
        


    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    pass