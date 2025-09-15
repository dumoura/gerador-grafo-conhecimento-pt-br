# 🔧 Troubleshooting - Streamlit Cloud

## ❌ Erro: "Error installing requirements"

### **Solução 1: Versões Simplificadas**
Se estiver usando versões específicas, tente usar versões mais flexíveis:

```txt
streamlit
langchain
langchain-experimental
langchain-openai
python-dotenv
pyvis
```

### **Solução 2: Verificar Compatibilidade**
1. Acesse [PyPI](https://pypi.org) e verifique se as versões existem
2. Use versões mais antigas se necessário
3. Remova dependências desnecessárias

### **Solução 3: Dependências Conflitantes**
Se houver conflitos entre pacotes:
1. Remova `pydantic` e `typing-extensions` temporariamente
2. Teste com apenas as dependências essenciais
3. Adicione dependências uma por vez

### **Solução 4: Cache do Streamlit Cloud**
1. Aguarde 5-10 minutos
2. Tente fazer deploy novamente
3. O cache pode estar causando problemas

## 🔍 Verificações Importantes

### **1. Verificar Logs**
- Acesse "Manage App" no Streamlit Cloud
- Clique em "Logs"
- Procure por erros específicos

### **2. Testar Localmente**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### **3. Verificar Python Version**
O Streamlit Cloud usa Python 3.9 por padrão.
Verifique se suas dependências são compatíveis.

## 🚀 Soluções Rápidas

### **Requirements.txt Mínimo**
```txt
streamlit
langchain
langchain-experimental
langchain-openai
python-dotenv
pyvis
```

### **Se Ainda Não Funcionar**
1. Use apenas `streamlit` e `langchain`
2. Adicione outras dependências gradualmente
3. Teste cada adição

## 📞 Suporte

Se o problema persistir:
1. Verifique os logs detalhados
2. Teste localmente primeiro
3. Consulte a documentação do Streamlit Cloud
4. Poste no fórum do Streamlit

---

**Dica**: Sempre teste localmente antes de fazer deploy! 🧪
