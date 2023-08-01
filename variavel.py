# input é uma função que permite perguntar algo ao usuário
# nome = input("Qual é o seu nome?")

'''
Bloco
de
Comentário
Permite que várias linhas se tornem um comentário
'''

# print("Olá,", nome, ". Tudo bem com vc?")

# print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

print("Tipo da var a: ", type(a)) # tipo inteiro (números inteiros)
print("Tipo da var b: ", type(b)) # tipo float (números reais)
print("Tipo da var c: ", type(c)) # tipo string (alfanumérico)
print("Tipo da var d: ", type(d)) # tipo boolean (True ou False)

a = 20
print("a: ", a)
b = "São Paulo"
print("b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))

a = input("Informe um número: ")
b = input("Informe um número: ")
print("a: ", a, "- b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b # concatenou as strings de a e b
print("c: ", c)
print("Tipo da var c: ", type(c))
d = int(a)
print("d: ", d)
print("Tipo da var d: ", type(d))

a = int(input("Informe um número: "))
b = int(input("Informe um número: "))
print("a: ", a, "- b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c: ", c)
print("Tipo da var c: ", type(c))

a = float(input("Informe um número: "))
b = float(input("Informe um número: "))
print("a: ", a, "- b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c: ", c)
print("Tipo da var c: ", type(c))