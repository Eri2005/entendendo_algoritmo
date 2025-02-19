
def conta(list):
    if list == []:
        return 0
    return 1 + conta(list[1:])

resultado = conta([1, 2, 3, 4])
print(resultado)