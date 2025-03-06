# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

resultado = 0

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = (abs(num1 - num2))
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"

print("Resultado: ", resultado)
