import pandas as pd

print("Iniciando a leitura da base de dados...\n")

try:
    # Ler o arquivo Excel
    df = pd.read_excel(r'C:\Users\Administrador\Desktop\Exercício Python Prof Bruno\tarefa_python.xlsx')
    
    # Mostrar a base original na tela
    print("--- Base Original ---")
    print(df)
    print("\n")
    
    # Criar uma coluna de média
    df['media'] = (df['Nota 1'] + df['Nota 2']) / 2
    
    # Classificar Aprovado (>= 6) ou Reprovado (< 6)
    df.loc[df['media'] >= 6, 'situacao'] = 'Aprovado'
    df.loc[df['media'] < 6, 'situacao'] = 'Reprovado'
    
    # Exibir o resultado final processado
    print("--- Resultado Final ---")
    print(df)

except FileNotFoundError:
    print("ERRO: O arquivo 'tarefa_python.xlsx' não foi encontrado!")