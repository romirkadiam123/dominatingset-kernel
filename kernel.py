import networkx as nx

def apply_R1(G):
    changed = True
    while changed:
        changed = False
        for v in list(G.nodes()):
            if G.degree(v) == 0:
                G.remove_node(v)
                changed = True
    return G

def apply_R2(G):
    nodes = list(G.nodes())
    to_remove = set()

    closed_neigh = {v: set(G.neighbors(v)) | {v} for v in nodes}

    for i, u in enumerate(nodes):
        for v in nodes[i+1:]:
            if u in to_remove or v in to_remove:
                continue
            if closed_neigh[u] <= closed_neigh[v]:
                to_remove.add(u)
            elif closed_neigh[v] <= closed_neigh[u]:
                to_remove.add(v)

    G.remove_nodes_from(to_remove)
    return G

def apply_R4(G):
    closed_neigh = {}
    reps = {}

    for v in G.nodes():
        key = frozenset(G.neighbors(v)) | {v}
        if key not in reps:
            reps[key] = v
        else:
            closed_neigh[v] = reps[key]

    G.remove_nodes_from(closed_neigh.keys())
    return G

def kernelize(G):
    changed = True
    passes = 0
    while changed:
        before = G.number_of_nodes()
        G = apply_R1(G)
        G = apply_R2(G)
        G = apply_R4(G)
        after = G.number_of_nodes()
        changed = (before != after)
        passes += 1
    return G, passes
