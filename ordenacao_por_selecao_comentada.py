
# Função para encontrar o índice do menor elemento de uma lista
def buscaMenor(arr):
    
    # Inicializa o menor valor com o primeiro elemento do array
    menor = arr[0]
    
    # Inicializa o índice do menor valor como 0 zero
    menor_indice = 0
    
    # Itera pela lista a partir do segundo elemento
    for i in range(1, len(arr)):
        
        # Se o elemento atual for menor que o menor conhecido, atualiza
        if arr[i] < menor:
            menor = arr[i] # Atualiza o menor valor
            menor_indice = i # Atualiza o índice do menor valor
            
    return menor_indice # Retorna o índice do menor elemento

# Função que implementa o algoritmo de ordenação por seleção
def ordenacaoPorSelecao(arr):
    
    # Cria uma nova lista para armazenar os elementos ordenados
    novoArr = []
    
    # Itera até que todos os elementos sejam removidos da lista original
    for i in range(len(arr)):
        
        # Encontra o índice do menor elemento da lista atual
        menor = buscaMenor(arr)
        
        # Remove o menor elemento da lista original e o adiciona à nova lista
        novoArr.append(arr.pop(menor))
        
    return novoArr # Retorna a lista ordenada

# Testa a função de ordenação por seleção com uma lista de exemplo
print (ordenacaoPorSelecao([5, 3, 6, 2, 10]))