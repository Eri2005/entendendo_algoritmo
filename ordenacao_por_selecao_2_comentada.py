
# Função para calcular o menor valor
def buscaMenor(arr):
    
    # Inicializa o menor valor com o primeiro elemento do array
    menor = arr[0]
    
    # Inicializa o índice do menor valor como 0 zero
    menor_indice = 0
    
    # Exibe o estado inicial da busca
    print(f"    Iniciando buscaMenor em: {arr}")
    
    # Loop que varrerar o Array a partir do indice 1
    for i in range(1, len(arr)):
        
        # Se o elemento atual for menor que o menor conhecido, atualiza
        if arr[i] < menor:
            
            # Atualiza o menor valor
            menor = arr[i]
            
            # Atualiza o índice do menor valor
            menor_indice = i
            
            # Exibe o menor valor atualizado durante a busca
            print(f"    Novo menor encontrado: {menor} (índice {menor_indice})")
    print(f"    Menor valor final: {menor} (índice {menor_indice})")
    return menor_indice

# Função que implementa o algoritmo de ordenação por seleção
def ordenacaoPorSelecao(arr):
    
    # Cria uma nova lista para armazenar os elementos ordenados
    novoArr = []
    
    print(f"Lista inicial: {arr}")
    
    # Itera até que todos os elementos sejam removidos da lista original
    for i in range(len(arr)):
        
        # Encontra o índice do menor elemento e o remove
        menor = buscaMenor(arr)
        
        # Adiciona à nova lista
        menor_valor = arr.pop(menor)
        
        # Remove o menor elemento da lista original
        novoArr.append(menor_valor)
        
        # Exibe o estado das listas a cada iteração
        print(f"Iteração {i + 1}:")
        print(f"    Menor valor removido: {menor_valor}")
        print(f"    Lista original após remoção: {arr}")
        print(f"    Lista ordenada até agora: {novoArr}")
    return novoArr

# Testa o código com uma lista de exemplo
resultado = ordenacaoPorSelecao([5, 3, 6, 2, 10])
print(f"Lista ordenada: {resultado}")
