import networkx as nx
import matplotlib.pyplot as plt

def findCenter(edges):
    if edges[0][0] in edges[1]:
        return edges[0][0]
    return edges[0][1]


def visualize_star_graph(edges, center):
    G = nx.Graph()
    for edge in edges:
        G.add_edge(*edge)
    
    pos = nx.shell_layout(G)
    
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue")
    nx.draw_networkx_nodes(G, pos, nodelist=[center], node_color='lightgreen')
    
    plt.title("Star Graph Visualization")
    plt.show()

edges1 = [[1,2],[2,3],[4,2]]
edges2 = [[1,2],[5,1],[1,3],[1,4]]

center1 = findCenter(edges1)
center2 = findCenter(edges2)

print("Center of Graph 1:", center1)
visualize_star_graph(edges1, center1)

print("Center of Graph 2:", center2)
visualize_star_graph(edges2, center2)
