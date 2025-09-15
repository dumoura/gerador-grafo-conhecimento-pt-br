# 🚀 Guia Completo para Publicar no GitHub

## 📋 Passo a Passo

### 1. Criar Repositório no GitHub

1. **Acesse:** https://github.com/new
2. **Configure:**
   - **Repository name:** `gerador-grafo-conhecimento-pt-br`
   - **Description:** `Gerador de Grafo de Conhecimento em Português Brasileiro - Aplicação Streamlit que extrai entidades e relacionamentos de texto usando LangChain e OpenAI`
   - **Visibility:** Public (recomendado)
   - **NÃO** marque "Add a README file"
   - **NÃO** marque "Add .gitignore"
   - **NÃO** marque "Choose a license" (já temos um)

3. **Clique em "Create repository"**

### 2. Executar Script de Configuração

```bash
./setup-github.sh
```

O script irá:
- Pedir seu nome de usuário do GitHub
- Configurar o remote automaticamente
- Fazer o push do código

### 3. Configuração Manual (Alternativa)

Se preferir fazer manualmente:

```bash
# Substitua SEU_USUARIO pelo seu nome de usuário do GitHub
git remote add origin https://github.com/SEU_USUARIO/gerador-grafo-conhecimento-pt-br.git
git push -u origin main
```

## 🎯 Configurações Recomendadas no GitHub

### Topics (Tags)
Adicione estas topics no repositório:
- `streamlit`
- `langchain`
- `openai`
- `knowledge-graph`
- `portuguese`
- `brazilian-portuguese`
- `ai`
- `nlp`
- `graph-visualization`

### Descrição do Repositório
```
🧠 Gerador de Grafo de Conhecimento em Português Brasileiro

Aplicação Streamlit que extrai entidades e relacionamentos de texto usando LangChain e OpenAI GPT-4o, gerando grafos interativos de conhecimento.

✨ Características:
• Interface 100% em Português Brasileiro
• Upload de arquivos .txt ou entrada direta de texto
• Visualização interativa de grafos
• Extração inteligente de entidades e relacionamentos
• Configuração simples com arquivo .env

🚀 Tecnologias: Streamlit, LangChain, OpenAI, PyVis
```

### README Personalizado
O README já está configurado, mas você pode adicionar:
- Badges de status
- Screenshots da aplicação
- Links para demo online
- Contribuição guidelines

## 🔧 Configurações Avançadas

### GitHub Pages (Opcional)
Para criar uma página de demonstração:

1. Vá em Settings > Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)
5. Salve

### Actions (Opcional)
Para CI/CD automático, crie `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Streamlit Cloud
      uses: streamlit/streamlit-cloud-action@v1
      with:
        streamlit-app-path: app.py
```

### Issues Template
Crie `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug report
about: Reportar um problema
title: '[BUG] '
labels: bug
assignees: ''

---

**Descrição do Bug**
Uma descrição clara do problema.

**Como Reproduzir**
1. Vá para '...'
2. Clique em '....'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente:**
 - OS: [ex: macOS, Windows]
 - Python: [ex: 3.9]
 - Streamlit: [ex: 1.32.0]
```

## 📊 Métricas e Analytics

### Shields.io Badges
Adicione ao README:

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
```

### Repo Stats
```markdown
![GitHub stars](https://img.shields.io/github/stars/SEU_USUARIO/gerador-grafo-conhecimento-pt-br)
![GitHub forks](https://img.shields.io/github/forks/SEU_USUARIO/gerador-grafo-conhecimento-pt-br)
![GitHub issues](https://img.shields.io/github/issues/SEU_USUARIO/gerador-grafo-conhecimento-pt-br)
```

## 🎉 Próximos Passos

1. **Teste a aplicação** localmente
2. **Faça screenshots** da interface
3. **Crie um demo** online (Streamlit Cloud)
4. **Compartilhe** nas redes sociais
5. **Adicione** ao seu portfólio

---

**Boa sorte com seu projeto! 🚀** 