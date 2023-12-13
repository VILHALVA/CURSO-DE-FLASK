# ROTAS
Em Flask, as rotas definem como a sua aplicação responde a requisições do cliente. Elas indicam qual função deve ser executada para uma URL específica. A criação de rotas é uma parte fundamental do desenvolvimento web com Flask. Aqui estão algumas noções básicas sobre como definir rotas:

## Criando Rotas Simples:
A forma mais básica de definir uma rota em Flask é usar o decorador `@app.route()`. Este decorador permite associar uma função a uma URL específica. Por exemplo:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página Inicial'

@app.route('/about')
def about():
    return 'Sobre Nós'

if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, a função `home()` será executada quando a URL principal (`/`) for acessada, e a função `about()` será executada quando a URL `/about` for acessada.

## Passando Parâmetros nas Rotas:
Você pode definir rotas que aceitam parâmetros. Por exemplo:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    return f'Perfil do usuário: {username}'

if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, ao acessar `/user/john`, a função `profile()` será chamada com o parâmetro `username` definido como `'john'`.

## Métodos HTTP:
Você pode especificar quais métodos HTTP uma rota deve responder. O padrão é `GET`, mas você pode incluir outros, como `POST`. Exemplo:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação para o método POST
        return 'Autenticação realizada'
    else:
        # Página de login para o método GET
        return 'Página de Login'

if __name__ == '__main__':
    app.run(debug=True)
```

## Renderizando Templates HTML:
Para renderizar templates HTML em vez de retornar strings diretamente, você pode usar a função `render_template` do Flask. Por exemplo:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/template_example/<name>')
def template_example(name):
    return render_template('template_example.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)
```

## Redirecionamento:
Você pode redirecionar o usuário para outra rota usando `redirect`:

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Página Inicial'

@app.route('/redirect')
def redirecionar():
    # Redireciona para a rota '/home'
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

Estas são apenas noções básicas para começar a trabalhar com rotas no Flask. À medida que sua aplicação cresce, você pode explorar mais funcionalidades, como blueprints para organizar rotas, manipulação de formulários, etc.