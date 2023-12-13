# TEMPLATES
Em Flask, para renderizar páginas HTML de maneira dinâmica, você geralmente utiliza templates. Os templates permitem que você insira dados dinâmicos nas páginas HTML, facilitando a geração de conteúdo dinâmico para o usuário. O Flask usa o motor de templates Jinja2, que é poderoso e flexível.

Aqui está uma introdução básica ao uso de templates em Flask:

## Estrutura do Projeto:
Certifique-se de ter a seguinte estrutura de projeto, onde o diretório `templates` conterá seus arquivos HTML:

```
seu_projeto/
|-- app.py
|-- templates/
|   |-- index.html
|   |-- about.html
```

## Instalação da Extensão Flask:
Se ainda não tiver, você pode instalar a extensão Flask para trabalhar com templates Jinja2:

```bash
pip install Flask
```

## Uso de Templates em Flask:
**1. Criando a Aplicação:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Página Inicial', content='Bem-vindo ao meu site!')

@app.route('/about')
def about():
    return render_template('about.html', title='Sobre Nós', content='Somos uma empresa incrível.')

if __name__ == '__main__':
    app.run(debug=True)
```

**2. Criando Templates:**

- **`templates/index.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

- **`templates/about.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

## Explicação:
- `render_template`: Essa função do Flask é usada para renderizar os templates. Ela aceita o nome do arquivo HTML e quaisquer variáveis ​​que você deseje passar para o template.

- `{{ variavel }}`: Isso é uma expressão Jinja2. O que está entre `{{ }}` será substituído pelo valor da variável correspondente.

- Em cada rota, a função `render_template` é chamada com o título e o conteúdo específicos para aquela página.

- Os templates contêm HTML padrão, mas com a capacidade de incorporar variáveis dinâmicas usando a sintaxe Jinja2.

Ao acessar a rota `/`, o usuário verá a página inicial, e ao acessar a rota `/about`, verá a página "Sobre Nós". Essas páginas são geradas dinamicamente usando os templates e as variáveis fornecidas.