""" 2 - Definir una función max_de_tres(),
que tome tres números como argumentos y devuelva el mayor de ellos."""

def max_de_tres(n1, n2, n3):

    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3> n1 and n3 > n2:
        print(n3)
    else:
        print("The numbers can't be the same.")


max_de_tres(3, 5, 1)
