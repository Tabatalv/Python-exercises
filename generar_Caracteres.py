"""9 - Definir una función generar_n_caracteres()
que tome un entero n y devuelva el caracter multiplicado por n.
 Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""


def generar_n_caracteres(letra, entero):
    word = ""
    for _ in range(entero):
        word += letra
    print(word)


generar_n_caracteres("a", 3)
