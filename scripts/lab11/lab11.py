import linkpred
import matplotlib.pyplot as plt
import networkx as nx 

def read_net_w(filename):
    g = nx.Graph()
    with open(filename) as f:
        f.readline()  # skip header
        for line in f:
            i = line.strip().split(",")
            if len(i) < 4:
                continue
            g.add_edge(i[0], i[1], weight=int(i[3]))
    return g

g = read_net_w('/content/asoiaf-book1-edges.csv')

# Common Neighbours
cn = linkpred.predictors.CommonNeighbours(g, excluded=g.edges())
cn_results = cn.predict()
print("Top Common Neighbours:")
for edge, score in cn_results.top(5).items():
    print(edge, score)

# Adamic Adar
aa = linkpred.predictors.AdamicAdar(g, excluded=g.edges())
aa_results = aa.predict()
print("\nTop Adamic Adar:")
for edge, score in aa_results.top(5).items():
    print(edge, score)

# Katz
kz = linkpred.predictors.Katz(g, excluded=g.edges())
kz_results = kz.predict()
print("\nTop Katz:")
for edge, score in kz_results.top(5).items():
    print(edge, score)

# Graph Distance
gd = linkpred.predictors.GraphDistance(g, excluded=g.edges())
gd_results = gd.predict()
print("\nTop Graph Distance:")
for edge, score in gd_results.top(5).items():
    print(edge, score)
