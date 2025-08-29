#EX01: Crie um algoritmo que pede ao usuário para que digite um número inicial e um número final. 
#Em seguida, ele mostrará todos os números pares neste intervalo usando for.
ex01_inicial = int(input('Digite um número inicial: '))
ex01_final = int(input('Digite um número final: '))

for i in range(ex01_inicial, ex01_final+1):
    print(i)

#EX02:Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela se ele é primo ou não usando o for.
ex02_num = int(input("Digite um número: "))
primo = True

for i in range(2, ex02_num):
    if ex02_num % i == 0:
        primo = False
        break

if primo:
    print(ex02_num, "é um número primo")
else:
    print(ex02_num, "não é um número primo")


#EX03: Crie um algoritmo que mostra todos números de 5 a -5 usando o for.

ex03_lista = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

for i in ex03_lista:
    print(i)

#EX04: Crie um algoritmo para calcular o fatorial de um número usando o for.
ex04_num = int(input("Digite um número: "))

fatorial = 1
for i in range(1, ex04_num+1):
    fatorial *= i

print("O fatorial de", ex04_num, "é", fatorial)

#EX05: Escreva um algoritmo para verificar se uma palavra é um palíndromo usando o while.
palavra = input("Digite uma palavra: ")
i = 0
j = len(palavra) - 1
palindromo = True

while i < j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1

if palindromo:
    print(palavra, "é um palíndromo")
else:
    print(palavra, "não é um palíndromo")