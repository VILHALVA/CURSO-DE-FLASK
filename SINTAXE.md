# SINTAXE
Abaixo está um exemplo básico de um aplicativo Flask que cria um servidor web simples para exibir "Hello, World!" quando acessado:

1. **Instale o Flask**:
Antes de iniciar, você precisa instalar o Flask. Você pode fazer isso usando o pip, o gerenciador de pacotes do Python:
```bash
pip install Flask
```

2. **Crie um arquivo `app.py` e adicione o seguinte código**:
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

3. **Inicie o servidor**:
Para iniciar o servidor, execute o arquivo `app.py`:
```bash
python app.py
```

4. **Acesse o aplicativo no navegador**:
Abra um navegador da web e vá para `http://localhost:5000/`. Você deverá ver a mensagem "Hello, World!" sendo exibida.

**Explicação**:
- Importamos a classe Flask do módulo flask.
- Criamos uma instância do aplicativo Flask, passando `__name__` como argumento. Isso ajuda o Flask a determinar a localização dos arquivos estáticos, entre outras coisas.
- Definimos uma rota usando o decorador `@app.route('/')`. Isso indica que a função `hello()` será executada quando a rota raiz (`/`) for acessada.
- A função `hello()` simplesmente retorna a string "Hello, World!".
- Finalmente, usamos `app.run()` para iniciar o servidor. Se o arquivo `app.py` for executado diretamente (ou seja, não importado como um módulo em outro arquivo), o servidor Flask será iniciado.
- Quando o servidor está em execução, você pode acessá-lo em `http://localhost:5000/` em seu navegador.

