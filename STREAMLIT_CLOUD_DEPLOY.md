# 🚀 Deploy no Streamlit Cloud - Guia Completo

## 📋 Pré-requisitos

- Conta no GitHub
- Conta no Streamlit Cloud (conectada ao GitHub)
- Chave da API OpenAI

## 🔧 Passo a Passo

### 1. Preparar o Repositório

1. **Fork** este repositório no GitHub
2. **Clone** o repositório forkado para sua máquina local
3. **Teste** localmente para garantir que tudo funciona:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

### 2. Deploy no Streamlit Cloud

1. **Acesse** [share.streamlit.io](https://share.streamlit.io/)
2. **Faça login** com sua conta GitHub
3. **Clique** em "New app"
4. **Configure** o app:
   - **Repository**: Seu repositório forkado
   - **Branch**: main
   - **Main file path**: app.py
   - **App URL**: Escolha um nome único (ex: `meu-grafo-conhecimento`)

### 3. Configurar Variáveis de Ambiente

Na seção "Advanced settings", adicione:

```
OPENAI_API_KEY = sua_chave_da_api_openai_aqui
```

**Importante**: Substitua `sua_chave_da_api_openai_aqui` pela sua chave real da API OpenAI.

### 4. Deploy

1. **Clique** em "Deploy"
2. **Aguarde** o processo de deploy (2-5 minutos)
3. **Acesse** sua aplicação no link fornecido

## 🔍 Troubleshooting

### Erro: "OPENAI_API_KEY não encontrada"

**Solução**: Verifique se a variável de ambiente está configurada corretamente no Streamlit Cloud.

### Erro: "Module not found"

**Solução**: Verifique se todas as dependências estão no `requirements.txt` com versões específicas.

### Erro: "Timeout"

**Solução**: 
1. Aumente o timeout nas configurações avançadas
2. Use textos menores para teste
3. Verifique se a API da OpenAI está funcionando

### Erro: "Permission denied"

**Solução**: Verifique se o repositório é público ou se você tem as permissões corretas.

## 📊 Monitoramento

### Logs
- Acesse a aba "Logs" no Streamlit Cloud para ver erros
- Verifique se há mensagens de erro específicas

### Métricas
- Monitore o uso da API OpenAI
- Verifique o tempo de resposta da aplicação

## 🔄 Atualizações

Para atualizar sua aplicação:

1. **Faça push** das mudanças para o repositório
2. **Acesse** o Streamlit Cloud
3. **Clique** em "Reboot app" se necessário
4. A aplicação será atualizada automaticamente

## 💡 Dicas

- **Teste localmente** antes de fazer deploy
- **Use textos pequenos** para teste inicial
- **Monitore** o uso da API OpenAI
- **Mantenha** o repositório atualizado

## 🆘 Suporte

Se encontrar problemas:

1. Verifique os logs no Streamlit Cloud
2. Teste localmente primeiro
3. Verifique se a chave da API está correta
4. Consulte a documentação do Streamlit Cloud

---

**Boa sorte com seu deploy! 🚀**
