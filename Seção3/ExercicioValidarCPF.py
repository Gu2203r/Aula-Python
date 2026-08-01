cpf = "358.653.520-15"

cpf_numeros, digitos_verificadores = cpf.replace(".", "").split("-")

print("Numeros CPF:", cpf_numeros)
print("Digitos Verificadores:", digitos_verificadores)

## Verificacao primeiro digito verificador
soma = 0
multiplicador = 10

for i in range(len(cpf_numeros)):
    soma += int(cpf_numeros[i]) * multiplicador
    multiplicador -= 1

soma = soma * 10
primeiro_digito = soma % 11

print("Primeiro digito verificador:", primeiro_digito)

## Verificacao segundo digito verificador

cpf_numeros = cpf_numeros + digitos_verificadores[0]

soma = 0
multiplicador = 11

for i in range(len(cpf_numeros)):
    soma += int(cpf_numeros[i]) * multiplicador
    multiplicador -= 1

soma = soma * 10
segundo_digito = soma % 11

print("Segundo digito verificador:", segundo_digito)


if digitos_verificadores == (str(primeiro_digito) + str(segundo_digito)):
    print("O CPF é valido")
else:
    print("O cpf é invalido")

