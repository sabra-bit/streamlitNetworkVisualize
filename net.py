import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network

st.write("generation of visual network graphs  ")
    # Create networkx graph object from pandas dataframe
G =  nx.MultiGraph()


G.add_edge('Egypt',"cairo")
G.add_edge('Egypt',"giza")
G.add_edge('Egypt',"alex")
G.add_node('alex', size=10, title='chile',color='green',)
            
G.add_node('Egypt', size=20, title='head',color='red',)

# pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
# nx.draw(G,pos=pos,with_labels=True,node_size=1000)

    # Initiate PyVis network object
drug_net = Network(height='665px', width='665px',directed=True, bgcolor='#222222', font_color='white')

    # Take Networkx graph and translate it to a PyVis graph format
drug_net.from_nx(G)

    # Generate network with specific layout settings
drug_net.repulsion(node_distance=420, central_gravity=1.33,spring_length=110, spring_strength=1.70,damping=3.95,)
drug_net.show_buttons(filter_=['physics'])


    # Save and read graph as HTML file (on Streamlit Sharing)
try:
        path = 'img'
        drug_net.save_graph(f'{path}\\pyvis_graph.html')
        HtmlFile = open(f'{path}\\pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
except:
        path = 'html_files'
        drug_net.save_graph(f'{path}\\pyvis_graph.html')
        HtmlFile = open(f'{path}\\pyvis_graph.html', 'r', encoding='utf-8')

components.html(HtmlFile.read(), height=835 ,width=835,scrolling=True)
