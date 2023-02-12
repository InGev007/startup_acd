import csv
import networkx as nx
import matplotlib.pyplot as plt


# First task
city_list = []
with open('cities.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        city_list.append(row)

G = nx.Graph()
for edge in city_list:
    G.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.title("Cities Graph Generation")
plt.show()


# Second task
def graph_short_path(graph, city_1, city_2):
    short_path = nx.shortest_path(graph, city_1, city_2, "weight")
    path_length = nx.shortest_path_length(graph, city_1, city_2, "weight")
    return short_path, path_length


path, length = graph_short_path(G, 'Zmiiv', 'Zhdanivka')
print(f"Самый короткий маршрут:{path}. Растояние по нему:{length}")