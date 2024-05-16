"""6 - Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""

def inversa(char):
  word = [letter for letter in char]
  new_word = ""

  for n in range(1, len(word) + 1):
    new_word += word[-n]
  print(new_word)

inversa("estoy probando")
