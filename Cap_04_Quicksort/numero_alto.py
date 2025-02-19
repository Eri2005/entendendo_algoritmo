
'''
Usando modo Case-Base e depois Recursivo
'''

def maior(lista):
    alto = lista[0]
    
    for num in lista:
        if num > alto:
            alto = num
    return alto
            
arr = [2, 5, 41, 55, 6, 9, 10]

resultado = maior(arr)
print(resultado)