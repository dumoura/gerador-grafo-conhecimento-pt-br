from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from pyvis.network import Network

from dotenv import load_dotenv
import os
import asyncio


# Carrega o arquivo .env
load_dotenv()
# Obtém a chave da API das variáveis de ambiente
api_key = os.getenv("OPENAI_API_KEY")

# Configura o modelo LLM
llm = ChatOpenAI(
    temperature=0, 
    model_name="gpt-4o",
    api_key=api_key
)

# Configura o transformador de grafo
graph_transformer = LLMGraphTransformer(llm=llm)


# Extrai dados do grafo do texto de entrada
async def extract_graph_data(text):
    """
    Extrai assincronamente dados do grafo do texto de entrada usando um transformador de grafo.

    Args:
        text (str): Texto de entrada a ser processado em formato de grafo.

    Returns:
        list: Uma lista de objetos GraphDocument contendo nós e relacionamentos.
    """
    documents = [Document(page_content=text)]
    graph_documents = await graph_transformer.aconvert_to_graph_documents(documents)
    return graph_documents


def visualize_graph(graph_documents):
    """
    Visualiza um grafo de conhecimento usando PyVis baseado nos documentos de grafo extraídos.

    Args:
        graph_documents (list): Uma lista de objetos GraphDocument com nós e relacionamentos.

    Returns:
        pyvis.network.Network: O objeto de rede visualizada.
    """
    # Cria a rede
    net = Network(
        height="1200px", 
        width="100%", 
        directed=True,
        notebook=False, 
        bgcolor="#222222", 
        font_color="white", 
        filter_menu=True, 
        cdn_resources='remote'
    ) 

    nodes = graph_documents[0].nodes
    relationships = graph_documents[0].relationships

    # Constrói lookup para nós válidos
    node_dict = {node.id: node for node in nodes}
    
    # Filtra arestas inválidas e coleta IDs de nós válidos
    valid_edges = []
    valid_node_ids = set()
    for rel in relationships:
        if rel.source.id in node_dict and rel.target.id in node_dict:
            valid_edges.append(rel)
            valid_node_ids.update([rel.source.id, rel.target.id])

    # Rastreia quais nós fazem parte de qualquer relacionamento
    connected_node_ids = set()
    for rel in relationships:
        connected_node_ids.add(rel.source.id)
        connected_node_ids.add(rel.target.id)

    # Adiciona nós válidos ao grafo
    for node_id in valid_node_ids:
        node = node_dict[node_id]
        try:
            net.add_node(node.id, label=node.id, title=node.type, group=node.type)
        except:
            continue  # Pula o nó se ocorrer erro

    # Adiciona arestas válidas ao grafo
    for rel in valid_edges:
        try:
            net.add_edge(rel.source.id, rel.target.id, label=rel.type.lower())
        except:
            continue  # Pula a aresta se ocorrer erro

    # Configura layout e física do grafo
    net.set_options("""
        {
            "physics": {
                "forceAtlas2Based": {
                    "gravitationalConstant": -100,
                    "centralGravity": 0.01,
                    "springLength": 200,
                    "springConstant": 0.08
                },
                "minVelocity": 0.75,
                "solver": "forceAtlas2Based"
            }
        }
    """)

    output_file = "knowledge_graph.html"
    try:
        net.save_graph(output_file)
        print(f"Grafo salvo em {os.path.abspath(output_file)}")
        return net
    except Exception as e:
        print(f"Erro ao salvar grafo: {e}")
        return None


def generate_knowledge_graph(text):
    """
    Gera e visualiza um grafo de conhecimento a partir do texto de entrada.

    Esta função executa a extração do grafo de forma assíncrona e depois visualiza
    o grafo resultante usando PyVis.

    Args:
        text (str): Texto de entrada para converter em grafo de conhecimento.

    Returns:
        pyvis.network.Network: O objeto de rede visualizada.
    """
    graph_documents = asyncio.run(extract_graph_data(text))
    net = visualize_graph(graph_documents)
    return net