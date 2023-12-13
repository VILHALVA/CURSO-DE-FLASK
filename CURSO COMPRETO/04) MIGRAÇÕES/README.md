# MIGRAÇÕES
Quando você trabalha com bancos de dados em uma aplicação Flask, é uma boa prática usar migrações para gerenciar alterações no esquema do banco de dados ao longo do tempo. A extensão Flask-Migrate é comumente usada para facilitar esse processo.

Aqui estão os passos básicos para usar Flask-Migrate:

1. **Instale o Flask-Migrate:**

   ```bash
   pip install Flask-Migrate
   ```

2. **Configure o Flask-Migrate na sua aplicação:**

   No script principal da sua aplicação (onde você cria a instância do Flask), inicialize o Flask-Migrate.

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_migrate import Migrate

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
   db = SQLAlchemy(app)
   migrate = Migrate(app, db)
   ```

3. **Crie as migrações iniciais:**

   Após configurar o Flask-Migrate, você precisa criar uma migração inicial que representa o estado inicial do seu banco de dados.

   Execute os seguintes comandos no terminal:

   ```bash
   flask db init
   flask db migrate -m "initial commit"
   ```

   O primeiro comando inicializa o diretório de migrações, enquanto o segundo cria a migração inicial.

4. **Aplique as migrações ao banco de dados:**

   Depois de criar a migração, você precisa aplicá-la ao banco de dados.

   ```bash
   flask db upgrade
   ```

   Este comando aplica todas as migrações pendentes ao banco de dados.

5. **Trabalhando com Migrações Futuras:**

   Sempre que você fizer alterações no seu modelo de dados, execute os seguintes comandos para criar e aplicar migrações:

   ```bash
   flask db migrate -m "descrição da alteração"
   flask db upgrade
   ```

   O primeiro comando cria uma nova migração com base nas alterações no modelo, e o segundo aplica essas alterações ao banco de dados.

Este é um resumo básico do uso do Flask-Migrate. Lembre-se de que o processo de migração é crucial ao trabalhar com bancos de dados em ambientes de produção para garantir que as alterações no esquema do banco de dados sejam aplicadas de maneira controlada e consistente.