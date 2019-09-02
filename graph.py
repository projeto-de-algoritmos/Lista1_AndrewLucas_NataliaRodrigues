import pandas as pd
import numpy as np
import queue
import networkx as nx
import matplotlib.pyplot as plt


class Graph():
    graph = {}

    def __init__(self):
        network = pd.read_csv('network.csv')
        for username in network['username']:
            self.graph[username] = []
        self.graph.update(network.groupby(['followed_by'])[
                          'username'].apply(list))

    def plotGraph(self):
        # Plot a graph of all edges
        edges = []
        for key in self.graph.keys():
            for value in self.graph[key]:
                edges.append((key, value))
        print('ploting...')
        G = nx.DiGraph(directed=True)
        G.add_edges_from(edges)
        options = {
            'node_color': 'red',
            'node_size': 50,
            'width': 0.1,
            'arrowstyle': '-|>',
            'arrowsize': 10,
            'font_color': 'yellow',
            'font_size': 10
        }
        f = plt.figure(figsize=(100, 100))
        nx.draw_networkx(G, arrows=True, **options)
        f.savefig("grafo.png")

    def distance(self, u, v):
        # Given two usernames, return the number of edges between them.
        visited = {}
        distance = {}

        Q = queue.Queue()
        distance[u] = 0

        Q.put(u)
        visited[u] = True
        while (not Q.empty()):
            x = Q.get()

            for i in range(len(self.graph[x])):
                if (self.graph[x][i] in visited.keys()):
                    continue

                distance[self.graph[x][i]] = distance[x] + 1
                Q.put(self.graph[x][i])
                visited[self.graph[x][i]] = True

        return distance[v] if v in distance.keys() else 'Não há caminho'
