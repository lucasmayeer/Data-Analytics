#Operadores Logicos - IF, ELIF e ELSE

#EX01 - Crie um algoritmo que solicita ao usuário que insira um número inteiro e exibe na tela se ele é par ou ímpar.
ex01_num = int(input("Digite um número inteiro: "))

if ex01_num % 2 == 0:
    print("O número digitado é par!") 
else:
    print("O número digitado é ímpar!")


#EX02 - Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela se ele é positivo, negativo ou zero.
ex02_num = float(input("Digite um número: "))

if ex02_num == 0:
    print("O número digitado é 0!")
elif ex02_num > 0:
    print("O número digitado é um número positivo!")
elif ex02_num < 0:
    print("O número digitado é um número negativo!")


#EX03 - Crie um algoritmo que peça ao usuário três números e informe qual deles é o maior.
ex03_num01 = float(input("Digite o primeiro número: "))
ex03_num02 = float(input("Digite o segundo número: "))
ex03_num03 = float(input("Digite o terceiro número: "))

if ex03_num01 > ex03_num02 and ex03_num01 > ex03_num03:
    print(f"O primeiro número digitado ({ex03_num01}) é maior que o segundo e terceiro números digitados!")
elif ex03_num02 > ex03_num01 and ex03_num02 > ex03_num03:
    print(f"O segundo número digitado ({ex03_num02}) é maior que o primerio e terceiro números digitados!")
else:
    print(f"O terceiro número digitado ({ex03_num03}) é maior que o primeiro e segundo números digitados!")


#EX04 - Escreva um código que solicite o preço de um produto e, caso o valor seja maior que R$ 100,00, aplique um desconto de 10%. 
#Caso contrário, não aplique nenhum desconto e informe o preço final ao usuário.
ex04_produto = input("Qual produto você deseja comprar? ")
ex04_valorp = float(input("Digite o valor do produto R$"))

if ex04_valorp > 100:
    ex04_desconto = ex04_valorp * (10 / 100)
    ex04_valorp_desconto = ex04_valorp - ex04_desconto

    print(f"Você vai comprar o produto {ex04_produto} e ele recebeu um desconto de 10%!")
    print(f"O valor final do produto ficou em R${ex04_valorp_desconto:.2f}")
else:
    print(f"Você vai comprar o produto {ex04_produto} e o produto não recebe desconto!")
    print(f"O valor final do produto ficou em R${ex04_valorp}")


#EX05 - Escreva um código que solicite a idade e o gênero de uma pessoa e informe se ela pode se aposentar,levando em consideração 
#as seguintes regras: mulheres podem se aposentar com 63 anos ou mais, enquanto homens podem se aposentar com 68 anos ou mais.
ex05_nome = input("Digite seu nome: ")
ex05_sexo = input("Digite seu sexo [M/F]: ")
ex05_idade = int(input("Digite sua idade: "))

if ex05_sexo == "F": 
    if ex05_idade >= 63:
        print(f"Você se chama {ex05_nome}, você possui {ex05_idade} anos e já está apta para se aposentar!")
    else:
        print(f"Olá {ex05_nome}, você ainda não está apta para se aposentar, a idade mínima para as mulheres é 63 anos!")
elif ex05_sexo == "M":
    if ex05_idade >= 68:
        print(f"Você se chama {ex05_nome}, você possui {ex05_idade} anos e já está apto para se aposentar!")
    else:
        print(f"Olá {ex05_nome}, você ainda não está apta para se aposentar, a idade mínima para os homens é 68 anos!")