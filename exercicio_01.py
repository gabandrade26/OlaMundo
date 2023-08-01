nota_a = int(input("Qual foi sua nota?"))
nota_b = int(input("Qual foi sua nota?"))
nota_c = int(input("Qual foi sua nota?"))
media = (nota_a+nota_b+nota_c)/3
print("Sua média: ", media)

'''
Elabore um programa que pergunte ao aluno as suas 3 notas escolares. O programa deverá calcular a média das 3 notas inseridas e exibir está média
'''

# Etapa 1: entrada de dados
nota1 = float(input("Informe a sua nota 1: "))
nota2 = float(input("Informe a sua nota 2: "))
nota3 = float(input("Informe a sua nota 3: "))

# Etapa 2: processamento de dados
media = (nota1 + nota2 + nota3) / 3

# Etapa 3: Saída de dados (resposta na tela do usuário)
print("Sua média é", media)