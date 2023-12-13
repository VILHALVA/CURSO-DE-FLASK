# FORMULÁRIOS
Em uma aplicação web, os formulários são uma parte crucial para coletar dados dos usuários. O Flask facilita a manipulação de formulários através de suas extensões e funcionalidades integradas. Vou guiar você na criação e manipulação básica de formulários em Flask.

## Instalação e Configuração:
Certifique-se de ter o Flask instalado:

```bash
pip install Flask
```

## Exemplo Básico de Formulário:
**1. Crie a Aplicação:**

```python
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_super_secreta'
```

**2. Crie o Formulário:**

- Crie um arquivo chamado `forms.py` para definir o formulário.

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MyForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')
```

- Certifique-se de instalar as extensões necessárias:

```bash
pip install Flask-WTF WTForms
```

**3. Crie uma Rota para o Formulário:**

```python
from forms import MyForm

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        return f'Formulário submetido com sucesso! Nome de usuário: {username}'

    return render_template('form.html', form=form)
```

**4. Crie o Template HTML para o Formulário:**

- Crie um arquivo chamado `form.html` dentro do diretório `templates`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário</title>
</head>
<body>
    <h1>Meu Formulário</h1>
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <p>{{ form.username.label }}</p>
        <p>{{ form.username }}</p>
        <p>{{ form.submit }}</p>
    </form>
</body>
</html>
```

## Explicação:
- `FlaskForm` e `StringField` são parte da extensão Flask-WTF e WTForms, respectivamente, para trabalhar com formulários em Flask.

- `form.validate_on_submit()`: Esta função valida o formulário quando é submetido.

- `form.hidden_tag()`: Gera campos ocultos no formulário para segurança contra ataques CSRF.

- `request.method == 'POST'`: Verifica se o formulário foi submetido.

- No template HTML, `{{ form.field_name }}` é usado para renderizar campos do formulário e `{{ form.hidden_tag() }}` para renderizar campos ocultos.

Essa é uma introdução básica à manipulação de formulários em Flask. Conforme sua aplicação cresce, você pode precisar adicionar mais campos ao formulário, trabalhar com validação, lidar com uploads de arquivos, entre outras funcionalidades avançadas. Para isso, a extensão Flask-WTF e WTForms são poderosas e flexíveis.