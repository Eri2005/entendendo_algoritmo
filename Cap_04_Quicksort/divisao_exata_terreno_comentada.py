
'''
Esse calculo esta usando o Algoritmo de Euclides MDC (Maximo Divisor Comum)
Ele se baseia no fato de que o MDC de dois números não muda se o maior for substituído pelo resto da divisão do maior pelo menor
'''

# Recebendo dois valores
def calculando_terreno(comprimento, largura):
    
    '''
    Utilizando um Loop com WHILE.
    Verifica se o valor da [Largura] é diferente de Zero [0].
    Enquanto o valor da Largura não for ZERO ele repete o LOOP
    '''
    while largura != 0:
        
        ''' 
        Calcula o MDC e atribui os valores as variaveis
        Aqui ele substituindo o valor da [Comprimento] com o valor da [Largura]
        E o valor da [Largura] é substituido pelo calculo do resto da divisão de [Comprimento] e a [Largura]
        Esse calculo [%] é MOD
        Ou seja pega o resto da divisão
        É chamado de CASO-BASE
        '''
        comprimento, largura = largura, comprimento % largura
        
    # Retorna o valor do comprimento da area em quadrados
    return comprimento

#comprimento = 1680
#largura = 640

comprimento = int(input("Informe o valor do comprimento da area: "))
largura = int(input("Informe o valor da largura da area: "))

resultado = calculando_terreno(comprimento, largura)

print(f'O valor total é: \nComprimento = {resultado}\nLargura = {resultado}')