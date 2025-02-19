
'''
Calculo realizado da forma convenvional.
Ou seja, sem usar o Algoritmo de Euclides
Que usa o MDC (Máximo Divisor Comum)
'''
def divisaoExata(comprimento, largura):
    
    while largura != 0:
        comprimento, largura = largura, comprimento - (comprimento // largura * largura)
        
    return comprimento, largura

#comprimento = 1680
#largura = 640

comprimento = int(input("Informe o valor do comprimento da area: "))
largura = int(input("Informe o valor da largura da area: "))

resultado = divisaoExata(comprimento, largura)
print(resultado)
print(resultado[0])
print(f'A medida máxima para obter um quadrado de um terreno {comprimento} X {largura} é de {resultado[0]} X {resultado[0]}')