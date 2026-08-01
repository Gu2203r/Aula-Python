perguntas_respostas = [
    {
        "Pergunta": "Quanto é 5 + 5?",
        "Ações": ["1", "5", "3", "4", "10"],
        "Resposta": "10"
    },

    {
        "Pergunta": "Quanto é 5 * 5?",
        "Ações": ["50", "15", "25", "20", "13"],
        "Resposta": "25"
    },

    {
        "Pergunta": "Quanto é 15 / 5?",
        "Ações": ["3", "5", "30", "2", "8"],
        "Resposta": "3"
    }
]

for i in range(len(perguntas_respostas)):
    print(perguntas_respostas[i].get("Pergunta"))
    resposta = input(f"Opções:\n {perguntas_respostas[i].get("Ações")} \n")

    while(resposta not in perguntas_respostas[i].get("Ações")):
        resposta = input("Essa opcao nao existe, por favor digite uma opcao valida: \n")

    if resposta == perguntas_respostas[i].get("Resposta"):
        print("Resposta correta!!!")
    else:
        print("Resposta Errada!")
        