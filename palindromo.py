"""7 - Definir una función es_palindromo()
 que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
  ejemplo: es_palindromo ("radar") tendría que devolver True."""

def palindromo(word):
    s_word = ""
    rever = [letter for letter in word]
    for n in range(1, len(rever) + 1):
        s_word += rever[-n]
    if s_word == word:
        print("True")
    else:
        print("False")

palindromo("plata")