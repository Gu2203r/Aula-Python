primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor =} é maior que {segundo_valor = }")

elif primeiro_valor < segundo_valor:
    print(f"{segundo_valor =} é maior que {primeiro_valor = }")

else:
    print("Os numeros possuem o mesmo valor")
    