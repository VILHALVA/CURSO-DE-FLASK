# MANUAL
## INICIO:
1. **Crie o ambiente virtual:**
   Você pode instalar o `virtualenv` usando o `pip`, que é o gerenciador de pacotes do Python.

   Para instalar o `virtualenv`, você pode executar o seguinte comando:

   ```
   pip install virtualenv
   ```

   Depois de instalar o `virtualenv`, você pode criar um novo ambiente virtual com o seguinte comando:

   ```
   virtualenv venv
   ```

   Se quiser, você pode substituir "venv" pelo nome que você deseja dar ao seu ambiente virtual (Não se esqueça de atualizar o `.gitignore`). Em seguida, você pode ativar o ambiente virtual com os seguintes comandos:

   - No Windows:

   ```
   venv\Scripts\activate
   ```

   - No Linux/Mac:

   ```
   source venv/bin/activate
   ```

   Uma vez ativado o ambiente virtual, você pode tentar instalar os pacotes necessários usando o `pip`, e eles serão instalados apenas no escopo do ambiente virtual, evitando possíveis conflitos com outros pacotes no seu sistema.

2. **Instale o Flask**:
    Antes de iniciar, você precisa instalar o Flask. Você pode fazer isso usando o pip, o gerenciador de pacotes do Python:
    ```bash
    pip install Flask
    ```

3. **Crie um arquivo `app.py` e adicione o seguinte código**:
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
    
4. **Executando o Aplicativo:**
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

    







