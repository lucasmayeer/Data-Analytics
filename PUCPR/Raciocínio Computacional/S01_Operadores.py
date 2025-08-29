#EX01: Crie um algoritmo que solicita ao usuário que insira seu nome e exibe na tela uma mensagem de saudação.
ex01_nome = input("Digite seu nome: ")

print(f"Olá, seja bem vindo {ex01_nome}, é muito bom ter você aqui!")
print("_______________________________")
print(" ")

#EX02: Crie um algoritmo que solicita ao usuário que insira um número decimal e exibe o dobro desse número na tela.
ex02_decimal = float(input("Digitel um número decimal:"))

print(f"O dobro do número digitado ({ex02_decimal}) é: {ex02_decimal*2}")
print("_______________________________")
print(" ")

#EX03: Crie um algoritmo que solicita ao usuário que insira um número inteiro e exibe na tela True se ele for par e False se for ímpar.
ex03_inteiro = int(input("Digite um número inteiro: "))

print(f"O número digitado ({ex03_inteiro}) é par (True=Par | False=Ímpar)? {ex03_inteiro % 2 == 0}")
print("_______________________________")
print(" ")

#EX04: Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela True se ele for igual ou acima de zero 
#ou False se menor do que zero.
ex04_numero = float(input("Digite um número: "))

print(f"O número digitado ({ex04_numero}) é igual ou maior que zero (True=Maior ou igual a zero | False=Menor que zero)? {ex04_numero >= 0}")
print("_______________________________")
print(" ")

#EX05: Crie um algoritmo que solicita ao usuário que insira a temperatura em graus Celsius e exibe na tela a temperatura em Fahrenheit.
ex05_celsius = float(input("Digite a temperatura em graus Celsius: "))
conversao_fahrenheit = (ex05_celsius * 9/5) + 32 #Constante

print(f"A temperatura em Fahrenheit é: {conversao_fahrenheit}°F")
print("_______________________________")
print(" ")

#EX06: Crie um algoritmo que solicita ao usuário que insira a sua altura em metros e o seu peso em quilogramas 
#e exibe na tela o seu índice de massa corporal (IMC).
ex06_altura = float(input("Digite sua altura em metros: "))
ex06_peso = float(input("Digite seu peso em quilogramas: "))

imc = ex06_peso / (ex06_altura ** 2)  # Constante: Fórmula do IMC

print(f"Seu índice de massa corporal (IMC) é: {imc:.2f}")
print("_______________________________")
print(" ")

#EX07: Crie um algoritmo que solicita ao usuário que insira dois números 
#e exibe na tela o resultado da soma, subtração, multiplicação e divisão desses números.
ex07_num1 = int(input("Digite o primeiro número: "))
ex07_num2 = int(input("Digite o segundo número: "))

ex07_soma= ex07_num1 + ex07_num2
ex07_sub = ex07_num1 - ex07_num2
ex07_mult = ex07_num1 * ex07_num2
ex07_div = ex07_num1 / ex07_num2

print(f"A soma dos números {ex07_num1} e {ex07_num2} resulta em: {ex07_soma}")
print(f"A subtração dos números {ex07_num1} e {ex07_num2} resulta em: {ex07_sub}")
print(f"A multiplicação dos números {ex07_num1} e {ex07_num2} resulta em: {ex07_mult}")
print(f"A divisão dos números {ex07_num1} e {ex07_num2} resulta em: {ex07_div}")
print("_______________________________")