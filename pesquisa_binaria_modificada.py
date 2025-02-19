def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        buscando_posicao = lista[meio] 
        if buscando_posicao == item:
            return meio
        if buscando_posicao > item: 
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]


numero_desejado = int(input("Digite um número que deseja encontrar a posição: "))

resultado = pesquisa_binaria(minha_lista, numero_desejado)

if resultado is not None:
    print(f'O número {numero_desejado} foi encontrado no índice {resultado} na posição {resultado + 1} da lista')
else:
    print(f'O número {numero_desejado} não foi encontrado na lista!')


#print (pesquisa_binaria(minha_lista, 7))
#print (pesquisa_binaria(minha_lista, -1))