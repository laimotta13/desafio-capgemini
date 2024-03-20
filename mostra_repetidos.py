palavra = input("Digite uma palavra: ")

quantidade_diagramas = 0

for i in range(len(palavra) - 1):
    if palavra[i] != ' ' and palavra[i+1] != ' ':  # Ignora espaços em branco
        quantidade_diagramas += 1

print("Quantidade de diagramas:", quantidade_diagramas)
