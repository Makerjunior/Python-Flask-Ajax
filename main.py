from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/dados')
def get_dados():

  dados = [
    {
        "marca": "Ford",
        "modelo": "Mustang",
        "ano": 2022,
        "valor": 150000,
        "cor": "vermelho",
        "motor": "V8",
        "portas": 2
    },
    {
        "marca": "Chevrolet",
        "modelo": "Camaro",
        "ano": 2023,
        "valor": 160000,
        "cor": "amarelo",
        "motor": "V8",
        "portas": 2
    },
    {
        "marca": "Tesla",
        "modelo": "Model S",
        "ano": 2022,
        "valor": 80000,
        "cor": "preto",
        "motor": "Elétrico",
        "portas": 4
    },
    {
        "marca": "BMW",
        "modelo": "Série 3",
        "ano": 2022,
        "valor": 90000,
        "cor": "branco",
        "motor": "V6",
        "portas": 4
    }
  ]

  return dados


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
