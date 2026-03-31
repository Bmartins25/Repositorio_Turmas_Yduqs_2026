from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def ola_alunos():
    url_imagem = url_for('static', filename='python.png')
    return f"""
    <h1>Ola, alunos!</h1>
    <nav>
        <a href="/">Início</a> | <a href="/sobre">Sobre Mim</a>
    </nav>
    <p style="font-size: 30px;">Bem-vindos ao meu servidor Flask.</p>
    <img src="{url_imagem}" alt="Logo Python" style="width:500px; border-radius:10px;">
    """

@app.route("/sobre")
def sobre():
    return f"""
    <nav>
        <a href="/">Início</a> | <a href="/sobre">Sobre Mim</a>
    </nav>
    <h1>Sobre mim</h1>
    <p>Meu nome é David...</p>
    """
if __name__ == "__main__":
    app.run(debug=True)