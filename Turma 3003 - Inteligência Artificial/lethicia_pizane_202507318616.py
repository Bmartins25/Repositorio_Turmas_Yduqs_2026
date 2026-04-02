import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df_raw = pd.read_excel('base_dados_ia.xlsx')
df_raw.head()

df_raw.info()
df_raw['resultado'] = df_raw['resultado'].map({'Aprovado': 1, 'Reprovado': 0})
# nosso target, variável alvo,  está como string, portanto, deve ser mudado para binário.

df_encoded = df_raw.copy()
X = df_encoded.drop(['resultado', 'nome'], axis=1)
y = df_encoded['resultado']
# separação das variáveis

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# padronização dos dados (tirando o resultado) para que nenhum deles tenha um peso maior que o outro na hora de dar o resultado final

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
# testando o modelo
probabilidade = model.predict_proba(X_test_scaled)[:, 1]
# probabilidade requerida, onde  o fatiamento mostra somente a probabilidade de aprovação
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}%')
# acurácia do modelo final




