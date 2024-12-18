import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu
from geopy.geocoders import Nominatim
import LocationCordonnate as LC


class ShortestPathApp:
    def __init__(self, master):
        self.master = master
        master.title("Shortest Path Finder")

        # Define locations_dict before using it in __init__
        self.locations_dict = LC.loca()
        self.label_start = Label(master, text="Point de départ:")
        self.label_start.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.start_location_var = StringVar()
        self.entry_start = OptionMenu(master, self.start_location_var, *self.get_predefined_places())
        self.entry_start.grid(row=0, column=1, columnspan=2, pady=5)

        self.label_end = Label(master, text="Point d'arrivée:")
        self.label_end.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.end_location_var = StringVar()
        self.entry_end = OptionMenu(master, self.end_location_var, *self.get_predefined_places())
        self.entry_end.grid(row=1, column=1, columnspan=2, pady=5)

        self.button_find_path = Button(master, text="Trouver le chemin le plus court", command=self.find_shortest_path)
        self.button_find_path.grid(row=2, column=0, columnspan=3, pady=10)

    def find_shortest_path(self):
        start_location = self.start_location_var.get()
        end_location = self.end_location_var.get()

        start_coordinates = self.locations_dict.get(start_location)
        end_coordinates = self.locations_dict.get(end_location)

        if start_coordinates is not None and end_coordinates is not None:
            graph = ox.graph_from_place("Fes, Morocco", network_type='all')

            start_node = ox.distance.nearest_nodes(graph, start_coordinates[1], start_coordinates[0])
            end_node = ox.distance.nearest_nodes(graph, end_coordinates[1], end_coordinates[0])

            heuristic = lambda u, v: ox.distance.euclidean_dist_vec(graph.nodes[u]['y'], graph.nodes[u]['x'],
                                                                    graph.nodes[v]['y'], graph.nodes[v]['x'])
            shortest_path = nx.astar_path(graph, start_node, end_node, heuristic=heuristic, weight='length')

            fig, ax = ox.plot_graph_route(graph, shortest_path, node_size=0, show=False, close=False)
            ax.scatter(start_coordinates[1], start_coordinates[0], c='green', marker='o', s=100, label='Start')
            ax.scatter(end_coordinates[1], end_coordinates[0], c='red', marker='o', s=100, label='End')
            plt.legend()
            plt.show()

    def get_predefined_places(self):
        return list(self.locations_dict.keys())


if __name__ == "__main__":
    root = Tk()
    app = ShortestPathApp(root)
    root.mainloop()
