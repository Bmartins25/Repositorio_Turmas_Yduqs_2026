from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, alunos!"

@app.route("/fazendo que se aprende")
def aula ():
    return "acho que consegui"
if __name__ == "__main__":
    app.run(debug="true")
    
    