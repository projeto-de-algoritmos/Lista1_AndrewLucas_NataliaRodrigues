import pandas as pd
import numpy as np
import queue
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from random import randint


class Graph():
    graph = {}

    def __init__(self):
        network = pd.read_csv('network.csv')
        for username in network['username']:
            self.graph[username] = []
        self.graph.update(network.groupby(['followed_by'])[
                          'username'].apply(list))

    def getVertices(self):
        return list(self.graph.keys())

    def DFS(self): 
        vertices = self.getVertices()
        visited = {}
        stack = []

        for s in vertices:
            stack.append(s)  

            while (len(stack)):  
                s = stack[-1]  
                stack.pop() 
    
                if (s not in visited.keys()):  
                    print(s, end='\t') 
                    visited[s] = True 
    
                for node in self.graph[s]:  
                    if (node not in visited.keys()):  
                        stack.append(node) 

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