#!/bin/bash

echo "🚀 Configurando repositório GitHub para Gerador de Grafo de Conhecimento"
echo ""

# Verificar se o repositório foi criado
echo "📋 PASSO 1: Crie o repositório no GitHub"
echo "1. Acesse: https://github.com/new"
echo "2. Nome: gerador-grafo-conhecimento-pt-br"
echo "3. Descrição: Gerador de Grafo de Conhecimento em Português Brasileiro"
echo "4. NÃO marque 'Add README' ou 'Add .gitignore'"
echo "5. Clique em 'Create repository'"
echo ""

read -p "✅ Repositório criado? Pressione ENTER para continuar..."

# Obter o nome do usuário
echo "👤 Qual é seu nome de usuário no GitHub?"
read github_username

# Configurar o remote
echo "🔗 Configurando remote do Git..."
git remote add origin https://github.com/$github_username/gerador-grafo-conhecimento-pt-br.git

# Fazer push
echo "📤 Fazendo push para o GitHub..."
git push -u origin main

echo ""
echo "🎉 Repositório configurado com sucesso!"
echo "🌐 Acesse: https://github.com/$github_username/gerador-grafo-conhecimento-pt-br"
echo ""
echo "📋 Próximos passos:"
echo "1. Adicione uma descrição no README do GitHub"
echo "2. Configure as topics: streamlit, langchain, openai, knowledge-graph, portuguese"
echo "3. Adicione um arquivo .env.example (já está incluído)"
echo "4. Configure GitHub Pages se desejar" 