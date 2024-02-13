import pandas as pd
from graphviz import Digraph

csv_paths = {
    'CIS2Concepts': 'CIS2Concepts.csv',
    'CIS2NIST': 'CIS2NIST.csv',
    'NIST2Concept': 'NIST2Concept.csv'
}

csv_dataframes = {}

for key, path in csv_paths.items():
    csv_dataframes[key] = pd.read_csv(path)

csv_structures = {key: df.head() for key, df in csv_dataframes.items()}
csv_structures

def generate_edges(data, source_col, target_col):
    edges = []
    for _, row in data.iterrows():
        source = row[source_col]
        target = row[target_col]
        edges.append((source, target))
    return edges

edges_CIS2Concepts = generate_edges(csv_dataframes['CIS2Concepts'], 'CIS Control', 'Concept')
edges_CIS2NIST = generate_edges(csv_dataframes['CIS2NIST'], 'CIS Control', 'NIST CSF Function')
edges_NIST2Concept = generate_edges(csv_dataframes['NIST2Concept'], 'NIST CSF Function', 'Concept')
combined_edges = edges_CIS2Concepts + edges_CIS2NIST + edges_NIST2Concept

dot = Digraph(comment='Cyber Security Concepts Mapping', format='png')
dot.attr('node', shape='box', style='filled')

for i, edge in enumerate(combined_edges):
    dot.node(edge[0], color='lightblue2')
    dot.node(edge[1], color='lightgrey')
    dot.edge(edge[0], edge[1], color=f'#{i % 6 + 1}66666')

output_graph_path = 'CyberSec_Concepts_Mapping'
dot.render(output_graph_path)
