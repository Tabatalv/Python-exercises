"""8 - Definir una función superposicion() que tome dos listas
y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
 Escribir la función usando el bucle for anidado."""

f_list = [1, 2, 3, 4, 5, 6]
s_list = [7, 8, 9, 10, 11, 6, 4]


def superposicion(list1, list2):
    is_true = 0
    is_false = 0
    for number in list1:
        if number in list2:
            is_true += 1
        else:
            is_false += 1
    if is_true > 0:
        print("True")
    else:
        print("False")


superposicion(f_list, s_list)
