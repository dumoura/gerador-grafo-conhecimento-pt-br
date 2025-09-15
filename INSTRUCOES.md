# 📋 Instruções de Uso - Gerador de Grafo de Conhecimento

## 🚀 Como Executar a Aplicação

### 1. Pré-requisitos
- Python 3.8 ou superior
- Conexão com a internet (para acessar a API da OpenAI)

### 2. Instalação das Dependências
```bash
pip install -r requirements.txt
```

### 3. Configuração
O arquivo `.env` já está configurado com sua chave da API OpenAI:
```
OPENAI_API_KEY=sua_chave_da_api_openai_aqui
```

### 4. Executar a Aplicação
```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador em: `http://localhost:8501`

## 📖 Como Usar a Aplicação

### Método 1: Upload de Arquivo
1. Selecione "📁 Enviar arquivo txt" no painel lateral
2. Clique em "Browse files" e selecione um arquivo .txt
3. O arquivo será carregado e você verá informações sobre ele
4. Clique em "🚀 Gerar Grafo de Conhecimento"
5. Aguarde o processamento (pode levar alguns segundos)
6. Explore o grafo interativo que será gerado

### Método 2: Inserção Direta de Texto
1. Selecione "✏️ Inserir texto" no painel lateral
2. Cole ou digite seu texto na área de texto
3. Você verá o número de caracteres inseridos
4. Clique em "🚀 Gerar Grafo de Conhecimento"
5. Aguarde o processamento
6. Explore o grafo interativo

## 🎯 Funcionalidades do Grafo

### Interação com o Grafo:
- **Arrastar nós**: Clique e arraste os nós para reorganizar o grafo
- **Zoom**: Use a roda do mouse para dar zoom in/out
- **Informações**: Passe o mouse sobre nós e arestas para ver detalhes
- **Filtros**: Use os controles no canto superior direito para filtrar elementos

### Elementos do Grafo:
- **Nós (círculos)**: Representam entidades (pessoas, lugares, conceitos)
- **Arestas (linhas)**: Representam relacionamentos entre entidades
- **Cores**: Diferentes cores indicam diferentes tipos de entidades

## 💡 Dicas para Melhores Resultados

### Texto Ideal:
- Use textos estruturados e bem organizados
- Inclua nomes próprios, lugares e conceitos importantes
- Quanto mais detalhado o texto, melhor será o grafo
- Evite textos muito curtos (menos de 50 palavras)

### Exemplos de Textos:
- Artigos científicos
- Biografias
- Descrições de lugares
- Histórias e narrativas
- Documentos técnicos

## 🔧 Solução de Problemas

### Erro de API:
- Verifique se a chave da API está correta no arquivo `.env`
- Certifique-se de ter créditos disponíveis na sua conta OpenAI

### Aplicação não carrega:
- Verifique se todas as dependências foram instaladas
- Certifique-se de estar no diretório correto
- Verifique se a porta 8501 não está sendo usada por outro processo

### Grafo não aparece:
- Aguarde alguns segundos para o processamento
- Verifique se o texto tem conteúdo suficiente
- Tente com um texto diferente

## 📁 Arquivos do Projeto

- `app.py`: Aplicação principal do Streamlit
- `generate_knowledge_graph.py`: Lógica de geração do grafo
- `requirements.txt`: Dependências do projeto
- `.env`: Configurações da API
- `exemplo.txt`: Arquivo de exemplo para teste
- `README.md`: Documentação do projeto

## 🆘 Suporte

Se encontrar problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que a chave da API está correta
3. Teste com o arquivo `exemplo.txt` fornecido
4. Verifique a conexão com a internet

---

**Desenvolvido com ❤️ usando Streamlit, LangChain e OpenAI**
