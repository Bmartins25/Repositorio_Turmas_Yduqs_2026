# Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2

# Decisão
if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# Saída
print("Média:", media)
print("Resultado:", resultado)