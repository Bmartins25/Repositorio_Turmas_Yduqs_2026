import pandas as pd

caminho_arquivo = 'tarefa_python.xlsx'

df = pd.read_excel(caminho_arquivo, engine='openpyxl')

print("--- Base de Dados Original ---")
print(df)
print("\n")

df['media'] = (df['Nota 1'] + df['Nota 2']) / 2

df.loc[df['media'] >= 6, 'situacao'] = 'Aprovado'
df.loc[df['media'] < 6, 'situacao'] = 'Reprovado'


print("--- Resultado Final ---")
print(df)