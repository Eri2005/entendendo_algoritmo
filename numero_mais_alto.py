
'''
Usando o modo Recursivo
'''
def numero_alto(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = numero_alto(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

arr = [2, 8, 16, 15, 8, 3, 1]

resultado = numero_alto(arr)

print (resultado)