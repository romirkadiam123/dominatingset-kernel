import networkx as nx
import random

def erdos_renyi_sparse(n, c):
    p = c / n
    return nx.fast_gnp_random_graph(n, p, seed=random.randint(0,10**9))

def random_regular(n, d):
    return nx.random_regular_graph(d, n)

def planar_grid(n):
    k = int(n**0.5)
    return nx.grid_2d_graph(k, k)
