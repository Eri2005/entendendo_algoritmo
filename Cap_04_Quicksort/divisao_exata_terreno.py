
'''
Esse calculo esta usando o Algoritmo de Euclides MDC (Maximo Divisor Comum)
Ele se baseia no fato de que o MDC de dois números não muda se o maior for substituído pelo resto da divisão do maior pelo menor
'''
def calculando_terreno(comprimento, largura):
    
    while largura != 0:
        comprimento, largura = largura, comprimento % largura
    return comprimento

#comprimento = 1680
#largura = 640

comprimento = int(input("Informe o valor do comprimento da area: "))
largura = int(input("Informe o valor da largura da area: "))

resultado = calculando_terreno(comprimento, largura)

print(f'O valor total é: \nComprimento = {resultado}\nLargura = {resultado}')
