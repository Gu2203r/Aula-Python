
def multiplica(*args):
    total = 1

    for i in args:
        total *= i
    
    return total

def parImpar(numero):
    return "Par" if numero % 2 == 0 else "Impar"

numero = multiplica(3, 3)
print(numero)
print(parImpar(numero))