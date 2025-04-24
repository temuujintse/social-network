import networkx as nx
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

def read_net_w(filename):
    g = nx.Graph()
    with open(filename) as f:
        f.readline()  # Skip header
        for l in f:
            l = l.strip().split(",")
            g.add_edge(l[0], l[1])
    return g

def node_overlap(g):
    for u, v in g.edges():
        n_u = set(g.neighbors(u))
        n_v = set(g.neighbors(v))
        union = n_u | n_v
        if len(union) > 0:
            overlap = len(n_u & n_v) / len(union)
        else:
            overlap = 0
        g[u][v]['overlap'] = overlap
        g[u][v]['weight'] = overlap
    return g

g = read_net_w('/content/asoiaf-book1-edges.csv')
g = node_overlap(g)

# KDE plot of overlap
weights = [d['overlap'] for _, _, d in g.edges(data=True)]
pd.DataFrame(weights)[0].plot.kde()
plt.xlabel("Neighborhood Overlap")
plt.xlim(0, 1)
plt.title("Overlap Distribution")
plt.show()

# KDE plot of weights
weights_got = [d['weight'] for _, _, d in g.edges(data=True)]
pd.DataFrame(weights_got)[0].plot.kde()
plt.xlabel("Interaction Weights")
plt.xlim(0, 1)
plt.title("Weight Distribution")
plt.show()
