# 91. Exercício - crie uma lista de compras com listas

lista = []
opcao = ''

while opcao != '4':

    print('Selecione uma opção:')
    opcao =  input('1 - inserir \n2 - apagar \n3 - listar \n4 - Sair \n')

    if opcao == '1':
        novo_valor = input('Digite o novo item da lista: ')
        lista.append(novo_valor)

    if opcao == '2':
        indice_apagar = input('Digite o indice do item que deseja apagar: ')

        try:

            indice = int(indice_apagar)
            del lista[indice]
            
        except:
            print('O indice digitado é invalido')

    if opcao == '3':

        if(len(lista) == 0):
            print('A lista esta vazia')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
        
        
