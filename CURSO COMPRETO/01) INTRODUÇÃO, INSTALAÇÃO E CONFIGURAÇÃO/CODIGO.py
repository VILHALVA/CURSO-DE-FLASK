from flask import Flask

# Criar uma instância do Flask
app = Flask(__name__)

# Definir uma rota e a função associada a ela
@app.route('/')
def index():
    return 'Olá, Flask!'

# Executar a aplicação se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
