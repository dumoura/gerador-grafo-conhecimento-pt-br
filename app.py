# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components  # For embedding custom HTML
from generate_knowledge_graph import generate_knowledge_graph

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Gerador de Grafo de Conhecimento",
    page_icon="🧠", 
    layout="wide",  # Use wide layout for better graph display
    initial_sidebar_state="auto", 
    menu_items=None
)

# Set the title of the app
st.title("🧠 Gerador de Grafo de Conhecimento")
st.markdown("### Extraia entidades e relacionamentos do seu texto usando IA")

# Initialize text variable
text = ""

# Sidebar section for user input method
st.sidebar.title("📄 Documento de Entrada")
input_method = st.sidebar.radio(
    "Escolha um método de entrada:",
    ["📁 Enviar arquivo txt", "✏️ Inserir texto"],  # Options for uploading a file or manually inputting text
)

# Case 1: User chooses to upload a .txt file
if input_method == "📁 Enviar arquivo txt":
    # File uploader widget in the sidebar
    uploaded_file = st.sidebar.file_uploader(label="Enviar arquivo", type=["txt"])
    
    if uploaded_file is not None:
        # Read the uploaded file content and decode it as UTF-8 text
        text = uploaded_file.read().decode("utf-8")
        
        # Show file info
        st.sidebar.success(f"✅ Arquivo carregado: {uploaded_file.name}")
        st.sidebar.info(f"📊 Tamanho: {len(text)} caracteres")
 
        # Button to generate the knowledge graph
        if st.sidebar.button("🚀 Gerar Grafo de Conhecimento", type="primary"):
            with st.spinner("🔄 Gerando grafo de conhecimento..."):
                # Call the function to generate the graph from the text
                net = generate_knowledge_graph(text)
                st.success("✅ Grafo de conhecimento gerado com sucesso!")
                
                # Save the graph to an HTML file
                output_file = "knowledge_graph.html"
                net.save_graph(output_file) 

                # Open the HTML file and display it within the Streamlit app
                HtmlFile = open(output_file, 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=1000)

# Case 2: User chooses to directly input text
else:
    # Text area for manual input
    text = st.sidebar.text_area("Inserir texto", height=300, placeholder="Cole ou digite seu texto aqui...")

    if text:  # Check if the text area is not empty
        # Show text info
        st.sidebar.info(f"📊 Texto inserido: {len(text)} caracteres")
        
        if st.sidebar.button("🚀 Gerar Grafo de Conhecimento", type="primary"):
            with st.spinner("🔄 Gerando grafo de conhecimento..."):
                # Call the function to generate the graph from the input text
                net = generate_knowledge_graph(text)
                st.success("✅ Grafo de conhecimento gerado com sucesso!")
                
                # Save the graph to an HTML file
                output_file = "knowledge_graph.html"
                net.save_graph(output_file) 

                # Open the HTML file and display it within the Streamlit app
                HtmlFile = open(output_file, 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=1000)

# Add instructions in the main area
if not text:
    st.markdown("""
    ## 📋 Como usar:
    
    1. **Escolha o método de entrada** no painel lateral
    2. **Envie um arquivo .txt** ou **cole seu texto** na área de texto
    3. **Clique em "Gerar Grafo de Conhecimento"**
    4. **Explore o grafo interativo** que será gerado
    
    ### 🎯 Funcionalidades do grafo:
    - **Arraste os nós** para reorganizar o grafo
    - **Passe o mouse** sobre nós e arestas para ver informações
    - **Zoom** usando a roda do mouse
    - **Filtre** o grafo para nós e arestas específicos
    
    ### 💡 Dica:
    Quanto mais detalhado e estruturado for o texto, melhor será o grafo de conhecimento gerado!
    """)

# Add footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Desenvolvido com ❤️ usando Streamlit, LangChain e OpenAI</p>
</div>
""", unsafe_allow_html=True)