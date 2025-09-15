# Gerador de Grafo de Conhecimento

Aplicação Streamlit que extrai dados de grafo (entidades e relacionamentos) de texto usando LangChain e modelos GPT da OpenAI, e gera grafos interativos.

![CleanShot 2025-05-28 at 13 11 46](https://github.com/user-attachments/assets/4fef9158-8dd8-432d-bb8a-b53953a82c6c)

👉 Este repositório foi inspirado no tutorial de Thu Vu:
[![](https://img.youtube.com/vi/O-T_6KOXML4/0.jpg)](https://www.youtube.com/watch?v=O-T_6KOXML4)

## Funcionalidades

- Dois métodos de entrada: upload de texto (arquivos .txt) ou entrada direta de texto
- Visualização interativa de grafo de conhecimento
- Exibição de grafo personalizável com layout baseado em física
- Extração de relacionamentos entre entidades alimentada pelo modelo GPT-4o da OpenAI

## 🚀 Deploy Rápido no Streamlit Cloud

### Opção 1: Deploy Automático (Recomendado)

[![Deploy](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy)

1. **Fork este repositório** no GitHub
2. **Acesse** [Streamlit Cloud](https://share.streamlit.io/)
3. **Conecte sua conta GitHub** e selecione este repositório
4. **Configure as variáveis de ambiente:**
   - `OPENAI_API_KEY`: Sua chave da API OpenAI
5. **Clique em "Deploy"** e aguarde alguns minutos
6. **Acesse sua aplicação** no link fornecido

### Opção 2: Instalação Local

#### Pré-requisitos

- Python 3.8 ou superior
- Chave da API OpenAI

#### Dependências

A aplicação requer os seguintes pacotes Python:

- langchain (== 0.3.7): Framework principal de LLM
- langchain-experimental (== 0.3.7): Recursos experimentais do LangChain
- langchain-openai (== 0.2.8): Integração OpenAI para LangChain
- python-dotenv (== 1.0.1): Suporte a variáveis de ambiente
- pyvis (== 0.3.2): Visualização de grafos
- streamlit (== 1.39.0): Framework de interface web

Instale todas as dependências necessárias usando o arquivo requirements.txt fornecido:

```bash
pip install -r requirements.txt
```

#### Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/gerador-grafo-conhecimento-pt-br.git
   cd gerador-grafo-conhecimento-pt-br
   ```

2. Copie o arquivo de exemplo de configuração:
   ```bash
   cp .env.example .env
   ```

3. Edite o arquivo `.env` e adicione sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_da_api_openai_aqui
   ```

#### Executando a Aplicação

Para executar a aplicação Streamlit:

```bash
streamlit run app.py
```

Isso iniciará a aplicação e a abrirá em seu navegador padrão (tipicamente em http://localhost:8501).

## ☁️ Deploy no Streamlit Cloud

### Configuração de Variáveis de Ambiente

No Streamlit Cloud, você precisa configurar as seguintes variáveis de ambiente:

1. **OPENAI_API_KEY**: Sua chave da API OpenAI (obrigatória)
2. **OPENAI_MODEL**: Modelo a ser usado (opcional, padrão: gpt-4o)
3. **OPENAI_TEMPERATURE**: Temperatura do modelo (opcional, padrão: 0)

### Passos para Deploy

1. **Fork** este repositório no GitHub
2. **Acesse** [share.streamlit.io](https://share.streamlit.io/)
3. **Conecte** sua conta GitHub
4. **Selecione** o repositório forkado
5. **Configure** as variáveis de ambiente na seção "Advanced settings"
6. **Clique** em "Deploy"
7. **Aguarde** o deploy ser concluído (2-5 minutos)
8. **Acesse** sua aplicação no link fornecido

### Troubleshooting

- **Erro de API**: Verifique se a chave da API está correta
- **Timeout**: Aumente o timeout nas configurações avançadas
- **Dependências**: Verifique se todas as dependências estão no requirements.txt

## Como Usar

1. Escolha seu método de entrada na barra lateral (Enviar arquivo txt ou Inserir texto)
2. Se estiver enviando um arquivo, selecione um arquivo .txt do seu computador
3. Se estiver usando entrada direta, digite ou cole seu texto na área de texto
4. Clique no botão "Gerar Grafo de Conhecimento"
5. Aguarde o grafo ser gerado (isso pode levar alguns momentos dependendo do tamanho do texto)
6. Explore o grafo de conhecimento interativo:
   - Arraste nós para reorganizar o grafo
   - Passe o mouse sobre nós e arestas para ver informações adicionais
   - Zoom in/out usando a roda do mouse
   - Filtre o grafo para nós e arestas específicos

## Como Funciona

A aplicação usa os transformadores de grafo experimentais do LangChain com o modelo GPT-4o da OpenAI para:
1. Extrair entidades do texto de entrada
2. Identificar relacionamentos entre essas entidades
3. Gerar uma estrutura de grafo representando essas informações
4. Visualizar o grafo usando PyVis, uma interface Python para a biblioteca de visualização vis.js

## Licença

Este projeto está licenciado sob a Licença MIT - uma licença de código aberto permissiva que permite uso, modificação e distribuição gratuitos do software.

Para mais detalhes, consulte a documentação da [Licença MIT](https://opensource.org/licenses/MIT).
