import pandas as pd

arquivo = "C:/Users/gallo/codigos/tarefa_python.xlsx"

df = pd.read_excel(arquivo, header=1, nrows=5)

print(df)

# Converter colunas para número
df["Nota 1"] = pd.to_numeric(df["Nota 1"], errors='coerce')
df["Nota 2"] = pd.to_numeric(df["Nota 2"], errors='coerce')

# Criar coluna de média
df["Media"] = (df["Nota 1"] + df["Nota 2"]) / 2

# Criar coluna de classificação
df["Situacao"] = df["Media"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")

# Mostrar resultado final
print("\nResultado com média e situação:")
print(df)


