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

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Chave da API OpenAI

### Dependências

A aplicação requer os seguintes pacotes Python:

- langchain (>= 0.1.0): Framework principal de LLM
- langchain-experimental (>= 0.0.45): Recursos experimentais do LangChain
- langchain-openai (>= 0.1.0): Integração OpenAI para LangChain
- python-dotenv (>= 1.0.0): Suporte a variáveis de ambiente
- pyvis (>= 0.3.2): Visualização de grafos
- streamlit (>= 1.32.0): Framework de interface web

Instale todas as dependências necessárias usando o arquivo requirements.txt fornecido:

```bash
pip install -r requirements.txt
```

### Configuração

1. Clone este repositório:
   ```bash
   git clone [url-do-repositório]
   cd knowledge_graph_app_2
   ```

   Nota: Substitua `[url-do-repositório]` pela URL real deste repositório.

2. Crie um arquivo `.env` no diretório raiz com sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_da_api_openai_aqui
   ```

## Executando a Aplicação

Para executar a aplicação Streamlit:

```bash
streamlit run app.py
```

Isso iniciará a aplicação e a abrirá em seu navegador padrão (tipicamente em http://localhost:8501).

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
