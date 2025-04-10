import os

print("Insira seus dados:")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("idade: ")
idade = int(idade)
ano_atual = 2025
altura_metros = input("Altura em metros: ")

if idade >= 18:
    maior_de_idade = "sim"
else:
    maior_de_idade= "não"

os.system("cls")

print("Nome inteiro:" , nome , sobrenome)
print("Idade:", idade)
print("Ano de Nascimento:", ano_atual - idade)
print("É maior de idade?",maior_de_idade )
print("Altura em metros", altura_metros)