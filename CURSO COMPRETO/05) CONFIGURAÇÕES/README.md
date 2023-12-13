# CONFIGURAÇÕES
As configurações em uma aplicação Flask são usadas para definir variáveis de configuração que controlam o comportamento da aplicação em diferentes ambientes (desenvolvimento, teste, produção, etc.). O Flask utiliza o objeto `config` para gerenciar essas configurações.

Aqui estão algumas configurações comuns e como você pode configurar a sua aplicação Flask:

1. **Chave Secreta:**
   A chave secreta é usada para proteger sessões e outras coisas. Certifique-se de definir uma chave secreta ao criar sua aplicação.

   ```python
   app.config['SECRET_KEY'] = 'sua_chave_secreta'
   ```

2. **Ambiente de Execução:**
   Defina o ambiente de execução, como "development" ou "production". Isso pode afetar o comportamento da aplicação.

   ```python
   app.config['ENV'] = 'development'
   ```

3. **Debug Mode:**
   O modo de depuração permite ver mensagens detalhadas de erro e reinicia automaticamente a aplicação quando você faz alterações no código.

   ```python
   app.config['DEBUG'] = True
   ```

4. **Configuração do Banco de Dados:**
   Se você estiver usando um banco de dados, configure a URL do banco de dados.

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
   ```

5. **Habilitar/Desabilitar Recursos:**
   Configure recursos específicos, como a ativação ou desativação do envio de e-mails.

   ```python
   app.config['MAIL_SERVER'] = 'smtp.example.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   ```

6. **Configurações Personalizadas:**
   Você pode definir suas próprias configurações personalizadas conforme necessário.

   ```python
   app.config['MY_CUSTOM_SETTING'] = 'valor_personalizado'
   ```

7. **Usando Arquivos de Configuração:**
   Em vez de definir configurações diretamente no código, você pode usar arquivos de configuração. Por exemplo, você pode criar um arquivo `config.py`:

   ```python
   class Config:
       SECRET_KEY = 'sua_chave_secreta'
       SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
   ```

   E, em seguida, carregá-lo na sua aplicação:

   ```python
   app.config.from_object('config.Config')
   ```

   Ou você pode usar variáveis de ambiente ou outros métodos para carregar configurações dinamicamente.

8. **Configurações Sensíveis:**
   Para informações sensíveis, como chaves de API ou senhas, é uma prática recomendada usar variáveis de ambiente e carregá-las em sua aplicação Flask.

   ```python
   import os

   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   app.config['API_KEY'] = os.environ.get('API_KEY')
   ```

   Certifique-se de configurar essas variáveis de ambiente em seu ambiente de execução.

Lembre-se de que, ao lidar com configurações sensíveis, é crucial manter essas informações confidenciais e não compartilhá-las diretamente em repositórios públicos. Use práticas seguras, como o uso de variáveis de ambiente e ferramentas para gestão de segredos, conforme necessário.