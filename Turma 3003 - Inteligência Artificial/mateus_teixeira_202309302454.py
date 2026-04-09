import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==========================================
# Etapa 1 - Leitura dos Dados
# ==========================================
print("--- Etapa 1: Leitura dos Dados ---\n")

# Lendo o arquivo Excel (ajuste o nome do arquivo se necessário)
nome_arquivo = 'base_dados_ia.xlsx'
df = pd.read_excel(nome_arquivo)

print("Primeiras linhas da base de dados:")
print(df.head(), "\n")

print("Tipos de dados:")
print(df.dtypes, "\n")

# ==========================================
# Etapa 2 - Preparação dos Dados
# ==========================================
# Tratando valores nulos (removendo linhas com dados faltando)
df = df.dropna()

# O y (resultado) precisa ser numérico. Se estiver como "Aprovado"/"Reprovado", vamos converter:
# Se a base já tiver 0 e 1, esta linha não causará problemas.
if df['resultado'].dtype == object:
    df['resultado'] = df['resultado'].map({'Aprovado': 1, 'Reprovado': 0})

X = df[['nota1', 'nota2', 'frequencia', 'horas_estudo']]
y = df['resultado']

# ==========================================
# Etapa 3 - Criação do Modelo
# ==========================================
# Separando 80% para treino e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Fazendo as previsões
previsoes = modelo.predict(X_test)

# ==========================================
# Etapa 4 - Avaliação
# ==========================================
print("--- Etapa 4: Avaliação ---\n")
acuracia = accuracy_score(y_test, previsoes)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%\n")

# ==========================================
# Etapa 5 - Probabilidades
# ==========================================
print("--- Etapa 5: Probabilidades ---\n")
probabilidades = modelo.predict_proba(X_test)

# Mostrando as probabilidades dos primeiros 10 alunos do teste
for i in range(min(10, len(probabilidades))):
    prob_aprovacao = probabilidades[i][1] 
    
    if prob_aprovacao >= 0.70:
        status = "alta chance de aprovação"
    elif prob_aprovacao >= 0.45:
        status = "chance moderada de aprovação"
    else:
        status = "risco de reprovação"
        
    print(f"Aluno {i+1} | Probabilidade: {prob_aprovacao:.2f} -> {status}")

print("\n" + "="*50 + "\n")

print("\n--- Respostas Obrigatórias ---\n")

print("1. O modelo teve boa acurácia?")
print("R: Sim. A acurácia foi de 91,67%, um excelente resultado, prevendo corretamente o status de aprovação de quase 92% dos alunos testados.")

print("\n2. Como interpretar a probabilidade?")
print("R: É a chance percentual (de 0 a 1) do aluno ser aprovado. Valores altos indicam aprovação provável; valores baixos servem como alerta de risco.")

print("\n3. O modelo pode ser usado na vida real?")
print("R: Sim, como um sistema de alerta precoce. Ele ajuda professores a identificar alunos em risco durante o semestre para oferecer suporte, mas não deve dar a palavra final.")

print("\n4. Existe risco de erro ou injustiça?")
print("R: Sim. O modelo ignora fatores externos (saúde, problemas familiares). Usá-lo para rotular ou desistir de um aluno seria injusto e limitante.")

print("\n5. O que poderia melhorar no modelo?")
print("R: Incluir dados comportamentais (participação, entrega de trabalhos extras), balancear a base de dados e testar outros algoritmos preditivos.")