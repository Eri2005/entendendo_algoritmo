def buscaMenor(arr):
    menor = arr[0]
    
    menor_indice = 0
    
    print(f"    Iniciando buscaMenor em: {arr}")
    for i in range(1, len(arr)):
        
        if arr[i] < menor:
            
            menor = arr[i]
            
            menor_indice = i
            
            print(f"    Novo menor encontrado: {menor} (índice {menor_indice})")
    print(f"    Menor valor final: {menor} (índice {menor_indice})")
    return menor_indice

def ordenacaoPorSelecao(arr):
    
    novoArr = []
    
    print(f"Lista inicial: {arr}")
    
    for i in range(len(arr)):
        
        menor = buscaMenor(arr)
        
        menor_valor = arr.pop(menor)
        
        novoArr.append(menor_valor)
        
        print(f"Iteração {i + 1}:")
        print(f"    Menor valor removido: {menor_valor}")
        print(f"    Lista original após remoção: {arr}")
        print(f"    Lista ordenada até agora: {novoArr}")
    return novoArr

resultado = ordenacaoPorSelecao([5, 3, 6, 2, 10])
print(f"Lista ordenada: {resultado}")
