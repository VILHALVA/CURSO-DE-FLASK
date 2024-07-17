# MANUAL
## INICIO:
1. **Instale o Flask**:
    Antes de iniciar, você precisa instalar o Flask. Você pode fazer isso usando o pip, o gerenciador de pacotes do Python:
    ```bash
    pip install Flask
    ```

2. **Crie um arquivo `app.py` e adicione o seguinte código**:
    Abaixo está um exemplo básico de um aplicativo Flask que cria um servidor web simples para exibir "Hello, World!" quando acessado:

    ```python
    from flask import Flask

    # Crie uma instância do aplicativo Flask
    app = Flask(__name__)

    # Defina uma rota padrão que responde com "Hello, World!"
    @app.route('/')
    def hello():
        return 'Hello, World!'

    # Se este arquivo for executado diretamente, inicie o servidor
    if __name__ == '__main__':
        app.run(debug=True)
    ```

    **EXPLICAÇÃO:**
    - Importamos a classe Flask do módulo flask.
    - Criamos uma instância do aplicativo Flask, passando `__name__` como argumento. Isso ajuda o Flask a determinar a localização dos arquivos estáticos, entre outras coisas.
    - Definimos uma rota usando o decorador `@app.route('/')`. Isso indica que a função `hello()` será executada quando a rota raiz (`/`) for acessada.
    - A função `hello()` simplesmente retorna a string "Hello, World!".
    - Finalmente, usamos `app.run()` para iniciar o servidor. Se o arquivo `app.py` for executado diretamente (ou seja, não importado como um módulo em outro arquivo), o servidor Flask será iniciado.
    
3. **Executando o Aplicativo:**
   - Após instalar as dependências, para iniciar o servidor, navegue até o diretório da raiz do seu projeto no terminal.
   - Em seguida, execute o seguinte comando para iniciar o servidor Flask:
   ```bash
   python app.py
   ```
   - Uma vez que o servidor esteja em execução, você poderá acessar o aplicativo através do seu navegador, visitando o seguinte endereço: `http://localhost:5000/`. Você deverá ver a mensagem "Hello, World!" sendo exibida.

## SOBRE OS REQUIREMENTOS:
1. **Criando o requirements.txt:**
    Para criar o `requirements.txt`, você pode executar o seguinte comando:
    ```
    pip freeze > requirements.txt
    ```

    O comando `pip freeze` é utilizado para listar todas as dependências instaladas no ambiente Python juntamente com suas versões. Por exemplo, ao executar `pip freeze`, você verá uma lista de pacotes instalados e suas versões, algo assim:

    ```
    Flask==2.0.1
    Werkzeug==2.0.2
    ...
    ```

    Já o símbolo `>` é usado para redirecionar a saída de um comando para um arquivo. No caso específico do `pip freeze`, o redirecionamento para um arquivo chamado `requirements.txt` é uma prática comum para criar um arquivo que liste todas as dependências do projeto.

    Portanto, quando você executa `pip freeze > requirements.txt`, está dizendo ao Python para listar todas as dependências e salvar essa lista no arquivo `requirements.txt`. Isso é útil para compartilhar o ambiente de desenvolvimento com outras pessoas ou para garantir que você possa instalar exatamente as mesmas versões das dependências em outro ambiente.

2. **Instalando as dependências:**
    Antes de executar o aplicativo, é essencial garantir que todas as dependências necessárias estejam instaladas. O arquivo `requirements.txt` contém uma lista das dependências e suas versões correspondentes. Para instalar essas dependências, siga estas etapas:

    1. Abra o terminal ou prompt de comando na pasta raiz do seu projeto.

    2. Execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:
    
        ```bash
        pip install -r requirements.txt
        ```

    Isso instruirá o pip a ler o arquivo `requirements.txt` e instalar todas as dependências listadas, garantindo que o ambiente de desenvolvimento seja configurado corretamente.

    3. Aguarde até que todas as dependências sejam baixadas e instaladas. Isso pode levar alguns minutos, dependendo do número e do tamanho das dependências.

    4. Após a conclusão da instalação, você estará pronto para executar o aplicativo Flask sem problemas de dependências ausentes.

## DIRETÓRIOS:
Abaixo está uma explicação da estrutura de diretórios no padrão Model-View-Controller (MVC):

```markdown
- projeto/
    - __init__.py
    - models/
        - __init__.py
        - user.py
        - post.py
    - views/
        - __init__.py
        - user_view.py
        - post_view.py
    - controllers/
        - __init__.py
        - user_controller.py
        - post_controller.py
    - templates/
        - index.html
        - user/
            - profile.html
            - settings.html
        - post/
            - list.html
            - detail.html
```

### COM EXPLICAÇÃO:
```
- **projeto/**: Diretório raiz do projeto.
    - **__init__.py**: Arquivo vazio que indica que o diretório é um pacote Python.
    - **models/**: Diretório que contém os modelos de dados.
        - **__init__.py**: Arquivo que inicializa o pacote `models`.
        - **user.py**: Arquivo que contém o modelo de usuário.
        - **post.py**: Arquivo que contém o modelo de postagem.
    - **views/**: Diretório que contém as visualizações (ou controladores de apresentação).
        - **__init__.py**: Arquivo que inicializa o pacote `views`.
        - **user_view.py**: Arquivo que contém as visualizações relacionadas ao usuário.
        - **post_view.py**: Arquivo que contém as visualizações relacionadas às postagens.
    - **controllers/**: Diretório que contém os controladores.
        - **__init__.py**: Arquivo que inicializa o pacote `controllers`.
        - **user_controller.py**: Arquivo que contém os controladores relacionados ao usuário.
        - **post_controller.py**: Arquivo que contém os controladores relacionados às postagens.
    - **templates/**: Diretório que contém os templates HTML.
        - **index.html**: Página inicial do site.
        - **user/**: Diretório com os templates relacionados ao usuário.
            - **profile.html**: Template para exibir o perfil do usuário.
            - **settings.html**: Template para exibir as configurações do usuário.
        - **post/**: Diretório com os templates relacionados às postagens.
            - **list.html**: Template para exibir a lista de postagens.
            - **detail.html**: Template para exibir os detalhes de uma postagem.
```

Essa é uma estrutura típica de diretórios para um projeto usando o padrão MVC em Python, onde os modelos (`models`), visualizações (`views`) e controladores (`controllers`) são separados em diretórios distintos para manter o código organizado e modular. Os templates HTML são armazenados no diretório `templates`. O arquivo `__init__.py` em cada diretório indica que eles são pacotes Python.

    







