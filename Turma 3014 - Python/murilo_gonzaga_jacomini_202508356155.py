from flask import Flask
from flask import render_template,url_for


app = Flask(__name__)

#rotas

@app.route("/")
def homepage():
    image = url_for('static',filename='python.png')
    return render_template("flask.html",pic=image)

@app.route("/blog")
def blog():
    return "Bem vindo ao meu blog!!!"

    
if __name__ == "__main__":
     app.run()

     