# LOGIN
A implementação de um sistema de login em uma aplicação Flask geralmente envolve o uso de extensões específicas para gerenciar autenticação de usuários. Uma extensão comum para isso é o Flask-Login. Vou guiá-lo através dos passos básicos para implementar um sistema de login usando Flask-Login.

## Instalação e Configuração:
Certifique-se de ter as extensões necessárias instaladas:

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF WTForms Flask-Login
```

## Exemplo Básico de Login:
**1. Configure o Flask-Login:**

```python
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_super_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
```

**2. Crie o Modelo do Usuário:**

```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'Usuário: {self.username}'
```

**3. Crie o Formulário de Login:**

```python
class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
```

**4. Rotas para o Login:**

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Falha no login. Verifique seu nome de usuário e senha.', 'danger')

    return render_template('login.html', form=form)
```

**5. Rotas para o Logout e Dashboard:**

```python
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Bem-vindo, {current_user.username}!'
```

**6. Template HTML para o Login:**

- Crie um arquivo chamado `login.html` dentro do diretório `templates`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <p>{{ form.username.label }}</p>
        <p>{{ form.username }}</p>
        <p>{{ form.password.label }}</p>
        <p>{{ form.password }}</p>
        <p>{{ form.submit }}</p>
    </form>
</body>
</html>
```

## Explicação:
- `Flask-Login` simplifica o gerenciamento de sessões de usuários e fornece funções como `login_user`, `logout_user`, e `current_user`.

- `UserMixin` fornece implementações padrão de métodos de usuário, facilitando a integração com Flask-Login.

- `login_manager.login_view = 'login'` define a rota para onde os usuários serão redirecionados se tentarem acessar uma rota protegida sem estar autenticados.

- A rota `/login` valida o formulário, autentica o usuário e redireciona para o painel de controle (`dashboard`) em caso de sucesso.

- A rota `/logout` faz o logout do usuário e redireciona para a rota inicial (`home`).

- `@login_required` é um decorador que protege uma rota, garantindo que o usuário esteja autenticado antes de acessá-la.

Este é um exemplo básico de implementação de login em uma aplicação Flask. Dependendo dos requisitos da sua aplicação, você pode precisar de funcionalidades adicionais, como registro de usuários, redefinição de senha, etc.