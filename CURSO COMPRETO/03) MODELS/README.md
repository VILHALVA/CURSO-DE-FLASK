# MODELS 
Em Flask, o termo "model" geralmente se refere à camada de dados ou à representação da estrutura de dados no seu aplicativo. O modelo em um contexto de aplicativo web é frequentemente associado a bancos de dados, pois é onde você define a estrutura dos dados que sua aplicação vai armazenar e manipular.

Vamos passar pelos passos básicos para usar um modelo em Flask, usando um banco de dados simples, SQLite, como exemplo. Existem várias extensões em Flask, como Flask-SQLAlchemy, que facilitam a integração de bancos de dados.

1. **Instale a extensão Flask-SQLAlchemy:**

   ```bash
   pip install Flask-SQLAlchemy
   ```

2. **Crie uma aplicação Flask com um modelo:**

   Vamos criar uma aplicação simples com um modelo para armazenar informações de usuários.

   ```python
   from flask import Flask, render_template
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Usando SQLite, o arquivo será criado na mesma pasta do script
   db = SQLAlchemy(app)

   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(20), unique=True, nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)

       def __repr__(self):
           return f"User('{self.username}', '{self.email}')"

   @app.route('/')
   def index():
       return render_template('index.html')

   if __name__ == '__main__':
       db.create_all()  # Cria as tabelas no banco de dados
       app.run(debug=True)
   ```

3. **Criar tabelas no banco de dados:**

   Ao executar o aplicativo pela primeira vez, as tabelas no banco de dados devem ser criadas. No exemplo acima, `db.create_all()` faz isso automaticamente. Execute o aplicativo e acesse `http://localhost:5000/` para criar as tabelas.

4. **Utilize o modelo nas rotas:**

   Agora você pode usar o modelo nas rotas para realizar operações no banco de dados. Por exemplo, adicionar um usuário:

   ```python
   from flask import request, redirect, url_for

   @app.route('/add_user', methods=['POST'])
   def add_user():
       username = request.form['username']
       email = request.form['email']

       new_user = User(username=username, email=email)
       db.session.add(new_user)
       db.session.commit()

       return redirect(url_for('index'))
   ```

   Este é um exemplo básico e há muitos outros conceitos e práticas recomendadas ao trabalhar com modelos e bancos de dados em uma aplicação Flask. Se você está construindo um aplicativo mais complexo, pode ser útil considerar o uso de extensões mais avançadas, como Flask-Migrate para gerenciar migrações de banco de dados.