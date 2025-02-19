
'''
Código é um exemplo de Modo Recursivo
É quando o código chama a si mesmo
'''
def tamanho_array(lista):
    if lista == []:
        return 0
    return lista[0] + tamanho_array(lista[1:])

minha_lista = tamanho_array([1, 2, 3, 4, 5])

print(minha_lista)
        