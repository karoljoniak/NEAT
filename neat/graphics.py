import networkx as nx
import matplotlib.pyplot as plt


def show_ann_as_graph(nodes, connections):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(connections)
    print(connections)

    options = {
        'node_color': 'yellow',
        'node_size': 100,
        'width': 3,
        'arrowstyle': '-|>',
        'arrowsize': 12,
    }

    nx.draw_networkx(g, arrows=True, **options)
    #plt.savefig("simple_path.png")  # save as png
    plt.show()  # display
