from flask import Flask

app = Flask(__name__)

# Rota principal exigida no enunciado
@app.route("/")
def home():
    return "Olá, alunos!"

# Desafio opcional: Outra rota com mensagem diferente
@app.route("/desafio")
def desafio():
    return "Desafio opcional concluído com sucesso! Bem-vindo à segunda rota."

if __name__ == "__main__":
    # O debug=True ajuda muito no desenvolvimento, atualizando o servidor sozinho se você mudar o código
    app.run(debug=True)