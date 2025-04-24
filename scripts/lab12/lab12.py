import dynetx as dn
import networkx as nx

def read_net(filename):
    g = nx.Graph()
    with open(filename) as f:
        f.readline()  # skip header
        for line in f:
            i = line.strip().split(",")
            if len(i) < 2:
                continue
            g.add_edge(i[0], i[1])
    return g

g = dn.DynGraph()

# Add time-aware edges
for t in range(1, 9):
    er = read_net('/content/asoiaf-book1-edges.csv')
    g.add_interactions_from([(u, v, t) for u, v in er.edges()])

# Snapshots
print("Time snapshots:", g.temporal_snapshots_ids())

# Graph at time 1
g1 = g.time_slice(1)
print("Nodes at t=1:", g1.number_of_nodes())
print("Edges at t=1:", g1.number_of_edges())

# Flattened version
g1_flat = nx.Graph(g1.edges())
print("Flattened graph has", g1_flat.number_of_edges(), "edges")

# Inter-event time distributions
print("All edge event times:", g.inter_event_time_distribution())
print("All edge event times (mean):", g.inter_event_time_distribution("M"))

# For a specific node pair
u = 'Eddard-Stark'
v = 'Catelyn-Stark'
if (u, v) in g.edges():
    print(f"Event times for ({u}, {v}):", g.inter_event_time_distribution(u, v))
else:
    print(f"No edge between {u} and {v} found.")

# Degree at time 3
print("Degree of Eddard-Stark at t=3:", g.degree(t=3).get('Eddard-Stark', 0))

# Coverageimport dynetx as dn
import networkx as nx
import random

def read_net(filename):
    g = nx.Graph()
    with open(filename) as f:
        f.readline()
        for line in f:
            i = line.split(",")
            g.add_edge(line[0], line[1])
    return g

g = dn.DynGraph()

for t in range(1,9):
  er = read_net(f'/content/asoiaf-book1-edges.csv')
  g.add_interactions_from(er.edges, t=t)

g.temporal_snapshots_ids()

g1 = g.time_slice(1)
g1.number_of_nodes()
g1.number_of_edges()

g1_flat = nx.Graph(g1.edges())

r = g.inter_event_time_distribution()
print(f"Number interactions: temporal distance\t{r}")

r = g.inter_event_time_distribution("M")
print(f"Number interactions: temporal distance\t{r}")

print(list(g.edges()))

u = 'A'
v = 'd'

r = g.inter_event_time_distribution(u, v)
print(f"Number interactions: temporal distance\t{r}")

g.degree(t=3)['A'] # degree of node 0 at time t=2

g.coverage()
print("Temporal coverage:", g.coverage())
