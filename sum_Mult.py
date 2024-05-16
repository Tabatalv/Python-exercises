"""5 - Escribir una función sum() y una función multip()
 que sumen y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""

my_list = [1, 2, 3, 4]

def Sum(list):
    total = sum(list)
    print(total)


def multip(list):
    result = 1

    for item in my_list:
        result *= item
    print(result)

Sum(my_list)
multip(my_list)
