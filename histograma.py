"""10 - Definir un histograma procedimiento()
que tome una lista de números enteros e imprima un histograma en la pantalla.
 Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******"""

def histograma(list):
    for number in list:
        lenght_num = ""
        for n in range(number):
            lenght_num += "*"
        print(lenght_num)

histograma([2, 3, 4])
