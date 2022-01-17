'''
The new algorithm developed by Li Ka Lok for computing modular multiplicative inverses and show
the computation from step to step using networkx directed graphs
'''
## import the required library
import sys
import networkx as nx
import matplotlib.pyplot as plt

## The inversing algorithm a*a^-1 = b*(-b)^-1(mod a) + 1
def inverse(a, b, g, h):
    '''
    Compute the modular inverse of a mod b
    '''
    ## show the procedure in a graph
    g.add_node(a)
    h.add_node(b)
    x = [n for n in g.nodes if g.out_degree(n) == 0]
    y = [n for n in h.nodes if h.out_degree(n) == 0]
    if x[0] != a: g.add_edge(x[0], a)
    if y[0] != b: h.add_edge(y[0], b)
    ## actually computing the function
    return (b*(a-inverse(b%a, a, g, h))+1)/a if a%b != 1 else 1

## driver code
g = nx.DiGraph()
h = nx.DiGraph()
a = int(input("input value a:"))
b = int(input("input value b:"))
print(f"The modular multiplcative inverse of a mod b is {inverse(a, b, g, h)}")
posg = nx.kamada_kawai_layout(g)
posh = nx.kamada_kawai_layout(h)
plt.figure(f"values of a")
nx.draw(g, posg, with_labels = True, edge_color = "black", node_color = "red")
plt.figure(f"values of b")
nx.draw(h, posh, with_labels = True, edge_color = "black", node_color = "red")
plt.show()
