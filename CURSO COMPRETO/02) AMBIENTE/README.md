# AMBIENTE
Preparar o ambiente de desenvolvimento é uma etapa importante antes de começar a trabalhar com Flask. Aqui estão os passos básicos para preparar o ambiente:

1. **Instalação do Python:**
   Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/).

2. **Instalação do Virtualenv (opcional, mas recomendado):**
   O Virtualenv é uma ferramenta que ajuda a criar ambientes Python isolados, o que é útil para gerenciar dependências específicas do projeto. Para instalá-lo, execute o seguinte comando:

   ```bash
   pip install virtualenv
   ```

   Depois de instalado, você pode criar um ambiente virtual em seu projeto usando:

   ```bash
   virtualenv venv
   ```

   E ativá-lo:

   - No Windows: `venv\Scripts\activate`
   - No Unix ou MacOS: `source venv/bin/activate`

3. **Instalação do Flask:**
   Dentro do ambiente virtual, você pode instalar o Flask utilizando o `pip`:

   ```bash
   pip install Flask
   ```

4. **Editor de Código:**
   Escolha um editor de código ou ambiente de desenvolvimento integrado (IDE) para trabalhar. Alguns populares incluem Visual Studio Code, PyCharm, Sublime Text, e Atom.

5. **Git (opcional):**
   Se você planeja versionar seu código com o Git, certifique-se de tê-lo instalado. Você pode baixar o Git em [git-scm.com](https://git-scm.com/).

Com esses passos, seu ambiente estará pronto para desenvolver aplicações Flask. Lembre-se de que a criação e ativação do ambiente virtual são práticas recomendadas para isolar as dependências do seu projeto, evitando conflitos entre diferentes projetos Python no mesmo sistema.