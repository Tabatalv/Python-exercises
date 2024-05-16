"""4 - Escribir una función que tome un carácter y devuelva True si es una vocal,
 de lo contrario devuelve False."""

vocals = ["a", "e", "i", "o", "u"]


def vocal(char):
    if char in vocals:
        print("True")
    else:
        print("False")



character = input("Type a letter: ")
vocal(character)
