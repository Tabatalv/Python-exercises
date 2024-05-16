"""3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada,
 pero escribirla por nosotros mismos resulta un muy buen ejercicio."""

#Sin len()
list = [3, 5, 6, 9, 10, 45, 22, 1, 76, 54]
counter = 0

for item in list:
    counter += 1
print(f"In total, there are {counter} items in the list. ")

#Con len()
list = [3, 5, 6, 9, 10, 45, 22, 1, 76, 54]
print(len(list))
