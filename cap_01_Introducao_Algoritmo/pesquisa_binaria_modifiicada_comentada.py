def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2 # O resultado a ser atribuido é o valor absoluto da divisão [2.5 => 2]
        '''
        Vai pegar o resultado da divisão exata para encontrar o meio e,
        Com isso encontrar o meio da lista e salvando em uma variavel
        '''
        buscando_posicao = lista[meio] 
        if buscando_posicao == item: # Verifica se o numero informado foi encontrado
            return meio
        
        '''
        Se o meio for maior que o número do usuário
        Vai informar que o número esta da metade da lista para esquerda
        E ignora da metade para direita
        '''
        if buscando_posicao > item: 
            alto = meio - 1
        
            '''
        Se o meio for menor que o número do usuário
        Vai informar que o número esta da metade da lista para direita
        E ignora da metade para esquerda
        '''
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

"""
Lembrando que na programação o indice se inicia a partir do zero[0]
"""
numero_desejado = int(input("Digite um número que deseja encontrar a posição: "))

'''
Agora com o número informado iremos jogar para a função "pesquisa_binaria"
pesquisa_binaria(minha_lista, numero_desejado)
Onde "minha_lista" irá pegar a tabela 
E "numero_desejado" é o número informado pelo usuário que irá buscar na lista
'''
resultado = pesquisa_binaria(minha_lista, numero_desejado)

'''
Aqui irá verificar se o resultadfo não é "None"
Daí então mostrará o resultado
'''
if resultado is not None:
    print(f'O número {numero_desejado} foi encontrado no índice {resultado} na posição {resultado + 1} da lista')
else:
    print(f'O número {numero_desejado} não foi encontrado na lista!')


#print (pesquisa_binaria(minha_lista, 7))
#print (pesquisa_binaria(minha_lista, -1))