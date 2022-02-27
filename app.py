from flask import Flask, render_template

app = Flask(__name__)

#Criando primeira página
# Route > Func > template


@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/contato")
def contato():
    return "email: eraldoest@gmail.com"


#Colocando no ar
if __name__ == "__main__":
    app.run(debug=True)