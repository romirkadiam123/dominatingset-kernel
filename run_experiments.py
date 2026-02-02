import csv, time
import networkx as nx

from kernel import kernelize
from metrics import dominance_core_ratio, neighborhood_inclusion_density
from generators import erdos_renyi_sparse, planar_grid, random_regular

def run():
    outpath = "results/data.csv"
    with open(outpath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "family", "trial", "n", "edges",
            "passes", "kernel_n", "DCR", "NID", "time_sec"
        ])

        settings = [
            ("ER_c2", lambda: erdos_renyi_sparse(800, 2)),
            ("ER_c4", lambda: erdos_renyi_sparse(800, 4)),
            ("ER_c8", lambda: erdos_renyi_sparse(800, 8)),
            ("Grid",  lambda: planar_grid(900)),
            ("Reg3",  lambda: random_regular(900, 3)),
            ("Reg4",  lambda: random_regular(900, 4)),
        ]

        trials = 20

        for family, gen in settings:
            for t in range(trials):
                G0 = gen()
                # Copy for kernelization so metrics use original graph
                G_for_kernel = G0.copy()

                n0 = G0.number_of_nodes()
                e0 = G0.number_of_edges()

                nid = neighborhood_inclusion_density(G0)

                start = time.time()
                Gk, passes = kernelize(G_for_kernel)
                elapsed = time.time() - start

                nk = Gk.number_of_nodes()
                dcr = dominance_core_ratio(n0, nk)

                writer.writerow([
                    family, t, n0, e0,
                    passes, nk, dcr, nid, elapsed
                ])

    print(f"Wrote {outpath}")

if __name__ == "__main__":
    run()
