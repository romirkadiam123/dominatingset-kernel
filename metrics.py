def dominance_core_ratio(n_before, n_after):
    return n_after / n_before

def neighborhood_inclusion_density(G):
    nodes = list(G.nodes())
    n = len(nodes)
    if n <= 1:
        return 0.0

    closed = {v: set(G.neighbors(v)) | {v} for v in nodes}
    count = 0

    for i, u in enumerate(nodes):
        for v in nodes[i+1:]:
            if closed[u] < closed[v] or closed[v] < closed[u]:
                count += 1

    return count / (n * (n - 1))
