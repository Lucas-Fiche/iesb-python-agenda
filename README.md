# Agenda Telefônica | Atividade Avaliativa

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

[cite_start]Projeto de uma agenda telefônica de console, desenvolvido como parte de uma atividade avaliativa da faculdade[cite: 2, 3]. O foco principal do projeto é aplicar conceitos fundamentais de Python, como a manipulação de dicionários, funções e persistência de dados em arquivos.

## 🚀 Sobre o Projeto

A Agenda Telefônica é uma aplicação de terminal (console) que permite ao usuário gerenciar seus contatos de forma simples e eficiente. [cite_start]O programa armazena nome, telefone, e-mail e redes sociais (Twitter e Instagram) de cada contato[cite: 5]. Todos os dados são salvos em um arquivo local para que as informações não se percam ao fechar o programa.

### ✨ Funcionalidades

* [cite_start]**Menu Interativo:** Um menu de fácil navegação para acessar todas as funcionalidades do sistema[cite: 11].
* [cite_start]**Adicionar Contatos:** Permite a inserção de um ou mais contatos de uma só vez[cite: 19].
* [cite_start]**Consultar Contatos:** Busca e exibe os dados de um contato específico a partir do nome[cite: 13].
* [cite_start]**Alterar Contatos:** Modifica qualquer informação de um contato já cadastrado[cite: 17].
* [cite_start]**Remover Contatos:** Exclui um contato da agenda a partir do nome[cite: 16].
* [cite_start]**Listar Todos os Contatos:** Gera um relatório em formato de tabela com os dados de todos os contatos cadastrados[cite: 26].
* [cite_start]**Persistência de Dados:** Salva a agenda em um arquivo `agenda.txt` e carrega os dados ao iniciar o programa[cite: 35].

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Tabulate:** Biblioteca externa para a formatação e exibição de dados em tabelas no console.

## 🧠 Principais Aprendizados e Conceitos Aplicados

Este projeto foi fundamental para solidificar o conhecimento sobre a organização de um projeto em Python e a aplicação de estruturas de dados. Os principais tópicos abordados foram:

#### 1. **Modularização do Código**
   - [cite_start]O código foi dividido em funções específicas para cada responsabilidade (inserir, consultar, remover, etc.), conforme solicitado na atividade[cite: 22].
   - A estrutura foi separada em arquivos (`main.py`, `menu.py`, `agenda.py`) para melhorar a organização e a legibilidade.

#### 2. **Estrutura de Dados (Dicionários)**
   - [cite_start]Utilização de dicionários para armazenar os dados de cada contato de forma estruturada, facilitando o acesso e a manipulação das informações (nome, telefone, e-mail, etc.)[cite: 12].

#### 3. **Manipulação de Arquivos (File I/O)**
   - [cite_start]Implementação de funções para salvar (`'w'`) e carregar (`'r'`) os dados dos contatos em um arquivo de texto, garantindo a persistência das informações entre as execuções do programa[cite: 35].

#### 4. **Interface de Linha de Comando (CLI)**
   - Criação de um menu interativo no terminal, utilizando laços de repetição (`while`) e condicionais (`match case`) para processar a entrada do usuário e chamar as funções correspondentes.

#### 5. **Uso de Bibliotecas Externas**
   - Utilização da biblioteca `tabulate` para apresentar os relatórios de contatos de forma organizada e profissional, melhorando a experiência do usuário.

## 📂 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a Agenda Telefônica em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [URL-DO-SEU-REPOSITORIO]
    cd [NOME-DA-PASTA-DO-PROJETO]
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows
    .\.venv\Scripts\activate

    # Ativar no Linux/macOS
    source .venv/bin/activate
    ```

3.  **Crie o arquivo `requirements.txt`:**
    Crie um arquivo chamado `requirements.txt` na raiz do projeto e adicione o seguinte conteúdo:
    ```
    tabulate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python main.py
    ```
    A aplicação será iniciada no seu terminal.

## 👨‍💻 Autor

Projeto desenvolvido por **[Seu Nome Completo]** para a atividade da faculdade.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]([URL-DO-SEU-LINKEDIN])
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)]([URL-DO-SEU-GITHUB])