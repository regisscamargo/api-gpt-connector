# API de Conexão com o ChatGPT

Este repositório abriga uma API e uma interface projetadas para facilitar a comunicação com o modelo GPT (Generative Pre-trained Transformer) da OpenAI. Com esta ferramenta, os usuários podem fazer perguntas e receber respostas de maneira eficiente. É importante destacar que o acesso a uma chave de API fornecida pela OpenAI é necessário para utilizar este serviço. Caso o usuário não possua uma chave válida ou não disponha de cotas suficientes para utilização, o código retornará um erro indicando "insufficient_quota".

## Descrição

A API desenvolvida neste projeto é uma ferramenta de integração com os modelos GPT da OpenAI, projetada para facilitar a comunicação com o chatbot. Ela permite aos usuários enviar perguntas para o modelo GPT e receber respostas geradas pelo mesmo, tudo isso de forma simples e intuitiva.

## Funcionalidades

- **Envio de Perguntas:** Os usuários podem enviar perguntas para o modelo GPT através da Interface que se comunica com a API.
- **Recebimento de Respostas:** Após enviar uma pergunta, os usuários recebem a resposta gerada pelo modelo GPT.
- **Integração Facilitada:** A API é projetada para facilitar a integração com outras aplicações, permitindo uma comunicação eficiente com o chatbot.

## Estrutura do Projeto

O projeto é composto por uma API desenvolvida em Python, que se comunica com os modelos GPT da OpenAI por meio de requisições HTTP.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal para implementação da API.
- **OpenAI GPT:** Modelo de linguagem natural utilizado para gerar respostas às perguntas dos usuários.
- **Flask:** Framework utilizado para criar a API web em Python.
- **Docker:** Implantação e execução de aplicativos em contêineres, garantindo a portabilidade e consistência da aplicação em diferentes ambientes.

## Como Usar

**Executando o aap.py**
1. Clone este repositório em sua máquina local.
2. Instale as dependências do projeto.
3. Acesse a pasta chatgpt_api > constants.py e insira sua KEY válida gerada pelo GPT. **Exemplo: ACCESS_KEY_GPT = "sua-chave-aqui"**
4. Execute a API usando o Flask, o app.py e acesse **http://localhost:5000/index** - confira a porta destinada em app.py
5. Envie perguntas para a API e receba as respostas geradas pelo modelo GPT.

**Executando o Docker**
1. Caso deseje, pode montar a imagem Docker execute os comandos abaixo
2. Acesse a pasta chatgpt_api > constants.py e insira sua KEY válida gerada pelo GPT. **Exemplo: ACCESS_KEY_GPT = "sua-chave-aqui"**
3. Execute docker build -t ms-chat-gpt . e depois de criado, executar docker compose up
4. Acesse **http://127.0.0.1:5000** - confira a porta destinada em docker.compose.yaml
5. Envie perguntas para a API e receba as respostas geradas pelo modelo GPT.

## Autor
Este projeto foi desenvolvido por Régis Camargo.
