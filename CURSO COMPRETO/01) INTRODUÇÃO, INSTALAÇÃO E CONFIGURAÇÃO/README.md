# INTRODUÇÃO, INSTALAÇÃO E CONFIGURAÇÃO
## Introdução:
Flask é um framework web em Python que facilita a criação de aplicações web. Ele segue a filosofia "micro", fornecendo o mínimo necessário para começar a desenvolver, mas permitindo uma grande flexibilidade para escolher outras ferramentas e bibliotecas conforme necessário. Flask é adequado para o desenvolvimento rápido de pequenas e médias aplicações web.

## Instalação do Flask:
Antes de começar a usar o Flask, você precisa instalá-lo no seu ambiente Python. Você pode fazer isso usando o pip, que é o gerenciador de pacotes do Python. Abra o terminal e execute o seguinte comando:

```bash
pip install Flask
```

Este comando instalará o Flask e suas dependências.

## Configuração Básica:
A configuração básica de uma aplicação Flask envolve a criação de uma instância do Flask e a definição de rotas. Aqui está um exemplo mínimo de uma aplicação Flask:

```python
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
```

- **`from flask import Flask`**: Importa a classe `Flask` do módulo Flask.
- **`app = Flask(__name__)`**: Cria uma instância da aplicação Flask, usando `__name__` como ponto de partida.
- **`@app.route('/')`**: Define uma rota para a URL '/' e associa a função `index()` a ela.
- **`def index():`**: A função que será chamada quando alguém acessar a URL definida.

Você pode executar este arquivo Python e acessar `http://localhost:5000/` no seu navegador para ver a mensagem "Olá, Flask!".

Esta é uma configuração mínima para começar com o Flask. À medida que você avança, pode adicionar mais funcionalidades, como templates, manipulação de formulários, integração com bancos de dados, entre outros.

## NÃO PRECISA SUBIR O SERVIDOR:
Sim, isso mesmo! Uma das características convenientes do Flask é que ele vem com um servidor de desenvolvimento embutido. Quando você executa o arquivo Python da sua aplicação Flask (por exemplo, `python app.py` se seu arquivo for chamado `app.py`), o servidor embutido é iniciado automaticamente e a sua aplicação estará acessível no endereço `http://localhost:5000/` (o número da porta padrão é 5000).

Então, ao contrário de alguns frameworks em que você precisa configurar servidores separados, como o Node.js/Express, Flask cuida disso para você. Isso é particularmente útil durante o desenvolvimento, pois facilita a visualização e teste rápidos da sua aplicação sem a necessidade de configurações complexas.

Lembre-se de que o servidor de desenvolvimento embutido do Flask não é adequado para ambientes de produção. Para a produção, você geralmente usaria um servidor WSGI (Web Server Gateway Interface) como Gunicorn ou integraria o Flask a um servidor web como o Apache ou o Nginx.

Se você quiser especificar uma porta diferente, você pode fazer isso passando o argumento `port` para o método `run()`:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8080)
```

Dessa forma, sua aplicação estaria acessível em `http://localhost:8080/`.