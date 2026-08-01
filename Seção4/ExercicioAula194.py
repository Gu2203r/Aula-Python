lista_tarefas = []

lista_redesfazer = []
lista_desfazer = []

def listar():
    for tarefa in lista_tarefas:
        print(tarefa)

def desfazer():
    lista_redesfazer.append(lista_tarefas[len(lista_tarefas) - 1])
    lista_tarefas.pop()

    listar()

def redesfazer():
    lista_tarefas.append(lista_redesfazer[len(lista_redesfazer) - 1])
    lista_redesfazer.pop()

    listar()


while True:

    print("comandos: listar, desfazer, refazer")
    tarefa = input("escreva uma tarefa ou um comando:\n")

    if tarefa == "listar":
        listar()
    elif tarefa == "desfazer":
        desfazer()
    elif tarefa == "redesfazer":
        redesfazer()
    else:
        lista_tarefas.append(tarefa)

