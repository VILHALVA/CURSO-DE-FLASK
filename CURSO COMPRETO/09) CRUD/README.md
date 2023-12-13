# CRUD
CRUD (Create, Read, Update, Delete) é um conjunto de operações básicas frequentemente utilizadas em sistemas que envolvem banco de dados e manipulação de dados. Vou guiar você na implementação básica de um CRUD usando Flask e SQLAlchemy, que é um ORM (Object-Relational Mapping) para interagir com bancos de dados relacionais.

## Instalação e Configuração:
Certifique-se de ter as extensões necessárias instaladas:

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF WTForms
```

## Exemplo Básico de CRUD:
**1. Crie a Aplicação:**

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_super_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

**2. Crie o Modelo:**

```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'Todo Item: {self.content}'
```

**3. Crie o Formulário:**

```python
class TodoForm(FlaskForm):
    content = StringField('Tarefa', render_kw={"placeholder": "Digite sua tarefa aqui..."})
    submit = SubmitField('Adicionar Tarefa')
```

**4. Crie Rotas para o CRUD:**

```python
@app.route('/')
def index():
    todos = Todo.query.all()
    form = TodoForm()
    return render_template('index.html', todos=todos, form=form)

@app.route('/add', methods=['POST'])
def add():
    form = TodoForm()

    if form.validate_on_submit():
        new_todo = Todo(content=form.content.data)
        db.session.add(new_todo)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo_to_delete = Todo.query.get(id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
```

**5. Crie o Template HTML:**

- Crie um arquivo chamado `index.html` dentro do diretório `templates`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD com Flask</title>
</head>
<body>
    <h1>Lista de Tarefas</h1>

    <form method="POST" action="/add">
        {{ form.hidden_tag() }}
        <p>{{ form.content }}</p>
        <p>{{ form.submit }}</p>
    </form>

    <ul>
        {% for todo in todos %}
            <li>{{ todo.content }} | <a href="{{ url_for('delete', id=todo.id) }}">Excluir</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Explicação:
- `Todo` é o modelo que representa uma tarefa.

- `TodoForm` é o formulário utilizado para adicionar novas tarefas.

- `index()` mostra a lista de tarefas e o formulário de adição.

- `add()` adiciona uma nova tarefa ao banco de dados.

- `delete()` exclui uma tarefa do banco de dados.

- O template HTML usa a sintaxe Jinja2 para iterar sobre as tarefas e exibir o formulário.

Esse é um exemplo básico de como implementar um CRUD com Flask e SQLAlchemy. À medida que sua aplicação cresce, você pode precisar adicionar mais funcionalidades, como edição de tarefas, ordenação, filtragem, autenticação de usuários, entre outras.