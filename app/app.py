# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância da aplicação Flask
app = Flask(__name__)


# Define uma rota para a URL raiz ("/")
@app.route("/")
def hello():
    # Retorna a string "Olá, Mundo!" quando a rota raiz é acessada
    return "Olá, Mundo!"


# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Executa a aplicação Flask no host 0.0.0.0 e na porta 5000
    app.run(host="0.0.0.0", port=5000)
