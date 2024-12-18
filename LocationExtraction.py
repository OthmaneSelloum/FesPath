import osmnx as ox
import networkx as nx

place_name = "Fes, Morocco"
graph1 = ox.graph_from_place(place_name, network_type='all')

# Itérez sur les nœuds du graphe et imprimez les coordonnées de chaque point
def matrice_adj(max_points_to_print = 100,points_printed = 0,M=[],graph=graph1):
    for node, data in graph.nodes(data=True):
        if points_printed < max_points_to_print:
            M.append((data['y'],data['x']))
            points_printed += 1
        else:
            break
    return M
